import cv2
import numpy as np

from src.speed_estimation import SpeedEstimation

class CarClassifier:
    '''
        This Class handles the Object detection. This is being done
        with the help of Yolov3.

        After all cars are detected we call the SpeedEstimation class and
        in particular the SpeedEstimation.find_speed_color() in order to
        estimate the car's speed.

        -This class has also the function of drawing the route of each and every
        car with the help of the SpeedEstimation class.-
    '''
    def __init__(self, route):
        self.network = cv2.dnn.readNet("yolo_versions/yolov3.weights", "yolo_versions/yolov3.cfg")
        self.output_layers = [self.network.getLayerNames()[i[0] - 1] for i in self.network.getUnconnectedOutLayers()]

        self.speed_estimation = SpeedEstimation()
        self.route = route

    def yolo_calculation(self, frame):
        # Detecting objects
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        self.network.setInput(blob)
        outs = self.network.forward(self.output_layers)
        height, width, channels = frame.shape
        
        # Showing informations on the screen
        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.2:
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    x = int(int(detection[0] * width) - w / 2)
                    y = int(int(detection[1] * height) - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        return self.draw_contours(frame, boxes, confidences)

    def draw_contours(self, frame, boxes, confidences):
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        
        colors = self.speed_estimation.find_speed_color(indexes, boxes)
        count = 0
        for i in range(len(boxes)):
            if i in indexes:
                # Draw a small line for tracking
                if(self.route == 1):
                    if(self.speed_estimation.tracking_history):
                        for j in self.speed_estimation.tracking_history:
                            for k in j:
                                x, y, w, h = k
                                cv2.circle(frame, (x+int(w/2), y+int(h/2)), 2, (0, 255, 0), 3)

                x, y, w, h = boxes[i]
                if(colors):
                   cv2.circle(frame, (x+int(w/2), y+int(h/2)), 3, colors[count], 2)
                   count += 1
        return frame


import cv2
import numpy as np

import time
import glob

from src.car_detection import CarClassifier

FONT = cv2.FONT_HERSHEY_PLAIN

class VideoRecording:
    '''
        This class' functions are:
            - It is getting the preferred input of data and it
            starts to process it. After the data is converted into 
            bits it calls the CarClassifier class and in particular the
            CarClassifier.yolo_calculation() function.

            After the yolo_calculation function it displays the new frame
            that is being returned.

            - It calculates the frames per second (fps) of the video
            it displays.

            - It can save the newly recorded video.

        All of the rest are being sorted in the yolo_calculation()
        function.  
    '''

    def __init__(self, live, save_file, route):
        self.live = live
        self.save_file = save_file

        self.samples = glob.glob("./samples/*.mp4")
        self.classification = CarClassifier(route)
        
        self.starting_time = time.time()
        self.frame_id = 0

    def start_measuring(self):
        if(self.live == 0):
            if(self.samples):
                self.sampled_data()
            else:
                print("There are no '*.mp4' Videos inside the samples folder!")
        else:
            self.realtime_speed()
        
    def realtime_speed(self):
        cap = cv2.VideoCapture(0)
        while(True):
            _, frame = cap.read()
            self.frame_id += 1

            frame = self.classification.yolo_calculation(frame)

            elapsed_time = time.time() - self.starting_time
            fps = self.frame_id / elapsed_time
            cv2.putText(frame, "FPS: " + str(round(fps, 2)), (10, 30), FONT, 2, (0, 0, 0), 2)

            cv2.imshow('Highway', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


    def sampled_data(self):
        # Iterate throw all the samples
        for sample in self.samples:
            cap = cv2.VideoCapture(sample)

            # Recording the data
            if(self.save_file):
                _, frame = cap.read()
                fourcc = cv2.VideoWriter_fourcc(*'XVID')
                output = cv2.VideoWriter(sample[10:], fourcc, 20.0, (frame.shape[1], frame.shape[0]))

            while (cap.isOpened()):
                ret, frame = cap.read()
                self.frame_id += 1

                if ret == True:
                    frame = self.classification.yolo_calculation(frame)
                    elapsed_time = time.time() - self.starting_time
                    fps = self.frame_id / elapsed_time
                    cv2.putText(frame, "FPS: " + str(round(fps, 2)), (10, 30), FONT, 2, (0, 0, 0), 2)

                    if(self.save_file):
                        output.write(frame)
                    cv2.imshow('Highway', frame)
                    if cv2.waitKey(25) & 0xFF == ord('q'):
                        break
                else:
                    break
        cap.release()
        cv2.destroyAllWindows()
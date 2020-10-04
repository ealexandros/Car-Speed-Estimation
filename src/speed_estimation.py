import math

class SpeedEstimation:
    '''
        This Class does the speed estimation by calculation the distance
        between the current frame and the next one.

        - It uses the euclidean distance for that calculation.
        - It also stores the tracking history of every car for the
        last 1-2 seconds.
    '''
    def __init__(self):
        self.short_memory = []
        self.tracking_history = []

    def remove_car_noise(self, boxes, indexes):
        current_location = []
        for i in range(len(boxes)):
            if(i in indexes):
                current_location.append(boxes[i])

        self.tracking_history.append(current_location)
        if(len(self.tracking_history) > 10):
            del self.tracking_history[0]
        return current_location

    def find_minumum_distance(self, current_location):
        speeds = []
        if(current_location and self.short_memory):
            for i in current_location:
                min_distance = 100000000
                for j in self.short_memory:
                    dist = math.sqrt((i[1]+int(i[3]/2) - j[1]+int(j[3]/2))**2 + (i[0]+int(i[2]/2) - j[0]+int(j[2]/2))**2)
                    if(dist < min_distance):
                        min_distance = dist
                speeds.append(min_distance)

        self.short_memory = current_location
        return speeds
        

    def find_speed_color(self, indexes, boxes):
        colors = []

        current_location = self.remove_car_noise(boxes, indexes)
        speeds = self.find_minumum_distance(current_location)
        
        # print(max(speeds)) # debug
        for i in speeds:
            if(i > 255):
                colors.append((0, 0, 0))
            else:
                colors.append((0, 0+i*8, 255-i*8))
        return colors
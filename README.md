# Car Speed Estimation - Route

*This is still a work in Progress.*

### Goal Of the Project

The main goal of the **Project** is to have a camera placed wherever you want and find the car with the highest speed.

All the cars will be sorted in a decreased order. An indicator on top of them will show the relative speed. 

The indicator be a small dot in the middle of the car. From `red`, which will be the highest to `green` that will be the slowest of them.

**- Without knowing the distance of the camera placement.**

## ToDo-List

- All the things that I have done:

 1. Find the Cars from an image.
 2. Save the new Video. `(with the speeds)`
 3. Find the distance it traveled.
 4. Draw the route of the car.


- All the things that need to be done:

 1. Optimize the distance it traveled

## Description

At this state of the Project you can see the different level of speed of every car. You can also have some different settings. Those are:

1. In particular you can have a prerecorded video or you can test it real-time.
2. You can draw the path of each car.
3. You can save the edited video on the same folder.

*As I previously mentioned `This project is still in Progress`. There will be more functions in the future*.

## Technologies Used

In this project I used the following technologies:

- `Yolov3`, in order to find all the cars.
- `OpenCv, Numpy`, this helps with the connection of *Yolov3*.
- `Glob, Math`, those are some predownloaded libs in python.

## Conclusion

This is one my first ever `yolo` Project. If you are looking for object detection, this is the right fit!

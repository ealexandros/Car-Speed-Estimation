from src.video_input import VideoRecording

#----- Small Configurations -----#
#
#   If you want to test it set all the values to 0.
#   After that place your already recorded video.
#   Run the code and see the result.

SHOW_ROUTE = 0  # If you want to see the route of each car change the Value to '1'.
REALTIME = 0    # If you want to test it in realtime change the Value to '1'.
SAVE_FILE = 0   # If you want to save the changed Video change the Value to '1'.

if("__main__" == __name__):
    model = VideoRecording(REALTIME, SAVE_FILE, SHOW_ROUTE)
    model.start_measuring()
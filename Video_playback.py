"""
3. Video processing
    3.1. Video playback
    This script has functions of play/pause/playback.

    step 1: Input configurable arguments
            It is capable of using IDE (1.1) and command line(1.2)
    step 2: Play videos
"""


# importing libraries
import sys  # command line arg inputs
import cv2  # openCV


def video_playback(video_file_path, fps=None, display_resolution=None, monochrome=False):
    """
    :param video_file_path: str
    :param fps: int -> frame/second
    :param display_resolution: [int, int] -> [width, height]
    :param monochrome: Boolean -> RBG or Gray
    :return: play processed video
    """

    # read video file
    cap = cv2.VideoCapture(video_file_path)

    # assure video file is open
    try:
        assert cap.isOpened() == True
    # print error message
    except AssertionError:
        print("Error opening file, please check the availability of the video source.")

    if fps:
        cap.set(cv2.CAP_PROP_FPS, fps)

    h, w = cap.get(cv2.CAP_PROP_FRAME_HEIGHT), cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    print('Original Frame Size: ', h, w)

    # initialise a list to store frames
    frame_list = []

    # Play video
    while cap.isOpened():
        # read frame by frame
        ret, frame = cap.read()
        frame_list.append(frame)
        if ret == True:

            # Process each frame by monochrome
            if monochrome:
                frame_list[-1] = cv2.cvtColor(frame_list[-1], cv2.COLOR_BGR2GRAY)

            # Process each frame by display_resolution
            if display_resolution != None:
                dim = (int(display_resolution[0]), int(display_resolution[1]))
                frame_list[-1] = cv2.resize(frame_list[-1], dim, interpolation=cv2.INTER_AREA)

            # Press b on keyboard to play back one frame, 'b' corresponds to key value = 98
            if cv2.waitKey(98) == ord('b'):
                # remove the newest frame, so that the second newest frame is back-played
                frame_list.pop(-1)
                cv2.imshow('Frame', frame_list[-1])
                print('Played back one frame.')
            else:
                # Display the newest frame
                cv2.imshow('Frame', frame_list[-1])

            # Press p on keyboard to Pause, 'p' corresponds to key value = 112
            if cv2.waitKey(112) == ord('p'):
                print('Press any keys to continue.')
                cv2.waitKey(0)

        else:
            break

    # Release the video capture object
    cap.release()
    # Closes all the frames
    cv2.destroyAllWindows()


# Helper function
def key_ref():
    """
    find the corresponding key code with input key
    :return: key code
    """

    cap = cv2.VideoCapture('video_2.mp4')  # load a dummy image
    while (1):
        ret, frame = cap.read()
        cv2.imshow('Frame', frame)
        k = cv2.waitKey(33)
        if k == 27:  # Esc key to stop
            break
        elif k == -1:  # normally -1 returned,so don't print it
            continue
        else:
            print(k)


if __name__ == '__main__':
    # 1.1 if run in IDE, uncomment below 4 lines
    video_file_path = 'video_2.mp4'
    fps = 30
    display_resolution = [200, 200]
    monochrome = True

    # 1.2 if run in the command line, uncomment below 4 lines
    # video_file_path = str(sys.argv[1])
    # fps = sys.argv[2]
    # display_resolution = sys.argv[3]
    # monochrome = sys.argv[4]

    # 2. execute main function
    video_playback(video_file_path, fps, display_resolution, monochrome)
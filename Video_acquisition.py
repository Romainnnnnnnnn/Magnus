#Script to acquire video from a camera and display it with a grid overlay
#Script to be used for calibrating the camera with the 8x8 chessboard grid

import cv2

cap = None  # Initialize the camera variable globally

def initialize_camera():
    global cap

    cap = cv2.VideoCapture(0) # Connects to webcam

    # Set width and height of the video feed
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1024)

def stop_camera():
    global cap

    # When everything done, release the capture and destroy the windows
    cap.release()
    cv2.destroyAllWindows()

def display_video_with_grid():
    global cap

    while True:
        ret, frame = cap.read() # Capture frame-by-frame
        frame_resized = frame[0:1024, 128:1152] # Crop the frame to the center 1024x1024 region

        # Draw an 8x8 grid
        for i in range(1, 8):
            cv2.line(frame_resized, (0, i * 128), (1024, i * 128), (255, 255, 255), 1)  # horizontal lines
            cv2.line(frame_resized, (i * 128, 0), (i * 128, 1024), (255, 255, 255), 1)  # vertical lines

        cv2.imshow('frame', frame_resized) # Display the resulting frame with the grid

        # This command lets us quit with the "q" button on a keyboard
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    initialize_camera()
    try:
        display_video_with_grid()
    finally:
        stop_camera()

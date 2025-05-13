#Script to acquire video from a camera and display it with a grid overlay
#Script to be used for calibrating the camera with the 8x8 chessboard grid

import cv2

# Connects to webcam
cap = cv2.VideoCapture(0)

# Automatically grab width and height from video feed
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1024)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Crop the frame to the center 1024x1024 region
    frame_resized = frame[0:1024, 128:1152]

    # Draw an 8x8 grid
    for i in range(1, 8):
        cv2.line(frame_resized, (0, i * 128), (1024, i * 128), (255, 255, 255), 1) # horizontal lines
        cv2.line(frame_resized, (i * 128, 0), (i * 128, 1024), (255, 255, 255), 1) # vertical lines
    
     # Display the resulting frame with the grid
    cv2.imshow('frame', frame_resized)
    
    # This command let's us quit with the "q" button on a keyboard.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture and destroy the windows
cap.release()
cv2.destroyAllWindows()

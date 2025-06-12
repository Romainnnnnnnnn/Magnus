#Script to acquire video from a camera and display it with a grid overlay
#Script to be used for calibrating the camera with the 8x8 chessboard grid

import cv2
from matplotlib import pyplot as plt
import numpy as np

cap = None  # Initialize the camera variable globally

def initialize_camera():
    global cap 

    cap = cv2.VideoCapture(2) # Connects to webcam

    # Set width and height of the video feed
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1024)

    # let time to adjust the camera
    for i in range(50):
        ret, frame = cap.read()

def acquire_grid_images():
    global cap

    ret, frame = cap.read() # Capture a frame
    frame_resized = frame[0:1024, 128:1152] # Crop the frame to the center 1024x1024 region

    # Draw an 8x8 grid
    for i in range(1, 8):
        cv2.line(frame_resized, (0, i * 128), (1024, i * 128), (255, 255, 255), 1)  # horizontal lines
        cv2.line(frame_resized, (i * 128, 0), (i * 128, 1024), (255, 255, 255), 1)  # vertical lines

    # Cut the frame into 64 squares of 128x128
    squares = []
    for row in range(8):
        for col in range(8):
            square = frame_resized[row * 128:(row + 1) * 128, col * 128:(col + 1) * 128]
            square = cv2.rotate(square, cv2.ROTATE_180)
            squares.append(square)

    # Convert the list of squares to a numpy array
    np_squares = np.stack(squares, axis=0)
    #print("Size of the numpy array:", np_squares.shape)

    """
    # Display the squares
    fig, axes = plt.subplots(8, 8, figsize=(10, 10))
    for idx, ax in enumerate(axes.flat):
        ax.imshow(cv2.cvtColor(squares[idx], cv2.COLOR_BGR2RGB))
        ax.axis('off')  # Turn off axis
    plt.tight_layout()
    plt.show()
    """
    # Save each square as an image, used for the creation of the dataset
    #for idx, square in enumerate(squares, start = 64):
    #    filename = f"square_{idx:02d}.png"
    #    cv2.imwrite(filename, square)
        
    return np_squares

def stop_camera():
    global cap

    # When everything done, release the capture and destroy the windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    initialize_camera()
    acquire_grid_images()
    stop_camera()
    

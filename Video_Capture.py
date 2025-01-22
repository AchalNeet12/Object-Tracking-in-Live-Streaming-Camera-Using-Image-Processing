import cv2
from tracker import *  # Ensure tracker.py is correctly importing zip_longest

# Initialize video capture from the provided file
cap = cv2.VideoCapture(r"highway.mp4")

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("End of video or error reading frame.")
        break
    
    cv2.imshow('Frame', frame)  # Display the current frame
    
    # Break the loop when 'Esc' key is pressed
    key = cv2.waitKey(30)
    if key == 27:  # 27 is the ASCII code for the 'Esc' key
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

import cv2
import numpy as np
import pickle
from src.utils import Park_classifier


def demostration():
    rect_width, rect_height = 107, 48
    carp_park_positions_path = "data/source/CarParkPos"
    video_path = "data/source/carPark.mp4"
    classifier = Park_classifier(carp_park_positions_path, rect_width, rect_height)
    cap = cv2.VideoCapture(video_path)
    while True:
        ret, frame = cap.read()
        if not ret:break
        prosessed_frame = classifier.implement_process(frame) 
        denoted_image = classifier.classify(image=frame, prosessed_image = prosessed_frame)
        cv2.imshow("Car Park Image which drawn According to  empty or occupied", denoted_image)
        k = cv2.waitKey(1)
        if k & 0xFF == ord('q'):
            break
        
        if k & 0xFF == ord('s'):
            cv2.imwrite("output.jpg", denoted_image)
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    demostration()

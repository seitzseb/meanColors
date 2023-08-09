import numpy as np
import cv2

ZOOM = 0.25

vid = cv2.VideoCapture("video.mp4")

while vid.isOpened():
    ret, frame = vid.read()
    if ret:
        newsize = [int(x*ZOOM) for x in frame.shape[:2]]
        newsize = [newsize[1],newsize[0]]
        frame = cv2.resize(frame,newsize)
        print(frame.shape)
        for i in range(frame.shape[0]):
            frame[i,:,:] = np.mean(frame,axis = 0)
        cv2.imshow("frame",frame)
        if cv2.waitKey(25) & 0xFF == ord("q"):
            break

    else:
        break

vid.release()
cv2.destroyAllWindows()
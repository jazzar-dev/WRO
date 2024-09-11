import cv2
from PIL import Image

from util import get_limits


yellow = [0, 255, 255]  # yellow in BGR colorspace
colors = [(0, 255, 255)]
colors = [get_limits(i) for i in colors]
colors = [(i[0].tolist(), i[1].tolist()) for i in colors]


cap = cv2.VideoCapture(2)
while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for color in colors:
        # lowerLimit, upperLimit = get_limits(color=yellow)
        lowerLimit, upperLimit = color[0], color[1]
        mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
        
        mask_ = Image.fromarray(mask)

        bbox = mask_.getbbox()

        if bbox is not None:
            x1, y1, x2, y2 = bbox

            frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
            frame = cv2.circle(frame, (((x2-x1)/2), y1), 1, (255, 0, 0), -1)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()


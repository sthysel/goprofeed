import cv2 as cv

cap = cv.VideoCapture('udp://127.0.0.1:10000', cv.CAP_FFMPEG)
if not cap.isOpened():
    print('VideoCapture not opened')
    exit(-1)

cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.resizeWindow('image', 1920, 1080)

while True:
    ret, frame = cap.read()

    if not ret:
        print('frame empty')
        break

    cv.imshow('image', frame)

    if cv.waitKey(1) & 0XFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

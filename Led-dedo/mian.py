import cv2
from cvzone.HandTrackingModule import HandDetector
from pyfirmata import Arduino

video = cv2.VideoCapture(0)  # Use camera index 0
detector = HandDetector(detectionCon=0.7)
board = Arduino('COM1')

led1 = board.get_pin('d:7:o')
led2 = board.get_pin('d:8:o')
led3 = board.get_pin('d:9:o')
led4 = board.get_pin('d:10:o')


while True:
    ret, img = video.read()

    if not ret:
        print("Error: Could not read frame from the camera.")
        break

    hands, img = detector.findHands(img)

    if hands:
        fingers = detector.fingersUp(hands[0])
        led1.write(1)
        led2.write(2)
        led3.write(3)
        led4.write(4)

    led1.write(0)
    led2.write(0)
    led3.write(0)
    led4.write(0)

    cv2.imshow('IMG', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

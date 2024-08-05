#!/home/user/venv/bin/python
import cv2
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

Button3 = 26
GPIO.setup(Button3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280);
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720);
cap.set(cv2.CAP_PROP_FPS, 30);

while(cap.isOpened()):
    ret, frame = cap.read()
    #print(frame.shape)
    #cv2.imshow('Webcam', frame)

    if GPIO.input(Button3): # if button press, then take a shot
        cv2.imwrite("snapshot.jpg", frame)

    #if cv2.waitKey(10) & 0xFF == ord('q'):
    #    break
cap.release()
cv2.destroyAllWindows()

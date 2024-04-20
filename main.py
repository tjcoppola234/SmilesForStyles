'''
Emotion...
Helpful video: https://www.youtube.com/watch?v=fkgpvkqcoJc. It uses Deepface for emotion, race, and age image recognition. Also works in real-time

Clothing...
Clothing dataset: https://github.com/switchablenorms/DeepFashion2
Finding similar clothes: https://github.com/axinc-ai/ailia-models/tree/master/deep_fashion/mmfashion_retrieval
Clothing detection: https://github.com/axinc-ai/ailia-models/tree/master/deep_fashion/clothing-detection
Clothing attribute detection: https://github.com/open-mmlab/mmfashion
Alt Attribute Resource: https://github.com/tsennikova/fashion-ai/blob/main/fashion-attribute-recognition.ipynb
'''
import cv2
from deepface import DeepFace

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not capture frame.")
        break
    try:
        emotion = DeepFace.analyze(frame, actions = ['emotion'])[0]['dominant_emotion']
    except ValueError:
        emotion = 'Unknown'

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.putText(frame, emotion, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 2, cv2.LINE_4)

    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
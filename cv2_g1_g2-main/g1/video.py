import cv2


cap = cv2.VideoCapture(0)
faces = cv2.CascadeClassifier("smail")

while True:
    success, img = cap.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    results = faces.detectMultiScale(img, scaleFactor=2.1, minNeighbors=30)

    print(results)
    for (x,y,w,h) in results:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0, 255), thickness=3)

    cv2.imshow("Video 5", img)

    if cv2.waitKey(1) and 0xFF == ord("q"):
        break
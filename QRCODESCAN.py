import cv2
from pyzbar.pyzbar import decode

# Open the webcam
cap = cv2.VideoCapture(0)  # Use default webcam

while True:
    ret, frame = cap.read()  # Read a frame from the webcam
    if not ret:
        break

    # Decode QR codes in the frame
    for obj in decode(frame):
        print(f"QR Code Data: {obj.data.decode('utf-8')}")  # Print the decoded data

    # Display the video feed
    cv2.imshow("QR Code Scanner", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()

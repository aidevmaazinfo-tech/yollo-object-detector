from ultralytics import YOLO
import cv2
from tkinter import Tk, filedialog
import os

# Model load
model = YOLO("yolov8n.pt")

# File browse karne ke liye
Tk().withdraw()

file_path = filedialog.askopenfilename(
    title="Select Image or Video",
    filetypes=[
        ("Media Files", "*.jpg *.jpeg *.png *.mp4 *.avi *.mov *.mkv")
    ]
)

if not file_path:
    print("No file selected")
    exit()

# Check file type
ext = os.path.splitext(file_path)[1].lower()

image_ext = [".jpg", ".jpeg", ".png"]
video_ext = [".mp4", ".avi", ".mov", ".mkv"]


# ================= IMAGE DETECTION =================
if ext in image_ext:

    results = model(
        file_path,
        conf=0.10,
        iou=0.45,
        verbose=False
    )

    r = results[0]

    print("Detected Objects:", len(r.boxes))

    for box in r.boxes:
        cls = int(box.cls[0])
        conf = float(box.conf[0])
        print(model.names[cls], round(conf, 2))

    r.show()
    r.save(filename="output.jpg")


# ================= VIDEO DETECTION =================
elif ext in video_ext:

    cap = cv2.VideoCapture(file_path)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        results = model(
            frame,
            conf=0.10,
            iou=0.45,
            verbose=False
        )

        annotated = results[0].plot()

        cv2.imshow(
            "YOLO Detection",
            annotated
        )

        # q press kar ke exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


else:
    print("Unsupported file type")
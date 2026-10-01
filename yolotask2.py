from ultralytics import YOLO
import cv2
from tkinter import Tk, filedialog
import os

print("Loading YOLOv8 Open Images Model (600 Classes)...")
# YOLOv8 ka Open Images model load kar rahay hain.
# Pehli baar run hone par yeh internet se thori si file download karega.
model = YOLO("yolov8s-oiv7.pt")

while True:
    # Tkinter Setup (Popup hamesha Top par)
    root = Tk()
    root.attributes('-topmost', True)
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Select Image or Video (Click Cancel to Exit)",
        filetypes=[("Media Files", "*.jpg *.jpeg *.png *.jfif *.mp4 *.avi *.mov *.mkv")]
    )

    root.destroy()

    if not file_path:
        print("No file selected. Exiting program...")
        break

    ext = os.path.splitext(file_path)[1].lower()
    image_ext = [".jpg", ".jpeg", ".png", ".jfif"]
    video_ext = [".mp4", ".avi", ".mov", ".mkv"]

    # ================= IMAGE DETECTION =================
    if ext in image_ext:
        print(f"\nProcessing Image: {file_path}")

        results = model(
            file_path,
            conf=0.25,
            iou=0.45,
            verbose=False
        )

        r = results[0]
        print(f"Detected {len(r.boxes)} Objects:")

        for box in r.boxes:
            cls_id = int(box.cls[0])
            # Model apne andar mojood 600 names mein se khud naam nikalega
            class_name = model.names[cls_id]
            conf = float(box.conf[0])
            print(f"-> {class_name}: {round(conf, 2)}")

        annotated_img = r.plot()
        cv2.imshow("YOLOv8 Open Images Detection (Press Any Key to close and select next)", annotated_img)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

        r.save(filename="output_final.jpg")
        print("Image saved as output_final.jpg")

    # ================= VIDEO DETECTION =================
    elif ext in video_ext:
        print(f"\nProcessing Video: {file_path}")
        cap = cv2.VideoCapture(file_path)

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            results = model(
                frame,
                conf=0.25,
                iou=0.45,
                verbose=False
            )

            annotated = results[0].plot()
            cv2.imshow("YOLOv8 Open Images Video (Press 'q' to close)", annotated)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    else:
        print("Unsupported file type")

        
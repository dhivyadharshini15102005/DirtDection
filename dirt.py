from ultralytics import YOLO
import os

# === Step 1: Train the Model ===
def train_model():
    print("🚀 Starting training...")
    model = YOLO("yolov8n.pt")  # Nano model (fast)
    model.train(
        data="dirt.yaml",  # Path to your dataset config file
        epochs=50,
        imgsz=640,
        batch=16
    )
    print("✅ Training complete! Best weights saved in runs/detect/train/weights/best.pt")


# === Step 2: Run Live Webcam Detection ===
def run_webcam():
    print("🎥 Starting webcam detection...")
    best_weights = "runs/detect/train/weights/best.pt"

    if not os.path.exists(best_weights):
        raise FileNotFoundError("Best weights not found! Train the model first.")

    model = YOLO(best_weights)
    model.predict(source=0, show=True)  # 0 = default webcam


if __name__ == "__main__":
    # Step 1: Train the model
    train_model()

    # Step 2: Run webcam detection
    run_webcam()

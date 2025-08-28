import os
import glob

# Path to your dataset folder
DATASET_PATH = r"C:\Users\rajar\OneDrive\Desktop\dirtdection\dataset"

# Paths to train and val image folders
train_images = os.path.join(DATASET_PATH, "images", "train")
val_images = os.path.join(DATASET_PATH, "images", "val")

train_labels = os.path.join(DATASET_PATH, "labels", "train")
val_labels = os.path.join(DATASET_PATH, "labels", "val")

def check_folder(path, file_exts):
    if not os.path.exists(path):
        print(f"❌ Folder not found: {path}")
        return False
    files = []
    for ext in file_exts:
        files.extend(glob.glob(os.path.join(path, f"*.{ext}")))
    if not files:
        print(f"⚠️ No files found in: {path}")
        return False
    print(f"✅ Found {len(files)} files in {path}")
    return True

print("\n=== Checking Dataset Structure ===\n")
ok = True
ok &= check_folder(train_images, ["jpg", "png", "jpeg"])
ok &= check_folder(val_images, ["jpg", "png", "jpeg"])
ok &= check_folder(train_labels, ["txt"])
ok &= check_folder(val_labels, ["txt"])

if ok:
    print("\n🎉 Dataset structure looks good! You can train now.")
else:
    print("\n❗ Dataset structure has problems. Please fix before training.")

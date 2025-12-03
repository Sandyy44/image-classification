import os
import shutil
import random
import csv

SOURCE_DIR = os.path.join('traffic_Data', 'DATA')
LABELS_FILE = 'labels.csv'
DEST_DIR = 'dataset'
TRAIN_RATIO = 0.8  # 80% train, 20% val

def load_labels(csv_path):
    """Reads the CSV to map folder numbers (ClassId) to actual names (Name)"""
    label_map = {}
    if not os.path.exists(csv_path):
        print(f"Error: CSV file not found at {csv_path}")
        return {}

    with open(csv_path, mode='r') as f:
        reader = csv.reader(f)
        try:
            # Skip header if it exists
            header = next(reader)
        except StopIteration:
            return {}
        
        for row in reader:
            if len(row) >= 2:
                # Key = the ID (folder number), Value = The Class Name
                class_id = row[0].strip()
                class_name = row[1].strip()
                label_map[class_id] = class_name
    return label_map

def split_dataset():
    # Load the labels
    print("Loading labels...")
    labels = load_labels(LABELS_FILE)
    
    if not labels:
        print("No labels found or CSV is empty. Check your path.")
        return

    # Create Destination Folders
    train_dir = os.path.join(DEST_DIR, 'train')
    val_dir = os.path.join(DEST_DIR, 'val')

    # Create directories if they don't exist
    for d in [train_dir, val_dir]:
        os.makedirs(d, exist_ok=True)

    # Iterate through the numeric folders in DATA
    if not os.path.exists(SOURCE_DIR):
        print(f"Source directory {SOURCE_DIR} not found.")
        return

    folders = [f for f in os.listdir(SOURCE_DIR) if os.path.isdir(os.path.join(SOURCE_DIR, f))]
    
    print(f"Found {len(folders)} class folders. Starting split...")

    for folder_id in folders:
        # Get the actual class name from the CSV map
        # If the ID isn't in the CSV, we fallback to using the folder_id as the name
        class_name = labels.get(folder_id, folder_id)
        
        # Sanitize class name for file system (remove illegal chars just in case)
        class_name = "".join([c for c in class_name if c.isalnum() or c in (' ', '_', '-')]).strip()

        source_class_path = os.path.join(SOURCE_DIR, folder_id)
        
        # Get all images in the folder
        images = [img for img in os.listdir(source_class_path) 
                  if img.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
        
        # Shuffle to ensure random distribution
        random.shuffle(images)

        # Calculate split index
        split_point = int(len(images) * TRAIN_RATIO)
        
        train_images = images[:split_point]
        val_images = images[split_point:]

        # Define destination paths for this specific class
        dest_train_class_dir = os.path.join(train_dir, class_name)
        dest_val_class_dir = os.path.join(val_dir, class_name)

        os.makedirs(dest_train_class_dir, exist_ok=True)
        os.makedirs(dest_val_class_dir, exist_ok=True)

        # Copy Train Images
        for img in train_images:
            src = os.path.join(source_class_path, img)
            dst = os.path.join(dest_train_class_dir, img)
            shutil.copy2(src, dst)

        # Copy Val Images
        for img in val_images:
            src = os.path.join(source_class_path, img)
            dst = os.path.join(dest_val_class_dir, img)
            shutil.copy2(src, dst)

        print(f"Processed Class '{class_name}' (ID: {folder_id}): {len(train_images)} Train, {len(val_images)} Val")

    print("\n------------------------------------------------")
    print("Dataset construction complete")
    print(f"Check the '{DEST_DIR}' folder.")

if __name__ == "__main__":
    split_dataset()
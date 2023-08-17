import os
import hashlib
import shutil
from PIL import Image

folder1_path = (r"D:\duplicate\first")
folder2_path = (r"D:\duplicate\second")
destination_path = (r"D:\duplicate\moved_images")

def calculate_hash(image_path):
    with open(image_path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def move_identical_images(folder1_path, folder2_path, destination_path):
    identical_count = 0
    folder1_images = [f for f in os.listdir(folder1_path) if f.endswith('.jpg') or f.endswith('.png')]

    for image_file in folder1_images:
        image_path1 = os.path.join(folder1_path, image_file)
        image_path2 = os.path.join(folder2_path, image_file)

        if os.path.exists(image_path2):
            hash1 = calculate_hash(image_path1)
            hash2 = calculate_hash(image_path2)

            if hash1 == hash2:
                print(f"Moving identical image: {image_path2}")
                destination_image_path = os.path.join(destination_path, image_file)
                shutil.move(image_path2, destination_image_path)
                identical_count += 1

    print(f"Moved {identical_count} identical images.")

if __name__ == "__main__":
    move_identical_images(folder1_path, folder2_path, destination_path)

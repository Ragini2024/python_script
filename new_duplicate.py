import os
import hashlib
from PIL import Image

def calculate_hash(image_path):
    with open(image_path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def remove_identical_images(folder1, folder2):
    identical_count = 0
    folder1_images = [f for f in os.listdir(folder1) if f.endswith('.jpg') or f.endswith('.png')]

    for image_file in folder1_images:
        image_path1 = os.path.join(folder1, image_file)
        image_path2 = os.path.join(folder2, image_file)

        if os.path.exists(image_path2):
            hash1 = calculate_hash(image_path1)
            hash2 = calculate_hash(image_path2)

            if hash1 == hash2:
                print(f"Removing identical image: {image_path2}")
                os.remove(image_path2)
                identical_count += 1

    print(f"Removed {identical_count} identical images.")

if __name__ == "__main__":
    folder1_path = (r"D:\duplicate\first")
    folder2_path = (r"D:\duplicate\second")
    
    remove_identical_images(folder1_path, folder2_path)

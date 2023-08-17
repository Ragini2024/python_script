import os
import shutil

image_folder = (r"C:\Users\ASUS\Downloads\Ragini_cts_cellphone_reverification\Ragini_cts_cellphone_reverification")
label_folder = (r"C:\Users\ASUS\Downloads\Ragini_cts_cellphone_reverification\Ragini_cts_cellphone_reverification")
target_class = "cellphone"
unlabeled_folder = (r"C:\Users\ASUS\Downloads\Ragini_cts_cellphone_reverification\no_cellphone")
moved_folder = (r"C:\Users\ASUS\Downloads\Ragini_cts_cellphone_reverification\no_cellphone")

image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
label_files = [f for f in os.listdir(label_folder) if f.endswith('.xml')]

for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)
    label_file = os.path.splitext(image_file)[0] + ".xml"
    label_path = os.path.join(label_folder, label_file)

    if label_file not in label_files:
        shutil.move(image_path, os.path.join(unlabeled_folder, image_file))
        print(f"Moved unlabeled image: {image_file}")
    else:
        with open(label_path, 'r') as label_file:
            label_content = label_file.read().strip()  # Assuming label content is a single line
            if target_class not in label_content:
                shutil.move(image_path, os.path.join(unlabeled_folder, image_file))
                print(f"Moved image without '{target_class}' label: {image_file}")
                shutil.move(label_path, os.path.join(unlabeled_folder, label_file))
                print(f"Moved corresponding label file: {label_file}")

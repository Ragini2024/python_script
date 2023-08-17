import os

image_folder = (r"C:\Users\ASUS\Downloads\Ragini_cts_cellphone_reverification\Ragini_cts_cellphone_reverification")
label_folder = (r"C:\Users\ASUS\Downloads\Ragini_cts_cellphone_reverification\Ragini_cts_cellphone_reverification")
target_class = "cellphone"

image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
label_files = [f for f in os.listdir(label_folder) if f.endswith('.xml')]

not_labeled_count = 0

for image_file in image_files:
    label_file = os.path.splitext(image_file)[0] + ".txt"
    label_path = os.path.join(label_folder, label_file)

    if label_file not in label_files:
        not_labeled_count += 1
    else:
        with open(label_path, 'r') as label_file:
            label_content = label_file.read().strip()  # Assuming label content is a single line
            if target_class not in label_content:
                not_labeled_count += 1

print(f"Total number of images not labeled with '{target_class}': {not_labeled_count}")

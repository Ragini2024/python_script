import os

image_folder = (r"C:\Users\ASUS\Downloads\Ragini_cts_cellphone_reverification\Ragini_cts_cellphone_reverification")
label_folder = (r"C:\Users\ASUS\Downloads\Ragini_cts_cellphone_reverification\Ragini_cts_cellphone_reverification")
target_class = "cellphone"

image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
label_files = [f for f in os.listdir(label_folder) if f.endswith('.txt')]

for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)
    label_file = os.path.splitext(image_file)[0] + ".txt"
    label_path = os.path.join(label_folder, label_file)

    if label_file in label_files:
        with open(label_path, 'r') as label_file:
            label_content = label_file.read().strip()  # Assuming label content is a single line
            if target_class in label_content:
                print(f"Image {image_file} is labeled with '{target_class}' class.")
            else:
                print(f"Image {image_file} is not labeled with '{target_class}' class.")
    else:
        print(f"Image {image_file} is not labeled.")
        print(len({image_file}))

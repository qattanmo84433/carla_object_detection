import os
import shutil

# Base input folder
base_input_folder = 'input'
# Define the paths to the source folders
images_src_folder = os.path.join(base_input_folder, 'images')
labels_src_folder = os.path.join(base_input_folder, 'labels')

# Define the base directory for train, test, and val folders
base_dir = './input'

# Text files containing the mappings
text_files = {
    'train': os.path.join(base_input_folder, 'autosplit_train.txt'),
    'test': os.path.join(base_input_folder, 'autosplit_test.txt'),
    'val': os.path.join(base_input_folder, 'autosplit_val.txt')
}

# Function to create directories if they don't exist
def create_dir_if_not_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Process each text file
for dataset_type, file_path in text_files.items():
    # Create the directories for images and labels
    images_dest_folder = os.path.join(base_dir, dataset_type, 'images')
    labels_dest_folder = os.path.join(base_dir, dataset_type, 'labels')
    create_dir_if_not_exists(images_dest_folder)
    create_dir_if_not_exists(labels_dest_folder)
    
    # Open and read the text file
    with open(file_path, 'r') as file:
        for line in file:
            # Extract the path and then the image name from each line
            image_rel_path = line.strip()  # e.g., ./images/DATASET_00010194.jpg
            image_name = os.path.basename(image_rel_path)  # Extracts DATASET_00010194.jpg from the path
            # Assuming label file has the same base name with .txt extension
            label_name = os.path.splitext(image_name)[0] + '.txt'
            
            # Define source and destination paths for the image and label
            image_src = os.path.join(images_src_folder, image_name)
            label_src = os.path.join(labels_src_folder, label_name)
            image_dest = os.path.join(images_dest_folder, image_name)
            label_dest = os.path.join(labels_dest_folder, label_name)
            
            # Check if the source files exist before copying
            if os.path.exists(image_src) and os.path.exists(label_src):
                shutil.copy(image_src, image_dest)
                shutil.copy(label_src, label_dest)
            else:
                print(f"Warning: Missing file(s) for {image_name}")

print("Processing completed.")

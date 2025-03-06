import os
from pdf2image import convert_from_path

# Function to convert PDF to JPG images
def convert_pdf_to_images(pdf_path, output_folder):
    images = convert_from_path(pdf_path, dpi=300)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_paths = []
    for i, img in enumerate(images):
        image_name = f"page_{i + 1}.jpg"
        image_path = os.path.join(output_folder, image_name)
        img.save(image_path, "JPEG")
        image_paths.append(image_path)  

    return image_paths

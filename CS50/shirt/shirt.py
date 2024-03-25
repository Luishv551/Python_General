import sys
import os
from PIL import Image, ImageOps
from pathlib import Path

def overlay_shirt(input_image_path, output_image_path):
    # Check if exactly two command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python shirt.py <input_image_path> <output_image_path>")
        sys.exit(1)

    # Get input and output file paths from command-line arguments
    input_image_path = Path(input_image_path)
    output_image_path = Path(output_image_path)

    # Check if input and output image paths end with supported extensions
    supported_extensions = ['.jpg', '.jpeg', '.png']
    if (input_image_path.suffix.lower() not in supported_extensions or
        output_image_path.suffix.lower() not in supported_extensions):
        print("Input and output images must have .jpg, .jpeg, or .png extension")
        sys.exit(1)

    # Check if input and output image paths have the same extension
    if input_image_path.suffix.lower() != output_image_path.suffix.lower():
        print("Input and output images must have the same extension")
        sys.exit(1)

    # Check if input image exists
    if not input_image_path.is_file():
        print("Input image does not exist")
        sys.exit(1)

    try:
        # Open input image
        input_image = Image.open(input_image_path)

        # Open shirt image
        shirt_image = Image.open("shirt.png")

        # Resize and crop input image to match shirt size
        input_image = ImageOps.fit(input_image, shirt_image.size)

        # Overlay shirt on input image
        input_image.paste(shirt_image, (0, 0), shirt_image)

        # Save the resulting image
        input_image.save(output_image_path)

        print(f"Shirt overlay saved as {output_image_path}")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Expecting two command-line arguments: input image path and output image path
    if len(sys.argv) != 3:
        print("Usage: python shirt.py <input_image_path> <output_image_path>")
        sys.exit(1)

    input_image_path = sys.argv[1]
    output_image_path = sys.argv[2]

    overlay_shirt(input_image_path, output_image_path)

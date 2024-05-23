from PIL import image
import os 

def resize_image(input_path, output_path, size):
    """Resize the image to the specified size and save it to output path."""
    with Image.open(input_path) as img:
        img = img.resize(size, Image.ANTIALIAS)
        img.save(output_path)

def convert_image(input_path, output_path, output_format):
    """Convert the image to the specified format and save it to output path."""
    with Image.open(input_path) as img:
        img.save(output_path, format = output_format)
        
def process_images(input_dir, output_dir, size, output_format):
    """Resize and convert all images in input directory."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)
        if os.path.isfile(input_path):
            output_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.{output_format.lower}")
            
            resize_image(input_path, output_path, size)
            convert_image(output_path, output_path, output_format)
            print(f"Processed image: {filename}")
            

if __name__ == "main":
    print("This program converts and resizeds images.")
    
    input_dir = input("Which directory would you like to target?")
    output_dir = input("In which directory would you like to output to?")
    # TODO: input to maintain aspect ratio
    resize_x = input("How tall would you like the image?")
    resize_y = input("How wide would you like the image?")
    resize_dimensions = (resize_x, resize_y)
    output_format = input("What type of file do you want to convert to?")
    
    process_images(input_dir, output_dir, resize_dimensions, output_format)

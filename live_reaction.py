from PIL import Image
from sys import exit
from os.path import exists


# Try to return an image, exit if a valid file is not found
def try_open(path):
    extensions = [".bmp", ".png", ".jpg", ".jfif", ".jpg_large", ".jpe", ".jif", ".jfi"]

    try:
        # Check for compatible file extensions
        for i in range(len(extensions)):
            if exists(path + extensions[i]):
                return Image.open(path + extensions[i])
            else:
                # Try opening an image without an extension
                if exists(path):
                    return Image.open(path)
    except OSError:
        print(f"Cannot open \"{path}\". Does the file exist?")
        exit(1)


def main():
    # Set the dimensions (width/height) and position of the images
    main_dimensions = (656, 373)
    main_position = (12, 117)
    title_dimensions = (214, 74)
    title_position = (150, 22)
    
    # Open images for processing
    base = Image.open("images/base.png")
    main_image = try_open("images/input")
    title_image = try_open("images/input")

    # Scale both images 
    main_image = main_image.resize(main_dimensions)
    title_image = title_image.resize(title_dimensions)

    # Paste images onto base
    base.paste(main_image, main_position)
    base.paste(title_image, title_position)

    # Save final image
    base.save("output.png")


if __name__ == "__main__":
    main()
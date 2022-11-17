"""
[Day 7] Assignment: Steganography
    - Turn in on Gradescope (https://make.sc/bew2.3-gradescope)
    - Lesson Plan: https://tech-at-du.github.io/ACS-3230-Web-Security/#/Lessons/Steganography

Deliverables:
    1. All TODOs in this file.
    2. Decoded sample image with secret text revealed
    3. Your own image encoded with hidden secret text!
"""
# TODO: Run `pip3 install Pillow` before running the code.
from PIL import Image


def decode_image(path_to_png):
    """
    This function takes an encoded image, 
    Decodes a hidden image based upon the red channel values,
    Then saves the decoded image to your disc
    """
    # Open the image using PIL:
    encoded_image = Image.open(path_to_png)

    # Separate the red channel from the rest of the image:
    red_channel = encoded_image.split()[0]

    # Create a new PIL image with the same size as the encoded image:
    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()
    x_size, y_size = encoded_image.size

    # TODO: Using the variables declared above, replace `print(red_channel)` with a complete implementation:
    for y in range(y_size):
        for x in range(x_size):
            ''' sort pixels of encoded image here'''
            # get the pixel
            red_value = red_channel.getpixel((x,y))
            # convert the red value to a bit
            red_value = format(red_value, 'b')
            # sort based on Least Significant Bit
            if red_value[-1] == '1':
                decoded_image.putpixel((x,y), (0,0,0))
            else:
                decoded_image.putpixel((x,y), (255,255,255))
            

    # DO NOT MODIFY. Save the decoded image to disk:
    decoded_image.save("decoded_image.png")


def encode_image(path_to_png):
    """
    This function takes an image,
    Edits the red channel of the image to encode a secret image,
    Then saves the encoded image to your disc.
    """
    pass


def write_text(text_to_write):
    """
    TODO: Add docstring and complete implementation.
    """
    pass

if __name__ == "__main__":
    decode_image('encoded_sample.png')
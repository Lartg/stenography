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
from PIL import Image, ImageDraw


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

    # construct decoded image
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


def encode_image(path_to_png, text_to_write: str):
    """
    This function takes an image,
    Edits the red channel of the image to encode a secret message,
    Then saves the encoded image to your disc.
    """

    # load image that will be encoded
    base_image = Image.open(path_to_png)


    # create text template
    x_size, y_size = base_image.size
    secret_message = write_text(text_to_write, (x_size, y_size))

    # draw over the base image red channel using the template
    for y in range(y_size):
        for x in range(x_size):
            ''' prep base image for editing'''
            # get pixel
            base_pixel = base_image.getpixel((x,y))

            # convert red channel to string bit
            base_pixel_red_channel = format(base_pixel[0], 'b')

            # drop least Significant Bit
            base_pixel_red_channel = base_pixel_red_channel[:-1]

            ''' edit base image using template reference'''
            # get pixel of template
            message_pixel = secret_message.getpixel((x,y))
    
            # check if text present
            if message_pixel[0] == 255:
                # change Least Significant Bit of red channel to 0
                base_pixel_red_channel += '0'

                # convert red channel string to number
                base_pixel_red_channel = int(base_pixel_red_channel, 2)

                # rewrite pixel
                base_image.putpixel((x,y), (base_pixel_red_channel, base_pixel[1], base_pixel[2]))

                pass
            else:
                # change Least Significant Bit of red channel to 1
                base_pixel_red_channel += '1'

                # convert red channel string to number
                base_pixel_red_channel = int(base_pixel_red_channel, 2)

                # rewrite pixel
                base_image.putpixel((x,y), (base_pixel_red_channel, base_pixel[1], base_pixel[2]))
                pass

    # save encoded image
    base_image.save("encoded_image.png")


def write_text(text_to_write, size):
    """
    Converts text to an image of text to act as a stencil for secret message encoding
    """

    secret_message = Image.new("RGB", size, (255,255,255))

    text = ImageDraw.Draw(secret_message)
    
    text.multiline_text((10, 10), text_to_write, fill=(0, 0, 0))

    return secret_message

if __name__ == "__main__":
    encode_image('encoded_sample.png', 'This is string!')
    decode_image('encoded_image.png')
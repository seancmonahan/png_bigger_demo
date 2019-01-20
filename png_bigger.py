#!python
#Sean Monahan, 2019

"""Demo that lossless compression (PNG) of *random* data (generally) increases size."""

from __future__ import print_function
import numpy as np
from PIL import Image
import os

def random_bytes(width, height, depth):
    return np.random.bytes(width*height*depth)

def random_image(width, height):
    return Image.frombytes("RGB", (width, height), random_bytes(width, height, depth=3))

if __name__ == '__main__':
    print()
    print(__doc__)
    print()

    dimensions = {'width': 800, 'height': 600}
    filename_base = "random_{width}_{height}".format(**dimensions)
    image = random_image(**dimensions)

    bmp_filename = filename_base + '.bmp'
    png_filename = filename_base + '.png'
    print('Saving image as "{}" and "{}"'.format(bmp_filename, png_filename))

    image.save(bmp_filename, format='bmp')
    image.save(png_filename, format='png')

    # Verify that the images decoded again yield identical data
    print()
    print("Verifying that the image files decode to identical images...\t\t", end='')
    image_from_bmp = Image.open(bmp_filename)
    image_from_png = Image.open(png_filename)

    if image_from_bmp.tobytes() != image_from_png.tobytes():
        print("FAIL!!!!!\nThe bmp and png files don't decode to the same image")
    else:
        print("OK\nBMP and PNG files decode to the same image data")

    bmp_size = os.stat(bmp_filename).st_size
    png_size = os.stat(png_filename).st_size
    delta = png_size - bmp_size

    print()
    print("BMP size: {:20d} bytes".format(bmp_size))
    print("PNG size: {:20d} bytes".format(png_size))
    print("-"*30)
    print()
    print("PNG is {:d} bytes larger".format(delta))

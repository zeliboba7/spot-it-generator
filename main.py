import glob
import os
import argparse


from spotit.utilities import generate_images
from spotit import create_sheets


# parse command line argumnents
parser = argparse.ArgumentParser(description="""
Plots the card for the Dobble or Spot It! game.  More about the game see
http://en.wikipedia.org/wiki/Dobble
""")
parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)  # add default values to help
parser.add_argument('-i', '--images', default='images', type=str,
                    help="Input image directory, for 5 images per card 31 images rquired")
parser.add_argument('-o', '--output', default='cards.pdf', type=str,
                    help="Output file name")
parser.add_argument('-O', '--order', default=5,type=int,
                    help="Number of images per card, i.e. order + 1")
args = parser.parse_args()

filename = args.output  # filename of the PDF
order = args.order  # number of images at each card
images_path = args.images # path where to store generated images

# create a directory for generated images
if not os.path.isdir(images_path):
    os.makedirs(images_path)

generate_images(images_path, order=5)  # generate images with numbers
images = sorted(glob.glob(os.path.join(images_path, '*.png')))  # list of the images
create_sheets(filename, order, images)  # create the PDF with cards

import os
from Tkinter import*
from tkFileDialog import askdirectory

from PIL import Image

from PIL.ExifTags import TAGS

from os import rename, listdir

def get_exif(img):
    ret = {}

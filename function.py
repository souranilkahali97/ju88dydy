import numpy as np
from ipywidgets import interact, fixed
from PIL import Image

def imshow(X, resize=None):
    resized_width, resized_height = resize
    img=Image.fromarray(X.astype('unit8'), 'RGB')
    im_resized=img.resize((resized_width, resized_height), Image.ANTIALIAS)
    im_resized.show()
    pass
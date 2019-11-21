import numpy as np
from PIL import Image

im = np.array(Image.open('temp/samplenotes.jpg').convert('L').resize((2480 , 3508)))

th = 115
im_bool = im > th

threshold = (im > th) * 255

Image.fromarray(np.uint8(threshold)).save('temp/newimage.png')

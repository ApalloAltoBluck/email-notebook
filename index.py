import numpy as np
from PIL import Image

im = np.array(Image.open('temp/samplenotes.jpg').convert('L').resize((1240, 1754)))

th = 150
im_bool = im > th

threshold = (im > th) * 255
im_bin_64 = (im > 64) * 255
im_bin_192 = (im > 192) * 255

im_bin = np.concatenate((im_bin_64, threshold, im_bin_192), axis=1)
Image.fromarray(np.uint8(im_bin)).save('temp/newimage.png')

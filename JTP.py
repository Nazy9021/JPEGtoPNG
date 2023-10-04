import sys
import os
from PIL import Image

img_name = sys.argv[1]
out_img = sys.argv[2]
# print(img_name,out_img)

if not os.path.exists(out_img):
   os.makedirs(out_img)

for filename in os.listdir(img_name):
	imge = Image.open(f'{img_name}{filename}')
	cl_n = os.path.splitext(filename)[0]
	imge.save(f'{out_img}{cl_n}.png','png')
print('all done!')

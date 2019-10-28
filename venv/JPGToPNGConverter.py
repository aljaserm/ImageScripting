import  sys
import os
from PIL import Image

image_folder = sys.argv[1]
output_folder = sys.argv[2]

# print(os.path.exists(output_folder))
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for fileName in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{fileName}')
    clean_name = os.path.splitext(fileName)[0]
    # print(clean_name)
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('Done!')


print(image_folder, output_folder)
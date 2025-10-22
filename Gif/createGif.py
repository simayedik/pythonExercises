from pickletools import optimize

from PIL  import Image

image_paths = ['img.png','img_1.png',]
output_path = 'output_image.gif'

images = [Image.open(image) for image in image_paths]

images[0].save(output_path,
               optimize=True,
               save_all=True,
               append_images=images,
               loop=0)


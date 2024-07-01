from PIL import Image

image_list=["indir.jpeg","indir2.jpeg","indir3.jpeg"]
image_list=[Image.open(image) for image in image_list]
image_list[0].save("squirell.gif",save_all=True,append_images=image_list[1:],duration=1000)
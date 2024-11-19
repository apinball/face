from PIL import Image

img = Image.open('./ffhq_image/source.png')

img_cropped = img.crop((150,0,750,600))

img_resized = img_cropped.resize((1024,1024))

img_resized.save('sample.png')
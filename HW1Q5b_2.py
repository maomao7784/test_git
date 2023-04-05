from PIL import Image

# open the bmp image
bmp_image = Image.open("/Users/linyinghsiao/Downloads/HW1/Q5_1/watermarked_lena.bmp")

# save the bmp image as jpg
bmp_image.save("/Users/linyinghsiao/Downloads/HW1/Q5_2/example.jpg")

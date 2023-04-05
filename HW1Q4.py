from PIL import Image

def overlay_image(image1, image2):
    width1, height1 = image1.size
    width2, height2 = image2.size

    for y in range(height2):
        for x in range(width2):
            pixel2 = image2.getpixel((x, y))

            # Check if the pixel is not white
            if pixel2 != (255, 255, 255, 255):
                image1.putpixel((x, y), pixel2)

    return image1

if __name__ == "__main__":
    lena_path = "/Users/linyinghsiao/Downloads/HW1/Q3/resized_lena.bmp"
    graveler_path = "/Users/linyinghsiao/Downloads/HW1/graveler.bmp"
    output_path = "/Users/linyinghsiao/Downloads/HW1/Q4/overlay_image.bmp"

    lena_image = Image.open(lena_path).convert("RGBA")
    graveler_image = Image.open(graveler_path).convert("RGBA")

    overlayed_image = overlay_image(lena_image, graveler_image)
    overlayed_image.save(output_path)

    print(f"Overlayed image saved at {output_path}")


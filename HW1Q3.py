from PIL import Image

def bilinear_interpolation(image, new_width, new_height):
    width, height = image.size
    resized_image = Image.new("RGBA", (new_width, new_height))

    for y in range(new_height):
        for x in range(new_width):
            x_ratio = (x + 0.0) / (new_width - 1) * (width - 1)
            y_ratio = (y + 0.0) / (new_height - 1) * (height - 1)

            x1, y1 = int(x_ratio), int(y_ratio)
            x2, y2 = min(x1 + 1, width - 1), min(y1 + 1, height - 1)

            x_diff, y_diff = x_ratio - x1, y_ratio - y1

            pixel1 = image.getpixel((x1, y1))
            pixel2 = image.getpixel((x1, y2))
            pixel3 = image.getpixel((x2, y1))
            pixel4 = image.getpixel((x2, y2))

            new_pixel = []
            for i in range(4):
                value = int(pixel1[i] * (1 - x_diff) * (1 - y_diff) +
                            pixel2[i] * (1 - x_diff) * y_diff +
                            pixel3[i] * x_diff * (1 - y_diff) +
                            pixel4[i] * x_diff * y_diff)
                new_pixel.append(value)
                
            resized_image.putpixel((x, y), tuple(new_pixel))

    return resized_image

if __name__ == "__main__":
    input_path = "/Users/linyinghsiao/Downloads/HW1/lena.bmp"
    output_path = "/Users/linyinghsiao/Downloads/HW1/Q3/resized_lena.bmp"
    new_width, new_height = 1024, 1024

    image = Image.open(input_path).convert("RGBA")
    resized_image = bilinear_interpolation(image, new_width, new_height)
    resized_image.save(output_path)

    print(f"Resized image saved at {output_path}")
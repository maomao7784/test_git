from PIL import Image, ImageOps

def embed_watermark(image, watermark, alpha=0.2):
    width, height = image.size
    width_w, height_w = watermark.size

    for y in range(height_w):
        for x in range(width_w):
            pixel_w = watermark.getpixel((x, y))
            pixel_i = image.getpixel((x, y))

            # Embed the watermark's pixel into the image using the alpha value
            r = int(pixel_i[0] * (1 - alpha) + pixel_w[0] * alpha)
            g = int(pixel_i[1] * (1 - alpha) + pixel_w[1] * alpha)
            b = int(pixel_i[2] * (1 - alpha) + pixel_w[2] * alpha)

            image.putpixel((x, y), (r, g, b))

    return image

def retrieve_watermark(image, watermark_size, alpha=0.2):
    width, height = image.size
    retrieved_watermark = Image.new("RGB", watermark_size)

    for y in range(watermark_size[1]):
        for x in range(watermark_size[0]):
            pixel_i = image.getpixel((x, y))

            # Retrieve the watermark's pixel from the image using the alpha value
            r = int((pixel_i[0] - (1 - alpha) * 255) / alpha)
            g = int((pixel_i[1] - (1 - alpha) * 255) / alpha)
            b = int((pixel_i[2] - (1 - alpha) * 255) / alpha)

            retrieved_watermark.putpixel((x, y), (r, g, b))

    return retrieved_watermark

if __name__ == "__main__":
    lena_path = "/Users/linyinghsiao/Downloads/HW1/lena.bmp"
    flipped_lena_path = "/Users/linyinghsiao/Downloads/HW1/Q5_1/flipped_lena.bmp"

    graveler_path = "/Users/linyinghsiao/Downloads/HW1/graveler.bmp"

    watermarked_path = "/Users/linyinghsiao/Downloads/HW1/Q5_1/watermarked_lena.bmp"
    
    retrieved_path = "/Users/linyinghsiao/Downloads/HW1/Q5_1/retrieved_graveler.bmp"

    lena_image = Image.open(lena_path).convert("RGB")
    flipped_lena = ImageOps.mirror(lena_image)  # Updated
    flipped_lena.save(flipped_lena_path)

    graveler_image = Image.open(graveler_path).convert("RGB")

    watermarked_image = embed_watermark(flipped_lena, graveler_image, alpha=0.2)
    watermarked_image.save(watermarked_path)

    retrieved_watermark = retrieve_watermark(watermarked_image, graveler_image.size, alpha=0.2)
    retrieved_watermark.save(retrieved_path)

    print(f"Watermarked image saved at {watermarked_path}")
    print(f"Retrieved watermark image saved at {retrieved_path}")
import cv2
import numpy as np
from PIL import Image, ImageOps

# Embed watermark
def embed_watermark(image, watermark, alpha=0.2):
    width, height = image.size
    width_w, height_w = watermark.size

    for y in range(height_w):
        for x in range(width_w):
            pixel_w = watermark.getpixel((x, y))
            pixel_i = image.getpixel((x, y))

            r = int(pixel_i[0] * (1 - alpha) + pixel_w[0] * alpha)
            g = int(pixel_i[1] * (1 - alpha) + pixel_w[1] * alpha)
            b = int(pixel_i[2] * (1 - alpha) + pixel_w[2] * alpha)

            image.putpixel((x, y), (r, g, b))

    return image

# Retrieve watermark
def retrieve_watermark(image, watermark_size, alpha=0.2):
    width, height = image.size
    retrieved_watermark = Image.new("RGB", watermark_size)

    for y in range(watermark_size[1]):
        for x in range(watermark_size[0]):
            pixel_i = image.getpixel((x, y))

            r = int((pixel_i[0] - (1 - alpha) * 255) / alpha)
            g = int((pixel_i[1] - (1 - alpha) * 255) / alpha)
            b = int((pixel_i[2] - (1 - alpha) * 255) / alpha)

            retrieved_watermark.putpixel((x, y), (r, g, b))

    return retrieved_watermark

# Calculate PSNR
def calculate_psnr(img1, img2):
    mse = np.mean((img1 - img2) ** 2)
    if mse == 0:
        return 100
    max_pixel = 255.0
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr

if __name__ == "__main__":
    lena_path = "/Users/linyinghsiao/Downloads/HW1/lena.bmp"
    flipped_lena_path = "/Users/linyinghsiao/Downloads/HW1/Q5_1/flipped_lena.bmp"

    graveler_path = "/Users/linyinghsiao/Downloads/HW1/graveler.bmp"

    watermarked_path = "/Users/linyinghsiao/Downloads/HW1/Q5_1/watermarked_lena.bmp"
    
    retrieved_path = "/Users/linyinghsiao/Downloads/HW1/Q5_1/retrieved_graveler.bmp"

    lena_image = Image.open(lena_path).convert("RGB")
    flipped_lena = ImageOps.mirror(lena_image)                  
    flipped_lena.save(flipped_lena_path)

    graveler_image = Image.open(graveler_path).convert("RGB")

    watermarked_image = embed_watermark(flipped_lena, graveler_image, alpha=0.2)
    watermarked_image.save(watermarked_path)

    retrieved_watermark = retrieve_watermark(watermarked_image, graveler_image.size, alpha=0.2)
    retrieved_watermark.save(retrieved_path)

    compression_ratios = [50, 75, 90]                      

    for ratio in compression_ratios:
        jpeg_path = f"/Users/linyinghsiao/Downloads/HW1/Q5_2/watermarked_lena_{ratio}.jpg"
        decoded_path = f"/Users/linyinghsiao/Downloads/HW1/Q5_2/decoded_lena_{ratio}.bmp"

        # Encode the watermarked image with the given compression ratio
        watermarked_image.save(jpeg_path, format="JPEG", quality=ratio)

        # Decode the JPEG image
        decoded_image = Image.open(jpeg_path)
        decoded_image.save(decoded_path)

        # Retrieve the watermark from the decoded image
        retrieved_watermark = retrieve_watermark(decoded_image, graveler_image.size, alpha=0.2)
        retrieved_watermark_path = f"/Users/linyinghsiao/Downloads/HW1/Q5_2/retrieved_graveler_{ratio}.bmp"
        retrieved_watermark.save(retrieved_watermark_path)

        # Calculate the PSNR between the original and retrieved watermarks
        original_watermark_np = np.array(graveler_image)
        retrieved_watermark_np = np.array(retrieved_watermark)

        psnr = calculate_psnr(original_watermark_np, retrieved_watermark_np)

        print(f"Compression ratio: {ratio}, PSNR: {psnr:.2f} dB")
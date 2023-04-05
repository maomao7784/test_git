import cv2
import numpy as np
from scipy.fftpack import dct, idct

def dct2(block):
    return dct(dct(block.T, norm='ortho').T, norm='ortho')

def idct2(block):
    return idct(idct(block.T, norm='ortho').T, norm='ortho')

def embed_watermark(image, watermark, alpha=1):
    h, w, _ = image.shape
    watermark_resized = cv2.resize(watermark, (w, h), interpolation=cv2.INTER_LINEAR)

    coeffs_image = dct2(image[:, :, 0])
    coeffs_watermark = dct2(watermark_resized)

    watermarked_coeffs = coeffs_image + alpha * coeffs_watermark
    watermarked_y_channel = idct2(watermarked_coeffs)
    watermarked_img = image.copy()
    watermarked_img[:, :, 0] = watermarked_y_channel
    return watermarked_img

def main():
    # Load Lena image, flip it, and convert to YCrCb color space
    lena_img = cv2.imread("/Users/linyinghsiao/Downloads/HW1/lena.bmp")
    flipped_lena = cv2.flip(lena_img, 1)
    flipped_lena_ycrcb = cv2.cvtColor(flipped_lena, cv2.COLOR_BGR2YCrCb)

    # Load watermark image and convert it to grayscale
    watermark = cv2.imread("/Users/linyinghsiao/Downloads/HW1/graveler.bmp")
    watermark_gray = cv2.cvtColor(watermark, cv2.COLOR_BGR2GRAY)

    # Embed the watermark into the Lena image
    watermarked_img_ycrcb = embed_watermark(flipped_lena_ycrcb, watermark_gray)
    watermarked_img = cv2.cvtColor(watermarked_img_ycrcb, cv2.COLOR_YCrCb2BGR)

    # Save the watermarked image
    cv2.imwrite("/Users/linyinghsiao/Downloads/HW1/Q5_1/watermarked_lena.bmp", watermarked_img)

if __name__ == "__main__":
    main()

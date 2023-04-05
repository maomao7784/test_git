import cv2
import numpy as np

# Define the PSNR function
def psnr(img1, img2):
    mse = np.mean((img1 - img2) ** 2)
    if mse == 0:
        return float('inf')
    max_pixel = 255.0
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr

# Load the original watermark image
original_watermark = cv2.imread("/Users/linyinghsiao/Downloads/HW1/Q5_2/example.jpg")

# Load the decoded watermarked images for different compression ratios
decoded1 = cv2.imread("/Users/linyinghsiao/Downloads/HW1/Q5_2/decoded_watermarked_lena_quality_50.jpg")
decoded2 = cv2.imread("/Users/linyinghsiao/Downloads/HW1/Q5_2/decoded_watermarked_lena_quality_75.jpg")
decoded3 = cv2.imread("/Users/linyinghsiao/Downloads/HW1/Q5_2/decoded_watermarked_lena_quality_95.jpg")

# Calculate the PSNR value between the original and retrieved watermarks for each compression ratio
psnr1 = psnr(original_watermark, decoded1)
psnr2 = psnr(original_watermark, decoded2)
psnr3 = psnr(original_watermark, decoded3)

# Print the PSNR values
print("PSNR (Compression Ratio 1): ", psnr1)
print("PSNR (Compression Ratio 2): ", psnr2)
print("PSNR (Compression Ratio 3): ", psnr3)

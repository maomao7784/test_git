import cv2

def main():
    # Read the watermarked image
    watermarked_img = cv2.imread("/Users/linyinghsiao/Downloads/HW1/Q5_1/watermarked_lena.bmp")

    # Define three different JPEG compression ratios
    compression_ratios = [50, 75, 95]

    for ratio in compression_ratios:
        # Encode the watermarked image using the JPEG standard with a specific compression ratio
        encoded_img = cv2.imencode(".jpg", watermarked_img, [int(cv2.IMWRITE_JPEG_QUALITY), ratio])[1]

        # Decode the encoded image
        decoded_img = cv2.imdecode(encoded_img, cv2.IMREAD_COLOR)

        # Save the decoded image
        cv2.imwrite(f"/Users/linyinghsiao/Downloads/HW1/Q5_2/decoded_watermarked_lena_quality_{ratio}.jpg", decoded_img)

if __name__ == "__main__":
    main()

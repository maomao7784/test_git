import cv2
import numpy as np

def merge_images(image1, image2):
    h1, w1 = image1.shape[:2]
    h2, w2 = image2.shape[:2]

    height = max(h1, h2)
    width = w1 + w2

    merged_image = np.zeros((height, width, 3), dtype=np.uint8)

    # Place image1 on the left side of the merged image
    merged_image[:h1, :w1] = image1

    # Place image2 on the right side of the merged image
    merged_image[:h2, w1:] = image2

    return merged_image

if __name__ == "__main__":
    image1_path = "/Users/linyinghsiao/Downloads/HW1/laptop_left.png"
    image2_path = "/Users/linyinghsiao/Downloads/HW1/laptop_right.png"
    merged_image_path = "/Users/linyinghsiao/Downloads/HW1/Q1/merged_image.png"

    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    merged_image = merge_images(image1, image2)

    cv2.imwrite(merged_image_path, merged_image)

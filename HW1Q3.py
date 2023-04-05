import cv2
import numpy as np

def bilinear_interpolation(image, new_width, new_height):
    height, width = image.shape[:2]
    resized_image = np.zeros((new_height, new_width, 3), dtype=np.uint8)

    x_ratio = float(width - 1) / (new_width - 1)
    y_ratio = float(height - 1) / (new_height - 1)

    for y in range(new_height):
        for x in range(new_width):
            x_src = x * x_ratio
            y_src = y * y_ratio

            x1, y1 = int(x_src), int(y_src)
            x2, y2 = min(x1 + 1, width - 1), min(y1 + 1, height - 1)

            x_diff = x_src - x1
            y_diff = y_src - y1

            # Apply bilinear interpolation
            pixel = (1 - x_diff) * (1 - y_diff) * image[y1, x1] + \
                    x_diff * (1 - y_diff) * image[y1, x2] + \
                    (1 - x_diff) * y_diff * image[y2, x1] + \
                    x_diff * y_diff * image[y2, x2]

            # Assign the interpolated pixel value to the resized image
            resized_image[y, x] = pixel

    return resized_image

if __name__ == "__main__":
    input_image_path = "/Users/linyinghsiao/Downloads/HW1/lena.bmp"
    output_image_path = "/Users/linyinghsiao/Downloads/HW1/Q3/resized_lena.bmp"
    new_width, new_height = 1024, 1024

    input_image = cv2.imread(input_image_path)
    resized_image = bilinear_interpolation(input_image, new_width, new_height)
    cv2.imwrite(output_image_path, resized_image)


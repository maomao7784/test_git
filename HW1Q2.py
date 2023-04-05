import cv2
import numpy as np

def rotate_image(image, angle):
    height, width = image.shape[:2]
    center = (width // 2, height // 2)

    # Create a rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

    # Calculate the new dimensions of the image
    cos_angle = np.abs(rotation_matrix[0, 0])
    sin_angle = np.abs(rotation_matrix[0, 1])
    new_width = int(height * sin_angle + width * cos_angle)
    new_height = int(height * cos_angle + width * sin_angle)

    # Adjust the rotation matrix to consider the translation
    rotation_matrix[0, 2] += (new_width / 2) - center[0]
    rotation_matrix[1, 2] += (new_height / 2) - center[1]

    # Perform the rotation using the rotation matrix
    rotated_image = cv2.warpAffine(image, rotation_matrix, (new_width, new_height))

    return rotated_image

def main():
    # Load the image
    image = cv2.imread("/Users/linyinghsiao/Downloads/HW1/Q1/merged_image.png", cv2.IMREAD_UNCHANGED)

    # Rotate the image
    rotated_image = rotate_image(image, -15)  # Negative angle for clockwise rotation

    # Save the rotated image
    cv2.imwrite("/Users/linyinghsiao/Downloads/HW1/Q2/rotated_image.png", rotated_image)

if __name__ == "__main__":
    main()

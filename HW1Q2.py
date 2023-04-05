import math
from PIL import Image

def rotate_image(image, angle):
    angle_radians = math.radians(angle)
    cos_angle = math.cos(angle_radians)
    sin_angle = math.sin(angle_radians)

    width, height = image.size
    new_width = int(abs(width * cos_angle) + abs(height * sin_angle))
    new_height = int(abs(width * sin_angle) + abs(height * cos_angle))

    rotated_image = Image.new("RGBA", (new_width, new_height), (0, 0, 0, 0))

    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))

            new_x = int((x - width / 2) * cos_angle - (y - height / 2) * sin_angle + new_width / 2)
            new_y = int((x - width / 2) * sin_angle + (y - height / 2) * cos_angle + new_height / 2)

            if 0 <= new_x < new_width and 0 <= new_y < new_height:
                rotated_image.putpixel((new_x, new_y), pixel)

    return rotated_image

if __name__ == "__main__":
    input_path = "/Users/linyinghsiao/Downloads/HW1/Q1/combined_image.png"
    output_path = "/Users/linyinghsiao/Downloads/HW1/Q2/rotated_image.png"

    image = Image.open(input_path).convert("RGBA")
    rotated_image = rotate_image(image, 15)  # Rotate 15 degrees clockwise

    rotated_image.save(output_path)
    print(f"Rotated image saved at {output_path}")
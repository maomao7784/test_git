from PIL import Image
def merge_images(image1, image2):
    width1, height1 = image1.size
    width2, height2 = image2.size

    merged_width = width1 + width2
    merged_height = max(height1, height2)

    merged_image = Image.new("RGBA", (merged_width, merged_height))

    for y in range(merged_height):
        for x in range(merged_width):
            if x < width1:
                pixel1 = image1.getpixel((x, y))
                pixel = pixel1
            elif x - width1 < width2 and y < height2:
                pixel2 = image2.getpixel((x - width1, y))
                pixel = pixel2
            else:
                pixel = (0, 0, 0, 0)
            merged_image.putpixel((x, y), pixel)

    return merged_image

if __name__ == "__main__":
    image1_path = "/Users/linyinghsiao/Downloads/HW1/laptop_left.png"
    image2_path = "/Users/linyinghsiao/Downloads/HW1/laptop_right.png"
    output_path = "/Users/linyinghsiao/Downloads/HW1/Q1/combined_image.png"
    
    image1 = Image.open(image1_path).convert("RGBA")
    image2 = Image.open(image2_path).convert("RGBA")

    merged_image = merge_images(image1, image2)
    merged_image.save(output_path)

    print(f"Merged image saved at {output_path}")
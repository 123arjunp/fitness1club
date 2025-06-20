# Redesign the image to preserve content clarity while making it more vertical
# We'll keep the original width and increase the height proportionally without squeezing

# Define the new height for better verticality (e.g., double the current height)
new_height = image.height * 1.5
new_size = (image.width, int(new_height))

# Resize with appropriate scaling
redesigned_image = image.resize(new_size, Image.LANCZOS)

# Save the updated image
redesigned_image_path = "/mnt/data/more_vertical_image.jpg"
redesigned_image.save(redesigned_image_path)

redesigned_image.show()  # Display the updated image for verification
redesigned_image_path  # Provide the path for downloading

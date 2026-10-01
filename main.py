import cv2

# Image path input
image_path = input("Image ka path likho: ")

# Image read
img = cv2.imread(image_path)

# Check image
if img is None:
    print("Image nahi mili!")
    exit()

# Text input
text = input("Image par kya likhna hai? ")

# Color input
print("\nColors:")
print("red")
print("green")
print("blue")
print("white")
print("black")

color_name = input("Color choose karo: ").lower()

# Colors in BGR format
colors = {
    "red": (0, 0, 255),
    "green": (0, 255, 0),
    "blue": (255, 0, 0),
    "white": (255, 255, 255),
    "black": (0, 0, 0)
}

color = colors.get(color_name, (255, 255, 255))

# Text position
x = int(input("X position: "))
y = int(input("Y position: "))

# Font
font = cv2.FONT_HERSHEY_SIMPLEX

# Write text
cv2.putText(
    img,
    text,
    (x, y),
    font,
    1,
    color,
    2,
    cv2.LINE_AA
)

# Show image
cv2.imshow("Result", img)

# Save image
cv2.imwrite("output.jpg", img)

print("Image save ho gayi: output.jpg")

cv2.waitKey(0)
cv2.destroyAllWindows()
COLOR_OF_CODE = {
    "aliceblue": "#F0F8FF",
    "antiquewhite": "#FAEBD7",
    "aqua": "#00FFFF",
    "aquamarine": "#7FFFD4",
    "azure": "#F0FFFF",
    "beige": "#F5F5DC",
    "bisque": "#FFE4C4",
    "black": "#000000",
    "blanchedalmond": "#FFEBCD",
    "blue": "#0000FF"
}

while True:
    color_name = input("Enter a color name: ").lower()
    if color_name in COLOR_OF_CODE:
        print(COLOR_OF_CODE[color_name])
    else:
        print("Invalid color name")

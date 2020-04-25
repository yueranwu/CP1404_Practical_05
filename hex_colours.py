"""
CP1404 Practical 05
This program create a dictionary for hex colours
When the user enters the name of the color, it returns the code of that colour
"""

HEX_COLOURS = {"LightPink": "#ffb6c1", "LightSkyBlue": "#87cefa", "moccasin": "#ffe4b5", "pale": "#db7093",
               "purple": "#a020f0", "salmon": "	#fa8072", "SandyBrown": "#f4a460", "seashell1": "#fff5ee",
               "SpringGreen1": "#00ff7f", "orange1": "#ffa500"}

colour_name = input("Enter a colour: ")
while colour_name != "":
    if colour_name in HEX_COLOURS:
        print(HEX_COLOURS[colour_name])
    else:
        print("Invalid Colour")
    colour_name = input("Enter a colour: ")

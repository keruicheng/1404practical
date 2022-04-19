name = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
        "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
        "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6", "aquamarine4": "#458b74", "azure1": "#f0ffff"}
print(name)
input_color = input("Enter the color: ")
while input_color != "":
    if input_color in name:
        print('The code of the color {} is {}'.format(input_color, name.get(input_color)))
    else:
        print("Invalid color name")
    input_color = input("Enter the color: ")
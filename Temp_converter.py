def tempconverter(cent):
    if cent < -273.75:
        Far='Invalid Temp'
    else:
        Far=(cent*9/5)+32
    return str(Far)

print(tempconverter(-360))

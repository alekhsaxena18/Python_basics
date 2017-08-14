def tempconverter(temperature):
    farhen=list()
    for temp in temperature:
        if temp < -273.75:
            Far=("invalid Temp")
        else:
            Far=(temp*9/5)+32
        farhen.append(Far) 
    return farhen

temper=[10,-20,-289,100,50]

print(tempconverter(temper))

temperature=[10,-20,-289,100]

for t in temperature:
    if t > -273.75:
        with open("temp.txt","a+") as file:
            file.write(str(t*9/5+32)+"\n")

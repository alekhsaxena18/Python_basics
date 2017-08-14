l=['line1','line2']
file=open("writeFile.txt",'w')
for item in l:
    file.write(item +"\n")
file.close()

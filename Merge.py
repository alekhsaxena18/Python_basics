import datetime
import glob2

now=datetime.datetime.now().strftime("%Y-%m-%d")+".txt"

with open(now,'w') as new:
    new.write('')

filenames=glob2.glob("file*.txt")
for file in filenames:
    with open(file,'r') as content:
        with open(now,'a') as new:
            new.write(content.read()+"\n")

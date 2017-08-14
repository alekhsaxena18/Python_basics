import string,random,re

size=[]
output=[]

vowels='aeiou'
letter=string.ascii_lowercase
const=re.sub("[a,e,i,o,u]","",letter)

wordsize=int(input("enter size: "))

for x in range(0,wordsize):
    size.insert(x,input("enter letter: "))

def gen():
    for y in range(0,len(size)):
        if size[y] == 'v':
            output.insert(y,random.choice(vowels))
        elif size[y] == 'c':
            output.insert(y,random.choice(const))
        elif size[y] == 'l':
            output.insert(y,random.choice(letter))
        else:
            output.insert(y,str(size[x]))
    return output


for i in range(0,int(input("Numer of names: "))):
    x=re.sub('[^a-z]','',str(gen()))
    print(x)
    output=[]

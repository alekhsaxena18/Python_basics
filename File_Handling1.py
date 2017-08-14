file =open("example.txt",'r')
content=file.readlines()
print(content)
content1=[i.rstrip("\n") for i in content]
print(content1)

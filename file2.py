f = open("sample.txt",'r')
data = f.read(5)
print(data) #here the function only reads 5 characters of the file
f.close()
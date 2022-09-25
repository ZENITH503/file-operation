#readline fucntion allows to print and read more than one line in the txt file
f = open("sample.txt")
#reads the first line
data=f.readline()
print(data)
#reads the second line
data=f.readline()
print(data)
f.close()
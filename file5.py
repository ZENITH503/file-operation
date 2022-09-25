  #with statement fucntion helps to open and close the file automatically
with open("sample.txt",'r') as f:
    a=f.read()
    print(a) 
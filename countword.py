f = open("C:\\Users\\amits\\python course\\text.txt","r")

def reword (str):
    low_str=str.lower()
    new_str=low_str[::-1]
    return new_str

def countword (txt):
    count=1
    lst=[]
    for line in f:
        data = line.split()
        lst.append(data)
        word1=lst[0]
        for i in data:
            new_data=reword(i).split()
            if new_data == word1:
               count=count+1
    print(count)

countword(f)

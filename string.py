string=input("please type any string : ")
c=input("please type the character to check frequency : ")
count=0
for i in string:
    if i==c:
        count+=1
print("Number", c, "in your word : ",count )    
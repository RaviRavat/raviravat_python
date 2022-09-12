s=input("Enter String:")
count=0
space_count=0
for i in s:
    count+=1
    if i.isspace():
        space_count+=1
print("Total Character is : ",count)
print("Total Space:",space_count)
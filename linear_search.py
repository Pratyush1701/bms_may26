def linear_search(elements,search_ele):
    for i in range(len(elements)):
        if elements[i]==search_ele:
            return i
    return -1 

elements=[]
n=int(input("Enter no of elements:"))
for i in range (n):
    element=float(input(""))
    elements.append(element)
search_ele=float(input("Enter the element to be searched:"))

a=linear_search(elements,search_ele)
if a==-1:
    print(f"{search_ele} is not found")
else:
    print(f"{search_ele} is found at {a+1} position")

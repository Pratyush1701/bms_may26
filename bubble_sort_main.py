import bubble_sort as bs

elements=[]
n=int(input("Enter the no of elements:"))
for i in range(n):
    element=float(input(""))
    elements.append(element)
    
print(f"Unsorted list is: {elements}:")  

bs.bubble_sort_optimize(elements,n)
bs.bubble_sort(elements,n)
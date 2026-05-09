def bubble_sort_optimize(elements,n):
    for i in range(n-1):
        sorted=True
        for j in range(n-i-1):
            if elements[j] > elements[j+1]:
                elements[j] , elements[j+1] = elements[j+1] , elements[j]
                sorted=False
        if sorted:
            break
    print(f"sorted list is: {elements}") 


def bubble_sort(elements,n):
    for i in range(n-1):
        for j in range(n-i-1):
            if elements[j] > elements[j+1]:
                elements[j] , elements[j+1] = elements[j+1] , elements[j]
    print(f"sorted list is: {elements}")

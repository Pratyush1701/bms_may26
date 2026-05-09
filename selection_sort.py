def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

       
        arr[i], arr[min_index] = arr[min_index], arr[i]


    return arr
    
arr=[]
n=int(input("Enter no of terms:"))
for i in range(n):
    x=float(input(""))
    arr.append(x)
print(f"unsorted_arr is: {arr}")
print(f"sorted arr is: {selection_sort(arr)}")
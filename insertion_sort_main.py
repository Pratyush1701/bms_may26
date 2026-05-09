import insertion_sort as ins_sort
import sys

numbers=[]

for i in range(1,len(sys.argv)):
    numbers.append(float(sys.argv[i]))
print("Numbers before sorting: \n", numbers)
print("Number after sorting:",)
print(ins_sort.insertion_sort(numbers))


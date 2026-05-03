# find largest element in a list

arr = [1, 2, 12, 33, 53, 122, 121]

largest = arr[0]

for num in arr:
    if num > largest:
        largest = num

print("Largest Element is", largest)        

        
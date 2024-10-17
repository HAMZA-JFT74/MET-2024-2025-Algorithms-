#Section 2

def selection_sort(arr):
    Size = len(arr)
    for i in range(Size):
        min_index = i
        for j in range(i+1, Size):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Step {i+1}: {arr}")

num = int(input("Enter the number of elements: "))
arr = []

print("Enter the elements one by one:")
for _ in range(num):
    element = int(input())
    arr.append(element)

selection_sort(arr)
print("Sorted array:", arr)

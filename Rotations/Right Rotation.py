#Basic Right Rotation of an Array by 1 position
arr = list(map(int, input("Enter the elements using space: ").split()))
last = arr[-1]
for i in range(len(arr)-1, 0, -1):
  arr[i] = arr[i-1]
print(arr)

#Example:
#Input: [1,2,3,4,5]
#Output: [5,1,2,3,4]

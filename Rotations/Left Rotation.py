#Basic Left Rotation of an Array by 1 position
arr = list(map(int, input("Enter the elements using space: ").split()))
first = arr[0]
for i in range(len(arr)):
  arr[i] = arr[i+1]
print(arr)

#Example: 
#Input: [1,2,3,4,5]
#Output: [2,3,4,5,1]

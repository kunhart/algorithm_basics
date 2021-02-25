#Insertion Sort Example
#
#A simple example of insertion sort.  
#Input: an array A of n integers
#Output: array A with the same n integers, sorted in increasing order

def insertionsort(A):
	#Sort each element of the array, starting with the second
	for j in range(len(A)):
		#Set the element to be sorted as the key and the compared integer to i
		key = A[j]
		i = j - 1
		#While the key is less than i or we've reached the end of the array, move i forward 1 spot and decrement i
		while i >= 0 and A[i] > key:
			A[i + 1] = A[i]
			i = i - 1
		#Place the key into its appropriate place sorted
		A[i + 1] = key
	return A

#Testing insertionsort
A = [5,2,36,4,7,75,34,9,105,-6,-20,40]
print ("Unsorted array: ", A)
A = insertionsort(A)
print ("Sorted array: ", A)

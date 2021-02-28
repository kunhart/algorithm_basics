#MergeSort

#A mergesort example. A classic example of a divide-and-conquer approach to an algorithm. 
#It works by dividing up the input array of unsorted integers into halves recursively until there are only arrays of 1 or 2 elements.
#It then combines each pair of halves into a sorted whole, starting from base case up each level of recursion.
#Input: an array A of n integers
#Output: array A with the same n integers, sorted in increasing order

def mergesort(A):
	length = len(A)
	if length > 1: #if array length is 1, then it is sorted.  Only sort if its greater than 1
		mid = length // 2
		#create left and right halves of the input array
		left = A[:mid]
		right = A[mid:]
		#recursive step to merge left and right subarrays
		mergesort(left)
		mergesort(right)
		#create pointers for input, left, and right array
		p = q = r = 0
		#sort the elements into the input until left or right is empty
		while p < len(left) and q < len(right):
			if left[p] < right[q]:
				A[r] = left[p]
				p = p + 1
			else:
				A[r] = right[q]
				q = q + 1
			r = r + 1
		#add remaining elements of left or right to the input
		if p < len(left):
			A[r:] = left[p:]
		else:
			A[r:] = right[q:]

#Testing mergesort
A = [96, 14, 25, 96, 76, 30, 36, 47, 20, 16, 79, 67, 45, 59, 26, 35, 12, 68, 2, 30, 14, 69, 38, 89, 15, 1, 71, 21, 71, 7, 77, 61]
print ("Unsorted array: ", A)
mergesort(A)
print ("Sorted array: ", A)

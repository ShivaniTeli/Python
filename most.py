# python program for the above approach

# Function to count the number of
# elements common in both the arrays
def countEqual(A, B, N):

	# variable to store answer
	ans = 0
	
	# first loop for array A
	for i in range(N):
	
		# This loop to find array A element in B
		for j in range(N):
		
			# if found then increase count and exit the loop
			if A[i] == B[j]:
				ans += 1
				break
	return ans

# driver code
A = [1, 3, 4, 6, 7, 9]
B = [1, 2, 4, 5, 9, 10]
N = len(A)
print(countEqual(A, B, N))

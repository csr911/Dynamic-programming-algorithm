# Python3 program to find longest alternating subsequence in an array

# Function to return max of two numbers


def Max(a, b):

	if a > b:
		return a
	else:
		return b

# Function to return longest alternating subsequence length


def zzis(arr, n):
	"""las[i][0] = Length of the longest alternating subsequence ending at index i and last element is greater than its previous element
	 las[i][1] = Length of the longest alternating subsequence ending at index i and last element is smaller than its previous element"""
	las = [[0 for i in range(2)]
		for j in range(n)]

	# Initialize all values from 1
	for i in range(n):
		las[i][0], las[i][1] = 1, 1

	# Initialize result
	res = 1

	# Compute values in bottom up manner
	for i in range(1, n):

		# Consider all elements as
		# previous of arr[i]
		for j in range(0, i):

			# If arr[i] is greater, then
			# check with las[j][1]
			if (arr[j] < arr[i] and
					las[i][0] < las[j][1] + 1):
				las[i][0] = las[j][1] + 1

			# If arr[i] is smaller, then
			# check with las[j][0]
			if(arr[j] > arr[i] and
			las[i][1] < las[j][0] + 1):
				las[i][1] = las[j][0] + 1

		# Pick maximum of both values at index i
		if (res < max(las[i][0], las[i][1])):
			res = max(las[i][0], las[i][1])

	return res


# Driver Code
arr = [10, 22, 9, 33, 49, 50, 31, 60]
n = len(arr)

print("Length of Longest alternating subsequence is",
	zzis(arr, n))

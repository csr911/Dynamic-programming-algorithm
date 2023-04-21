# Dynamic-programming-algorithm

Dynamic programming is a technique in Analysis of Design and Algorithm. Dynamic Programming is a paradigm of algorithm design in which an optimization problem is solved by a combination of achieving sub-problem solutions and appearing to the "principle of optimality". Dynamic programming is a technique that breaks the problems into sub-problems, and saves the result for future purposes so that we do not need to compute the result again. The subproblems are optimized to optimize the overall solution is known as optimal substructure property. The main use of dynamic programming is to solve optimization problems. Here, optimization problems mean that when we are trying to find out the minimum or the maximum solution of a problem. The dynamic programming guarantees to find the optimal solution of a problem if the solution exists.

The definition of dynamic programming says that it is a technique for solving a complex problem by first breaking into a collection of simpler subproblems, solving each subproblem just once, and then storing their solutions to avoid repetitive computations.

# Longest-Alternating-Subsequence
This script returns the longest possible subsequence of the input array where each element is different than the one preceding it.

To achieve this, the function first initializes an empty output list and a variable x set to None. It then loops over each element in the input array and checks whether the current element is not equal to the previous element (stored in x). If the current element is not equal to the previous element, it is appended to the output list and x is updated to the current element. If the current element is equal to the previous element, the loop continues to the next element.

# Follow the below steps to solve the problem:

Let A is given an array of length N 
We define a 2D array las[n][2] such that las[i][0] contains the longest alternating subsequence ending at index i and the last element is greater than its previous element 
las[i][1] contains the longest alternating subsequence ending at index i and the last element is smaller than its previous element, then we have the following recurrence relation between them,  
las[i][0] = Length of the longest alternating subsequence 
                  ending at index i and last element is greater
                  than its previous element

las[i][1] = Length of the longest alternating subsequence 
                  ending at index i and last element is smaller
                  than its previous element

# Recursive Formulation:

   las[i][0] = max (las[i][0], las[j][1] + 1); 
                  for all j < i and A[j] < A[i] 
                  
The first recurrence relation is based on the fact that, If we are at position i and this element has to be bigger than its previous element then for this sequence (upto i) to be bigger we will try to choose an element j ( < i) such that A[j] < A[i] i.e. A[j] can become A[i]’s previous element and las[j][1] + 1 is bigger than las[i][0] then we will update las[i][0]. 
Remember we have chosen las[j][1] + 1 not las[j][0] + 1 to satisfy the alternate property because in las[j][0] the last element is bigger than its previous one and A[i] is greater than A[j] which will break the alternating property if we update. So above fact derives the first recurrence relation, a similar argument can be made for the second recurrence relation also. 

# Kadane's-Algorithm

Kadane's algorithm is a dynamic programming algorithm(It is an iterative dynamic programming algorithm) used to find the maximum subarray sum in an array of integers. The algorithm has a time complexity of O(n) and works by iterating over the array and keeping track of the maximum sum seen so far and the maximum sum ending at the current index. At each iteration, the maximum sum ending at the current index is either the current number or the sum of the current number and the maximum sum ending at the previous index. The maximum sum seen so far is updated if the maximum sum ending at the current index is greater than the maximum sum seen so far. By the end of the iteration, the maximum sum seen so far is the maximum subarray sum of the given array.

# How the code works
This code defines a function called max_subarray_sum which takes an array arr as input. It finds the maximum sum subarray in the given array and prints the subarray, the sum of the subarray, and the starting and ending indices of the subarray.

The function initializes four variables max_so_far, max_ending_here, starting_index, and ending_index to negative infinity, negative infinity, 0 and 0 respectively. It then iterates through the array using a for loop and updates max_ending_here and max_so_far at each step.

For each element of the array, the function checks if adding that element to max_ending_here would result in a larger sum. If it does, then it updates max_ending_here. Otherwise, it sets max_ending_here to the current element. It then checks if the new value of max_ending_here is greater than the current value of max_so_far, and updates max_so_far and the starting and ending indices of the subarray accordingly.

Finally, the function prints the input array, the maximum subarray, its sum, and the starting and ending indices of the subarray. The input array used in the example is [-2, 1, -3, 4, -1, 2, 1, -5, 4].

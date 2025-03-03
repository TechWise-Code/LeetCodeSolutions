# Iterative Approach
class Solution:
    def generate(self, n: int) -> List[List[int]]:
        # Base case: if n is 0, return the first row of Pascal's triangle
        if n == 0:
            return [[1]]

        # Initialize the triangle with the first row
        answer = [[1]]
        
        # Generate each row of Pascal's triangle
        for i in range(2, n + 1):
            # Create a new row with 'i' elements, initialized to 0
            new_row = [0] * i
            # The first and last elements of each row are always 1
            new_row[0] = 1
            new_row[-1] = 1

            # Fill in the interior elements of the row
            for j in range(1, i - 1): # Skip first and last element
                new_row[j] = answer[-1][j] + answer[-1][j - 1]

            # Append the new row to the triangle
            answer.append(new_row)

        return answer

# Recursive Approach
class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n == 1:  # Base case: if n is 1, return the first row of Pascal's triangle
            return [[1]]

        prev_tri = self.generate(n-1)  # Recursive case: generate Pascal's triangle for n-1
        last_row = prev_tri[-1]  # Get the last row from the previous triangle
        new_row = [1] * n  # Initialize the new row with 1s
        for i in range(1, n-1):  # Fill in the interior elements of the new row
            new_row[i] = last_row[i-1] + last_row[i]
        
        prev_tri.append(new_row)  # Append the new row to the triangle
        return prev_tri  # Return the updated triangle

# Recursive Approach with Memoization
class Solution():
    def generate(self, n: int, cache={}): # Create cache
        if n in cache: # Check if n in cache
            return cache[n]
        if n == 1: # base case (n >= 1)
            return [[1]]

        prev_tri = self.generate(n-1) # recursive case
        last_row = prev_tri[-1] # last row, from recurisve call
        new_row = [1] * n
        for i in range(1, n-1): # Every element, except for the first and the last
            new_row[i] = last_row[i-1] + last_row[i]
            print(new_row,)
        
        prev_tri.append(new_row) # append new row
        cache[n] = prev_tri # Add n and the triangle to the cache
        return prev_tri

  # Optimized Iterative Approach
  class Solution:
    def generate(self, n):
        if n == 1:  # Base case: if n is 1, return the first row of Pascal's triangle
            return [[1]]

        tri = [[1]]  # Initialize the triangle with the first row
        for _ in range(n-1):  # Generate the next n-1 rows
            prev_row = tri[-1]  # Get the last row from the triangle
            new_row = [1] * (len(prev_row) + 1)  # Initialize the new row with 1s
            for i in range(1, len(new_row) - 1):  # Fill in the interior elements of the new row
                new_row[i] = prev_row[i-1] + prev_row[i]

            tri.append(new_row)  # Append the new row to the triangle
        return tri  # Return the complete triangle

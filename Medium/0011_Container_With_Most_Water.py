# Basic Approach (Brute Force)
def maxArea(height):
    max_area = 0
    n = len(height)
    
    for i in range(n):
        for j in range(i + 1, n):
            # Calculate width between lines
            width = j - i
            # The height is limited by the shorter line
            current_height = min(height[i], height[j])
            # Calculate the area
            area = width * current_height
            # Update max_area if current area is larger
            max_area = max(max_area, area)
    
    return max_area

# Intermediate Approach (Two Pointers) 
def maxArea(height):
    left = 0
    right = len(height) - 1
    max_area = 0
    
    while left < right:
        # Calculate width between lines
        width = right - left
        # The height is limited by the shorter line
        current_height = min(height[left], height[right])
        # Calculate the area
        area = width * current_height
        # Update max_area if current area is larger
        if area > max_area:
            max_area = area
        
        # Move the pointer of the shorter line inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

# Optimal Approach (Two Pointers, shorter)
def maxArea(height):
    left = 0
    right = len(height) - 1
    max_area = 0
    
    while left < right:
        # Calculate width between lines
        width = right - left
        # Calculate area directly using the shorter height
        max_area = max(max_area, width * min(height[left], height[right]))
        
        # Move the pointer of the shorter line inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

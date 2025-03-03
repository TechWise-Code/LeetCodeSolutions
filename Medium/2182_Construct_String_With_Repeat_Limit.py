from collections import Counter
import heapq

def repeatLimitedString(s: str, repeatLimit: int) -> str:
    result = []
    last = None

    while heap:
        # Get character with highest value
        ord_val, count = heapq.heappop(heap)
        char = chr(-ord_val)
        
        # Add characters up to limit
        chars_to_add = min(count, repeatLimit if not result or result[-1] != char else 1) 
        result.extend([char] * chars_to_add)

        remaining = count - chars_to_add
        if remaining > 0: # If there are more letters to add.. 
            if last: # Add last if it exists
                heapq.heappush(heap, last)
            last = (ord_val, remaining) # assign value to last
        elif last: # Simply add last
            heapq.heappush(heap, last)
            last = None

    return "".join(result)

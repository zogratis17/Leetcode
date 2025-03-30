class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        prev_value = 0  # Keep track of the previous value
        
        for char in reversed(s):  # Traverse from right to left
            curr_value = roman_dict[char]
            
            if curr_value < prev_value:  # If smaller value precedes a larger one
                total -= curr_value
            else:
                total += curr_value
                
            prev_value = curr_value  # Update previous value
        
        return total

        # Time : O(N)
        # Space : O(1)
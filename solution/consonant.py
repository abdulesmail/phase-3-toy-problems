def solve(s):
    vowels = "aeiou"
    
    def get_consonant_value(substring):
        return sum(ord(char) - ord('a') + 1 for char in substring)

    max_value = 0
    current_value = 0

    for char in s:
        if char not in vowels:
            current_value += ord(char) - ord('a') + 1
        else:
            max_value = max(max_value, current_value)
            current_value = 0

    
    # Check the last subsrting, if it's a consonant substring
    max_value = max(max_value, current_value)

    return max_value


# Examples
print(solve("software"))    
print(solve("development"))   
print(solve("element")) 
print(solve("character"))  



    
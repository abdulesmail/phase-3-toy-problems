# Define a function that counts the number of postive integers among 'a', 'b', 'c', and returns 'True' if the count is exactly 2 and 'false' otherwise
def exactly_two_positive(a, b, c):
    positive_count = 0

    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1

    return positive_count == 2

# Examples
print(exactly_two_positive(5, -9, 7))
print(exactly_two_positive(3, 6, 9))  
print(exactly_two_positive(8, 5, -9))   
print(exactly_two_positive(2, 6, -3))   
print(exactly_two_positive(-6, -3, 8))  
print(exactly_two_positive(9, -7, -4))
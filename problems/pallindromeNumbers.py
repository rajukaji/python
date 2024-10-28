def generate_palindromes(start, end):
    return [i for i in range(start, end+1) if i <= end and str(i) == str(i)[::-1]]

print(generate_palindromes(24, 1999))
# Intuition

In Python, the easiest way would be:

```python
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))
```

Many languages have similar libraries (like Java's `BigInteger`), but using these built-in solutions doesn't demonstrate understanding of the underlying algorithm.

To show how multiplication actually works at the digit level, we'll implement long multiplication, the manual multiplication method we learn in school.

In long multiplication, we multiply each digit of one number by each digit of the other number, keeping track of the position (place value) and handling carries.

For example, when multiplying `123 × 456`:

```text
    123
  × 456
  -----
    738  (123 × 6 = 738)
   615   (123 × 5 = 615, shifted left by 1 place)
  492    (123 × 4 = 492, shifted left by 2 places)
  -----
  56088  (Sum of all partial products)
```

# Approach

This solution simulates the long multiplication algorithm:

1. Handle the edge case where either number is "0"

2. Convert string digits to integers and process from right to left

3. Multiply each digit of `num2` with each digit of `num1`

4. Handle carries properly using `divmod()`

5. Convert the result back to string format

# Complexity

- Time complexity: `O(m × n)` where m and n are the lengths of num1 and num2

- Space Complexity: `O(m + n)` for the result array

# Code

```python3
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Handle zero case
        if num1 == '0' or num2 == '0':
            return "0"
    
        # Convert num1 to integers, reversed for easier processing
        num1_list = [ord(i) - 48 for i in reversed(num1)]
        
        # Result array to store multiplication
        result = [0] * (len(num1) + len(num2))
        
        # Multiply each digit of num2 with each digit of num1
        for idx, i in enumerate(reversed(num2)):
            curr = idx
            for j in num1_list:
                result[curr] += (ord(i) - 48) * j
                # Handle carry
                k, result[curr] = divmod(result[curr], 10)
                result[curr + 1] += k
                curr += 1
        
        # Convert back to string and remove leading zeros
        return ''.join(chr(i + 48) for i in reversed(result)).lstrip('0')
```

# Key Points

- ASCII conversion: `ord(i) - 48` converts string digits to integers and `chr(i + 48)` converts int to string.

- Processes numbers from right to left (least significant digit first)

- The result array size is `len(num1) + len(num2)` to handle maximum possible length

- `divmod()` efficiently handles both the digit value and carry in one operation

- `lstrip('0')` removes leading zeros from the final result

# 文檔連結

[點我](https://leetcode.com/problems/multiply-strings/solutions/6857541/python3-long-multiplication-solution-without-int-str/)

# Introduction

The linear search algorithm is used to find an element within a list.

In this algorithm, we sequentially check each element of the list until the desired element is found.

Suppose we have the following list, and we have to find the index of element 4 (the target value).


In linear search, we sequentially check each index to see if the target value (in this case, element 4) is present. We start from index 0, then index 1, index 2, and so on, until the element is found.

In this particular case, the target value is at index 5. Once this element is found, the linear search ends.


# Time Complexity for Linear Search

Best Case Complexity: O(1)

If the element is at the beginning of the list, the time complexity is O(1).

Worst Case Complexity: O(n)

If the element is at the last index or if the element is not present in the list, the time complexity is O(n).

Average Case Complexity: O(n)

The average case is when the element can be at any index. It can be at 1, 2, 3, …, n index.

Average case = sum of all possible cases / no. of cases
             = (1 + 2 + 3 + 4… + n) / n
             = n (n + 1)/ 2 * (1 / n)
             = O((n + 1) / 2)
             ≈ O(n)    
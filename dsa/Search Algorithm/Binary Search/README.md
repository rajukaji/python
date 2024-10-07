# Introduction 

Similar to linear search, binary search is used to find an element within a list.

However, unlike linear search, binary search can only be implemented in a sorted list. If the elements in the list are unsorted, we need to sort the elements first.

Next, we will explore the workings of binary search.


# Binary Search Time Complexity

Best Case Complexity: O(1)

If the target element is in the middle of the array, we find the element on the first check. In this case, the time complexity is O(1).

Average Case Complexity: O(log n)

Binary search continually narrows down the search space in half with each iteration (or recursive call).

Therefore, the average time complexity is O(log n).

Worst Case Complexity: O(log n)

The worst case occurs if the target is found in the last search (or recursive call) before low exceeds high. The time complexity in this scenario is also O(log n).

The average time complexity of linear search is O(n), whereas the average time complexity of binary search is O(log n).

Therefore, binary search is significantly faster than linear search. However, a limitation of binary search is that it can only be applied to sorted lists.
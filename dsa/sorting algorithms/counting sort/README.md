# Introduction

Counting sort is a way to arrange the items in a list by counting how many times each item appears. We then put the elements in order based on those counts.

Let's learn the workings of counting sort next

# Time Complexity

Best Case Complexity: O(n + max)

The best-case scenario occurs when the numbers in the input list are uniformly distributed and have a relatively small range.

Counting each element's occurrence in the input list takes O(n) time.

The accumulation step for the counting list takes O(max) time, where max is the maximum element.

Finally, creating the sorted output list by placing each element takes O(n) time.

Therefore, the best-case time complexity is O(n + max).

Worst Case Complexity: O(n + max)

The worst-case scenario is the same as the best case, as counting sort's time complexity is not affected by the order of the input elements.

Even if the numbers are not uniformly distributed or the range is larger, the time complexity remains O(n + max).

Average Case Complexity: O(n + max)

Counting sort's average-case time complexity is also O(n + max), as it depends on the number of elements and the range of elements in the input list.


# Space Complexity
The space complexity of counting sort is O(max). The larger the range of elements, the larger the space complexity.
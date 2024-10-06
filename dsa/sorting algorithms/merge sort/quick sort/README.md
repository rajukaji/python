# Introduction to Quick Sort
The quick sort algorithm selects a random element of the list as the pivot and partitions the remaining elements into two sublists: those less than the pivot and those greater than the pivot.

The sublists are then sorted recursively.

Next, we will visualize the working of quick sort using images.

1. Select the pivot element.

There are several variations of quick sort depending on what element is selected as the pivot.

It is important to pick a good pivot element for the fast implementation of quick sort. A pivot can be:

The first element
The last element
The middle element
Any random element from the list
We'll use the last element as our pivot element:

2. Rearrange the list.

Now, the elements that are smaller than the pivot are put on the left, and the elements larger than the pivot are put on the right.

3. Divide the sublists.

We choose pivot elements again for the left and right sublists separately, and then we repeat step 2.

4. Sort and merge the sublists.

First, we sort and merge the divided elements left to the initial pivot. Then, we do the same to the divided elements to the right of the pivot.

This leaves us with two sorted sublists.

Finally, we merge the left sublist, the pivot, and the right sublist to get the final sorted list.

# Time Complexity

As recursion is used in quick sort, we need to use the master theorem to find its complexity.

To learn more about how the master theorem is used in calculating the time complexity of recurrence relations, refer to our Complexity Calculation course.

Best Case: O(n log n)
Average Case: O(n log n)
Worst Case: O(n2)


Note: The worst-case scenario occurs when the pivot selection leads to unbalanced partitions. But this can be prevented with proper pivot selection techniques.


# Space Complexity
The space complexity for quick sort is O(log n).

This is due to the maximum depth of the recursion tree, which is determined by the number of times the input list can be divided in half.

Applications of Quick Sort
When to use quick sort?

Use quick sort for quickly sorting large datasets. It's efficient and works best when dealing with diverse data.

# When not to use quick sort?

Avoid quick sort if you need a sorting algorithm that maintains the order of equal elements. Also, quick sort can be slow in worst-case scenarios.

Therefore, if worst-case time complexity is important, consider using merge sort instead.


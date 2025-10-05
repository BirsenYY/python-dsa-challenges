def removeElement_1(self, nums: list[int], val: int) -> int:
        '''
       Time Complexity: O(n) average, O(n²) worst-case
       Space Complexity: O(1)
       Removes all occurrences of `val` in-place by swapping with last valid element.
       Order of remaining elements may change.
       '''
        m = len(nums)
        if m == 0:
            return 0
        last = m - 1
        for i in range(0, m):
            if nums[i] == val:
                while nums[last] == val and last > 0:
                    last -= 1
                if last <= i:
                    return i
                print(f"last: {last}, i: {i}, nums: {nums}")   
                nums[i] = nums[last]
                nums[last] = val
            last -= 1
        return last + 1

def removeElement_2(self, nums: list[int], val: int) -> int:
    """
    Removes all occurrences of a given value from the list in-place.

    This function iterates through the list and overwrites elements equal to `val`
    with the next valid element, preserving the relative order of non-`val` elements.
    The operation is done in-place with O(1) extra space.

    Args:
        nums (List[int]): The input list of integers.
        val (int): The value to remove from the list.

    Returns:
        int: The number of elements remaining after removal (new length).

    Example:
        >>> nums = [3, 2, 2, 3]
        >>> k = removeElement(nums, 3)
        >>> k
        2
        >>> nums[:k]
        [2, 2]

    Time Complexity:
        O(n) — Each element is checked once.

    Space Complexity:
        O(1) — Uses constant extra space.
    """
    k = 0  # index for next valid element
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

if __name__ == "__main__":
    nums = [5, 5,5,5]
    val = 5
    k = removeElement_2(None, nums, val)
    print(k)  # Output: 2
    print(nums)  # Output: [2,2,_,_]
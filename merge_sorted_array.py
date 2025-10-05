def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    '''
        Problem: Merge Sorted Array
        
        Description:
            Merge two sorted integer arrays, nums1 and nums2, into a single 
            sorted array in-place within nums1.
        
        Time Complexity:  O(m + n)
            Each element in nums1 and nums2 is compared and placed exactly once.
        
        Space Complexity: O(1)
            The merge is done in-place without using extra data structures.
        
        Approach:
            - Initialize three pointers: i (end of nums1’s valid elements), 
              j (end of nums2), and k (end of total length).
            - Compare nums1[i] and nums2[j] from the back, placing the larger 
              at nums1[k].
            - Move pointers accordingly until all elements are merged.
    '''
    k = m + n - 1 
    i, j = m - 1, n - 1 
    while j >= 0: 
        print(f"i: {i}, j: {j}, k: {k}")
        print(f"nums1: {nums1}, nums2: {nums2}")
        take_from_nums1 = i >= 0 and nums1[i] > nums2[j] 
        nums1[k] = nums1[i] if take_from_nums1 else nums2[j] 
        i -= 1 if take_from_nums1 else 0 
        j -= 0 if take_from_nums1 else 1 
        k -= 1

if __name__ == "__main__":
    nums1 = [2,5,6,0,0,0]
    m = 3
    nums2 = [1,2,3]
    n = 3
    merge(None, nums1, m, nums2, n)
    print(nums1)  # Output: [1,2,2,3,5,6]
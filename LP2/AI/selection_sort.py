# ============================================
#  AI Practical - Greedy Algorithm
#  Application: Selection Sort
# ============================================

def selection_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        min_index = i  # Greedy: assume current is minimum
        
        # Find actual minimum in unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap minimum to correct position
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Pass {i+1}: {arr}")
    
    return arr


# ---- Main ----
arr = list(map(int, input("Enter numbers: ").split()))
print(f"\nOriginal : {arr}")
print("\n--- Sorting Steps ---")
sorted_arr = selection_sort(arr)
print(f"\nSorted   : {sorted_arr}")


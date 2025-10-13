"""
PERFORMANCE ANTI-PATTERN: O(n²) Algorithms
Risk: Exponential performance degradation with data size
Detection: Manual review, complexity analysis tools
Severity: Medium

This example shows an O(n²) algorithm where a nested loop could be
replaced with an O(n) solution using a hash map or dictionary.
"""

def find_duplicates_slow(data):
    """
    VULNERABLE: O(n²) nested loop approach
    """
    duplicates = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] == data[j] and data[i] not in duplicates:
                duplicates.append(data[i])
    return duplicates

def find_duplicates_fast(data):
    """
    FIXED: O(n) solution using dictionary
    """
    seen = {}
    duplicates = []
    
    for item in data:
        if item in seen:
            if item not in duplicates:
                duplicates.append(item)
        else:
            seen[item] = True
    
    return duplicates

def find_pairs_slow(target_sum, data):
    """
    VULNERABLE: O(n²) nested loop for finding pairs
    """
    pairs = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] + data[j] == target_sum:
                pairs.append((data[i], data[j]))
    return pairs

def find_pairs_fast(target_sum, data):
    """
    FIXED: O(n) solution using hash set
    """
    pairs = []
    seen = set()
    
    for num in data:
        complement = target_sum - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    
    return pairs

# Example usage
if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 1]
    target_sum = 9
    
    print("Duplicates (slow):", find_duplicates_slow(data))
    print("Duplicates (fast):", find_duplicates_fast(data))
    print("Pairs (slow):", find_pairs_slow(target_sum, data))
    print("Pairs (fast):", find_pairs_fast(target_sum, data))
"""
PERFORMANCE ANTI-PATTERN: Inefficient String Operations
Risk: Memory overhead, quadratic time complexity
Detection: Manual review, profiling tools
Severity: Medium

This example shows inefficient string operations where repeated
string concatenation in loops creates unnecessary memory overhead.
"""

def build_string_slow(items):
    """
    VULNERABLE: Repeated string concatenation in loop
    """
    result = ""
    for item in items:
        result += item + ", "  # Creates new string each time
    return result

def build_string_fast(items):
    """
    FIXED: Use list and join for efficient string building
    """
    return ", ".join(items)

def process_text_slow(text):
    """
    VULNERABLE: Multiple string operations in loop
    """
    words = text.split()
    result = []
    for word in words:
        # Multiple string operations per iteration
        processed = word.upper().replace("A", "X").replace("E", "Y")
        result.append(processed)
    return " ".join(result)

def process_text_fast(text):
    """
    FIXED: Minimize string operations and use efficient methods
    """
    # Use translation table for multiple character replacements
    translation_table = str.maketrans({'A': 'X', 'E': 'Y'})
    
    words = text.split()
    processed_words = []
    for word in words:
        # Single operation with translation table
        processed = word.upper().translate(translation_table)
        processed_words.append(processed)
    
    return " ".join(processed_words)

def format_data_slow(data):
    """
    VULNERABLE: Multiple format operations in nested loop
    """
    result = []
    for i, item in enumerate(data):
        row = []
        for j, value in enumerate(item):
            # Multiple format operations
            formatted = f"Row {i}, Col {j}: {value:08d}"
            row.append(formatted)
        result.append("\n".join(row))
    return "\n\n".join(result)

def format_data_fast(data):
    """
    FIXED: Pre-compute format strings and use efficient methods
    """
    # Pre-compute format strings
    format_str = "Row {}, Col {}: {:08d}"
    
    result = []
    for i, item in enumerate(data):
        # Use list comprehension and single format operation
        row = [format_str.format(i, j, value) for j, value in enumerate(item)]
        result.append("\n".join(row))
    
    return "\n\n".join(result)

# Example usage
if __name__ == "__main__":
    items = ["apple", "banana", "cherry", "date"]
    text = "A quick brown fox jumps over the lazy dog"
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    print("String building (slow):", build_string_slow(items))
    print("String building (fast):", build_string_fast(items))
    print("Text processing (slow):", process_text_slow(text))
    print("Text processing (fast):", process_text_fast(text))
    print("Data formatting (slow):", format_data_slow(data))
    print("Data formatting (fast):", format_data_fast(data))
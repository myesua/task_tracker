# Security and Performance Anti-Patterns

## Security Anti-Patterns

### 1. Insecure File Handling

**Pattern**: Direct file operations without validation or sanitization
**Risk**: Path traversal, information disclosure, data corruption
**Detection**: Bandit B108, B605
**Severity**: High

### 2. Weak Input Validation

**Pattern**: No validation of user input before processing
**Risk**: Injection attacks, data corruption, unexpected behavior
**Detection**: Bandit B105, B106
**Severity**: High

### 3. Hardcoded Secrets

**Pattern**: API keys, passwords, or sensitive data in source code
**Risk**: Credential exposure, unauthorized access
**Detection**: Bandit B105, B602
**Severity**: Critical

### 4. Insecure Deserialization

**Pattern**: Using unsafe deserialization methods
**Risk**: Remote code execution, object injection
**Detection**: Bandit B301, B302
**Severity**: Critical

### 5. Command Injection

**Pattern**: Using shell=True with user input
**Risk**: Remote code execution
**Detection**: Bandit B602
**Severity**: Critical

## Performance Anti-Patterns

### 1. O(n²) Algorithms

**Pattern**: Nested loops where O(n) solution exists
**Risk**: Exponential performance degradation with data size
**Detection**: Manual review, complexity analysis tools
**Severity**: Medium

### 2. Inefficient String Operations

**Pattern**: Repeated string concatenation in loops
**Risk**: Memory overhead, quadratic time complexity
**Detection**: Manual review, profiling tools
**Severity**: Medium

### 3. Unnecessary Database Queries

**Pattern**: N+1 query problem, repeated queries in loops
**Risk**: Database overload, slow response times
**Detection**: Database profiling, query analysis tools
**Severity**: High

### 4. Memory Leaks

**Pattern**: Objects not properly cleaned up, circular references
**Risk**: Memory exhaustion, crashes
**Detection**: Memory profiling tools, garbage collection analysis
**Severity**: High

### 5. Blocking Operations in Main Thread

**Pattern**: Synchronous I/O operations in main thread
**Risk**: Poor user experience, unresponsive applications
**Detection**: Code review, profiling tools
**Severity**: Medium

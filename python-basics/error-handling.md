# Python Exception Handling (`try-except-else-finally`) – Interview Notes

## Purpose

Exception handling prevents a program from crashing when an error occurs and allows you to handle errors gracefully.

## Syntax

```python
try:
    # Code that may cause an exception
except ExceptionType:
    # Handle the exception
else:
    # Runs only if no exception occurs
finally:
    # Always executes
```

---

## Execution Flow

1. **`try`**

   * Contains code that might raise an exception.
   * Python executes this block first.

2. **`except`**

   * Executes only if the specified exception occurs.
   * Multiple `except` blocks can handle different exceptions.

3. **`else`**

   * Executes only when **no exception** occurs in the `try` block.
   * Useful for code that should run after successful execution.

4. **`finally`**

   * Executes **every time**, whether an exception occurs or not.
   * Commonly used for cleanup (closing files, database connections, releasing resources).

---

## Code Explanation

```python
try:
    x = int(input("Enter the number = "))
    ans = 10 / x
except ZeroDivisionError:
    print("Can't divide by zero")
except ValueError:
    print("Invalid input value..")
else:
    print(f"Division Successful {ans}")
finally:
    print("End of file")
```

### Possible Outputs

### Case 1: Input = `2`

```
Division Successful 5.0
End of file
```

### Case 2: Input = `0`

```
Can't divide by zero
End of file
```

### Case 3: Input = `abc`

```
Invalid input value..
End of file
```

---

# Common Exceptions

| Exception           | Cause                              |
| ------------------- | ---------------------------------- |
| `ZeroDivisionError` | Division by zero                   |
| `ValueError`        | Invalid value (e.g., `int("abc")`) |
| `TypeError`         | Operation on incompatible types    |
| `IndexError`        | List index out of range            |
| `KeyError`          | Dictionary key not found           |
| `FileNotFoundError` | File does not exist                |

---

# Interview Questions

### 1. Why use exception handling?

* Prevents program crashes.
* Improves user experience.
* Allows graceful error recovery.

### 2. Difference between `except` and `finally`?

| `except`                           | `finally`        |
| ---------------------------------- | ---------------- |
| Runs only when an exception occurs | Runs always      |
| Handles errors                     | Performs cleanup |

---

### 3. Difference between `else` and `finally`?

| `else`                           | `finally`                     |
| -------------------------------- | ----------------------------- |
| Runs only if no exception occurs | Runs regardless of exceptions |

---

### 4. Can we have multiple `except` blocks?

**Yes.**

```python
try:
    ...
except ValueError:
    ...
except ZeroDivisionError:
    ...
```

---

### 5. Can we write `try` without `except`?

**Yes**, but it must have `finally`.

```python
try:
    print("Hello")
finally:
    print("Done")
```

---

### 6. Can we write `try` alone?

**No.** A `try` block must be followed by at least one of:

* `except`
* `finally`

---

# Execution Order

### No Exception

```
try
 ↓
else
 ↓
finally
```

### Exception Occurs

```
try
 ↓
except
 ↓
finally
```

---

# Best Practices

* Catch **specific exceptions** instead of using a generic `except`.
* Use `else` for code that should run only after successful execution.
* Use `finally` to release resources (files, sockets, database connections).
* Avoid empty `except:` blocks, as they hide unexpected errors.

---

# Interview One-Liners

* **`try`** → Code that may raise an exception.
* **`except`** → Handles specific exceptions.
* **`else`** → Executes only when no exception occurs.
* **`finally`** → Always executes, used for cleanup.
* **Order:** `try → except → else → finally`
* **One `try` can have multiple `except` blocks.`
* **`finally` executes even if `return`, `break`, or an exception occurs.**

```python
from typing import List, Optional, Dict, Union

def process_user_data(name: str, age: int, user_items: Optional[List[str]] = None) -> Dict[str, Union[str, int, List[str]]]:
    if user_items is None:
        user_items = []

    # Validate name
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Name must be a non-empty string.")

    # Validate age
    if not isinstance(age, int) or age < 0:
        raise ValueError("Age must be a non-negative integer.")

    # Sanitize the name to prevent injection vulnerabilities
    sanitized_name = ''.join(char for char in name if char.isalnum() or char.isspace())

    # Process user data
    user_items.append(sanitized_name)

    output = f"User {sanitized_name} is {age} years old."
    print(output)

    return {
        "name": sanitized_name,
        "age": age,
        "user_items": user_items
    }
```

### Markdown Explanation of Changes

1. **Changed Mutable Default Argument**:
   - The `items` parameter was renamed to `user_items` and set to `None` by default. This prevents the unintended accumulation of data across multiple calls by initializing a fresh list each time the function is invoked.

2. **Parameter Validation**:
   - Added checks to validate the type and value of `name` and `age`. If `name` is not a non-empty string or if `age` is not a non-negative integer, the function raises `ValueError`. This ensures that the function behaves predictably and only accepts valid data.

3. **Input Sanitization**:
   - Sanitized `name` to remove any characters that are not alphanumeric or spaces. This mitigates the risk of injection attacks by filtering out potentially harmful input.

4. **Type Hints**:
   - Added type hints for `name`, `age`, `user_items`, and the return type of the function to enhance code clarity and maintainability, following best practices for modern Python.

5. **Improved Readability**:
   - Renamed `items` to `user_items` to clarify its purpose, enhancing code self-documentation and alignment with PEP 8 recommendations for naming.

6. **Graceful Handling of Empty or Invalid Input**:
   - The function now properly raises errors for empty names and negative ages, addressing edge cases that could lead to misleading output or exceptions.

7. **Total Return Structure**:
   - The function returns a dictionary containing the processed name, age, and the updated list of valid user items. This approach allows for easier subsequent processing of results by the caller.

By implementing these refinements, the code has become more robust, secure, and maintainable while adhering to established Python coding standards.
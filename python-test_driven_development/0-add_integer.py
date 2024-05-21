def add_integer(a, b=98):
    """
    Adds two integers or floats. If the inputs are floats, they are cast to integers before addition.
    
    Args:
    a: The first number, must be an integer or float.
    b: The second number, must be an integer or float, defaults to 98.
    
    Returns:
    The integer sum of a and b.
    
    Raises:
    TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    
    # Cast to integers if they are floats
    a = int(a)
    b = int(b)
    
    return a + b

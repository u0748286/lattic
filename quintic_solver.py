import numpy as np

def solve_quintic(pairs):
    """
    Solves for the coefficients of a quintic polynomial given 6 pairs of (S, T).
    
    Args:
    pairs (list of tuples): A list of 6 pairs (S, T).

    Returns:
    np.ndarray: Coefficients of the quintic polynomial.
    """
    if len(pairs) != 6:
        raise ValueError("Exactly 6 pairs of (S, T) are required.")
    
    # Create the matrix and the vector for the linear system
    A = np.zeros((6, 6))
    b = np.zeros(6)
    
    for i, (S, T) in enumerate(pairs):
        for j in range(6):
            A[i, j] = T ** j
        b[i] = S
    
    # Solve the linear system
    coefficients = np.linalg.solve(A, b)
    
    return coefficients
'''
    # Example usage
    pairs = [
        (1, 0),
        (3, 1),
        (5, 2),
        (7, 3),
        (9, 4),
        (11, 5)
    ]

    coefficients = solve_quintic(pairs)
    print("Quintic polynomial coefficients:", coefficients)
'''
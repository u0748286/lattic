# Define the equations for the constraints
def constraints(vars,T , # Duration
d0, dot_d0, ddot_d0 , # Initial conditions
d1, dot_d1, ddot_d1   # Final conditions
):
    a0, a1, a2, a3, a4, a5 = vars
    eq1 = a0 - d0
    eq2 = a1 - dot_d0
    eq3 = a2 - ddot_d0 / 2
    eq4 = a0 + a1 * T + a2 * T**2 + a3 * T**3 + a4 * T**4 + a5 * T**5 - d1
    eq5 = a1 + 2 * a2 * T + 3 * a3 * T**2 + 4 * a4 * T**3 + 5 * a5 * T**4 - dot_d1
    eq6 = 2 * a2 + 6 * a3 * T + 12 * a4 * T**2 + 20 * a5 * T**3 - ddot_d1
    return [eq1, eq2, eq3, eq4, eq5, eq6]
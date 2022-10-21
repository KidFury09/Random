def quad_form():
    eqn = input("Enter the eqaution in <ax^2 + bx + c>: ")
    L = eqn.split("x")
    a = int(L[0])
    b = int(L[1][2:])
    c = int(L[2])

    return(quad_root(a, b, c))

def quad_root(a, b, c):
    D = b**2 - 4*a*c
    if D < 0:
        return "Roots of this eqaution don't exist"
    elif D == 0:
        return (-b + D**0.5)/2*a
    else:
        return (-b + D**0.5)/2*a, (-b - D**0.5)/2*a

print(quad_form())

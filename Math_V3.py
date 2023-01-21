from math import sin

def quad_form():
    eqn = input("Enter the eqaution in <ax^2 + bx + c>: ")
    L = eqn.split("x")
    a = float(L[0])
    b = float(L[1][2:])
    c = float(L[2])

    return(quad_root(a, b, c))

def quad_root(a, b, c):
    D = b**2 - 4*a*c
    if D < 0:
        return "Roots of this eqaution don't exist"
    elif D == 0:
        return (-b + D**0.5)/2*a
    else:
        return (-b + D**0.5)/2*a, (-b - D**0.5)/2*a

def vector_mag():
    v = input("Enter the form <ai + bj + ck>: ")
    s = ""
    l = list(v)

    for i in l:
        if i in "+-":
            s += " " # + i can be used for places where sing is neccessary
        elif i.isnumeric():
            s += i
    
    s = s.split()
    l = []

    for i in s:
        l.append(float(i))
    
    s = 0
    for i in l:
        s += i ** 2

    return s ** 0.5

def mag_cross_prod(m1, m2, a):
    return m1 * m2 * sin(a)

def matrix_mul(m1, m2): #[[x1,x2],[y1,y2]] works with sqaure matrix
    
    n1 = len(m1)
    arr1 = []
    arr2 = []

    for i in m1:
        arr1.append(i)

    for i in range(n1):
        l = []
        
        for j in m2:
            l.append(j[i])

        arr2.append(l)

    arr3 = []

    for i in range(n1):
        l = []
        
        for j in range(n1):
            x = arr1[i][j]  * arr2[i][j]
            l.append(x)

        arr3.append(l)

    result = []

    for i in arr3:
        t = 0
        
        for j in i:
            t += j
        
        result.append(t)

    return result

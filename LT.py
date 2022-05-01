import sympy
sympy.init_printing()

#Define Sympols
t, s = sympy.symbols('t, s')
a = sympy.symbols('a', real=True, positive=True)

f = sympy.exp(-a*t) #Define a function for test

print("Function: "+str(f)) #Display the function

#Use laplace tramsform
F = sympy.laplace_transform(f, t, s, noconds=True)
print("Transfomation: "+str(F)) #Print the function in laplace domain

#Define Laplace formula
def L(f):
    return sympy.laplace_transform(f, t, s, noconds=True)

#Define inverce Laplace formula
def invL(F):
    return sympy.inverse_laplace_transform(F, s, t)

#Define some sympols
omega = sympy.Symbol('omega', real=True)
exp = sympy.exp
sin = sympy.sin
cos = sympy.cos
#Make a list of bsics functions
functions = [
         1,
         t,
         exp(-a*t),
         t*exp(-a*t),
         t**2*exp(-a*t),
         sin(omega*t),
         cos(omega*t),
         1 - exp(-a*t),
         exp(-a*t)*sin(omega*t),
         exp(-a*t)*cos(omega*t),
         ]
#Print the List
print("\nList of basics fuctions: ")
print(functions)

#Print List after transfomation
print("\nThe transformations: (Note that {**} is {power})")
Fs = [L(f) for f in functions]
print(Fs)
#End of Program.
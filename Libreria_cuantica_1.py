"""libreria complejos presentada por Gabriel alejandro Silva Lozada """
import math
def sumaComplejos(a,b):
    return (a[0]+b[0],a[1]+b[1])

def restaComplejos(a,b):
    return (a[0]-b[0],a[1]-b[1])

def multiComplejos(a,b):
    real =(a[0]* b[0])-(a[1]* b[1])
    imaginaria = (a[0]* b[1])+(a[1]* b[0])
    return (real,imaginaria)

def divcomplejos(a,b):
    real = (a[0]* b[0]+a[1]* b[1])/(b[0]**2 + b[1]**2)
    imaginaria = (b[0]* a[0] - a[0]* b[1])/(b[0]**2 + b[1]**2)
    return (real, imaginaria)

def conjugadoComplejo(a):
    return (a[0],a[1]*-1)

def moduloComplejo(a):
    return (a[0]**2 + a[1]**2)**1/2

def carteAPolar(a):
    Ro = (a[0]**2 + a[1]**2)**1/2
    angulo = math.atan(a[1]/a[0])
    return (Ro,angulo)

def fase(a):
    angulo = math.atan(a[1]/a[0])
    return (angulo)

a = (3,4)

b = (5,1)

print("la suma es: ",sumaComplejos(a,b))
print("la resta es: ",restaComplejos(a,b))
print("la multiplicacion es: ",multiComplejos(a,b))
print("la division es: ",divcomplejos(a,b))
print("el conjugado de a es: ",conjugadoComplejo(a))
print("el modulo de a es: ",moduloComplejo(a))
print("el numero polar de a es: ",carteAPolar(a))
print("el angulo de a es: ",fase(a))
    


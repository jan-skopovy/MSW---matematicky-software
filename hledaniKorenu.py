import numpy as np
import datetime

def polynomialniFce(x, derive=0):
    """y=-x^3+3x^2 +x-3"""
    if derive == 0:
        return(-x**3 + 3*x**2 + x-3)
    else:
        return(-x**2 + 6*x +1)

def exponencialniFce(x, derive=0):
    """y=5^(3*x-2)-1"""
    if derive == 0:
        return(5**(3*x-2)-1)
    else:
        return(3*5**(3*x-2)*np.log(5))

def harmonickaFce(x, derive=0):
    """y=0.5*sin(2*pi*x + pi)"""
    if derive == 0:
        return(0.5*np.sin(2*np.pi*x+np.pi))
    else:
        return(-1*np.pi * np.cos(2*np.pi*x))

def puleniIntervalu(fce,a,b,p=0.001):
    """Metoda puleni intervalu: 
        (y=vstupni fce, interval od a, interval do b, presnost p=0.001)"""
    x0=0
    steps=0
    start_time = datetime.datetime.now()
    while((b-a)>p):
        steps+=1
        x0=(a+b)/2
        if((fce(a)*fce(x0))<0):
            b=x0
        else:
            a=x0
        #print(f'KROK: {steps}, x = {x0}, y = {fce(x0)}')
    return(f'Metoda půlení intervalu: KROK:{steps}. s výsledkem x = {x0} a časem: {datetime.datetime.now() - start_time}')

def metodaTecen(fce, x, p=0.001):
    """Metoda tečen: 
        (y=vstupni fce, interval od a, interval do b, presnost p=0.001)"""
    steps=0
    start_time = datetime.datetime.now()
    while(abs(fce(x))>p):
        steps+=1
        x = x - fce(x)/fce(x,derive=1) 
        #print(f'KROK: {steps}, x = {x}, y = {fce(x)}')
    return(f'Metoda tečen: KROK:{steps}. s výsledkem x = {x} a časem: {datetime.datetime.now() - start_time}')        

print("\n")
print("\n")
print(f'Polynomiální fce y=-x^3+3x^2 +x-3 na intervalu (a,b) s přesností p:')
print(puleniIntervalu(polynomialniFce,0,3,0.001))
print(metodaTecen(polynomialniFce,2,0.001))
print("\n")
print("\n")
print(f'Exponenciální fce y=-x^3+3x^2 +x-3 na intervalu (a,b) s přesností p:')
print(puleniIntervalu(exponencialniFce,0.1,1,0.001))
print(metodaTecen(exponencialniFce,1,0.001))
print("\n")
print("\n")
print(f'Harmonická fce y=0.5*sin(2*pi*x + pi) na intervalu (a,b) s přesností p:')
print(puleniIntervalu(harmonickaFce,0.3,0.7,0.001))
print(metodaTecen(harmonickaFce,0.7,0.001))
print("\n")
print("\n")

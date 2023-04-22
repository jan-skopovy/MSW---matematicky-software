import numpy as np
import datetime

def polynomialniFce(x):
    """int(0→2) (3x^3-2x+5)dx"""
    return(3*x**3 - 2*x + 5)

def harmonickaFce(x):
    """int(0→pi) 2*sin(x)dx"""
    return(2*(np.sin(x)))

def logaritmickaFce(x):
    """int(1→e) ln(x) dx """
    return(np.log(x))

def obdelnikovePravidlo(fce,a,b,n):
    start_time = datetime.datetime.now()
    middle=[] #pole pro stredy intervalu
    funkce=[] #pole pro součet funkčních hodnot
    krajni_bod=[] # pole int OD + krok
    krajni_bod.append(a)
    krok=(b-a)/(n)
    
    for i in range(1,n+1):   
        krajni_bod.append(krajni_bod[i-1]+krok)
        middle.append(krajni_bod[i]-krok/2)
        funkce.append(fce(middle[i-1]))

    y = (sum(funkce)) *krok
    return(print(f'Obdelníkové pravidlo: y = {y}, čas:{datetime.datetime.now()-start_time}, při {n} dílkách'))

def lichobeznikovePravidlo(fce,a,b,n):
    start_time = datetime.datetime.now()
    funkce=[] # obsahuje fce(krajnic_bod)
    krajni_bod=[] # pole int OD + krok
    krajni_bod.append(a)
    krok=(b-a)/n

    for i in range(1,n+1):
        krajni_bod.append(krajni_bod[i-1]+krok)
        funkce.append((fce(krajni_bod[i-1])+fce(krajni_bod[i]))/2)

    y = (sum(funkce))*krok
    return(print(f'Lichobeznikove pravidlo: y = {y}, čas: {datetime.datetime.now()-start_time}, při {n} dílkách'))

print("\n")
print("\n")
print(f'Polynomiální fce int(0→2) (3x^3-2x+5)dx: [analyticky y=18]')
obdelnikovePravidlo(polynomialniFce,0,2,10)
lichobeznikovePravidlo(polynomialniFce,0,2,10)
print("\n")
print("\n")
print(f'Harmonická fce int(0→pi) 2*sin(x)dx: [analyticky y=4]')
obdelnikovePravidlo(harmonickaFce,0,np.pi,10)
lichobeznikovePravidlo(harmonickaFce,0,np.pi,10)
print("\n")
print("\n")
print(f'Logaritmická fce int(1→e) ln(x) dx: [analyticky y=1]')
obdelnikovePravidlo(logaritmickaFce,1,np.e,10)
lichobeznikovePravidlo(logaritmickaFce,1,np.e,10)
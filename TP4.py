# TP4 
def ajoute(l,e):
    T=[0]*(len(l)+1)
    for i in range(0,len(l)):
        T[i]=l[i]
    T[len(l)]=e
    return T

def dichopos(l,e):
    deb=0
    fin=len(l)-1
    if e>l[deb]:
        return 0
    if e<l[fin]:
        return len(l)
    while deb+1<fin:
        milieu=(fin+deb)//2
        if e<=l[milieu]:
            deb=milieu
        else:
            fin=milieu
    if l[deb]==e:
        return deb
    if e>l[deb]:
        return deb
    return deb+1

def inserdicho(l,e):
    ind=dichopos(l,e)
    T=[]
    for i in range(0,ind):
        T=ajoute(T,l[i])
    T=ajoute(T,e)
    for i in range(ind,len(l)):
        T=ajoute(T,l[i])
    return T
    
def triinserdicho(l):
    T=[l[0]]
    for i in range(1,len(l)):
        T=inserdicho(T,l[i])
    return T

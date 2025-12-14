## TP 3 et début 4 BD
def retindice(T,e):
    if trie(T) == False:
        return 'Impossible tableau pas trié'
    else:
        deb = 0
        fin = len(T)-1
        if T[fin]>=e:
            if T[fin]==e:
                return True
            else :
                return fin +1
        if T[deb]<=e:
            if T[deb]==e:
                return True
            else :
                return deb
        while (deb +1)<fin:
            milieu =(fin +deb)//2
            if e <= T[milieu]:
                deb = milieu
            else:
                fin = milieu
        if e == T[deb]:
            return True
        else:
            return deb+1
        
def inser(l,e):
    if trie(l) == False:
        return 'impossible tableau pas trié'
    else :
        T = []
        if e>l[0]:
            T.append(e)
            return T + l
        if e <l[len(l)-1]:
            l.append(e)
            return l
        T.append(l[0])
        for i in range(1, len(l)):
            if e>= l[i-1] and e<l[i]:
                T.append(l[i])
                T.append(e)
            else:
                T.append(l[i])
        return T

def rdichotomie_indice(n,L):
    if trie(L)==True:
        debut = 0
        fin = len(L)-1
        if L(debut)<= n:
            return debut
        elif L[fin]>= n:
            return fin +1
        else:
            while debut +1 < fin:
                mid = (fin + debut)//2
                if L[mid]<=n:
                    fin = mid
                else : 
                    debut = mid
            if L[fin]<=n:
                return fin

def ajouter(T,a):
    L = [0]*(len(T)+1)
    for i in range(len(T)):
        L[i] = T[i]
    L[len(L)-1] = a
    return L

def rdichotomie_indice(n,L):
    if trie(L)==True:
        debut = 0
        fin = len(L)-1
        if L(debut)<= n:
            return debut
        elif L[fin]>= n:
            return fin +1
        else:
            while debut +1 < fin:
                mid = (fin + debut)//2
                if L[mid]<=n:
                    fin = mid
                else : 
                    debut = mid
            if L[fin]<=n:
                return fin
def insertion(i,n,L):
    T = [O]*(len(L)+1)
    for j in range(i):
        T[j]= L[j]
    for j in range(i,len(L)):
        T[j+1]= L[j]
    T[i]=n
    return T

def insertion_dichot(n,L):
    s = rdichotomie_indice(n,L)
    return insertion(s,n,L)


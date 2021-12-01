import numpy as py

# OPPGAVE 1

# metode push back legger element x inn på slutten av Teque-en
def push_back(teque,x):
    if (len(teque) == 0):
        teque[0] = x
    else:
        teque.append(x)

# metode push front legger elementet inn på første indeks i Teque
def push_front(teque, x):
    teque.insert(0,x)

# metode push middle legger elementet inn på midten av Teque-en, dette gjør
# vi ved å hente ut størrelsen av teque-en  deler på to for å finne riktig
# indeks å legge elementet på.
def push_middle(teque, x):
    if len(teque) == 0:
        teque.append(x)
    else:
        y = (int((len(A)+1)/2))
        teque.insert(y, x)

# metode get printer ut elementet på en gitt indeks.
def get(teque, i):
    print(teque[i])

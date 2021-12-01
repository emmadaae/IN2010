import math
# Oppgave 3: balanserte søketrær

# i denne oppgaven skal vi, gitt et sortet Array med heltall, printe ut
# elementene slik at hvis de blir plasert i et binært søketre på denne måten
# vil dette også være et balansert søketre.

def finn_slutt(end, balansert):
    while end > 0:
        if end in balansert:
            end -= 1
        else:
            return end
    return 0


def balansert_soketre(sortert_array):
    balansert = []

    start = 0
    slutt = (len(sortert_array)-1)

    while len(balansert) < len(sortert_array):
        if slutt - start == 1:
            if slutt not in balansert:
                balansert.append(slutt)
            if start not in balansert:
                balansert.append(start)
            start = min(balansert)
            slutt = finn_slutt(slutt, balansert)
            if slutt - start < 1:
                start = 0
            continue

        median = math.ceil((start + slutt)/2)
        start = median

        if slutt - start == 1:
            if slutt not in balansert:
                balansert.append(slutt)
            if start not in balansert:
                balansert.append(start)
            start = min(balansert)
            slutt = finn_slutt(slutt, balansert)
            if slutt - start < 1:
                start = 0
            continue

        balansert.append(median)

    return balansert

a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]

for i in balansert_soketre(a):
    print(a[i])

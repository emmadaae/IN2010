class Node:
    # lager en node klasse som holder orden på verdien til noden
    # og forelderen til noden
    def __init__(self, data):
        self._data = data
        self._forelder = None


def main():
    # l = [int(x.strip()) for i in sys.stdin.readlines() for x in i]

    sti = [] #liste for sti vi ha som return verdi

    #lager først en liste med node-objekter mellom 1 og 100
    Noder = [Node] * 101
    for i in range(101):
        Noder[i] = Node(i)
    nvd_node = Noder[int(input())] # setter nåværende node som noden på indeks av
    # verdien noden har
    sti.append(nvd_node._data) #legger verdi av denne noden til i stien
    while True:
        verdier = [int(x) for x in input().split()] # legger verdier i input i
        # en liste som integer
        forelder = verdier[0] # setter første element av input som forelder
        if forelder == -1: # hvis input -1 break
            break

        for i in range(1, len(verdier)):
            Noder[verdier[i]]._forelder = Noder[forelder] # setter forelder av
            # noder på verdi input gir som foreler variabel for node-objektene


    nvd_node = nvd_node._forelder # setter node vi er på til forelder av denne noden
    while nvd_node is not None: # while loop som kjører så
    # lenge nåværende node har en forelder
        sti.append(nvd_node._data) # legger node til i sti
        nvd_node = nvd_node._forelder # setter neste node som forelder av denne noden

    print(*sti, sep=" ") # printer ut verdiene i stien med mellomrom mellom
    # hver verdi


if __name__ == "__main__":
    main()

import pickle

filename = 'betalinger.pk'

fodboldtur ={}

def afslut():
    outfile = open(filename, 'wb')
    pickle.dump(fodboldtur, outfile)
    outfile.close()
    print("Programmet er afsluttet!")

def printliste():
    for item in fodboldtur.items():
        print(item)

def menu():
    print("MENU")
    print("1: se listen")
    print("2: redigere beløb")
    print("3: se hvem der mangler at betale det fulde beløb")
    print("4: Afslut program")

    valg = input("Indtast dit valg:")
    if (valg == '1'):
        printliste()
        menu()

    if (valg == '2'):
        printliste()
        Navn = input("hvem vil du ændre beløb på")
        if Navn in fodboldtur:
            beløb = int(input("hvor meget vil du ændre beløbet med?"))
            fodboldtur[Navn] += beløb
            menu()

        else:
            print("dette navn er ikke i listen tjek for stort bogstav")
            menu()

    if (valg == '3'):
        printliste()
        

        menu()

    if (valg == '4'):
        afslut()

infile = open(filename,'rb')
fodboldtur = pickle.load(infile)
infile.close()

menu()


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
    print("3: se hvor meget der mangler at blive betalt")
    print("4: Afslut program")
# lige oven over fortæller vi hvad der skal være med i vors menu
    valg = input("Indtast dit valg:")
    if (valg == '1'): # if statement hvis man vælger 1 i terminalen så skal den printe listen for holdet og menuen igen
        printliste()
        menu()

    if (valg == '2'):
        printliste()# den printe listen så du har et overbilk
        Navn = input("hvem vil du ændre beløb på") #her bliver der fortalt at den skal sige det som står i input parentesen hvis du vælger 2
        if Navn in fodboldtur:
            beløb = int(input("hvor meget vil du ændre beløbet med?"))
            fodboldtur[Navn] += beløb
            menu()

        else:
            print("dette navn er ikke i listen tjek for stort bogstav")
            menu()

    if (valg == '3'):
        sum = 0
        for key in fodboldtur.keys():
            sum += fodboldtur[key]
        print(sum-4500)

        menu()

    if (valg == '4'):
        afslut()

infile = open(filename,'rb')
fodboldtur = pickle.load(infile)
infile.close()

menu()


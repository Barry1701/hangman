expanses = []

def show_expanses(month):
    for expanse_ammount, expanse_type, expanse_month in expanses:
        if expanse_month == month:
            print(f"{expanse_ammount} - {expanse_type}")


def add_expanses(month):
    print()
    expanse_ammount = int(input("Podaj Kwote: "))
    expanse_type = input("Jedzienie, Dom, Rozrywka, Inny: ")

    expanse = (expanse_ammount, expanse_type, month)
    expanses.append(expanse)

def show_stats(month):
    total_ammount_this_month = sum(expanse_ammount for expanse_ammount, _, expanse_month in expanses if expanse_month == month)
    number_of_expanses_this_month = sum(1 for _, _, expanse_month in expanses if expanse_month == month)
    average_expanse_this_month = total_ammount_this_month / number_of_expanses_this_month
    total_ammount_all = sum(expanse_ammount for expanse_ammount, _, _  in expanses)
    average_expanse_all = total_ammount_all / len(expanses)
    

    
    print()
    print("Statystyki")
    print("Wszsytkie wydatki w tym miesiacu [$]: ", total_ammount_this_month)
    print("Sredni wydatek w tym miesiacu [$]: ", average_expanse_this_month)
    print("Wszsytkie wydatki [$]: ", total_ammount_all)
    print("Sredni wydatek [$]: ", average_expanse_all)


while True:
    print()
    month = int(input("Ktory miesiac wybierasz? [1-12] "))
    if month <= 0 or month > 12:
        break

    while True:
        print()
        print("0. Powrot do wyboru miesiaca")
        print("1. Wyswietl wszystkie wydatki")
        print("2. Dodaj wydatek")
        print("3. Statystyki")

        choice = int(input("Wybierz opcje: "))
        if choice == 0:
            break
     

        if choice == 1:

            show_expanses(month)

        if choice == 2:
            add_expanses(month)

        if choice == 3:
            show_stats(month)



        
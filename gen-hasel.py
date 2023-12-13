import sys
import random
import string

password = []
characters_left = -1

def update_characters_left(number_of_characters):
    global characters_left

    if number_of_characters < 0 or number_of_characters > characters_left:
        print("Liczba znakow spoza przedzialu 0,",characters_left)
        sys.exit(0)
    else:
        characters_left -= number_of_characters
        print("pozostalo znakow:", characters_left)


password_length = int(input("Jak dlugie ma byc haslo? "))

if password_length < 5:
    print("Haslo jest za krotkie!Minimum 5 znakow!")
    sys.exit(0)
else:
    characters_left = password_length


lowercase_letters = int(input("Ile malych liter ma miec haslo? "))

update_characters_left(lowercase_letters)

uppercase_letters = int(input("ile duzych liter ma miec haslo? "))

update_characters_left(uppercase_letters)

  
special_signs = int(input("Ile znakow specjalnych ma miec haslo? "))
update_characters_left(special_signs)

digits = int(input("Ile cyfr ma miec haslo? "))
update_characters_left(digits)

if characters_left > 0:
    print("Nie wszytkie pola zostaly wykozystane.Reszta zostanie uzupelniona cyframi")
    digits += characters_left
print()
print("Dlugosc Hasla:", password_length )
print("Male Litery:", lowercase_letters )
print("Duze Litery:", uppercase_letters)
print("Znaki Specjalne:", special_signs)
print("Cyfry:", digits)


for i in range(password_length):
    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase`
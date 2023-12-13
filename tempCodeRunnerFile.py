if lowercase_letters < 0 or lowercase_letters > characters_left:
    print("Liczba znakow spoza przedzialu 0,",characters_left)
    sys.exit(0)
else:
    characters_left -= lowercase_letters
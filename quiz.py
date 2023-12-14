import json

points = 0

def show_question(question):
    global points
    print()
    print(question["pytanie"])
    print("a", question["a"])
    print("b", question["b"])
    print("c", question["c"])
    print("d", question["d"])
    print()

    anwser = input("Jaka jest Twoja odpowiedz? ")

    if anwser == question["prawidlowa_odpowiedz"]:
        points += 1
        print()
        print("To prawidlowa Odpowiedz! Gratulacje! Masz juz", points, "punktow.")
    else:
        print()
        print("Niestety, Twoja odpowiez jest bledna. prawidlowa odpowiedz to", question["prawidlowa_odpowiedz"] + "." )

with open("quiz.json") as pytania_json:
    questions = json.load(pytania_json)


    for i in range(0, len(questions)):
        show_question(questions[i])

print()
print("Game Over. Liczba zdobytych punktow to:", str(points) + ".")

   


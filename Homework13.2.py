import datetime
import json
import random

class Result():
    def __init__(self, score, player_name, date):
        self.score = score
        self.player_name = player_name
        self.date = date

def likecontinue():
    ask = input("Möchten Sie nochmal Spielen? a = ja, b = nein: ")
    if ask == "a":
        secretnumber()
    else:
        print("bye")


with open("results.txt", "r") as results_file:  # Hier wird die score_list.txt Textdatei geöffnet

    results = json.loads(results_file.read())

    print(results)
player_name = input("Geben Sie bitte Ihren Namen ein: ")

def secretnumber():
    secret = random.randint(1, 30)
    attempts = 0


    while True:
        attempts += 1
        guess = input("Geben sie hier ihre Nummer ein: ")
        if secret == int(guess):

            theResults = Result(score=str(attempts), player_name=str(player_name), date=str(datetime.datetime.now()))
            results.append({"Versuche:": theResults.score, "Spielername:":theResults.player_name, "Datum:":theResults.date})
            with open("results.txt", "w") as results_file:
                results_file.write(json.dumps(results))
            print("Richtig")
            likecontinue()
            break

        elif secret > int(guess):
            print("bigger")


        elif secret < int(guess):
            print("smaller")

secretnumber()






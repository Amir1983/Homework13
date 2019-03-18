import json

class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds

class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards




def askReturn():
    wantContinue = input("Möchten sie fortfahren?: a = ja, b = nein")
    if wantContinue == "a":
        checkIn()
    else:
        print("bye")





def checkIn():
    while True:
        wichSport = input("In welcher Sportart sind Sie aktiv? : a = Basketball, b = Fußball, c = Beenden")

        if wichSport == "a":
            with open("basketball.txt", "r") as basketball_file:

                basketball = json.loads(basketball_file.read())
                print(basketball)
            personBasketball = BasketballPlayer(first_name=input("Please Enter your Firstname: "), last_name=input("Please Enter your last name: "), height_cm=input("Please Enter your height(cm): "), weight_kg=input("Please Enter your weight: "), points=input("Please Enter your points: "), rebounds=input("Please Enter your rebounds: "), assists=input("Please Enter your assists: "))
            basketball.append({"Vorname: ": personBasketball.first_name, "Nachname: ": personBasketball.last_name, "Groeße: ": personBasketball.height_cm, "Gewicht: ": personBasketball.weight_kg,"Punkte: ": personBasketball.points,"Rebound: ": personBasketball.rebounds,"geholfen: ": personBasketball.assists})

            with open("basketball.txt", "w") as basketball_file:
                basketball_file.write(json.dumps(basketball))
            askReturn()
            break


        elif wichSport == "b":
            with open("football.txt", "r") as football_file:

                football = json.loads(football_file.read())
                print(football)
            personFootball= FootballPlayer(first_name=input("Please Enter your Firstname: "), last_name=input("Please Enter your last name: "), height_cm=input("Please Enter your height(cm): "), weight_kg=input("Please Enter your weight: "), goals=input("Please Enter your goals: "), yellow_cards=input("Please Enter your yellow cards: "), red_cards=input("Please Enter your red cards: "))
            football.append({"Vorname: ": personFootball.first_name, "Nachname: ": personFootball.last_name, "Groeße: ": personFootball.height_cm, "Gewicht: ": personFootball.weight_kg,"Punkte: ": personFootball.goals,"Rebound: ": personFootball.yellow_cards,"geholfen: ": personFootball.red_cards})
            with open("football.txt", "w") as football_file:
                football_file.write(json.dumps(football))

            askReturn()
            break

        elif wichSport == "c":
            break

        else:
            break



checkIn()










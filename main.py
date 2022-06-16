import scenarios as scenarios
from colorama import Fore, Back, Style, init
import json
from random import *

print(Fore.RED + """
        Welcome to the Millionare Journey,
        """)
print(Fore.GREEN + """
        Bob, a 15 year-old, wants to make sure he doesn't go bankrupt.
        Your job is to help Bob choose the correct decisions so that he doesn't go bankrupt.
        If you get through all the options without going bankrupt, you win, as simple as that.
        """)

print(Fore.CYAN + """
        Whoops I forgot to tell you... You only get a single cent to start off with.""" + Fore.RED + """
        If you dip below $0.00 at any point during this game, game is over.
        """ + Fore.YELLOW +
        """Good Luck!""")

print(Fore.YELLOW + "----------------------------------------------------------------------------------------------------------------------")
print(Fore.YELLOW + "----------------------------------------------------------------------------------------------------------------------")

balance = 0.01

f = open('scenarios.json')
data = json.load(f)

print("")
print(Fore.RED + f"You have ${balance} in your account")

print("")
print("")

i = 0

for scenario in data["scenarios"]:
    if balance > 0:
      print(Fore.YELLOW + "Scenario Number " + str(scenario["scenario_number"]))
      print(scenario["scenario_name"])
      print(Fore.CYAN + scenario["scenario_description"])
      print("")
      print("")

      i = 0

      while i < 2:
        print(Fore.MAGENTA + f"Option {i+1}: ")
        print(Fore.MAGENTA + "    " + scenario["options"][i]["name"])
        print(Fore.MAGENTA + "    " + scenario["options"][i]["description"])
        input()
        print(Fore.MAGENTA + "        >> It costs $" + str(scenario["options"][i]["cost"]))
        input()
        print(
          Fore.MAGENTA + "        >> You can make up to " + str(scenario["options"][i]["possible_money_to_be_made"]))
        input()
        print(
          Fore.MAGENTA + "        >> You can lose up to " + str(scenario["options"][i]["possible_money_to_be_lost"]))
        input()
        print(Fore.MAGENTA + "        >> This requires " + scenario["options"][i]["time_required"] + " of time")
        input()
        i+=1

      print("")
      print(Fore.RED + "Which option would you like to choose")
      print(Fore.RED + f"You still have ${balance} left in your account")
      print(Fore.RED + "Type " + Fore.GREEN + "1 " + Fore.RED + "for option one or type " + Fore.YELLOW + "2 " + Fore.RED + "for option two")
      response = input(">> ")

      if str(response) == "1":

        money = int(randint(scenario["options"][0]["possible_money_to_be_lost"], scenario["options"][0]["possible_money_to_be_made"]))
        cost_op_1 = scenario["options"][0]["cost"]

        if money > 0:
          balance = balance - cost_op_1

          if balance > 0:
            print(f"You made ${str(money)}")
            balance = balance + money
            print(f"Your new balance is ${str(balance)}")

          if balance < 0:
            print("Sorry man you ran out of money")
            print("Good luck next time")
            input(
              Fore.WHITE + "Click " + Fore.BLUE + "ENTER" + Fore.WHITE + " to leave the game")
            quit()

        if money < 0:
          print(f"You lost ${str(money*-1)}")
          balance = balance - cost_op_1

          if balance > 0:
            balance = balance + money
            print(f"Your new balance is ${str(balance)}")

          if balance < 0:
            print("Sorry man you ran out of money")
            print("Good luck next time")
            input(
              Fore.WHITE + "Click " + Fore.BLUE + "ENTER" + Fore.WHITE + " to leave the game")
            quit()

    if str(response) == "2":
      money = int(randint((scenario["options"][1]["possible_money_to_be_lost"])*-1, scenario["options"][1]["possible_money_to_be_made"]))
      cost_op_2= scenario["options"][1]["cost"]

      if money > 0:
        balance = balance - cost_op_2

        if balance > 0:
          print(f"You made ${str(money)}")
          balance = balance + money
          print(f"Your new balance is ${str(balance)}")

        if balance < 0:
          print("Sorry man you ran out of money")
          print("Good luck next time")
          input(
            Fore.WHITE + "Click " + Fore.BLUE + "ENTER" + Fore.WHITE + " to leave the game")
          quit()

      if money < 0:
        print(f"You lost ${str(money*-1)}")
        balance = balance - cost_op_2

        if balance > 0:
          balance = balance + money
          print(f"Your new balance is ${str(balance)}")

        if balance < 0:
          print("Sorry man you ran out of money")
          print("Good luck next time")
          input(
            Fore.WHITE + "Click " + Fore.BLUE + "ENTER" + Fore.WHITE + " to leave the game")
          quit()


      input(Fore.WHITE + "Time to move on to the next scenario, click the " + Fore.BLUE + "ENTER" + Fore.WHITE + " key to move on!")
      print("")

    if balance < 0:
      print(Fore.RED + f"Sorry fam you are out of money")
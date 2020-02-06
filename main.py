
import time

import calendar

import locale

from datetime import datetime

from view.eventview import EventView

print("Bienvenue sur votre agenda personnel")

locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
currentyear = datetime.now().year
currentmonth = datetime.now().month

action = ""
while action != 'q':
    view = EventView()
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Nous sommes le : {}".format(datetime.today().strftime('%d %B %Y')))
    print("\n__________________________\n")

    print (calendar.month(currentyear, currentmonth, 2, 1))
    print("Que souhaitez vous faire ? (v: voir les evenements, a: supprimer évenement, n: ajouter evenement, m: modifier, s: mois suivant, p: mois précédent, q: quitter)")
    action = input("appuyer sur la touche correspondante : ")

    if action == "s":
        if currentmonth < 12:
            currentmonth += 1
        else:
            currentmonth = 1
            currenyear += 1
    elif action == "p":
        if currentmonth > 1:
            currentmonth -= 1
        else:
            currentmonth = 12
            currentyear -= 1
    elif action == "v":
        view.to_show_events()
    elif action == "n":
        view.new_event()
    elif action == "a":
        view.to_delete_event()
    elif action == "m":
        view.to_update_event()
    else:
        pass


print("Merci et au revoir")
time.sleep(3)
exit()

from model.eventmodel import EventModel

from model.event import Event

class EventView():
    """ """
    def __init__(self):
        model = EventModel()
        event = Event()

    def to_show_events(self):
        """ """
        date = input(" : ")
        events = self.model.show_events(date)
        print("\nVotre agenda du {}\n".format(date))
        if events:
            for event in events:
                print(event)
        else:
            print("Rien ce jour là, vous n'avez aucun rendez vous :-)")
        input("Tapez sur une touche pour continuer")

    def new_event(self):
        """ """
        event.title = input('Titre : ')
        event.description = input('Description : ')
        event.date = input('Date (jj/mm/aaaa) : ')
        event.time = input('Heure (hh:mm) : ')
        while self.model.display_one_event(event.date, event.time):
            print("Vous avez déjà un événement à cette heure  !")
            event.time = input('Nouvelle heure : ')
        self.model.add_event(event)

    def to_delete_event(self):
        """ """
        date = input("Jour de l'événement : ")
        hour = input("Heure de l'événement : ")
        self.model.delete_event(date, hour)

    def to_update_event(self):
        """ """

        choice = ""
        while choice != "s":
            date = input("Jour de l'événement : ")
            hour = input("Heure de l'événement : ")
            event = self.model.display_one_event(date, hour)
            if event : 
                break
            print("il y a rien a cette date")
            choice = input("Tapez s pour arrêter, n'importe quelle touche pour continuer")

        if event:
            print("Voici les informations enregistrées")

            while True:
                print(event)
                print("Tapez a pour arrêter")
                attribut = input("Attribut à modifier : ")
                if attribut == 'a' : 
                    break
                value = input("Nouvelle valeur : ")

                if attribut == "time":
                    while self.model.display_one_event(event.date, value):
                        print("Vous avez déjà un événement à cette heure !")
                        value = input('Nouvelle heure : ')



from model.connection import Connection

from model.event import Event

class EventModel():
    """Class to perform all queries related to the event table in the database"""

    def __init__(self):
        # Create a instance of the connection class to acces the database
        self.db = Connection()
    
    def show_events(self, date):
        """method to display all the events of the day """
        sql = "SELECT * FROM events WHERE date = %s;"
        self.db.initialize_connection()
        self.db.cursor.execute(sql, (date,))
        events = self.db.cursor.fetchall()
        self.db.close_connection()
        for key, value in enumerate(events):
            events[key] = Event(value)
        return events

    def display_one_event(self, date, time):
        """method to dislay one event  """
        sql = "SELECT * FROM events WHERE date = %s AND time = %s;"
        self.db.initialize_connection()
        self.db.cursor.execute(sql, (date, time))
        event = self.db.cursor.fetchone()
        self.db.close_connection()
        if event:
            return Event(event)
        return False

    def add_event(self, event):
        """ """
        sql = "INSERT INTO events(title, date, time, description) VALUES(%s, %s, %s, %s);"
        percent_s = (event.title, event.date, event.time, event.description )
        self.db.initialize_connection()
        self.db.cursor.execute(sql, percent_s)
        self.db.connection.commit()
        self.db.close_connection()

    def delete_event(self, date, time):
        """ """
        sql = "DELETE FROM events WHERE date = %s AND time = %s;"
        percent_s = (date, time)
        self.db.initialize_connection()
        self.db.cursor.execute(sql, percent_s)
        self.db.connection.commit()
        self.db.close_connection()

    def update_event(self,title, date, time, description, actual_date,actual_time):
        """ """
        sql = "UPDATE events SET title=%s, date=%s, time=%s, description = %s WHERE date = %s AND time = %s;"
        percent_s =(event.title, event.date, event.time, event.description, actual_date, actual_time)
        self.db.initialize_connection()
        self.db.cursor.execute(sql,percent_s)
        self.db.connection.commit()
        self.db.close_connection()
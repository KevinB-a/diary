from model.connection import Connection

class EventModel():
    """"""
     def __init__(self):
         """ """
        self.db = Connection()

    def show_events(self, date):
        """ """
        sql = "SELECT * FROM events WHERE date = %s;"
        self.db.initialize_connection()
        self.db.cursor.execute(sql, (date,))
        events = self.db.cursor.fetchall()
        self.db.close_connection()
        return events 

    def display_one_event(self):
        """ """
        sql = "SELECT * FROM events WHERE date = %s AND time = %s;"
        self.db.initialize_connection()
        self.db.cursor.execute(sql, (date, hour))
        event = self.db.cursor.fetchone()
        self.db.close_connection()
        if event:
            return Event(event)
        return False

    def add_event(self, event):
        """ """
        sql = "INSERT INTO events(title, date, time, description) VALUES(%s, %s, %s, %s);"
        values = (title, date, time, description )
        self.db.initialize_connection()
        self.db.cursor.execute(sql, values)
        self.db.connection.commit()
        self.db.close_connection()

    def delete_event(self, date, hour):
        """ """
        sql = "DELETE FROM events WHERE date = %s AND time = %s;"
        self.db.initialize_connection()
        self.db.cursor.execute(sql)
        self.db.connection.commit()
        self.db.close_connection()

    def update_event(self,event):
        """ """
        sql = "UPDATE events set title=%s, date=%s, time=%s, description = %s WHERE event_id=%s;"
        self.db.initialize_connection()
        self.db.cursor.execute(sql)
        self.db.connection.commit()
        self.db.close_connection()
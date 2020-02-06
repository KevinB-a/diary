from model.connection import Connection

class EventModel():
         """ """
    def __init__(self):
        """instantiating an object of the class connection """
        self.db = Connection()

    def show_events(self, date):
        """ """
        sql = "SELECT * FROM events WHERE date = %s;"
        self.db.initialize_connection()
        self.db.cursor.execute(sql, (date,))
        events = self.db.cursor.fetchall()
        self.db.close_connection()
        return events 

    def display_one_event(self, date, hour ):
        """ """
        sql = "SELECT * FROM events WHERE date = %s AND time = %s;"
        self.db.initialize_connection()
        self.db.cursor.execute(sql, (date, hour))
        event = self.db.cursor.fetchone()
        self.db.close_connection()

    def add_event(self, event):
        """ """
        sql = "INSERT INTO events(title, date, time, description) VALUES(%s, %s, %s, %s);"
        percent_s = (event.title, event.date, event.time, event.description )
        self.db.initialize_connection()
        self.db.cursor.execute(sql, percent_s)
        self.db.connection.commit()
        self.db.close_connection()

    def delete_event(self, date, hour)
        """ """
        sql = "DELETE FROM events WHERE date = %s AND time = %s;"
        percent_s = (date, time)
        self.db.initialize_connection()
        self.db.cursor.execute(sql, percent_s)
        self.db.connection.commit()
        self.db.close_connection()

    def update_event(self,event):
        """ """
        sql = "UPDATE events set title=%s, date=%s, time=%s, description = %s WHERE id_event=%s;"
        percent_s =(event.title, event.date, event.time, event.description, event.id_event)
        self.db.initialize_connection()
        self.db.cursor.execute(sql,percent_s)
        self.db.connection.commit()
        self.db.close_connection()
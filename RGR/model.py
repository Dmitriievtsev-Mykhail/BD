import psycopg2


class Model:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname='volunteer_management_system',
            user='postgres',
            password='1111',
            host='localhost',
            port=3000
        )

    def add_event(self, event_id, title, organizer, date_of_event):
        c = self.conn.cursor()
        c.execute('INSERT INTO events(event_id, title, organizer, date_of_event) VALUES(%s, %s, %s, %s);',
                  (event_id, title, organizer, date_of_event))
        self.conn.commit()

    def add_task(self, task_id, importance, event_id):
        c = self.conn.cursor()
        c.execute('INSERT INTO tasks(task_id, importance, event_id) VALUES(%s, %s, %s);',
                  (task_id, importance, event_id))
        self.conn.commit()

    def add_volunteer(self, volunteer_id, name, state_date_of_volunteering):
        c = self.conn.cursor()
        c.execute('INSERT INTO volunteers(volunteer_id, name, state_date_of_volunteering) VALUES(%s, %s, %s);',
                  (volunteer_id, name, state_date_of_volunteering))
        self.conn.commit()

    def add_volunteer_task(self, volunteer_task_id, volunteer_id, task_id):
        c = self.conn.cursor()
        c.execute('INSERT INTO volunteer_tasks(volunteer_task_id, volunteer_id, task_id) VALUES(%s, %s, %s);',
                  (volunteer_task_id, volunteer_id, task_id))
        self.conn.commit()

    def get_events(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM events;')
        return c.fetchall()

    def get_tasks(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM tasks;')
        return c.fetchall()

    def get_volunteers(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM volunteers;')
        return c.fetchall()

    def get_volunteer_tasks(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM volunteer_tasks;')
        return c.fetchall()

    def update_event(self, event_id, title, organizer, date_of_event, id):
        c = self.conn.cursor()
        c.execute('UPDATE events SET event_id=%s, title=%s, organizer=%s, date_of_event=%s WHERE event_id=%s',
                  (event_id, title, organizer, date_of_event, id))
        self.conn.commit()

    def update_task(self, task_id, importance, event_id, id):
        c = self.conn.cursor()
        c.execute('UPDATE tasks SET task_id=%s, importance=%s, event_id=%s WHERE task_id=%s',
                  (task_id, importance, event_id, id))
        self.conn.commit()

    def update_volunteer(self, volunteer_id, name, state_date_of_volunteering, id):
        c = self.conn.cursor()
        c.execute('UPDATE volunteers SET volunteer_id=%s, name=%s, state_date_of_volunteering=%s WHERE volunteer_id=%s',
                  (volunteer_id, name, state_date_of_volunteering, id))
        self.conn.commit()

    def update_volunteer_task(self, volunteer_task_id, volunteer_id, task_id, id):
        c = self.conn.cursor()
        c.execute('UPDATE volunteer_tasks SET volunteer_task_id=%s, volunteer_id=%s, task_id=%s WHERE volunteer_task_id=%s',
                  (volunteer_task_id, volunteer_id, task_id, id))
        self.conn.commit()

    def delete_event(self, event_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM events WHERE "event_id"=%s', (event_id,))
        self.conn.commit()

    def delete_task(self, task_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM tasks WHERE "task_id"=%s', (task_id,))
        self.conn.commit()

    def delete_volunteer(self, volunteer_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM volunteers WHERE "volunteer_id"=%s', (volunteer_id,))
        self.conn.commit()

    def delete_volunteer_task(self, volunteer_task_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM volunteer_tasks WHERE "volunteer_task_id"=%s', (volunteer_task_id,))
        self.conn.commit()

    def get_number_of_volunteers_for_each_event(self):
        c = self.conn.cursor()
        c.execute('SELECT e.event_id, e.title, COUNT(vt.volunteer_id) AS total_volunteers FROM events e JOIN volunteer_tasks vt ON e.event_id = vt.task_id GROUP BY e.event_id, e.title;')
        return c.fetchall()

    def get_volunteer_task_event(self):
        c = self.conn.cursor()
        c.execute('SELECT v.name AS volunteer_name, t.importance AS task_importance, e.title AS event_title FROM volunteers v JOIN volunteer_tasks vt ON v.volunteer_id = vt.volunteer_id JOIN tasks t ON vt.task_id = t.task_id JOIN events e ON t.event_id = e.event_id;')
        return c.fetchall()

    def get_upcoming_events(self):
        c = self.conn.cursor()
        c.execute('SELECT title AS event_title, date_of_event FROM events WHERE date_of_event >= CURRENT_DATE ORDER BY date_of_event LIMIT 5;')
        return c.fetchall()

    def add_random_fields(self, number):
        c = self.conn.cursor()
        c.execute("INSERT INTO events (event_id, title, organizer, date_of_event) SELECT row_number() OVER () + (SELECT COALESCE(MAX(event_id), 0) FROM events), chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int), chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int), '2023-01-01'::date + (random() * (365 * 10))::integer FROM generate_series(1, %s);",
                  (number,))
        self.conn.commit()
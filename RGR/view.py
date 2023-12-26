from datetime import datetime


class View:

    def show_menu(self):
        self.show_message("\nMenu:")
        self.show_message("1. Add row")
        self.show_message('2. Generating `randomized` data (only for "Events")')
        self.show_message("3. Show table")
        self.show_message("4. Update row")
        self.show_message("5. Delete row")
        self.show_message("6. Search")
        self.show_message("7. Exit")
        choice = input("Select your choice: ")
        return choice

    def show_tables(self):
        self.show_message("\nTables:")
        self.show_message("1. Events")
        self.show_message("2. Tasks")
        self.show_message("3. Volunteers")
        self.show_message("4. Volunteer Tasks")
        self.show_message("5. Back to menu")
        table = input("Select table: ")
        return table

    def show_search(self):
        self.show_message("\nSearch:")
        self.show_message("1. Number of volunteers for each event")
        self.show_message("2. Volunteer's name, task importance, and corresponding event title.")
        self.show_message("3. Events that will take place in the near future.")
        self.show_message("4. Back to menu")
        choice = input("Select something: ")
        return choice


    def show_events(self, events):
        print("\nEvents:")
        for event in events:
            print(f"Event ID: {event[0]}, Title: {event[1]}, Organizer: {event[2]}, Date of event: {event[3]}")

    def show_tasks(self, tasks):
        print("\nTasks:")
        for task in tasks:
            print(f"Task ID: {task[0]}, Importance: {task[1]}, Event ID: {task[2]}")

    def show_volunteers(self, volunteers):
        print("\nVolunteers:")
        for volunteer in volunteers:
            print(f"Volunteer ID: {volunteer[0]}, Name: {volunteer[1]}, State date of volunteering: {volunteer[2]}")

    def show_volunteer_tasks(self, volunteer_tasks):
        print("\nVolunteer Tasks:")
        for volunteer_task in volunteer_tasks:
            print(f"Volunteer task ID: {volunteer_task[0]}, Volunteer ID: {volunteer_task[1]}, Task ID: {volunteer_task[2]}")

    def get_event_input(self):
        while True:
            try:
                event_id = input("Enter event ID: ")
                if event_id.strip():
                    event_id = int(event_id)
                    break
                else:
                    print("Event ID cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                title = input("Enter title: ")
                if title.strip():
                    break
                else:
                    print("Title cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                organizer = input("Enter organizer: ")
                if organizer.strip():
                    break
                else:
                    print("Organizer cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                date_of_event = input("Enter date of event (YYYY-MM-DD): ")
                if date_of_event.strip():
                    datetime.strptime(date_of_event, "%Y-%m-%d")
                    break
                else:
                    print("Date of event cannot be empty.")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
        return event_id, title, organizer, date_of_event


    def get_task_input(self):
        while True:
            try:
                task_id = input("Enter task ID: ")
                if task_id.strip():
                    task_id = int(task_id)
                    break
                else:
                    print("Task ID cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                importance = input("Enter importance: ")
                if importance.strip():
                    break
                else:
                    print("Importance cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                event_id = input("Enter event ID: ")
                if event_id.strip():
                    event_id = int(event_id)
                    break
                else:
                    print("Event ID cannot be empty.")
            except ValueError:
                print("It must be a number.")
        return task_id, importance, event_id


    def get_volunteer_input(self):
        while True:
            try:
                volunteer_id = input("Enter volunteer ID: ")
                if volunteer_id.strip():
                    volunteer_id = int(volunteer_id)
                    break
                else:
                    print("Volunteer ID cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                name = input("Enter name: ")
                if name.strip():
                    break
                else:
                    print("Name cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                state_date_of_volunteering = input("Enter state date of volunteering (YYYY-MM-DD): ")
                if state_date_of_volunteering.strip():
                    datetime.strptime(state_date_of_volunteering, "%Y-%m-%d")
                    break
                else:
                    print("State date of volunteering cannot be empty.")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
        return volunteer_id, name, state_date_of_volunteering

    def get_volunteer_task_input(self):
        while True:
            try:
                volunteer_task_id = input("Enter volunteer task ID: ")
                if volunteer_task_id.strip():
                    volunteer_task_id = int(volunteer_task_id)
                    break
                else:
                    print("Volunteer task ID cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                volunteer_id = input("Enter volunteer ID: ")
                if volunteer_id.strip():
                    volunteer_id = int(volunteer_id)
                    break
                else:
                    print("Volunteer ID cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                task_id = input("Enter task ID: ")
                if task_id.strip():
                    task_id = int(task_id)
                    break
                else:
                    print("Task ID cannot be empty.")
            except ValueError:
                print("It must be a number.")
        return volunteer_task_id, volunteer_id, task_id

    def get_event_id(self):
        while True:
            try:
                id = int(input("Enter event ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    def get_task_id(self):
        while True:
            try:
                id = int(input("Enter task ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    def get_volunteer_id(self):
        while True:
            try:
                id = int(input("Enter volunteer ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    def get_volunteer_task_id(self):
        while True:
            try:
                id = int(input("Enter volunteer task ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    def show_number_of_volunteers_for_each_event(self, rows):
        print("\nNumber of volunteers for each event:")
        for row in rows:
            print(f"Event ID: {row[0]}, Title: {row[1]}, Total volunteers: {row[2]}")

    def show_volunteer_task_event(self, rows):
        print("\nVolunteer's name, task importance, and corresponding event title:")
        for row in rows:
            print(f"Volunteer name: {row[0]}, Task importance: {row[1]}, Event title: {row[2]}")

    def show_upcoming_events(self, rows):
        print("\nEvents that will take place in the near future:")
        for row in rows:
            print(f"Event title: {row[0]}, Date of event: {row[1]}")

    def show_message(self, message):
        print(message)

    def get_number(self):
        while True:
            try:
                number = int(input("Enter the number: "))
                break
            except ValueError:
                print("It must be a number.")
        return number
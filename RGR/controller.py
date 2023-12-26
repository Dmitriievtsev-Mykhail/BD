import time
from model import Model
from view import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        while True:
            choice = self.view.show_menu()

            if choice == '7':
                break
            if choice == '6':
                self.process_search_option()
            elif choice in ['1', '2', '3', '4', '5']:
                self.process_menu_choice(choice)
            else:
                self.view.show_message("Wrong choice. Try again.")

    def process_menu_choice(self, choice):
        while True:
            table = self.view.show_tables()

            if table == '6':
                break

            if choice == '1':
                self.process_add_option(table)
            elif choice == '2':
                self.process_add_random_option(table)
            elif choice == '3':
                self.process_view_option(table)
            elif choice == '4':
                self.process_update_option(table)
            elif choice == '5':
                self.process_delete_option(table)
            else:
                self.view.show_message("Wrong choice. Try again.")

    def process_add_option(self, table):
        if table == '1':
            self.view.show_message("\nAdding event:")
            self.add_event()
        elif table == '2':
            self.view.show_message("\nAdding task:")
            self.add_task()
        elif table == '3':
            self.view.show_message("\nAdding volunteer:")
            self.add_volunteer()
        elif table == '4':
            self.view.show_message("\nAdding volunteer task:")
            self.add_volunteer_task()
        elif table == '5':
            self.view.show_menu()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_add_random_option(self, table):
        if table == '1':
            self.view.show_message("\nAdding random events:")
            self.add_random_fields()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_view_option(self, table):
        if table == '1':
            self.show_events()
        elif table == '2':
            self.show_tasks()
        elif table == '3':
            self.show_volunteers()
        elif table == '4':
            self.show_volunteer_tasks()
        elif table == '5':
            self.view.show_menu()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_update_option(self, table):
        if table == '1':
            self.view.show_message("\nUpdating event:")
            self.update_event()
        elif table == '2':
            self.view.show_message("\nUpdating task:")
            self.update_task()
        elif table == '3':
            self.view.show_message("\nUpdating volunteer:")
            self.update_volunteer()
        elif table == '4':
            self.view.show_message("\nUpdating volunteer task:")
            self.update_volunteer_task()
        elif table == '5':
            self.view.show_menu()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_delete_option(self, table):
        if table == '1':
            self.view.show_message("\nDeleting event:")
            self.delete_event()
        elif table == '2':
            self.view.show_message("\nDeleting task:")
            self.delete_task()
        elif table == '3':
            self.view.show_message("\nDeleting volunteer:")
            self.delete_volunteer()
        elif table == '4':
            self.view.show_message("\nDeleting volunteer task:")
            self.delete_volunteer_task()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_search_option(self):
        option = self.view.show_search()

        if option == '1':
            start_time = time.time()
            self.show_number_of_volunteers_for_each_event()
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print(f"Execution time: {elapsed_time:.2f} msec")
        elif option == '2':
            start_time = time.time()
            self.show_volunteer_and_task_and_event()
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print(f"Execution time: {elapsed_time:.2f} msec")
        elif option == '3':
            start_time = time.time()
            self.show_upcoming_events()
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print(f"Execution time: {elapsed_time:.2f} msec")
        else:
            self.view.show_menu()

    def add_event(self):
        try:
            event_id, title, organizer, date_of_event = self.view.get_event_input()
            self.model.add_event(event_id, title, organizer, date_of_event)
            self.view.show_message("Event added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_task(self):
        try:
            task_id, importance, event_id = self.view.get_task_input()
            self.model.add_task(task_id, importance, event_id)
            self.view.show_message("Task added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_volunteer(self):
        try:
            volunteer_id, name, state_date_of_volunteering = self.view.get_volunteer_input()
            self.model.add_volunteer(volunteer_id, name, state_date_of_volunteering)
            self.view.show_message("Volunteer added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_volunteer_task(self):
        try:
            volunteer_task_id, volunteer_id, task_id = self.view.get_volunteer_task_input()
            self.model.add_volunteer_task(volunteer_task_id, volunteer_id, task_id)
            self.view.show_message("Volunteer Task added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def show_events(self):
        try:
            events = self.model.get_events()
            self.view.show_events(events)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def show_tasks(self):
        try:
            tasks = self.model.get_tasks()
            self.view.show_tasks(tasks)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def show_volunteers(self):
        try:
            volunteers = self.model.get_volunteers()
            self.view.show_volunteers(volunteers)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def show_volunteer_tasks(self):
        try:
            volunteer_tasks = self.model.get_volunteer_tasks()
            self.view.show_volunteer_tasks(volunteer_tasks)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_event(self):
        try:
            id = self.view.get_event_id()
            event_id, title, organizer, date_of_event = self.view.get_event_input()
            self.model.update_event(event_id, title, organizer, date_of_event, id)
            self.view.show_message("Event updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_task(self):
        try:
            id = self.view.get_task_id()
            task_id, importance, event_id = self.view.get_task_input()
            self.model.update_task(task_id, importance, event_id, id)
            self.view.show_message("Task updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_volunteer(self):
        try:
            id = self.view.get_volunteer_id()
            volunteer_id, name, state_date_of_volunteering = self.view.get_volunteer_input()
            self.model.update_volunteer(volunteer_id, name, state_date_of_volunteering, id)
            self.view.show_message("Volunteer updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_volunteer_task(self):
        try:
            id = self.view.get_volunteer_task_id()
            volunteer_task_id, volunteer_id, task_id = self.view.get_volunteer_task_input()
            self.model.update_volunteer_task(volunteer_task_id, volunteer_id, task_id, id)
            self.view.show_message("Volunteer Task updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_event(self):
        try:
            event_id = self.view.get_event_id()
            self.model.delete_event(event_id)
            self.view.show_message("Event deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_task(self):
        try:
            task_id = self.view.get_task_id()
            self.model.delete_task(task_id)
            self.view.show_message("Task deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_volunteer(self):
        try:
            volunteer_id = self.view.get_volunteer_id()
            self.model.delete_volunteer(volunteer_id)
            self.view.show_message("Volunteer deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_volunteer_task(self):
        try:
            volunteer_task_id = self.view.get_volunteer_task_id()
            self.model.delete_volunteer_task(volunteer_task_id)
            self.view.show_message("Volunteer Task deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def show_number_of_volunteers_for_each_event(self):
        try:
            number_of_volunteers = self.model.get_number_of_volunteers_for_each_event()
            self.view.show_number_of_volunteers_for_each_event(number_of_volunteers)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def show_volunteer_and_task_and_event(self):
        try:
            volunteer_task_event = self.model.get_volunteer_task_event()
            self.view.show_volunteer_task_event(volunteer_task_event)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def show_upcoming_events(self):
        try:
            rows = self.model.get_upcoming_events()
            self.view.show_upcoming_events(rows)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_random_fields(self):
        try:
            number = self.view.get_number()
            self.model.add_random_fields(number)
            self.view.show_message("Random fields added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")
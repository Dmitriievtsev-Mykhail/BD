from db import Base, Session, engine
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, Date

s = Session()


class Event(Base):
    __tablename__ = 'events'
    event_id = Column(Integer, primary_key=True)
    title = Column(String)
    organizer = Column(String)
    date_of_event = Column(Date)

    task = relationship("Task")

    def __init__(self, event_id, title, organizer, date_of_event):
        self.event_id = event_id
        self.title = title
        self.organizer = organizer
        self.date_of_event = date_of_event

    def __repr__(self):
        return f"<Events(event_id={self.event_id}, title={self.title}, organizer={self.organizer}, date_of_event={self.date_of_event})>"


class Task(Base):
    __tablename__ = 'tasks'
    task_id = Column(Integer, primary_key=True)
    importance = Column(String)

    event_id = Column(Integer, ForeignKey('events.event_id'), primary_key=True)

    volunteer_task = relationship("VolunteerTask")

    def __init__(self, task_id, importance, event_id):
        self.task_id = task_id
        self.importance = importance
        self.event_id = event_id

    def __repr__(self):
        return f"<Tasks(task_id={self.task_id}, importance={self.importance}, event_id={self.event_id})>"


class Volunteer(Base):
    __tablename__ = 'volunteers'
    volunteer_id = Column(Integer, primary_key=True)
    name = Column(String)
    state_date_of_volunteering = Column(Date)

    volunteer_task = relationship("VolunteerTask")

    def __init__(self, volunteer_id, name, state_date_of_volunteering):
        self.volunteer_id = volunteer_id
        self.name = name
        self.state_date_of_volunteering = state_date_of_volunteering

    def __repr__(self):
        return f"<Volunteers(volunteer_id={self.volunteer_id}, name={self.name}, state_date_of_volunteering={self.state_date_of_volunteering})>"


class VolunteerTask(Base):
    __tablename__ = 'volunteer_tasks'
    volunteer_task_id = Column(Integer, primary_key=True)
    volunteer_id = Column(Integer, ForeignKey('volunteers.volunteer_id'), primary_key=True)
    task_id = Column(Integer, ForeignKey('tasks.task_id'), primary_key=True)

    def __init__(self, volunteer_task_id, volunteer_id, task_id):
        self.volunteer_task_id = volunteer_task_id
        self.volunteer_id = volunteer_id
        self.task_id = task_id

    def __repr__(self):
        return f"<VolunteerTasks(volunteer_task_id={self.volunteer_task_id}, volunteer_id={self.volunteer_id}, task_id={self.task_id})>"


class Model:
    def __init__(self):
        self.session = Session()
        self.connection = engine.connect()

    def insert_event(self, event_id: int, title: str, organizer: str, date_of_event: Date) -> None:
        event = Event(event_id=event_id, title=title, organizer=organizer, date_of_event=date_of_event)
        s.add(event)
        s.commit()

    def insert_task(self, task_id: int, importance: str, event_id: int) -> None:
        task = Task(task_id=task_id, importance=importance, event_id=event_id)
        s.add(task)
        s.commit()

    def insert_volunteer(self, volunteer_id: int, name: str, state_date_of_volunteering: Date) -> None:
        volunteer = Volunteer(volunteer_id=volunteer_id, name=name, state_date_of_volunteering=state_date_of_volunteering)
        s.add(volunteer)
        s.commit()

    def insert_volunteer_task(self, volunteer_task_id: int, volunteer_id: int, task_id: int) -> None:
        volunteer_task = VolunteerTask(volunteer_task_id=volunteer_task_id, volunteer_id=volunteer_id, task_id=task_id)
        s.add(volunteer_task)
        s.commit()

    def show_events(self):
        return s.query(Event.event_id, Event.title, Event.organizer, Event.date_of_event).all()

    def show_tasks(self):
        return s.query(Task.task_id, Task.importance, Task.event_id).all()

    def show_volunteers(self):
        return s.query(Volunteer.volunteer_id, Volunteer.name, Volunteer.state_date_of_volunteering).all()

    def show_volunteer_tasks(self):
        return s.query(VolunteerTask.volunteer_task_id, VolunteerTask.volunteer_id, VolunteerTask.task_id).all()

    @staticmethod
    def update_event(event_id: int, title: str, organizer: str, date_of_event: Date, id: int) -> None:
        s.query(Event).filter_by(event_id=id).update({Event.event_id: event_id, Event.title: title, Event.organizer: organizer, Event.date_of_event: date_of_event})
        s.commit()

    @staticmethod
    def update_task(task_id: int, importance: str, event_id: int, id: int) -> None:
        s.query(Task).filter_by(task_id=id).update({Task.task_id: task_id, Task.importance: importance, Task.event_id: event_id})
        s.commit()

    @staticmethod
    def update_volunteer(self, volunteer_id: int, name: str, state_date_of_volunteering: Date, id: int) -> None:
        s.query(Volunteer).filter_by(volunteer_id=id).update({Volunteer.volunteer_id: volunteer_id, Volunteer.name: name, Volunteer.state_date_of_volunteering: state_date_of_volunteering})
        s.commit()

    @staticmethod
    def update_volunteer_task(self, volunteer_task_id: int, volunteer_id: int, task_id: int, id: int) -> None:
        s.query(VolunteerTask).filter_by(volunteer_task_id=id).update({VolunteerTask.volunteer_task_id: volunteer_task_id, VolunteerTask.volunteer_id: volunteer_id, VolunteerTask.task_id: task_id})
        s.commit()

    def delete_event(self, event_id) -> None:
        event = s.query(Event).filter_by(event_id=event_id).one()
        s.delete(event)
        s.commit()

    def delete_task(self, task_id) -> None:
        task = s.query(Task).filter_by(task_id=task_id).one()
        s.delete(task)
        s.commit()

    def delete_volunteer(self, volunteer_id) -> None:
        volunteer = s.query(Volunteer).filter_by(volunteer_id=volunteer_id).one()
        s.delete(volunteer)
        s.commit()

    def delete_volunteer_task(self, volunteer_task_id) -> None:
        volunteer_task = s.query(VolunteerTask).filter_by(volunteer_task_id=volunteer_task_id).one()
        s.delete(volunteer_task)
        s.commit()

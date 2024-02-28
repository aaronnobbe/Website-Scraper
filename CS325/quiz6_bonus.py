#SOLID implementation

#SRP: Single Responsibility Principle
# Each class has a single responsibility, and changes to one part of the overall code.
# User: Creates a user for the information.
# Activity: This class is used as an abstract class to set up the activities for change to be easily implemented in the future.
# Steps, Distance, and Calories Burned are subclasses of activities that have their own data.
# ActivityMonitor: Coordinates the recording, storage, and display of activity data.
# DataStorage: Stores all of the activity data
# Display: Prepares the data for the console display operation.
# ConsoleDisplay: Finally displays the data.

#OCP: Open-Closed Principle
# Classes can be added to but not modified.
# This program allows you to add new activites and then also modify the display of the activities.

#LSP: Liskov Substitution Principle
# Subclasses should be substitutable for a base class.
# The Steps, Distance, and CaloriesBurned classes are consistent with this step in SOLID, they can take the place of their base class.

#ISP: Interface Segregation Principle
# The user shouldn't be efffected by classes they do not use.
# Storage and display are independant functions and will not vilate this principle.
# ActivityMonitor does depend on storage but only when needed.

#DIP: Dependency Inversion Principle
# High-level modules should not depend on low-level modules.
# ActivityMonitor depends on abstractions such as storage and display as demonstrated.

from abc import ABC, abstractmethod
from typing import List

#create a person/user in order to keep track of data
class User:
    def __init__(self, user_id:int, name:str):
        self.user_id = user_id
        self.name = name

#abstract class and actual activities defined in subclasses
class Activity(ABC):
    @abstractmethod
    def record(self):
        pass

class Steps(Activity):
    def record(self):
        print("Recording dummy - so many steps")

class Distance(Activity):
    def record(self):
        print("Recording dummy - such a long distance because you walked so far")

class CaloriesBurned(Activity):
    def record(self):
        print("Recording dummy - you burned so many calories")
#setup for coordinating the recording, storage, and display of activity data.
class ActivityMonitor:
    def __init__(self, user: User, activities: List[Activity], data_storage: 'DataStorage', display: 'Display'):
        self.user = user
        self.activities = activities
        self.data_storage = data_storage
        self.display = display

    def record_activity(self, activity: Activity):
        activity.record()
        self.data_storage.save_activity_data(self.user, activity)
        self.display.update(activity)

class DataStorage:
    def save_activity_data(self, user: User, activity: Activity):
        print(f"data storage dummy - Activity done by {user.name}: {activity.__class__.__name__}")
#abstract class for console display. 
class Display(ABC):
    @abstractmethod
    def update(self, activity: Activity):
        pass
#display to the console.
class ConsoleDisplay(Display):
    def update(self, activity: Activity):
        print(f"display dummy - Activity: {activity.__class__.__name__}")

if __name__ == "__main__":
    # Dummy data
    user = User(1, "jimmy(dummy)")
    steps_activity = Steps()
    distance_activity = Distance()
    calories_burned_activity = CaloriesBurned()

    # Setup 
    data_storage = DataStorage()
    console_display = ConsoleDisplay()
    activity_monitor = ActivityMonitor(user, [steps_activity, distance_activity, calories_burned_activity], data_storage, console_display)

    # Record activities
    for activity in activity_monitor.activities:
        activity_monitor.record_activity(activity)
        #program successfully records, saves, and then displays the workout, distance and calories burned
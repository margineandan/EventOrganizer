from validation.functions import Functions
from domain.event import Event


class EventService(Functions):
    """
    Class definition for EventService class.

    Args:
        Functions (Functions): inherited class

    Attributes:
        event_repository (private: EventRepository): EventRepository object
        event_validator (private: EventValidator): EventValidator object

    Methods:
        __init__: constructor for EventService class
        add_event: add new Event object
        get_events: get all Event objects
        delete_event: delete Event object
        modify_event_date: update Event object 'date' attribute
        modify_event_time: update Event object 'time' attribute
        modify_event_description: update Event object 'description' attribute
        search_event: search Event object
    """

    def __init__(self, event_repository, event_validator) -> None:
        """
        Constructor for CommonService object.

        Args:
            event_repository (EventRepository): EventRepository object repository
            event_validator (EventValidator): EventValidator object validator

        Return: None
        """

        self.__event_repository = event_repository
        self.__event_validator = event_validator

    def add_event(self, id: int, date: str, time: str, description: str) -> None:
        """
        Add new Event object.

        Args:
            id (int): id of Event object
            date (str): date of Event object
            time (str): time of Event object
            description (str): description of Event object

        Return: None
        """

        event = Event(id, date, time, description)
        self.__event_validator.validate_event(event)
        self.__event_repository.add_event(event)

    def get_events(self) -> list:
        """
        Get all Event objects.

        Args: None

        Return: list
        """

        return self.__event_repository.get_events()

    def delete_event(self, id: int) -> None:
        """
        Delete Event object.

        Args:
            id (int): id of Event object

        Return: None
        """

        event = self.__event_repository.search_event(id)
        self.__event_repository.delete_event(event)

    def modify_event_date(self, id: int, new_date: str) -> None:
        """
        Update Event object 'date' attribute.

        Args:
            id (int): id of Event object
            new_date (str): updated date of Event object

        Return: None
        """

        event = self.__event_repository.search_event(id)
        new_event = Event(id, new_date, event.get_time(), event.get_description())
        self.__event_validator.validate_event(new_event)
        self.__event_repository.modify_event(new_event)

    def modify_event_time(self, id: int, new_time: str) -> None:
        """
        Update Event object 'time' attribute.

        Args:
            id (int): id of Event object
            new_time (str): updated time of Event object

        Return: None
        """

        event = self.__event_repository.search_event(id)
        new_event = Event(id, event.get_date(), new_time, event.get_description())
        self.__event_validator.validate_event(new_event)
        self.__event_repository.modify_event(new_event)

    def modify_event_description(self, id: int, new_description: str) -> None:
        """
        Update Event object 'description' attribute.

        Args:
            id (int): id of Event object
            new_description (str): updated description of Event object

        Return: None
        """

        event = self.__event_repository.search_event(id)
        new_event = Event(id, event.get_date(), event.get_time(), new_description)
        self.__event_validator.validate_event(new_event)
        self.__event_repository.modify_event(new_event)

    def search_event(self, id: int) -> Event:
        """
        Search Event object.

        Args:
            id (int): id of Event object

        Return: Event
        """
        event = self.__event_repository.search_event(id)

        return event


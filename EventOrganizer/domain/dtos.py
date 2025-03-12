import domain
from domain.person import Person


class TopPersonsDTO:

    def __init__(self, person: domain, nr_events: int) -> None:
        """
        Constructor for TopPersonsDTO object.

        Args:
            person (Person): Person object
            nr_events (int): number of events Person object attends

        Return: None
        """

        self.__person = person
        self.__nr_events = nr_events

    def get_person(self) -> domain:
        """
        Return Person object.

        Args: None

        Return: Person object
        """

        return self.__person

    def get_nr_events(self) -> int:
        """
        Return number of events Person object attends.

        Args: None

        Return: int
        """

        return self.__nr_events

    def __str__(self) -> str:
        """
        Return reader-friendly string representation of TopPersonsDTO object.

        Args: None

        Return: str
        """

        return f"{self.__person} - - > Number of events: {self.__nr_events} \n"


class TopEventsDTO:

    def __init__(self, event_description: str, nr_persons: int) -> None:
        """
        Constructor for TopEventsDTO object.

        Args:
            event_description (str): description of Event object
            nr_persons (int): number of persons attending Event object

        Return: None
        """

        self.__event_description = event_description
        self.__nr_persons = nr_persons

    def get_event_description(self) -> str:
        """
        Return description of Event object.

        Args: None

        Return: str
        """

        return self.__event_description

    def get_nr_persons(self) -> int:
        """
        Return number of persons attending Event object.

        Args: None

        Return: int
        """

        return self.__nr_persons

    def __str__(self):
        """
        Return reader-friendly string representation of TopEventsDTO object.

        Args: None

        Return: str
        """

        return f" - - > Description: {self.__event_description} \n - - > Number of persons: {self.__nr_persons} \n"
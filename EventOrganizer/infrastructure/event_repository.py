from domain.event import Event
from exceptions.repo_exc import RepoError


class EventRepository:

    def __init__(self) -> None:
        """
        Constructor for EventRepository object.

        Args: None

        Return: None
        """

        self._events = {

        }

    def add_event(self, event: Event) -> None:
        """
        Add Event object to 'events'.

        Args:
            event (Event): Event object to add

        Return: None
        """

        if id in self._events.keys():
            raise RepoError("ERROR: event already exists...")

        self._events[event.get_id()] = event

    def get_events(self) -> list:
        """
        Return Event objects from 'events'.

        Args: None

        Return: list
        """

        return [self._events[identifier] for identifier in self._events.keys()]

    def delete_event(self, event) -> None:
        """
        Delete Event object from 'events'.

        Args:
            event (Event): Event object to delete

        Return: None
        """

        event_id = event.get_id()
        if event_id not in self._events.keys():
            raise RepoError("ERROR: event does not exist...")

        self._events.pop(event_id)

    def modify_event(self, event: Event) -> None:
        """
        Modify Event object attributes.

        Args:
            event (Event): Event object to modify

        Return: None
        """

        event_id = event.get_id()
        if event_id not in self._events.keys():
            raise RepoError("ERROR: event does not exist...")

        self._events[event.get_id()] = event

    def search_event(self, id: int) -> Event:
        """
        Search Event object in 'events'.

        Args:
            id (int): id of Event object to search

        Return: Event
        """

        if id not in self._events.keys():
            raise RepoError("ERROR: event does not exist...")

        return self._events[id]


class FileEventRepository(EventRepository):

    def __init__(self, file_path: str) -> None:
        """
        Constructor for FileEventRepository object.

        Args:
            file_path (str): file path of text file

        Return: None
        """

        EventRepository.__init__(self)
        self.__file_path = file_path

    def __read_events_from_file(self) -> None:
        """
        Read data form 'events' text file.

        Args: None

        Return: None
        """

        try:
            f = open(self.__file_path, "r")
        except IOError:
            raise RepoError(f"ERROR: path '{self.__file_path}' does not exist..")

        self._events.clear()
        lines = f.readlines()

        for line in lines:
            if line != "":
                line = line.strip()
                tokens = line.split(",")
                event_id = int(tokens[0])
                event_date = tokens[1]
                event_time = tokens[2]
                event_description = tokens[3]
                event = Event(event_id, event_date, event_time, event_description)
                self._events[event_id] = event

        f.close()

    def __write_events_to_file(self) -> None:
        """
        Write data to 'events' text file.

        Args: None

        Return: None
        """

        try:
            f = open(self.__file_path, "w")
        except IOError:
            raise RepoError(f"ERROR: path '{self.__file_path}' does not exist..")

        for event in self._events.values():
            f.write(f"{event.get_id()},{event.get_date()},{event.get_time()},{event.get_description()}" + "\n")

        f.close()

    def add_event(self, event: Event) -> None:
        """
        Add Event object to 'events' text file.

        Args:
            event (Event): Event object to add

        Return: None
        """

        self.__read_events_from_file()
        EventRepository.add_event(self, event)
        self.__write_events_to_file()

    def get_events(self) -> list:
        """
        Return Event objects from 'events' text file.

        Args: None

        Return: list
        """

        self.__read_events_from_file()
        return EventRepository.get_events(self)

    def delete_event(self, event: Event) -> None:
        """
        Delete Event object from 'events' text file.

        Args:
            event (Event): Event object to delete

        Return: None
        """

        self.__read_events_from_file()
        EventRepository.delete_event(self, event)
        self.__write_events_to_file()

    def modify_event(self, event: Event) -> None:
        """
        Modify Event object attrributes in text file.

        Args:
            event (Event): Event object to modify

        Return: None
        """

        self.__read_events_from_file()
        EventRepository.modify_event(self, event)
        self.__write_events_to_file()

    def search_event(self, event_id: int) -> Event:
        """
        Search Event object in 'events' text file.

        Args:
            event_id (int): id of Event object to search

        Return: Event
        """

        self.__read_events_from_file()
        return EventRepository.search_event(self, event_id)
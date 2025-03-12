from domain.person_event import PersonEvent
from domain.person import Person
from domain.event import Event
from exceptions.repo_exc import RepoError


class PersonEventRepository:

    def __init__(self) -> None:
        """
        Constructor for PersonEventRepository object.

        Args: None

        Return: None
        """

        self._person_event_maps = [

        ]

    def store(self, person_event: PersonEvent) -> None:
        """
        Add PersonEvent object.

        Args:
            person_event (PersonEvent): PersonEvent object to add

        Return: None
        """

        if person_event in self._person_event_maps:
            raise RepoError("ERROR: person already attends the event...")

        self._person_event_maps.append(person_event)

    def get_person_events(self, person: Person) -> list:
        """
        Return Event objects Person object attends.

        Args:
            person (Person): Person object to search attending Event objects

        Return: list
        """

        person_id = person.get_id()
        event_ids = []

        for person_event_map in self._person_event_maps:
            if person_event_map.get_person_id() == person_id:
                event_ids.append(person_event_map.get_event_id())

        return event_ids

    def get_event_persons(self, event: Event) -> list:
        """
        Return Person objects attending Event object.

        Args:
            event (Event): Event object to search attending Person objects

        Return: list
        """

        event_id = event.get_id()
        person_ids = []

        for person_event_map in self._person_event_maps:
            if person_event_map.get_event_id() == event_id:
                person_ids.append(person_event_map.get_person_id())

        return person_ids

    def delete(self, person_event: PersonEvent) -> None:
        """
        Delete PersonEvent object.

        Args:
            person_event (PersonEvent): PersonEvent object to delete

        Return: None
        """

        if person_event not in self._person_event_maps:
            raise RepoError("ERROR: person does not attend the event...")

        self._person_event_maps.remove(person_event)

    def update_deleted_person(self, person: Person) -> None:
        """
        Update after Person object deletion.

        Args:
            person (Person): deleted Person object

        Return: None
        """

        person_id = person.get_id()

        for person_event_map in self._person_event_maps:
            if person_event_map.get_person_id() == person_id:
                self._person_event_maps.remove(person_event_map)

    def update_deleted_event(self, event: Event) -> None:
        """
        Update after Event object deletion.

        Args:
            event (Event): deleted Event object

        Return: None
        """

        event_id = event.get_id()

        for person_event_map in self._person_event_maps:
            if person_event_map.get_event_id() == event_id:
                self._person_event_maps.remove(person_event_map)


class FilePersonEventRepository(PersonEventRepository):

    def __init__(self, file_path: str) -> None:
        """
        Constructor for FilePersonEventRepository object.

        Args:
            file_path (str): file path of text file

        Return: None
        """

        PersonEventRepository.__init__(self)
        self.__file_path = file_path

    def __read_person_event_maps_from_file(self) -> None:
        """
        Read data form 'person_event' text file.

        Args: None

        Return: None
        """

        try:
            f = open(self.__file_path, "r")
        except IOError:
            raise RepoError(f"ERROR: path '{self.__file_path}' does not exist..")

        self._person_event_maps.clear()
        lines = f.readlines()

        for line in lines:
            if line != "":
                line = line.strip()
                tokens = line.split(",")
                person_id = int(tokens[0])
                event_id = int(tokens[1])
                person_event_map = PersonEvent(person_id, event_id)
                self._person_event_maps.append(person_event_map)

        f.close()

    def __write_person_event_maps_to_file(self) -> None:
        """
        Write data to 'person_event' text file.

        Args: None

        Return: None
        """

        try:
            f = open(self.__file_path, "w")
        except IOError:
            raise RepoError(f"ERROR: path '{self.__file_path}' does not exist..")

        for person_event_map in self._person_event_maps:
            f.write(str(person_event_map) + "\n")

        f.close()

    def store(self, person_event: PersonEvent) -> None:
        """
        Add PersonEvent object to 'person_event' text file.

        Args:
            person_event (PersonEvent): PersonEvent object to add

        Return: None
        """

        self.__read_person_event_maps_from_file()
        PersonEventRepository.store(self, person_event)
        self.__write_person_event_maps_to_file()

    def get_person_events(self, person: Person) -> list:
        """
        Return Event objects Person object attents from 'person_event' text file.

        Args:
            person (Person): Person object to search attending Event objects

        Return: list
        """

        self.__read_person_event_maps_from_file()
        return PersonEventRepository.get_person_events(self, person)

    def get_event_persons(self, event: Event) -> list:
        """
        Return Person objects attending Event object from 'person_event' text file.

        Args:
            event (Event): Event object to search attending Person objects

        Return: list
        """

        self.__read_person_event_maps_from_file()
        return PersonEventRepository.get_event_persons(self, event)

    def delete(self, person_event: PersonEvent) -> None:
        """
        Delete PersonEvent object from 'person_event' text file.

        Args:
            person_event (PersonEvent): PersonEvent object to delete

        Return: None
        """

        self.__read_person_event_maps_from_file()
        PersonEventRepository.delete(self, person_event)
        self.__write_person_event_maps_to_file()

    def update_deleted_person(self, person: Person) -> None:
        """
        Update 'person_event' text file after Person object deletion.

        Args:
            person (Person): deleted Person object

        Return: None
        """

        self.__read_person_event_maps_from_file()
        PersonEventRepository.update_deleted_person(self, person)
        self.__write_person_event_maps_to_file()

    def update_deleted_event(self, event: Event) -> None:
        """
        Update 'person_event' text file after Event object deletion.

        Args:
            event (Event): deleted Event object

        Return: None
        """

        self.__read_person_event_maps_from_file()
        PersonEventRepository.update_deleted_event(self, event)
        self.__write_person_event_maps_to_file()
from domain.person import Person
from exceptions.repo_exc import RepoError


class PersonRepository:

    def __init__(self) -> None:
        """
        Constructor for PersonRepository object.

        Args: None

        Return: None
        """

        self._persons = {

        }

    def add_person(self, person: Person) -> None:
        """
        Add Person object to 'persons'.

        Args:
            person (Person): Person object to add

        Return: None
        """

        person_id = person.get_id()
        person_address = person.get_address()

        if person_id in self._persons.keys():
            raise RepoError("ERROR: id already exists...")

        for entity in self._persons.values():
            if person_address == entity.get_address():
                raise RepoError("ERROR: address already exists...")

        self._persons[person_id] = person

    """
    def get_persons(self) -> list:
    
        return [self._persons[identifier] for identifier in self._persons.keys()]
    """

    def get_persons_recursive(self, identifiers=None, index=0) -> list:
        """
        Return Person objects from 'persons' recursively.

        Args:
            identifiers (list): A list to store identifiers.
            index (int): Current index while traversing.

        Return: list
        """
        if identifiers is None:
            identifiers = list(self._persons.keys())

        if index == len(identifiers):
            return []

        current_identifier = identifiers[index]
        person_object = self._persons[current_identifier]

        remaining_persons = self.get_persons_recursive(identifiers, index + 1)

        return [person_object] + remaining_persons

    def get_persons(self) -> list:
        """
        Return Person objects from 'persons'.

        Args: None

        Return: list
        """
        return self.get_persons_recursive()

    def delete_person(self, person) -> None:
        """
        Delete Person object from 'persons'.

        Args:
            person (Person): Person object

        Return: None
        """

        person_id = person.get_id()
        if person_id not in self._persons.keys():
            raise RepoError("ERROR: person does not exist...")

        self._persons.pop(person_id)

    def modify_person(self, person: Person) -> None:
        """
        Modify Person object attributes.

        Args:
            person: Person object to modify

        Return: None
        """

        person_id = person.get_id()
        if person_id not in self._persons.keys():
            raise RepoError("ERROR: person does not exist...")

        for entity in self._persons.values():
            if person.get_id() != entity.get_id() and person.get_address() == entity.get_address():
                raise RepoError("ERROR: address already exists...")

        self._persons[person.get_id()] = person

    def search_person(self, id: int) -> Person:
        """
        Search Person object in 'persons'.

        Args:
            id (int): id of Person object to search

        Return: Person
        """

        if id not in self._persons.keys():
            raise RepoError("ERROR: person does not exist...")

        return self._persons[id]


class FilePersonRepository(PersonRepository):

    def __init__(self, file_path: str) -> None:
        """
        Constructor for FilePersonRepository object.

        Args:
            file_path (str): file path of text file

        Return: None
        """

        PersonRepository.__init__(self)
        self.__file_path = file_path

    def __read_persons_from_file(self) -> None:
        """
        Read data form 'persons' text file.

        Args: None

        Return: None
        """

        try:
            f = open(self.__file_path, "r")
        except IOError:
            raise RepoError(f"ERROR: path '{self.__file_path}' does not exist..")

        self._persons.clear()
        lines = f.readlines()

        for i in range(0, len(lines), 3):
            person_id = int(lines[i].strip())
            person_name = lines[i + 1].strip()
            person_address = lines[i + 2].strip()
            person = Person(person_id, person_name, person_address)
            self._persons[person_id] = person

        f.close()

    def __write_persons_to_file(self) -> None:
        """
        Write data to 'persons' text file.

        Args: None

        Return: None
        """

        try:
            f = open(self.__file_path, "w")
        except IOError:
            raise RepoError(f"ERROR: path '{self.__file_path}' does not exist..")

        for person in self._persons.values():
            f.write(f"{person.get_id()}\n{person.get_name()}\n{person.get_address()}\n")

        f.close()

    def add_person(self, person: Person) -> None:
        """
        Add Person object to 'persons' text file.

        Args:
            person (Person): Person object to add

        Return: None
        """

        self.__read_persons_from_file()
        PersonRepository.add_person(self, person)
        self.__write_persons_to_file()

    def get_persons(self) -> list:
        """
        Return Person objects from 'persons' text file.

        Args: None

        Return: list
        """

        self.__read_persons_from_file()
        return PersonRepository.get_persons(self)

    def delete_person(self, person: Person) -> None:
        """
        Delete Person object from 'persons' text file.

        Args:
            person (Person): Person object

        Return: None
        """

        self.__read_persons_from_file()
        PersonRepository.delete_person(self, person)
        self.__write_persons_to_file()

    def modify_person(self, person: Person) -> None:
        """
        Modify Person object attributes in text file.

        Args:
            person: Person object to modify

        Return: None
        """

        self.__read_persons_from_file()
        PersonRepository.modify_person(self, person)
        self.__write_persons_to_file()

    def search_person(self, person_id: int):
        """
        Search Person object in 'persons' text file.

        Args:
            person_id (int): id of Person object to search

        Return: Person
        """

        self.__read_persons_from_file()
        return PersonRepository.search_person(self, person_id)

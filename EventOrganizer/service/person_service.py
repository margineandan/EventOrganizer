from domain.person import Person
from validation.functions import Functions
import random
import string


class PersonService(Functions):
    def __init__(self, person_repository, person_validator) -> None:
        """
        Constructor for PersonService object.

        Args:
            person_repository (PersonRepository): PersonRepository object repository
            person_validator (PersonValidator): PersonValidator object validator

        Return: None
        """

        self.__person_repository = person_repository
        self.__person_validator = person_validator

    def add_person(self, id: int, name: str, address: str) -> None:
        """
        Add new Person object.

        Args:
            id (int): id of Person object
            name (str): name of Person object
            address (str): address of Person object

        Return: None
        """

        person = Person(id, name.capitalize(), address)
        self.__person_validator.validate_person(person)
        self.__person_repository.add_person(person)

    def get_persons(self) -> list:
        """
        Get all Person objects.

        Args: None

        Return: list
        """

        return self.__person_repository.get_persons()

    def delete_person(self, id: int) -> None:
        """
        Delete Person object.

        Args:
            id (int): id of Person object

        Return: None
        """

        person = self.__person_repository.search_person(id)
        self.__person_repository.delete_person(person)

    def modify_person_name(self, id: int, new_name: str) -> None:
        """
        Update Person object 'name' attribute.

        Args:
            id (int): id of Person object
            new_name (str): updated name of Person object

        Return: None
        """

        person = self.__person_repository.search_person(id)
        new_person = Person(id, new_name, person.get_address())
        self.__person_validator.validate_person(new_person)
        self.__person_repository.modify_person(new_person)

    def modify_person_address(self, id: int, new_address: str) -> None:
        """
        Update Person object 'address' attribute.

        Args:
            id (int): id of Person object
            new_address (str): updated address of Person object

        Return: None
        """

        person = self.__person_repository.search_person(id)
        new_person = Person(id, person.get_name(), new_address)
        self.__person_validator.validate_person(new_person)
        self.__person_repository.modify_person(new_person)

    def search_person(self, id: int) -> Person:
        """
        Search Person object.

        Args:
            id (int): id of Person object

        Return: Person
        """

        person = self.__person_repository.search_person(id)

        return person

    """
    def add_random_people(self, number_of_people: int) -> None:

        for i in range(0, number_of_people):
            person_id = random.randrange(100, 1000)
            name = ''.join(random.choice(string.ascii_letters) for _ in range(0, 5))
            address = ''.join(random.choice(string.ascii_letters) for _ in range(0, 8))
            address += str(random.randrange(1, 99))

            self.add_person(person_id, name, address)
    """

    def add_random_people(self, number_of_people: int) -> None:
        """
        Add randomly generated people recursively.

        Args:
            number_of_people (int): the number of people to add

        Return: None
        """
        if number_of_people <= 0:
            return

        person_id = random.randrange(100, 1000)
        name = ''.join(random.choice(string.ascii_letters) for _ in range(0, 5))
        address = ''.join(random.choice(string.ascii_letters) for _ in range(0, 8))
        address += str(random.randrange(1, 99))

        self.add_person(person_id, name, address)
        self.add_random_people(number_of_people - 1)
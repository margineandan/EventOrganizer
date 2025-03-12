class Person:

    def __init__(self, id: int, name: str, address: str) -> None:
        """
        Constructor for Person object.

        Args:
            id (int): Person object id
            name (str): Person object name
            address (str): Person object address

        Return: None
        """

        self.__id = id
        self.__name = name
        self.__address = address

    def __str__(self) -> str:
        """
        Return reader-friendly string representation of Person object.

        Args: None

        Return: str
        """
        return f" - - > ID: {self.__id} \n - - > Name: {self.__name} \n - - > Address: {self.__address} \n"

    def __eq__(self, entity) -> bool:
        """
        Return if two Person objects are equal by 'id' or 'address'.

        Args:
            entity (Person): Person object

        Return: bool
        """

        return self.__id == entity.__id or self.__address == entity.__address

    def get_id(self) -> int:
        """
        Return Person object 'id' attribute.

        Args: None

        Return: str
        """

        return self.__id

    def get_name(self) -> str:
        """
        Return Person object 'name' attribute.

        Args: None

        Return: str
        """

        return self.__name

    def get_address(self) -> str:
        """
        Return Person object 'address' attribute.

        Args: None

        Return: str
        """

        return self.__address

    def set_name(self, new_name: str) -> None:
        """
        Update Person object 'name' attribute.

        Args:
            new_name (str): updated Person object name

        Return: None
        """

        self.__name = new_name

    def set_address(self, new_address: str) -> None:
        """
        Update Person object 'address' attribute.

        Args:
            new_address (str): updated Person object address

        Return: None
        """

        self.__address = new_address

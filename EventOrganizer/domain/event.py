class Event:

    def __init__(self, id: int, date: str, time: str, description: str) -> None:
        """
        Constructor for Person object.

        Args:
            id (int): Event object id
            date (str): Event object date
            time (str): Event object time
            description (str): Event object description

        Return: None
        """

        self.__id = id
        self.__date = date
        self.__time = time
        self.__description = description

    def __str__(self) -> str:
        """
        Return reader-friendly string representation of Event object.

        Args: None

        Return: str
        """
        return f" - - > Date: {self.__date} \n - - > Time: {self.__time} \n - - > Description: {self.__description} \n"

    def __eq__(self, entity) -> bool:
        """
        Return if two Event objects are equal by 'id'.

        Args:
            entity (Event): Event object

        Return: bool
        """

        return self.__id == entity.__id

    def get_id(self) -> int:
        """
        Return Event object 'id' attribute.

        Args: None

        Return: str
        """

        return self.__id

    def get_date(self) -> str:
        """
        Return Event object 'date' attribute.

        Args: None

        Return: str
        """

        return self.__date

    def get_time(self) -> str:
        """
        Return Event object 'time' attribute.

        Args: None

        Return: str
        """

        return self.__time

    def get_description(self) -> str:
        """
        Return Event object 'description' attribute.

        Args: None

        Return: str
        """

        return self.__description

    def set_date(self, new_date: str) -> None:
        """
        Update Event object 'date' attribute.

        Args:
            new_date (str): updated Person object date

        Return: None
        """

        self.__date = new_date

    def set_time(self, new_time: str) -> None:
        """
        Update Event object 'time' attribute.

        Args:
            new_time (str): updated Event object time

        Return: None
        """

        self.__time = new_time

    def set_description(self, new_description: str) -> None:
        """
        Update Event object 'description' attribute.

        Args:
            new_description (str): updated Event object description

        Return: None
        """

        self.__description = new_description


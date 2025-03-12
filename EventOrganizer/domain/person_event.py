class PersonEvent:

    def __init__(self, person_id: int, event_id: int) -> None:
        """
        Constructor for PersonEvent object.

        Args:
            person_id (int): id of Person object
            event_id (int): id of Event object

        Return: None
        """

        self.__person_id = person_id
        self.__event_id = event_id

    def get_person_id(self) -> int:
        """
        Return Person object id attribute

        Return: int
        """

        return self.__person_id

    def get_event_id(self) -> int:
        """
        Return Event object id attribute

        Return: int
        """

        return self.__event_id

    def __str__(self) -> str:
        """
        Return reader-friendly string representation of PersonEvent object.

        Args: None

        Return: str
        """

        return f"{self.__person_id},{self.__event_id}"



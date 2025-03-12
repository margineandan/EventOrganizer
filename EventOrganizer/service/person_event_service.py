from domain.person_event import PersonEvent
from domain.dtos import TopPersonsDTO
from domain.dtos import TopEventsDTO


class PersonEventService:

    def __init__(self, person_repository, event_repository, person_event_repository) -> None:
        """
        Constructor for PersonEventService object.

        Args:
            person_repository (PersonRepository): PersonRepository object
            event_repository (EventRepository): EventRepository object
            person_event_repository (PersonEventRepository): PersonEventRepository object

        Return: None
        """

        self.__person_repository = person_repository
        self.__event_repository = event_repository
        self.__person_event_repository = person_event_repository

    @staticmethod
    def cmp_generic(item_1, item_2, keys: list) -> int:
        """
        Compare items based on multiple keys.

        Args:
            item_1: First item to compare
            item_2: Second item to compare
            keys (list): List of keys

        Returns: int
        """
        for key in keys:
            key_1 = key(item_1)
            key_2 = key(item_2)
            if key_1 < key_2:
                return -1
            elif key_1 > key_2:
                return 1

        return 0

    @staticmethod
    def cmp(item_1, item_2) -> bool:
        """
        Compare items based on multiple keys.

        Args:
            item_1: First item to compare
            item_2: Second item to compare

        Returns: bool
        """
        if item_1.get_description() == item_2.get_description():
            return item_1.get_date() > item_2.get_date()

        return item_1.get_description() > item_2.get_description()

    def selection_sort(self, items: list, key_func, reverse=False) -> list:
        """
        Perform selection sort on a list of items based on a custom key function.

        Time Complexity:
            O(n^2) (worst-case) / Θ(n^2) (average-case) / Ω(n^2) (best-case)

        Space Complexity:
            O(1) - constant

        Args:
            items (list): List of items to be sorted
            key_func (list): A list of functions that take an item and return keys for comparison
            reverse (bool): Dictates the direction of the sort (ascending / descending)

        Returns: list
        """
        for i in range(len(items)):
            index = i
            for j in range(i + 1, len(items)):
                if reverse:
                    if self.cmp_generic(items[j], items[index], key_func) > 0:
                        index = j
                else:
                    if self.cmp_generic(items[j], items[index], key_func) < 0:
                        index = j

            items[i], items[index] = items[index], items[i]

        return items

    def shake_sort(self, items: list, key_func, reverse=False) -> list:
        """
        Perform shake sort on a list of items based on a custom key function.

        Time Complexity:
            O(n^2) (worst-case) / Θ(n^2) (average-case) / Ω(n^2) (best-case)

        Space Complexity:
            O(1) - constant

        Args:
            items (list): List of items to be sorted
            key_func (list): A list of functions that take an item and return keys for comparison
            reverse (bool): Dictates the direction of the sort (ascending / descending)

        Returns: list
        """
        left = 0
        right = len(items) - 1
        while left <= right:
            for i in range(left, right):
                if reverse:
                    if self.cmp_generic(items[i + 1], items[i], key_func) > 0:
                        items[i], items[i + 1] = items[i + 1], items[i]
                else:
                    if self.cmp_generic(items[i + 1], items[i], key_func) < 0:
                        items[i], items[i + 1] = items[i + 1], items[i]

            right = right - 1

            for i in range(right, left, -1):
                if reverse:
                    if self.cmp_generic(items[i], items[i - 1], key_func) > 0:
                        items[i], items[i - 1] = items[i - 1], items[i]
                else:
                    if self.cmp_generic(items[i], items[i - 1], key_func) < 0:
                        items[i], items[i - 1] = items[i - 1], items[i]

            left = left + 1

        return items

    def add_person_to_event(self, person_id: int, event_id: int) -> None:
        """
        Add Person object to attend Event object.

        Args:
            person_id (int): id of Person object
            event_id (int): id of Event object

        Return: None
        """

        person_event = PersonEvent(person_id, event_id)

        self.__person_event_repository.store(person_event)

    def remove_person_from_event(self, person_id: int, event_id: int) -> None:
        """
        Remove attendance of Person object to Event object.

        Args:
            person_id (int): id of Person object
            event_id (int): id of Event object

        Return: None
        """

        person_event = PersonEvent(person_id, event_id)

        self.__person_event_repository.delete(person_event)

    def update_deleted_person(self, person_id: int) -> None:
        """
        Update Person object attendances to Event objects after deletion.

        Args:
            person_id (int): id of Person object

        Return: None
        """

        person = self.__person_repository.search_person(person_id)

        self.__person_event_repository.update_deleted_person(person)

    def update_deleted_event(self, event_id: int) -> None:
        """
        Update Event object attendances of Person objects after deletion.

        Args:
            event_id (int): id of Event object

        Return: None
        """

        event = self.__event_repository.search_event(event_id)

        self.__person_event_repository.update_deleted_event(event)

    def get_person_events(self, person_id: int) -> list:
        """
        Return Event objects Person object attends.

        Args:
            person_id (int): id of Person object

        Return: list
        """

        person = self.__person_repository.search_person(person_id)
        event_ids = self.__person_event_repository.get_person_events(person)
        events = [self.__event_repository.search_event(event_id) for event_id in event_ids]

        return events

    def get_event_persons(self, event_id: int) -> list:
        """
        Return Person objects attending Event object.

        Args:
            event_id (int): id of Event object

        Return: list
        """

        event = self.__event_repository.search_event(event_id)
        person_ids = self.__person_event_repository.get_event_persons(event)
        persons = [self.__person_repository.search_person(person_id) for person_id in person_ids]

        return persons

    def get_person_events_by_description(self, person_id: int) -> list:
        """
        Return Event objects Person object attends by description ascending.

        Args:
            person_id (int): id of Person object

        Return: list
        """

        person = self.__person_repository.search_person(person_id)
        event_ids = self.__person_event_repository.get_person_events(person)
        events = [self.__event_repository.search_event(event_id) for event_id in event_ids]
        # events.sort(key=lambda event: event.get_description(), reverse=False)
        events = self.shake_sort(events, key_func=[lambda event: event.get_description(), lambda event: event.get_date()])

        return events

    def get_person_events_by_date(self, person_id: int) -> list:
        """
        Return Event objects Person object attends by date ascending.

        Args:
            person_id (int): id of Person object

        Return: list
        """

        person = self.__person_repository.search_person(person_id)
        event_ids = self.__person_event_repository.get_person_events(person)
        events = [self.__event_repository.search_event(event_id) for event_id in event_ids]
        # events.sort(key=lambda event: event.get_date(), reverse=False)
        events = self.selection_sort(events, key_func=[lambda event: event.get_date(), lambda event: event.get_time()])

        return events

    def get_top_persons(self) -> list:
        """
        Return top 20% Person objects with most attendances to events.

        Args: None

        Return: list
        """

        persons = self.__person_repository.get_persons()
        nr_events = {}

        for person in persons:
            person_id = person.get_id()
            nr_events[person_id] = len(self.__person_event_repository.get_person_events(person))

        result = []

        for key, value in nr_events.items():
            person = self.__person_repository.search_person(key)
            events = value
            dto = TopPersonsDTO(person, events)
            result.append(dto)

        # result.sort(key=lambda x: x.get_nr_events(), reverse=True)
        result = self.shake_sort(result, key_func=[lambda obj: obj.get_nr_events()], reverse=True)

        return result[:(len(result) // 5)]

    def get_top_events(self) -> list:
        """
        Return top 20% Event objects with most attending persons.

        Args: None

        Return: list
        """

        events = self.__event_repository.get_events()
        nr_persons = {}

        for event in events:
            event_id = event.get_id()
            nr_persons[event_id] = len(self.__person_event_repository.get_event_persons(event))

        result = []

        for key, value in nr_persons.items():
            event = self.__event_repository.search_event(key)
            event_description = event.get_description()
            persons = value
            dto = TopEventsDTO(event_description, persons)
            result.append(dto)

        # result.sort(key=lambda x: x.get_nr_persons(), reverse=True)
        result = self.selection_sort(result, key_func=[lambda obj: obj.get_nr_persons()], reverse=True)

        return result[:(len(result) // 5)]

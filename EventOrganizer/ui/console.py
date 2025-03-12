from exceptions.ui_exc import UIError
from exceptions.repo_exc import RepoError
import time


class Console:

    def __init__(self, person_service, event_service, person_event_service) -> None:
        """
        Constructor for UI object.

        Args:
            person_service (PersonService): PersonService object service
            event_service (EventService): EventService object service
            person_event_service (PersonEventService): PersonEventService object service

        Return: None
        """

        self.__person_service = person_service
        self.__event_service = event_service
        self.__person_event_service = person_event_service
        self.__commands = {
            "commands": [self.__ui_commands, "()"],
            "add_person": [self.__ui_add_person, "(person_id, person_name, person_address)"],
            "display_persons": [self.__ui_display_persons, "()"],
            "delete_person": [self.__ui_delete_person, "(person_id)"],
            "modify_person_name": [self.__ui_modify_person_name, "(person_id, new_name)"],
            "modify_person_address": [self.__ui_modify_person_address, "(person_id, new_address)"],
            "person_display_events": [self.__ui_person_display_events, "(person_id)"],
            "search_person": [self.__ui_search_person, "(person_id)"],
            "person_display_events_by_description": [self.__ui_person_display_events_by_description, "(person_id)"],
            "person_display_events_by_date": [self.__ui_person_display_events_by_date, "(person_id)"],
            "add_event": [self.__ui_add_event, "(event_id, event_date, event_time, event_description)"],
            "display_events": [self.__ui_display_events, "()"],
            "delete_event": [self.__ui_delete_event, "(event_id)"],
            "modify_event_date": [self.__ui_modify_event_date, "(event_id, new_date)"],
            "modify_event_time": [self.__ui_modify_event_time, "(event_id, new_time)"],
            "modify_event_description": [self.__ui_modify_event_description, "(event_id, new_description)"],
            "search_event": [self.__ui_search_event, "(event_id)"],
            "add_person_to_event": [self.__ui_add_person_to_event, "(person_id, event_id)"],
            "remove_person_from_event": [self.__ui_remove_person_from_event, "(person_id, event_id)"],
            "event_display_persons": [self.__ui_event_display_persons, "(event_id)"],
            "person_events_number": [self.__ui_person_events_number, "(person_id)"],
            "top_events": [self.__ui_top_events, "()"],
            "top_persons": [self.__ui_top_persons, "()"],
            "add_random_people": [self.__ui_add_random_people, "(number_of_people)"],
            "exit": [self.__ui_exit_program, "()"],
        }

    def __ui_commands(self, params: list) -> None:
        """
        Interface to display commands.

        Args:
            params (list): list of function arguments

        Return: None
        """

        if len(params) != 0:
            print(f"ERROR: function 'commands' takes 0 arguments but {len(params)} were given...")
            return

        for key, value in self.__commands.items():
            print(f"{key}{value[1]}")

    def __ui_add_person(self, params: list) -> None:
        """
        Interface to add Person object.

        Args:
            params (list): list of function arguments

        Return: None
        """

        if len(params) != 3:
            print(f"ERROR: function 'add_person' takes 3 arguments but {len(params)} were given...")
            return

        try:
            id = int(params[0])
            name = params[1].capitalize()
            address = params[2]
            self.__person_service.add_person(id, name, address)
            print("SUCCESS: new person was successfully added...")
        except ValueError:
            raise UIError("ERROR: 'id' must be a positive numeric value...")
        except RepoError as err:
            raise UIError(err)

    def __ui_add_random_people(self, params: list) -> None:
        """
        Interface to add Person object.

        Args:
            params (list): list of function arguments

        Return: None
        """
        if len(params) != 1:
            print(f"ERROR: function 'add_person' takes 1 argument but {len(params)} were given...")
            return

        try:
            number_of_people = int(params[0])
            if number_of_people <= 0:
                raise UIError("ERROR: 'number_of_people' must be a positive numeric value...")
            self.__person_service.add_random_people(number_of_people)
            print(f"SUCCESS: new {number_of_people} random people were successfully added...")
        except ValueError:
            raise UIError("ERROR: 'number_of_people' must be a numeric value...")
        except RepoError as err:
            raise UIError(err)

    def __ui_display_persons(self, params: list) -> None:
        """
        Interface to display all Person objects.

        Args:
            params (list): list of function arguments

        Return: None
        """

        if len(params) != 0:
            print(f"ERROR: function 'display_persons' takes 0 arguments but {len(params)} were given...")
            return

        persons = self.__person_service.get_persons()
        if len(persons) == 0:
            print("No persons available...")
        else:
            for person in persons:
                print(person)

    def __ui_delete_person(self, params: list) -> None:
        """
        Interface to delete Person object.

        Args:
            params (list): list of function arguments

        Return: None
        """

        if len(params) != 1:
            print(f"ERROR: function 'delete_person' takes 1 arguments but {len(params)} were given...")
            return

        try:
            id = int(params[0])

            self.__person_event_service.update_deleted_person(id)
            self.__person_service.delete_person(id)
            print("SUCCESS: person was successfully deleted...")
        except ValueError:
            raise UIError("ERROR: 'id' must be a positive numeric value...")
        except RepoError as err:
            raise UIError(err)

    def __ui_modify_person_name(self, params: list) -> None:
        """
        Interface to modify Person object name.

        Args:
            params (list): list of function arguments

        Return: None
        """

        if len(params) != 2:
            print(f"ERROR: function 'modify_person_address' takes 2 arguments but {len(params)} were given...")
            return

        try:
            id = int(params[0])
            new_name = params[1].capitalize()

            self.__person_service.modify_person_name(id, new_name)
            print("SUCCESS: person was successfully modified...")
        except ValueError:
            raise UIError("ERROR: 'id' must be a positive numeric value...")
        except RepoError as err:
            raise UIError(err)

    def __ui_person_display_events(self, params: list) -> None:
        """
        Interface to display all events Person object attends.

        Args:
            params (list): list of function arguments

        Return: None
        """

        if len(params) != 1:
            print(f"ERROR: function 'person_display_events' takes 1 arguments but {len(params)} were given...")
            return

        try:
            id = int(params[0])

            events = self.__person_event_service.get_person_events(id)
            if len(events) == 0:
                print("Person does not attend any event...")
            else:
                for event in events:
                    print(event)
        except ValueError:
            raise UIError("ERROR: 'id' must be a positive numeric value...")
        except RepoError as err:
            raise UIError(err)

    def __ui_modify_person_address(self, params: list) -> None:
        """
        Interface to modify Person object address.

        Args:
            params (list): list of function arguments

        Return: None
        """

        if len(params) != 2:
            print(f"ERROR: function 'modify_person_address' takes 2 arguments but {len(params)} were given...")
            return

        try:
            id = int(params[0])
            new_address = params[1]

            self.__person_service.modify_person_address(id, new_address)
            print("SUCCESS: person was successfully modified...")
        except ValueError:
            raise UIError("ERROR: 'id' must be a positive numeric value...")
        except RepoError as err:
            raise UIError(err)

    def __ui_search_person(self, params: list) -> None:
        """
        Interface to search Person object.

        Args:
            params (list): list of function arguments

        Return: None
        """

        if len(params) != 1:
            print(f"ERROR: function 'search_person' takes 1 arguments but {len(params)} were given...")
            return

        try:
            id = int(params[0])

            person = self.__person_service.search_person(id)
            print(person)
        except ValueError:
            raise UIError("ERROR: 'id' must be a positive numeric value...")
        except RepoError as err:
            raise UIError(err)

    def __ui_person_display_events_by_description(self, params: list) -> None:
        """
        Interface to display all events Person object attends by description lexicographically.

        Args:
            params (list): list of function arguments

        Return: None
        """

        if len(params) != 1:
            print(
                f"ERROR: function 'person_display_events_by_description' takes 1 arguments but {len(params)} were given...")
            return

        try:
            id = int(params[0])
            events = self.__person_event_service.get_person_events_by_description(id)
            if len(events) == 0:
                print("Person does not attend any event...")
            else:
                for event in events:
                    print(event)
        except ValueError:
            raise UIError("ERROR: 'id' must be a positive numeric value...")
        except RepoError as err:
            raise UIError(err)

    def __ui_person_display_events_by_date(self, params: list) -> None:
        """
        Interface to display all events Person object attends by date ascending.

        Args:
            params (list): list of function arguments

        Return: None
        """

        if len(params) != 1:
            print(f"ERROR: function 'person_display_events_by_date takes 1 arguments but {len(params)} were given...")
            return

        try:
            id = int(params[0])
            events = self.__person_event_service.get_person_events_by_date(id)
            if len(events) == 0:
                print("Person does not attend any event...")
            else:
                for event in events:
                    print(event)
        except ValueError:
            raise UIError("ERROR: 'id' must be a positive numeric value...")
        except RepoError as err:
            raise UIError(err)

    def __ui_add_event(self, params: list) -> None:
        """
        Interface to add Event object.

        Args:
            params (list): list of function arguments

        Return: None
        """

        try:
            id = int(params[0])
            date = params[1]
            event_time = params[2]
            description = ' '.join(params[3:]).capitalize()

            self.__event_service.add_event(id, date, event_time, description)
            print("SUCCESS: event was successfully added...")
        except ValueError:
            raise UIError("ERROR: 'id' must be a positive numeric value...")
        except RepoError as err:
            raise UIError(err)

    def __ui_display_events(self, params: list) -> None:
        """
        Interface to display all Event objects.

        Args:
            params (list): list of function arguments

        Return: None
        """

        if len(params) != 0:
            print(f"ERROR: function 'display_events' takes 0 arguments but {len(params)} were given...")
            return

        events = self.__event_service.get_events()
        if len(events) == 0:
            print("No events available...")
        else:
            for event in events:
                print(event)

    def __ui_delete_event(self, params: list) -> None:
        """
        Interface to delete Event object.

        Args:
            params (list): list of function arguments

        Return: None
        """

        if len(params) != 1:
            print(f"ERROR: function 'delete_event' takes 1 arguments but {len(params)} were given...")
            return

        try:
            id = int(params[0])

            self.__person_event_service.update_deleted_event(id)
            self.__event_service.delete_event(id)
            print("SUCCESS: event was successfully deleted...")
        except ValueError:
            raise UIError("ERROR: 'id' must be a positive numeric value...")
        except RepoError as err:
            raise UIError(err)

    def __ui_modify_event_date(self, params: list) -> None:
        """
        Interface to modify Event object date.

        Args:
            params (list): list of function arguments

        Return: None
        """

        if len(params) != 2:
            print(f"ERROR: function 'modify_event_date' takes 2 arguments but {len(params)} were given...")
            return

        try:
            id = int(params[0])
            new_date = params[1]

            self.__event_service.modify_event_date(id, new_date)
            print("SUCCESS: event was successfully modified...")
        except ValueError:
            raise UIError("ERROR: 'id' must be a positive numeric value...")
        except RepoError as err:
            raise UIError(err)

    def __ui_modify_event_time(self, params: list) -> None:
        """
        Interface to modify Event object time.

        Args:
            params (list): list of function arguments

        Return: None
        """

        if len(params) != 2:
            print(f"ERROR: function 'modify_event_time' takes 2 arguments but {len(params)} were given...")
            return

        try:
            id = int(params[0])
            new_time = params[1]

            self.__event_service.modify_event_time(id, new_time)
            print("SUCCESS: event was successfully modified...")
        except ValueError:
            raise UIError("ERROR: 'id' must be a positive numeric value...")
        except RepoError as err:
            raise UIError(err)

    def __ui_modify_event_description(self, params: list) -> None:
        """
        Interface to modify Event object description.

        Args:
            params (list): list of function arguments

        Return: None
        """

        try:
            id = int(params[0])
            new_description = ' '.join(params[1:]).capitalize()

            self.__event_service.modify_event_description(id, new_description)
            print("SUCCESS: event was successfully modified...")
        except ValueError:
            raise UIError("ERROR: 'id' must be a positive numeric value...")
        except RepoError as err:
            raise UIError(err)

    def __ui_search_event(self, params: list) -> None:
        """
        Interface to search Event object.

        Args:
            params (list): list of function arguments

        Return: None
        """

        if len(params) != 1:
            print(f"ERROR: function 'search_event' takes 1 arguments but {len(params)} were given...")
            return

        try:
            id = int(params[0])

            event = self.__event_service.search_event(id)
            print(event)
        except ValueError:
            raise UIError("ERROR: 'id' must be a positive numeric value...")
        except RepoError as err:
            raise UIError(err)

    def __ui_add_person_to_event(self, params: list) -> None:
        """
        Interface to add new person to attend Event object.

        Args:
            params (list): list of function arguments

        Return: None
        """

        if len(params) != 2:
            print(f"ERROR: function 'add_person_to_event' takes 2 arguments but {len(params)} were given...")
            return

        try:
            person_id = int(params[0])
            event_id = int(params[1])

            self.__person_event_service.add_person_to_event(person_id, event_id)
            print("SUCCESS: person was successfully added to the event...")
        except ValueError:
            raise UIError("ERROR: 'id' must be a positive numeric value...")
        except RepoError as err:
            raise UIError(err)

    def __ui_remove_person_from_event(self, params: list) -> None:
        """
        Interface to delete person attending Event object.

        Args:
            params (list): list of function arguments

        Return: None
        """

        if len(params) != 2:
            print(f"ERROR: function 'remove_person_from_event' takes 2 arguments but {len(params)} were given...")
            return

        try:
            person_id = int(params[0])
            event_id = int(params[1])

            self.__person_event_service.remove_person_from_event(person_id, event_id)
            print("SUCCESS: person was successfully deleted from the event...")
        except ValueError:
            raise UIError("ERROR: 'id' must be a positive numeric value...")
        except RepoError as err:
            raise UIError(err)

    def __ui_event_display_persons(self, params: list) -> None:
        """
        Interface to display all Event objects person attends.

        Args:
            params (list): list of function arguments

        Return: None
        """

        if len(params) != 1:
            print(f"ERROR: function 'event_display_persons' takes 1 arguments but {len(params)} were given...")
            return

        try:
            id = int(params[0])
            persons = self.__person_event_service.get_event_persons(id)
            if len(persons) == 0:
                print("No persons attending this event...")
            else:
                for person in persons:
                    print(person)
        except ValueError:
            raise UIError("ERROR: 'id' must be a positive numeric value...")
        except RepoError as err:
            raise UIError(err)

    def __ui_person_events_number(self, params: list) -> None:
        """
        Interface to display number of all Event objects person attends.

        Args:
            params (list): list of function arguments

        Return: None
        """

        if len(params) != 1:
            print(f"ERROR: function 'person_events_number' takes 1 arguments but {len(params)} were given...")
            return

        try:
            id = int(params[0])
            events_number = self.__person_event_service.person_number_events(id)
            print(f"Person attends {events_number} events...")
        except ValueError:
            raise UIError("ERROR: 'id' must be a positive numeric value...")
        except RepoError as err:
            raise UIError(err)

    def __ui_top_events(self, params: list) -> None:
        """
        Interface to display first 20% Event objects with most participants decreasing.

        Args:
            params (list): list of function arguments

        Return: None
        """

        if len(params) != 0:
            print(f"ERROR: function 'top_events' takes 0 arguments but {len(params)} were given...")
            return

        events = self.__person_event_service.get_top_events()
        if len(events) == 0:
            print("No persons attending any event...")
        else:
            for event in events:
                print(event)

    def __ui_top_persons(self, params: list) -> None:
        """
        Interface to display first 20% Person objects with most attending events decreasing.

        Args:
            params (list): list of function arguments

        Return: None
        """

        if len(params) != 0:
            print(f"ERROR: function 'top_persons' takes 0 arguments but {len(params)} were given...")
            return

        persons = self.__person_event_service.get_top_persons()
        if len(persons) == 0:
            print("No persons attending any event...")
        else:
            for person in persons:
                print(person)

    @staticmethod
    def __ui_exit_program(params: list) -> None:
        """
        Interface to exit the program.

        Args:
            params (list): list of function arguments

        Return: None
        """

        if len(params) != 0:
            print(f"ERROR: function 'commands' takes 0 arguments but {len(params)} were given...")
            return

        print("Exiting program...")
        time.sleep(1.5)
        clear_screen()
        exit()

    def run(self) -> None:
        """
        Interface for I/O.

        Return: None
        """

        print("Use \"commands\" to show available options. ", end='')
        while True:
            command = input("\n>>> ")
            try:
                tokens = [token.strip() for token in command.split()]
                command_name = tokens[0]
                params = tokens[1:]
                if command_name in self.__commands:
                    try:
                        self.__commands[command_name][0](params)
                    except Exception as exception:
                        print(exception)
                else:
                    print(f"ERROR: invalid command '{command_name}'...")
            except IndexError:
                print(f"ERROR: command must not be blank...")


def clear_screen() -> None:
    print(
        "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

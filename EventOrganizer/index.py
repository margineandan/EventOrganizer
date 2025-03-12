from tests.testing import Tests
from validation.person_validator import PersonValidator
from validation.event_validator import EventValidator
from infrastructure.person_repository import FilePersonRepository
from infrastructure.event_repository import FileEventRepository
from infrastructure.person_event_repository import FilePersonEventRepository
from service.person_service import PersonService
from service.event_service import EventService
from service.person_event_service import PersonEventService
from ui.console import Console
from ui.console import clear_screen


def main() -> None:
    """
    Main function of the application.

    Return: None
    """
    clear_screen()

    tester = Tests()
    tester.run_tests()

    person_validator = PersonValidator()
    event_validator = EventValidator()

    person_repository = FilePersonRepository(
        r"C:\Users\margi\PycharmProjects\EventOrganizer\infrastructure\persons.txt")
    event_repository = FileEventRepository(
        r"C:\Users\margi\PycharmProjects\EventOrganizer\infrastructure\events.txt")
    person_event_repository = FilePersonEventRepository(
        r"C:\Users\margi\PycharmProjects\EventOrganizer\infrastructure\person_event.txt")

    person_service = PersonService(person_repository, person_validator)
    event_service = EventService(event_repository, event_validator)
    person_event_service = PersonEventService(person_repository, event_repository, person_event_repository)

    console = Console(person_service, event_service, person_event_service)
    console.run()


if __name__ == "__main__":
    main()

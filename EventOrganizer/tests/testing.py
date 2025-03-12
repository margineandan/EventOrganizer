from domain.person import Person
from domain.event import Event
from infrastructure.person_repository import PersonRepository
from infrastructure.event_repository import EventRepository
from validation.functions import Functions


class Tests:

    def __init__(self) -> None:
        self.__person_repository = PersonRepository()
        self.__event_repository = EventRepository()
        person = Person(1, "Dan", "Tudor23")
        self.__person_repository.add_person(person)
        person = Person(2, "Alex", "Principala1")
        self.__person_repository.add_person(person)
        event = Event(1, "2020-10-10", "18:00", "Concurs de informatica")
        self.__event_repository.add_event(event)
        event = Event(2, "2020-10-11", "00:00", "Balul Bobocilor UBB")
        self.__event_repository.add_event(event)

    def test_add_person(self) -> None:
        person = Person(3, "Gigi", "Vantului22")
        self.__person_repository.add_person(person)
        person = self.__person_repository.search_person(3)
        assert person is not None
        assert person.get_id() == 3
        assert person.get_name() == "Gigi"
        assert person.get_address() == "Vantului22"

    def test_create_person(self) -> None:
        person = Person(3, "Alex", "AurelVlaicu184")
        assert person.get_id() == 3
        assert person.get_name() == "Alex"
        assert person.get_address() == "AurelVlaicu184"

    def test_create_event(self) -> None:
        event = Event(3, "11-14-2023", "20:00", "Untold Festival")
        assert event.get_id() == 3
        assert event.get_date() == "11-14-2023"
        assert event.get_time() == "20:00"
        assert event.get_description() == "Untold Festival"

    def test_equal_person(self) -> None:
        person_1 = Person(1, "Alex", "Aurel Vlaicu 184")
        person_2 = Person(1, "Dan", "Principala 72")
        assert person_1 == person_2

    def test_equal_event(self) -> None:
        event_1 = Event(1, "11-08-2023", "22:00", "Untold Festival")
        event_2 = Event(1, "01-01-2024", "00:00", "New Years Party")
        assert event_1 == event_2

    def test_validate_address(self) -> None:
        validate = Functions()
        isTrue = validate.validate_address("Grigorescu32")
        isFalse = validate.validate_address("CaleaMotiilor")
        assert isTrue == True
        assert isFalse == False

    def test_validate_numeric(self) -> None:
        validate = Functions()
        isTrue = validate.validate_numeric("12")
        isFalse = validate.validate_numeric("12A")
        assert isTrue == True
        assert isFalse == False

    def test_validate_name(self) -> None:
        validate = Functions()
        isTrue = validate.validate_name("Dan")
        isFalse = validate.validate_name("Dan1")
        assert isTrue == True
        assert isFalse == False

    def test_validate_date(self) -> None:
        validate = Functions()
        isTrue = validate.validate_date("2023-12-10")
        isFalse = validate.validate_date("2023-12-NU")
        assert isTrue == True
        assert isFalse == False
        isFalse = validate.validate_date("202-12-10")
        assert isFalse == False
        isFalse = validate.validate_date("2023-122-10")
        assert isFalse == False
        isFalse = validate.validate_date("2023-12-100")
        assert isFalse == False
        isTrue = validate.validate_date("2023-01-01")
        isFalse = validate.validate_date("2023-99-99")
        assert isTrue == True
        assert isFalse == False

    def test_validate_time(self) -> None:
        validate = Functions()
        isTrue = validate.validate_time("13:22")
        isFalse = validate.validate_time("DA:NU")
        assert isTrue == True
        assert isFalse == False
        isFalse = validate.validate_time("25:00")
        assert isFalse == False
        isFalse = validate.validate_time("20:60")
        assert isFalse == False
        isFalse = validate.validate_time("200:00")
        assert isFalse == False
        isFalse = validate.validate_time("22:000")
        assert isFalse == False
        isFalse = validate.validate_time("22 : 00")
        assert isFalse == False
        isFalse = validate.validate_time("00-00")
        assert isFalse == False

    def run_tests(self) -> None:
        print("Running tests...")
        self.test_validate_time()
        self.test_validate_date()
        self.test_validate_name()
        self.test_validate_numeric()
        self.test_create_person()
        self.test_add_person()
        self.test_create_event()
        self.test_equal_event()
        self.test_equal_person()
        self.test_validate_address()
        print("Tests ran successfully!")

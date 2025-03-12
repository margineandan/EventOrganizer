from validation.functions import Functions
from exceptions.valid_exc import ValidError


class PersonValidator(Functions):
    """
    Class definition for person validator.

    Args:
        Functions (Functions): inherited class

    Methods:
        validate_person: check if Person object is correctly defined
    """

    def validate_person(self, person) -> None:
        """
        Check if Person object is correctly defined.

        Args:
            person (Person): Person object to check

        Raises:
            Exception: Person object is not correctly defined

        Return: None
        """

        errors = ""
        if person.get_id() < 0:
            errors += "ERROR: 'id' must be a positive numeric value...\n"
        if not self.validate_name(person.get_name()):
            errors += "ERROR: 'name' must be an alphabetic value...\n"
        if not self.validate_address(person.get_address()):
            errors += "ERROR: 'address' is invalid...\n"

        if len(errors) > 0:
            errors = errors[:-1]
            raise ValidError(errors)

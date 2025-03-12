from validation.functions import Functions
from exceptions.valid_exc import ValidError


class EventValidator(Functions):
    """
    Class definition for event validator.

    Args:
        Functions (Functions): inherited class

    Methods:
        validate_event: check if Event object is correctly defined
    """

    def validate_event(self, event) -> None:
        """
        Check if Event object is correctly defined.

        Args:
            event (Event): Event object to check

        Raises:
            Exception: Event object is not correctly defined

        Return: None
        """

        errors = ""
        if not self.validate_date(event.get_date()):
            errors += "ERROR: 'date' must have valid 'year-month-day' format...\n"
        if not self.validate_time(event.get_time()):
            errors += "ERROR: 'time' must have valid 'hour:minute' format...\n"

        if len(errors) > 0:
            errors = errors[:-1]
            raise ValidError(errors)

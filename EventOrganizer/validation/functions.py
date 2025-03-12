import re
import datetime
from exceptions.valid_exc import ValidError


class Functions:
    """
    Class definition for Functions.

    Methods:
        validate_name: check if string value is alphabetic
        validate_address: check if string value is valid email address
        validate_date: check if string value is valid calendaristic date
        validate_time: check if string value is valid time
        compare_dates: compare two calendaristic dates
    """

    @staticmethod
    def validate_numeric(input_string: str) -> bool:
        """
        Check if string is numeric.

        Args:
            input_string (str): string to check

        Returns: bool
        """
        try:
            value = int(input_string)
            return value > 0
        except ValueError:
            return False

    @staticmethod
    def validate_name(string_value: str) -> bool:
        """
        Check if string value is alphabetic.

        Args:
            string_value (str): string value to check

        Returns: bool
        """

        if len(string_value) < 3:
            raise ValidError("ERROR: name must have at least 3 characters...")

        return string_value.isalpha()

    @staticmethod
    def validate_address(input_string: str) -> bool:
        """
        Check if string is a valid address.

        Args:
            input_string (str): string value to check

        Returns: bool
        """
        pattern = re.compile(r'^[a-zA-Z]+\d+$')

        if pattern.match(input_string):
            return True
        return False

    @staticmethod
    def validate_date(string_value: str) -> bool:
        """
        Check if string value is valid calendaristic date.

        Args:
            string_value (str): string value to check

        Returns: bool
        """

        try:
            datetime.datetime.strptime(string_value, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    @staticmethod
    def validate_time(string_value: str) -> bool:
        """
        Check if string value is valid time.

        Args:
            string_value (str): string value to check

        Returns: bool
        """

        pattern = re.compile(r'^(?:[01]?\d|2[0-3]):[0-5]\d$')
        return bool(pattern.match(string_value))

    @staticmethod
    def compare_dates(string_value_1: str, string_value_2: str) -> bool:
        """
        Compare two calendaristic dates.

        Args:
            string_value_1 (str): first string value to compare
            string_value_2 (str): second string value to compare

        Returns: bool
        """

        date_1 = datetime.datetime.strptime(string_value_1, '%Y-%m-%d')
        date_2 = datetime.datetime.strptime(string_value_2, '%Y-%m-%d')
        return date_1 > date_2

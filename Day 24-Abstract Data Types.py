from datetime import date

class Person:
    def __init__(self, name):
        """
        Initializes a Person object.
        Abstracts internal storage of names.
        """
        self._name = name

        # Try to extract last name from full name
        try:
            last_space = name.rindex(' ')
            self._last_name = name[last_space+1:]
        except ValueError:
            # If no space, use full name as last name
            self._last_name = name

        self._birthday = None  # Encapsulated birthday info

    def get_name(self):
        """Returns the full name of the person."""
        return self._name

    def get_last_name(self):
        """Returns the person's last name."""
        return self._last_name

    def set_birthday(self, birthdate):
        """
        Sets the birthday. Expects a datetime.date object.
        """
        self._birthday = birthdate

    def get_age(self):
        """
        Returns the age in days.
        Handles the logic internally so user doesn't need to.
        """
        if self._birthday is None:
            raise ValueError("Birthday not set.")
        return (date.today() - self._birthday).days

    def __lt__(self, other):
        """
        Compares two Person objects alphabetically.
        Sorts by last name, then full name if tied.
        """
        if self._last_name == other._last_name:
            return self._name < other._name
        return self._last_name < other._last_name

    def __str__(self):
        """Returns a string representation (just the name)."""
        return self._name

# -------------------------------
# Example Usage (Demo Section)
# -------------------------------

if __name__ == "__main__":
    # Creating two Person objects
    p1 = Person("Adebayo Tunde")
    p2 = Person("Chukwu Ada")

    # Setting birthday
    p1.set_birthday(date(2000, 5, 20))
    p2.set_birthday(date(1998, 8, 14))

    # Printing age
    print(f"{p1.get_name()} is {p1.get_age()} days old.")
    print(f"{p2.get_name()} is {p2.get_age()} days old.")

    # Sorting example
    people = [p1, p2]
    people.sort()

    print("\nSorted List:")
    for person in people:
        print(person)

class Baker:
    """Class baker."""

    def __init__(self, name: str, experience_level: int, money: int):
        """Class constructor."""
        self.name = name
        self.experience_level = experience_level
        self.money = money

    def __str__(self):
        """Represent object in string format."""
        return "Baker: {}({})".format(self.name, self.experience_level)

    def __repr__(self):
        """Represent object in string format."""
        return "Baker: {}({})".format(self.name, self.experience_level)

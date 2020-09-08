class Pastry:
    """Pastry class."""

    def __init__(self, name: str, complexity_level: int):
        """Class constructor."""
        self.name = name
        self.complexity_level = complexity_level

    def __repr__(self):
        """Represent object in string format."""
        return self.name

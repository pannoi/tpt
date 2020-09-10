class Bakery:
    """Class bakery."""

    def __init__(self, name: str, min_experience_level: int, budget: int):
        """Class constructor."""
        self.name = name
        self.min_experience_level = min_experience_level
        self.budget = budget
        self.recipes = {}
        self.bakers = []
        self.pastries = []

    def add_baker(self, baker: Baker) -> Baker:
        """Add baker."""
        pass

    def remove_baker(self, baker: Baker):
        """Remove baker."""
        pass

    def add_recipe(self, name: str):
        """Add recipe."""
        pass

    def make_order(self, name: str) -> Pastry:
        """Make order."""
        pass

    def get_recipes(self) -> dict:
        """Get recipes."""
        pass

    def get_pastries(self) -> list:
        """Get pastries."""
        pass

    def get_bakers(self) -> list:
        """Get baker."""
        pass
    
    def __str__(self):
        """Represent object in string format."""
        return "Bakery {}: {} baker(s)".format(self.name, len(self.bakers))

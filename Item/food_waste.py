class FoodWaste:
    """
    This class represents an instance of food waste.

    It has a name, type, description, source, where to throw, image, time to decay, and carbon footprint.
    """

    def __init__(self, id, name, type, description, source, where_to_throw, image, time_to_decay, carbon_footprint):
        """
        This is the constructor for the FoodWaste class.

        It takes a id, name, type, description, source, where_to_throw, image, time_to_decay, and carbon_footprint as arguments.
        """
        self.id = id
        self.name = name
        self.type = type
        self.description = description
        self.source = source
        self.where_to_throw = where_to_throw
        self.image = image
        self.time_to_decay = time_to_decay
        self.carbon_footprint = carbon_footprint

    def __str__(self):
        """
        This method is used to represent the FoodWaste class as a string.
        """
        return f"{self.name} ({self.type}) - {self.description}"

    def get_fields(self):
        """
        This method returns a list of dictionaries, where each dictionary represents a field in the FoodWaste class.
        """
        fields = [
            {'name': 'id', 'purpose': 'The unique identifier for the food waste', 'data_type': type(self.id).__name__, 'constraints': ''},
            {'name': 'name', 'purpose': 'The name of the food waste', 'data_type': type(self.name).__name__, 'constraints': ''},
            {'name': 'type', 'purpose': 'The type of the food waste', 'data_type': type(self.type).__name__, 'constraints': ''},
            {'name': 'description', 'purpose': 'The description of the food waste', 'data_type': type(self.description).__name__, 'constraints': ''},
            {'name': 'source', 'purpose': 'The source of the food waste', 'data_type': type(self.source).__name__, 'constraints': ''},
            {'name': 'where_to_throw', 'purpose': 'Where to throw the food waste', 'data_type': type(self.where_to_throw).__name__, 'constraints': ''},
            {'name': 'image', 'purpose': 'The image of the food waste', 'data_type': type(self.image).__name__, 'constraints': ''},
            {'name': 'time_to_decay', 'purpose': 'The time it takes for the food waste to decay', 'data_type': type(self.time_to_decay).__name__, 'constraints': ''},
            {'name': 'carbon_footprint', 'purpose': 'The carbon footprint of the food waste', 'data_type': type(self.carbon_footprint).__name__, 'constraints': ''},
        ]
        return fields


class Item:
    """
    This class is used to represent an item.

    It has a name, description, and price and image.
    """

    def __init__(self,id,  name, description, price,in_stock, image):
        """
        This is the constructor for the Item class.

        It takes a id, name, description, price, in_stock and image as arguments.
        """
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.image = image
        self.in_stock = in_stock

    def __str__(self):
        """
        This method is used to represent the Item class as a string.
        """ 
    
    def get_item_id(self):
        """
        This method returns the id of the item.
        """
        return self.id

    def get_fields(self):
        """
        This method returns a list of dictionaries, where each dictionary represents a field in the Item class.
        """
        fields = [
            {'name': 'id', 'purpose': 'The unique identifier for the item', 'data_type': type(self.id).__name__, 'constraints': ''},
            {'name': 'name', 'purpose': 'The name of the item', 'data_type': type(self.name).__name__, 'constraints': ''},
            {'name': 'description', 'purpose': 'The description of the item', 'data_type': type(self.description).__name__, 'constraints': ''},
            {'name': 'price', 'purpose': 'The price of the item', 'data_type': type(self.price).__name__, 'constraints': ''},
            {'name': 'image', 'purpose': 'The image of the item', 'data_type': type(self.image).__name__, 'constraints': ''},
            {'name': 'in_stock', 'purpose': 'Whether the item is in stock or not', 'data_type': type(self.in_stock).__name__, 'constraints': ''},
        ]
        return fields
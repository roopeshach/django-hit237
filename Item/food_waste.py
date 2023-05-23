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


food_waste = [
FoodWaste(1, 
          "Bread", 
          "Starchy food", 
          "Bread is a staple food made from flour and water, and often contains other ingredients such as yeast, salt, and sugar. It is commonly consumed as a snack or as part of a meal.", 
          "Bakeries, supermarkets, households", 
          "Composting, landfill", 
          "https://magazinebbm.com/assets/img/uploads/en-US/2019/08/Bread3.jpg", 
          "1-2 weeks", 
          "0.6 kg CO2 equivalent per kg of bread"),
FoodWaste(2, 
          "Banana peel", 
          "Fruit waste", 
          "Banana peel is the outer layer of a banana fruit, which is typically discarded after consumption. It is rich in nutrients such as potassium and fiber, and can be used in a variety of ways.", 
          "Households, restaurants, supermarkets", 
          "Composting", 
          "https://www.conserve-energy-future.com/wp-content/uploads/2021/02/banana-peels.jpg", 
          "2-4 weeks", 
          "0.08 kg CO2 equivalent per kg of banana peel"),
FoodWaste(3, 
          "Eggshells", 
          "Protein waste", 
          "Eggshells are the hard outer layer of an egg, which are typically discarded after use. They are composed mainly of calcium carbonate and can be used in a variety of ways.", 
          "Households, restaurants, food processing plants", 
          "Composting", 
          "https://d2cbg94ubxgsnp.cloudfront.net/Pictures/480xAny/5/8/8/125588_eggshells_410_tcm18-208338.jpg", 
          "1-2 years", 
          "0.06 kg CO2 equivalent per kg of eggshells"),
FoodWaste(4, 
          "Coffee grounds", 
          "Beverage waste", 
          "Coffee grounds are the leftover residue from brewing coffee, and are typically discarded after use. They contain caffeine and other compounds that can be beneficial in various applications.", 
          "Households, coffee shops, restaurants", 
          "Composting", 
          "https://c.files.bbci.co.uk/0D2F/production/_106557330_mediaitem106557329.jpg", 
          "2-5 weeks", 
          "0.35 kg CO2 equivalent per kg of coffee grounds"),
FoodWaste(5, 
          "Potato peels", 
          "Starchy food waste", 
          "Potato peels are the outer layer of a potato, which are typically removed before cooking. They are rich in nutrients and can be used in a variety of ways.", 
          "Households, restaurants, food processing plants", 
          "Composting", 
          "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYyAxx3J7xdumBT2Vu3wl-l7KPpD0O-jEwdg&usqp=CAU", 
          "2-4 weeks", 
          "0.05 kg CO2 equivalent per kg of potato peels"),
FoodWaste(6, 
          "Apple peels", 
          "Fruit waste", 
          "Apple peels are the outer layer of an apple, which are typically discarded after consumption. They are rich in nutrients and can be used in a variety of ways.", 
          "Households, restaurants, food processing plants", 
          "Composting", 
          "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTwLV5zxgCP07bk6F-JOY9LAJp-q0gQjH5ycQ&usqp=CAU",
          "2-4 weeks", 
          "0.05 kg CO2 equivalent per kg of apple peels"),
]

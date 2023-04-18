from django.shortcuts import render
from .food_waste import FoodWaste

# Create your views here.
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


def index(request):
    '''
    This function is used to render the index.html template, 
    which is the home page of the website.

    It also passes the list of students and the intro paragraph to the template.
  
    '''
    #
    #  a list of dictionaries that contains the name and roll number of students
    students = [
        {'name': 'Yugant Patel ', 'roll': 'S356344'},
        {'name': 'Suman Rimal', 'roll': 'S361104'},
        {'name': 'Kowsik Tiash', 'roll': 'S357478'},
        {'name': 'AN Nguyen', 'roll': 'S356095'},

    ]

    #  a brief paragraph that introduces the website 
    intro = """
   <h2>About Food Waste</h2>
    <p>
    This website provides information about different types of food waste, including their name, type, description, source, where to throw, time to decay, and carbon footprint.
    </p>
    <p>
    FoodWaste is a model that has attributes like name, type, description, source, where_to_throw, image, time_to_decay, and carbon_footprint. With separate pages for each food waste item, you can view its details and learn more about how to reduce food waste and properly dispose of it.
    </p>
    <h3>Features</h3>
    <ul>
    <li>Clickable links for every food waste's page.</li>
    <li>Easily navigate through navbar.</li>
    <li>Images to help identify each food waste item.</li>
    <li>Information on how to properly dispose of each type of food waste to reduce environmental impact.</li>
    </ul>
    <h3>How to use</h3>
    <p>
    To view the list of food waste items, click on the "Food Waste" link in the navbar. To view the details of a particular food waste item, click on the name of the item. To view the data model of the FoodWaste class, click on the "Data Model" link in the navbar.
    </p>



    """

    context = {
        'students': students,
        'intro': intro,
    }
   
    return render(request, "Item/index.html", context)


def food_waste_list(request):

    '''
        This function is used to render the food_waste_list.html template,
        which is the page that shows the list of food waste items.
    '''
    context = {
        'food_waste': food_waste,
    }
    return render(request, "Item/food_waste.html", context)

def food_waste_detail(request, food_waste_id):
    '''
        This function is used to render the food_waste_detail.html template,
        which is the page that shows the details of a particular food waste item.
    '''
    waste = food_waste[food_waste_id - 1]
    context = {
        'waste': waste,
    }
    return render(request, "Item/foodwaste_page.html", context)

def data_model(request):
    '''
        This function is used to render the data_model.html template,
        which is the page that shows the data model of the Item Class.
    '''
    waste = food_waste[0]
    context = {
        'data_model': waste.get_fields(),
    }
    
    return render(request, "Item/data_model.html", context)
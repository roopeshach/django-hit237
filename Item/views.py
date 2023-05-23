from django.shortcuts import render
from .food_waste import FoodWaste, food_waste

# Create your views here.


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


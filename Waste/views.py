from django.shortcuts import render, redirect
from .models import Student

# Create your views here.

def index(request):
    students = Student.objects.all()
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
    return render(request, 'Waste/index.html', context)


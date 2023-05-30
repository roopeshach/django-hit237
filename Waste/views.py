from django.shortcuts import render, redirect
from .models import Student

# Create your views here.

def index(request):
    students = Student.objects.all()
    #  a brief paragraph that introduces the website 
    intro = """
   <h2>About Food Waste</h2>
    <p>Welcome to our Django website! We are proud to present a platform that aims to raise awareness about waste management and promote sustainable practices. Our website provides valuable information on various waste types and their impact on the environment.</p>

    <p>Through our comprehensive database, you can explore different categories of waste, such as food waste, and learn about their sources, how to dispose of them properly, and their environmental consequences. Our dedicated team of students has worked diligently to create a user-friendly interface that allows you to navigate effortlessly through the website and access essential information.</p>

    <p>Using Django's dynamic database storage, we ensure that the information on our website is constantly updated and easily accessible. The website incorporates Django ModelForms, enabling you to interact with the database by submitting user input that can influence waste management practices.</p>

    <p>With full CRUD functionality for each table in our data model, you have the ability to create, read, update, and delete records seamlessly. Whether you want to add new waste types, contribute information about food waste, or explore sustainable food recovery methods, our website provides a robust platform for managing waste-related data.</p>

    <p>All hyperlinks on our website are constructed using named URL Paths and the {% url %} template tag, ensuring a consistent and efficient navigation experience. The website adheres to standard HTML5 syntax and incorporates essential formatting elements, such as headers, tables, hyperlinks, and text formatting, to enhance readability and usability.</p>

    <p>Our data model includes multiple related classes, including Student, WasteType, FoodWaste, and FoodRecovery, with appropriate relationships defined using Django's model fields. Furthermore, we have provided a sample dataset with primary and secondary records associated with each primary record, ensuring a meaningful and realistic representation of waste management data.</p>

    <p>Visit our website and join us in our mission to promote sustainable waste management practices. Together, we can make a positive impact on the environment and create a greener future for generations to come.</p>

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


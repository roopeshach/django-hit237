from django.shortcuts import render
from .item import Item

# Create your views here.
items = [
        Item(1, "Apple", "A red fruit", 1.5, True, "https://images.unsplash.com/photo-1600423115367-87ea7661688f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTV8fGZydWl0fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60"),
        Item(2, "Banana", "A yellow fruit", 2.5, True, "https://images.unsplash.com/photo-1528825871115-3581a5387919?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Nnx8ZnJ1aXR8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60"),
        Item(3, "Orange", "A orange fruit", 4.5, True, "https://plus.unsplash.com/premium_photo-1669631947841-f5913ec5602e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8ZnJ1aXR8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60"),
        Item(4, "Mango", "A yellow fruit", 1, True, "https://plus.unsplash.com/premium_photo-1675731118152-67e6032a543e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NTV8fGZydWl0fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60"),
        Item(5, "Pineapple", "A yellow fruit", 1.5, True, "https://images.unsplash.com/photo-1550258987-190a2d41a8ba?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8ZnJ1aXR8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60"),
        Item(6, "Watermelon", "A green fruit", 21.5, True, "https://images.unsplash.com/photo-1595475207225-428b62bda831?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MjR8fGZydWl0fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60"),
        Item(7, "Grapes", "A purple fruit", 4.9, True, "https://images.unsplash.com/photo-1604132847935-2fa64ea9c4a5?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NjZ8fGZydWl0fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60"),
        Item(8, "Strawberry", "A red fruit", 3.5, True, "https://images.unsplash.com/photo-1601004890684-d8cbf643f5f2?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8ZnJ1aXR8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60"),
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
        {'name': 'Ramesh Basnet', 'roll': 'TA-13421'},
        {'name': 'Binesh Kumar', 'roll': 'TA-13422'},
        {'name': 'Jarvis Gurung', 'roll': 'TA-13423'},

    ]

    #  a brief paragraph that introduces the website 
    intro = """
    <h2>About this website.</h2>
    <p>
    This is a website that allows you to keep track of your items.
    you can add, edit, and delete items.
    </p>
    <p>
    Item is a model that has a name, description, and price.
    With separate pages for each item, you can view its details.
    </p>
    <h3>Features</h3>
    <li>Clickable links for every product's page.</li>
    <li>Easily navigation through navbar. </li>
    </ul>
    """

    context = {
        'students': students,
        'intro': intro,
    }
   
    return render(request, "Item/index.html", context)



def item_list(request):
    """
    This function is used to render the items.html template,
    which is the page that lists all the items.

    It also passes the list of items to the template.
    """

    

    context = {
        'items': items,
    }

    return render(request, "Item/items.html", context)

def item_detail(request, item_id):
    """
    This function is used to render the item_detail.html template,
    which is the page that shows the details of a particular item.

    It also passes the item details to the template.
    """

    

    item = None
    for i in items:
        if i.get_item_id() == item_id:
            item = i
            break

    context = {
        'item': item,
    }


    return render(request, "Item/item_page.html", context)

def data_model(request):
    '''
        This function is used to render the data_model.html template,
        which is the page that shows the data model of the Item Class.
    '''
    item = items[0]
    context = {
        'data_model': item.get_fields(),
    }
    
    return render(request, "Item/data_model.html", context)
# Project 3

Web Programming with Python and JavaScript

## Authentication
Login at http://127.0.0.1:8000/users/

Register at http://127.0.0.1:8000/users/register

Logout at http://127.0.0.1:8000/users/logout




### Requirements


1. Menu: Your web application should support all of the available menu items for Pinnochio’s Pizza & Subs (a popular pizza place in Cambridge). It’s up to you, based on analyzing the menu and the various types of possible ordered items (small vs. large, toppings, additions, etc.) to decide how to construct your models to best represent the information. Add your models to orders/models.py, make the necessary migration files, and apply those migrations.

2. Adding Items: Using Django Admin, site administrators (restaurant owners) should be able to add, update, and remove items on the menu. Add all of the items from the Pinnochio’s menu into your database using either the Admin UI or by running Python commands in Django’s shell.

3. Registration, Login, Logout: Site users (customers) should be able to register for your web application with a username, password, first name, last name, and email address. Customers should then be able to log in and log out of your website.
4. Shopping Cart: Once logged in, users should see a representation of the restaurant’s menu, where they can add items (along with toppings or extras, if appropriate) to their virtual “shopping cart.” The contents of the shopping should be saved even if a user closes the window, or logs out and logs back in again.
5. Placing an Order: Once there is at least one item in a user’s shopping cart, they should be able to place an order, whereby the user is asked to confirm the items in the shopping cart, and the total (no need to worry about tax!) before placing an order.

4. Viewing Orders: Site administrators should have access to a page where they can view any orders that have already been placed.
 
5. Personal Touch: Add at least one additional feature of your choosing to the web application. Possibilities include: allowing site administrators to mark orders as complete and allowing users to see the status of their pending or completed orders, integrating with the Stripe API to allow users to actually use a credit card to make a purchase during checkout, or supporting sending users a confirmation email once their purchase is complete. If you need to use any credentials (like passwords or API credentials) for your personal touch, be sure not to store any credentials in your source code, better to use environment variables!

6. In README.md, include a short writeup describing your project, what’s contained in each file you created or modified, and (optionally) any other additional information the staff should know about your project. Also, include a description of your personal touch and what you chose to add to the project.

7. If you’ve added any Python packages that need to be installed in order to run your web application, be sure to add them to requirements.txt!

Beyond these requirements, the design, look, and feel of the website are up to you! You’re also welcome to add additional features to your website, so long as you meet the requirements laid out in the above specification!

### Milestones
1. Complete the Menu, Adding Items, and Registration/Login/Logout steps by April 1.
1. Complete the Shopping Cart and Placing an Order steps by April 8.
1. Complete the Viewing Orders and Personal Touch steps by April 15.

### User Data
#### Toppings
Pepperoni
Sausage
Mushrooms
Onions
Ham
Canadian Bacon
Pineapple
Eggplant
Tomato & Basil
Green Peppers
Hamburger
Spinach
Artichoke
Buffalo Chicken
Barbecue Chicken
Anchovies
Black Olives
Fresh Garlic
Zucchini

Regular Pizza
Small	Large
Cheese	12.20	17.45
1 topping	13.20	19.45
2 toppings	14.70	21.45
3 toppings	15.70	23.45
Special	17.25	25.45

Sicilian Pizza
Small	Large
Cheese	23.45	37.70
1 item	25.45	39.70
2 items	27.45	41.70
3 items	28.45	43.70
Special	29.45	44.70

Subs
Small	Large
Cheese	6.50	7.95
Italian	6.50	7.95
Ham + Cheese	6.50	7.95
Meatball	6.50	7.95
Tuna	6.50	7.95
Turkey	7.50	8.50
Chicken Parmigiana	7.50	8.50
Eggplant Parmigiana	6.50	7.95
Steak	6.50	7.95
Steak + Cheese	6.95	8.50
+ Mushrooms	+0.50	+0.50
+ Green Peppers	+0.50	+0.50
+ Onions	+0.50	+0.50
Sausage, Peppers & Onions		8.50
Hamburger	4.60	6.95
Cheeseburger	5.10	7.45
Fried Chicken	6.95	8.50
Veggie	6.95	8.50
Extra Cheese on any sub	+0.50	+0.50

Pasta
Baked Ziti w/Mozzarella	6.50
Baked Ziti w/Meatballs	8.75
Baked Ziti w/Chicken	9.75


Salads
Garden Salad	6.25
Greek Salad	8.25
Antipasto	8.25
Salad w/Tuna	8.25
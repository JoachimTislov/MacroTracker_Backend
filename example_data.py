###### DISCLAIMER ######

# Most of this is written by CHATgpt 

# Its a time consuming task and therefore we used chatgpt 

###### EXAMPLE USERS ######
users_data = [
    ("Per", "Peddi", "peder@123", "per.ole@gmail.com", 23, None, 70, 175, 1, 3), # Male, Moderately Active
]

###### EXAMPLE MEALS #######

### Adding personal meals for Peddi with user id 1###
personal_meals_data = [
    # MEAL NAME  # USER ID # Protein # Calories # Carbohydrates # Fat # Sugar
    ('Chicken Salad', 1, 21.5, 180, 7, 5, 3),
    ('Vegetable Stir-Fry', 1, 3.5, 60, 14, 0, 8),
    ('Salmon with Rice', 1, 35, 700, 95, 12, 2),
    ('Pasta Primavera', 1, 34, 460, 15, 20, 8),
    ('Grilled Steak', 1, 8.5, 310, 42, 16, 1),
    ('Quinoa Salad', 1, 18, 200, 17, 10, 8),
    ('Tofu Stir-Fry', 1, 17.5, 240, 11, 12, 5),
    ('Eggplant Parmesan', 1, 21, 405, 22, 15, 11),
    ('Shrimp Scampi', 1, 34, 600, 55, 11, 11),
    ('Turkey Chili', 1, 9, 250, 5, 22, 1),
]

##### Ingredients for each meal ######

ingredients_for_each_meal_data = [
    # MEAL ID AND INGREDIENT ID #
    (1,1),(1,2),(1,3),
    (2,4),(2,5),(2,6),
    (3,7),(3,8),(3,9),
    (4,10),(4,11),(4,12),
    (5,13),(5,14),(5,15),
    (6,16),(6,17),(6,18),
    (7,19),(7,20),(7,21),
    (8,22),(8,23),(8,24),
    (9,25),(9,26),(9,27),
    (10,28),(10,29),(10,30)
]

###### Personal ingredients ######

personal_ingredients_data = [
    #USER ID # INGREDIENT NAME # AMOUNT # protein # calories # carbohydrates # fat # sugar
    (1, 'Chicken Breast', '200g', 20, 150, 0, 5, 0),
    (1, 'Lettuce', '100g', 1, 20, 5, 0, 2),
    (1, 'Tomato', '1', 0.5, 10, 2, 0, 1),
    (1, 'Broccoli', '150g', 2, 30, 7, 0, 3),
    (1, 'Carrots', '100g', 1, 20, 5, 0, 3),
    (1, 'Soy Sauce', '2 tbsp', 0.5, 10, 2, 0, 2),
    (1, 'Salmon Fillet', '150g', 20, 250, 0, 10, 0),
    (1, 'Rice', '1 cup', 5, 150, 35, 0, 0),
    (1, 'Pasta', '200g', 10, 300, 60, 2, 2),
    (1, 'Mixed Vegetables', '150g', 2, 30, 10, 0, 5),
    (1, 'Ribeye Steak', '250g', 30, 400, 0, 20, 0),
    (1, 'Asparagus', '150g', 2, 30, 5, 0, 3),
    (1, 'Butter', '1 tbsp', 0, 100, 0, 12, 0),
    (1, 'Quinoa', '1 cup', 8, 200, 40, 4, 0),
    (1, 'Cucumber', '1', 0.5, 10, 2, 0, 1),
    (1, 'Cherry Tomatoes', '100g', 1, 20, 5, 0, 2),
    (1, 'Tofu', '200g', 15, 150, 5, 10, 3),
    (1, 'Bell Peppers', '2', 2, 30, 7, 0, 3),
    (1, 'Soy Sauce', '2 tbsp', 0.5, 10, 2, 0, 2),
    (1, 'Eggplant', '1', 2, 30, 7, 0, 3),
    (1, 'Mozzarella Cheese', '100g', 15, 200, 2, 12, 0),
    (1, 'Marinara Sauce', '1 cup', 1, 150, 20, 5, 10),
    (1, 'Shrimp', '200g', 20, 250, 0, 10, 0),
    (1, 'Lemon Juice', '2 tbsp', 0, 5, 2, 0, 1),
    (1, 'Ground Turkey', '250g', 25, 300, 5, 10, 1),
    (1, 'Kidney Beans', '1 can', 7, 200, 30, 1, 0),
    (1, 'Tomato Sauce', '1 cup', 2, 100, 20, 0, 10),
    (1, 'Spinach', '100g', 2, 20, 4, 0, 1),
    (1, 'Olive Oil', '1 tbsp', 0, 120, 0, 14, 0),
    (1, 'Parmesan Cheese', '30g', 7, 110, 1, 8, 0)
]


###### Meals for each random date ######

meal_calender_data = [
    (1, "10-06-2024", "01:34:32"),
    (2, "11-06-2024", "09:12:05"),
    (3, "12-06-2024", "15:45:22"),
    (4, "13-06-2024", "10:20:17"),
    (5, "14-06-2024", "18:55:49"),
    (6, "15-06-2024", "07:30:10"),
    (7, "16-06-2024", "01:34:32"),
    (8, "17-06-2024", "09:12:05"),
    (9, "18-06-2024", "15:45:22"),
    (10, "19-06-2024", "10:20:17"),
    (1, "19-06-2024", "18:55:49"),
    (2, "18-06-2024", "07:30:10"),
    (3, "17-06-2024", "14:15:37"),
    (4, "16-06-2024", "11:22:08"),
    (5, "15-06-2024", "20:40:55"),
    (6, "14-06-2024", "08:05:19"),
    (7, "13-06-2024", "00:45:33"),
    (8, "12-06-2024", "13:10:12"),
    (9, "11-06-2024", "17:28:44"),
    (10, "10-06-2024", "06:52:59"),
    (1, "16-06-2024", "22:15:26"),
    (2, "15-06-2024", "05:08:03"),
    (3, "17-06-2024", "16:37:10"),
    (4, "14-06-2024", "12:04:58"),
    (5, "18-06-2024", "23:20:30"),
    (6, "13-06-2024", "09:36:17"),
    (7, "19-06-2024", "02:58:44"),
    (8, "12-06-2024", "14:25:56"),
    (9, "20-06-2024", "19:10:11"),
    (10, "23-06-2024", "08:44:27"),
    (1, "22-06-2024", "21:15:33"),
    (2, "24-06-2024", "04:07:59"),
    (3, "22-06-2024", "17:29:08"),
    (4, "21-06-2024", "13:10:22"),
    (5, "22-06-2024", "00:55:46"),
    (6, "23-06-2024", "10:25:57"),
    (7, "24-06-2024", "03:20:34"),
    (8, "25-06-2024", "15:05:02"),
    (9, "26-06-2024", "18:45:18"),
    (10, "23-06-2024", "07:36:29"),
]

        



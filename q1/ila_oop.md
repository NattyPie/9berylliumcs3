# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
    Enscapsulation can be used by creating a Product class that contains the product's name, price, and stock as its properties. Methods such as add_stock() and remove_stock() can be used to change the stock insted of changing it directly. This keeps the product's data organized and helps prevent unwanted changes to the inventory.

### 2. Abstraction
    Abstraction can be used by hiding complicated parts of the inventory system and only showing the functions that are needed. For example, the store owner can use a method such as sell_product() without needing to know how the system updates the stock internally. This makes the program easier to understand and use. 

### 3. Inheritance
    Inheritance can be used when different types of products share the same basic properties. For example, a FoodProduct and DrinkProduct could both have a display_info() method, but each could display information diffeerently. This makes the inventory system more flexible when new types of products are added.

### 4. Polymorphism
    Polymorphism allows different objects to use the same method name butperform the method in different ways. For example, a FoodProduct and DrinkProduct could both have a display_info() method, but each could display information differently. This makes the inventory system more flexible when new types f products are added.

## Reflection
    Among the four pillars of Object-Oriented Programming, I think encapsulation would be the most useful for the sari-sari store inventory system. It keeps important information such as the price and stock organized inside each product object. It also allows the program to control how the inventory is changed, which can help prevent mistakes. Overall, encapsulation would make the inventory system easier to manage and maintain. 
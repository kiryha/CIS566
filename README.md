# CIS566
UMICH CIS566 Course Project:
Software Architecture and Design Patterns

#### Split smart
The code provided is using the Model-View-Controller (MVC) architecture pattern.

In this pattern, the Model represents the data and the business logic, the View represents the user interface, and the 
Controller acts as an intermediary between the Model and the View, handling user input and updating the View based on changes in the Model.

In the given code, the ListModel and ComboboxModel classes are both Models that are used to represent different sets 
of data from a database. They implement the necessary methods required by the Qt framework for models, such as rowCount() and data().

The View is not shown in the code snippet provided, but it is likely implemented using Qt widgets that are bound to the Models. 
The Controller is also not explicitly shown in the code, but it would be responsible for handling user input events and updating the Models accordingly.

Therefore, the software architecture pattern used in this code is Model-View-Controller 

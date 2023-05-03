# Django_Assignment 

create a file named models.py .
Here, we have defined the Client, Artist, and Work models with the required fields. The Client model has a foreign key to the built-in User model to associate each client with a user.

Next, we need to create a signal to automatically create a Client object whenever a new user is registered.
In the same models.py file, add the  code: 
Here, we have defined a post_save signal that listens for the User model's save() method. When a new user is created, the create_client function is called, which creates a new Client object associated with the user.

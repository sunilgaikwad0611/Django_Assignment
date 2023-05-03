# Django_Assignment 

create a file named models.py .
Here, we have defined the Client, Artist, and Work models with the required fields. The Client model has a foreign key to the built-in User model to associate each client with a user.

Next, we need to create a signal to automatically create a Client object whenever a new user is registered.
In the same models.py file, add the  code: 
Here, we have defined a post_save signal that listens for the User model's save() method. When a new user is created, the create_client function is called, which creates a new Client object associated with the user.

Now creating views.py for rest api 

Now, let's move on to creating the REST API endpoints. In your Django project's app, create a file named views.py 

Here, we have defined two API endpoints: work_list and register.

The work_list endpoint returns a list of all works with their links, link types, and associated artists. It accepts two optional query parameters: artist and work_type, which can be used to filter the results by artist name and work type. 

The register endpoint accepts a POST request with the username and password in the request body and creates a new user with the provided credentials. It returns the newly created user's ID.

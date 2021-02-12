# sandbox-flask

This is a small service written with Python and Flask

If you would like to know more about Flask visit this [link](https://flask.palletsprojects.com/en/1.1.x/). 

To run this service just install python, install flask, install virtual-env (following the instructions listed in the documentation). 

This service runs in port 4000 and support the following operations:

- `/api/books` `GET`: An operation to retrieve a list of books
- `/api/book` `POST`: An operation to add a book
- `/api/books/<string:book_name>` `PUT`: let you update an existing book
- `/api/books/<string:book_name>` `DELETE`: let you delete an existing book

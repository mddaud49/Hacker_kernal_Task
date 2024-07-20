Library Management System

Overview
This Django application serves as a Library Management System, allowing users to manage authors, books, and borrowing records efficiently.

Features
Authors Management:

Add, view, and edit author details including name, email, and bio.
Ensure email validation during author addition.
Books Management:

Add, view, and edit book details such as title, genre, published date, and associated author.
Use a dropdown to select an author from existing records.
Borrow Records Management:

Track borrowing activities including user name, borrowed book, borrow date, and return date.
View and manage borrow records with ease.
Pagination:

Utilize Django's built-in pagination for all lists (authors, books, borrow records) to enhance user experience.
Export to Excel:

Export all data (authors, books, borrow records) to separate sheets in an Excel file for offline analysis or reporting purposes.
Error Handling and Notifications:

Implement robust error handling and user notifications for form submissions and actions to provide a smooth user experience.
Best Practices and Conventions:

Adhere to Django best practices and conventions throughout the application development.

Technologies Used
Django 3.x: Python web framework
Python 3.x: Programming language
PostgreSQL: Database management system (or your preferred database)
HTML, CSS, JavaScript: Frontend technologies
Bootstrap: Frontend framework for styling


Installation
Clone the repository:
git clone  https://github.com/mddaud49/Hacker_kernal_Task.git
cd project
pip install -r requirements.txt
py manage.py makemirgations
py manage.py migrate
py manage.py runserver

Created by: Daud Khan
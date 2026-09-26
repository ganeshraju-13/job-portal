\# Job Portal



A full-stack Job Portal web application built using Django and MySQL. The platform allows users to register, search for jobs, apply for jobs, upload resumes, and track application status. Administrators can manage job postings and applications through an admin dashboard.



\## Features



\### User Features



\- User registration and login

\- Browse available jobs

\- Search jobs by title, company, or location

\- View detailed job information

\- Apply for jobs

\- Upload resume in PDF, DOC, or DOCX format

\- Resume file size validation up to 5 MB

\- Prevent duplicate applications for the same job

\- View submitted applications

\- Track application status

\- Logout functionality



\### Admin Features



\- Admin dashboard

\- View total jobs

\- View total applications

\- View pending, shortlisted, and rejected applications

\- Add and manage job postings through Django Admin

\- Edit job details

\- Delete job postings

\- View applicant details

\- View and download applicant resumes

\- Update application status



\## Technologies Used



\- Python

\- Django

\- MySQL

\- HTML

\- CSS

\- JavaScript

\- Django Authentication

\- Git

\- GitHub



\## Project Structure



```text

jobportal/

│

├── config/

│   ├── settings.py

│   ├── urls.py

│   ├── asgi.py

│   └── wsgi.py

│

├── jobapp/

│   ├── migrations/

│   ├── templates/

│   ├── static/

│   ├── admin.py

│   ├── models.py

│   ├── urls.py

│   └── views.py

│

├── media/

├── manage.py

├── .gitignore

└── README.md

Database



The application uses MySQL for storing:



Job information

User accounts

Job applications

Application status

Uploaded resume references

Application Status



Applications can have the following statuses:



Pending

Shortlisted

Rejected

Resume Validation



The application supports:



PDF

DOC

DOCX



Maximum allowed file size:



5 MB

Security



Sensitive database credentials are stored using environment variables instead of being included directly in the source code.



The .env file is excluded from Git using .gitignore.



Installation

1\. Clone the repository

git clone https://github.com/ganeshraju-13/job-portal.git

2\. Navigate to the project

cd job-portal

3\. Create a virtual environment

python -m venv venv

4\. Activate the virtual environment



Windows:



venv\\Scripts\\activate

5\. Install dependencies

pip install django mysqlclient

6\. Configure environment variables



Create a .env file:



DB\_PASSWORD=your\_mysql\_password

7\. Configure MySQL



Create a MySQL database named:



jobportal\_db



Update the database username and other configuration values in:



config/settings.py

8\. Apply migrations

python manage.py migrate

9\. Create an admin user

python manage.py createsuperuser

10\. Start the development server

python manage.py runserver



Open:



http://127.0.0.1:8000/

Admin Panel



The Django administration panel is available at:



http://127.0.0.1:8000/admin/

Future Improvements

Job categories and filtering

Company profiles

Email notifications

Pagination

Advanced applicant filtering

Job recommendation system

REST API integration

Deployment to a cloud platform

Author



Ganesh Raju



GitHub:

https://github.com/ganeshraju-13


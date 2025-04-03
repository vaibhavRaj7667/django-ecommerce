# E-Commerce Website

## Overview
This is a e-commerce website built using Django. The platform allows users to browse products, add them to the cart, and proceed to checkout. It supports both logged-in users and anonymous users, ensuring a seamless shopping experience.

## Features
- User authentication (Signup, Login, Logout,)
- Product listing with categories and filters
- Product details page
- Cart functionality for both logged-in and anonymous users
- Order placement and management
- Search functionality
- Responsive design

## Technologies Used
- **Backend:** Django
- **Frontend:** HTML, CSS
- **Database:** SQLite 
- **Authentication:** Django's built-in authentication system

## Installation Guide
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Django
- Virtual Environment (optional but recommended)

### Steps to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/vaibhavRaj7667/django-ecommerce
   cd ecommerce-django
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```
7. Open the browser and visit:
   - User Site: `http://127.0.0.1:8000/`
   - Admin Panel: `http://127.0.0.1:8000/admin/`

## Deployment
1. Set up a production database (e.g., PostgreSQL).
2. Configure environment variables for secret keys and database settings.
3. Use Gunicorn and Nginx for deployment.
4. Set up a cloud storage solution for media files (e.g., AWS S3, DigitalOcean Spaces).

## Future Enhancements
- Implement AI-powered recommendations
- Add a review and rating system
- Enhance UI/UX with JavaScript
- Introduce multi-vendor support

## License
This project is licensed under the MIT License.

## Contact
For any queries or contributions, feel free to reach out:
- Email: zivaibhav1@gmail.com



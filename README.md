# E-Commerce Website

## Overview
This is a e-commerce website built using Django. The platform allows users to browse products, add them to the cart, and proceed to checkout. It supports both logged-in users and anonymous users, ensuring a seamless shopping experience.

## Screenshots
![Screenshot 2025-04-03 111016](https://github.com/user-attachments/assets/70339fd4-d81a-403b-90c6-98a6a22b1ca7)

![Screenshot 2025-04-03 111052](https://github.com/user-attachments/assets/718fafae-1520-47ea-ae02-07c39547c16e)

![Screenshot 2025-04-03 111109](https://github.com/user-attachments/assets/b5f2422e-cab1-42da-9aae-89b021e3e114)

![Screenshot 2025-04-03 111123](https://github.com/user-attachments/assets/92555000-6667-4178-8a11-3c8358887e16)

![Screenshot 2025-04-03 111138](https://github.com/user-attachments/assets/e241294c-ab51-4e51-99c6-6fbfbbd32e1b)

![Screenshot 2025-04-03 111202](https://github.com/user-attachments/assets/0b24c67f-011d-4212-b9d2-7ecbc88d4cc9)



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



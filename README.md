# ♻️ Replasify

A full-stack web application built with Django and Bootstrap, featuring a modern dashboard, service listings, and user engagement tools.


## Project Overview

Replasify is a Django-based web application designed to provide users with a comprehensive platform for service discovery, engagement, and account management. The application features a responsive design with a modern UI built using Bootstrap and custom CSS.

## Features

- **User Authentication**: Secure login and registration system
- **Service Listings**: Browse and explore available services
- **Contact & Inquiry System**: Submit inquiries and get in touch
- **Dashboard**: User dashboard for managing account and interactions
- **Responsive Design**: Mobile-friendly interface built with Bootstrap
- **Admin Panel**: Django admin interface for managing content
- **Rate Checking**: Service rate comparison tool

## Technologies Used

### Backend
- **Django 5.1.5** - Web framework
- **Python** - Programming language
- **SQLite** - Database

### Frontend
- **Bootstrap** - CSS framework
- **jQuery** - JavaScript library
- **Bootstrap Icons** - Icon library
- **AOS (Animate on Scroll)** - Scroll animation
- **GLightbox** - Lightbox gallery
- **Swiper** - Touch slider carousel

### Additional Libraries
Bootstrap Icons
Swiper.js
AOS (Animate On Scroll)
GLightbox


## Project Structure

```
Replasify/
├── application/                    # Django application
│   ├── models.py                  # Database models
│   ├── views.py                   # View logic
│   ├── urls.py                    # URL routing
│   ├── admin.py                   # Admin configuration
│   ├── migrations/                # Database migrations
│   └── tests.py                   # Unit tests
├── Project3/                      # Django project settings
│   ├── settings.py               # Project settings
│   ├── urls.py                   # Main URL configuration
│   ├── wsgi.py                   # WSGI configuration
│   └── asgi.py                   # ASGI configuration
├── templates/                     # HTML templates
│   ├── index.html                # Homepage
│   ├── about.html                # About page
│   ├── services.html             # Services page
│   ├── contact.html              # Contact page
│   ├── login.html                # Login page
│   ├── checkrate.html            # Rate checking page
│   ├── header.html               # Header component
│   ├── footer.html               # Footer component
│   └── dashboard/                # Dashboard templates
│       ├── index.html            # Dashboard home
│       ├── form-basic.html       # Basic form page
│       └── form-wizard.html      # Wizard form page
├── static/                        # Static files
│   ├── assets/                   # Custom assets
│   │   ├── css/                  # Custom stylesheets
│   │   ├── js/                   # Custom JavaScript
│   │   ├── img/                  # Images
│   │   └── vendor/               # Third-party libraries
│   ├── dashboard/                # Dashboard assets
│   └── _content/                 # Content files
├── manage.py                     # Django management script
└── requirements.txt              # Python dependencies
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone the repository** 
   ```bash
   git clone https://github.com/IshitaSajeev/Replasify.git 
   cd Replasify
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv myenv
   ```

3. **Activate the virtual environment**
   
   On Windows:
   ```bash
   myenv\Scripts\activate
   ```
   
   On macOS/Linux:
   ```bash
   source myenv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```


## Running the Application

### Development Server

1. Ensure your virtual environment is activated
2. Run migrations (if needed):
   ```bash
   python manage.py migrate
   ```

3. Create a superuser (admin account):
   ```bash
   python manage.py createsuperuser
   ```

4. Start the development server:
   ```bash
   python manage.py runserver
   ```

5. Access the application:
   - Main site: http://localhost:8000/
   - Admin panel: http://localhost:8000/admin/

### Collecting Static Files (Production)

```bash
python manage.py collectstatic
```

## Database

### Models

The application includes the following models:

- **enquiry_table**: Stores user inquiries and contact messages
  - `name` (CharField)
  - `email` (EmailField)
  - `phone` (CharField)
  - `message` (TextField)

### Running Migrations

Create new migrations:
```bash
python manage.py makemigrations
```

Apply migrations:
```bash
python manage.py migrate
```

View migration status:
```bash
python manage.py showmigrations
```

## Static Files

Static files are organized in the `static/` directory:

- **CSS**: Bootstrap and custom stylesheets
- **JavaScript**: jQuery, Swiper, and custom scripts
- **Images**: Blog images, team photos, and backgrounds
- **Vendor Libraries**: Third-party components


### Future Enhancements

- AI-based waste classification
- Reward points system
- Real-time recycling tracking
- GIS integration for nearby recycling centers
- Email notification system

### License

This project is developed for educational and learning purposes.

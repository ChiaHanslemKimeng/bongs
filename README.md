# BONGS - Luxury Glassware Platform

An ultra-modern, futuristic premium e-commerce platform built with Django, PostgreSQL, and Tailwind CSS.

## Features
- Glassmorphism UI & Dark Theme
- Real-time HTMX Cart
- Stripe Integration
- Custom User Dashboard
- Celery + Redis Background Tasks
- Django Allauth

## Local Installation

1. Create a virtual environment and install dependencies:
```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

2. Setup `.env` file based on `.env.example`.

3. Run migrations:
```bash
python manage.py migrate
```

4. Create superuser:
```bash
python manage.py createsuperuser
```

5. Run server:
```bash
python manage.py runserver
```

## Deployment to Namecheap VPS (Ubuntu 22.04)

1. Connect to your VPS via SSH.
2. Install Docker and Docker Compose:
```bash
sudo apt update
sudo apt install docker.io docker-compose
```

3. Clone your repository onto the VPS.
```bash
git clone <your-repo-url> /opt/bongs
cd /opt/bongs
```

4. Populate your `.env` file with production keys (Stripe, Postgres, etc.)

5. Run the Docker containers:
```bash
sudo docker-compose up -d --build
```

6. The Nginx container will serve the application on port 80. To add SSL/HTTPS, install Certbot:
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

7. Setup static files (run inside the web container):
```bash
sudo docker-compose exec web python manage.py collectstatic --no-input
sudo docker-compose exec web python manage.py migrate
```

Your premium platform is now live!

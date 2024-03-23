# CYCLE HUB 🚀: Cycle E-commerce! 🌐

Welcome to CYCLE HUB,  Your ultimate destination for all cycling needs, from bikes and accessories to expert advice and community connections.

## User Experience:

- *Secure OTP Login:* Elevate user security with seamless one-time password verification.
- *Tyre Size Variants:* Explore a diverse cycle collection with different size options.
- *Smart Navigation:* Effortlessly find your perfect pair using intuitive search and advanced filtering options.
- *Inquiry Feature:* Engage with us! Have questions or need assistance? Utilize our easy inquiry system for quick responses.
- *Personalized Profiles:* Elevate your shopping journey with profiles tailored to your preferences.
- *Effortless Cart & Checkout:* Smoothly manage your shopping cart and experience a hassle-free checkout process.
- *Flexible Payment Options:* Choose from various payment methods, including Razorpay, wallet, and Cash on Delivery.
- *Automated Invoicing:* Enjoy transparency in transactions with automatic invoice generation.
- *Exclusive Coupons:* Unlock discounts and special offers with promotional coupons.
- *Password Management:* Forgot your password or want to make a change? User-friendly options for seamless account control.

## Admin Empowerment:

- *Intuitive Dashboard:* Comprehensive insights at a glance, empowering quick and informed decision-making.
- *Sales Analytics:* Dive deep into sales performance with detailed analytics and customizable date filters.
- *Downloadable Sales Reports:* Effortlessly download detailed sales reports in Excel & pdf format for in-depth analysis.
- *Streamlined Order Management:* Efficiently track and manage orders for a streamlined fulfillment process.
- *Product and User Control:* Enjoy effortless control over products and user accounts for optimal administration.
- *Coupon Mastery:* Fine-tune promotions with comprehensive control over coupon generation and management.
- *Dynamic Banner Changes:* Keep your storefront fresh with the ability to dynamically change banners for strategic promotions.


## Cutting-Edge Tech Stack:

- *Django Backend:* Powering our platform with the reliability and scalability of the Django framework.
- *Sleek Frontend Design:* Crafted using HTML, CSS, and Bootstrap for a visually stunning and responsive user interface.
- *Dynamic User Experience:* Implementing Ajax & JQuery for a dynamic and responsive user journey.
- *Reliable Database Management:* Leveraging the efficiency of PostgreSQL for seamless data management.
- *Scalable Deployment with Docker:* Ensuring scalability and ease of deployment using Docker.
- *Secure Hosting on AWS EC2:* Hosted securely and reliably on AWS EC2 for a worry-free experience.
- *Real-Time Chat with Django Channels and ASGI Daphne:* Offering a real-time, interactive experience with our users.



# Get Started:

## Procedure to Run CYCLE HUB Locally:

### 1. Clone the Repository:

```bash
git clone https://github.com/Sinanalungal/cyclehub_ecommerce_web.git
cd cyclehub

python -m venv venv
venv/Scipts/activate

pip install -r requirements.txt

```
Configure Database:
Ensure you have PostgreSQL installed.

Create a new database for CYCLE HUB.

Update the database configurations in cyclehub/settings.py:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
5. Create .env file:
Create a file named .env in the project root and add the following:
```
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
DB_NAME=
DB_USER=
DB_PASSWORD=
DEFAULT_FROM_EMAIL=
```
6. Run the Project:
    ```
      python manage.py runserver
    ```
7. Run Using Docker Compose :

    instead of host in setting.py postgress database change that into the 'postgres_db'
   then in project directory
   ```
     docker compose up -d
   ```

Happy Coding !!

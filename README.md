# Vendly

Vendly is a modern e-commerce platform built with Django and styled using Tailwind CSS. Designed for flexibility and performance, Vendly makes it easy to create a streamlined online store that delivers a fast and seamless shopping experience. Whether you're launching a small boutique or expanding an existing product catalog, Vendly provides the tools to manage your store efficiently and grow your business online.

## Installation Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/vendly.git
   cd vendly
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (for admin access)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

Vendly will be accessible at `http://localhost:8000`.

## Usage

Once the server is running:

* Visit the homepage to browse available products
* Register or log in to your account to manage your cart and place orders
* Access the admin dashboard at `/admin/` to add products, view orders, and manage users

Vendly is designed to be easily customizable, so you can adjust product categories, styles, and business rules to match your brand's needs.

## Contact

For questions, suggestions, or support, feel free to reach out:

**Email:** [KeneanSufa@gmail.com](mailto:keneansufa@gmail.com)
**GitHub:** [github.com/KeneanDita/vendly](https://github.com/keneandita/vendly)

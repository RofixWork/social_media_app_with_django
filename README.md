# Social Media Project

## Overview
This project is a fully functional social media platform built with Django. It includes features for user authentication, profile management, and post interactions. The admin panel is customized with Jazzmin for an enhanced user experience, and Django Extensions are used to add additional functionalities for development and debugging.

---

## Features

### Authentication
- **User Registration:** Allow users to sign up for an account.
- **Login:** Secure authentication for returning users.
- **Logout:** End user sessions securely.
- **Reset Password:** Enable users to recover access to their accounts if they forget their password.
- **Change Password:** Allow logged-in users to update their passwords.

### User Profile
- **View Profile:** Display user-specific information.
- **Edit Profile:** Update personal details, such as name, email, or profile picture.

### Posts
- **Create New Post:** Share content with other users.
- **Update Post:** Modify an existing post.
- **Delete Post:** Remove posts no longer needed.
- **Like Post:** Allow users to engage with posts they enjoy.

### Admin Panel
- **Jazzmin Integration:** Customize the Django admin interface for a modern look and improved usability.

### Development Features
- **Django Extensions:** Enhance development with features like shell-plus, model visualization, and other utilities.

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/social-media-project.git
   cd social-media-project
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server:**
   ```bash
   python manage.py runserver_plus
   ```

---

## Usage

1. **Access the application:**
   - Visit `http://127.0.0.1:8000/` in your browser.

2. **Admin Panel:**
   - Access the admin panel at `http://127.0.0.1:8000/admin/` using the superuser credentials.
   
3. **Customize Admin Panel:**
   - Modify the admin interface using Jazzmin settings in `settings.py`.

4. **Debugging Tools:**
   - Use Django Extensions commands like `shell_plus` for an enhanced interactive shell.

---

## Contributing
If you’d like to contribute to this project, please fork the repository and create a pull request. For major changes, open an issue first to discuss what you’d like to change.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.




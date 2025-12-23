
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vishubh_bridge.settings')
django.setup()

from django.contrib.auth import get_user_model

def create_admin():
    User = get_user_model()
    username = 'admin'
    email = 'admin@example.com'
    password = 'admin'  # Simple password for local dev

    if not User.objects.filter(username=username).exists():
        print(f"Creating superuser '{username}'...")
        try:
            User.objects.create_superuser(username, email, password)
            print(f"Superuser '{username}' created successfully.")
            print(f"Email: {email}")
            print(f"Password: {password}")
        except Exception as e:
            print(f"Error creating superuser: {e}")
    else:
        print(f"Superuser '{username}' already exists.")

if __name__ == '__main__':
    create_admin()

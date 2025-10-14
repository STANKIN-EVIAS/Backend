import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','app.settings.dev')
import django
django.setup()

from users.models import User
from django.contrib.auth import authenticate
from users.serializers import LoginSerializer

email='test@example.com'
pwd='password123'

u=User.objects.filter(email=email).first()
if not u:
    User.objects.create_user(username=email, email=email, password=pwd)
    print('created user')
else:
    print('user exists')

# try authenticate with username=email
user = authenticate(username=email, password=pwd)
print('authenticate(username=) ->', type(user), getattr(user, 'email', None))

# try serializer validate
serializer = LoginSerializer(data={'email': email, 'password': pwd}, context={'request': None})
valid = serializer.is_valid()
print('serializer valid ->', valid)
print('serializer errors ->', serializer.errors)
print('serializer validated_data ->', serializer.validated_data if valid else None)

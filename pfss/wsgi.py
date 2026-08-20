import os
import sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pfss.settings")

# Securely initialize the Django App Registry first
application = get_wsgi_application()

# Now that the registry is ready, safely patch the missing functions
try:
    import django.contrib.sites.shortcuts
    import django.contrib.sites.models
    
    # Append the missing shortcut function to the real models file
    django.contrib.sites.models.get_current_site = django.contrib.sites.shortcuts.get_current_site
    sys.modules['django.contrib.sites.models'].get_current_site = django.contrib.sites.shortcuts.get_current_site
except Exception:
    pass

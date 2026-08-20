import sys

# Production Compatibility Bridge
try:
    from django.contrib.auth.models import AnonymousUser, AbstractBaseUser
    from pfss.settings import CallableBool
    
    # 1. Safely attach .is_authenticated compatibility properties
    AbstractBaseUser.is_authenticated = property(lambda self: CallableBool(True))
    AnonymousUser.is_authenticated = property(lambda self: CallableBool(False))
    
    # 2. Safely bridge legacy sites.models shortcuts
    import django.contrib.sites.shortcuts as shortcuts
    import django.contrib.sites.models as sites_models
    sites_models.get_current_site = shortcuts.get_current_site
    sys.modules['django.contrib.sites.models'].get_current_site = shortcuts.get_current_site
except Exception:
    pass

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from pfss import views as pfss_views
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include("account.urls")),
    url(r'^slist/handle/$', pfss_views.handleList),
    url(r'^slist/$', pfss_views.creatureList),
    url(r'^slist/(?P<group_ID>\d+)/$', pfss_views.creatureList),
    url(r'^slist/code/(?P<code>\w+)/$', pfss_views.creatureListByCode),
    url(r'^creature/(\d+)/$', pfss_views.creatureView),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


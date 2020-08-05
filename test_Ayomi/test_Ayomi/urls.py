from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'test_Ayomi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^accueil/', include('accueil.urls')),
    url(r'info/', include('info.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

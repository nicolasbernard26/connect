"""
high level support for doing this and that.
"""

from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
    url(r'^accounts/', include('accounts.urls')),
]

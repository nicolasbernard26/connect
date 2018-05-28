from django.conf.urls import url
from account_API.views.connection_view import ConnectionView
from account_API.views.involve_view import InvolveView
from account_API.views.notification_view import NotificationView
from account_API.views.profile_view import ProfileView
from account_API.views.login_view import LoginView


urlpatterns = [
    url(r'^profile/(\d+)$', ProfileView.as_view(), name="profile"),
    url(r'^login$', LoginView.as_view(), name="login"),
    url(r'^connection$', ConnectionView.as_view(), name="connection"),
    url(r'^events$', InvolveView.as_view(), name="events"),
    url(r'^notification', NotificationView.as_view(), name="events")
]
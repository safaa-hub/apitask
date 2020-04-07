from django.urls import path

from . import views
from .views import RegisterView, LoginView, GetUserView

urlpatterns = [

    (r'^register/$', RegisterView.as_view())
    (r'^login/$', LoginView.as_view())
    (r'^get-user/$', GetUserView.as_view())

]

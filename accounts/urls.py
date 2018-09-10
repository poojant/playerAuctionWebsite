from django.urls import path
from django.conf.urls import url
from . import views
from django.urls import reverse_lazy
#from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    #path('', views.home),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
   	path('logout/', LogoutView.as_view(next_page = reverse_lazy('login')), name="logout"),
    path('auction/', views.startAuction),
    path('register/',views.register, name="register"),
    path('teamdisplay/',views.displayTeam),
    path('imagegallery/',views.imageGallery)
    #path('logout/', views.logoutView)
]
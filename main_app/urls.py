from django.urls import path
from django.shortcuts import redirect
from .views import Home, SignUp

urlpatterns = [
    # path('', Home.as_view(), name='home'),
    path('', lambda req: redirect('accounts/signup/'), name='home'),
    path('accounts/signup/', SignUp.as_view(), name='signup'),
]

# Regex: r'^.../$'
# Warning: Your URL pattern '^signup/$' has a route that contains '(?P<', begins with a '^', or ends with a '$'. This was likely an oversight when migrating to django.urls.path().
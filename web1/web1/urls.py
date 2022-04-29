"""web1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views
from PMM import viewsPMM
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include



urlpatterns = [
    # URLs for PMM begins from Here
    path('admin/', admin.site.urls),
    path('', views.Login, name='Login'),
    path('Homepage', viewsPMM.homepage),
    path('HomepagePMM', viewsPMM.homepagePMM),
    path('Product', viewsPMM.products),
    path('Order', viewsPMM.Orders),
    path('Commission Sheet', viewsPMM.Commision),
    path('Reservation', viewsPMM.Reservation),
    path('Rules and Regulation', viewsPMM.Rules),
    path('User Profile', viewsPMM.Profile),
    path('Order Form', viewsPMM.Orderform),
    path('delete Reservation',viewsPMM.deleresservation),
    path('Order Update',viewsPMM.orderupdate),


    # views for PM begins from Here
    path('HomepagePM', viewsPMM.homepagePM),
    path('ProductPM', viewsPMM.productsPM),
    path('OrderPM', viewsPMM.OrdersPM),
    path('Order Update PM',viewsPMM.orderupdatepm),
    path('Commission Sheet PM', viewsPMM.CommisionPM),
    path('ReservationPM', viewsPMM.ReservationPM),
    path('User Profile PM', viewsPMM.ProfilePM),
    path('productadd', viewsPMM.productadd),



    # views for Admins begins from Here
    path('homepageadmin', viewsPMM.homepageAdmin),
    path('RemovePM', viewsPMM.removePM),
    path('RemovePMM', viewsPMM.removePMM),
    path('delete Orders', viewsPMM.deleteorder),
    

    path('__debug__/', include('debug_toolbar.urls')),



]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)


from django.urls import path
from . import views

urlpatterns = [
    path('', views.sample, name='home'),                 # Homepage
    path('creation/', views.creation, name='creation'),  # My creation page
    path('template/', views.templateview, name='template'),  # Template view (index)
    path('reviews/', views.review_page, name='reviews'), # Reviews page
    path('thank-you/', views.thank_you, name='thank_you'), # Thank you page
    path('contribute/', views.contribute_view, name='contribute'), # Contribution page
]
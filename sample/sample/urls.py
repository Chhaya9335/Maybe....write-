"""
URL configuration for sample project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.views.generic import TemplateView
import os
from django.conf import settings
from django.conf.urls.static import static
from sampleapp import views

# from .views import contribute_view

BASE_DIR = settings.BASE_DIR

urlpatterns = [

    path('admin/', admin.site.urls),
     path('contribution/', views.contribute_view, name='contribution'),
    path('reviews/', views.review_page, name='reviews'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('index/', TemplateView.as_view(template_name='index.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='aboutt.html'), name='about'),
    path('my-creation/', TemplateView.as_view(template_name='my_creation.html'), name='my_creation'),
    path('true-writers/', TemplateView.as_view(template_name='true_writer.html'), name='true_writers'),
    # path('contribution/', TemplateView.as_view(template_name='contribution.html'), name='contribution'),
    path('aladin/', TemplateView.as_view(template_name='aladin.html'), name='aladin'),
    path('beauty/', TemplateView.as_view(template_name='beauty.html'), name='beauty'),
    path('agni/', TemplateView.as_view(template_name='agni.html'), name='agni'),
    path('bail/', TemplateView.as_view(template_name='bail.html'), name='bail'),
    path('chota/', TemplateView.as_view(template_name='chota.html'), name='chota'),
    path('cindrella/', TemplateView.as_view(template_name='cindrella.html'), name='cindrella'),
    path('cloud/', TemplateView.as_view(template_name='cloud.html'), name='cloud'),
    path('essay2/', TemplateView.as_view(template_name='essay2.html'), name='essay2'),
    path('essay/', TemplateView.as_view(template_name='essay.html'), name='essay'),
    path('fiction/', TemplateView.as_view(template_name='fiction.html'), name='fiction'),
    path('fiction1/', TemplateView.as_view(template_name='fiction1.html'), name='fiction1'),
    path('happy/', TemplateView.as_view(template_name='happy.html'), name='happy'),
    path('imagination/', TemplateView.as_view(template_name='imagination.html'), name='imagination'),
    path('kahani-5/', TemplateView.as_view(template_name='kahani_5.html'), name='kahani_5'),
    path('kahani/', TemplateView.as_view(template_name='kahani.html'), name='kahani'),
    path('kahani2/', TemplateView.as_view(template_name='kahani2.html'), name='kahani2'),
    path('kahani3/', TemplateView.as_view(template_name='kahani3.html'), name='kahani3'),
    path('kahani4/', TemplateView.as_view(template_name='kahani4.html'), name='kahani4'),
    path('katha/', TemplateView.as_view(template_name='katha.html'), name='katha'),
    path('kavita/', TemplateView.as_view(template_name='kavita.html'), name='kavita'),
    path('kavitas/', TemplateView.as_view(template_name='kavitas.html'), name='kavitas'),
    path('last/', TemplateView.as_view(template_name='last.html'), name='last'),
    path('little/', TemplateView.as_view(template_name='little.html'), name='little'),
    path('lost/', TemplateView.as_view(template_name='lost.html'), name='lost'),
    path('necklace/', TemplateView.as_view(template_name='necklace.html'), name='necklace'),
    path('poem/', TemplateView.as_view(template_name='poem.html'), name='poem'),
    path('poosh/', TemplateView.as_view(template_name='poosh.html'), name='poosh'),
    path('road/', TemplateView.as_view(template_name='road.html'), name='road'),
    path('shayari/', TemplateView.as_view(template_name='shayari.html'), name='shayari'),
    path('still/', TemplateView.as_view(template_name='still.html'), name='still'),
    path('story/', TemplateView.as_view(template_name='story.html'), name='story'),
    path('thoughts/', TemplateView.as_view(template_name='thoughts.html'), name='thoughts'),
    

]
# Serve static files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(BASE_DIR, 'sampleapp', 'static'))


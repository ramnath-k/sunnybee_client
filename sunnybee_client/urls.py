"""sunnybee_client URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

import tag_metrics.views as tag_metrics_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^store_stock/$', tag_metrics_views.store_stock),
    url(r'^tag_location/$', tag_metrics_views.tag_location),
    url(r'^tag_flow_today/$', tag_metrics_views.tag_flow_today),
    url(r'^tag_flow_week/$', tag_metrics_views.tag_flow_week),
    url(r'^update_tag_location/$', tag_metrics_views.update_tag_location),
]

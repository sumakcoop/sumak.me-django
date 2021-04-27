#
# This file is part of Sumak.me-django
# Copyright (C) 2021 Asociación SUMAK <info (at) sumakcoop (dot) org
#
# Sumak.me-django is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Sumak.me-django is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Sumak.me-django.  If not, see <http://www.gnu.org/licenses/>.
#

# sumakMe URL Configuration
#
# The `urlpatterns` list routes URLs to views. For more information please see:
#    https://docs.djangoproject.com/en/2.2/topics/http/urls/
# Examples:
# Function views
#    1. Add an import:  from my_app import views
#    2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#    1. Add an import:  from other_app.views import Home
#    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#    1. Import the include() function: from django.urls import include, path
#    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

from django.apps import apps
from django.urls import path, include

from web import views as web_index


urlpatterns = [
    path('', include(apps.get_app_config('oscar').urls[0])),
    path('index.html', web_index.index, name="home"),
]

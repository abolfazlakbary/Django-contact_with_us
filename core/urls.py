from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('contact_us.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/rest-auth/registeration/', include('dj_rest_auth.registration.urls')),
    path('schema/', get_schema_view(title="Blog API")), #Machine readable information about our API
    path('docs/', include_docs_urls("Blog API")), #Human readable information about our API using Core API
    path('swagger-docs/', get_swagger_view()), #Human readable information about our API using Swagger
]


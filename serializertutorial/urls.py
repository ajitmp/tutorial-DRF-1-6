from django.urls import path, include

urlpatterns = [
    path('', include('snippets.urls')),
]
# to include the login and logout views for the browsable API.
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
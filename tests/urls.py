from django.urls import path, include

urlpatterns = [
    path('sde/', include('armada_sde_rest.urls')),
]

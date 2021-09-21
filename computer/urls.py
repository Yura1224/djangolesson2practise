from django.urls import path
from .views import ComputerListCreateView, ComputerRetrieveUpdateDeleteView

urlpatterns = [
    path('', ComputerListCreateView.as_view(), name='computer_list_create'),
    path('/<int:pk>', ComputerRetrieveUpdateDeleteView.as_view(), name='car_retrieve_update_delete')
]

# http:localhost:8000/computers

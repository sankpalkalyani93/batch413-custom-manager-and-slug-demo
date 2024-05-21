from django.urls import path
from .views import active_state_person_list, person_detail

urlpatterns = [
    path('active_persons/', active_state_person_list, name='active_persons'),
    path('person/<slug:slug>/', person_detail, name='person_detail'),
]

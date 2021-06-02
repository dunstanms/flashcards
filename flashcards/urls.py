# flashcards app urls conf
from django.urls import path,include
from django.conf.urls import url
from . import views # . means we are in the same directory (views is in same directory as urls)

urlpatterns = [ 
    path('', views.flashcards, name = 'flashcards'), 
    path('create/', views.create_card_set, name = 'create_card_set'), 
    path('create_card/(?P<card_set_id>[\d]+)', views.create_card, name = 'create_card'), 
    path('delete/(?P<card_set_id>[\d]+)', views.delete_card_set, name = 'delete_card_set'), 
    path('delete_card/(?P<card_id>[\d]+)', views.delete_card, name = 'delete_card'), 
    path('edit/(?P<card_set_id>[\d]+)', views.edit_card_set, name = 'edit_card_set'),
    path('edit_card/(?P<card_id>[\d]+)', views.edit_card, name = 'edit_card'), 
    path('view/(?P<card_set_id>[\d]+)', views.view_card_set, name = 'view_card_set'), 
    path('dictionary/', views.dictionary, name = 'dictionary'), 
]
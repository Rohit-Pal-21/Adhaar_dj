# urls.py
from django.urls import path
from .views import login_view,logout_view, index_view, translate_function, adhaar_list_view, delete_adhaar_card, adhaar_card_detail

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    
    path('', index_view, name='adhaar_card_detail'),
    path('translate_function/', translate_function, name='translate_function'),
    path("adhaar_card_list/",adhaar_list_view,name='adhaar_card_list'),
    
    path('delete_adhaar_card/<int:id>/', delete_adhaar_card, name='delete_adhaar_card'),
    path('adhaar_card_detail/<int:id>/', adhaar_card_detail, name='adhaar_card_detail'),

]

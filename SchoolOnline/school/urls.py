from django.urls import path
from . import views

urlpatterns = [
    path('speciality',views.SpecialityList.as_view()),
    path('speciality/<int:pk>',views.SpecialityAct.as_view()),
    
    path('level',views.LevelList.as_view()),
    path('level/<int:pk>',views.LevelAct.as_view()),
    
    path('classe',views.ClasseList.as_view()),
    path('classe/<int:pk>',views.ClasseAct.as_view()),
    
    path('matter',views.MatterList.as_view()),
    path('matter/<int:pk>',views.MatterAct.as_view()),
]

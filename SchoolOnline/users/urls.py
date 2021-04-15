{
    "matricule": "17l2023",
    "email": "berlin@gmail.com",
    "username": "berlin",
    "first_name": "berlino",
    "born_at": "2002-06-05",
    "gender": "F",
    "classes":[1,2,3],
    "role": 2,
    "dep":1
}
from django.urls import path
from . import views

urlpatterns = [
    path('role',views.RolesList.as_view()),
    path('roles/<int:pk>',views.RolesAct.as_view()),
    
    path('departement',views.DepartementList.as_view()),
    path('departement/<int:pk>',views.DepartementAct.as_view()),
    
    # path('',views.user_list_create),
    # path('<int:pk>',views.UserAct.as_view()),
    path('',views.UserView.as_view({
            'get': 'list',
            'post': 'create',
        })),
    
    path('<int:pk>', views.UserView.as_view({
            'get': 'retrieve',
            'put': 'update',
            # 'delete': 'destroy'
        }))
]

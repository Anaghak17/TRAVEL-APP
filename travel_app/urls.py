from django.urls import path
from .import views

urlpatterns = [
      path('adddestinaton/',views.adddestinaton,name="addDestination"),
      path('viewdestination/',views.viewdestination,name="viewDestination"),
      path('getdata/',views.getdata,name="getdata"),
      path('edit/<int:id>/',views.edit,name="edit"),
      path('update/<int:id>/',views.update,name="update"),
      path('delete/<int:id>/',views.delete,name="delete"),
      path('login/',views.login,name="login"),
      path('registration/',views.registration,name="registration"),
      path('table/',views.table,name="table"),
      path('getdata2/',views.getdata2,name="getdata2"),
      path('index/',views.index,name="index"),
      path('add_destination/',views.add_destination,name="add_destination"),
      path('view_destination/',views.view_destination,name="view_destination"),
      


]



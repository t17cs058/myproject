from django.urls import path # @UnresolvedImport

from .views import ItemList, ItemDeleteView # @UnresolvedImport


appname = "shoppinglist"

urlpatterns = [

    path("list/", ItemList.as_view(), name="list"),  # @UndefinedVariable
    path("delete/", ItemDeleteView.as_view(), name="delete"),  # @UndefinedVariable

    ]

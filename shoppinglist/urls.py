from django.urls import path # @UnresolvedImport
from .views import ItemList ,ItemAddView, ItemShowView,ItemDeleteView # @UnresolvedImport

appname = "shoppinglist"

urlpatterns = [
    path("list/", ItemList.as_view(), name="list"),  # @UndefinedVariable
    path('add/', ItemAddView.as_view(),name='add'),  # @UndefinedVariable
    path('show/', ItemShowView.as_view(),name='show'), # @UndefinedVariable
    path("delete/", ItemDeleteView.as_view(), name="delete"),  # @UndefinedVariable
    ]

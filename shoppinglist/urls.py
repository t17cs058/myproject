from django.urls import path # @UnresolvedImport
from .views import ItemList ,ItemAddView,ItemEditView, ItemShowView,ItemDeleteView # @UnresolvedImport

appname = "shoppinglist"

urlpatterns = [

    path("list/", ItemList.as_view(), name="list"),  # @UndefinedVariable
    path('add', ItemAddView.as_view(),name='add'),  # @UndefinedVariable
    path('edit', ItemEditView.as_view(),name='edit'),# @UndefinedVariable
    path('show', ItemShowView.as_view(),name='show'), # @UndefinedVariable
    path("delete", ItemDeleteView.as_view(), name="delete"),  # @UndefinedVariable

    ]

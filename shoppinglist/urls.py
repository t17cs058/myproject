from django.urls import path # @UnresolvedImport
from .views import ItemList ,ItemAddView,ItemEditView, ItemShowView,ItemDeleteView # @UnresolvedImport

appname = "shoppinglist"

urlpatterns = [

    path("list/", ItemList.as_view(), name="list"),  # @UndefinedVariable
    path('add', ItemAddView.as_view(),name='add'),  # @UndefinedVariable
    path('edit', ItemEditView.as_view(),name='edit'),# @UndefinedVariable
    path('show', ItemShowView.as_view(),name='show'), # @UndefinedVariable
    path("delete", ItemDeleteView.as_view(), name="delete"),  # @UndefinedVariable
    path('delete/<int:item_id>', ItemDeleteView.as_view(), name='delete'),
    path('edit/<int:item_id>', ItemEditView.as_view(), name='edit'),
    # path('edit/<int:pk>', ItemEditView.as_view(), name='edit'),
    # r'^(?P<pk>[0-9]+)/$

    ]

from django.urls import path # @UnresolvedImport
from .views import ItemList ,ItemAddView,ItemEditView, ItemShowView,ItemDeleteView,ItemBuyView# @UnresolvedImport

appname = "shoppinglist"

urlpatterns = [

    path("list/", ItemList.as_view(), name="list"),  # @UndefinedVariable
    path('add', ItemAddView.as_view(),name='add'),  # @UndefinedVariable
    path('edit', ItemEditView.as_view(),name='edit'),# @UndefinedVariable
    path('show', ItemShowView.as_view(),name='show'), # @UndefinedVariable
    path("delete", ItemDeleteView.as_view(), name="delete"),  # @UndefinedVariable
    path("buy", ItemBuyView.as_view(), name="buy"),  # @UndefinedVariable
    path('delete/<int:item_id>', ItemDeleteView.as_view(), name='delete'),
    path('edit/<int:item_id>', ItemEditView.as_view(), name='edit'),
    path('list/<int:item_id>', ItemList.as_view(), name='list'),
    path("buy/<int:item_id>", ItemBuyView.as_view(), name="buy"),

    ]

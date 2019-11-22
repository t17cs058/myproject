from django.urls import path # @UnresolvedImport
from .views import ItemList,ItemEditView

appname = "shoppinglist"

urlpatterns = [
     path("list/", ItemList.as_view(), name="list"),
     path('edit', ItemEditView.as_view(),name='edit'),
     # @UndefinedVariable
    ]

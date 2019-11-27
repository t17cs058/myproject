from django.views.generic import ListView # @UnresolvedImport
from .models import Item
from django.http import HttpResponseRedirect # @UnresolvedImport
from django.urls import reverse # @UnresolvedImport
from django.shortcuts import get_object_or_404 # @UnresolvedImport
from .forms import ItemBuy, ItemIdForm , ItemForm# @UnresolvedImport
from django.views.generic.base import TemplateView # @UnresolvedImport
from lib2to3.fixes.fix_input import context
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

class ItemList(ListView):
    model = Item

    def post(self, request, *args, **kwargs):
        item_id = self.request.POST.get('item_id')
        item = get_object_or_404(Item, pk=item_id)
        item_status = self.request.POST.get('item_status')
        item.buy = item_status
        item.save()
        return HttpResponseRedirect(reverse('list'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ItemBuy()
        return context

class ItemAddView(CreateView):
    model = Item
    fields = ('name', 'item_url', 'count', 'buy_date', 'shop')
    template_name = 'shoppinglist/item_add.html'
    success_url = 'list/'
    
class ItemShowView(TemplateView):
    model = Item
    template_name = 'shoppinglist/item_show.html'

    def post(self, request, *args, **kwargs):
        item_id = self.request.POST.get('item_id')
        item = Item.objects.get(pk=item_id)
        context = super().get_context_data(**kwargs)
        context['form_id'] = ItemIdForm()
        context['item'] = item
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_id'] = ItemIdForm()
        return context


class ItemEditView(TemplateView):
    model = Item
    template_name = 'shoppinglist/item_edit.html'
    success_url = 'list/'

    def post(self, request, *args, **kwargs):
        item_id = self.request.POST.get('item_id')
        name = self.request.POST.get('name')
        count = self.request.POST.get('count')
        buy_date = self.request.POST.get('buy_date')

        item = get_object_or_404(Item, pk=item_id)
        item.name = name
        item.count = count
        item.buy_date = buy_date
        item.save()
        return HttpResponseRedirect(reverse('list'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_id'] = ItemIdForm()
        context['form'] = ItemForm()
        return context

class ItemDeleteView(TemplateView):
    model = Item
    template_name = "shoppinglist/item_delete.html"

    def post(self, request, *args, **kwargs):
        item_id = self.request.POST.get("item_id")
        item = get_object_or_404(Item, pk=item_id)
        item.delete()
        return HttpResponseRedirect(reverse("list"))

    def get_context_data(self, **kwarg):
        context = super().get_context_data(**kwarg)
        context["form"] = ItemIdForm()
        return context


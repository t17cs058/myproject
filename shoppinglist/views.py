#from django.shortcuts import render
from django.views.generic import ListView # @UnresolvedImport
from .models import Item
from django.http import HttpResponseRedirect # @UnresolvedImport
from django.urls import reverse # @UnresolvedImport
from django.shortcuts import get_object_or_404 # @UnresolvedImport
from .forms import ItemBuy
from lib2to3.fixes.fix_input import context

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
    
# class ItemShowView(TemplateView):
#     model = Item
#     template_name = 'shoppinglist/item_show.html'

#     def post(self, request, *args, **kwargs):
#         item_id = self.request.POST.get('item_id')
#         item = Item.objects.get(pk=item_id)
#         context = super().get_context_data(**kwargs)
#         context['form_id'] = ItemIdForm()
#         context['item'] = item
#         return self.render_to_response(context)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form_id'] = ItemIdForm()
#         return context
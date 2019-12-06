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
from django.views.generic.edit import UpdateView
from django.db.models import Q # @UnresolvedImpor


class ItemList(ListView):
    model = Item
    names = [ "きてれつ", "とんがり" ]

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

    def get_queryset(self):
        q = Item.objects.all()
        if (self.request.GET.get("name") != ""):
            q = q.filter(Q(name=self.request.GET.get("name")))
        if (self.request.GET.get("count") != ""):
            q = q.filter(Q(count=self.request.GET.get("count")))
        if (self.request.GET.get("buy_date") != ""):
            q = q.filter(Q(buy_date=self.request.GET.get("buy_date")))
        if (self.request.GET.get("buy") == "1"):
            q = q.filter(Q(buy=1))
        elif (self.request.GET.get("buy") == "2"):
            q = q.filter(Q(buy=0))
        print(self.request.GET.get("order_by"))
        if (self.request.GET.get("order_kind") == "0"):
            if(self.request.GET.get("order_by")=="0"):
                q = q.order_by("name")
            elif(self.request.GET.get("order_by")=="1"):
                q = q.order_by("name").reverse()

        elif (self.request.GET.get("order_kind") == "1"):
            if(self.request.GET.get("order_by")=="0"):
                q = q.order_by("count")
            elif(self.request.GET.get("order_by")=="1"):
                q = q.order_by("count").reverse()

        elif (self.request.GET.get("order_kind") == "2"):
            if(self.request.GET.get("order_by")=="0"):
                q = q.order_by("buy_date")
            elif(self.request.GET.get("order_by")=="1"):
                q = q.order_by("buy_date").reverse()

        return q


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



class ItemEditView(TemplateView,):
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

    def get_context_data(self, **kwarg):
        context = super().get_context_data(**kwarg)
        if( kwarg.get("item_id") == None ):
            context["form_id"] = ItemIdForm()
            context['form'] = ItemForm()
            return context
        else:  
            context["form_id"] = ItemIdForm(initial={'item_id':kwarg.get("item_id")})
            item = Item.objects.get(pk=kwarg.get("item_id"))
            context['form'] = ItemForm(initial={'name':item.name,"item_url":item.item_url,'count':item.count,'buy_date':item.buy_date})

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
        if( kwarg.get("item_id") == None ):
            context["form"] = ItemIdForm()
        else:  
            context["form"] = ItemIdForm(initial={'item_id':kwarg.get("item_id")})
            item = get_object_or_404(Item, pk=kwarg.get("item_id"))
        return context
    
class ItemBuyView(TemplateView):
    model = Item
    template_name = "shoppinglist/item_buy.html"
 
    def post(self, request, *args, **kwargs):
        item_id = self.request.POST.get("item_id")
        item = get_object_or_404(Item, pk=item_id)
        if( item.buy == 0):
            item.buy = 1
        else:
            item.buy = 0
        return HttpResponseRedirect(reverse("list"))
 
    def get(self, request, *arg, **kwarg):
        context = super().get_context_data(**kwarg)
        context["form"] = ItemIdForm()
        item = get_object_or_404(Item, pk=kwarg.get("item_id"))
        if( item.buy == 0):
            item.buy = 1
        else:
            item.buy = 0
        item.save()
        return HttpResponseRedirect(reverse("list"))




from django import template

register = template.Library()

@register.filter
def name(querydict):
    name = querydict.get("name")
    return "" if name is None else name

@register.filter
def count(querydict):
    count = querydict.get("count")
    return "" if count is None else count

@register.filter
def buy_date(querydict):
    buy_date = querydict.get("buy_date")
    return "" if buy_date is None else buy_date

@register.filter
def buy(querydict):
    buy = querydict.get("buy")
    return "" if buy is None else buy

@register.filter
def order_kind(querydict):
    order_kind = querydict.get("order_kind")
    return "" if order_kind is None else order_kind

@register.filter
def order_by(querydict):
    order_by = querydict.get("order_by")
    return "" if order_by is None else order_by




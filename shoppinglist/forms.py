from django import forms  # @UnresolvedImport

class ItemBuy(forms.Form):
    status = (
        (0, "まだ"),
        (1, "ずんだ")
        )
    item_id = forms.IntegerField(label = "ID")
    item_status = forms.ChoiceField(label='STATUS',widget=forms.Select, choices=status)

class ItemIdForm(forms.Form):
    item_id = forms.IntegerField(label='ID') 

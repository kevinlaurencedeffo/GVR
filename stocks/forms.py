from .models import Stocks
from django import forms

class StockForm(forms.ModelForm):    
    class Meta:
        model=Stocks
        fields=('article_name','libele','quantite','prix','date','typea','si')

from django import forms


class FormulaForm(forms.Form):
	min_market_cap = forms.IntegerField()
	stock_quantity = forms.IntegerField()
	
from django import forms


class FormulaForm(forms.Form):
	symbols = forms.CharField()
	stock_quantity = forms.IntegerField()
	
from django import forms
from django.forms import ModelForm
from formula.models import Symbols

class FormulaForm(ModelForm):
	class Meta:
		model = Symbols
		fields = ['ticker']
	
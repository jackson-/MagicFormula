from django.shortcuts import render
from django.views.generic import View
from bs4 import BeautifulSoup as bs4
import requests as r
from formula.forms import FormulaForm
from formula.models import QueryHistory
from django.http import HttpResponse, JsonResponse
import json
import re

# Create your views here.
class IndexView(View):
	template_name = 'index.html'
	form_class = FormulaForm

	def get(self, request):
		return render(request, self.template_name, {'form':self.form_class})

class MagicView(View):
	template_name = 'index.html'
	form_class = FormulaForm
	lookup_url = "http://dev.markitondemand.com/Api/v2/Lookup/json?input="
	quote_url = "http://dev.markitondemand.com/Api/v2/Quote/json?symbol="

	def post(self, request):
		symbols = request.POST['symbols'].split(',')
		for value in range(len(symbols)):
			symbols[value] = symbols[value].strip()
		QueryHistory.objects.create(symbols=symbols)
		roc = []
		pe_ratio = []
		for value in symbols:
			value = value.upper()
			# result = r.get(self.lookup_url + value).json()
			url = r.get("http://174.129.18.141/companies/" + value + "/pe_ratio")
			soup = bs4(url.text)
			pe_text = soup.select('span#pgNameVal')
			pe_text = pe_text[0].text
			pe_text = re.split('\s+', pe_text)
			for i in range(1):
				pe_ratio.append(float(pe_text[i]))
			url = r.get("http://www.gurufocus.com/term/ROC_JOEL/" + value + "/Return%252Bon%252BCapital%252B%252B-%252BJoel%252BGreenblatt/")
			soup = bs4(url.text)
			for div in soup.select('.data_value'):
				roc.append(float(div.get_text()[:-19]))
		magic_dict = {}
		counter = -1
		for value in symbols:
			counter+=1
			magic_dict[value] = roc[counter]-pe_ratio[counter]
		print(magic_dict)
		return render(request, self.template_name, {'magic_dict':magic_dict, 'form':self.form_class})
		# return render(request, self.template_name, {'this':'isgood', 'form':self.form_class})
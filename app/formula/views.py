from django.shortcuts import render
from django.views.generic import View
from bs4 import BeautifulSoup as bs4
import requests as r
from formula.forms import FormulaForm
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
	lookup_url = "http://dev.markitondemand.com/Api/v2/Lookup/json?input="
	quote_url = "http://dev.markitondemand.com/Api/v2/Quote/json?symbol="

	def post(self, request):
		symbols = request.POST['symbols'].split(',')
		for value in range(len(symbols)):
			symbols[value] = symbols[value].strip()
		roc = []
		for value in symbols:
			value = value.upper()
			# result = r.get(self.lookup_url + value).json()
			url = r.get("http://174.129.18.141/companies/GOOG/pe_ratio")
			soup = bs4(url.text)
			thing = soup.select('span#pgNameVal')
			thing = thing[0].text
			thing = re.split('\s+', thing)

			print(thing[:1])
			# for div in soup.select('.Es'):
			# 	print(div.get_text())
			# url = r.get("http://www.gurufocus.com/term/ROC_JOEL/" + value + "/Return%252Bon%252BCapital%252B%252B-%252BJoel%252BGreenblatt/")
			# soup = bs4(url.text)
			# for div in soup.select('.data_value'):
			# 	roc.append(div.get_text()[:-18])

		url = "http://www.wikinvest.com/stock/Symantec_(SYMC)/Data/P:E"
		return HttpResponse('test')
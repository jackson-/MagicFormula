from django.shortcuts import render
from django.views.generic import View
from bs4 import BeautifulSoup as bs4
import requests as r
from formula.forms import FormulaForm
from formula.models import Symbols, Entry, History
from django.http import HttpResponse, JsonResponse
import json
import re

# Create your views here.
class IndexView(View):
	template_name = 'index.html'
	form_class = FormulaForm

	def get(self, request):
		history = Symbols.objects.all()
		sym_hist = []
		for hist in history:
			sym_hist.append(hist)
		return render(request, self.template_name, {'form':self.form_class, 'history':sym_hist})

class MagicView(View):
	template_name = 'index.html'
	form_class = FormulaForm
	lookup_url = "http://dev.markitondemand.com/Api/v2/Lookup/json?input="
	quote_url = "http://dev.markitondemand.com/Api/v2/Quote/json?symbol="

	def post(self, request):
		Entry.objects.create()
		entry = Entry.objects.last()
		symbols = request.POST['ticker'].split(',')
		for symbol in range(len(symbols)):
			symbols[symbol] = symbols[symbol].strip()
			Symbols.objects.create(ticker=symbols[symbol])
			sym = Symbols.objects.last()
			History.objects.create(entry_id=entry, sym_id=sym, magic_number=0, market_cap=0)
		roc = []
		pe_ratio = []
		cap_list = []
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
			value = value.lower()
			url = r.get("http://finance.yahoo.com/q/ks?s="+ value +"+Key+Statistics")
			soup = bs4(url.text)
			cap_array = soup.select("#yfs_j10_"+value)
			for i in cap_array:
				thing = i.text
				cap_list.append(thing)
		magic_dict = {}
		counter = -1
		for value in symbols:
			counter+=1
			magic_dict[value] = {'magic_number': roc[counter]-pe_ratio[counter], 'market_cap': cap_list[counter]}
		history = Symbols.objects.all()
		sym_hist = []
		for hist in history:
			sym_hist.append(hist)
		return render(request, self.template_name, {'magic_dict':magic_dict, 'form':self.form_class, 'history':sym_hist})


class TableView(View):
	template_name = "table.html"
	def get(self, request, entry_id=None):
		hist_id = request.path[7:-1]
		info = Symbols.objects.get(id=hist_id)
		symbols = info.ticker
		for value in symbols:
			print(value)
			value = value.strip()
		Symbols.objects.create(ticker=symbols)
		roc = []
		pe_ratio = []
		cap_list = []
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
			value = value.lower()
			url = r.get("http://finance.yahoo.com/q/ks?s="+ value +"+Key+Statistics")
			soup = bs4(url.text)
			cap_array = soup.select("#yfs_j10_"+value)
			for i in cap_array:
				cap = i.text
				cap_list.append(cap)
		magic_dict = {}
		counter = -1
		for value in symbols:
			counter+=1
			magic_dict[value] = {'magic_number': roc[counter]-pe_ratio[counter], 'market_cap': cap_list[counter]}
		return render(request, self.template_name, {'magic_dict':magic_dict})

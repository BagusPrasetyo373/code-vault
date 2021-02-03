import requests
from bs4 import BeautifulSoup as bsoup

url = {'search': 'https://www.urbandictionary.com/define.php?term='}

class UrbanDictionary:
	def search(query: str):
		if query != ' ' or query != '':
			f_query = query.replace(' ','%20')
			s_query = url['search']+f_query
			g_query = requests.get(s_query)
			ctx = g_query.text
			ctx_soup = bsoup(ctx,'html.parser')
			defi = ctx_soup.find('div',attrs={'class','meaning'}).text
			example = ctx_soup.find('div',attrs={'class','example'}).text
			tb = ctx_soup.find('div',attrs={'class','thumbs'})
			tb_up = tb.find('a',attrs={'class','up'}).text
			tb_down = tb.find('a',attrs={'class','down'}).text

			# get author with token method
			tok = ctx.split('author=')
			tok_end = tok[1].split('\">')
			auth = tok_end[1].split('<')

			return {'Term': query,'Meaning': defi,'Example': example, 'Total_Thumbs': tb.text, 'Thumbs_Up': tb_up, 'Thumbs_Down': tb_down, 'Author': auth[0]}

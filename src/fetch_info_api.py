import os
import re
import requests  
from bs4 import BeautifulSoup
ch=''
def main():
	
	def screen_clear():                                   #clearing terminal screen
		if os.name == 'nt':
			os.system('cls')
		else:
			os.system('clear')
			
	def intro():
		print("\t\t\t\t\t-----Google Play App Info------")
		box_msg(''' Created by Gautham Prakash @: gauthamp10@gmail.com''')
		
		
	def box_msg(msg):                                     #for printing text in a box
		row = len(msg)
		h = ''.join(['+'] + ['-' *row] + ['+'])
		result= h + '\n'"|"+msg+"|"'\n' + h
		print(result)	
		
	def print_lines():                                    #printing dotted lines
		print(("-"*68))	
	
	def get_app_link(query):
		html_page = requests.get("https://play.google.com/store/search?q="+query+"&c=apps")
		soup = BeautifulSoup(html_page.text,'html.parser')
		applink=soup.find('a',attrs={'class':'card-click-target'})
		return applink['href']
		
	def get_info(url,soup):
		name=soup.find('meta',attrs={'itemprop':'name'}) 
		icon=soup.find('img',attrs={'itemprop':'image'})
		price=soup.find('meta',attrs={'itemprop':'price'})
		priceCurrency=soup.find('meta',attrs={'itemprop':'priceCurrency'})
		desc=soup.find('meta',attrs={'itemprop':'description'})
		contentRating=soup.find('meta',attrs={'itemprop':'contentRating'})
		applicationCategory=soup.find('meta',attrs={'itemprop':'applicationCategory'})
		ratingValue=soup.find('meta',attrs={'itemprop':'ratingValue'})
		reviewCount=soup.find('meta',attrs={'itemprop':'reviewCount'})
		availability=soup.find('meta',attrs={'itemprop':'availability'})
		updated=soup.find('span',attrs={'class':'htlgb'})
		print("App name: ",name['content'])
		print("Icon url: ",icon['src'])
		print("Price: ",price['content']+priceCurrency['content'])
		print("Description: ",desc['content'][:80]+".....")
		print("Content Rated for: ",contentRating['content'])
		print("Category: ",applicationCategory['content'])
		print("Rating: ",ratingValue['content'])
		print("Total Reviews: ",reviewCount['content'])
		print("Last Updated on: ",updated.text)
		print("Availability: ",availability['content'].rsplit('/',1)[1])
		print("App URL: ",url)
	
	screen_clear()
	intro()	
	query=input("Enter the app name: ")
	query=query.replace(' ','+')

	try:	
		url='https://play.google.com'+get_app_link(query)
		print_lines()
		data=requests.get(url)
		soup = BeautifulSoup(data.text,'html.parser')
		get_info(url,soup)
	except:
		print("Network Error| Unknown App!...")
	print_lines()	
	
if __name__ == '__main__':                                       #Calling main(), the actual entry point for the scraper
    
	main()
	exit(0)

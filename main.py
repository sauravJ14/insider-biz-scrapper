
#Add name of companies in below list
# thinks to  remeber
# you have to add - in place of space after every character and remove any brackets if there
comp=['TATA-ADVANCED-SYSTEMS-LIMITED','TATA-GLOBAL-BEVERAGES-LIMITED','WHITE-DIAMOND-INDUSTRIES-LIMITED',
'MARDIA-FARMS-LIMITED',
'EURO-AGRO-INDIA-LIMITED']

import concurrent.futures
import requests
from bs4 import BeautifulSoup

def get_address(company):
    url = f"https://www.insiderbiz.in/company/{company}"
    response = requests.get(url)
    website_html = response.text
    soup = BeautifulSoup(website_html, "html.parser")
    establishments_details_div = soup.find("div", class_="col-lg-6")
    address_p = establishments_details_div.find("p", string="Registered Office Address:")
    if address_p:
        address_text = address_p.find_next("p").get_text(strip=True)
        print(address_text)
    else:
        print(f"No registered office address found for {company}.")



with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(get_address, comp)

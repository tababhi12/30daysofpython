#with dynamic url 
import requests
from bs4 import BeautifulSoup
file = 'scrapping_data.txt'
base_url = 'https://www.yelp.com/search?cflt=restaurants&find_loc='
page = 0
while page < 200:
    print(page)
    loc = 'New York,NY'
    url = base_url + loc + '&start=' + str(page)
    yelp_r = requests.get(url)
    #print(yelp_r.status_code)
    soup = BeautifulSoup(yelp_r.text,'html.parser')
    #print(soup.prettify())
    bel = soup.findAll('div',{'class':'lemon--div__373c0__1mboc businessName__373c0__1fTgn border-color--default__373c0__2oFDT'})
    addphone = soup.findAll('div',{'class':'lemon--div__373c0__1mboc container__373c0__19wDx u-padding-l2 border-color--default__373c0__2oFDT text-align--right__373c0__3fmmn'})
    for ad,b in zip(addphone,bel):
        with open(file,'a') as f:
            try:
                title = b.findAll('a')[0].text
                address = ad.findAll('address')[0].text
                phone = ad.findAll('div',{'class':'lemon--div__373c0__1mboc display--inline-block__373c0__2de_K u-space-b1 border-color--default__373c0__2oFDT'})[0].text
                page_line = f'{title} has address {address} and phone number {phone}\n'  
                f.write(page_line)
            except:
                pass
    page = page + 30
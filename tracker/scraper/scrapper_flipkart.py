class scrapper_flipkart:
    def __price__(URL):
        import mysql.connector
        from bs4 import BeautifulSoup
        import requests

        header = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 OPR/89.0.4447.64 (Edition std-1)'}

        page = requests.get(URL, headers=header)

        soup = BeautifulSoup(page.content, 'html.parser')

        if URL != '':
            try:
                price = soup.find("div", "_30jeq3 _16Jk6d").get_text()
            except:
                price = 'NaN'

        else: price ='NaN'


        return price
    

class scrapper_amazon:
    
    def __price__(URL):

        header = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 OPR/89.0.4447.64 (Edition std-1)'}

        from bs4 import BeautifulSoup
        import requests
   
        page = requests.get(URL, headers=header)

        soup = BeautifulSoup(page.content, 'html.parser')

        try:
            price = soup.find("span", "a-offscreen").get_text()
        except:
            price = 'NaN'


        return price
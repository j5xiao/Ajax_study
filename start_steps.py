URL = 'https://spa1.scrape.center/'

import requests
html = requests.get(URL).text
# print(html)

"""
Output:
    <!DOCTYPE html>
    <html lang=en><head><meta charset=utf-8>
    <meta http-equiv=X-UA-Compatible content="IE=edge">
    <meta name=viewport content="width=device-width,initial-scale=1">
    <link rel=icon href=/favicon.ico>
    <title>Scrape | Movie</title>
    <link href=/css/chunk-700f70e1.1126d090.css rel=prefetch><
    link href=/css/chunk-d1db5eda.0ff76b36.css rel=prefetch>
    <link href=/js/chunk-700f70e1.0548e2b4.js rel=prefetch>
    <link href=/js/chunk-d1db5eda.b564504d.js rel=prefetch>
    <link href=/css/app.ea9d802a.css rel=preload as=style>
    <link href=/js/app.17b3aaa5.js rel=preload as=script>
    <link href=/js/chunk-vendors.683ca77c.js rel=preload as=script>
    <link href=/css/app.ea9d802a.css rel=stylesheet></head><body>
    <noscript>
    <strong>We're sorry but portal doesn't work properly without 
            JavaScript enabled. Please enable it to continue.</strong></noscript>
    <div id=app></div><script src=/js/chunk-vendors.683ca77c.js>
    </script><script src=/js/app.17b3aaa5.js></script></body></html>
"""

html_2 = requests.get('https://spa1.scrape.center/api/movie/11').json()
# print(html_2)


"""
Start Practice
"""
URL_INDEX = "https://spa1.scrape.center/api/movie/?limit={limit}&offset={offset}"

def scrape_page(url):
    try:
        respones = requests.get(url)
        if respones.status_code == 200:
            return respones.json()
    except:
        return "Wrong!"
    
def get_index(page):
    limit = 10
    index_url = URL_INDEX.format(limit=10, offset=limit * (page - 1))
    return scrape_page(index_url)

def page_deatil(count):
    element_url = 'https://spa1.scrape.center/api/movie/{}'.format(count)
    print(element_url)
    return scrape_page(element_url)

def main():
    total_page = 1
    for i in range(1, total_page + 1):
        page = get_index(i)
        for j in page.get('results'):
            result = page_deatil(j['id'])
            print("Name: {}".format(result['name']))
            print("Alias: {}".format(result['alias']))
            print("Categories: {}".format(result['categories']))


if __name__ == "__main__":
    main()
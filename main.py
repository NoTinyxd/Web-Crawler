import curl_cffi as requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


visited = set()

queue = ['google.com']
print(f"Crawling {queue}")
while queue:
    url = queue.pop(0)
    if url in visited:
        continue
    visited.add(url)
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")


    for a_tag in soup.find_all("a"):
        href = a_tag.get("href")  
        if not href:
            continue
        full_urls = urljoin(url,href)
        if full_urls.startswith('http'):
            if full_urls not in visited:
                queue.append(full_urls)
        print(f"FOUND {full_urls} \n")

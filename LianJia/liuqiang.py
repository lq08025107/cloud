from bs4 import BeautifulSoup
html = """
<p>aaa</p>     bbb
<p>ccc</p>/&nbsp;ddd
"""
soup = BeautifulSoup(html,"html.parser")
for p in soup.findAll('p'):
    print p.next_sibling.strip().strip()
#[p.next_sibling.strip() for p in soup.findAll('p')]
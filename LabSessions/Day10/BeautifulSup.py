from bs4 import BeautifulSoup
import requests
import urllib3

# requests verify=False causes SSL warning → suppress it
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

html = """
<html>
<head><title>My Page</title></head>
<body>

<h1>Welcome</h1>
<h2>Sub heading</h2>

<p>This is first paragraph.</p>
<p>This is second paragraph.</p>

<a href="https://google.com">Google</a>
<a href="https://github.com">GitHub</a>

<b>Bold Text Here</b>

<img src="image1.jpg" alt="img1">
<img src="image2.png" alt="img2">

<table>
<tr><th>Name</th><th>Age</th></tr>
<tr><td>Deepak</td><td>22</td></tr>
<tr><td>Rahul</td><td>25</td></tr>
</table>

</body>
</html>
"""

# BeautifulSoup builds a DOM tree (like browser inspector Elements tab)
# Every tag becomes a Python object → Tag, NavigableString, Attribute
soup = BeautifulSoup(html, "html.parser")


# soup.title → traverses tree root → head → title node
# .text → extracts inner text by removing tags
print("\n1) Title:", soup.title.text)

# soup.h1 → returns first occurrence while scanning depth-first
print("H1:", soup.h1.text)


print("\n2) Paragraphs:")
# find_all walks entire tree and collects every <p> node into list
for p in soup.find_all("p"):
    # p.text reads child text node stored inside Tag object
    print(p.text)


# find_all("a") → returns list of anchor Tag objects
links = soup.find_all("a")

# len() works because result is a Python list
print("\n3) Links Count:", len(links))

for l in links:
    # l.text → child text node
    # l.get("href") → fetch attribute from attribute dictionary
    print(l.text, "->", l.get("href"))


print("\n4) Attributes of first link:")
# every Tag stores attributes internally as dictionary
# {'href': 'https://google.com'}
print(links[0].attrs)


# find() stops at first match instead of scanning entire document
print("\n5) First h2:", soup.find("h2").text)


# returns first <b> node then extracts its text child
print("\n6) Bold Text:", soup.find("b").text)


print("\n7) All href values:")
for l in links:
    # l["href"] directly accesses attribute dictionary key
    print(l["href"])


print("\n8) All Text:")
# get_text() recursively traverses all nodes
# joins every text node using separator
print(soup.get_text(separator="\n"))


print("\n9) Website Title:")
# HTTP GET request downloads HTML
res = requests.get("https://example.com", verify=False)

# parse downloaded HTML into another DOM tree
websoup = BeautifulSoup(res.text, "html.parser")

# again tree traversal → head → title
print(websoup.title.text)


print("\n10) All Headings:")
# passing list → BeautifulSoup checks tag.name in list
for tag in soup.find_all(["h1","h2","h3","h4","h5","h6"]):
    print(tag.name, ":", tag.text)


print("\n11) Table Data:")
# find_all("tr") collects row nodes
rows = soup.find_all("tr")

for row in rows:
    # inside each row search th and td children only
    # list comprehension builds Python list of column texts
    cols = [col.text for col in row.find_all(["td","th"])]
    print(cols)


print("\n12) Images:")
# extract src attribute from each image node
for img in soup.find_all("img"):
    print(img.get("src"))

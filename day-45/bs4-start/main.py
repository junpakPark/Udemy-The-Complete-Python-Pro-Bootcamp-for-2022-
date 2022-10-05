from bs4 import BeautifulSoup
import requests

res = requests.get("https://news.ycombinator.com/")
yc_web_page = res.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.select(".titleline a")

article_text = []
article_link = []
for i in range(0, len(articles), 2):
    article_text.append(articles[i].getText())
    article_link.append(articles[i].get("href"))

article_upvotes = [int(score.getText().split()[0]) for score in soup.select('.score')]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_text[largest_index])
print(article_link[largest_index])




# import lxml


# with open("website.html") as site:
#     contents = site.read()

# soup = BeautifulSoup(contents, 'html.parser')

# # print(soup)
# # print(soup.prettify())

# # print(soup.title)
# # print(soup.title.string)

# # print(soup.a)
# # print(soup.p)

# all_anchor_tag = soup.find_all(name="a")

# # print(all_anchor_tag)

# for tag in all_anchor_tag:
#     print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find_all(name="h1", id="name")
# print(heading)

# class_heading = soup.find_all(class_="heading")
# print(class_heading)

# section_heading = soup.find_all(name="h3", class_="heading")
# print(section_heading)

# company_url = soup.select_one(selector="p a")
# print(company_url)

# name = soup.select_one(selector="#name")
# print(name)

# headings = soup.select(".heading")
# print(headings)

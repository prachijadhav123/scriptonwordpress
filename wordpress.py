import MySQLdb
import bs4
import requests
res=requests.get("https://wordpress.com/themes")
soup=bs4.BeautifulSoup(res.text,"lxml")
image=[]
for images in soup.find_all('img',{"class":"theme__img"}):
    image.append(images.get("src"))
print("scrapped links: ",image)



res=requests.get("https://en.blog.wordpress.com/")
soup=bs4.BeautifulSoup(res.text,"lxml")
posts=[]
for post in soup.find_all('p'):
    posts.append(post.text)
print("Scrapped Posts: ",posts)
res=requests.get("https://wordpress.com/create-blog/")
soup=bs4.BeautifulSoup(res.text,"lxml")
blogs=[]
for blog in soup.find_all('h5',{'class':"lp-features-feature--title no-widows"}):
    blogs.append(blog.text.strip())
print("Scrapped blogs: ",blogs)

blog_detail=[]
for detail in soup.find_all('div',{"class":"lp-features-feature--description no-widows lp-text"}):
    blog_detail.append(detail.text.strip())
print("scrapped blog details corresspond to blog: ",blog_detail)

db = MySQLdb.connect(host='127.0.0.1', user='root', password='root', db='wordpress')
cur = db.cursor()
sql_insert_query='''REPLACE INTO `wordpress`.`images` (`idimages`) VALUES (%s)'''
df=cur.executemany(sql_insert_query,image)
db.commit()
print("Total "+str(len(image))+" ImagesLink Successfully stored in database.")


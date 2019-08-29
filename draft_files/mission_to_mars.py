from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    # Visit mars.nasa.gov/news
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    try:
        html = browser.html
        soup = bs(html, "html.parser")
                            # get_text(strip=True)
        news = soup.find('div', {"class":'list_text'}).text

        dict_test = {"x":news}

        # news_text=soup.find_all()
    
    except NameError:
        pass

    browser.quit()
    
    return dict_test

    
#  # Print all ten headlines
# tds = soup.find_all('td')
# # A blank list to hold the headlines
# headlines = []
# # Loop over td elements
# for td in tds:
#     # If td element has an anchor...
#     if (td.a):
#         # And the anchor has non-blank text...
#         if (td.a.text):
#             # Append the td to the list
#             headlines.append(td)

# Print all paragraph texts
# paragraphs = soup.find_all('p')
# for paragraph in paragraphs:
#     print(paragraph.text)

# Retrieve the parent divs for all articles
# results = soup.find_all('li', class_='mixed-feed__item--article')

# # Loop through results to retrieve article title, header, and timestamp of article
# for result in results:
#     title = result.find('h4', class_='mixed-feed__header').text

#     lede = result.find('h5', class_='mixed-feed__subheader').text

#     # The time and date of article publication
#     date = result.find('time')['datetime']
#     # Slice the datetime string for the date
#     article_date = date[:10]
#     # Slice the datetime string for the time
#     time = date[11:16]
#     # Determine whether article was published in AM or PM
#     if (int(time[:2]) >= 13):
#         meridiem = 'pm'
#     else:
#         meridiem = 'am'

#     # Concatenate time string
#     time = time + meridiem
#     print('-----------------')
#     print(title)
#     print(lede)
#     print(article_date)
#     print(time)

#     # Dictionary to be inserted into MongoDB
#     post = {
#         'title': title,
#         'lede': lede,
#         'date': article_date,
#         'time published': time
#     }

#     # Insert dictionary into MongoDB as a document
#     collection.insert_one(post)

# Pandas reader code example:
# url = 'https://en.wikipedia.org/wiki/List_of_medical_abbreviations'
# med_abbreviations = ['BMR', 'BP', 'ECG', 'MRI', 'qid', 'WBC']
# Use Panda's `read_html` to parse the url
# tables = pd.read_html(url)
# Find the medical abbreviations DataFrame in the list of DataFrames as assign it to `df`
# Assign the columns `['abb', 'full_name', 'other']`
### BEGIN SOLUTION
# df = tables[2]
# df.columns = ['abb', 'full_name', 'other']
# df.head()
### END SOLUTION
# Assign the columns `['abb', 'full_name', 'other']`
### BEGIN SOLUTION
# df = tables[2]
# df.columns = ['abb', 'full_name', 'other']
# df.head()
### END SOLUTION
# drop the `other` column
### BEGIN SOLUTION
# del df['other']
### END SOLUTION
# Loop through the list of medical abbreviations and print the abbreviation
# along with the full description.
# Use the DataFrame to perform the lookup.
### BEGIN SOLUTION
# for abb in med_abbreviations:
#     print(abb, df.loc[abb].full_name)
### END SOLUTION


# Splinter code example:
# html = browser.html
# soup = BeautifulSoup(html, 'html.parser')

# sidebar = soup.find('ul', class_='nav-list')

# categories = sidebar.find_all('li')

# category_list = []
# url_list = []
# book_url_list = []
# for category in categories:
#     title = category.text.strip()
#     category_list.append(title)
#     book_url = category.find('a')['href']
#     url_list.append(book_url)

# book_url_list = ['http://books.toscrape.com/' + url for url in url_list]

# titles_and_urls = zip(category_list, book_url_list)

# try:
#     for title_url in titles_and_urls:
#         browser.click_link_by_partial_text('next')
# except ElementDoesNotExist:
#     print("Scraping Complete")

#Another Splinter example:

# url = 'http://quotes.toscrape.com/'
# browser.visit(url)  In [6]:  for x in range(1, 6):

#     html = browser.html
#     soup = BeautifulSoup(html, 'html.parser')

#     quotes = soup.find_all('span', class_='text')

#     for quote in quotes:
#         print('page:', x, '-------------')
#         print(quote.text)

#     browser.click_link_by_partial_text('Next')
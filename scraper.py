from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.edge.options import Options
import pandas as pd
import time


def duration_in_minutes(duration):
    if type(duration) is not str:
        return duration
    total_time = 0
    durations = duration.split('and')
    for duration in durations:
        time_quantity, abbreviation = duration.split()
        time_quantity = int(time_quantity)
        if abbreviation in ['hrs', 'hr']:
            total_time += time_quantity*60
        elif abbreviation in ['mins', 'min']:
            total_time += time_quantity
    return total_time


def data_cleaning(data):
    # Function to clean up data columns
    data.author = data.author.apply(lambda x: x[len('Written by:'):].strip() if x.startswith('Written by:') else x)
    data.narrator = data.narrator.apply(
        lambda x: x[len('Narrated by:'):].strip() if x.startswith('Narrated by:') else x)
    data.series = data.series.apply(lambda x: x[len('Series:'):].strip() if x.startswith('Series:') else x)

    data.runtime = data.runtime.apply(lambda x: x[len('Length:'):].strip() if x.startswith('Length:') else x)
    data.runtime = data.runtime.apply(duration_in_minutes)

    data.release_date = data.release_date.apply(
        lambda x: x[len('Release Date:'):].strip() if x.startswith('Release Date:') else x)
    data.language = data.language.apply(lambda x: x.split(' ')[-1])
    data.total_ratings = data.total_ratings.apply(lambda x: x.split(' ')[0] if 'rating' in x else '0' if x == 'NA' else x)
    data.stars = data.stars.apply(lambda x: x.split(' ')[0] if 'stars' in x else '0' if x == 'Not rated yet' else x)

    data.price = data.price.str.replace('Listen for free', '0')
    data.price = data.price.str.replace('₹', '').str.replace(',', '')
    return data


options = Options()
# options.add_argument('--headless') # to turn on headless mode
# options.add_argument('window-size=1920x1080')

# Initialize webdriver
website = 'https://www.audible.in/search'
# Change the path to the location where you have downloaded the WebDriver executable
path = "D:/Software/edgeDriver/msedgedriver.exe"
edgeService = webdriver.EdgeService(executable_path=path)
driver = webdriver.Edge(service=edgeService, options=options)

driver.get(website)
driver.maximize_window()

# Fetch total number of pages for pagination
pagination = driver.find_element(by='xpath', value='//ul[contains(@class,"pagingElements")]')
total_pages = int(pagination.find_elements(By.TAG_NAME, value='li')[-2].text)

# XPaths for different data fields
audiobook_xpath = './div/span[2]/ul/li'
xpath_dict = {
    'title': './/h3[contains(@class,"bc-heading")]',
    'author': './/li[contains(@class,"authorLabel")]/span',
    'narrator': './/li[contains(@class,"narratorLabel")]/span',
    'series': './/li[contains(@class,"seriesLabel")]/span',
    'runtime': './/li[contains(@class,"runtimeLabel")]',
    'release_date': './/li[contains(@class,"releaseDateLabel")]/span',
    'language': './/li[contains(@class,"languageLabel")]/span',
    'total_ratings': './/li[contains(@class,"ratingsLabel")]/span[2]',
    'stars': './/li[contains(@class,"ratingsLabel")]/span[1]',
    'price': ('.//p[contains(@class,"buybox-regular-price")]/span[2]',
              './/div[contains(@id,"buybox-trigger")]')
}

# Loop through each page
data = pd.DataFrame()
for i in range(total_pages):
    container = driver.find_element(by='xpath', value='//div[@data-widget="productList"]')
    # Loop through each audiobook element on the current page
    for book in container.find_elements(By.XPATH, value=audiobook_xpath):
        audiobook_dict = {key: 'NA' for key in xpath_dict.keys()}
        for key, value in xpath_dict.items():
            try:
                # Try to extract data for each field using XPath
                if key != 'price':
                    audiobook_dict[key] = book.find_element(by='xpath', value=value).text
                else:
                    try:
                        audiobook_dict[key] = book.find_element(by='xpath', value=value[0]).text
                    except:
                        audiobook_dict[key] = book.find_element(by='xpath', value=value[1]).text
            except exceptions.NoSuchElementException:
                print('"{}" is not available for book name "{}"'.format(key, audiobook_dict['title']))
            except Exception as e:
                print(e)
        # Concatenate extracted data into DataFrame
        data = pd.concat((data, pd.DataFrame([audiobook_dict])), ignore_index=True)
    try:
        # Click on next button to navigate to the next page
        nxt_btn = driver.find_element(by='xpath', value='//span[contains(@class,"nextButton")]')
        nxt_btn.click()
    except Exception as e:
        print(e)
    time.sleep(2)  # Add a short delay to ensure the page loads completely

# Quit the webdriver after fetching all data
driver.quit()

# Clean up data and save to CSV
data = data_cleaning(data)
data.rename(columns={'runtime': 'runtime (in minutes)', 'stars': 'stars (out of 5)', 'price': 'price (in rupees)'},
            inplace=True)
data.to_csv('audiobooks.csv', index=False)

# Amazon Audiobooks Scraper

This repository contains a Python script for scraping data from Amazon's audiobooks section. The script utilizes the Selenium library to automate web browsing and extract information such as title, author, narrator, series, runtime, release date, language, total ratings, stars, and price of various audiobooks available on Amazon.

## Amzon Audiobooks Website Screenshot
![image](https://github.com/HarmanBytes/Amazon-Audiobooks-Scraper/assets/105145207/13be0a3b-036a-4e7c-8d5c-f50857d62510)

## Usage

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your_username/amazon-audiobooks-scraper.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Python script to scrape audiobook data:

```bash
python scrape_audiobooks.py
```

4. The scraped data will be saved to a CSV file named `audiobooks.csv` in the same directory.

## Sample Data

Below is a sample of the data scraped from Amazon's audiobooks:

| Title                                        | Author                                      | Narrator                                    | Series                        | Runtime          | Release Date | Language      | Total Ratings | Stars         | Price     |
|----------------------------------------------|---------------------------------------------|---------------------------------------------|-------------------------------|------------------|--------------|---------------|---------------|---------------|-----------|
| Kautilya Arthshastra (Hindi Edition)         | Chanakya                                    | Ashwini Walia                              | NA                            | 6 hrs            | 26-02-20     | Language: Hindi | 40            | 4.5           | Listen for free |
| The Art of Focus                            | Dan Koe                                     | Dan Koe                                     | NA                            | 6 hrs and 52 mins| 16-01-24    | Language: English | 3             | 5             | ₹668.00  |
| Generative AI                               | Harvard Business Review                     | Randye Kaye, Mike Lenz                     | HBR Insights Series           | 3 hrs and 4 mins| 27-02-24     | Language: English | NA            | Not rated yet | ₹351.00  |
| The Art of Influencing People              | Virender Kapoor                             | Rajat Verman                               | NA                            | 38 mins          | 03-05-18     | Language: English | 26            | 4             | Listen for free |
| The First Rule of Mastery                  | Michael Gervais, Kevin Lake - contributor  | Michael Gervais                            | NA                            | 5 hrs and 3 mins | 20-02-24     | Language: English | NA            | Not rated yet | ₹586.00  |
| Kaisa Kutta Hai [What Kind of Dog Is That] | Rahgir                                      | Rishi Upadhyay                             | NA                            | 2 hrs and 38 mins| 07-02-24     | Language: Hindi | NA            | Not rated yet | ₹233.00  |

## Note

This script is intended for educational purposes only. Use it responsibly and respect Amazon's terms of service.

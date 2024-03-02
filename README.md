# Amazon Audiobooks Scraper

This repository contains a Python script for scraping data from Amazon's audiobooks section. The script utilizes the Selenium library to automate web browsing and extract information such as title, author, narrator, series, runtime, release date, language, total ratings, stars, and price of various audiobooks available on Amazon.

## Amzon Audiobooks Website Screenshot
![image](https://github.com/HarmanBytes/Amazon-Audiobooks-Scraper/assets/105145207/13be0a3b-036a-4e7c-8d5c-f50857d62510)

## Usage

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your_username/Amazon-Audiobooks-Scraper.git
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

<table class="table table-bordered table-hover table-condensed">
    <thead>
        <tr>
            <th title="Field #1">title</th>
            <th title="Field #2">author</th>
            <th title="Field #3">narrator</th>
            <th title="Field #4">series</th>
            <th title="Field #5">runtime (in minutes)</th>
            <th title="Field #6">release_date</th>
            <th title="Field #7">language</th>
            <th title="Field #8">total_ratings</th>
            <th title="Field #9">stars (out of 5)</th>
            <th title="Field #10">price (in rupees)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>The Art of Influencing People</td>
            <td>Virender Kapoor</td>
            <td>Rajat Verman</td>
            <td>NA</td>
            <td align="right">38</td>
            <td>03-05-18</td>
            <td>English</td>
            <td align="right">26</td>
            <td align="right">4</td>
            <td align="right">0</td>
        </tr>
        <tr>
            <td>Vaishali Ki Nagarvadhu [City of Vaishali]</td>
            <td>Acharya Chatursen</td>
            <td>Ashish Bhandari</td>
            <td>NA</td>
            <td align="right">1433</td>
            <td>10-06-20</td>
            <td>Hindi</td>
            <td align="right">138</td>
            <td align="right">4.5</td>
            <td align="right">0</td>
        </tr>
        <tr>
            <td>Kaisa Kutta Hai [What Kind of Dog Is That]</td>
            <td>Rahgir</td>
            <td>Rishi Upadhyay</td>
            <td>NA</td>
            <td align="right">158</td>
            <td>07-02-24</td>
            <td>Hindi</td>
            <td align="right">1</td>
            <td align="right">4</td>
            <td align="right">233.00</td>
        </tr>
        <tr>
            <td>21 Shreshth Kahaniyan Prem Chand (Hindi Edition)</td>
            <td>Munshi Premchand</td>
            <td>Avdhesh Tondak</td>
            <td>NA</td>
            <td align="right">464</td>
            <td>19-07-21</td>
            <td>Hindi</td>
            <td align="right">159</td>
            <td align="right">5</td>
            <td align="right">0</td>
        </tr>
        <tr>
            <td>41 Anmol Kahaniya [41 Priceless Stories]</td>
            <td>Premchand</td>
            <td>Prachi Chaube</td>
            <td>NA</td>
            <td align="right">928</td>
            <td>14-10-21</td>
            <td>Hindi</td>
            <td align="right">43</td>
            <td align="right">4.5</td>
            <td align="right">1003.00</td>
        </tr>
        <tr>
            <td>Kautilya Arthshastra (Hindi Edition)</td>
            <td>Chanakya</td>
            <td>Ashwini Walia</td>
            <td>NA</td>
            <td align="right">360</td>
            <td>26-02-20</td>
            <td>Hindi</td>
            <td align="right">40</td>
            <td align="right">4.5</td>
            <td align="right">0</td>
        </tr>
    </tbody>
</table>

- A price of 0 indicates that the book is available for free listening.
- Books that have not been rated yet are assigned a rating count of 0.
- A star rating of 0 in the stars column signifies that the book has not been rated yet.

## Note

This script is intended for educational purposes only. Use it responsibly and respect Amazon's terms of service.

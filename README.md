# LinkedIn Job Scraper

Automatically search for job listings on LinkedIn using Google search and save the results to an Excel file.

- **Automated Search**: Uses Selenium to perform a Google search for LinkedIn job listings.
- **Customizable Filters**: Includes filters for job role, location, experience level, and required skills.
- **Data Export**: Saves the top 10 job listing URLs to an Excel file.

## How to Use

1. **Install requirements**: Open your terminal and run `pip install -r requirements.txt`
2. **Download ChromeDriver**: Ensure you have the correct version of ChromeDriver for your Chrome browser and place it in the same directory as the script.
3. **Run the Script**: Execute the `main.py` script to start the job search and data collection process.

## Features

- **Google Search Integration**: Utilizes Google search to find LinkedIn job listings.
- **Advanced Search Filters**: Includes filters for:
  - Job role (e.g., "Python" OR "Desenvolvedor Python")
  - Work arrangement (e.g., "remoto" OR "Remote")
  - Location (e.g., "Brasil" OR "Brazil")
  - Experience level (e.g., "júnior" OR "trainee" OR "estágio")
  - Required skills (e.g., "VBA" OR "Python" OR "SQL" OR "Inglês" OR "Excel" OR "Power BI")
- **Time-based Filtering**: Filters results to show job listings from the last month.
- **Data Collection**: Collects URLs of the top 10 job listings.
- **Excel Export**: Saves the collected URLs to an Excel file named 'job_links.xlsx'.

## Script Components

### Web Automation
- **Library Used**: Selenium WebDriver
- **Purpose**: To automate the process of searching Google and interacting with search results.
- **Features**:
  - Automated Google search
  - Interaction with search tools and date filters
  - Collection of job listing URLs

### Data Processing
- **Library Used**: Pandas
- **Purpose**: To organize and export the collected data.
- **Features**:
  - Creation of a DataFrame with collected URLs
  - Export of data to an Excel file

### Note on Usage
This script is intended for educational purposes and personal use. Be aware that web scraping may be against the terms of service of some websites. Always review and comply with the terms of service and robots.txt files of the websites you interact with.
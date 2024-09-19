from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchWindowException, WebDriverException
import time

# Initialize the Chrome WebDriver
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Bypass bot detection (only needs to be done once)


# Set Base URL
base_url = "Add URL"

try:
    for page_number in range(1, 10):
        # Set complete URL with page number
        page_url = f"{base_url}{page_number}"
        
        # Open the webpage
        driver.get(page_url)
        
        # Allow some time for the page to load completely
        time.sleep(.5)  # Adjust sleep time as necessary
        
        try:
            # Get the page content
            page_source = driver.page_source
            
            # Pass the content to BeautifulSoup for parsing
            soup = BeautifulSoup(page_source, "html.parser")
            
            # Find the price elements
            price_elements = soup.findAll("Set element type", class_="Set element name")
            
            if price_elements:
                # Extract and print the price information
                for price in price_elements:
                    print(price.text)
            else:
                # Print a message if no results are found
                print(f"No results found on page {page_number}.")
                
        except NoSuchWindowException:
            print("The window was closed unexpectedly during processing.")
            break  # Exit the loop if the window is closed
        
        except WebDriverException as e:
            print(f"WebDriverException occurred: {e}")
            break  # Exit the loop on WebDriver exceptions

finally:
    # Ensure the browser is closed properly
    driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import random
import threading

# Path to Brave Browser executable
brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"  # Replace with your Brave path

# Path to ChromeDriver
chromedriver_path = "C:\\Apps\\ChromeDriver\\chromedriver.exe"  # Replace with your ChromeDriver path

# Login credentials
email = "jugheadjones0194@gmail.com"  # Replace with your email
password = "OnePiece0192"  # Replace with your password

# List of websites to claim coins from
websites = [
    "https://freebitcoinclick.com",
    "https://freeethereumclick.com",  # Add more websites here
    "https://freetronclick.com",
    "https://freetonclick.com",
    "https://freelitecoinclick.com",
    "https://freedogeclick.com",
    "https://freebnbclick.com",
    "https://freeadaclick.com"    
    # Add more websites as needed
]

# Function to log in
def login(driver, website, email, password):
    try:
        # Open the website
        driver.get(website)

        # Wait for the page to load
        time.sleep(10)

        # Find the login button and click it
        home_claim_button = driver.find_element(By.CLASS_NAME, 'Main_button__Mal_0')
        home_claim_button.click()
        time.sleep(3)
        
        go_to_login_button = driver.find_element(By.CLASS_NAME, 'CreateAccount_link__gNu5i')
        go_to_login_button.click()
        time.sleep(3)
        
        # Find the email input field and enter the email
        email_input = driver.find_element(By.NAME, 'email')  # Replace 'email' with the actual name or ID of the email input field
        email_input.send_keys(email)

        # Find the password input field and enter the password
        password_input = driver.find_element(By.NAME, 'password')  # Replace 'password' with the actual name or ID of the password input field
        password_input.send_keys(password)
        
        login_button = driver.find_element(By.CLASS_NAME, 'SignIn_button__bXTeV')  # Replace 'login-button' with the actual class name or ID of the login button
        login_button.click()

        # Wait for the login process to complete
        time.sleep(10)

    except Exception as e:
        print(f"An error occurred during login on {website}: {e}")

# Function to claim coins
def claim_coins(driver, website):
    try:
        # Open the website
        driver.get(website)

        # Wait for the page to load
        time.sleep(5)

        # Find the "Claim" button and click it
        claim_button = driver.find_element(By.CLASS_NAME, 'Main_button__Mal_0')  # Replace with the actual class name or ID of the button
        claim_button.click()

        # Wait for a few seconds to ensure the claim is processed
        time.sleep(5)

    except Exception as e:
        print(f"An error occurred on {website}: {e}")

# Function to handle all websites in tabs
def bot_tabs():
    # Set up Brave options
    options = webdriver.ChromeOptions()
    options.binary_location = brave_path  # Specify the path to Brave

    # Initialize the WebDriver with Brave
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)

    # Open the first website in the main tab
    driver.get(websites[0])

    # Open the remaining websites in new tabs
    for website in websites[1:]:
        driver.execute_script("window.open('');")  # Open a new tab
        driver.switch_to.window(driver.window_handles[-1])  # Switch to the new tab
        driver.get(website)  # Open the website in the new tab

    # Log in to all websites
    for i, website in enumerate(websites):
        driver.switch_to.window(driver.window_handles[i])  # Switch to the tab
        login(driver, website, email, password)

    # Start claiming coins on all websites
    while True:
        for i, website in enumerate(websites):
            driver.switch_to.window(driver.window_handles[i])  # Switch to the tab
            claim_coins(driver, website)
            time.sleep(5)
            
        # Wait for a random time between 10 to 15 minutes before the next claim
        wait_time = random.randint(620, 660)  # 600 seconds = 10 minutes, 900 seconds = 15 minutes
        time.sleep(wait_time)

# Run the bot
if __name__ == "__main__":
    bot_tabs()
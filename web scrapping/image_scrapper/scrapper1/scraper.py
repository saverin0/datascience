import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from PIL import Image
import base64
from io import BytesIO

def fetch_image_urls(query: str, max_links_to_fetch: int, wd: webdriver, sleep_between_interactions: int = 1):
    def scroll_to_end(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(sleep_between_interactions)

    search_url = "https://www.google.com/search?tbm=isch&q={q}"
    wd.get(search_url.format(q=query))

    image_urls = set()
    image_count = 0
    results_start = 0
    while image_count < max_links_to_fetch:
        scroll_to_end(wd)

        # Debugging: Print the page source to understand the structure
        print("Page source length:", len(wd.page_source))

        # Updated CSS selectors
        thumbnail_results = wd.find_elements(By.CSS_SELECTOR, "img")
        number_results = len(thumbnail_results)
        
        print(f"Found: {number_results} thumbnail(s). Extracting links from {results_start}:{number_results}")

        if number_results == 0:
            print("No thumbnails found. Exiting.")
            break

        for img in thumbnail_results[results_start:number_results]:
            try:
                src = img.get_attribute('src')
                if src and 'data:image' in src:
                    print("Found Base64 Image:", src[:100])  # Print the start of the data URI for debugging
                    image_urls.add(src)
                elif src:
                    print("Found URL Image:", src)  # Print URL images
            except Exception as e:
                print(f"Error accessing image src: {e}")
                continue

            image_count = len(image_urls)
            if len(image_urls) >= max_links_to_fetch:
                print(f"Found: {len(image_urls)} image links, done!")
                break
        else:
            print("Found:", len(image_urls), "image links, looking for more ...")
            time.sleep(30)

        results_start = len(thumbnail_results)

    return image_urls

def persist_image(folder_path: str, data: str, counter):
    if data.startswith('data:image'):
        base64_data = data.split(',')[1]
        try:
            image_data = base64.b64decode(base64_data)
            image = Image.open(BytesIO(image_data))
            image_path = os.path.join(folder_path, f'image_{counter}.png')
            image.save(image_path)
            print(f"SUCCESS - saved image {counter} - as {image_path}")
        except Exception as e:
            print(f"ERROR - Could not save image {counter} - {e}")
    else:
        try:
            image_content = requests.get(data).content
            with open(os.path.join(folder_path, f'image_{counter}.jpg'), 'wb') as f:
                f.write(image_content)
            print(f"SUCCESS - saved image {counter} - as {folder_path}")
        except Exception as e:
            print(f"ERROR - Could not download {data} - {e}")

def search_and_download(search_term: str, driver_path: str, target_path='./images', number_images=10):
    target_folder = os.path.join(target_path, '_'.join(search_term.lower().split(' ')))

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    service = Service(driver_path)
    with webdriver.Chrome(service=service) as wd:
        res = fetch_image_urls(search_term, number_images, wd=wd, sleep_between_interactions=0.5)

    counter = 0
    for elem in res:
        persist_image(target_folder, elem, counter)
        counter += 1

# Update the driver path to point to the correct chromedriver.exe location
DRIVER_PATH = r'C:\Users\abres\Downloads\ineuron\image_scrapper\scrapper1\chromedriver.exe'
search_term = 'trump'
search_and_download(search_term=search_term, driver_path=DRIVER_PATH, number_images=50)

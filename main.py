import requests
import time
import threading

# Function to perform Google search and navigate to target URL
def google_search_navigate(search_query, target_url):
    try:
        # Perform the Google search
        params = {'q': search_query}
        response = requests.get('https://www.google.com/search', params=params)
        response.raise_for_status()
        
        # Parse the search results
        search_results = response.text
        # Implement your parsing logic to extract URLs or other relevant data
        
        # Example: Navigate to the target URL directly
        response = requests.get(target_url)
        response.raise_for_status()
        
        # Perform automation tasks or further processing if needed
        # Example: Extract data or perform actions on the target page
        
    except Exception as e:
        print(f"Error performing search and navigation: {e}")

# List of tasks to perform
search_tasks = [
    ("Sanjay Patidar Neemuch", "https://sanjay-patidar.vercel.app/"),
    ("Sanjay Patidar blogs", "https://sanjay-patidar.vercel.app/blogs"),
    ("Contact Sanjay Patidar", "https://sanjay-patidar.vercel.app/contact"),
    ("Sanjay Patidar Resume", "https://sanjay-patidar.vercel.app/resume"),
]

# Number of times to repeat the process
repeat_count = 5

def start_search_task(search_query, target_url):
    for _ in range(repeat_count):
        google_search_navigate(search_query, target_url)
        time.sleep(1)  # Add a small delay between repetitions

# Create and start threads for parallel execution
threads = []
for search_query, target_url in search_tasks:
    thread = threading.Thread(target=start_search_task, args=(search_query, target_url))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

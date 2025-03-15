import requests
import time
import threading

# Define the URL of your FastAPI app (change to your service's URL)
url = "http://0.0.0.0:8000/analyze"

# Function to send GET requests
def send_requests(request_count):
    count = 0
    while count < request_count:
        try:
            response = requests.get(url)
            print(f"Response Code: {response.status_code}, Response Time: {response.elapsed.total_seconds()}s")
            count += 1
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
        time.sleep(0.1)  # Adjust this to control the rate of requests (0.1s = 10 requests/sec)

# Function to simulate load with multiple threads (concurrent requests)
def simulate_traffic(total_requests, thread_count=10):
    # Calculate the number of requests per thread
    requests_per_thread = total_requests // thread_count

    threads = []
    for _ in range(thread_count):
        thread = threading.Thread(target=send_requests, args=(requests_per_thread,))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    total_requests = 10000  # Total number of requests you want to send
    thread_count = 10  # Number of threads (concurrent requests)

    simulate_traffic(total_requests=total_requests, thread_count=thread_count)

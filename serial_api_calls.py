import requests
import time

urls = [
    "https://dummyjson.com/users/1",
    "https://dummyjson.com/users/2",
    "https://dummyjson.com/users/3"
]

start_time = time.time()

for url in urls:
    response = requests.get(url)
    data = response.json()
    print(f"User ID: {data['id']}, Name: {data['firstName']}")

end_time = time.time()

print("Total Time Taken (Serial):", end_time - start_time, "seconds")

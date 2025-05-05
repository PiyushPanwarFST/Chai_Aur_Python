import time

wait_time = 1
max_retries = 5
attemps = 0

while attemps < max_retries:
    attemps += 1
    wait_time *= 2
    print(f"Attempt {attemps}: Waiting for {wait_time} seconds...")
    time.sleep(wait_time)
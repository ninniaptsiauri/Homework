# Number 1

import threading
import json
from faker import Faker
from random import randint

fake = Faker()

num_employees = 5

def generate_employee():
    return {
        "name": fake.name(),
        "age": randint(20, 50),
        "salary": randint(1500, 3000)
    }



def create_and_parse_employee_data(i):
    employee_data = generate_employee()
    file_name = f"employee{i}.json"
    with open(file_name, 'w') as f:
        json.dump(employee_data, f, indent=4)
    with open(file_name, 'r') as f:
        data = json.load(f)
        print(f"File name: {file_name}, Data: {data}")


if __name__ == "__main__":
    threads = []
    for i in range(1, num_employees + 1):
        thread = threading.Thread(target=create_and_parse_employee_data, args=(i,))
        threads.append(thread)
        thread.start()


    for thread in threads:
        thread.join()








# Number 2

from queue import Queue

def queue_threads(task_queue):
    while True:
        task = task_queue.get()
        if task is None:
            break

        thread_name = threading.current_thread().name
        is_even = "even" if task % 2 == 0 else "odd"
        print(f'{thread_name}: processed number {task}, is {is_even}.')

        task_queue.task_done()



task_queue = Queue()

num_workers = 3
threads = []

for i in range(num_workers):
    thread = threading.Thread(target=queue_threads, args=(task_queue,), name=f'Thread{i+1}')
    thread.start()
    threads.append(thread)


tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for task in tasks:
    task_queue.put(task)

task_queue.join()

for _ in range(num_workers):
    task_queue.put(None)

for thread in threads:
    thread.join()


print("All tasks are completed.")

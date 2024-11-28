import time
from datetime import datetime
import asyncio
import random

# Number 1

async def first():
    print('Start First Function')
    await asyncio.sleep(2)
    print('End First Function')


async def second():
    print('Start Second Function')
    await asyncio.sleep(5)
    print('End Second Function')


async def main():
    start_time = datetime.now()
    coroutines = asyncio.gather(first(), second())
    await coroutines
    end_time = datetime.now()
    print(f"Finished in {end_time - start_time}")


if __name__ == "__main__":
    asyncio.run(main())







# Number 2

async def print_numbers(number, delay):
    await asyncio.sleep(delay)
    print(f'Number: {number}')


async def main():
    tasks = []
    for i in range(1, 11):
        delay = random.randint(1, 5)
        tasks.append(print_numbers(i, delay))

    await asyncio.gather(*tasks)        


if __name__ == "__main__":
    start_time = datetime.now()
    asyncio.run(main())
    end_time = datetime.now()
    print(f"Finished in {end_time - start_time}")







# Number 3

async def check_even_number(number):
    await asyncio.sleep(0.5)
    return number % 2 == 0
    

async def square_number(number):
    if await check_even_number(number):
        return number ** 2
    return None


async def main():
    tasks = []
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for number in numbers:
        tasks.append(square_number(number))

    results = await asyncio.gather(*tasks)
    
    for number, result in zip(numbers, results):
        if result is not None:
            print(f'Number: {number}, Square: {result}')

        else:
            print(f'Number {number} is odd.')


if __name__ == "__main__":
    asyncio.run(main())







# Number 4

async def write_to_file(file_name, text):
    print(f"Task for {file_name} started")
    await asyncio.sleep(2)
    with open(file_name, 'w') as file:
        file.write(text)
    print(f"Task for {file_name} finished")


async def main():
    tasks = [
        write_to_file('file1.txt', 'Information for File 1'),
        write_to_file('file2.txt', 'Information for File 2'),
        write_to_file('file3.txt', 'Information for File 3'),
        write_to_file('file4.txt', 'Information for File 4'),
        write_to_file('file5.txt', 'Information for File 5')
    ]

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
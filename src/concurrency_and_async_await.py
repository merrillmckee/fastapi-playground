# since the fastapi website doesn't have a full code example, using external link
#   https://www.pythontutorial.net/python-concurrency/python-async-await/
#   https://www.pythontutorial.net/python-concurrency/python-asyncio-create_task/

import asyncio
import time


async def call_io_bound(message: str, result: int = 1000, delay: int = 3) -> int:
    print(message)
    await asyncio.sleep(delay)
    return result


async def demo_pausing():
    start = time.perf_counter()

    io_value = await call_io_bound('Get IO data', 200, delay=2)
    print(io_value)

    io_value = await call_io_bound('Get IO data', 300, delay=3)
    print(io_value)

    end = time.perf_counter()
    print(f"It took {end - start} seconds to complete")


async def demo_concurrency():
    start = time.perf_counter()

    task_2 = asyncio.create_task(call_io_bound('Get IO data 2', 200, delay=2))
    task_3 = asyncio.create_task(call_io_bound('Get IO data 3', 300, delay=3))
    task_1 = asyncio.create_task(call_io_bound('Get IO data 1', 100, delay=1))

    io_value = await task_2
    print(io_value)

    io_value = await task_3
    print(io_value)

    io_value = await task_1
    print(io_value)

    end = time.perf_counter()
    print(f"It took {end - start} seconds to complete")


if __name__ == "__main__":
    asyncio.run(demo_pausing())  # ~5 seconds
    asyncio.run(demo_concurrency())  # ~3 seconds

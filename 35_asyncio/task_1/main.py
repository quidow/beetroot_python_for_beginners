"""
Practice asynchronous code

Create a separate asynchronous code to calculate Fibonacci, factorial, squares and cubic for an input number.
Schedule the execution of this code using asyncio.gather for a list of integers from 1 to 10.
You need to get four lists of results from corresponding functions.

Rewrite the code to use simple functions to get the same results but using a multiprocessing library.
Time the execution of both realizations, explore the results, what realization is more effective,
why did you get a result like this.
"""
import asyncio
import async_func
import multiprocess_func
import multiprocessing
import time

if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    async_fibonacci = asyncio.gather(*[async_func.fibonacci(i) for i in range(1, 11)])
    async_factorial = asyncio.gather(*[async_func.factorial(i) for i in range(1, 11)])
    async_square = asyncio.gather(*[async_func.square(i) for i in range(1, 11)])
    async_cube = asyncio.gather(*[async_func.cube(i) for i in range(1, 11)])
    async_results = loop.run_until_complete(asyncio.gather(async_fibonacci, async_factorial, async_square, async_cube))
    loop.close()
    print(f"--- {time.time() - start_time} seconds ---")

    start_time = time.time()
    pool = multiprocessing.Pool(processes=3)
    multiprocess_fibonacci = pool.map(multiprocess_func.fibonacci, range(1, 11))
    multiprocess_factorial = pool.map(multiprocess_func.factorial, range(1, 11))
    multiprocess_square = pool.map(multiprocess_func.square, range(1, 11))
    multiprocess_cube = pool.map(multiprocess_func.cube, range(1, 11))
    multiprocess_results = [multiprocess_fibonacci, multiprocess_factorial, multiprocess_square, multiprocess_cube]
    print(f"--- {time.time() - start_time} seconds ---")

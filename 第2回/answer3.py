import answer2
import time

start_time = time.perf_counter()

answer2.fibonacci(500)

end_time = time.perf_counter()

print(end_time - start_time)
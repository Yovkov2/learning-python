import random
import math

throws = [random.randint(1, 6) for _ in range(100)]
average = sum(throws) / len(throws)
print(f"Average throw: {math.floor(average)}")

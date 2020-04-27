import random
from quick_sorting import quick_sorting

if __name__ == "__main__":
    num_array = [random.randint(1, 100) for i in range(10)]
    print(quick_sorting(num_array))

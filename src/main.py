import sys
import time
from lib.example_func import func_under_test

if __name__ == "__main__":
    input = int(sys.argv[1])
    result = func_under_test(input)
    print(result)
    time.sleep(100)

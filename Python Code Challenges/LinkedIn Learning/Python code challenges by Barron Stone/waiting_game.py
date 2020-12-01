import time
import random

def waiting_game():
    target = random.randint(2, 8)
    print("Your target time is {} seconds.".format(target))

    input("--- Press Enter to Begin ---")
    start_time = time.perf_counter()

    input("\n Press Enter again after {} seconds...".format(target))
    elapsed = time.perf_counter() - start_time

    print("Elapsed time: {0:.3f} seconds".format(elapsed))
    if elapsed == target:
        print("Unbelievable! Perfect timing!")
    elif elapsed < target:
        print("{0:.3f} seconds too fast".format(target - elapsed))
    else:
        print("{0:.3f} seconds too slow".format(elapsed - target))


if __name__ == '__main__':
    waiting_game()
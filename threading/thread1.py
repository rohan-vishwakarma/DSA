import time
import threading


def print_numbers():
    for num in range(0, 10):
        print(f"Number: {num}")
        time.sleep(1)


def print_letter():
    for letter in "ABCDE":
        print(f"Letter: {letter}")
        time.sleep(1)


if __name__ == '__main__':
    thread1 = threading.Thread(target=print_numbers, name="print numbers")
    thread2 = threading.Thread(target=print_letter, name="print letters")

    thread1.start()
    thread2.start()

    # Wait briefly for both to become active (adjust delay if needed)
    time.sleep(0.1)

    # Now inspect
    print(f"Active thread count: {threading.active_count()}")
    print("All active threads:")
    for t in threading.enumerate():
        print(f"  - {t.name} (alive: {t.is_alive()})")

    thread1.join()
    thread2.join()

    print("Done!")
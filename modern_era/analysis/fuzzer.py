from time import sleep
import random
import string
import subprocess
import sys
from util.flag.flag_finder import FlagFinder


def random_lowercase_string(length):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))


def fuz(path):
    print(f"Fuzzing...\n")
    iteration = 0
    max_tries = 1000

    while iteration <= max_tries:
        iteration += 1

        process = subprocess.Popen(
            f'"{path}"',
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            text=True,
        )

        while True:

            length = random.randint(0, 128)
            input_str = random_lowercase_string(length) + "\n"

            try:
                process.stdin.write(input_str)
                process.stdin.flush()

                output = process.stdout.read(1024)

                flag = FlagFinder().search_for_flag_in_text(output)

                if flag:
                    print(
                        f"Flag has been found using this input:\n{input_str}\noutput:\n{output}\n{flag}"
                    )
                    sys.exit()

            except subprocess.TimeoutExpired:
                print("Subprocess timed out")
                break
            except Exception as e:
                print(f"Error during fuzzing: {e}")
                break

            sleep(0.001)
            if process.poll() is not None:
                process.terminate()
                break

    print("Flag could not be found using fuzzing")

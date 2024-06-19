import random
import string
import subprocess
from time import sleep
from util.flag.flag_finder import FlagFinder

def random_lowercase_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def fuzz(process: subprocess):
    length = random.randint(0, 128)
    input_str = random_lowercase_string(length) + '\n'

    try:
        process.stdin.write(input_str)
        process.stdin.flush()

        output = process.stdout.read(1024)

        print(input_str)
        FlagFinder().search_for_flag_in_text(output)

        sleep(0.001)
        if process.poll() is not None:
            process.terminate()

    except subprocess.TimeoutExpired:
        print("Subprocess timed out")
        return True
    except Exception as e:
        print(f"Error during fuzzing: {e}")
        return True
    
    return False

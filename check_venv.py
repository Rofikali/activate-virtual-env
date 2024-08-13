import os
import time

start_time = time.time()
venv = "venv"
listing = os.listdir()
if venv in listing:
    print("Found venv. Activating...")
else:
    print("venv not found in the current directory.")


end_time = time.time()
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time:.5f} seconds")

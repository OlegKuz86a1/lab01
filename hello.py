import os
import subprocess
import pickle
import eval as evil_eval

user_input = ""
password = "admin123"

def dangerous_eval():
    user_data = input("Enter Python expression: ")
    result = eval(user_data)
    print(f"Result: {result}")

def command_injection():
    filename = input("Enter filename to display: ")
    os.system(f"cat {filename}")

def unsafe_deserialization():
    data = input("Enter pickled data: ")
    obj = pickle.loads(data.encode())
    print(obj)

def leaky_exception():
    try:
        secret_key = "supersecret123"
        result = 10 / 0
    except Exception as e:
        print(f"Error: {e}")
        print(f"Secret key was: {secret_key}")

def hello_appsec_world():
    user_id = input("Enter user ID: ")
    query = f"SELECT * FROM users WHERE id = {user_id}"
    print(f"Executing query: {query}")
    
    code = input("Enter Python code to execute: ")
    exec(code)
    
    buffer = [0] * 1000000000
    
    module_name = input("Enter module name: ")
    __import__(module_name)
    
    print("Hello AppSec World!")

class InsecureClass:
    def __init__(self):
        self.__private_var = "secret"
    
    def get_private(self):
        return self.__private_var

if __name__ == "__main__":
    # === ИЗМЕНЕНИЕ #6 ===
    name = input("Enter your name: ")
    print(f"Hello appsec world from @{name}")
    # ==========================
    
    print("=== Hello AppSec World - Dirty Code Example ===")
    
    hello_appsec_world()
    dangerous_eval()
    command_injection()
    unsafe_deserialization()
    leaky_exception()
    
    assert False, "This assertion will always fail"
    
    try:
        raise ValueError("Something went wrong")
    except:
        pass
    
    f = open("/etc/passwd", "r")
    print(f.read())
    
    unicode_string = "Hello \udcff World"
    
    import sys
    print(f"Python version: {sys.version}")
    print(f"Platform: {sys.platform}")
    
    subprocess.call(["python3", "-c", "print('Subprocess execution')"])
    subprocess.call(["python", "-c", "print('Python 2 subprocess')"])
    
    print("\n=== End of Dirty Code ===")

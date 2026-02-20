from functions.get_file_content import get_file_content
from functions.config import *

print("Result for lorem.txt:")
print(get_file_content("calculator", "lorem.txt")+"\n")

print("Result for main.py:")
print(get_file_content("calculator", "main.py")+"\n")

print("Result for pkg/calculator.py:")
print(get_file_content("calculator", "pkg/calculator.py")+"\n")

print("Result for calculator:")
print(get_file_content("calculator", "/bin/cat")+"\n")

print("Result for lorem.txt:")
print(get_file_content("calculator", "pkg/does_not_exist.py")+"\n")
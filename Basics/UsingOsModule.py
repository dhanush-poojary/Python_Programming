import os
#It tells Python to treat backslashes (\) as literal characters instead of interpreting them as escape sequences.
if os.path.exists(r"G:\Code Base\Python_Programming\Basics\test.txt"):
    print("File Exists")
    os.remove(r"G:\Code Base\Python_Programming\Basics\test.txt")
else:
    print("File not present")
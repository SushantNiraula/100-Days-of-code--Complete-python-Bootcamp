# file=open('my_file.txt')
# contents=file.read()
# print(contents)
# file.close()

# with open('my_file.txt') as f: ## opening file as read only by default
#     f.write('New-text') ## can't write as file opened as readonly
'''
Traceback (most recent call last):
  File "/Users/sushantniraula/Coding/100 Days of python/24. Day24- Files, Directories, path/open-read-write-file.py", line 7, in <module>
    f.write('New-text') ## can't write as file opened as readonly
    ^^^^^^^^^^^^^^^^^^^
io.UnsupportedOperation: not writable
'''
with open("my_file.txt",mode='a') as f:
    f.write(".\nHow are you?")



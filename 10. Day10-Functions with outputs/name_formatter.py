## Output of a function means that it returns something as output to the place where the function was called.
## Function that formats the inputed name into TitleCase.
def name_format(fname, sname):
    fname=fname.title()
    sname=sname.title()
    return f'{fname} {sname}'

name=input('Enter the name: ')
surname=input('Enter the surname: ')
print(name_format(name,surname))

"""command = input("Enter command:")
while command != "stop":
    if command == "MAY":
        break
    print("executing comment: " + command)
    command = input("Enter command:")
else:
    print("good day")
print("excution stoped")
"""\
#if, elif, else examples
"""language = 'Java'
if language == 'python':
    print('language is python')
elif language == 'Java':
    print('language is Java')
elif language == 'JavaScript':
    print('language is JavaScript')
else:
    print('not match') 
"""
#and
# or
# not
"""user = 'admin'
logged_in = False
if not logged_in:
#if user == 'admin ' and, or logged_in:
    print('please logged in')
else:
    print('welcome')
"""
"""a = [1,2,3,4]
b = a
print(id(a))
print(id(b))
print(a == b)
"""
""" suppliers = ["companyA", "companyB", "CompanyC"]
for x in suppliers:
    print(x)
"""
""" for x in range (5):
    print(x)
"""
"""for x in range (2, 20, 2):
    print(x)
    """
""" for x in range (10):
    if x == 3 : continue
    if x == 7 : break
    print(x)
"""
"""for x in range (5):
    print(x)
else:
    print("no count")
"""
"""count = 1
while count < 6 :
    print(count)
    count = count + 1
"""

def function(x , y):
    return x * y
num = function(1, 5)
print(num)



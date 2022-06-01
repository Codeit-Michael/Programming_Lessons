import test

# def xo(s):
#     x,o = 0,0
#     for i in s:
#         if i == 'x' or i == 'X':
#             x+=1
#         elif i == 'o' or i == 'O':
#             o+=1
#     print(x,o)
#     if x == o:
#         return True
#     else:
#         return False

def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

print(xo('xo'))
print(xo('xo0'))
print(xo('xxxoo'))
print(xo('XXooxxO'))
print(xo('rfdcs'))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def find_short(s):
#     s = [x for x in s.split(' ')]
#     l = len(s[0])
#     for x in s:
#         if len(x) < l:
#             l = len(x)
#     return l

def find_short(s):
    return min(len(x) for x in s.split())

print(find_short('bobo amp'))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def areYouPlayingBanjo(name):
#     if name[0].lower() == 'r':
#             return f'{name} is playing banjo'
#     else:
#         return f'{name} is not playing bajo'

def areYouPlayingBanjo(name):
    return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo"

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
mylist = ['q','w','e','r','t','y',]
print('/'.join(mylist))

mylist = ['q','w','e','r','t','y',]
delimeter = '/'
print(delimeter.join(mylist))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def make_negative(number):
# 	if number > 0:
# 		return number*(-1)
# 	else:
# 		return number

def make_negative(number):
	# abs => return the absolute value
	return -abs(number)

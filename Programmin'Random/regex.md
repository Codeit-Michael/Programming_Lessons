## Regex Module
```
import re
```

`re.search()` - similar to python's `find()` which finds matching string
`re.findall()` - combination of `find()` & slicing: `var[5:10]`
`^` - same as `startswith` 

```
word = re.search("^From", line) # means search trough lines where a line starts with "From"
```

~Dot `.` matches any character
~`*` means any no. of times
~`\s` whitespaces
~`\S` match any non-whitespace char
~`+` one or more times								


### Matching & Extracting Data
`re.search()` - return bool, depends on whether the str matches the regular 
expression
~You can use `re.findall()` to extract matching strs
```
>>> import re
>>> x = "My 2 fav. no. are 19 and 42"
>>> y = re.findall('[0-9]+',x) # '[0-9]+' - 1 char, means 1 or more digits
>>> print(y)
['2','19','42']
```
### Greedy Matching
```
>>> import re
>>> x = "From: Using the : character"
>>> y = re.findall('^F.+:',X)
>>> print(y)
["From: Using the :"]
```
**`'^F.+:'` means**
`^F` - starts with 'F'
`.+` - has one or more any characters
`:` - ends with ':'
`\$` - use to search a dollar sign ($)
**Why `'From: Uisng the :'` instead `'From:'`?**
~It always take the long one always, not the short one (that's why greedy matching)
~To make the `'^F.+:'` above ungreedy, do `'^F.+?:'`

### Fine tuning Extraction
```
>>> import re
>>> x = "my email is ro.bot17@gmail.com"
>>> y = re.findall('\S+@\S+')
>>> print(y)
['ro.bot17@gmail.com']
```
~Parentheses aren't part of the match - they tell where to start n stop what str to extract
```
>>> x = 'my email is ro.bot17@gmail.com mate'
>>> e1 = re.findall('\S+@\S+', x)
>>> e2 = re.findall('^my (\S+@\S+)', x)
```
~`e1` and `e2` has the same output



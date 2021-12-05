import re
s = '@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%'

list = re.findall(r"@\w+\W",s)
print(list)
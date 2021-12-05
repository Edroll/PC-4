import re

s = "Unfortunately one of those moments wasn't a giant squid monster. User_mentions:2, likes: 9, number of retweets: 7"
#Usuarios que sigan el siguiente patron: User_mentions:9
list = re.findall(r"\w+_\w+:\d",s)
print(list)

#encuentre los numero de likes: likes: 5
list1 = re.findall(r"l.{4}:\s\d",s)
print(list1)

#que permita encontrar el numero de retweets. number of retweets: 4
list2 = re.findall(r"n.{17}:\s\d",s)
print(list2)

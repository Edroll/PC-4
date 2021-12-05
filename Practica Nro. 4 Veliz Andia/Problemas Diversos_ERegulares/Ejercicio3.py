import re

s = "AiUlockm.txt es el archivo escondido"
d = "AOUloc_m.txt  es mayor que OoOkdkad_ASda.txt"

list = re.findall(r"^[aeiouAEIOU]{2,3}\S+txt",d)
print(list)
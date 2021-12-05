import re
# Escriba una expresión regular para validar un correo
regex = r"^[456][^[0]{4,}][^[1]{4,}][^[2]{4,}][^[3]{4,}][^[4]{4,}][^[5]{4,}][^[6]{4,}][^[7]{4,}][^[8]{4,}][^[9]{4,}][0-9]{15}"

tarjetas = ['4253625879615786', '5122-2368-7954-3214', '5122-2368-7954 - 3214']
for example in tarjetas:

    if re.match(regex, example):

        print("La tarjeta {tar_example} es valida".format(tar_example=example))
    else:
        print("La tarjeta {tar_example} es invalida".format(tar_example=example)) 
import hashlib, crypt

# $6$GDFm1k/L$cku7JxnqL3SPsnpWivy2DRxhecAw5ZI7gkJoicpcjsabJLfjxtAx0m5W0RZaeLFANHF0hddxbjlL4P7zSxRy80
ctype = "6" #for sha512 (see man crypt)
salt = "GDFm1k/L"
insalt = '${}${}$'.format(ctype, salt)
password = "toor"
value1 = hashlib.sha512(insalt + password).hexdigest() #what's wrong with this one?
value2 = crypt.crypt(password, insalt) #this one is correct on Ubuntu 12.04

print value1
print value2

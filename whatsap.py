import pywhatkit as kit

try :                          
    kit.sendwhatmsg("+905389681812","THT adam gibi adam",13,31)
    print("Gönderme başarılı.")
except :
    print("Beklenmeyen bir hata oluştu.")
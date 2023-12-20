user={'username':'harika','password':'lokesh123'}
username=str(input('enter username'))
password=str(input('enter password'))
if username!=user['username']:
    print('username is invalid')
else:
     print('username is valid')
if password!=user['password']:
    print('password is incorrect')
else:
    print('possword is valid')
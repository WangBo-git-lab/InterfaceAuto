from common import Common
import  time

uri = '/auth/login'
mobile = '15137139921'
password = 'xyz1230.'
xmjz_time = int(time.time())
payload = f'mobile={mobile}&password={password}&xmjz_time={xmjz_time}'
comm = Common('https://appapi-test.jiazhengye.cn')
response_login = comm.post(uri, params=payload)
if response_login.status_code == 200:
    print('Response内容：' + response_login.text)
else:
    print(f'请求失败，状态码：{response_login.status_code}')



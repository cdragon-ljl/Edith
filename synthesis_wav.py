#coding:utf-8

from aip.speech import AipSpeech
import os

APP_ID = '16886339'
API_KEY = 'Ly0TST3N8Y7PA7pLrrou1PZX'
SECRET_KEY = 'O4BphHmbRrwL4K7jBIdHD9cuzVMWAKmg'


aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

#string = '现在温度是{}摄氏度'.format(27.0)
string = '我没听懂，能再说一次吗'

result  = aipSpeech.synthesis(string, 'zh', 1, {
    'vol': 5, 'per': 5,
})


# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('./bgm/disunderstand.mp3', 'wb') as f:
        f.write(result)
    os.system("sudo mpg123 ./bgm/disunderstand.mp3")


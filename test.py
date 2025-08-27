#!/usr/bin/python3
# -*- coding: utf8 -*-
"""
说明: 环境变量`Value_Test`
cron: 20 9 */7 * *
new Env('test');
"""
import os
try:
    from sendNotify import send
except:
    def send(*args):
        print("未找到通知文件sendNotify.py不启用通知！")

# 内置Python环境变量[纯Python环境可启用]
os.environ['Value_Test'] = "NotifyTest"

List = []

if __name__ == '__main__':
    if 'Value_Test' in os.environ:
        print(f'已配置环境变量Value_Test: {os.environ['Value_Test']}')
        List.append(f'已配置环境变量Value_Test：{os.environ['Value_Test']}')
        msg = '\n'.join(List)
        send('NotifyTest', msg)
    else:
        print('未配置环境变量Value_Test')
        send('test', '未配置环境变量Value_Test')

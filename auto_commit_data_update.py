import os
import time
import zoneinfo
import datetime


def get_input():
    """
    返回值: 'YYYY-MM-DD' 格式的字符串（如 '2026-02-02'）
    
    若输入无效，打印错误并退出
    """
    user_input = input('输入日期：').strip()

    try:
        if not user_input:
            # 输入为空 → 使用昨天（按 UTC+8 计算“昨天”）
            print('空输入，自动使用昨天')
            tz = zoneinfo.ZoneInfo("Asia/Shanghai")
            today_utc8 = datetime.datetime.now(tz).date()
            target_date = today_utc8 - datetime.timedelta(days=1)
        else:
            # 解析输入为 YYYY-MM-DD
            target_date = datetime.datetime.strptime(user_input, "%Y-%m-%d").date()
    except ValueError:
        print("❌ 错误：请输入空行或有效日期（格式：2026-02-02）")
        time.sleep(3)
        exit(1)
    return target_date.strftime("%Y-%m-%d")


if __name__ == '__main__':
    date_str = get_input()
    commands = [
        'git add data/',
        f'git commit -m 更新{date_str}数据',
        'git push'
    ]
    print(f"\n\033[33;1m将执行以下命令：\033[m\n\n{'\n'.join(commands)}\n")
    c = input('\033[33;1m确认？(Y/N)\033[m ')
    print()
    if c.lower() == 'y':
        for t in commands:
            print(f'Command: \033[36;1m{t}\033[m')
            ec = os.system(t)
            if ec:
                print(f'\033[31;1m执行命令时遇到错误\033[m')
                if input('\033[33;1m退出？(Y/N)\033[m ').lower() == 'y':
                    exit(1)
        print('\n\033[32;1m执行完成\033[m')
    else:
        print('\033[33;1m操作被取消\033[m')
    time.sleep(3)
    exit()

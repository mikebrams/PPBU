import json
import sys

def check(code, body):

    if code >= 400:
        return f"Ошибка HTTP: код {code}"

    try:
        data = json.loads(body)
    except json.JSONDecodeError:
        return 'Ответ не JSON'

    if not 'status' in data or data['status'] != 'success':
        return 'Сервис сообщил об ошибке'

    if not 'message' in data:
        return 'В ответе нет поля message'

    return f'Готово: {data['message']}'

code = int(input())
body = sys.stdin.read()

print(check(code, body))
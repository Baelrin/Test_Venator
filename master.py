import requests


def check_phone_number(phone_number):
    api_key = "d9b88e7c252c3361e52a351bfc09037d"
    url = f"https://htmlweb.ru/geo/api.php?json&telcod={phone_number}&api_key={api_key}"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return "Ошибка при получении информации."
    message = f"📞 Информация по номеру: {phone_number}\n"
    if "country" in data:
        message += f"Страна: {data['country']['name']}\n"
    if "city" in data:
        message += f"Город: {data['city']}\n"
    if "region" in data:
        message += f"Регион: {data['region']['name']}\n"
    if "district" in data:
        message += f"Округ: {data['region']['okrug']}\n"
    if "timezone" in data:
        message += f"Часовой пояс: {data['timezone']}\n"
    if "operator" in data:
        message += f"Оператор: {data['operator']}\n"
    if "company" in data:
        message += f"ОАО: {data['company']}\n"
    return message


# Тестовый номер
phone_number = "+79626822241"
print(check_phone_number(phone_number))

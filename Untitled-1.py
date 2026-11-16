
import requests
import os

# Этап 1. Разведка

name = input("Введите имя цели: ").strip()
journal_number = int(input("Введите номер по журналу: "))

age = None
gender = None
female_probability = None
posts_count = 0

# Получаем возраст
try:
    response = requests.get(
        "https://api.agify.io",
        params={"name": name},
        timeout=5
    )
    response.raise_for_status()

    age_data = response.json()
    age = age_data.get("age")

except requests.exceptions.RequestException as error:
    print(f"Ошибка получения возраста: {error}")

# Получаем пол

try:
    response = requests.get(
        "https://api.genderize.io",
        params={"name": name},
        timeout=5
    )
    response.raise_for_status()

    gender_data = response.json()

    gender = gender_data.get("gender")
    probability = gender_data.get("probability")

    if gender == "male":
        gender_text = "Мужской"
    elif gender == "female":
        gender_text = "Женский"
    else:
        gender_text = "Не определён"

    if probability is not None:
        probability_text = f"{probability * 100:.2f}%"
    else:
        probability_text = "Нет данных"

except requests.exceptions.RequestException as error:
    gender_text = "Не определён"
    probability_text = "Нет данных"
    print(f"Ошибка получения пола: {error}")

print("\n=== ЭТАП 1. РАЗВЕДКА ===")
print(f"Цель: {name}")
print(f"Вероятный возраст: {age if age is not None else 'Не определён'}")
print(f"Вероятный пол: {gender_text}")
print(f"Вероятность определения: {probability_text}")


# Этап 2. Маскировка

print("\n=== ЭТАП 2. МАСКИРОВКА ===")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) SecretAgentBot/1.0",
    "Accept-Language": "ru-RU,ru;q=0.9"
}

params = {
    "userId": journal_number
}

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        params=params,
        headers=headers,
        timeout=5
    )

    response.raise_for_status()

    posts = response.json()
    posts_count = len(posts)

    print(f"Количество полученных постов: {posts_count}")

    if posts_count > 0:
        print(f"Первый пост: {posts[0]['title']}")
    else:
        print("Посты пользователя не найдены.")

except requests.exceptions.Timeout:
    print("Ошибка: сервер не ответил вовремя.")

except requests.exceptions.HTTPError as error:
    print(f"Ошибка HTTP: {error}")

except requests.exceptions.RequestException as error:
    print(f"Ошибка подключения: {error}")


# Этап 3. Передача данных

print("\n=== ЭТАП 3. ПЕРЕДАЧА ДАННЫХ ===")

report = {
    "name": name,
    "age": age,
    "gender": gender,
    "posts_count": posts_count
}

try:
    response = requests.post(
        "https://httpbin.org/post",
        json=report,
        timeout=5
    )
    response.raise_for_status()

    result = response.json()

    print("Отчёт успешно отправлен!")
    print("Полученный сервером JSON:")
    print(result.get("json"))

except requests.exceptions.RequestException as error:
    print(f"Ошибка отправки отчёта: {error}")


# Этап 4. Загрузка улик

print("\n=== ЭТАП 4. ЗАГРУЗКА УЛИК ===")

try:
    with requests.get(
        "https://picsum.photos/400/300",
        stream=True,
        timeout=10
    ) as response:
        response.raise_for_status()

        with open("evidence.jpg", "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)

    file_size = os.path.getsize("evidence.jpg")

    print("Фотография сохранена: evidence.jpg")
    print(f"Размер файла: {file_size} байт")

except requests.exceptions.RequestException as error:
    print(f"Ошибка скачивания фотографии: {error}")

except OSError as error:
    print(f"Ошибка сохранения файла: {error}")


# Этап 5. Обработка сбоев

print("\n=== ЭТАП 5. ОБРАБОТКА СБОЕВ ===")

# Проверяем ошибку HTTP 404
try:
    response = requests.get(
        "https://httpbin.org/status/404",
        timeout=3
    )
    response.raise_for_status()

except requests.exceptions.HTTPError:
    print("Ошибка HTTP: сервер вернул код 404.")

except requests.exceptions.Timeout:
    print("Ошибка: сервер не ответил вовремя.")

except requests.exceptions.RequestException as error:
    print(f"Ошибка соединения: {error}")


# Проверяем превышение времени ожидания
try:
    response = requests.get(
        "https://httpbin.org/delay/6",
        timeout=3
    )
    response.raise_for_status()

    print("Сервер ответил успешно.")

except requests.exceptions.Timeout:
    print("Превышено время ожидания ответа (3 секунды).")

except requests.exceptions.HTTPError as error:
    print(f"Ошибка HTTP: {error}")

except requests.exceptions.RequestException as error:
    print(f"Ошибка соединения: {error}")


print("\n=== РАБОТА ПРОГРАММЫ ЗАВЕРШЕНА ===")

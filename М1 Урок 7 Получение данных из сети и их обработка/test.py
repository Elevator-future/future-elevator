import requests


URL = "http://futurelevator.sami-znaete-kto.ru:5000"


# Запрос на удаление товара
print("Запрос на удаление товара")
_id = int(input("Введите ID товара: "))


response = requests.delete(URL + "/products/" + str(_id))
if response.status_code == 204:
    print("Товар успешно удален")
else:
    print("Ошибка: ", response.status_code)
    print(response.json())
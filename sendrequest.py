import configuration
import requests
import data


# Создание нового заказа
def new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)


order_track = new_order(data.order_body).json()["track"]


# Получение информации о заказе по треку
def get_info_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK + str(track))
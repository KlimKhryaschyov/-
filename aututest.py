# Хрящёв Клим 15-я кагорта - диплом автоматизция теста
import sendrequest
import data


# 1. Выполнить запрос на создание заказа.
def test_create_order():
    response = sendrequest.new_order(data.order_body)


# 2. Сохранить номер трека заказа.
def test_save_order_track():
    order_track = sendrequest.new_order(data.order_body).json()["track"]
    return order_track


# 3. Выполнить запрос на получения заказа по треку заказа.
def test_take_order_by_orders_track():
    response = sendrequest.get_info_order(sendrequest.order_track)


# Проверить, что код ответа равен 200.
    assert response.status_code == 200
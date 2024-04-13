# Хрящёв Клим 15-я кагорта - диплом автоматизция теста
import sendrequest
import data


# Сохранить номер трека заказа.
def test_save_order_track():
    order_track = sendrequest.new_order(data.order_body).json()["track"]
    return order_track

# Проверить, что код ответа равен 200.
    assert response.status_code == 200

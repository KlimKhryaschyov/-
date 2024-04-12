# Хрящёв Клим 15-я кагорта, дипломный проект. Вторая практическая часть, задание №1

#Нужно проверить, отображается ли созданный заказ в базе данных
#Для этого: вывеcти список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true).

SELECT c.login, COUNT(o.id) AS "deliveryCount"
FROM "Couriers" AS c
LEFT JOIN "Orders" AS o ON c.id = o."courierId"
WHERE o."inDelivery" = true
GROUP BY c.login;

#Нужно убедиться, что в базе данных статусы заказов записываются корректно.
#Для этого: выведи все трекеры заказов и их статусы.
#Если поле finished == true, то вывести статус 2.
#Если поле canсelled == true, то вывести статус -1.
#Если поле inDelivery == true, то вывести статус 1.
#Для остальных случаев вывести 0.

SELECT track,
	CASE
	WHEN finished = true THEN 2
	WHEN cancelled = true THEN -1
	WHEN "inDelivery" = true THEN 1
    ELSE 0 END AS status
FROM "Orders";
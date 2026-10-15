
# 01 Проверка данных
# 1. Создайте папку dronehub и перенесите образец dronehub.json из вводной части. 
# Исходный файл прошлого проекта не перезаписывайте.
# 2. Загрузите JSON и выведите количество дронов и доставок.
import json

with open("dronehub.json", "r", encoding="utf-8") as file:
    data = json.load(file)
        
print(f" Кол-во дронов: {len(data["drones"])}")
print(f" Кол-во доставок: {len(data["deliveries"])}")

# 02 Доставки выбранного статуса
# 1. Напишите filter_status(deliveries, status), возвращающую все доставки заданного статуса.
# 2. Верните новый список, не меняя исходные записи. Для неизвестного статуса верните [].
def filter_status(deliveries, status):
    result = []
    for delivery in deliveries:
        if delivery["status"] == status:
            result.append(delivery)
    return result

# 03 Завершённые доставки от заданной цены
# 1. Напишите completed_from(deliveries, min_price). Выбирайте только done с ценой не меньше min_price.
# 2. Граница включается: доставка с ценой ровно min_price тоже подходит.
def completed_from(deliveries, min_price):
    result = []
    for delivery in deliveries:
        if delivery["status"]  == "done" and delivery["price"] >= min_price:
            result.append(delivery)
    return result

# 04 Доставки без завершения
# 1. Напишите not_completed(deliveries), выбирающую записи ready или cancelled.
# 2. Не включайте done и не меняйте статусы.
def not_completed(deliveries):
    result = []
    for delivery in deliveries:
        if delivery["status"]  == "ready" or delivery["status"] == "cancelled":
            result.append(delivery)
    return result
print(not_completed(data["deliveries"]))
print("="*70)
print(completed_from(data["deliveries"],1500))
print("="*70)
print(filter_status(data["deliveries"],"done"))
# 05 Карточки без лишних полей
# 1. Напишите short_rows(deliveries). Верните новый список словарей только с id и cargo.
# 2. Проверьте функцию на результате completed_from с min_price=1500.
def short_rows(deliveries):
    result = []
    for delivery in deliveries:
# создаем новый словарь с двумя ключами
        short_delivery = {
            "id": delivery["id"],
            "cargo": delivery["cargo"]                 
        }
        result.append(short_delivery)
    return result

filtered_deliveries = completed_from(data["deliveries"],1500)
# передаем отфильтрованный список в функцию short_rows
print("="*70)
print(f"Укороченный словарь: {short_rows(filtered_deliveries)}")

# 06 Два самых дорогих результата
# 1. Напишите top_deliveries(deliveries, limit). Отсортируйте полученный список по цене по убыванию 
# и верните первые limit записей.
# 2. Если limit <= 0, верните []. Если записей меньше limit, верните все. 
# Сначала передайте результат completed_from, а не все доставки.
def top_deliveries(deliveries, limit):
# проводим проверку на наличие записей, если записей нет, то возвращаем пустой список
    if limit <=0:
        return []
# сортируем список по цене по убыванию
    sorted_deliveries = sorted(deliveries, 
                               key=lambda delivery: delivery["price"], 
                               reverse = True)
# возвращаем весь отсортированный список 
    return sorted_deliveries[:limit]
filtered_deliveries = completed_from(data["deliveries"],1500)
# передаем отфильтрованные доставки от min_price в функцию и определяем топ 2 доставок
top_two = top_deliveries(filtered_deliveries,limit=2)
print("="*70)
print(f"Топ доставок: {top_two}")

# 07 Итог завершённых доставок
# 1. Напишите delivery_summary(deliveries). Верните словарь count и total только по done.
# 2. Для пустого списка оба значения должны быть нулевыми.
def delivery_summary(deliveries):
    count = 0
    total = 0
    for delivery in deliveries:
        if delivery["status"] == "done":
            count += 1
            total += delivery["price"]
    return {"count":count, "total":total}
print("="*70)
print(f"Сумма всего доставок: {delivery_summary(data["deliveries"])}")
filtered_deliveries = completed_from(data["deliveries"],1500)
print(f"Сумма отсортированных доставок: {delivery_summary(filtered_deliveries)}")

# 08 Полезный отчёт
# 1. Напишите export_top_completed(data, min_price, limit), 
# используя completed_from и top_deliveries из предыдущих заданий.
# 2. Запишите выбранные названия грузов и цены в top_completed.txt. 
# Если выборка пуста, сохраните только заголовок. Верните количество строк доставок.
# 3. Запустите с min_price=1500 и limit=2. Обновите README и отправьте работу в Git без веток.
def export_top_completed(data, min_price, limit):
    completed = completed_from(data["deliveries"],min_price)
    top_items = top_deliveries(completed, limit=limit)
    lines = ["Название груза | Цена\n"]
    for delivery in top_items:
        lines.append (f"{delivery['cargo']} | {delivery['price']}\n")

    with open("top_completed.txt", "w", encoding="utf-8") as file:
        file.writelines(lines)

    return len(top_items)  
 
result = export_top_completed(data, min_price=1500, limit=2)
print("="*70)
print(f"Количество топ доставок: {result}")
import certifi
from pymongo.mongo_client import MongoClient
from pymongo.errors import ConnectionFailure

# Підключення до MongoDB
uri = "mongodb+srv://user:user1@cluster0.gadv49o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    client = MongoClient(uri, tlsCAFile=certifi.where())
    print("Підключення до MongoDB вдале")
except ConnectionFailure as e:
    print("Не вдалося підключитися до MongoDB:", e)

# Вибір бази даних
db = client['cats_database']

# Вибір колекції (аналог таблиці у SQL)
cats_collection = db['cats']


def read_all_cats():
    try:
        # Виведення всіх записів із колекції
        return cats_collection.find()
    except Exception as e:
        print("Під час зчитування сталася помилка:", e)


def read_cat_by_name(name):
    try:
        # Пошук кота за ім'ям та виведення інформації про нього
        return cats_collection.find_one({"name": name})
    except Exception as e:
        print("Під час читання кота за ім'ям сталася помилка:", e)


def update_cat_age(name, new_age):
    try:
        # Оновлення віку кота за ім'ям
        cats_collection.update_one({"name": name}, {"$set": {"age": new_age}})
        print("Вік оновлено.")
    except Exception as e:
        print("Під час оновлення віку кота сталася помилка:", e)


def add_feature_to_cat(name, feature):
    try:
        # Додавання нової характеристики до списку features кота за ім'ям
        cats_collection.update_one({"name": name}, {"$push": {"features": feature}})
        print("Характеристика додана.")
    except Exception as e:
        print("Під час додавання характеристики до кота сталася помилка:", e)


def delete_cat_by_name(name):
    try:
        # Видалення запису з колекції за ім'ям тварини
        cats_collection.delete_one({"name": name})
        print("Кота видалено.")
    except Exception as e:
        print("Під час видалення всіх котів сталася помилка:", e)


def delete_all_cats():
    try:
        # Видалення всіх записів із колекції
        cats_collection.delete_many({})
        print("Всіх котів видалено.")
    except Exception as e:
        print("Під час видалення кота за ім'ям сталася помилка:", e)


if __name__ == "__main__":
    # Додавання документу про кота до колекції
    cat_document = {
        "name": "barsik",
        "age": 3,
        "features": ["ходить в капці", "дає себе гладити", "рудий"]
    }
    try:
        cats_collection.insert_one(cat_document)
    except Exception as e:
        print("Під час додавання документа про кота сталася помилка:", e)

    # Виведення всіх котів
    print("Всі коти:")
    for cat in read_all_cats():
        print(cat)

    # Пошук кота за ім'ям та виведення інформації про нього
    cat_name = input("Введіть імя кота: ")
    print("Інформація про кота:")
    print(read_cat_by_name(cat_name))

    # Оновлення віку кота за ім'ям
    cat_name = input("Введіть імя кота для оновлення його віку: ")
    new_age = int(input("Введіть новий вік кота: "))
    update_cat_age(cat_name, new_age)

    # Додавання нової характеристики до списку features кота за ім'ям
    cat_name = input("Введіть імя кота для добавлення нової характеристики: ")
    feature = input("Введіть нову характеристику: ")
    add_feature_to_cat(cat_name, feature)

    # Видалення запису з колекції за ім'ям тварини
    cat_name = input("Введіть імя кота для видалення: ")
    delete_cat_by_name(cat_name)

    # Видалення всіх записів із колекції
    delete_all_cats()
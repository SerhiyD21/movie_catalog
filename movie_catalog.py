import pymongo

# Підключення до сервера MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Створення бази даних
db = client["movie_catalog"]

# Створення колекції
movies_collection = db["movies"]

# Функція для додавання нового фільму
def add_movie(title, director, year, reviews=[]):
    movie = {
        "title": title,
        "director": director,
        "year": year,
        "reviews": reviews
    }
    result = movies_collection.insert_one(movie)
    print(f"Фільм '{title}' додано з ID: {result.inserted_id}")

# Функція для зчитування всіх фільмів
def get_all_movies():
    movies = movies_collection.find()
    for movie in movies:
        print(movie)

# Функція для оновлення інформації про фільм
def update_movie(title, new_data):
    query = {"title": title}
    update = {"$set": new_data}
    result = movies_collection.update_one(query, update)
    if result.modified_count > 0:
        print(f"Фільм '{title}' оновлено.")
    else:
        print(f"Фільм '{title}' не знайдено або дані не змінено.")

# Функція для додавання відгуку до фільму
def add_review(title, review):
    query = {"title": title}
    update = {"$push": {"reviews": review}}
    result = movies_collection.update_one(query, update)
    if result.modified_count > 0:
        print(f"Відгук додано до фільму '{title}'.")
    else:
        print(f"Фільм '{title}' не знайдено.")

# Функція для видалення фільму
def delete_movie(title):
    query = {"title": title}
    result = movies_collection.delete_one(query)
    if result.deleted_count > 0:
        print(f"Фільм '{title}' видалено.")
    else:
        print(f"Фільм '{title}' не знайдено.")

# Демонстрація роботи
if __name__ == "__main__":
    # Додавання фільмів
    add_movie("Inception", "Christopher Nolan", 2010, ["Чудовий фільм!", "Справжній шедевр."])
    add_movie("The Matrix", "Wachowskis", 1999)

    # Зчитування всіх фільмів
    print("\nУсі фільми:")
    get_all_movies()

    # Оновлення року виходу фільму
    update_movie("The Matrix", {"year": 2000})

    # Додавання відгуку
    add_review("Inception", "Дуже сподобався сюжет!")

    # Видалення фільму
    delete_movie("The Matrix")

    # Зчитування після змін
    print("\nФільми після змін:")
    get_all_movies()

# Закриття підключення
client.close()

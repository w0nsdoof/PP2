# Функций

def imdb55(movie_name:str): # Больше ли рейтинг названного фильма 5.5
    for d in movies:
        if d["name"] == movie_name :
            if d["imdb"] > 5.5:
                return True
            return False

    return "Incorrect input" 

def list_imdb55(): # list фильмов с рейтингом > 5.5
    result = []
    for d in movies:
        if d["imdb"] > 5.5:
            result.append(d["name"])

    return result

def by_category(user:str): # Выводить фильмы с категорией заданной пользователем
    result = []

    for d in movies:
        if d["category"] == user:
            result.append(d["name"])

    if len(result) != 0:
        return result
    else:
        return "Incorrect input"

def avg_imdb(user:list): # Среднее значение рейтинга по данному листу фильмов
    result = 0
    for d in movies:
        if d["name"] in user:
            result += d["imdb"]
    
    return (result / len(user))

def avg_by_category(user:str): # Среднее значение рейтинга по категорий
    result = 0
    amount = 0

    for d in movies:
        if d["category"] == user:
            result += d["imdb"]
            amount += 1

    return (result / amount)
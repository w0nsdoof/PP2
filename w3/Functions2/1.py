# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

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



             


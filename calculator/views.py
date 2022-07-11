from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def person_calc(request):
    dish_name = request.GET.get('dish_name')
    if dish_name in DATA:
        recipe = DATA[dish_name]
        persons_count = int(request.GET.get('persons_count'))
        if not persons_count:
            persons_count = 1
        if persons_count > 1:
            for ingredient in recipe:
                correct_amount = recipe[ingredient] * persons_count
                recipe.update({ingredient: correct_amount})
        context = {
            'recipe': recipe
            }
        return render(request, 'calculator/index.html', context)
    else:
        return HttpResponse('Что-то напутали')

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

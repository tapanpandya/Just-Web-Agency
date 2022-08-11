import json

movies_data = json.loads(open('data.json').read())

def get_actor_names(data):
    stars = []
    for item in data:
        for i in item['stars'].split(','):
            if i.strip(' ') not in stars:
                stars.append(i.strip(' '))
    return stars

def get_star_movies_count(data, star_name):
    count = 0
    for item in data:
        if star_name in item['stars']:
            count += 1
    return count

def get_avg_rating(data, star_name):
    rating = 0
    for item in data:
        if star_name in item['stars']:
            rating += float(item['rating'])
    return rating / get_star_movies_count(data, star_name)

def print_table(data):
    stars = get_actor_names(data)
    new_list = []
    for star in stars:
        if get_star_movies_count(data, star) >= 2:
            new_list.append([star, get_star_movies_count(data, star), get_avg_rating(data, star)])
    new_list.sort(key=lambda x: x[1])
    for i in new_list:
        print('Star Name: {:>15} \t | Movies: {:<10} \t | Avg. Rating: {:.2f}'.format(i[0], i[1], i[2]))

print_table(movies_data)

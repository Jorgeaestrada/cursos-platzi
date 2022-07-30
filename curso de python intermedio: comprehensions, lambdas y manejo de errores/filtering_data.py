DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

'''list comprehension approach'''


def list_comprehension():
    all_python_devs = [worker['name']
                       for worker in DATA if worker['language'] == 'python']
    # print(all_python_devs)

    all_platzi_workers = [worker['name']
                          for worker in DATA if worker['organization'] == 'Platzi']
    # print(all_platzi_workers)


'''filter, map, reduce approach'''


def filter_map_reduce():
    # filter +18 workers
    adults = list(filter(lambda x: x['age'] > 18, DATA))
    # print(adults)

    # filter +18 name worker
    adults = list(map(lambda x: x['name'], adults))
    # print(legal_age_workers)

    # filter +70 worker and add both dicts
    old_people = list(map(lambda worker: worker | {
                      "old": worker["age"] > 70}, DATA))
    # print(old_people)


'''challenge'''


def challenge():
    # filter names of workers that knows python
    all_python_devs = list(filter(lambda x: x['language'] == 'python', DATA))
    # print(python_workers)

    # filter names of workers that works in platzi
    all_platzi_workers = list(
        filter(lambda x: x['organization'] == 'Platzi', DATA))
    # print(all_platzi_workers)

    # filter +18 workers by list comprehension
    adults = [worker['name'] for worker in DATA if worker['age'] > 18]
    print(adults)

    old_people = [worker['name'] for worker in DATA if worker['age'] > 70]
    print(old_people)



if __name__ == '__main__':
    list_comprehension()
    filter_map_reduce()
    challenge()

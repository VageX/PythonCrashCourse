favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

should_poll = ['george', 'lauren', 'jen', 'biscuit', 'edward']

for person in should_poll:
    if person in favorite_languages.keys():
        print("\n" + person.title() + ", thank you for responding.")
    else:
        print("\n" + person.title() + ", please take the poll.")
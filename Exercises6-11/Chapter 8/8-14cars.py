def car(manufacturer, model, **other_info):
    """Store information about a car in a dictionary."""
    profile = {}
    profile['make'] = manufacturer
    profile['model'] = model
    for key, value in other_info.items():
        profile[key] = value
    return profile

car_one = car('mazda', '3',
              color='black',
              tech_package=True)

print(car_one)
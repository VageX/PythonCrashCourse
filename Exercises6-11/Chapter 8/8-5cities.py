def describe_city(city, country='usa'):
    """Print a simple sentence including the city and its country."""
    if country == 'usa':
        print("\n" + city.title() + " is in " + country.upper() + ".")
    else:
        print("\n" + city.title() + " is in " + country.title() + ".")

describe_city(city='dallas')
describe_city(city='new york')
describe_city(city='hong kong', country='china')
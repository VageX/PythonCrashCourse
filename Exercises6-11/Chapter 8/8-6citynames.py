def city_country(city, country):
    """Return a string formatted as city, country."""
    formatted = city + ', ' + country
    return formatted.title()

location = city_country('dallas', 'united states')
print(location)

location = city_country('tokyo', 'japan')
print(location)

location = city_country('london', 'united kingdom')
print(location)




def location(city, country, population=''):
    if population:
        formatted_location = city + ", " + country + " - population=" + population + "."
        return formatted_location.title()
    else:
        formatted_location = city + ", " + country
        return formatted_location.title()

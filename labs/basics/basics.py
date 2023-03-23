KM_PER_MILE = 1.609344
MILES_PER_KM = 0.62137119


def celsius_to_fahrenheit(celsius):
    '''
    Converts the given degrees in celsius to fahrenheit.

    The formula is: f = c * (9 / 5) + 32
    '''
    return (celsius * (9 / 5)) + 32


def fahrenheit_to_celsius(fahrenheit):
    '''
    Converts the given degrees in fahrenheit to celsius.

    The formula is: c = (f - 32) * 5 / 9
    '''
    return (fahrenheit - 32) * 5 / 9


def miles_to_kilometers(miles):
    return miles * KM_PER_MILE


def kilometers_to_miles(kilometers):
    return kilometers * MILES_PER_KM

def greet(country):
    greets = {'USA': 'Hello', 'France': 'Bonjour', 'Spain': 'Hola', 'Germany': 'Hallo', 'Italy': 'Ciao'}
    return greets[country]

#return greetings based on language
print(greet('USA'))
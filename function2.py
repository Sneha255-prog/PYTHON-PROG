def greet(lang):
    if lang=='es':
        return('hello')
    elif lang=='so':
        return('holla')
    else:
        return('Bonjour')

greet('so')  #it has passed parameters
print(greet('so'),"sneha")  #it has return values and also passed parameters
print(greet('es'),"sneha")
print(greet('sn'),"joyel")

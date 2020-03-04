PASSWORD = '123456'

def password_required(func):
    def wrapper():
        password = input('Cual es tu contraseña? ')

        if password == PASSWORD:
            return func()
        else:
            print('La contraseña es correcta')
    
    return wrapper

# Func es la funcion a la cual se le esta aplicando el decorador
def upper(func):
    def wrapper(*arg, **kwargs):
        # Obtenemos los parametros posicionales
        result = func(*arg, **kwargs)

        print(result)
        
        return result.upper()
    
    return wrapper


@upper
def say_my_name(name):
    
    return 'Hola {}'.format(name)


# Los decoradores nos permiten ejecutar logica antes y despues de la funcion
# Puede servir para determinar si el usuario tiene acceso a esa funcion o no
@password_required
def needs_password():
    print('La contraseña es correct')

if __name__ == "__main__":
    print(say_my_name('DAvid'))
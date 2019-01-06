class Animal :
    __name = None
    __height = 0
    __weight = 0
    __sound = 0

    def __init__(self, name, height, width, sound) :
        self.__name = name
        self.__height = height
        self.__width = width
        self.__sound = sound

    def set_name(self, name) :
        self.__name = name

    def get_name(self) :
        return self.__name

    def get_type(self) :
        print('Animal')

cat = Animal('Whiskers', 33, 10, 'Meow')
print(cat.get_name())
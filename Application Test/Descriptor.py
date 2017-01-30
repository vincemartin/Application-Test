
class Property: # Pattern Descriptor

   def __init__(self, initvalue):
      print("appel __init__ initvalue[{}]".format(initvalue))
      self._value = initvalue

   def __get__(self, instance, owner = None):
      print("appel __get__")
      return self._value 

   def __set__(self, instance, value):
       print("appel __set__ value[{}]".format(value))
       self._value = float(value)

   def __delete__(self, instance):
       print("appel __delete__")
       pass

class ContainerClass(object):
    attribut3 = Property(3) # property de class ContainerClass (static)


if (__name__ == "__main__"):

    c = ContainerClass()
    print ("ContainerClass.attribut3 = {}".format(c.attribut3))
    c.attribut3 = 4
    print ("ContainerClass.attribut3 = {}".format(c.attribut3))

class Celsius:
    def __get__(self, instance, owner):
        fahrenheit = instance._fahrenheit
        celcius = 9 * (fahrenheit + 32) / 5.0
        print("appel __get__ value[{} fahrenheit -> {} celcius]".format(fahrenheit, celcius))
        return celcius

    def __set__(self, instance, value):         
        celcius =value
        fahrenheit = 32 + 5 * celcius / 9.0
        print("appel __set__ value[{} celcius -> {} fahrenheit]".format(celcius, fahrenheit))
        instance._fahrenheit = fahrenheit

class Temperature:
    def __init__(self, initial_f): 
        self._fahrenheit = initial_f

    _celsius = Celsius()

if __name__ == "__main__":

    t = Temperature(212)
    print("Fahrenheit : {}".format(t._fahrenheit))
    print("Celsius : {}".format(t._celsius))
    t._celsius = 0
    print("Fahrenheit : {}".format(t._fahrenheit))

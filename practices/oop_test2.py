# Propiedades,metodos y eventos

class Vehiculo: 
    def __init__(self, marca, ruedas = 0):
        # marca y ruedas son propiedades

        self.marca = marca  
        self.ruedas = ruedas 

    # Metodos
    def arreglar_ruedas(self):
        self.ruedas = 4

    # Simulación de un evento (conceptual,ESTO NO ES UN EVENTO EN PYTHON)
    def pincho_rueda(self):
        if self.ruedas > 0:
            self.ruedas -= 1
        else:
            print("No se pudo haber pinchado ninguna rueda porque no había ninguna sana")

# Crear una clase Auto que se extienda/herede de la clase Vehiculo

class Auto(Vehiculo):

    def marca(self):
        print("Rolls Royce")

    def default_ruedas(self):
        self.ruedas = 4

    def get_descripcion(self):
        print("Soy un vehiculo del tipo", type(self).__name__)

    def stereo(self):
        print("SonyG32-A5")





















import pdb; pdb.set_trace()

'''
#vehiculo1 = Vehiculo("rollsroyce",4)
 #vehiculo1.marca
#'rollsroyce'
 #vehiculo1.ruedas
#4
 #vehiculo1.pincho_rueda()
 #vehiculo1.pincho_rueda
#<bound method Vehiculo.pincho_rueda of <__main__.Vehiculo object at 0x000001687AA43010>>
#vehiculo1.ruedas
#3
#vehiculo1.pincho_rueda
#<bound method Vehiculo.pincho_rueda of <__main__.Vehiculo object at 0x000001687AA43010>>
 #vehiculo1.pincho_rueda()
 #vehiculo1.ruedas
#2
#vehiculo1.arreglar_ruedas()
#vehiculo1.ruedas
#4
'''

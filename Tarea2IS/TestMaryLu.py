'''
Created on 21/4/2015

@author: MaryLu
'''
import unittest
from calcularPrecio import calcularPrecio,Tarifa
from decimal import Decimal
from datetime import timedelta,datetime

class TestCalcularPrecio(unittest.TestCase):

#--------------------------a)Tiempo reservable--------------------------------------
    
    #Caso de prueba Normal con un dia del fin de la semana
    #Entrada:    Tiempo de reservacion en horas: 24
    #            Tasa en bolivares de la hora: 100,200
    #Salida Esperada:    4800.00 bolivares
    #Solucion: Satisfactorio, ya que da la respuesta correcta.
    
    def testNormalFinSemana(self):
        tarifa1 = Tarifa(100,200)
        tiempoDeReservacionr1 = [datetime(2015,4,18,23,4), datetime(2015,4,19,23,4)]
        self.assertEqual(calcularPrecio(tarifa1, tiempoDeReservacionr1), 4800.00)
    
    #Caso de prueba con el borde inferior
    #Descripcion:    trata de evaluar una de las
    #fronteras cuando la reserva es de 15 minutos
    #Entrada:    Tiempo de reservacion en minutos: 15 
    #            Tasa en bolivares de la hora: 100,200
    #Salida Esperada    200.00 bolivares
    #Solucion: Insatisfactorio ya que no da la respuesta correcta.
    
    #Nota: en el enunciado se plantea que la tasa "Se cobra
    #a hora completa, de modo que por una reservacion de una
    #hora y un minuto se cobra el equivalente a dos horas de
    #uso.",de modo que si se reserva 15 minutos deberia cobrar
    #la hora completa de 200.00 bolivares.
          
    def testBordeInferiorFinSemana(self):
        tarifa1 = Tarifa(100,200)
        tiempoDeReservacionr1 = [datetime(2015,4,18,13,4), datetime(2015,4,18,13,19)]
        self.assertEqual(calcularPrecio(tarifa1, tiempoDeReservacionr1), 200.00)
        
    #Caso de prueba con el borde superior
    #Descripcion:    trata de evaluar una de las
    #fronteras cuando la reserva es de 7 dias
    #Entrada:    Tiempo de reservacion en horas: 24*7 = 168  
    #            Tasa en bolivares de la hora: 100,200
    #Salida Esperada    (2400.00*5)+(4800.00*2) = 21600.00 bolivares
    #Solucion: Satisfactorio, ya que da la respuesta correcta.

    def testBordeSuperiorFinSemana(self):
        tarifa1 = Tarifa(100,200)
        tiempoDeReservacionr1 = [datetime(2015,4,18,13,4), datetime(2015,4,25,13,4)]
        self.assertEqual(calcularPrecio(tarifa1, tiempoDeReservacionr1), 21600.00)

    #Caso de prueba cuabdo se reserva una hora de un dia de semana y una del fin de semana.
    #Descripcion:    trata de evaluar una de las fronteras cuando la reserva es de 1 hora
    #en un dia de semana y 1 hora del fin de semana.
    #Entrada:    Tiempo de reservacion en horas: 2 
    #            Tasa en bolivares de la hora: 100,200
    #Salida Esperada    300.00 bolivares
    #Solucion: Satisfactorio, ya que da la respuesta correcta.
          
    def testDiaSemanaAFin(self):
        tarifa1 = Tarifa(100,200)
        tiempoDeReservacionr1 = [datetime(2015,4,17,23,0), datetime(2015,4,17,23,0) + timedelta(hours = 2)]
        self.assertEqual(calcularPrecio(tarifa1, tiempoDeReservacionr1), 300.00)
                        
    #Caso de prueba con Tarifa cero en un dia de fin de semana
    #Descripcion:    trata de evaluar si la funcion trabaja
    #correctamente si la tarifa por hora es cero.
    #Entrada:    Tiempo de reservacion en horas: 24
    #            Tasa en bolivares de la hora: 0
    #Salida Esperada:    0 bolivares
    #Solucion: Satisfactorio, ya que da la respuesta correcta.
    
    def testTarifaCeroFinSemana(self):
        tarifa1 = Tarifa(0,0)
        tiempoDeReservacionr1 = [datetime(2015,4,18,23,4), datetime(2015,4,19,23,4)]
        self.assertEqual(calcularPrecio(tarifa1, tiempoDeReservacionr1), 0)
    
    #Caso de prueba con Tarifa de un centimo en un dia de fin de semana
    #Descripcion:    trata de evaluar si la funcion trabaja correctamente
    #si la tarifa por hora es representada en centimos.
    #Entrada:    Tiempo de reservacion en horas: 24
    #            Tasa en bolivares de la hora: 100,0.01
    #Salida Esperada:    0.24 bolivares
    #Solucion: Satisfactorio, ya que da la respuesta correcta.
    
    #Nota: Se tuvo que expresar la respuesta de forma que concordara a la salida
    #en decimal de la funcion debido a problemas de tipos de elementos en el lenguaje.
       
    def testTarifaCentimoDiaSemana(self):
        tarifa1 = Tarifa(100,0.01)
        tiempoDeReservacionr1 = [datetime(2015,4,18,23,4), datetime(2015,4,19,23,4)]
        self.assertEqual(calcularPrecio(tarifa1, tiempoDeReservacionr1), Decimal(0.24).quantize(Decimal('1.00')))
        
#--------------------------b)Tiempo No reservable-----------------------------------

    #Caso de prueba con el borde inferior
    #Descripcion:    trata de evaluar una de las
    #fronteras cuando la reserva es de 14 minutos
    #Entrada:    Tiempo de reservacion en minutos: 15 
    #            Tasa en bolivares de la hora: 100,200
    #Salida Esperada:    Error sobre menos de 15 minutos
    #Solucion: Satisfactorio, ya que da la respuesta correcta.
          
    def testBordeInferiorFinSemanaNR(self):
        tarifa1 = Tarifa(100,200)
        tiempoDeReservacionr1 = [datetime(2015,4,18,13,4), datetime(2015,4,18,13,14)]
        self.assertRaises(Exception,calcularPrecio,tarifa1,tiempoDeReservacionr1)
        
    #Caso de prueba con el borde superior
    #Descripcion:    trata de evaluar una de las
    #fronteras cuando la reserva es de 7 dias y 1 minuto
    #Entrada:    Tiempo de reservacion en horas: 24*7 + 1 = 169  
    #            Tasa en bolivares de la hora: 100,200
    #Salida Esperada:    Error sobre mas de 7 dias
    #Solucion: Satisfactorio, ya que da la respuesta correcta.

    def testBordeSuperiorFinSemanaNR(self):
        tarifa1 = Tarifa(100,200)
        tiempoDeReservacionr1 = [datetime(2015,4,11,13,4), datetime(2015,4,18,13,5)]
        self.assertRaises(Exception,calcularPrecio,tarifa1,tiempoDeReservacionr1) 


    #Caso de prueba con tarifa negativa en un dia de fin de semana
    #Descripcion:    trata de evaluar si la funcion trabaja correctamente
    #si la tarifa por hora es representada en numeros negativos.
    #Entrada:    Tiempo de reservacion en horas: 24
    #            Tasa en bolivares de la hora: 100,-200
    #Salida Esperada:    Excepcion de tarifas negativas
    #Solucion: Satisfactorio, ya que da la respuesta correcta.
    
    def testTarifaNegativaFinSemana(self):
        tarifa1 = Tarifa(100,-200)
        tiempoDeReservacionr1 = [datetime(2015,4,25,23,4), datetime(2015,4,26,23,4)]
        self.assertRaises(Exception,calcularPrecio,tarifa1,tiempoDeReservacionr1)    
                       
#--------------------------c)Esquina y Malicia---------------------------------------

    #Caso de prueba con Caracteres especiales en la tarifa en un dia de fin de semana
    #Descripcion:    trata de evaluar si la funcion trabaja correctamente
    #si la tarifa por hora es representada en caracter especial.
    #Entrada:    Tiempo de reservacion en horas: 24
    #            Tasa en bolivares de la hora: Caracter especial
    #Salida Esperada:    Excepcion de caracter especial
    #Solucion: Insatisfactorio ya que no se captura la excepcion en la funcion.
    
    def testTarifaCaracterFinSemana(self):
        tarifa1 = Tarifa('!','$')
        tiempoDeReservacionr1 = [datetime(2015,4,25,23,4), datetime(2015,4,26,23,4)]
        self.assertRaises(TypeError,calcularPrecio,tarifa1,tiempoDeReservacionr1)
    
    #Caso de prueba con String en la lista de tiempo de reservacion
    #Descripcion:    trata de evaluar si la funcion trabaja correctamente
    #cuando los datos de la resrva son String y no fechas.
    #Entrada:    Tiempo de reservacion en horas: Numeros enteros cualquiera
    #            Tasa en bolivares de la hora: 100,200
    #Salida Esperada:    Excepcion de error de tipo
    #Solucion: Insatisfactorio ya que no se captura la excepcion en la funcion.
    
    def testReservaString(self):
        tarifa1 = Tarifa(100,200)
        tiempoDeReservacionr1 = ["Hola","ALO"]
        self.assertRaises(TypeError,calcularPrecio,tarifa1,tiempoDeReservacionr1)

    #Caso de prueba con tarifas de decimales
    #Descripcion:    trata de evaluar si la funcion trabaja correctamente
    #si la tarifa por hora es representada en decimales.
    #Entrada:    Tiempo de reservacion en horas: 24
    #            Tasa en bolivares de la hora: 100,0.0001
    #Salida Esperada:    Excepcion
    #Solucion: Insatisfactorio ya que no se captura la excepcion en la funcion.
    
    #Nota: se esperaba que diese una excepcion ya que en el enunciado se plantea:
    #"Las tasas por hora se introducen en bolivares y centimos y no pueden ser negativas."
    #y se esta usando una tasa en la tarifa que es mucho menor que un centimo.
    
    def testTarifaDecimalesFinSemana(self):
        tarifa1 = Tarifa(100,0.0001)
        tiempoDeReservacionr1 = [datetime(2015,4,18,23,4), datetime(2015,4,19,23,4)]
        self.assertRaises(Exception,calcularPrecio,tarifa1,tiempoDeReservacionr1)
    
    #Caso de prueba con rangos de fechas invertidas de fin de semana
    #Descripcion:    trata de evaluar si la funcion trabaja correctamente
    #cuando se invierte el orden de las fechas.
    #Entrada:    Tiempo de reservacion en horas: 24
    #            Tasa en bolivares de la hora: 100,200
    #Salida Esperada:    Excepcion
    #Solucion: Insatisfactorio ya que no se captura la excepcion en la funcion.        

    def testInvertirOrdenReserva(self):
        tarifa1 = Tarifa(100,200)
        tiempoDeReservacionr1 = [datetime(2015,4,19,23,4), datetime(2015,4,18,23,4)]
        self.assertRaises(Exception, calcularPrecio,tarifa1, tiempoDeReservacionr1)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testcalcularPrecio']
    unittest.main()

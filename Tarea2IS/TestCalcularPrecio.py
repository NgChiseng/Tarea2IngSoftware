'''
Created on 21/4/2015

@author: NgChiseng
'''
import unittest
from calcularPrecio import calcularPrecio,Tarifa
from decimal import Decimal
from datetime import timedelta,datetime

class TestCalcularPrecio(unittest.TestCase):

#--------------------------a)Tiempo reservable--------------------------------------
    
    #Caso de prueba Normal con un dia de la semana
    #Entrada:    Tiempo de reservacion en horas: 24
    #            Tasa en bolivares de la hora: 100
    #Salida Esperada:    2400.00 bolivares
    #Solucion: Satisfactorio, ya que da la respuesta correcta.
    
    def testNormalDiaSemana(self):
        tarifa1 = Tarifa(100,200)
        tiempoDeReservacionr1 = [datetime(2015,4,20,23,4), datetime(2015,4,21,23,4)]
        self.assertEqual(calcularPrecio(tarifa1, tiempoDeReservacionr1), 2400.00)
    
    #Caso de prueba con el borde inferior
    #Descripcion:    trata de evaluar una de las
    #fronteras cuando la reserva es de 15 minutos
    #Entrada:    Tiempo de reservacion en minutos: 15 
    #            Tasa en bolivares de la hora: 100
    #Salida Esperada    100.00 bolivares
    #Solucion: Insatisfactorio ya que no da la respuesta correcta.
    
    #Nota: en el enunciado se plantea que la tasa "Se cobra
    #a hora completa, de modo que por una reservacion de una
    #hora y un minuto se cobra el equivalente a dos horas de
    #uso.",de modo que si se reserva 15 minutos deberia cobrar
    #la hora completa de 100.00 bolivares.
          
    def testBordeInferiorDiaSemana(self):
        tarifa1 = Tarifa(100,200)
        tiempoDeReservacionr1 = [datetime(2015,4,22,13,4), datetime(2015,4,22,13,19)]
        self.assertEqual(calcularPrecio(tarifa1, tiempoDeReservacionr1), 100.00)
        
    #Caso de prueba con el borde superior
    #Descripcion:    trata de evaluar una de las
    #fronteras cuando la reserva es de 7 dias
    #Entrada:    Tiempo de reservacion en horas: 24*7 = 168  
    #            Tasa en bolivares de la hora: 100
    #Salida Esperada    (2400.00*5)+(4800.00*2) = 21600.00 bolivares
    #Solucion: Satisfactorio, ya que da la respuesta correcta.

    def testBordeSuperiorDiaSemana(self):
        tarifa1 = Tarifa(100,200)
        tiempoDeReservacionr1 = [datetime(2015,4,22,13,4), datetime(2015,4,29,13,4)]
        self.assertEqual(calcularPrecio(tarifa1, tiempoDeReservacionr1), 21600.00)

    #Caso de prueba con el borde inferior minimo representable
    #Descripcion:    trata de evaluar una de las
    #fronteras cuando la reserva es de 15 minutos
    #Entrada:    Tiempo de reservacion en minutos: 15 
    #            Tasa en bolivares de la hora: 100
    #Salida Esperada    25.00 bolivares
    #Solucion: Satisfactorio, ya que da la respuesta correcta.
    
    #Nota: Posee el mismo problema que el caso BordeInferiorDiaSemana con los 15 minutos.
          
    def testBordeInferiorDiaSemanaMin(self):
        tarifa1 = Tarifa(100,200)
        tiempoDeReservacionr1 = [datetime.min, datetime.min + timedelta(minutes = 15)]
        self.assertEqual(calcularPrecio(tarifa1, tiempoDeReservacionr1), 25.00)
                
    #Caso de prueba con el borde superior maximo representable
    #Descripcion:    trata de evaluar una de las
    #fronteras cuando la reserva es de 7 dias
    #Entrada:    Tiempo de reservacion en horas: 24*7 = 168  
    #            Tasa en bolivares de la hora: 100
    #Salida Esperada    (2400.00*5)+(4800.00*2) = 21600.00 bolivares
    #Solucion: Satisfactorio, ya que da la respuesta correcta.
    
    def testBordeSuperiorDiaSemanaMaximo(self):
        tarifa1 = Tarifa(100,200)
        tiempoDeReservacionr1 = [datetime.max - timedelta(days = 7), datetime.max]
        self.assertEqual(calcularPrecio(tarifa1, tiempoDeReservacionr1), 21600.00)
        
    #Caso de prueba con Tarifa cero en un dia de la semana
    #Descripcion:    trata de evaluar si la funcion trabaja
    #correctamente si la tarifa por hora es cero.
    #Entrada:    Tiempo de reservacion en horas: 24
    #            Tasa en bolivares de la hora: 0
    #Salida Esperada:    0 bolivares
    #Solucion: Satisfactorio, ya que da la respuesta correcta.
    
    def testTarifaCeroDiaSemana(self):
        tarifa1 = Tarifa(0,200)
        tiempoDeReservacionr1 = [datetime(2015,4,20,23,4), datetime(2015,4,21,23,4)]
        self.assertEqual(calcularPrecio(tarifa1, tiempoDeReservacionr1), 0)
    
    #Caso de prueba con Tarifa de un centimo en un dia de la semana
    #Descripcion:    trata de evaluar si la funcion trabaja correctamente
    #si la tarifa por hora es representada en centimos.
    #Entrada:    Tiempo de reservacion en horas: 24
    #            Tasa en bolivares de la hora: 0.01
    #Salida Esperada:    0.24 bolivares
    #Solucion: Satisfactorio, ya que da la respuesta correcta.
    
    #Nota: Se tuvo que expresar la respuesta de forma que concordara a la salida
    #en decimal de la funcion debido a problemas de tipos de elementos en el lenguaje.
       
    def testTarifaCentimoDiaSemana(self):
        tarifa1 = Tarifa(0.01,200)
        tiempoDeReservacionr1 = [datetime(2015,4,20,23,4), datetime(2015,4,21,23,4)]
        self.assertEqual(calcularPrecio(tarifa1, tiempoDeReservacionr1), Decimal(0.24).quantize(Decimal('1.00')))
        
#--------------------------b)Tiempo No reservable-----------------------------------

    #Caso de prueba con el borde inferior
    #Descripcion:    trata de evaluar una de las
    #fronteras cuando la reserva es de 14 minutos
    #Entrada:    Tiempo de reservacion en minutos: 15 
    #            Tasa en bolivares de la hora: 100
    #Salida Esperada:    Error sobre menos de 15 minutos
    #Solucion: Satisfactorio, ya que da la respuesta correcta.
          
    def testBordeInferiorDiaSemanaNR(self):
        tarifa1 = Tarifa(100,200)
        tiempoDeReservacionr1 = [datetime(2015,4,22,13,4), datetime(2015,4,22,13,14)]
        self.assertRaises(Exception,calcularPrecio,tarifa1,tiempoDeReservacionr1)
        
    #Caso de prueba con el borde superior
    #Descripcion:    trata de evaluar una de las
    #fronteras cuando la reserva es de 7 dias y 1 minuto
    #Entrada:    Tiempo de reservacion en horas: 24*7 + 1 = 169  
    #            Tasa en bolivares de la hora: 100
    #Salida Esperada:    Error sobre mas de 7 dias
    #Solucion: Satisfactorio, ya que da la respuesta correcta.

    def testBordeSuperiorDiaSemanaNR(self):
        tarifa1 = Tarifa(100,200)
        tiempoDeReservacionr1 = [datetime(2015,4,22,13,4), datetime(2015,4,29,13,5)]
        self.assertRaises(Exception,calcularPrecio,tarifa1,tiempoDeReservacionr1) 


    #Caso de prueba con tarifa negativa en un dia de la semana
    #Descripcion:    trata de evaluar si la funcion trabaja correctamente
    #si la tarifa por hora es representada en numeros negativos.
    #Entrada:    Tiempo de reservacion en horas: 24
    #            Tasa en bolivares de la hora: -100
    #Salida Esperada:    Excepcion de tarifas negativas
    #Solucion: Satisfactorio, ya que da la respuesta correcta.
    
    def testTarifaNegativaDiaSemana(self):
        tarifa1 = Tarifa(-100,200)
        tiempoDeReservacionr1 = [datetime(2015,4,20,23,4), datetime(2015,4,21,23,4)]
        self.assertRaises(Exception,calcularPrecio,tarifa1,tiempoDeReservacionr1)    
                       
#--------------------------c)Esquina y Malicia---------------------------------------

    #Caso de prueba con string en la tarifa en un dia de la semana
    #Descripcion:    trata de evaluar si la funcion trabaja correctamente
    #si la tarifa por hora es representada en String.
    #Entrada:    Tiempo de reservacion en horas: 24
    #            Tasa en bolivares de la hora: String
    #Salida Esperada:    Excepcion de String
    #Solucion: Insatisfactorio ya que no se captura la excepcion en la funcion.
    
    def testTarifaStringDiaSemana(self):
        tarifa1 = Tarifa("aba","LOL")
        tiempoDeReservacionr1 = [datetime(2015,4,20,23,4), datetime(2015,4,21,23,4)]
        self.assertRaises(TypeError,calcularPrecio,tarifa1,tiempoDeReservacionr1)
    
    #Caso de prueba con numeros enteros en la lista de tiempo de reservacion
    #Descripcion:    trata de evaluar si la funcion trabaja correctamente
    #cuando los datos de la resrva son numeros entero y no fechas.
    #Entrada:    Tiempo de reservacion en horas: Numeros enteros cualquiera
    #            Tasa en bolivares de la hora: 100
    #Salida Esperada:    Excepcion
    #Solucion: Insatisfactorio ya que no se captura la excepcion en la funcion.
    
    def testReservaNumeroEnteroDiaSemana(self):
        tarifa1 = Tarifa(100,200)
        tiempoDeReservacionr1 = [10,130]
        self.assertRaises(TypeError,calcularPrecio,tarifa1,tiempoDeReservacionr1)

    #Caso de prueba con tarifas de decimales
    #Descripcion:    trata de evaluar si la funcion trabaja correctamente
    #si la tarifa por hora es representada en decimales.
    #Entrada:    Tiempo de reservacion en horas: 24
    #            Tasa en bolivares de la hora: 0.0001
    #Salida Esperada:    Excepcion
    #Solucion: Insatisfactorio ya que no se captura la excepcion en la funcion.
    
    #Nota: se esperaba que diese una excepcion ya que en el enunciado se plantea:
    #"Las tasas por hora se introducen en bolivares y centimos y no pueden ser negativas."
    #y se esta usando una tasa en la tarifa que es mucho menor que un centimo.
    
    def testTarifaDecimalesDiaSemana(self):
        tarifa1 = Tarifa(0.0001,200)
        tiempoDeReservacionr1 = [datetime(2015,4,20,23,4), datetime(2015,4,21,23,4)]
        self.assertRaises(Exception,calcularPrecio,tarifa1,tiempoDeReservacionr1)    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testcalcularPrecio']
    unittest.main()
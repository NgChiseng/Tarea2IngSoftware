'''
Created on 21/4/2015

@author: Chiseng
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
    #Salida Esperada:    2400.00 bolivares(Satisfactorio)
    
    def testNormalDiaSemana(self):
        tarifa1 = Tarifa(100,200)
        tiempoDeReservacionr1 = [datetime(2015,4,20,23,4), datetime(2015,4,21,23,4)]
        self.assertEqual(calcularPrecio(tarifa1, tiempoDeReservacionr1), 2400.00)
    
    #Caso de prueba con el borde inferior
    #Descripcion:    trata de evaluar una de las
    #fronteras cuando la reserva es de 15 minutos
    #Entrada:    Tiempo de reservacion en minutos: 15 
    #            Tasa en bolivares de la hora: 100
    #Salida Esperada    100.00 bolivares(Insatisfactorio)
    
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
    #Salida Esperada    (2400.00*5)+(4800.00*2) = 21600.00 bolivares(Satisfactorio)

    def testBordeSuperiorDiaSemana(self):
        tarifa1 = Tarifa(100,200)
        tiempoDeReservacionr1 = [datetime(2015,4,22,13,4), datetime(2015,4,29,13,4)]
        self.assertEqual(calcularPrecio(tarifa1, tiempoDeReservacionr1), 21600.00)

    #Caso de prueba con el borde inferior minimo representable
    #Descripcion:    trata de evaluar una de las
    #fronteras cuando la reserva es de 15 minutos
    #Entrada:    Tiempo de reservacion en minutos: 15 
    #            Tasa en bolivares de la hora: 100
    #Salida Esperada    25.00 bolivares(Satisfactorio)
    
    #Nota: Posee el mismo problema que el caso BordeInferiorDiaSemana
          
    def testBordeInferiorDiaSemanaMin(self):
        tarifa1 = Tarifa(100,200)
        tiempoDeReservacionr1 = [datetime.min, datetime.min + timedelta(minutes = 15)]
        self.assertEqual(calcularPrecio(tarifa1, tiempoDeReservacionr1), 25.00)
                
    #Caso de prueba con el borde superior maximo representable
    #Descripcion:    trata de evaluar una de las
    #fronteras cuando la reserva es de 7 dias
    #Entrada:    Tiempo de reservacion en horas: 24*7 = 168  
    #            Tasa en bolivares de la hora: 100
    #Salida Esperada    (2400.00*5)+(4800.00*2) = 21600.00 bolivares(Satisfactorio)
    
    def testBordeSuperiorDiaSemanaMaximo(self):
        tarifa1 = Tarifa(100,200)
        tiempoDeReservacionr1 = [datetime.max - timedelta(days = 7), datetime.max]
        self.assertEqual(calcularPrecio(tarifa1, tiempoDeReservacionr1), 21600.00)
        
    #Caso de prueba con Tarifa cero en un dia de la semana
    #Entrada:    Tiempo de reservacion en horas: 24
    #            Tasa en bolivares de la hora: 0
    #Salida Esperada:    0 bolivares(Satisfactorio)
    
    def testTarifaCeroDiaSemana(self):
        tarifa1 = Tarifa(0,200)
        tiempoDeReservacionr1 = [datetime(2015,4,20,23,4), datetime(2015,4,21,23,4)]
        self.assertEqual(calcularPrecio(tarifa1, tiempoDeReservacionr1), 0)
    
    #Caso de prueba con Tarifa de un centimo en un dia de la semana
    #Entrada:    Tiempo de reservacion en horas: 24
    #            Tasa en bolivares de la hora: 0.01
    #Salida Esperada:    0.24 bolivares(Satisfactorio)
    
    #Nota: da un error cuando se le da el resultado de 0.24   
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
    #Salida Esperada:    Error sobre menos de 15 minutos(Satisfactorio)
          
    def testBordeInferiorDiaSemanaNR(self):
        tarifa1 = Tarifa(100,200)
        tiempoDeReservacionr1 = [datetime(2015,4,22,13,4), datetime(2015,4,22,13,14)]
        try:
            calcularPrecio(tarifa1, tiempoDeReservacionr1)
        except:
            self.assertTrue(True)
        
    #Caso de prueba con el borde superior
    #Descripcion:    trata de evaluar una de las
    #fronteras cuando la reserva es de 7 dias y 1 minuto
    #Entrada:    Tiempo de reservacion en horas: 24*7 + 1 = 169  
    #            Tasa en bolivares de la hora: 100
    #Salida Esperada:    Error sobre mas de 7 dias(Satisfactorio)

    def testBordeSuperiorDiaSemanaNR(self):
        tarifa1 = Tarifa(100,200)
        tiempoDeReservacionr1 = [datetime(2015,4,22,13,4), datetime(2015,4,29,13,5)]
        try:
            calcularPrecio(tarifa1, tiempoDeReservacionr1)
        except:
            self.assertTrue(True)
            
    #Caso de prueba con el borde inferior minimo representable
    #Descripcion:    trata de evaluar una de las
    #fronteras cuando la reserva es de  menos de 15 minutos
    #Entrada:    Tiempo de reservacion en minutos: 15 
    #            Tasa en bolivares de la hora: 100
    #Salida Esperada: Error de Overflow(Satisfactorio)
    
    #Nota: Nota se da pero un error de Overflow y no como una excepcion que indica que tienen menos
    #de 15 minutos reservados.
          
    #def testBordeInferiorDiaSemanaMinNR(self):
    #    tarifa1 = Tarifa(100,200)
    #    tiempoDeReservacionr1 = [datetime.min - timedelta(minutes = 15), datetime.min]
    #    self.assertEqual(calcularPrecio(tarifa1, tiempoDeReservacionr1), 25.00)

    #Caso de prueba con el borde superior maximo representable
    #Descripcion:    trata de evaluar una de las
    #fronteras cuando la reserva es de mas de 7 dias
    #Entrada:    Tiempo de reservacion en horas: 24*7 = 168  
    #            Tasa en bolivares de la hora: 100
    #Salida Esperada:    Error de OverFlow(Satisfactorio)
    
    #def testBordeSuperiorDiaSemanaMaximoNR(self):
    #    tarifa1 = Tarifa(100,200)
    #    tiempoDeReservacionr1 = [datetime.max, datetime.max + timedelta(days = 7)]
    #    self.assertEqual(calcularPrecio(tarifa1, tiempoDeReservacionr1), 21600.00)        
    
#--------------------------c)Indefinido---------------------------------------------

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testcalcularPrecio']
    unittest.main()
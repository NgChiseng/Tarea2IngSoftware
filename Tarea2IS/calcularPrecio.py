'''
Creado el 17/04/2015

Funcion calcularPrecio para la Tarea 2 de Ing. del Software (ABR-JUL 2015). 
Modificacion del codigo legado por FragantSoft. 

'''

from decimal import Decimal
from datetime import timedelta

# Maneja una tasa para los dias de semana y otra para los fines de semana. 
class Tarifa(object):
    def __init__(self, tasaDiaSemana, tasaFinSemana):
        self.tasaDiaSemana = tasaDiaSemana
        self.tasaFinSemana = tasaFinSemana
    
# Dado un tiempo de reservacion:
#     tiempoDeReservacionr = [inicioDeReservacion, finDeReservacion]   
# Calcula el monto a pagar por la misma. 
def calcularPrecio(tarifa, tiempoDeReservacionr):
        
        if tarifa.tasaDiaSemana < 0 or tarifa.tasaFinSemana < 0:
            raise Exception("No se admiten tarifas negativas.")
        if tiempoDeReservacionr[1] - tiempoDeReservacionr[0] > timedelta(days=7):
            raise Exception("La reserva no debe ser mayor a siete (7) dias.")
        if tiempoDeReservacionr[1] - tiempoDeReservacionr[0] < timedelta(minutes=15):
            raise Exception("La reserva debe ser como minimo de quince (15) mintuos")
             
        minutosNormales    = 0
        minutosFinDeSemana = 0
        tiempoActual       = tiempoDeReservacionr[0]
        minuto             = timedelta(minutes=1)
        while tiempoActual < tiempoDeReservacionr[1]:
            # weekday() devuelve un numero del 0 al 6 tal que
            # 0 = Lunes
            # 1 = Martes
            # ..
            # 5 = Sabado
            # 6 = Domingo
            if tiempoActual.weekday() < 5:
                minutosNormales += 1
            else:
                minutosFinDeSemana += 1
            tiempoActual += minuto
        return Decimal(
            minutosNormales*tarifa.tasaDiaSemana/60 +
            minutosFinDeSemana*tarifa.tasaFinSemana/60
        ).quantize(Decimal('1.00'))
        
        
if __name__ == '__main__':
    pass
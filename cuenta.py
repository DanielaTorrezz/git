class Cuenta:
  pass
  def __init__ (self,titular,cantidad):
    self.titular= titular
    self.cantidad=cantidad
  def mostrar(self,Cuenta):
    self.Cuenta= Cuenta
    print("La persona titular de la cuenta es:", self.titular, "\nLa cantidad de saldo en su cuenta es de:", self.cantidad, "pesos")
  def ingresar (self,numero1):
    self.numero1= numero1
    print("Su nuevo saldo es:", self.numero1+self.cantidad, "pesos")
  def retirar (self,numero2):
    self.numero2= numero2
    print("Usted retiró:", numero2,"pesos" "\nSu saldo actual es:",self.cantidad-numero2, "pesos")
cuenta1= Cuenta("Daniela Torrez", 327523.76)
cuenta1.mostrar(Cuenta)
cuenta1.ingresar(7000)
cuenta1.retirar(2000)
print(cuenta1)
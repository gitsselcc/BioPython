class gene():
     def __init__(self,nombre,ubicacion,secuencia):
          self.nombre= nombre
          self.ubicacion= ubicacion
          self.secuencia= secuencia.upper()
     def cant_t(self):
          return self.secuencia.count("T")
     def longitud(self):
          return len(self.secuencia)
     def GC_porcentaje(self):
          gc= self.secuencia.count('G') + self.secuencia.count('C')
          return  (gc / len(self.secuencia)) * 100
     def secuencia_reversa (self):
          return self.secuencia[::-1]
     
hola=gene("susano","higado","aaaaaaCGCGCGCGCGCGCGCTTTTT")
print("Nuestro gen se llama",hola.nombre, "se ubica en", hola.ubicacion, "y su secuencia es", hola.secuencia)
print("Cantidad de T:", hola.cant_t())
print("Longitud de la secuencia:", hola.longitud())
print("El porcentaje de GC en nuestra secuencia es de", hola.GC_porcentaje())
print("La secuencia reversa es", hola.secuencia_reversa())
class Cafetera:
    def __init__(self, capacidad_maxima=1000, cantidad_actual=0):
        """
        Constructor de la clase Cafetera
        - Constructor predeterminado: capacidad máxima 1000 c.c., cantidad actual 0
        - Constructor con parámetros: Si cantidad_actual > capacidad_maxima, se ajusta al máximo
        
        Args:
            capacidad_maxima (int): Capacidad máxima de la cafetera en c.c. (por defecto 1000)
            cantidad_actual (int): Cantidad actual de café en la cafetera (por defecto 0)
        """
        self.capacidad_maxima = capacidad_maxima
        
        
        if cantidad_actual > capacidad_maxima:
            self.cantidad_actual = capacidad_maxima
        else:
            self.cantidad_actual = cantidad_actual
    
    def llenar_cafetera(self):
        """
        Llena la cafetera hasta su capacidad máxima
        """
        self.cantidad_actual = self.capacidad_maxima
        print(f"Cafetera llenada. Cantidad actual: {self.cantidad_actual} c.c.")
    
    def servir_taza(self, capacidad_taza):
        """
        Sirve una taza con la capacidad indicada
        Si la cantidad actual no alcanza para llenar la taza, se sirve lo que quede
        
        Args:
            capacidad_taza (int): Capacidad de la taza a servir
            
        Returns:
            int: Cantidad de café servida
        """
        if self.cantidad_actual >= capacidad_taza:
            self.cantidad_actual -= capacidad_taza
            cafe_servido = capacidad_taza
            print(f"Taza servida con {cafe_servido} c.c. Cantidad restante: {self.cantidad_actual} c.c.")
        else:
           
            cafe_servido = self.cantidad_actual
            self.cantidad_actual = 0
            print(f"No alcanza para llenar la taza. Se sirvió {cafe_servido} c.c. Cafetera vacía.")
        
        return cafe_servido
    
    def vaciar_cafetera(self):
        """
        Vacía completamente la cafetera (pone la cantidad actual en cero)
        """
        self.cantidad_actual = 0
        print("Cafetera vaciada completamente.")
    
    def agregar_cafe(self, cantidad):
        """
        Añade a la cafetera la cantidad de café indicada
        
        Args:
            cantidad (int): Cantidad de café a añadir
        """
        if self.cantidad_actual + cantidad <= self.capacidad_maxima:
            self.cantidad_actual += cantidad
            print(f"Se añadieron {cantidad} c.c. Cantidad actual: {self.cantidad_actual} c.c.")
        else:
            cantidad_agregada = self.capacidad_maxima - self.cantidad_actual
            self.cantidad_actual = self.capacidad_maxima
            print(f"Solo se pudieron añadir {cantidad_agregada} c.c. Cafetera llena: {self.cantidad_actual} c.c.")
    
    def mostrar_estado(self):
        """
        Muestra el estado actual de la cafetera
        """
        print(f"Estado de la cafetera:")
        print(f"- Capacidad máxima: {self.capacidad_maxima} c.c.")
        print(f"- Cantidad actual: {self.cantidad_actual} c.c.")
        print(f"- Espacio disponible: {self.capacidad_maxima - self.cantidad_actual} c.c.")
        print("-" * 40)


def main():
    """
    Método main que manipula la clase Cafetera
    Demuestra todos los métodos y funcionalidades implementadas
    """
    print("=== MANIPULACIÓN DE LA CLASE CAFETERA ===\n")
    
    
    print("1. Constructor predeterminado (capacidad 1000, cantidad 0):")
    cafetera1 = Cafetera()
    cafetera1.mostrar_estado()
    
    
    print("2. Constructor con parámetros (capacidad 800, cantidad 300):")
    cafetera2 = Cafetera(800, 300)
    cafetera2.mostrar_estado()
    
    
    print("3. Constructor con cantidad actual mayor a capacidad máxima (600, 900):")
    cafetera3 = Cafetera(600, 900)  
    cafetera3.mostrar_estado()
    
    
    print("4. Manipulando cafetera1:")
    
    
    print("   a) Llenando cafetera:")
    cafetera1.llenar_cafetera()
    
   
    print("   b) Sirviendo taza de 250 c.c.:")
    cafetera1.servir_taza(250)
    
    
    print("   c) Agregando 100 c.c. de café:")
    cafetera1.agregar_cafe(100)
    
   
    print("   d) Sirviendo taza de 1200 c.c. (más de lo disponible):")
    cafetera1.servir_taza(1200)
    

    print("   e) Agregando 500 c.c. a cafetera vacía:")
    cafetera1.agregar_cafe(500)

    print("   f) Intentando agregar 700 c.c. más (excede capacidad):")
    cafetera1.agregar_cafe(700)
    

    print("   g) Vaciando cafetera:")
    cafetera1.vaciar_cafetera()
    
  
    print("\n5. Manipulando cafetera2 (capacidad 800, con 300 c.c.):")
    
   
    print("   a) Sirviendo taza de 150 c.c.:")
    cafetera2.servir_taza(150)
    
    print("   b) Sirviendo taza de 100 c.c.:")
    cafetera2.servir_taza(100)
    
    print("   c) Intentando servir taza de 200 c.c. (más de lo que queda):")
    cafetera2.servir_taza(200)  
    
  
    print("   d) Llenando cafetera:")
    cafetera2.llenar_cafetera()
    
    print("   e) Vaciando cafetera:")
    cafetera2.vaciar_cafetera()
    
    print("\n=== FIN DE LA MANIPULACIÓN ===")



if __name__ == "__main__":
    main()
import numpy as np
import string
from tabulate import tabulate
import networkx as nx
import matplotlib.pyplot as plt
import os


class LogoMenu:
    
    def __init__(self):
        self.logo = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0],
            [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
            [0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
    
    def dibujar_logo(self):
        for i in range(20):
            print(" " * 15, end='')
            for j in range(16):
                if self.logo[i][j] == 1:
                    print(chr(42), end='')
                else:
                    print(" ", end='')
            print()
    
    def mostrar_menu(self):
        self.limpiar_pantalla()
        print("=" * 50)
        print("                    GRUPO 4")
        print("         Curso Matemática Computacional")
        self.dibujar_logo()
        print()
        print("Integrantes: ")
        print(" - Herrera Isla, Jose Luis")
        print(" - Quispe Salvador, Jean Paul")
        print(" - Rodriguez Espinoza, Jairo Jalil Antonino")
        print(" - Sandonas Mechato, Benjamín Del Piero")
        print(" - Zurita Lara, Rodrigo Eduardo")
        print()
        print("Profesor: ")
        print(" - Venegas Palacios, Edgard Kenny")
        print()
        print("=" * 50)
        print("\nMenú Principal:")
        print("1. Generar matriz aleatoria")
        print("2. Ingresar matriz manualmente")
        print("3. Salir")
        print("\n" + "=" * 50)
    
    @staticmethod
    def limpiar_pantalla():
        os.system('cls' if os.name == 'nt' else 'clear')


class Matriz:
    
    def __init__(self, n):
        self.n = n
        self.matriz = None
    
    def generar_aleatoria(self):
        self.matriz = np.random.randint(1, 100, size=(self.n, self.n))
        self.matriz = (self.matriz + self.matriz.T) // 2
        np.fill_diagonal(self.matriz, 0)
        return self.matriz
    
    def ingresar_manual(self):
        LogoMenu.limpiar_pantalla()
        print(f"\nIngrese los valores para la matriz {self.n}x{self.n}:")
        self.matriz = np.zeros((self.n, self.n))
        
        for i in range(self.n):
            for j in range(i+1, self.n):
                while True:
                    try:
                        valor = int(input(f"Ingrese el valor para la posición ({i},{j}): "))
                        if valor <= 0:
                            print("Error: Por favor ingrese solo números positivos mayores a 0.")
                            continue
                        self.matriz[i][j] = valor
                        self.matriz[j][i] = valor
                        break
                    except ValueError:
                        print("Error: Por favor ingrese un número válido.")
        return self.matriz
    
    def mostrar(self):
        print("\nMatriz de distancias:")
        print(self.matriz)
    
    @staticmethod
    def solicitar_tamano():
        while True:
            try:
                n = int(input("\nIngrese el tamaño de la matriz (entre 8 y 16): "))
                if 8 <= n <= 16:
                    return n
                else:
                    print("El tamaño debe estar entre 8 y 16")
            except ValueError:
                print("Por favor ingrese un número válido")


class Ruta:
    
    def __init__(self, secuencia, matriz):
        self.secuencia = secuencia
        self.matriz = matriz
        self.distancias = []
        self.distancia_total = 0
        self.calcular_distancia()
    
    def calcular_distancia(self):
        self.distancias = []
        for i in range(len(self.secuencia)-1):
            self.distancias.append(self.matriz[self.secuencia[i]][self.secuencia[i+1]])
        self.distancias.append(self.matriz[self.secuencia[-1]][self.secuencia[0]])
        self.distancia_total = sum(self.distancias)
    
    def convertir_a_letras(self):
        letras = string.ascii_uppercase
        ruta_letras = [letras[i] for i in self.secuencia]
        ruta_letras.append(letras[self.secuencia[0]])
        return ' -> '.join(ruta_letras)
    
    def obtener_distancias_str(self):
        return " + ".join(str(d) for d in self.distancias)


class GeneradorRutas:
    
    def __init__(self, n):
        self.n = n
        self.rutas = []
    
    def generar_todas(self):
        elementos_restantes = list(range(1, self.n))
        self.rutas = []
        self._generar_recursivo(elementos_restantes, [0], self.rutas)
        return self.rutas
    
    def _generar_recursivo(self, elementos, ruta_actual, rutas):
        if len(elementos) == 0:
            rutas.append(ruta_actual)
            return
        
        for i in range(len(elementos)):
            nuevo_elementos = elementos[:i] + elementos[i+1:]
            nueva_ruta = ruta_actual + [elementos[i]]
            self._generar_recursivo(nuevo_elementos, nueva_ruta, rutas)


class AlgoritmoFuerzaBruta:
    
    def __init__(self, matriz):
        self.matriz = matriz
        self.n = len(matriz)
        self.mejor_ruta = None
        self.mejor_distancia = float('inf')
        self.todas_rutas = []
    
    def resolver(self):
        generador = GeneradorRutas(self.n)
        rutas = generador.generar_todas()
        rutas.sort(key=lambda x: x[1:])
        total_rutas = len(rutas) // 2
        
        print(f"\nProcesando {total_rutas} rutas (eliminando simétricas):")
        
        headers = ["N° de ruta", "Secuencia de nodos", "Distancias", "Total"]
        table_data = []
        
        for i in range(total_rutas):
            ruta_obj = Ruta(rutas[i], self.matriz)
            
            row = [
                f"Ruta {i+1}",
                ruta_obj.convertir_a_letras(),
                ruta_obj.obtener_distancias_str(),
                ruta_obj.distancia_total
            ]
            
            table_data.append(row)
            self.todas_rutas.append((ruta_obj.secuencia, ruta_obj.distancia_total))
            
            if ruta_obj.distancia_total < self.mejor_distancia:
                self.mejor_distancia = ruta_obj.distancia_total
                self.mejor_ruta = ruta_obj.secuencia
        
        print(tabulate(table_data, headers=headers, tablefmt='pipe', stralign='center'))
        
        return self.mejor_ruta, self.mejor_distancia, self.todas_rutas


class AlgoritmoVecinoCercano:
    
    def __init__(self, matriz):
        self.matriz = matriz
        self.n = len(matriz)
        self.mejor_ruta = None
        self.mejor_distancia = float('inf')
        self.todas_rutas = []
    
    def generar_ruta_desde_inicio(self, inicio):
        ruta = [inicio]
        nodos_disponibles = set(range(self.n)) - {inicio}
        
        while nodos_disponibles:
            ultimo = ruta[-1]
            siguiente = min(nodos_disponibles, 
                          key=lambda x: self.matriz[ultimo][x])
            ruta.append(siguiente)
            nodos_disponibles.remove(siguiente)
        return ruta
    
    def resolver(self):
        rutas_con_distancias = []
        
        for inicio in range(self.n):
            ruta_secuencia = self.generar_ruta_desde_inicio(inicio)
            ruta_obj = Ruta(ruta_secuencia, self.matriz)
            rutas_con_distancias.append((ruta_obj.secuencia, ruta_obj.distancia_total))
        
        rutas_con_distancias.sort(key=lambda x: x[1])
        
        headers = ["N° de ruta", "Nodo inicial", "Secuencia de nodos", "Distancias", "Total"]
        table_data = []
        
        for i, (ruta_sec, dist_total) in enumerate(rutas_con_distancias, 1):
            ruta_obj = Ruta(ruta_sec, self.matriz)
            nodo_inicial = string.ascii_uppercase[ruta_sec[0]]
            
            row = [
                f"Ruta {i}",
                f"Desde {nodo_inicial}",
                ruta_obj.convertir_a_letras(),
                ruta_obj.obtener_distancias_str(),
                dist_total
            ]
            table_data.append(row)
            self.todas_rutas.append((ruta_sec, dist_total))
            
            if dist_total < self.mejor_distancia:
                self.mejor_distancia = dist_total
                self.mejor_ruta = ruta_sec
        
        print(f"\nRutas calculadas usando vecino más cercano desde cada nodo inicial:")
        print(tabulate(table_data, headers=headers, tablefmt='pipe', stralign='center'))
        
        return self.mejor_ruta, self.mejor_distancia, self.todas_rutas


class VisualizadorRutas:
    
    def __init__(self, matriz):
        self.matriz = matriz
        self.n = len(matriz)
    
    def dibujar_ruta(self, ruta, distancia_total, tipo_ruta="", num_ruta=0):
        G = nx.Graph()
        letras = string.ascii_uppercase
        pos = {}
        
        for i in range(self.n):
            angle = 2 * np.pi * i / self.n
            pos[i] = (np.cos(angle), np.sin(angle))
            G.add_node(i)
        
        for i in range(self.n):
            for j in range(i+1, self.n):
                if self.matriz[i][j] > 0:
                    G.add_edge(i, j, weight=self.matriz[i][j])
        
        ruta_edges = list(zip(ruta[:-1], ruta[1:])) + [(ruta[-1], ruta[0])]
        
        plt.figure(figsize=(12, 8))
        
        nx.draw_networkx_edges(G, pos, alpha=0.2, width=1)
        nx.draw_networkx_edges(G, pos, edgelist=ruta_edges, edge_color='red', width=2)
        nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue')
        
        labels = {i: letras[i] for i in range(self.n)}
        nx.draw_networkx_labels(G, pos, labels)
        
        edge_labels = {(ruta[i], ruta[i+1]): self.matriz[ruta[i]][ruta[i+1]] for i in range(len(ruta)-1)}
        edge_labels[(ruta[-1], ruta[0])] = self.matriz[ruta[-1]][ruta[0]]
        nx.draw_networkx_edge_labels(G, pos, edge_labels)
        
        ruta_obj = Ruta(ruta, self.matriz)
        secuencia = ruta_obj.convertir_a_letras()
        
        if tipo_ruta == "Mejor Ruta":
            titulo_completo = f"Mejor Ruta\nDistancia Total: {distancia_total}\nSecuencia: {secuencia}"
        else:
            titulo_completo = f"Ruta {num_ruta}\nDistancia Total: {distancia_total}\nSecuencia: {secuencia}"
        
        plt.title(titulo_completo, pad=20, wrap=True)
        plt.axis('equal')
        plt.axis('off')
        plt.tight_layout()
        plt.show()
    
    def menu_visualizacion(self, todas_rutas):
        while True:
            print("\nOpciones de visualización:")
            print("1. Ver mejor ruta")
            print("2. Ver ruta específica por número")
            print("3. Volver al menú principal")
            
            opcion = input("\nSeleccione una opción (1-3): ")
            
            if opcion == "1":
                mejor_ruta = min(todas_rutas, key=lambda x: x[1])[0]
                mejor_distancia = min(todas_rutas, key=lambda x: x[1])[1]
                self.dibujar_ruta(mejor_ruta, mejor_distancia, "Mejor Ruta", 0)
            elif opcion == "2":
                try:
                    num_ruta = int(input(f"Ingrese el número de ruta (1-{len(todas_rutas)}): ")) - 1
                    if 0 <= num_ruta < len(todas_rutas):
                        ruta = todas_rutas[num_ruta][0]
                        distancia = todas_rutas[num_ruta][1]
                        self.dibujar_ruta(ruta, distancia, "Ruta Específica", num_ruta + 1)
                    else:
                        print("Número de ruta fuera de rango")
                except ValueError:
                    print("Por favor ingrese un número válido")
            elif opcion == "3":
                break
            else:
                print("Opción no válida")


class SistemaAgenteViajero:
    
    def __init__(self):
        self.menu = LogoMenu()
        self.matriz = None
        self.algoritmo = None
        self.visualizador = None
    
    def mostrar_resultados_finales(self, mejor_ruta, mejor_distancia):
        ruta_obj = Ruta(mejor_ruta, self.matriz.matriz)
        print(f"\nMejor ruta encontrada: {ruta_obj.convertir_a_letras()}")
        print(f"Distancias: {ruta_obj.obtener_distancias_str()} = {mejor_distancia}")
    
    def ejecutar(self):
        while True:
            self.menu.mostrar_menu()
            opcion = input("\nSeleccione una opción (1-3): ")
            
            if opcion == '1' or opcion == '2':
                LogoMenu.limpiar_pantalla()
                n = Matriz.solicitar_tamano()
                
                self.matriz = Matriz(n)
                
                if opcion == '1':
                    self.matriz.generar_aleatoria()
                else:
                    self.matriz.ingresar_manual()
                
                self.matriz.mostrar()
                input("\nPresione Enter para continuar...")
                LogoMenu.limpiar_pantalla()
                
                if n >= 11:
                    print(f"\nUsando algoritmo del vecino más cercano para n={n}:")
                    print(f"Se generarán {n} rutas, una empezando desde cada nodo")
                    self.algoritmo = AlgoritmoVecinoCercano(self.matriz.matriz)
                else:
                    print(f"\nUsando algoritmo de fuerza bruta para n={n}...")
                    self.algoritmo = AlgoritmoFuerzaBruta(self.matriz.matriz)
                
                mejor_ruta, mejor_distancia, todas_rutas = self.algoritmo.resolver()
                
                self.mostrar_resultados_finales(mejor_ruta, mejor_distancia)
                
                self.visualizador = VisualizadorRutas(self.matriz.matriz)
                self.visualizador.menu_visualizacion(todas_rutas)
            
            elif opcion == '3':
                LogoMenu.limpiar_pantalla()
                print("\n¡Hasta pronto...! Grupo4")
                break
            else:
                print("\nOpción no válida. Presione Enter para continuar...")
                input()


def main():
    sistema = SistemaAgenteViajero()
    sistema.ejecutar()


if __name__ == "__main__":
    main()
# ================================
# NODO PARA LISTA DOBLEMENTE ENLAZADA
# ================================
# Representa un vehículo dentro de la vía (cada nodo guarda un vehículo)

class NodeD:
    __slots__ = ('__value', '__next', '__prev')

    def __init__(self, value):
        self.__value = value      # vehículo guardado en el nodo
        self.__next = None        # referencia al siguiente nodo
        self.__prev = None        # referencia al nodo anterior

    def __str__(self):
        return str(self.__value)

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, node):
        # valida que el siguiente sea un nodo o None
        if node is not None and not isinstance(node, NodeD):
            raise TypeError("next debe ser un objeto tipo nodo ó None")
        self.__next = node

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, node):
        # valida que el anterior sea un nodo o None
        if node is not None and not isinstance(node, NodeD):
            raise TypeError("prev debe ser un objeto tipo nodo ó None")
        self.__prev = node

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, newValue):
        if newValue is None:
            raise TypeError("el nuevo valor debe ser diferente de None")
        self.__value = newValue

# ================================
# LISTA DOBLEMENTE ENLAZADA (LA VIA DEL TALLER)
# ================================

class DoublyLinkedList:
    def __init__(self):
        self.__head = None    # primer vehículo de la vía
        self.__tail = None    # último vehículo de la vía
        self.__size = 0       # cantidad de vehículos

    @property
    def head(self):
        return self.__head

    @property
    def tail(self):
        return self.__tail

    @property
    def size(self):
        return self.__size

    @head.setter
    def head(self, node):
        if node is not None and not isinstance(node, NodeD):
            raise TypeError("Head debe ser un objeto tipo nodo ó None")
        self.__head = node

    @tail.setter
    def tail(self, node):
        if node is not None and not isinstance(node, NodeD):
            raise TypeError("Tail debe ser un objeto tipo nodo ó None")
        self.__tail = node

    @size.setter
    def size(self, num):
        self.__size = num

    # Muestra la vía completa
    def __str__(self):
        result = [str(nodo.value) for nodo in self]
        return ' <--> '.join(result)

    # imprime los vehículos uno por uno
    def print(self):
        for nodo in self:
            print(str(nodo.value))

    # permite recorrer la lista con for
    def __iter__(self):
        current = self.__head
        while current is not None:
            yield current
            current = current.next

    # ================================
    # PUNTO 1 DEL TALLER
    # Insertar vehículos al final de la vía
    # ================================
    def prepend(self, value):
        newnode = NodeD(value)
        if self.__head is None:
            self.__head = newnode
            self.__tail = newnode
        else:
            newnode.next = self.__head
            self.__head.prev = newnode
            self.__head = newnode
        self.__size += 1

    def append(self, value):
        newnode = NodeD(value)
        if self.__head is None:
            self.__head = newnode
            self.__tail = newnode
        else:
            self.__tail.next = newnode
            newnode.prev = self.__tail
            self.__tail = newnode
        self.__size += 1

# ================================
# NODO PARA LISTA ENLAZADA SIMPLE (USADA POR LA COLA)
# ================================

class Node:
    __slots__ = ('__value', '__next')

    def __init__(self, value):
        self.__value = value
        self.__next = None

    def __str__(self):
        return str(self.__value)

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, node):
        if node is not None and not isinstance(node, Node):
            raise TypeError("next debe ser un objeto tipo nodo ó None")
        self.__next = node

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, newValue):
        if newValue is None:
            raise TypeError("el nuevo valor debe ser diferente de None")
        self.__value = newValue

# ================================
# LISTA ENLAZADA SIMPLE (USADA INTERNAMENTE POR LA COLA)
# ================================

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    @property
    def head(self):
        return self.__head

    @property
    def tail(self):
        return self.__tail

    @property
    def size(self):
        return self.__size

    @head.setter
    def head(self, node):
        if node is not None and not isinstance(node, Node):
            raise TypeError("Head debe ser un objeto tipo nodo ó None")
        self.__head = node

    @tail.setter
    def tail(self, node):
        if node is not None and not isinstance(node, Node):
            raise TypeError("Tail debe ser un objeto tipo nodo ó None")
        self.__tail = node

    @size.setter
    def size(self, num):
        self.__size = num

    def __str__(self):
        result = [str(nodo.value) for nodo in self]
        return ' <--> '.join(result)

    def print(self):
        for nodo in self:
            print(str(nodo.value))

    def __iter__(self):
        current = self.__head
        while current is not None:
            yield current
            current = current.next

    def append(self, value):
        newnode = Node(value)
        if self.__head is None:
            self.__head = newnode
            self.__tail = newnode
        else:
            self.__tail.next = newnode
            self.__tail = newnode
        self.__size += 1

    def popfirst(self):
        tempNode = self.__head
        if self.__head is None:
            return None
        elif self.__size == 1:
            self.__head = None
            self.__tail = None
            self.__size = 0
        else:
            self.__head = self.__head.next
            self.__size -= 1

        tempNode.next = None
        return tempNode

# ================================
# COLA (USADA EN EL PUNTO 7 - SEMÁFORO)
# ================================

class Queue:
    def __init__(self):
        self.__queue = LinkedList()

    def enqueue(self, e):
        self.__queue.append(e)
        return True

    def dequeue(self):
        if self.is_empty():
            return "No hay elementos en la cola"
        else:
            first_node = self.__queue.popfirst()
            return first_node.value

    def is_empty(self):
        return self.__queue.size == 0

    def len(self):
        return self.__queue.size

    def firs(self):
        return self.__queue.head.value

    def __str__(self):
        result = [str(nodo.value) for nodo in self.__queue]
        return ' -- '.join(result)

# ================================
# CLASE VEHICULO (LO QUE GUARDA LA VIA)
# ================================

class Vehiculo:
    def __init__(self, placa, tipo, prioridad):
        self.placa = placa
        self.tipo = tipo
        self.prioridad = prioridad

    def __str__(self):
        return f"{self.placa} {self.tipo} {self.prioridad}"

# ================================
# PUNTO 2 DEL TALLER
# Paso preferencial: mover motos prioridad 1 al frente
# ================================

def paso_preferencial(via):
    ultimo_movido = None
    nodo = via.head

    while nodo:
        siguiente = nodo.next

        if nodo.value.tipo == "moto" and nodo.value.prioridad == 1:
            if nodo.prev:
                nodo.prev.next = nodo.next
            else:
                nodo = siguiente
                continue

            if nodo.next:
                nodo.next.prev = nodo.prev
            else:
                via.tail = nodo.prev

            if ultimo_movido is None:
                nodo.prev = None
                nodo.next = via.head
                if via.head:
                    via.head.prev = nodo
                via.head = nodo
            else:
                nodo.prev = ultimo_movido
                nodo.next = ultimo_movido.next
                if ultimo_movido.next:
                    ultimo_movido.next.prev = nodo
                ultimo_movido.next = nodo

            ultimo_movido = nodo

        nodo = siguiente

# ================================
# PUNTO 3 DEL TALLER
# Eliminar camiones con prioridad mayor a 3
# ================================

def eliminar_camiones(via):
    nodo = via.head

    while nodo:
        siguiente = nodo.next
        vehiculo = nodo.value

        if vehiculo.tipo == "camion" and vehiculo.prioridad > 3:
            if nodo == via.head:
                via.head = nodo.next
                if via.head:
                    via.head.prev = None
                else:
                    via.tail = None

            elif nodo == via.tail:
                via.tail = nodo.prev
                via.tail.next = None

            else:
                nodo.prev.next = nodo.next
                nodo.next.prev = nodo.prev

        nodo = siguiente

# ================================
# PUNTO 4 DEL TALLER
# Accidente entre dos placas
# ================================

def accidente(via, placa1, placa2):
    nodo = via.head
    nodo1 = None
    nodo2 = None

    while nodo:
        if nodo.value.placa == placa1:
            nodo1 = nodo
        if nodo.value.placa == placa2:
            nodo2 = nodo
        nodo = nodo.next

    if nodo1 is None or nodo2 is None:
        return

    actual = nodo1
    esta_en_orden = False

    while actual:
        if actual == nodo2:
            esta_en_orden = True
            break
        actual = actual.next

    if not esta_en_orden:
        nodo1, nodo2 = nodo2, nodo1

    actual = nodo1.next

    while actual != nodo2:
        siguiente = actual.next
        actual.prev.next = actual.next
        actual.next.prev = actual.prev
        actual = siguiente

# ================================
# PUNTO 5 DEL TALLER
# Invertir la vía solo si hay más autos que motos
# ================================

def invertir_via(via):
    autos = 0
    motos = 0

    nodo = via.head
    while nodo:
        if nodo.value.tipo == "auto":
            autos += 1
        elif nodo.value.tipo == "moto":
            motos += 1
        nodo = nodo.next

    if autos <= motos:
        return

    nodo = via.head
    while nodo:
        siguiente = nodo.next
        nodo.next = nodo.prev
        nodo.prev = siguiente
        nodo = siguiente

    via.head, via.tail = via.tail, via.head

# ================================
# PUNTO 6 DEL TALLER
# Reorganizar la vía por prioridad
# ================================

def reorganizar_via(via):
    nueva_head = None
    nueva_tail = None

    for p in range(1, 6):
        nodo = via.head

        while nodo:
            siguiente = nodo.next

            if nodo.value.prioridad == p:
                if nodo.prev:
                    nodo.prev.next = nodo.next
                else:
                    via.head = nodo.next

                if nodo.next:
                    nodo.next.prev = nodo.prev
                else:
                    via.tail = nodo.prev

                nodo.prev = nueva_tail
                nodo.next = None

                if nueva_tail:
                    nueva_tail.next = nodo
                else:
                    nueva_head = nodo

                nueva_tail = nodo

            nodo = siguiente

    via.head = nueva_head
    via.tail = nueva_tail

# ================================
# PUNTO 7 DEL TALLER
# Simulación de semáforo usando dos colas
# ================================

def simular_semaforo(via):
    def eliminar_de_via(placa):
        nodo = via.head
        while nodo:
            if nodo.value.placa == placa:
                if nodo.prev:
                    nodo.prev.next = nodo.next
                else:
                    via.head = nodo.next

                if nodo.next:
                    nodo.next.prev = nodo.prev
                else:
                    via.tail = nodo.prev
                return
            nodo = nodo.next

    colaSemaforo = Queue()
    colaRevision = Queue()

    nodo = via.head
    for _ in range(6):
        if nodo:
            colaSemaforo.enqueue(nodo.value)
            nodo = nodo.next

    tiempo = 0
    pasados = 0
    ultimo_tipo = None
    consecutivos = 0

    print("\n--- INICIO ---\n")

    while pasados < 6 and not colaSemaforo.is_empty():
        if colaRevision.len() == 3:
            print(f"{tiempo}s - Procesando revisión")
            while not colaRevision.is_empty():
                colaSemaforo.enqueue(colaRevision.dequeue())

        tamano = colaSemaforo.len()
        paso = False

        for _ in range(tamano):
            v = colaSemaforo.dequeue()

            if ultimo_tipo == v.tipo and consecutivos == 2:
                print(f"{tiempo}s - {v.placa} pospuesto")
                colaSemaforo.enqueue(v)
                continue

            if v.tipo == "camion" and v.prioridad > 3:
                colaRevision.enqueue(v)
                print(f"{tiempo}s - {v.placa} a revisión")
                paso = True
                break

            print(f"{tiempo}s - {v.placa} PASA")
            eliminar_de_via(v.placa)
            pasados += 1

            if ultimo_tipo == v.tipo:
                consecutivos += 1
            else:
                consecutivos = 1

            ultimo_tipo = v.tipo
            paso = True

            if v.tipo == "moto" and v.prioridad == 1 and not colaSemaforo.is_empty() and pasados < 6:
                v2 = colaSemaforo.dequeue()
                print(f"{tiempo}s - {v2.placa} PASA (doble)")
                eliminar_de_via(v2.placa)
                pasados += 1

                if ultimo_tipo == v2.tipo:
                    consecutivos += 1
                else:
                    consecutivos = 1

                ultimo_tipo = v2.tipo

            tiempo += 30
            break

        if not paso and not colaSemaforo.is_empty():
            v = colaSemaforo.dequeue()
            print(f"{tiempo}s - {v.placa} PASA (forzado)")
            eliminar_de_via(v.placa)
            pasados += 1
            ultimo_tipo = v.tipo
            consecutivos = 1
            tiempo += 30

    print("\n--- FIN ---\n")

# ================================
# MAIN (EJECUTA TODOS LOS PUNTOS DEL TALLER)
# ================================

def main():
    via = DoublyLinkedList()

    # ================================
    # CARGA INICIAL DE VEHÍCULOS
    # ================================
    via.append(Vehiculo("AAA111", "auto", 3))
    via.append(Vehiculo("BBB222", "moto", 1))
    via.append(Vehiculo("CCC333", "camion", 4))
    via.append(Vehiculo("DDD444", "auto", 2))
    via.append(Vehiculo("EEE555", "moto", 1))
    via.append(Vehiculo("OOO999", "camion", 4))
    via.append(Vehiculo("HHH666", "auto", 2))
    via.append(Vehiculo("KKK777", "moto", 1))
    via.append(Vehiculo("RRR888", "camion", 4))
    via.append(Vehiculo("XXX000", "auto", 2))

    print("\n" + "="*60)
    print("ESTADO INICIAL DE LA VÍA")
    print("="*60 + "\n")
    print(via)

    # ================================
    # PUNTO 2 - PASO PREFERENCIAL
    # ================================
    print("\n" + "="*60)
    print("PUNTO 2 - PASO PREFERENCIAL (MOTOS PRIORIDAD 1)")
    print("="*60 + "\n")

    paso_preferencial(via)
    print("Resultado:\n")
    print(via)

    # ================================
    # PUNTO 3 - ELIMINAR CAMIONES
    # ================================
    print("\n" + "="*60)
    print("PUNTO 3 - ELIMINAR CAMIONES CON PRIORIDAD MAYOR A 3")
    print("="*60 + "\n")

    eliminar_camiones(via)
    print("Resultado:\n")
    print(via)

    # ================================
    # PUNTO 4 - ACCIDENTE ENTRE DOS PLACAS
    # ================================
    print("\n" + "="*60)
    print("PUNTO 4 - ACCIDENTE ENTRE DDD444 Y XXX000")
    print("="*60 + "\n")

    accidente(via, "DDD444", "XXX000")
    print("Resultado:\n")
    print(via)

    # ================================
    # PUNTO 5 - INVERTIR LA VÍA
    # ================================
    print("\n" + "="*60)
    print("PUNTO 5 - INVERTIR LA VÍA (SI HAY MÁS AUTOS QUE MOTOS)")
    print("="*60 + "\n")

    invertir_via(via)
    print("Resultado:\n")
    print(via)

    # ================================
    # PUNTO 6 - REORGANIZAR POR PRIORIDAD
    # ================================
    print("\n" + "="*60)
    print("PUNTO 6 - REORGANIZAR LA VÍA POR PRIORIDAD")
    print("="*60 + "\n")

    reorganizar_via(via)
    print("Resultado:\n")
    print(via)

    # ================================
    # PUNTO 7 - SIMULACIÓN DEL SEMÁFORO
    # ================================
    print("\n" + "="*60)
    print("PUNTO 7 - SIMULACIÓN DEL SEMÁFORO")
    print("="*60)

    simular_semaforo(via)

main()
# ==============================================================
# SIMULADOR DE TRÁNSITO URBANO (VERSIÓN SIMPLE Y FÁCIL DE ENTENDER)
# Cumple todos los puntos del taller sin usar listas, diccionarios ni estructuras extra
# Solo se usan:
#   - Lista doblemente enlazada
#   - Cola (para el punto 7)
# ==============================================================


# ==============================================================
# NODO PARA LISTA DOBLEMENTE ENLAZADA
# Guarda un vehículo y los enlaces al nodo anterior y siguiente
# ==============================================================
class NodeD:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


# ==============================================================
# LISTA DOBLEMENTE ENLAZADA (LA VÍA PRINCIPAL)
# ==============================================================
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # PUNTO 1: insertar al final
    def append(self, value):
        new_node = NodeD(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.size += 1

    # mostrar la vía completa
    def __str__(self):
        result = ""
        current = self.head

        while current:
            result += str(current.value)
            if current.next:
                result += " <--> "
            current = current.next

        return result


# ==============================================================
# COLA (USADA EN EL PUNTO 7)
# ==============================================================
class Queue:
    def __init__(self):
        self.list = DoublyLinkedList()

    def enqueue(self, value):
        self.list.append(value)

    def dequeue(self):
        if self.list.head is None:
            return None

        value = self.list.head.value
        self.list.head = self.list.head.next

        if self.list.head:
            self.list.head.prev = None
        else:
            self.list.tail = None

        return value

    def is_empty(self):
        return self.list.head is None

    def length(self):
        return self.list.size


# ==============================================================
# CLASE VEHÍCULO
# ==============================================================
class Vehiculo:
    def __init__(self, placa, tipo, prioridad):
        self.placa = placa
        self.tipo = tipo
        self.prioridad = prioridad

    def __str__(self):
        return f"{self.placa} {self.tipo} {self.prioridad}"


# ==============================================================
# PUNTO 2: PASO PREFERENCIAL (motos prioridad 1 al frente)
# ==============================================================
def paso_preferencial(via):
    current = via.head
    last_moved = None

    while current:
        next_node = current.next

        if current.value.tipo == "moto" and current.value.prioridad == 1:

            # quitar el nodo de su posición
            if current.prev:
                current.prev.next = current.next
            else:
                via.head = current.next

            if current.next:
                current.next.prev = current.prev
            else:
                via.tail = current.prev

            # moverlo al inicio
            if last_moved is None:
                current.prev = None
                current.next = via.head

                if via.head:
                    via.head.prev = current

                via.head = current
            else:
                current.prev = last_moved
                current.next = last_moved.next

                if last_moved.next:
                    last_moved.next.prev = current

                last_moved.next = current

            last_moved = current

        current = next_node


# ==============================================================
# PUNTO 3: ELIMINAR CAMIONES PRIORIDAD > 3
# ==============================================================
def eliminar_camiones(via):
    current = via.head

    while current:
        next_node = current.next

        if current.value.tipo == "camion" and current.value.prioridad > 3:

            if current == via.head:
                via.head = current.next
                if via.head:
                    via.head.prev = None
                else:
                    via.tail = None

            elif current == via.tail:
                via.tail = current.prev
                via.tail.next = None

            else:
                current.prev.next = current.next
                current.next.prev = current.prev

        current = next_node


# ==============================================================
# PUNTO 4: ACCIDENTE ENTRE DOS PLACAS
# ==============================================================
def accidente(via, placa1, placa2):
    current = via.head
    nodo1 = None
    nodo2 = None

    while current:
        if current.value.placa == placa1:
            nodo1 = current
        if current.value.placa == placa2:
            nodo2 = current
        current = current.next

    if nodo1 is None or nodo2 is None:
        return

    actual = nodo1.next

    while actual and actual != nodo2:
        next_node = actual.next
        actual.prev.next = actual.next
        actual.next.prev = actual.prev
        actual = next_node


# ==============================================================
# PUNTO 5: INVERTIR SOLO SI HAY MÁS AUTOS QUE MOTOS
# ==============================================================
def invertir_via(via):
    autos = 0
    motos = 0

    current = via.head

    while current:
        if current.value.tipo == "auto":
            autos += 1
        elif current.value.tipo == "moto":
            motos += 1
        current = current.next

    if autos <= motos:
        return

    current = via.head

    while current:
        current.prev, current.next = current.next, current.prev
        current = current.prev

    via.head, via.tail = via.tail, via.head


# ==============================================================
# PUNTO 6: REORGANIZAR POR PRIORIDAD (1 a 5)
# ==============================================================
def reorganizar_via(via):
    new_head = None
    new_tail = None

    for p in range(1, 6):
        current = via.head

        while current:
            next_node = current.next

            if current.value.prioridad == p:

                # quitar
                if current.prev:
                    current.prev.next = current.next
                else:
                    via.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    via.tail = current.prev

                # agregar al final de nueva lista
                current.prev = new_tail
                current.next = None

                if new_tail:
                    new_tail.next = current
                else:
                    new_head = current

                new_tail = current

            current = next_node

    via.head = new_head
    via.tail = new_tail


# ==============================================================
# PUNTO 7: SIMULACIÓN DEL SEMÁFORO
# ==============================================================
def simular_semaforo(via):
    colaSemaforo = Queue()
    colaRevision = Queue()

    current = via.head

    # meter los primeros 6 vehículos en la cola
    for _ in range(6):
        if current:
            colaSemaforo.enqueue(current.value)
            current = current.next

    tiempo = 0
    pasaron = 0

    print("\n--- INICIO SEMÁFORO ---\n")

    while pasaron < 6 and not colaSemaforo.is_empty():
        v = colaSemaforo.dequeue()

        if v.tipo == "camion" and v.prioridad > 3:
            print(f"{tiempo}s - {v.placa} enviado a revisión")
            colaRevision.enqueue(v)
        else:
            print(f"{tiempo}s - {v.placa} PASA")
            pasaron += 1
            tiempo += 30

    print("\n--- FIN SEMÁFORO ---\n")


# ==============================================================
# MAIN (ejecuta todo automáticamente como pide el taller)
# ==============================================================
def main():
    via = DoublyLinkedList()

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

    print("\nVIA ORIGINAL:\n")
    print(via)

    paso_preferencial(via)
    print("\nPASO PREFERENCIAL:\n")
    print(via)

    eliminar_camiones(via)
    print("\nELIMINAR CAMIONES:\n")
    print(via)

    accidente(via, "DDD444", "XXX000")
    print("\nACCIDENTE:\n")
    print(via)

    invertir_via(via)
    print("\nINVERTIR VIA:\n")
    print(via)

    reorganizar_via(via)
    print("\nREORGANIZAR POR PRIORIDAD:\n")
    print(via)

    simular_semaforo(via)


main()

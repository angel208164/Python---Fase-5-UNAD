sesiones = [[1, 30, 2],[2, 50, 1],[3, 80, 3],[4, 220, 200],[5, 200, 80]]

id_cliente = int(input("Id del Cliente: \n"))

def clasificacion_compromiso():
    for cliente in sesiones:
        if cliente[0] == id_cliente:
            duracion, clicks = cliente[1], cliente[2]

            if duracion > 180 and clicks > 8:
                print(f"Id del Cliente: {id_cliente}\nClasificacion: Alto")
            elif duracion < 60 or clicks < 3:
                print(f"Id del Cliente: {id_cliente}\nClasificacion: Bajo")
            else:
                print(f"Id del Cliente: {id_cliente}\nClasificacion: Medio")
            return

clasificacion_compromiso()
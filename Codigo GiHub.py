# Oscar Alejandro Ramirez Rodriguez
# Simulador de atencion en un banco con una cola

#Suponemos que la forma de operar en el banco es dejar entrar cierta cantidad de
#personas, hasta que esa cantidad de personas no llega no se empieza a atender, 
#en el caso de que llegasen mas personas, deben esperar a que terminen con las
#personas que ya estan en la cola para poder ponerse en cola ellos, el maximo
#de personas que se atienden son de a 10

while True:

#Las personas empiezan a unirse a la cola de espera

    Cola_personas = []
    for i in range(10):
        nom = input('Escriba su nombre y espere a ser atendido\n')
        Cola_personas.append(nom)
        print('Su turno es el', len(Cola_personas))
    print(Cola_personas)

#Atencion de clientes
    if len(Cola_personas) == 10:
        for j in range(len(Cola_personas)):
            print('La persona con el turno',j+1, 'pase al cajero número 1')
            Cola_personas.pop(0)
    

















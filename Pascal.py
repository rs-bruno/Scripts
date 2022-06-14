import sys

def pascal(reng_prev, lines_left):
    '''Imprime lines_left lineas más del triangulo de pascal a partir de la linea reng_prev.
    
    Esta funcion requiere que se le pase una lista reng_prev, la cual dee contener el primer renglón a imprimir.
    '''
    if lines_left > 0:
        for i in range(0,len(reng_prev)):
            print(reng_prev[i], end=' ')
        print('\n')
        nuevo_reng = [1]
        for i in range(0, len(reng_prev) - 1):
            nuevo_reng.append(reng_prev[i] + reng_prev[i+1])
        nuevo_reng.append(1)
        pascal(nuevo_reng, lines_left -1)

list_ini = [1]
if __name__ == "__main__":
    if len(sys.argv) > 1:
        pascal(list_ini, int(sys.argv[1]))
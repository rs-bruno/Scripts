import sys

def codigoGray(cantidadNiveles):
    '''Imprime los codigos de Gray de cantidadNiveles de bits.
    
    Se espeta que cantidad niveles sea un entero n tal que n >= 1.'''
    if cantidadNiveles < 1:
        return
    nivel_actual = 2
    base_actual = 2
    renglones = [[0 for x in range(cantidadNiveles)]]
    reng2 = renglones[0].copy()
    reng2[cantidadNiveles-1] = 1
    renglones.append(reng2)
    print(*renglones[0], sep=' ')
    print(*renglones[1], sep=' ')
    while nivel_actual <= cantidadNiveles:
        for desp in range(2**(nivel_actual-1)): #el segundo nivel tiene 2 renglones, el tercero 4, el cuarto 8, etc.
            reng = []
            reng = renglones[base_actual - (desp+1)].copy()
            reng[cantidadNiveles - nivel_actual] = 1
            renglones.append(reng)
            print(*reng, sep=' ')
        base_actual = base_actual * 2
        nivel_actual = nivel_actual + 1

if __name__ == '__main__':
    if len(sys.argv) > 1:
        codigoGray(int(sys.argv[1]))
    else:
        codigoGray(4)
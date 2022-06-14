import sys

def histo(path):
    histograma = {0:0}
    s = open('salida.txt', 'w+')
    f = open(path, encoding='UTF-8')
    for line in f:
        words = line.split()
        for word in words:
            if len(word) in histograma:
                histograma[len(word)] = histograma[len(word)] + 1
            else:
                histograma[len(word)] = 1
    f.close()
    max_len = max(list(histograma))
    max_count = 0
    for x, y in histograma.items():
        if y > max_count:
            max_count = y
    for i in range(max_count, 0, -1):
        print(i, end = (len(str(max_count)) - len(str(i)) + 1)*' ', file = s)
        for j in range(max_len + 1):
            separador = len(str(j)) * ' '
            if j in list(histograma) and (histograma[j] >= i):
                print('X', end = separador, file = s)
            else:
                print(' ', end = separador, file = s)
        print(file = s)
    print(' ', end = (len(str(max_count))- len(str(' ')) + 1)*' ', file = s)
    print(*list(range(0, max_len + 1)), sep = ' ', end = ' ',file = s)
    s.close()

if __name__ == '__main__':
    if(len(sys.argv) > 1):
        histo(sys.argv[1])
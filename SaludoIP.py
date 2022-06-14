import os
import socket
import sys
import threading
import time

saludos = []
s = threading.Semaphore()

def atender_saludos():
  global saludos
  soc_receptor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  soc_receptor.bind(('',7777))
  while True:
    buff = soc_receptor.recv(2048).decode()
    buff.strip()
    s.acquire()
    saludos.append((time.localtime(), buff))
    s.release()

def enviar_saludo(receptor, texto=f'{socket.gethostname()} - Buenas!'):
  enc = texto.encode()
  if len(enc) > 2048:
    enc = enc[:2048]
  soc_envio = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  soc_envio.sendto(enc, (receptor, 7777))
  soc_envio.close()

def localtime_to_print(lt):
  return f'{lt[2]}/{lt[1]}/{lt[0]}, {lt[3]}:{lt[4]}:{lt[5]}'

if __name__ == '__main__':
  thrd_atencion = threading.Thread(target=atender_saludos, daemon=True)
  thrd_atencion.start()
  inp = ''
  while True:
    while not (inp == '1' or inp == '2' or inp == '3'):
      print('================================================================')
      print('1) Enviar saludo.')
      print('2) Mostrar saludos recibidos.')
      print('3) Salir.')
      inp = input('Seleccione una opcion: ')
    if inp == '1':
      inp = ''
      x = input('Ingrese texto del saludo: ')
      y = input('Ingrese nombre de host destinatario: ')
      if x != '':
        x = socket.gethostname() + ' - ' + x
        enviar_saludo(y, x)
      else:
        enviar_saludo(y)
    elif inp == '2':
      inp = ''
      if len(saludos) > 0:
        s.acquire()
        for saludo in saludos:
          print(localtime_to_print(saludo[0]), saludo[1], sep=', ')
        s.release()
      else:
        print('No hay saludos.')
    else:
        exit()
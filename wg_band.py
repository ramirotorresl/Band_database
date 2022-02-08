lista_de_notas={'F#1':123,'G1':13,'G#1':23,'A1':12,'A#1':1,'B1':2,'C1':0,'C#1':123,'D1':13,'D#1':23,'E1':12,'F1':1,'F#2':2,'G2':0,'G#2':23,'A2':12,'A#2':1,'B2':2,'C2':0,'C#2':12,'D2':1,'D#2':2,'E2':0,'F2':1,'F#3':2,'G3':0,'G#3':23,'A3':12,'A#3':1,'B3':2,'C3':0,'C#3':12,'D3':1,'D#3':2,'E3':0,'F3':1}

list(lista_de_notas)
#notas=['F1','G2','D1']
#dedos para F1, G2 y D1 son 1, 0 y 13
  
# Find fingers que funciona con lista de tres notas. Voy a meterla en class Part como method

# def find_fingerss(lista_x):
#   for nota in lista_x:
#     dedos=[]
#     print(lista_de_notas.get(nota))      
# print(find_fingerss(notas))
# print(lista_de_notas.get('G1'))

class Cancion:
    def __init__ (self, name, author, link=[]):
      self.link= link
      self.parts=[]
      self.name= name
      self.author= author

    def __repr__ (self):
      description= '{} by {}'.format(self.name, self.author)
      return description

    def add_part (self,part):
        self.parts.append(part)

class Part:
  def __init__ (self, name, cancion, notas, minuto=0):
    
    self.name = name
    self.song = cancion
    self.notes = notas
    self.minuto = minuto
    cancion.add_part(self)
    self.valves = []
    
    # Pego aca adentro find_fingers para que se llame sola cuando le definis las notas -al crear Part instance-. Despues le hago un call al method para que ya se append a valves.
    def find_fingers(self):
      for nota in self.notes:
        self.valves.append(lista_de_notas.get(nota))
    find_fingers(self)  
    
  def __repr__ (self):
    return '{} de {} '.format(self.name, self.song)

  def find_notes(self, lista_dedos):
    posibles_notas = []
    for dedo in lista_dedos:
      for nota, dedos in lista_de_notas.items():
        if dedo == dedos:
          posibles_notas.append(nota)
    print(posibles_notas)

  # def transpose(self,q):
  #   for nota in notas:
  #     transposed_index = []
  #     transposed_index.append(list(lista_de_notas).index(nota)+q)
  #     print(transposed_index)

  def transpose(self,q):
      transposed_part= []
      for nota in self.notes:
        if nota in lista_de_notas:
          transposed_index = list(lista_de_notas).index(nota)+q
          transposed_note = list(lista_de_notas)[transposed_index]
          transposed_part.append(str(lista_de_notas[transposed_note]))
        else:
          transposed_part.append(nota)  
      print('Trans '+str(q)+str(transposed_part))
        
# version que imprime nota y dedos: transposed_part.append(transposed_note+' '+str(lista_de_notas[transposed_note]))        

# CREACION DE CLASS INSTANCE: una_rosa_blanca y will_soon_be_a_woman
una_rosa_blanca=Cancion('Una Rosa Blanca','Ibrahim Maalouf','www.hola.com')
will_soon_be_a_woman=Cancion('Will soon be a woman','Ibrahim Maalouf')

# CREACION DE PART INSTANCE:intro (solo creandola se agrega a la cancion)
intro=Part('Introduccion', will_soon_be_a_woman, ['D1','G2','D1','G2','F1','E1'])
bajada=Part('Bajada', will_soon_be_a_woman, ['A2','A1','C#2'])

riff_urb=Part('Rif', una_rosa_blanca, ['B1','G#1','B1','C#1','D#1','/x2/','B1','C#1','C#1','B1','A#1','G#1','//', 'B1', 'C#1', 'C#1', 'A#1','/','F#2', 'E1', 'D#1','//','B1','C#1','D#1','E1','F#2','G#2','D#1','C#1','/','D#1','C#1','F#2','D#1','C#1','/','B1','A#1','G#1','///','D#1', 'E1', 'D#1', 'B1', 'D#1', 'B1', 'C#1', 'B1', 'G#1',])
print(will_soon_be_a_woman.parts)
print(intro.notes)
print(intro.valves)


# calleando la funcion find_notes de introB, me devuelve todas las posibles notas.
# introB.find_notes([123,23])
intro.transpose(2)
intro.transpose(8)
intro.transpose(-3)
print('\n')
riff_urb.transpose(2)
print('\n')
riff_urb.transpose(1)
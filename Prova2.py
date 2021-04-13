#atividade 1

def nota_aluno():
  nota1 = float(input('Digite a nota 1 do aluno: '))
  nota2 = float(input('Digite a nota 2 do aluno: '))
  nota3 = float(input('Digite a nota 3 do aluno: '))
  soma = nota1 + nota2 + nota3
  media = soma / 3
  return media


#atividade 2

def tamanho_lista():
  n = input('Digite o tamanho da lista: ')
  i = 0
  lista = []
  while i < int(n):
    i += 1
    usuarios = input('Digite aqui uma entrada: ')
    lista.append(int(usuarios))
  return lista


#atividade 3

entrada = input('Digite uma letra: ')
def menu(entrada):
  dicionario = {'a':'globo', 'b':'sbt'}
  if entrada == 'a':
    print(dicionario['a'])
  elif entrada == 'b':
    print(dicionario['b']
  elif entrada == 'z'
          quit()
        else:
          print('Invalido')
        return menu(entrada)
          
          
#atividade 4

def exercicio04():          
  media_dos_alunos = []
  reprovados = []
  i = 0
  while i < len(media_dos_alunos):
   if float(media_dos_alunos[i]) < 7;
      reprovados.append(media_dos_alunos[i])
   i += 1
if len(reprovados) > len(media_dos_alunos) * 0.25:
  return ('Professor Coxa')
else:
  return ('Professor Padrão')      

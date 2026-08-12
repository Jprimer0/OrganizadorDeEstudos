import os

pastas = {"Estudos/Python": ["Exercicios", "Projetos"], 
          "Estudos/Linux": ["Comandos", "Scripts"],
           "Estudos/Redes": ["TCP-IP", "Segurança"]
          }

for chave, valor in pastas.items():
    for item in valor:
        os.mkdir(chave + "/" + item) 
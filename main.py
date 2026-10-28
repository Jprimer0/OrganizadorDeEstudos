import os

pastas = {"Estudos/Python": ["Exercicios", "Projetos"], 
          "Estudos/Linux": ["Comandos", "Scripts"],
           "Estudos/Redes": ["TCP-IP", "Segurança"]
          }

for chave, valor in pastas.items():
    for item in valor:
        os.makedirs(chave + "/" + item, exist_ok=True)
            caminho = chave + "/" + item
              if not os.path.exists(caminho):
                  os.mkdir(caminho)
              else:
                  print(f"A pasta {caminho} já existe, pulando...")
 

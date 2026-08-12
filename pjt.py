
import os

lista_pastas = []

while True:
      sim_nao = input("deseja criar pastas? (s/n): ").lower().strip()
      if sim_nao == "s":
          print("ok, sera criado pastas")
          break           
          
      elif sim_nao == "n":
           print("ok, nao sera criado pastas")
           exit()
      else:
          print("Digite apenas 's' ou 'n'.")
          

print("digite o nome das pastas que deseja criar, separadas por virguras:")

#

while True:
    try:   

       
       nomes_pastas = [nome.strip() for nome in input("nome das pasta primcipal: ").split(",")]

       if not all(nome.isalpha() for nome in nomes_pastas):
           raise ValueError("O nome da pasta deve conter só letras. sem espaços ou numeros.")
       lista_pastas.extend([nome.strip() for nome in nomes_pastas])

       for lista in lista_pastas:
           os.mkdir(lista)
       print("nome valido")
       break   
    
    except ValueError as e:
        print("digite apenas letras, sem numeros", e)

#
subs = input("cria subpastas dentro das pastas criadas? (s/n): ").lower().strip()
if subs == "s":
    print("ok, sera criado subpastas")
elif subs == "n":
    print("ok, nao sera criado subpastas")
    exit()

while True:
    try:
        valor = int(input("quantas pastas deseja criar: "))
        break
    except ValueError:
        print("digite apenas numeros")
liste = []
for i in range(valor):
    while True:
          nome_pasta = input(f"Digite o nome da pasta {i + 1}: ").strip()
          if not nome_pasta.isalpha():
              print("O nome da pasta deve conter apenas letras. sem espaços ou numeros.")
              continue

          subpastas = [f"{pasta}/{subpasta}" for pasta in lista_pastas for subpasta in liste]
          
          liste.append(nome_pasta)
          os.mkdir(f"{lista_pastas[0]}/{liste[i]}")
          break
    
print("vocâ que cria aquivos txt/md na subpastas? (s/n): ")
while True:
    sim_nao = input("digite 's' para sim ou 'n' para nao: ").lower().strip()
    if sim_nao == "s":
        print("ok, sera criado aquivos txt/md")
        break

    elif sim_nao == "n":
        print("ok, nao sera criado aquivos txt/md")
        exit()

    else:
        print("Digite apenas 's' ou 'n'.")

nomes_arquivos = []

# um erro e que ele nao ta pegando a criação de aquivos txt e md,
# ele ta pegando apenas a criação de pastas, e o erro é que ele ta pegando a criação de pastas e aquivos txt/md juntos,
#  e nao separados, entao eu vou separar eles, e vou criar uma função para criar aquivos txt/md, e vou chamar essa função dentro do loop while True, 
# assim ele vai criar os aquivos txt/md dentro das pastas criadas.

while True:
    try:
        entrada = input("digite o nome dos aquivos que deseja criar, separados por virgulas: ").strip().lower()

        if entrada == "sair".lower():
           print("saindo do programa...")
           break

        nome_arquivo = [nome.strip() for nome in entrada.split(",")]
       


        if not all(nome.isalpha() for nome in nome_arquivo):
            raise ValueError("O nome do arquivo deve conter apenas letras. sem espaços ou numeros.")

        nomes_arquivos.extend(nome_arquivo)


        for arquivo in nomes_arquivos:
            with open(f"{lista_pastas}/{liste[i]}/{arquivo}.txt", "w") as arquivo_txt:
                arquivo_txt.write("")
                pass
        print("se que sair do programa digite 'sair' ou se nao quiser criar aquivos digite 'nao'")


        if entrada == "s".lower():
            print("ok, sera criado aquivos txt/md")
            break

        elif entrada == "n".lower():
            print("ok, nao sera criado aquivos txt/md")    
            exit()

            with open(f"{lista_pastas}/{liste[i]}/{arquivo}.md", "w") as arquivo_md:
                arquivo_md.write("")
                pass
            break
        print("\narquivos criados com sucesso!")

    except ValueError as e:
        print("digite apenas letras, sem numeros", e)
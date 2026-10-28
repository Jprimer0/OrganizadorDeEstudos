
import os

lista_pastas = []
liste = []


def proximo_comando():
            
    while True:
       escolha = input(" continua: (c), pular: (p), sair: (s): ").lower().strip()
       if escolha == "c":
          print("ok, sera criado pastas")
          return "continuar"           
          
       elif escolha == "p":
           print("ok, pastas sera puladas")
           return "pular"

       elif escolha == "s":
           exit()

       else:
           print("Digite apenas 'p', 'c' ou 's'.")
          

    
def criar_pastas():
    print("digite o nome das pastas que deseja criar, separadas por virguras:")
    while True:
      try:   

       
          nomes_pastas = [nome.strip() for nome in input("nome das pasta primcipal: ").split(",")]

          if not all(nome.isalpha() for nome in nomes_pastas):
             raise ValueError("O nome da pasta deve conter só letras. sem espaços ou numeros.")

          existe = False
                
          for lista in nomes_pastas:

              if os.path.exists(lista):
                  print(f"A pasta '{lista}' já existe. Por favor, crie uma pasta nova.")
                  existe = True
                  break

          if existe:
             continue

          lista_pastas.extend(nomes_pastas)

          for lista in nomes_pastas:
              os.mkdir(lista)
            
          print("nome valido")
          break   
    
      except ValueError as e:
         print("digite apenas letras, sem numeros", e)

def valores():
    while True:
        try: 
            valor = int(input("quantas pastas deseja criar: "))
            
            if valor <= 0:
               raise ValueError("O valor deve ser maior que zero.")
            
            break

        except ValueError:
            print("digite apenas numeros")  

    for i in range(valor):
        while True:
            nome_pasta = input(f"Digite o nome da pasta {i + 1}: ").strip()

            if not nome_pasta.isalpha():
                    print("O nome da pasta deve conter apenas letras. sem espaços ou numeros.")
                    continue
          
            existe = False

            for pasta in lista_pastas:
                camino = os.path.join(pasta, nome_pasta)

                if os.path.exists(camino):
                    print(f"A pasta '{camino}' já existe. Por favor, crie uma pasta nova.")
                    existe = True
                    break
                
            if existe:
                continue

            liste.append(nome_pasta)

            for pasta in lista_pastas:
                camino = os.path.join(pasta, nome_pasta)
                os.mkdir(camino) 
                          
            break
                  
#digite se quer criar aquivos txt/md nas subpastas
nomes_arquivos = []

def txt():

    while True:
        try:
           print("se que sair do programa digite 'sair' para encerrar o programa") 

           entrada = input("digite o nome dos aquivos que deseja criar, separados por virgulas: ").strip().lower()

           if entrada == "sair".lower():
            print("saindo do programa...")
            break

           nome_arquivo = [nome.strip() for nome in entrada.split(",")]
       
           while True:

            if not all(nome.isalpha() for nome in nome_arquivo):
                 raise ValueError("O nome do arquivo deve conter apenas letras. sem espaços ou numeros.")

            nomes_arquivos.extend(nome_arquivo)


            for arquivo in nomes_arquivos:
              camino = os.path.join(f"{lista_pastas}/{liste}")

              if not os.path.exists(camino):
                    print(f"A aquivo '{camino}' ja existe. Por favor, crie a arquivo novo.")
              else:
                 with open(os.path.join(f"{camino}", f"{arquivo}.txt" ), "w") as arquivo_txt:
                    arquivo_txt.write("")
                    pass
                 break
             
        except ValueError as e:
             print("digite apenas letras, sem numeros", e)

def txt2():
    while True:
     try: 
         print("se que sair do programa digite 'sair' para encerrar o programa") 
         
         
         entrada = input("digite o nome dos aquivos que deseja criar, separados por virgulas: ").strip().lower()

         if entrada == "sair".lower():
            print("ok saindo")
            break

         nome_arquivo = [nome.strip() for nome in entrada.split(",")]
               
        
        
         if not all(nome.isalpha() for nome in nome_arquivo):
             raise ValueError("O nome do arquivo deve conter apenas letras. sem espaços ou numeros.")

         nomes_arquivos.extend(nome_arquivo)


         while True:
            for arquivo in nomes_arquivos:
               if not os.path.exists(camino):
                print(f"A aquivo '{camino}' ja existe. Por favor, crie a arquivo novo.")
            else:
                camino = os.path.join(f"{lista_pastas}/{liste}")

            with open(os.path.join(f"{camino}", f"{arquivo}.md"), "w") as arquivo_md:
                 arquivo_md.write("")
                 pass
            break
     except ValueError as e:
             print("digite apenas letras, sem numeros", e)
    print("\narquivos criados com sucesso!")

def main():

    escolha = proximo_comando()

    if escolha == "continuar":
        criar_pastas()

    elif escolha == "pular":
        pass    

    escolha = proximo_comando()

    if escolha == "continuar":
        valores()

    elif escolha == "pular":
        pass    

    escolha = proximo_comando()

    if escolha == "continuar":
        txt()

    if escolha == "pular":
        pass

    escolha = proximo_comando()

    if escolha == "continuar":
        txt2()

    elif escolha == "pular":
        pass

if __name__ == "__main__":
    main()

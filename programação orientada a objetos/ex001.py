# 1. Crie um programa em Python usando dicionário que:
#  a. Crie uma agenda de tamanho fornecido pelo usuário que armazene o nome, telefone e e-mail dos contatos.
#  b. Faça a impressão de todos os contatos inseridos.
contatos={}
num_usuario=int(input("Informe o número de usuários que você irá cadastrar: "))
x=0
while x <num_usuario:
    nome=input("Informe o seu nome: ")
    telefone=int(input("Informe seu telefone: "))
    email=input("Informe o seu email: ")
    if "@" not in email:
        print("Email inválido")
        break
    else:
        contatos[nome]={
        "telefone":telefone,
        "email":email
}
    x+=1
print("\n--- Lista de contatos ---")
for nomes, dados in contatos.items():
    print(f"{nomes} - Telefone:{dados['telefone']} / email:{dados['email']}\n")



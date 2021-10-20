import sqlite3

MASTER_PASSWORD = "123456"

senha = input("Insira sua senha master: ")
if senha != MASTER_PASSWORD:
    print("Senha inválida! Encerrando...")
    exit()

# Não é preciso criar o arquivo, com o python você consegue criar
# automaticamente ao rodar o script pela primeira vez no diretório
# que estiver.
conn = sqlite3.connect('passwords.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS userS (
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
''')

def menu():
    print("******************************")
    print("* i : inserir nova senha     *")
    print("* l : listar serviços salvos *")
    print("* r : recuperar uma senha    *")
    print("* s : sair                   *")
    print("******************************")

# função para mostrar um serviço específico já cadastrado
# no banco
def get_service(service):
    cursor.execute(f'''
        SELECT username, password FROM users
        WHERE service = '{service}'
        ''')

    if cursor.rowcount == 0:
        print("Serviço não cadastrado(use 'l' para verificar os erviços).")
    else:
        for user in cursor.fetchall():
            print (user)

# cadastrar novos usuários
def insert_password(service, username, password):
    cursor.execute(f'''
        INSERT INTO users (service, username, password)
        VALUES('{service}', '{username}', '{password}')
        ''')
    conn.commit()

# função para mostar os serviços de cada usuário
def show_services():
    cursor.execute('''
        SELECT service FROM users;    
    ''')
    for service in cursor.fetchall():
        print(service)

# colocando as funções em prática
while True:
    menu()
    op = input("O que deseja fazer? ")
    if op not in ['i', 'l', 'r', 's']:
        print("Opção inválida!")
        continue

    if op == 's':
        break

    if op == 'l':
        show_services()
    
    if op == 'r':
        service = input('Qual o serviço para o qual quer a senha? ')
        get_service(service)

# sempre lembrando de fechar a conexão criada anteriormente
conn.close()
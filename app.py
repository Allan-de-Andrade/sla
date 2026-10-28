import mysql.connector
import bcrypt

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Allan2311@",
    database="usuarios"
)

cursor = conexao.cursor()
terminar_programa = False
def entrar(login: str, password: str):
    sql = "SELECT user, password FROM user WHERE login = %s"
    value = (login,)

    cursor.execute(sql, value)
    usuario = cursor.fetchone()

    if usuario is None:
        print("Credenciais inválidas!")
        return

    usernameRegistered, senha_hash = usuario

    senha_bytes = password.encode("utf-8")

    if isinstance(senha_hash, str):
        senha_hash = senha_hash.encode("utf-8")

    try:
        if bcrypt.checkpw(senha_bytes, senha_hash):
            print(f"Bem-vindo, {usernameRegistered}!")
        else:
            print("Credenciais inválidas!")
    except ValueError:
        print("A senha armazenada não é um hash bcrypt válido.")

def register(nome:str,login:str,password:str):
    if not nome or not login or not password:
        return 'Cade os dados filho de deus?'
    else:
        try:
            sql = "insert into user (user,login,password) value (%s,%s,%s)"
            val =(nome,login,bcrypt.hashpw(password.encode("utf-8"),bcrypt.gensalt()))
            cursor.execute(sql,val)
            conexao.commit()
            print("Cadastrro concluido com sucesso")
        except Exception:
            print("Ocorreu um erro ao tentar cadastrar no banco de dados tente novamente mais tarde")
def mostrar_usuarios():
    sql = "SELECT id,user,login FROM user"
    cursor.execute(sql)
    usuarios = cursor.fetchall()
    indice = 0
    for usuario in usuarios:
        print("=========================")
        print(f"id: {usuario[0]}")
        print(f"nome:{usuario[1]}")
        print(f"login: {usuario[2]}")
        print("=========================")
        indice +=1
def pegar_usuario_pelo_id(id:int):
    sql = "select * from user where id = %s"
    cursor.execute(sql,(id,))
    user = cursor.fetchone()
    return user;
def atualizar_usuario():
    id = input("Digite seu id, general:")
    user = pegar_usuario_pelo_id(id)
    
    if user is None:
        print("Usuário não encontrado!")
        return
        
    senha = input("Digite sua senha ai celestial:")
    senhaHash = user[3]
    
    if isinstance(senhaHash, str):
        senhaHash = senhaHash.encode("utf-8")
    if bcrypt.checkpw(senha.encode("utf-8"),senhaHash):
        sql = "update user set user =%s,login =%s, password=%s where id = %s"
        username = input("Digite seu novo username ai relampago amarelo:")
        senha = input("Digite sua nova senha ai mestre dos cosmos:")
        login = input("Digite seu novo login ai dragão guerreiro:")
        
        cursor.execute(sql,(username,login,senha,id))
        conexao.commit()
        print("ATUALIZADO COM SUCESSO MEU MAGNANIMO")

def excluir_usuario():
    id = input("Digite seu id, general:")
    user = pegar_usuario_pelo_id(id)
        
    if user is None:
        print("Usuário não encontrado!")
        return
            
    senha = input("Digite sua senha ai celestial:")



    senhaHash = user[3]

    if isinstance(senhaHash, str):
        senhaHash = senhaHash.encode("utf-8")

    if bcrypt.checkpw(senha.encode("utf-8"), senhaHash):
        response = input("""
        Você realmente deseja deletar sua conta?
        Se sim digite S, se não digite N
        """)

        if response.lower() == "s":
            sql = "DELETE FROM user WHERE id = %s"
            cursor.execute(sql, (id,))
            conexao.commit()
            print("DELETADO COM SUCESSO MEU MAGNANIMO")
        elif response.lower() == "n":
            print("Processo Cancelado")

        else:
            print("Caractere inválido")
    else:
        print("Senha incorreta!")

while not terminar_programa:
    opcao =  input("""
===SISTEMA DE USUARIOS ===
1- ENTRAR
2- CRIAR CONTA
3- LISTAR USUARIOS
4- ATUALIZAR USUARIO
5-EXCLUIR USUARIO
0- ENCERRAR
""")
    match opcao:
        case "1":
            login = input("Preciso do teu login abençoado:")
            password = input("Digite sua senha campeão:")
            entrar(login,password)
        case "2":
            nome = input("Digite teu nome ai patrão:")
            password = input("Meu consagrado digita sua senha ai:")
            login = input("Agora pra finalizar meu guerreiro coloca o login ai:")
            register(nome,login,password)
        case "3":
            mostrar_usuarios()
        case "4":
            atualizar_usuario()
        case "5":
            excluir_usuario()
        case "0":
            terminar_programa = True
        case _:
            break

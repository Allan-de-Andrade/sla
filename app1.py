import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="usuarios"
)

cursor = conexao.cursor()
# cursor.execute("""
#     INSERT INTO `user` (login, password, user)
#     VALUES (%s, %s, %s), (%s, %s, %s)
# """, ('kj', 'kj', 'kj', 'sl', 'sl', 'sl'))
conexao.commit()
cursor.execute("select * from user")
usuarios = cursor.fetchall()
for user in usuarios:
    print(f"id:{user[0]}")
    print(f"user:{user[1]}")
    print(f"login:{user[2]}")
    print(f"password:{user[3]}")
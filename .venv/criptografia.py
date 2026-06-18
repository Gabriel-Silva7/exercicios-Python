import bcrypt

senha = b"gabiru"
print(f"Bytes da senha {senha}")
salt = bcrypt.gensalt()
senha_cripto = bcrypt.hashpw(senha,salt)
print(f"Senha criptografada: {senha_cripto}")
import bcrypt

def password_hash(input_password):
    password = input_password.encode('utf-8')
    salt = bcrypt.gensalt(rounds=12)
    hashed_password = bcrypt.hashpw(password,salt).decode('utf-8')
    return hashed_password

def password_check(login_pass,register_pass):
    return bcrypt.checkpw(login_pass.encode('utf-8'),register_pass.encode('utf-8'))
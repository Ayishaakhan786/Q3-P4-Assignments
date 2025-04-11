import hashlib

# Function to hash a password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Example stored logins: emails mapped to hashed passwords
stored_logins = {
    "ayisha@example.com": hash_password("my_secure_password123"),
    "admin@example.com": hash_password("admin_pass"),
    "user@example.com": hash_password("letmein")
}

# Function to check login
def login(email, password_to_check):
    if email in stored_logins:
        return stored_logins[email] == hash_password(password_to_check)
    else:
        return False

# Example usage
email_input = input("Enter your email: ")
password_input = input("Enter your password: ")

if login(email_input, password_input):
    print("Login successful! ✅")
else:
    print("Invalid email or password. ❌")
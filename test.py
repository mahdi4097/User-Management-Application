import bcrypt


def hash_password(func):
    def wrapper(*args, **kwargs):
        # Check if password is in kwargs
        if 'password' in kwargs:
            password = kwargs['password']
        else:
            # Check if password is the last item in args
            password = args[-1] if len(args) > 0 else None

        if password:
            hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            # Update password in kwargs or args
            if 'password' in kwargs:
                kwargs['password'] = hashed
            else:
                args = list(args)
                args[-1] = hashed
                args = tuple(args)

        return func(*args, **kwargs)

    return wrapper


def verify_password(stored_password, provided_password):
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password)


@hash_password
def create_user(username, password):
    # Here, the password will be hashed
    print(f"Username: {username}, Password: {password}")
    return password  # Return the hashed password for verification


# Example usage
hashed_password = create_user("user1", "mysecretpassword")

# Verify the password
is_correct = verify_password(hashed_password, "mysecretpassword")
print(f"Password is correct: {is_correct}")

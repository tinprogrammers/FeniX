# fenix/extensions/middleware/auth.py

def auth_required(func):
    def wrapper(*args, **kwargs):
        # Dummy check (you'll replace with real session or header check)
        user_is_authenticated = True

        if not user_is_authenticated:
            return "⛔ Access denied! Please login."

        return func(*args, **kwargs)

    return wrapper

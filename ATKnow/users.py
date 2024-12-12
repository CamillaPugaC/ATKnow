from models import User 
users = []
def create_user(name,email):
    user = User(name,email)
    users.append(user)
    return user 

def get_users():
    return users

def get_user_by_id(user_id):
    for user in users:
        if user['id'] == user_id:
            return user
        return None
    
def update_user(user_id,updates):
    user = get_user_by_id(user_id)
    if user:
        user.update(updates)
        return user
    return None 

def delete_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        user.delete(user)
        return True
    return False 

new_user = create_user("Juan Pérez", "juan@example.com")
print(new_user)

all_users = get_users()
print(all_users)

updated_user = update_user(new_user['id'], {'name': 'Juanito Pérez'})
print(updated_user)

deleted = delete_user(new_user['id'])
print(deleted)
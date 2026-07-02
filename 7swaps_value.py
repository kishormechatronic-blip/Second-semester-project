user_database = {101: 'admin_user', 102: 'dev_guy', 103: 'guest_99'}
database_swap={value:key for (key ,value) in user_database.items()}
print(database_swap)
# These are the following issues here:
# 1. It is mentioned in the prompt that there should not be any comments unless specified which has not been followed as there is a comment "# Add new user to DataFrame."
# 2. While comparing the password it should be user.password == password, but the model has just written password == password, which is incorrect comparison.
# 3. Once the password is correct, the failed attempts should not be increased, which is currently getting increased right now. 
#     `user.increment_failed_attempts()` -> This line should not be there in the password comparison if block.
# 4. When the password doesn't matches, it goes to the else block, where the code is resetting the failed attempts instead of incrementing it.
#     So, instead of "user.reset_failed_attempts()" it should be "user.increment_failed_attempts()"
# 5. The failed attempts should be zero initially, while registering the user, instead of 3.
#     So, instead of  "failed_attempts_left": [3], it should be  "failed_attempts_left": [0], 
# 6. User should not be converted to lowercase. 
#     Instead of user_row = self.users[self.users['username'].str.lower() == username.lower()] it should be user_row = 
#     self.users[self.users['username'] == username].
# 7.  As instructed in the prompt, it should first login thrice with neena, 
#     "auth_system.login("neena", "password321")  
#       auth_system.login("Neena", "password123")  
#       auth_system.login("neena", "password123") "
#     and twice with helios,
#      "auth_system.login("helios", "password321")
#       auth_system.login("helios", "mysecurepassword")"

#   but it has logged in four times with neena and once with helios,

# "auth_system.login("neena", "password321")  
#  auth_system.login("Neena", "password123")  
#  auth_system.login("neena", "password321")  
#  auth_system.login("neena", "password123")   
#  auth_system.login("helios", "mysecurepassword")"


import pandas as pd


class User:

    def __init__(self, user_id, username, password, failed_attempts=0, is_locked=False):

        self.user_id = user_id

        self.username = username

        self.password = password

        self.failed_attempts = failed_attempts

        self.is_locked = is_locked



    def reset_failed_attempts(self):

        self.failed_attempts = 0

        print(f"Failed attempts reset for user {self.username}.")



    def increment_failed_attempts(self):

        self.failed_attempts += 1

        print(f"Failed attempts for {self.username}: {self.failed_attempts}")

        if self.failed_attempts >= 3:

            self.lock_account()



    def lock_account(self):

        self.is_locked = True

        print(f"Account for {self.username} has been locked due to too many failed login attempts.")



class AuthenticationSystem:

    def __init__(self):

        self.users = pd.DataFrame(columns=["user_id", "username", "password", "failed_attempts_left", "is_locked"])



    def register_user(self, user_id, username, password):

        new_user = User(user_id, username, password)

        self.users = pd.concat([self.users, pd.DataFrame({

            "user_id": [user_id], 

            "username": [username], 

            "password": [password], 

            "failed_attempts_left": [0], 

            "is_locked": [False]

        })], ignore_index=True) 

        print(f"User {username} registered successfully.")



    # Never alter this login function

    def login(self, username, password):

        user_row = self.users[self.users['username'] == username]

        if user_row.empty:

            print(f"User {username} not found.")

            return


        user = User(user_row['user_id'].values[0], user_row['username'].values[0], user_row['password'].values[0], 

                    user_row['failed_attempts_left'].values[0], user_row['is_locked'].values[0])

        
        if user.is_locked:

            print(f"Account for {username} is locked. Please contact support.")

            return


        if user.password == password:

            user.reset_failed_attempts()

            self.update_user(user)

            print(f"User {username} logged in successfully.")

        else:

            user.increment_failed_attempts()

            self.update_user(user)



    def update_user(self, user):

        self.users.loc[self.users['username'] == user.username, 'failed_attempts_left'] = user.failed_attempts

        self.users.loc[self.users['username'] == user.username, 'is_locked'] = user.is_locked

        print(f"User {user.username}'s data updated.")



auth_system = AuthenticationSystem()

auth_system.register_user(1, "neena", "password123") 

auth_system.register_user(2, "helios", "mysecurepassword") 



auth_system.login("neena", "password321")  

auth_system.login("Neena", "password123")  

auth_system.login("neena", "password123")  

auth_system.login("helios", "password321")

auth_system.login("helios", "mysecurepassword")



# These are the following rewrites:
# 1. A comment "# Add new user to DataFrame."  has been removed from the code as its been mentioned not to use any comments unless specified.
# 2. While comparing the password it should be user.password == password, but the model has just written password == password, which is incorrect comparison, so `password == password` -> `user.password == password`.
# 3. Once the password is correct, the failed attempts should not be increased, which is currently getting increased right now. 
#     `user.increment_failed_attempts()` -> This line should not be there in the password comparison if block and so it has been removed from there.
# 4. When the password doesn't matches, it goes to the else block, where the code is resetting the failed attempts instead of incrementing it.
#     So, "user.reset_failed_attempts()" has been changed to "user.increment_failed_attempts()"
# 5. The failed attempts should be zero initially, while registering the user, instead of 3.
#     So, "failed_attempts_left": [3], has been changed to  "failed_attempts_left": [0], 
# 6. username should not be converted to lowercase. 
#     `user_row = self.users[self.users['username'].str.lower() == username.lower()]` has been changed to `user_row = 
#     self.users[self.users['username'] == username]`
# 7.  As instructed in the prompt, it should first login thrice with neena, and then twice with helios, so
# "auth_system.login("neena", "password321")  
#  auth_system.login("Neena", "password123")  
#  auth_system.login("neena", "password321")  
#  auth_system.login("neena", "password123")   
#  auth_system.login("helios", "mysecurepassword")"

# has been replaced with 

# auth_system.login("neena", "password321")  
# auth_system.login("Neena", "password123")  
# auth_system.login("neena", "password123")  
# auth_system.login("helios", "password321")
# auth_system.login("helios", "mysecurepassword")


# So, the four lines below has been replaced with the above 5 lines.
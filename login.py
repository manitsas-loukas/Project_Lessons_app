import streamlit as st
from utils import hash_password
from storage import load_users, save_users


def register_user(username, password):
    # είναι ο παλιός τρόπος, τώρα αποθηκεύονται σε json
    #users = st.session_state.users
    #2ος τρόπος με αποθήκευση σε json
    users = load_users()
    # εάν υπάρχει ήδη το username
    # τότε απέτυχε για αυτό βάζω False
    if username in users:
        return False
    users[username] = hash_password(password)
    save_users(users)
    return True


def login_user(username, password):
    
    # το ίδιο και εδώ με το register
    users = load_users() 
    return users.get(username) == hash_password(password)
















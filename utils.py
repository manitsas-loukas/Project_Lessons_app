import streamlit as st
import hashlib

# με το hash
# μετατρέπειένα password σε string

# password.encode()--> κείμενο σε bytes
# sha256() --> αλγόριθμος hash
# hexdigest() --> αποτέλεσμα σε string
# ουσιαστικά δεν αποθηκεύεται κανονικό password
def hash_password(password:str)-> str:
    return hashlib.sha256(password.encode()).hexdigest()

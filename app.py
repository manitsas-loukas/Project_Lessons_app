import streamlit as st
from login import login_user, register_user

st.set_page_config(page_title="Mathema App")

# logged in είναι μια μεταβλητή κατάστασης state
# οπότε το logged in δημιουργείται καθώς έχει συνδεθεί κάποιος
# αρχικοποίηση 
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# εάν δεν υπάρχει η σύνδεση τότε εμφάνισε Welcome
if not st.session_state.logged_in:
    st.header("Welcome")
    # μετά εμφανίζεται η φόρμα
    with st.form("Σύνδεση"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        action = st.selectbox("Action", ["Login", "Register"])
        submitted = st.form_submit_button("Submit")

    # εξαρτάται τι επιλέγω ως action
    if submitted:
        if action == "Login":
            # καλείται από το αρχείο login
            if login_user(username, password):
                # με το login το logged in γίνεται True!
                st.session_state.logged_in = True
                st.session_state.user = username
                st.success("Logged in Mathema!")
                st.rerun()# τρέχει ξανά το app 
		# και έτσι μπορεί μετά να κάνει show app 
            else:
                st.error("Wrong password or username!!!")

        if action == "Register":
            if register_user(username, password):
                if password == "" or username =="":
                    st.warning("Παρακαλώ, συμπλήρωσε τα στοιχεία σου!")
                elif len(password)<=6 or len(username)<=5:
                    st.warning("Το password πρέπει να αποτελείται τουλάχιστον από 6 αριθμούς/γράμματα/σύμβολα")
                    st.warning("Το username πρέπει να αποτελείται τουλάχιστον από 5 αριθμούς/γράμματα/σύμβολα")
                else:
                    st.success("Account created")
            else:
                st.error("User exists")

else:# οπότε πλέον το logged in είναι True  και μπορείς να μπει εδώ
    st.success(f"Welcome {st.session_state.user}")
    st.write("Select a page from the sidebar")


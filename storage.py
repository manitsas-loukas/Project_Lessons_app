import json
from pathlib import Path

USERS_FILE = Path("users.json")

'''
Η δουλειά του αρχείο load_users() είναι να διαβάζει
χρήστες σε ήδη υπάρχον αρχείο
ενώ...
το function save_users() τους αποθηκεύει και αν δεν 
υπάρχει το αρχείο τότε το δημιουργεί
'''

'''
Ενώ το δημιουργεί το αρχείο, φαίνεται κατεστρεμμένο καθώς δεν περιέχει ούτε {}
'''


def load_users():
    # αν υπάρχει στον δίσκο το αρχείο json
    if not USERS_FILE.exists():
        return {}
    try:
        with open(USERS_FILE, "r") as file:
            # ως περιεχόμενο διαβάζει το αρχείο file και διώχνει 
            # όλα τα κενά
            content = file.read().strip() 
            if content =="": # εάν είναι κενό
                return {}
            # διάβασε το αρχείο json και κάντο python object!
            # json to python dictionary
            # εάν βάλω μέσα στην αρένθεση content τότε πρέπει να βάλω
            # εκτός loads
            # εάν έχω μέσα file, θα πρέπει να βάλω load, γιατί
            # αδυνατεί να διαβάσει string παρά μόνο αρχείο            
            return json.loads(content)
    except json.JSONDecodeError:
        return {}# αποτρέπει πρώτο crash στο 1ο run


def save_users(users: dict):
    with open(USERS_FILE, "w") as file:
        # μετατρέπει python obj σε json!
        # ident=2 είναι μόνο για την εμφάνιση
        # δηλαδή να εμφανίζονται στην ίδια σειρά key:value, στην 
        # επόμενη σειρά να εμφανίζεται άλλο ζευγάρι
        json.dump(users, file, indent=2)






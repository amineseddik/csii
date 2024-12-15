import streamlit as st

def chiffrement_cloture(texte, k):
    # Supprimer les espaces et convertir en majuscules
    texte = texte.replace(' ', '').upper()
    
    # Créer les rails
    rails = [[] for _ in range(k)]
    rail = 0
    direction = 1
    
    for char in texte:
        rails[rail].append(char)
        rail += direction
        
        # Changer de direction aux extrémités
        if rail == 0 or rail == k - 1:
            direction *= -1
    
    # Aplatir les rails
    resultat = ''.join([''.join(rail) for rail in rails])
    
    # Diviser en mots de 5 caractères
    return ' '.join([resultat[i:i+5] for i in range(0, len(resultat), 5)])

def dechiffrement_cloture(texte, k):
    # Supprimer les espaces et convertir en majuscules
    texte = texte.replace(' ', '').upper()
    
    # Créer un modèle de placement
    modele = [[None] * len(texte) for _ in range(k)]
    rail = 0
    direction = 1
    
    # Marquer les positions des caractères
    for i in range(len(texte)):
        modele[rail][i] = '*'
        rail += direction
        
        if rail == 0 or rail == k - 1:
            direction *= -1
    
    # Placer les caractères
    index = 0
    for r in range(k):
        for c in range(len(texte)):
            if modele[r][c] == '*':
                modele[r][c] = texte[index]
                index += 1
    
    # Lire le message
    resultat = []
    rail = 0
    direction = 1
    
    for c in range(len(texte)):
        resultat.append(modele[rail][c])
        rail += direction
        
        if rail == 0 or rail == k - 1:
            direction *= -1
    
    # Diviser en mots de 5 caractères
    message_dechiffre = ''.join(resultat)
    return ' '.join([message_dechiffre[i:i+5] for i in range(0, len(message_dechiffre), 5)])

# Custom CSS for styling
st.markdown("""
<style>
.main {
    background-color: #000022;  /* Beige background */
}
.stApp {
    background-color: #F5DEB3;
}
.stTextInput > div > label,
.stNumberInput > div > label,
.stRadio > div > label {
    color: #FF0000;  /* Red color for subtitles */
    font-weight: bold;
    padding-bottom: 5px;
}
.stTextInput > div > div > input {
    background-color: white;
    color: black;
}
.stSelectbox > div > div > select {
    background-color: white;
    color: black;
}
h1 {
    color: #F5DEB3;  /* Navy blue for main title */
    text-align: center;
    font-family: 'Courier New', monospace;
}
</style>
""", unsafe_allow_html=True)

# Main App
def principal():
    st.title("🔐 Application de Chiffrement de Clôture")
    
    # Input columns
    col1, col2 = st.columns(2)
    
    with col1:
        texte = st.text_input("Saisir le texte", placeholder="Texte à chiffrer/déchiffrer")
    
    with col2:
        k = st.number_input("Nombre des niveaux", min_value=2, max_value=10, value=3)
    
    # Operation selection
    operation = st.radio("Sélectionner l'Opération", 
                         ["Chiffrement", "Déchiffrement"], 
                         horizontal=True)
    
    # Process button
    if st.button("Traiter", type="primary"):
        if not texte:
            st.warning("Veuillez saisir du texte")
        else:
            # Perform encryption or decryption
            if operation == "Chiffrement":
                resultat = chiffrement_cloture(texte, k)
                st.success("Texte Chiffré :")
            else:
                resultat = dechiffrement_cloture(texte, k)
                st.success("Texte Déchiffré :")
            
            # Display result in a code block
            st.code(resultat)

if __name__ == "__main__":
    principal()
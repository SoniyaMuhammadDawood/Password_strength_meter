import streamlit as st
import re
from PIL import Image

def check_password_strength(password):
    score = 0
    
    # Criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r"[A-Z]", password))
    number_criteria = bool(re.search(r"\d", password))
    special_char_criteria = bool(re.search(r"[@$!%*?&]", password))
    
    # Scoring
    score += length_criteria
    score += uppercase_criteria
    score += number_criteria
    score += special_char_criteria
    
    return score

def get_strength_label(score):
    if score == 4:
        return "Strong", "#4CAF50"  # Green
    elif score == 3:
        return "Moderate", "#FFC107"  # Yellow
    elif score == 2:
        return "Weak", "#FF9800"  # Orange
    else:
        return "Very Weak", "#F44336"  # Red

def main():
    st.set_page_config(page_title="Password Strength Meter", page_icon="🔒")
    
    # Apply background gradient
    st.markdown(
        """
        <style>
            [data-testid="stAppViewContainer"] {
                background: linear-gradient(to right, #FFDEE9, #B5FFFC);
                color: black;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Title and description
    st.title(" 🔒 Password Strength Meter")
    st.write("Enter a password to check its strength.")
    
    # Input field
    password = st.text_input("Enter Password:", type="password")
    check_button = st.button("Check Password Strength")
    
    if password and check_button:
        score = check_password_strength(password)
        strength_label, color = get_strength_label(score)
        
        # Display strength
        st.markdown(f"""<p style='color:white; background-color:{color}; padding:10px; border-radius:5px; text-align:center;'>
                    Password Strength: <b>{strength_label}</b></p>""", unsafe_allow_html=True)
        
        # Criteria checklist
        st.subheader("Password Criteria:")
        st.markdown(f"✅ At least 8 characters: {'✔️' if len(password) >= 8 else '❌'}")
        st.markdown(f"✅ Contains uppercase letter: {'✔️' if re.search(r'[A-Z]', password) else '❌'}")
        st.markdown(f"✅ Contains number: {'✔️' if re.search(r'\d', password) else '❌'}")
        st.markdown(f"✅ Contains special character (@$!%*?&): {'✔️' if re.search(r'[@$!%*?&]', password) else '❌'}")
    
    # Footer
    st.markdown("""---
    Built with ❤️ by Soniya""")
    
if __name__ == "__main__":
    main()

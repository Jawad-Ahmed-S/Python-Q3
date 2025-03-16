import streamlit as st;
st.title("Password Strength Meter")

st.markdown("Enter your password to check the strength of your password")

password = st.text_input("Enter your password",type = "password")
def check_UpperCase(s):
    for char in s:
        if char.isupper():
            return True
    return False

def check_LowerCase(s):
    for char in s:
        if char.islower():
            return True
    return False
def check_Digits(s):
    for char in s:
        if char.isdigit():
            return True
    return False
def check_SpecialCharacter(s):
    for char in s:
        if char.isalnum():
            return True
    return False

def check_password_strength(password):
    strength = 0
    feedback =[]
    if len(password) >= 8:
        strength+=1;
    else:
        feedback.append("Please enter minimum 8 characters")

    if(check_UpperCase(password)):
        strength+=1;
    else:
        feedback.append("Password should include atleast 1 Uppercase")

    if(check_LowerCase(password)):
        strength+=1;
    else:
        feedback.append("Password should include atleast 1 Lowercase")

    if(check_Digits(password)):
        strength+=1;
    else:
        feedback.append("Password should include atleast 1 Number")

    if(check_SpecialCharacter(password)):
        strength+=1;
    else:
        feedback.append("Password should include atleast 1 special Character")

    st.warning(feedback);
    if(strength == 5):
        st.success("Very Strong!")
    elif(strength>=3):
        st.warning("Moderate")
    else:
        st.error("Weak!")    

if  st.button("Check"):
    check_password_strength(password);
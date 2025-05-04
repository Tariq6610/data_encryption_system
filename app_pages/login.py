import streamlit as st
from auth import Users

def clear_form():
    page = st.query_params.get("page")
    if st.session_state.get("clear_form", False):
        fields = []
        if page == "signUp":
            fields = ["signUp_name", "signUp_password"]
        elif page == "signIn":
            fields = ["signIn_name", "signIn_password"]

        for field in fields :
            st.session_state[field] = ""
        st.session_state.clear_form = False

def validate_creditials(name , password):
    user = Users.get_user(name, password)
    if user:
        return True
    else:
        return False

def login_page():
    is_sign_in_page = st.query_params.get("page")

    if is_sign_in_page:
        col1, col2, col3 = st.columns([2, 1, 2])
        col_1, col_2, col_3 = st.columns([1, 4, 1])
        with col2:
            st.title("Login")
        with col_2:
            with st.form("login form"):
                name = st.text_input("Write Your Name", placeholder= "Name", key="signIn_name")
                password = st.text_input("Write Your Password", placeholder= "Password", type= "password", key="signIn_password")
                submit_btn = st.form_submit_button("Login")
                
            st.text("Don't have account")
            signUp_btn = st.button("SignUp")
            if signUp_btn:
                st.query_params["page"] = "signUp"
                st.rerun()
            
            if submit_btn:
                missing_fields = []
                if name and password:
                    if validate_creditials(name, password):
                        st.success("Login successful")
                    else:
                        st.error("Invalid credentials")

                if not name:
                    missing_fields.append("name")
                
                if not password:
                    missing_fields.append("password")

                if missing_fields:
                    st.error(f"Missing : {' ,'.join(missing_fields)}")



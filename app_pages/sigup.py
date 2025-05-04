import streamlit as st
from auth import Users

def add_user(name, password):
    user = Users(name, password)
    user_is_added = user.save_user()
    if user_is_added:
        return True
    else:
        return False

def signUp_page():
    is_signUp_page = st.query_params.get("page")

    if is_signUp_page:
        col1, col2, col3 = st.columns([2, 2, 2])
        col_1, col_2, col_3 = st.columns([1, 4, 1])
        with col2:
            st.title("SignUp")
        with col_2:
            with st.form("login form"):
                name = st.text_input("Write Your Name", placeholder= "Name", key="signUp_name")
                password = st.text_input("Write Your Password", placeholder= "Password", type= "password", key="signUp_password")
                submit_btn = st.form_submit_button("SignUp")
                
            st.text("already have account")
            signIn_btn = st.button("Login")
            

            if signIn_btn:
                st.query_params["page"] = "signIn"
                st.rerun()
          
            if submit_btn:
                missing_fields = []
                if name and password:
                    if add_user(name, password):
                        st.success("User added successful")
                        st.rerun()
                    else:
                        st.error("Name already exist")
                        st.info("Please Try different Name")
                
                if not name:
                    missing_fields.append("name")
                
                if not password:
                    missing_fields.append("password")

                if missing_fields:
                    st.error(f"Missing : {' ,'.join(missing_fields)}")

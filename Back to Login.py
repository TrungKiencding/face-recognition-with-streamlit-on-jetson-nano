import streamlit as st

st.set_page_config(initial_sidebar_state="collapsed")
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)
st.title("Welcome To Access Control System!")

lg = 'a'
ps = 'a'
with st.form(key='login_form'):
    login = st.text_input("Login")
    password = st.text_input("Password", type="password")
    submit_button = st.form_submit_button(label='Login')
    if submit_button:
        if login == lg and password == ps:
            st.switch_page("pages/Tracking.py")
        else: 
            st.warning('Account not access')

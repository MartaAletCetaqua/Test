import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
with open('credentials.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
name, authentication_status, username = authenticator.login('Login', 'main')
if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write('# Project name')
    st.write(f'Bienvenido {name}')
elif authentication_status == False:
    st.error('El nombre de usuario o contraseña es incorrecto')
elif authentication_status == None:
    st.warning('Porfavor introduzca su nombre de usuario y contraseña')
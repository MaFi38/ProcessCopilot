from datetime import datetime as dt
import streamlit as st
import uuid
from components.sidebar import display_sidebar
from components.chat_interface import display_chat_interface
from components.auth import main
from components.sidebar import display_sidebar
from components.chat_interface import display_chat_interface
from components.utils import create_new_session, switch_session
from components.api_utils import user_chat_history
from components.document import display_documents

st.title("PoC Copilot")

# Initialize session state variables
if "sessions" not in st.session_state:
    st.session_state.sessions = {}
if "current_session" not in st.session_state:
    st.session_state.current_session = None
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    main()
else:
    

    display_sidebar(create_new_session, switch_session)
    display_chat_interface()
    display_documents()


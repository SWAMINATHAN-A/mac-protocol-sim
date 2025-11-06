import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Developed By",
    page_icon="👥",
    layout="wide"
)

# Sidebar navigation links (from your code)
st.sidebar.page_link('Home.py', label='Home')
st.sidebar.page_link('pages/CSMA_CD.py', label='CSMA/CD')
st.sidebar.page_link('pages/Slotted_Aloha.py', label='Slotted_Aloha')
st.sidebar.markdown("---")

# Custom CSS for the header
st.markdown("""
<style>
    .page-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

st.divider()

col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
with col1:
    if st.button("Home", use_container_width=True):
        st.switch_page("Home.py")
with col2:
    if st.button("Download", use_container_width=True):
        st.switch_page("pages/Download.py")
with col3:
    if st.button("Help", use_container_width=True):
        st.switch_page("pages/Help.py")
with col4:
    if st.button("Learn", use_container_width=True):
        st.switch_page("pages/Learn.py")
with col5:
    if st.button("Developed by", use_container_width=True):
        st.switch_page("pages/Developed_by.py")

st.divider()

st.markdown("""
<div class="page-header">
    <h1>Developed By</h1>
</div>
""", unsafe_allow_html=True)


st.markdown("## Project Team Members")

team_members = [
    {"name": "Katyayni Aarya", "reg_no": "24BCE1543", "photo": "images/me.png"},
    {"name": "Suyesha Saha", "reg_no": "24BCE1962", "photo": "images/suyesha.jpg"}
]

for member in team_members:
    with st.container(border=True):
        col1, col2 = st.columns([1, 3])
        
        with col1:
            try:
                st.image(member['photo'], width=150)
            except Exception as e:
                st.error(f"Could not load image: {member['photo']}")
                st.caption("Please check the file path.")

        with col2:
            st.subheader(member['name'])
            st.markdown(f"**Registration No:** {member['reg_no']}")
    
    st.write("") 
st.divider()


st.markdown("## Project Guide")

guide_info = {
    "name": "Dr. Swaminathan Annadurai",
    "title": "Professor, School of Computer Science",
    "photo": "images/guide.jpg"
}

with st.container(border=True):
    col1, col2 = st.columns([1, 3])
    
    with col1:
        try:
            st.image(guide_info['photo'], width=150)
        except Exception as e:
            st.error(f"Could not load image: {guide_info['photo']}")
            st.caption("Please check the file path.")
    
    with col2:
        st.subheader(guide_info['name'])
        st.markdown(f"**{guide_info['title']}**")
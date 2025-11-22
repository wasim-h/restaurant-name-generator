import streamlit as st
import restaurant_chain as cr

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox(
    "Pick a Cuisine", 
    ("Indian", "Italian", "Chinese", "Mexican", "Arabic", "American"),
    index=None,
    placeholder="Select a cuisine..."
)

    
if cuisine:
        response = cr.get_name_menu(cuisine)
        
        st.header(f"Top 5 {cuisine} Restaurant Names")
        
        if 'restaurant_names' in response:
            names = response['restaurant_names'].split(",")
            for name in names:
                st.write("•", name.strip())
        
        st.write("---") 
        st.header("Suggested Menu")
        
        if 'menu_items' in response:
            menu_items = response['menu_items'].split(",")
            for item in menu_items:
                st.write("-", item.strip())
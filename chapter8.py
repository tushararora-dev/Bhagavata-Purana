import streamlit as st
from app import create_image_text_layout   # reuse function from main.py

def display_content():

    st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bungee+Spice:wght@700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Beth+Ellen&display=swap');
    h2 {
        font-family: 'Bungee Spice', cursive !important;
        font-size: 45px;
        text-align: center;
        color: #e7b66c !important;
    }
    .stMainBlockContainer{
        padding-top: 0rem; !important}
    p, li { 
        font-size: 18px !important;
        # line-height: 1.6 !important;
        text-align: justify !important;
        color: oldlace;
    }

    .st-emotion-cache-1gcegfv h2 {
    font-size: 1.5rem;
    }
    table {
        border-collapse: collapse;
        width: 100%;
    }

    td {
        border: 2px solid #444 !important;
        padding: 5px;
        font-size: 16px !important;
        line-height: 1.2 !important;
        text-align: justify !important;
        color: oldlace;
        background-color: #6969691f; /* dark background to contrast oldlace */
    }


    .beth1 {
            font-family: 'Beth Ellen', cursive !important; /* <-- use Beth Ellen (imported) */
            font-size: 22px;
            color: oldlace !important;
            text-align: center !important;
            margin-top: 0.2em;
            color: dimgray !important;
        }

    </style>
    """,
    unsafe_allow_html=True
    )
    create_image_text_layout("attached_assets/chapter8/chapter8.jpg", layout="full")
    # Book 8 - Eighth Skandha
    text0 = """
    <h2>Book 8 - Eighth Skandha</h2>
    """
    # Book 8 - Eighth Skandha

    # Book 8 - Eighth Skandha

    # Chapter 1
    with st.expander("Chapter 1 - Description of Manvantaras"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter8/8.1.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 2
    with st.expander("Chapter 2 - The Elephant Leader seized by the Alligator"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter8/8.2.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 3
    with st.expander("Chapter 3 - The Liberation of the Mighty Elephant"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter8/8.3.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4
    with st.expander("Chapter 4 - Liberation of the Lord of Elephants"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter8/8.4.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 5
    with st.expander("Chapter 5 - Description of Fifth and Sixth Manvantaras—Brahmā Hymns the Lord"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter8/8.5.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6
    with st.expander("Chapter 6 - Mount Mandara Transported for Churning the Ocean"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter8/8.6.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7
    with st.expander("Chapter 7 - The Churning of the Sea for Nectar"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter8/8.7.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 8
    with st.expander("Chapter 8 - The Lord’s Manifestation as Mohinī (The Enchantress)"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter8/8.8.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 9
    with st.expander("Chapter 9 - Distribution of Nectar by Mohinī"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter8/8.9.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 10
    with st.expander("Chapter 10 - A Battle between Gods and Asuras"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter8/8.10.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 11
    with st.expander("Chapter 11 - End of the Battle Between Gods and Asuras at Nārada’s Mediation"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter8/8.11.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 12
    with st.expander("Chapter 12 - Lord Śiva Fascinated by Mohinī"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter8/8.12.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 13
    with st.expander("Chapter 13 - Description of the Future Manvantaras"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter8/8.13.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 14
    with st.expander("Chapter 14 - Duties of Manus and Their Functionaries"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter8/8.14.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 15
    with st.expander("Chapter 15 - Bali’s Conquest of the Svarga (Celestial Region)"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter8/8.15.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 16
    with st.expander("Chapter 16 - Instruction in the observance of Payovrata to Aditi"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter8/8.16.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 17
    with st.expander("Chapter 17 - The Manifestation of the Lord as Vāmana"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter8/8.17.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 18
    with st.expander("Chapter 18 - The Lord incarnates as Vāmana. Visit to Bali’s sacrifice"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter8/8.18.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 19
    with st.expander("Chapter 19 - Vāmana’s request for three paces of Land—Śukra’s opposition"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter8/8.19.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 20
    with st.expander("Chapter 20 - Manifestation of the Cosmic Form by Viṣṇu"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter8/8.20.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 21
    with st.expander("Chapter 21 - Bali Bound Down"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter8/8.21.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 22
    with st.expander("Chapter 22 - A Dialogue between Bali and Vāmana"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter8/8.22.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 23
    with st.expander("Chapter 23 - Bali, free from bonds, enters Sutala"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter8/8.23.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 24
    with st.expander("Chapter 24 - The Fish Incarnation of Lord Viṣṇu"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter8/8.24.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")
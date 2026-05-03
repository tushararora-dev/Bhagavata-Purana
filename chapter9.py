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
    create_image_text_layout("attached_assets/chapter9/chapter9.jpg", layout="full")
    # Book 9 - Ninth Skandha
    text0 = """
    <h2>Book 9 - Ninth Skandha</h2>
    """


    # Book 9 - Ninth Skandha

    # Chapter 1
    with st.expander("Chapter 1 - The story of King Sudyunma"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter9/9.1.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 2
    with st.expander("Chapter 2 - History of Karūṣa and other four sons of Manu"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter9/9.2.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 3
    with st.expander("Chapter 3 - The story of Cyavana and Sukanyā"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter9/9.3.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4
    with st.expander("Chapter 4 - The Account of Nābhāga and Ambarīṣa"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter9/9.4.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 5
    with st.expander("Chapter 5 - Protection of Durvāsas—The story of Ambarīṣa Concluded"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter9/9.5.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6
    with st.expander("Chapter 6 - History of Ikṣvāku’s Posterity"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter9/9.6.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7
    with st.expander("Chapter 7 - The Story of King Hariścandra"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter9/9.7.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 8
    with st.expander("Chapter 8 - The Story of King Sagara"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter9/9.8.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 9
    with st.expander("Chapter 9 - The Descent of the Gaṅgā; The Story of Kalmāṣapāda"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter9/9.9.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 10
    with st.expander("Chapter 10 - The Story of Rāma"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter9/9.10.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 11
    with st.expander("Chapter 11 - The Story of Rāma (concluded)"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter9/9.11.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 12
    with st.expander("Chapter 12 - The Description of Ikṣvāku’s Race (concluded)"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter9/9.12.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 13
    with st.expander("Chapter 13 - The Description of the Race of Nimi"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter9/9.13.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 14
    with st.expander("Chapter 14 - The Description of the Lunar Race"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter9/9.14.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 15
    with st.expander("Chapter 15 - The Story of Paraśurāma—Sahasrārjuna Slain"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter9/9.15.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 16
    with st.expander("Chapter 16 - The Story of Paraśurāma (concluded)"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter9/9.16.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 17
    with st.expander("Chapter 17 - The Lunar Dynasty—The Descendants of Āyu, the Son of Purūravas"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter9/9.17.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 18
    with st.expander("Chapter 18 - The History of Nahuṣa’s Line—The Story of Yayāti"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter9/9.18.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 19
    with st.expander("Chapter 19 - Yayāti’s Retirement and Final Emancipation"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter9/9.19.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 20
    with st.expander("Chapter 20 - The History of Pūru’s race—Birth of Bharata"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter9/9.20.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 21
    with st.expander("Chapter 21 - The Race of Bharata—The History of Rantideva"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter9/9.21.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 22
    with st.expander("Chapter 22 - The Royal Dynasties of Pāñcāla, Magadha and Kuru"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter9/9.22.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 23
    with st.expander("Chapter 23 - The History of the Dynasties of Anu, Druhyu, Turvasu and Yadu"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter9/9.23.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 24
    with st.expander("Chapter 24 - The History of the Race of Yadu"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter9/9.24.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")
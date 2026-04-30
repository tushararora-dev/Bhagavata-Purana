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
        text1 = """ 
        Raja Parikshit ne rishi se poocha,
“Alag-alag Manu ke time ki kahani bataiye.”

Rishi Shuka ne shanti se jawab diya.

Unhone kaha,
“Har yug me ek Manu hota hai, jo duniya ko guide karta hai.”

“Har Manvantara me Bhagwan alag roop lekar aate hain.”"""
        create_image_text_layout(
            "attached_assets/chapter8/8.1.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Raja dhyaan se sun raha tha.

Rishi ne bataya,
“Pehle Manu ne sab kuch chhod kar tapasya ki.”

“Woh forest me jaakar ek pair par khade hokar dhyaan karte the.”

Unhone Bhagwan ko yaad kiya aur unki stuti ki.

Phir unhone ek important baat samjhayi,

“Bhagwan har jagah hain.”

“Woh sabke andar rehte hain.”

“Woh sabko dekhte hain, lekin unhe koi nahi dekh sakta.”

Raja ko yeh baat interesting lagi.

Rishi ne aage kaha,
“Insaan ko jo milta hai, usme santosh rehna chahiye.”

“Dusron ki cheez par lalach nahi karna chahiye.”

Phir unhone bataya,

“Bhagwan sab kuch create bhi karte hain aur control bhi.”

“Lekin woh khud in sab se alag rehte hain.”

“Isliye jo log unka raasta follow karte hain,
woh dukhi nahi hote.”

Raja ko sab samajh aane laga.

Rishi ne phir bataya,
“Jab Manu tapasya kar rahe the, tab asur un par attack karne aaye.”

“Tab Bhagwan ne unki raksha ki aur asuron ko hara diya.”

Phir unhone alag-alag Manus aur unke yug ke baare me bataya.

Har yug me naye raja, naye devta aur naye rishi hote hain.

Aur har baar Bhagwan kisi na kisi roop me aate hain.

Raja Parikshit aur bhi sunna chahta tha.

Usne poocha,
“Woh elephant wali kahani kya hai?”

Rishi muskuraaye.

Woh ek aur interesting kahani shuru karne wale the.

Moral:
Bhagwan har yug me sabki raksha karte hain, aur jo un par vishwas rakhta hai, woh kabhi akela nahi hota."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 2
    with st.expander("Chapter 2 - The Elephant Leader seized by the Alligator"):
        text1 = """ 
        Rishi ne ek nayi kahani shuru ki.

Ek bahut sundar pahaad tha—Trikuta.

Uske paas ek bada sa lake tha,
jo phool aur kamal se bhara hua tha."""
        create_image_text_layout(
            "attached_assets/chapter8/8.2.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Wahan birds gaate the,
aur hawa me meethi khushboo hoti thi.

Ek din ek bada sa haathi wahan aaya.

Woh apne poore group ke saath tha.

Woh sabko lead kar raha tha.

Sab usse respect karte the.

Garmi se pareshaan hokar,
woh paani ke paas gaya.

Usne paani piya aur fresh feel kiya.

Phir usne apne family ko bhi paani pilaya.

Sab enjoy kar rahe the.

Lekin achanak ek alligator ne uska pair pakad liya.

Sab shock ho gaye.

Haathi ne poori strength se fight ki.

Uske friends bhi usse bachane lage.

Lekin koi bhi usse chhuda nahi paaya.

Fight bahut long time tak chali.

Dheere-dheere haathi weak hone laga.

Alligator paani me strong tha.

Ab haathi helpless ho gaya.

Usne samjha,
“Ab koi meri help nahi kar sakta.”

Phir usne Bhagwan ko yaad kiya.

Usne dil se prarthana ki,

“Hey Bhagwan, mujhe bachaiye!”

Uska mann ab pure ho gaya tha.

Woh sirf Bhagwan par depend kar raha tha.

Moral:
Jab sab raaste band ho jaate hain, tab sachchi shraddha aur Bhagwan par vishwas hi hume bachata hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 3
    with st.expander("Chapter 3 - The Liberation of the Mighty Elephant"):
        text1 = """ 
        Haathi ne dil se Bhagwan ko yaad kiya.

Ab woh sirf apni strength par nahi,
Bhagwan par depend kar raha tha.

Usne mann me prarthana ki,
“Hey Bhagwan, aap hi meri last hope ho.”

Woh apni purani yaadon se ek prayer yaad kar raha tha."""
        create_image_text_layout(
            "attached_assets/chapter8/8.3.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Usne Bhagwan ko yaad karte hue kaha,
“Aap sabke creator ho.”

“Aap sab jagah ho.”

“Aap hi sabko control karte ho.”

Haathi ka mann ab bilkul pure ho gaya tha.

Usse apni life ka sach samajh aa gaya.

Usne socha,
“Mujhe sirf bachna nahi hai…”

“Mujhe sachchi mukti chahiye.”

Yeh ek deep realization tha.

Tabhi achanak aasman me ek divine scene dikha.

Bhagwan Vishnu Garuda par baith kar aa rahe the.

Unke haath me Sudarshan chakra tha.

Sab devta unki stuti kar rahe the.

Haathi ne mushkil se apni trunk uthayi.

Usne ek kamal phool Bhagwan ko offer kiya.

Aur kaha,
“Hey Narayan, main aapko pranam karta hoon!”

Bhagwan turant uske paas aa gaye.

Unhone dekha ki haathi bahut dukh me hai.

Unhone delay nahi kiya.

Woh turant Garuda se utar gaye.

Aur haathi ko paani se bahar nikala.

Phir apne chakra se alligator ko maar diya.

Haathi free ho gaya.

Uski life bach gayi.

Sab devta yeh dekh kar hairaan reh gaye.

Bhagwan ne apne bhakt ko bacha liya.

Moral:
Jab bhakti sachchi aur pure hoti hai, tab Bhagwan khud aakar apne bhakt ki raksha karte hain."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4
    with st.expander("Chapter 4 - Liberation of the Lord of Elephants"):
        text1 = """ 
        Bhagwan Vishnu ne jab haathi ko bachaya,
toh sab devta bahut khush ho gaye.

Aasman se phool barasne lage.

Gandharv gaane lage,
aur sab Bhagwan ki tareef karne lage."""
        create_image_text_layout(
            "attached_assets/chapter8/8.4.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Tab ek amazing cheez hui.

Jo alligator tha,
woh apne asli roop me aa gaya.

Woh ek Gandharva tha,
jo shraap ki wajah se alligator bana hua tha.

Bhagwan ne use bhi free kar diya.

Woh thankful hokar wapas apne lok chala gaya.

Ab haathi ke saath bhi ek miracle hua.

Bhagwan ke touch se
uski ignorance khatam ho gayi.

Usse apni asli pehchaan yaad aa gayi.

Woh pehle ek raja tha—Indradyumna.

Ek shraap ki wajah se woh haathi bana tha.

Lekin uski bhakti ne use bachaa liya.

Ab usse ek divine roop mil gaya.

Woh Bhagwan ke paas chala gaya.

Sab log yeh dekh kar hairaan reh gaye.

Bhagwan apne bhakt ko sirf bachate nahi,
unhe upar bhi le jaate hain.

Phir Bhagwan Vishnu wapas apne dham chale gaye.

Jaate waqt unhone ek important baat kahi,

“Jo log subah uthkar mujhe yaad karte hain,
aur yeh kahani sunte hain,
unhe kabhi darr nahi hota.”

“Unka mann clear rehta hai.”

Yeh sun kar sab log aur bhi inspired ho gaye.

Moral:
Sachchi bhakti sirf problems solve nahi karti,
balki insaan ko highest level tak le jaati hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 5
    with st.expander("Chapter 5 - Description of Fifth and Sixth Manvantaras—Brahmā Hymns the Lord"):
        text1 = """ 
        Rishi ne kaha,
“Ab main tumhe ek aur important kahani batata hoon.”

Unhone bataya ki har yug me alag-alag Manu hote hain.

Ek Manu tha—Raivata."""
        create_image_text_layout(
            "attached_assets/chapter8/8.5.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Uske time par bhi Bhagwan ne apna roop liya.

Unhone Vaikuntha naam ka divine lok create kiya.

Wahan sab log shanti aur khushi se rehte the.

Phir ek aur Manu aaya—Chakshusha.

Uske time par Bhagwan Ajita ke roop me aaye.

Us time ek badi problem ho gayi.

Devta aur Asur ke beech war chal raha tha.

Devta weak ho gaye the.

Unki power aur energy khatam ho rahi thi.

Sab tension me aa gaye.

Unhone milkar Brahma ji ke paas jaane ka decision liya.

Sab devta Brahma ji ke paas gaye.

Unhone apni problem batayi.

Brahma ji ne unki baat suni aur kaha,

“Ab sirf Bhagwan hi help kar sakte hain.”

“Chalo sab milkar unse madad maangte hain.”

Sab devta ready ho gaye.

Woh sab milkar Bhagwan ke paas gaye.

Brahma ji ne unki stuti ki.

Unhone kaha,
“Hey Bhagwan, aap sabke creator ho.”

“Aap sab jagah ho aur sabko control karte ho.”

“Hum sab aapki sharan me aaye hain.”

“Please hume bachaiye.”

Sab devta bhi prarthana karne lage.

Unka mann ab sirf Bhagwan par depend tha.

Ab sabko wait tha—
Bhagwan kya solution denge.

Moral:
Jab problem bahut badi ho, tab ego chhodkar milkar sahi madad lena hi sabse best solution hota hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6
    with st.expander("Chapter 6 - Mount Mandara Transported for Churning the Ocean"):
        text1 = """ 
        Devta bahut pareshaan the.
Unhone milkar Bhagwan se help maangi.

Tab achanak Bhagwan Vishnu unke saamne prakat hue.

Unki roshni itni strong thi ki sab kuch chamakne laga."""
        create_image_text_layout(
            "attached_assets/chapter8/8.6.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Devta unhe dekhkar hairaan reh gaye.

Sabne jhuk kar unhe pranam kiya.

Bhagwan ne unki problem samajh li.

Unhone calmly kaha,
“Tumhe ek plan follow karna hoga.”

Sab dhyaan se sunne lage.

Bhagwan ne kaha,
“Abhi tum asuron se fight mat karo.”

“Unke saath milkar kaam karo.”

Devta thoda surprised ho gaye.

Bhagwan ne samjhaya,
“Jab goal bada ho,
toh kabhi-kabhi dushman ke saath bhi teamwork karna padta hai.”

Phir unhone ek important plan bataya.

“Samundar ko churn karo.”

“Usme se amrit niklega.”

“Jo usse piyega, woh amar ho jayega.”

Sab excited ho gaye.

Bhagwan ne detail me bataya,

“Mandara parvat ko rod banao.”

“Vasuki naag ko rope banao.”

“Sab milkar samundar ko churn karo.”

“Main tumhari help karunga.”

Phir unhone warning di,
“Jo bhi niklega, us par greed mat dikhana.”

“Sab patiently wait karna.”

Itna kehkar Bhagwan gayab ho gaye.

Devta turant asuron ke paas gaye.

Unhone shanti se baat ki.

Asur maan gaye.

Ab sab milkar Mandara parvat ko uthakar samundar ki taraf le jaane lage.

Lekin parvat bahut heavy tha.

Sab thak gaye aur beech raste me gir gaye.

Kuch log uske neeche dab gaye.

Sab helpless ho gaye.

Tab Bhagwan Vishnu wapas aaye.

Unhone apni shakti se sabko theek kar diya.

Phir unhone easily parvat ko uthaya.

Use Garuda par rakhkar samundar tak le gaye.

Sab yeh dekh kar amazed ho gaye.

Ab sab ready the—
samundar ko churn karne ke liye.

Moral:
Bada goal achieve karne ke liye kabhi teamwork aur patience zaroori hota hai—even dushman ke saath bhi."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7
    with st.expander("Chapter 7 - The Churning of the Sea for Nectar"):
        text1 = """ 
        Devta aur asur milkar samundar ko churn karne lage.

Unhone Vasuki naag ko rope banaya
aur Mandara parvat ko ghumaane lage.

Sab milkar full power laga rahe the.

Lekin ek problem ho gayi."""
        create_image_text_layout(
            "attached_assets/chapter8/8.7.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Parvat paani me doobne laga.

Sab log tension me aa gaye.

Tab Bhagwan Vishnu ne ek naya roop liya.

Woh ek bade se kachhua ban gaye.

Unhone apni peeth par parvat ko support diya.

Ab churning smoothly chalne lagi.

Sab fir se energy ke saath kaam karne lage.

Lekin kuch time baad ek dangerous cheez bahar aayi.

Woh tha—zehreela poison, Halahal.

Woh itna powerful tha ki sab jagah phailne laga.

Sab log dar gaye.

Unhe laga sab kuch khatam ho jayega.

Tab sab Bhagwan Shiva ke paas gaye.

Unhone help maangi,
“Please hume bachaiye!”

Bhagwan Shiva ne sabki baat suni.

Unhone socha,
“Dusron ki raksha karna hi sabse bada dharm hai.”

Phir unhone bina dare poison pee liya.

Sab shock ho gaye.

Parvati ji ne bhi unka support kiya.

Poison unke gale me ruk gaya.

Isliye unka gala neela ho gaya.

Tab se unhe Neelkanth kaha jaata hai.

Sab log unki tareef karne lage.

Unhone sabko bachaa liya.

Sabka darr khatam ho gaya.

Moral:
Sacrifice aur dusron ki help karna hi sabse bada heroism hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 8
    with st.expander("Chapter 8 - The Lord’s Manifestation as Mohinī (The Enchantress)"):
        text1 = """ 
        Samundar ka manthan chal raha tha.
Poison ke baad ab achhi cheezein nikalne lagi.

Sabse pehle ek divine cow aayi—
jo sabki wishes poori karti thi.

Phir ek sundar white ghoda nikla."""
        create_image_text_layout(
            "attached_assets/chapter8/8.8.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Ek bada sa haathi bhi aaya—Airavata.

Phir ek chamakdar jewel nikla—Kaustubh.

Sab cheezein dekh kar sab amaze ho rahe the.

Phir ek special moment aaya.

Goddess Lakshmi samundar se prakat hui.

Sab log unhe dekh kar attract ho gaye.

Sab unhe apni taraf chahte the.

Lekin Lakshmi ne sabko dhyaan se dekha.

Unhone socha,
“Kaun sabse perfect hai?”

Finally unhone Bhagwan Vishnu ko choose kiya.

Unhone unhe mala pehnayi
aur unke paas khadi ho gayi.

Ab sab jagah khushi ka mahaul tha.

Lekin kahani yahin khatam nahi hui.

Thodi der baad ek aur person aaya—

Woh tha Dhanvantari,
jo amrit ka kalash lekar aaya.

Jaise hi asuron ne dekha,
woh turant amrit le gaye.

Sab devta shock ho gaye.

Unhe laga ab toh asur hi amar ho jayenge.

Devta Bhagwan Vishnu ke paas gaye.

Unhone help maangi.

Bhagwan muskuraaye.

Unhone kaha,
“Main sab theek karunga.”

Phir unhone ek naya roop liya—

Ek bahut hi sundar ladki ka roop,
jise Mohini kaha gaya.

Woh itni attractive thi
ki sab asur us par fida ho gaye.

Sab apna jhagda bhool gaye.

Ab sab uski baat sunne ko ready ho gaye.

Bhagwan ka plan kaam karne wala tha.

Moral:
Kabhi-kabhi intelligence aur smart strategy se hi bade problems solve hote hain, sirf strength se nahi."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 9
    with st.expander("Chapter 9 - Distribution of Nectar by Mohinī"):
        text1 = """ 
        Asur log amrit ke liye lad rahe the.
Tabhi unhone ek sundar ladki ko aate hue dekha.

Woh Mohini thi—Bhagwan Vishnu ka roop.

Sab asur use dekhkar attract ho gaye."""
        create_image_text_layout(
            "attached_assets/chapter8/8.9.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Unhone poocha,
“Tum kaun ho? Hume help karo.”

Mohini muskuraayi aur boli,
“Main amrit baant sakti hoon…
lekin tumhe meri baat maan ni hogi.”

Asur turant maan gaye.

Unhone amrit ka kalash Mohini ko de diya.

Mohini ne ek plan banaya.

Usne devta aur asur ko alag-alag bitha diya.

Phir woh sweet baaton se asuron ko distract karne lagi.

Aur chupke se devtaon ko amrit dene lagi.

Asur bas uski baaton me busy the.

Unhe kuch samajh hi nahi aaya.

Tab ek asur, Rahu, smart nikla.

Woh devta ban kar unke beech baith gaya.

Aur amrit peene laga.

Lekin Surya aur Chandra ne use pehchaan liya.

Unhone signal diya.

Bhagwan Vishnu ne turant Sudarshan chakra se
uska sir kaat diya.

Rahu ka sir immortal ho gaya,
lekin body khatam ho gayi.

Isi wajah se woh aaj bhi Surya aur Chandra se badla leta hai.

Udhar devta amrit pee chuke the.

Ab woh powerful aur immortal ho gaye.

Tab Mohini ka roop gayab ho gaya.

Bhagwan Vishnu apne asli roop me aa gaye.

Asur tab tak samajh gaye the ki unke saath trick hua hai.

Lekin ab der ho chuki thi.

Devta jeet gaye the.

Moral:
Sirf strength nahi, smartness aur right intention se hi jeet milti hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 10
    with st.expander("Chapter 10 - A Battle between Gods and Asuras"):
        text1 = """ 
        Battle aur bhi intense ho gayi.

Har taraf chaos tha.

Koi ghodon par lad raha tha,
koi haathiyon par,
aur kuch log ajeeb-ajeeb jaanwaron par bhi fight kar rahe the."""
        create_image_text_layout(
            "attached_assets/chapter8/8.10.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Dono armies ek dusre par toot padi.

Bali aur Indra ke beech special fight chal rahi thi.

Bali ne arrows chalaye,
lekin Indra ne unhe easily rok diya.

Bali ne aur powerful weapons use kiye…
lekin Indra ne sab kaat diye.

Ab Bali ne ek trick use ki.

Usne illusion create kar diya.

Achanak aasman se bade-bade pathar girne lage.

Aag jalne lagi.

Zahreeli saamp, jangli janwar aur scary creatures appear hone lage.

Sab devta dar gaye.

Unhe samajh nahi aa raha tha kya karein.

Sab helpless feel karne lage.

Tab unhone Bhagwan ko yaad kiya.

Aur tabhi…

Bhagwan Vishnu Garuda par baith kar battlefield me aaye.

Unka roop bahut powerful tha.

Jaise hi woh aaye,
saari illusion khatam ho gayi.

Sab kuch normal ho gaya.

Bhagwan ne bina time waste kiye,
asuron par attack kiya.

Unhone powerful demons ko easily hara diya.

Kuch ko unhone turant maar diya.

Devtaon ka confidence wapas aa gaya.

Ab unhe pata tha—
Bhagwan unke saath hain.

Moral:
Jab situation kitni bhi confusing aur dangerous ho,
Bhagwan par vishwas aur sahi guidance se sab problems solve ho jaati hain."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 11
    with st.expander("Chapter 11 - End of the Battle Between Gods and Asuras at Nārada’s Mediation"):
        text1 = """ 
        Devta aur asur ke beech battle chal rahi thi.

Bhagwan ki kripa se devta fir strong ho gaye.

Indra aur dusre devta ne
asuron par powerful attack kiya.

Indra ka saamna Bali se hua."""
        create_image_text_layout(
            "attached_assets/chapter8/8.11.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Indra gusse me bola,
“Tum apni tricks se hume nahi hara sakte!”

Lekin Bali shaant tha.

Usne kaha,
“Jeet aur haar sab time par depend karti hai.”

“Wise log kabhi over-excited ya sad nahi hote.”

Battle fir se shuru ho gayi.

Indra ne apna Vajra use kiya
aur Bali ko gira diya.

Yeh dekh kar Bali ka dost Jambha aaya.

Usne Indra par attack kiya
aur uske haathi ko bhi hurt kiya.

Indra ne turant react kiya
aur Jambha ko maar diya.

Phir aur asur aaye—
Namuchi, Bala aur Paka.

Unhone milkar Indra par arrows barsaye.

Kuch time ke liye devta weak pad gaye.

Lekin Indra wapas strong ho gaya.

Usne Bala aur Paka ko bhi hara diya.

Ab Namuchi bacha tha.

Indra ne us par Vajra use kiya…
lekin woh kaam nahi kiya!

Indra confused ho gaya.

Tab aasman se awaaz aayi,

“Is asur ko na wet cheez se mara ja sakta hai,
na dry cheez se.”

Indra ne socha…

Phir usse ek idea aaya.

Usne samundar ki jhaag (foam) use ki.

Foam na poori tarah wet hota hai,
na dry.

Usne us foam se Namuchi ko maar diya.

Sab devta khush ho gaye.

Gandharv gaane lage,
aur apsaras dance karne lagi.

Lekin tab Narad rishi aaye.

Unhone kaha,
“Ab fight band karo.”

“Tumhe pehle hi amrit mil chuka hai.”

Devta ne unki baat maan li.

Woh wapas swarg chale gaye.

Asur apne leader Bali ko lekar chale gaye.

Unke guru Shukracharya ne
unhe wapas zinda kar diya.

Bali ne haar ke baad bhi
apna mann strong rakha.

Woh sad nahi hua.

Moral:
Real strength sirf jeet me nahi,
balki haar ke baad bhi strong rehne me hoti hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 12
    with st.expander("Chapter 12 - Lord Śiva Fascinated by Mohinī"):
        text1 = """ 
        Ek din Bhagwan Shiva ne suna ki
Bhagwan Vishnu ne Mohini ka roop lekar
asuron ko confuse kiya tha.

Unhe curiosity hui.

Unhone socha,
“Main bhi woh roop dekhna chahta hoon.”"""
        create_image_text_layout(
            "attached_assets/chapter8/8.12.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Shiva ji apni wife Parvati ke saath
Vishnu ji ke paas gaye.

Unhone respect se kaha,
“Mujhe woh Mohini roop dikhaiye.”

Bhagwan Vishnu muskuraaye.

Unhone kaha,
“Yeh roop bahut powerful hai…
lekin agar tum dekhna chahte ho,
toh main dikhata hoon.”

Phir Vishnu ji wahan se gayab ho gaye.

Kuch der baad…

Ek beautiful garden me
ek bahut hi sundar ladki dikhi.

Woh ball se khel rahi thi.

Woh itni charming thi
ki sabka attention us par chala gaya.

Shiva ji bhi use dekhkar attract ho gaye.

Woh uski taraf dekhte hi reh gaye.

Dheere-dheere unka mann control se bahar hone laga.

Woh us ladki ke peeche chalne lage.

Parvati ji sab dekh rahi thi.

Woh ladki thodi sharma kar bhaag gayi.

Shiva ji bhi uske peeche bhaag pade.

Woh bilkul uske jaadu me aa gaye the.

Lekin kuch time baad…

Shiva ji ko suddenly realization hua.

Unhe samajh aa gaya,
“Yeh sab Vishnu ji ki maya hai.”

Unhone apne aap ko control kiya.

Woh wapas normal ho gaye.

Tab Bhagwan Vishnu apne asli roop me aaye.

Unhone Shiva ji se kaha,

“Tumne meri maya ko pehchaan liya.”

“Yeh bahut mushkil hota hai.”

“Sirf strong aur aware log hi isse bahar aa sakte hain.”

Shiva ji muskuraaye.

Unhone Vishnu ji ko pranam kiya.

Phir apni wife ke saath wapas chale gaye.

Moral:
Maya aur distractions powerful hote hain,
lekin jo apne aap ko control karta hai,
wahi sach me strong hota hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 13
    with st.expander("Chapter 13 - Description of the Future Manvantaras"):
        text1 = """ 
        Rishi ne ek aur interesting baat batayi.

Unhone kaha,
“Duniya time ke hisaab se chalti hai.”

“Har period ko Manvantara kehte hain.”

Abhi jo chal raha hai,
woh Vaivasvata Manu ka time hai.

Unke bahut saare bete the,"""
        create_image_text_layout(
            "attached_assets/chapter8/8.13.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        aur unhone duniya ko guide kiya.

Rishi ne aage bataya,
“Har Manvantara me naye devta,
naye rishi aur naya Indra hota hai.”

Sab kuch time ke saath change hota rehta hai.

Phir unhone future ke baare me bataya.

“Agla Manu hoga—Savarna.”

Uske time par Bali Indra banega.

Haan, wahi Bali
jo pehle asuron ka king tha.

Bhagwan Vishnu ki kripa se
use yeh position milegi.

Rishi ne aur bhi future bataya,

“Har naye Manu ke saath
Bhagwan alag roop me aayenge.”

“Woh duniya ko protect karenge.”

“Har baar dharm ko bachayenge.”

Yeh cycle baar-baar chalta rahega.

Naye log, naye leaders,
lekin Bhagwan hamesha same rahenge.

Raja dhyaan se sun raha tha.

Usse samajh aa gaya,

“Time change hota hai,
lekin dharm aur Bhagwan kabhi nahi badalte.”

Moral:
Duniya change hoti rehti hai,
lekin sach aur dharm hamesha stable rehte hain."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 14
    with st.expander("Chapter 14 - Duties of Manus and Their Functionaries"):
        text1 = """ 
        Raja ne rishi se poocha,
“Yeh Manus aur dusre log kya kaam karte hain?”

Rishi ne calmly jawab diya.

Unhone kaha,
“Sab kuch Bhagwan ke control me hota hai.”

“Manu, devta, rishi aur Indra—
sab unke guidance me kaam karte hain.”

Raja dhyaan se sun raha tha."""
        create_image_text_layout(
            "attached_assets/chapter8/8.14.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Rishi ne samjhaya,

“Har naye yug ke start me,
rishi log tapasya karke
dharm ka gyaan fir se samajhte hain.”

“Phir Bhagwan unhe sahi raasta dikhate hain.”

“Uske baad Manu duniya me
dharm ko spread karte hain.”

Rishi ne aage kaha,

“Manu ke bete aur unki generations
duniya ki raksha karte hain.”

“Woh ensure karte hain ki sab log
dharm follow karein.”

“Indra rain laata hai
aur nature ka balance maintain karta hai.”

Phir unhone ek aur deep baat batayi,

“Bhagwan har yug me alag roop lete hain.”

“Kabhi rishi bankar gyaan dete hain.”

“Kabhi king bankar burai ko khatam karte hain.”

“Kabhi Time bankar sab kuch destroy kar dete hain.”

Sab roles Bhagwan hi nibhate hain.

Lekin ek twist hai.

Rishi ne kaha,

“Log Bhagwan ko directly nahi dekh paate.”

“Kyunki woh unki maya me uljhe rehte hain.”

Raja ko yeh baat samajh aa gayi.

Usne realise kiya,
“Sab kuch ek system se chal raha hai.”

Aur us system ka controller Bhagwan hai.

Moral:
Duniya ek system se chalti hai, aur us system ke peeche ek supreme power hoti hai—use samajhna hi asli gyaan hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 15
    with st.expander("Chapter 15 - Bali’s Conquest of the Svarga (Celestial Region)"):
        text1 = """ 
        Raja ne rishi se poocha,
“Bhagwan ne Bali se teen kadam zameen kyun maangi?”

Rishi ne kahani shuru ki.

Ek samay Bali asur haar gaya tha.

Woh weak ho gaya tha."""
        create_image_text_layout(
            "attached_assets/chapter8/8.15.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Lekin uske guru Shukracharya ne
use fir se strong bana diya.

Bali ne apne guru ki poori respect ki.

Usne sab kuch unhe dedicate kar diya.

Rishiyon ne khush hokar
uski madad ki.

Unhone ek special yagya karwaya.

Us yagya se Bali ko
divine powers mili.

Usse ek powerful chariot mila,
special weapons mile,
aur strong armor mila.

Ab Bali fir se ready tha.

Woh apni army ke saath
Indra ke rajya ki taraf badha.

Uski army bahut strong thi.

Jab woh swarg ke paas pahucha,
sab jagah uski power dikh rahi thi.

Indra ka rajya bahut sundar tha—
gardens, lakes, palaces sab perfect the.

Lekin Bali ne us par attack kar diya.

Usne apna shankh bajaya,
aur sabko challenge diya.

Indra tension me aa gaya.

Woh apne guru Brihaspati ke paas gaya.

Usne poocha,
“Yeh Bali itna powerful kaise ho gaya?”

Guru ne jawab diya,

“Uski power Brahmanon ki blessings se aayi hai.”

“Abhi tum usse nahi jeet sakte.”

“Thoda time wait karo.”

“Abhi swarg chhod do.”

Indra ne unki baat maan li.

Sab devta wahan se chale gaye.

Ab Bali ne swarg par kabza kar liya.

Usne teenon lok apne control me le liye.

Rishiyon ne use aur powerful banane ke liye
100 yagya karwaye.

Ab Bali ek mahaan aur successful king ban gaya.

Uski fame har jagah fail gayi.

Woh apni power aur success me khush tha.

Lekin kahani abhi khatam nahi hui…

Moral:
Power aur success mehnat aur guidance se milti hai,
lekin uska sahi use hi asli wisdom hota hai."""
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
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
        text1 = """ 
        Raja Parikshit ne ek aur kahani sunne ki ichchha ki.

Unhone kaha,
“Manu ke vansh ke rajaon ki kahani bataiye.”"""
        create_image_text_layout(
            "attached_assets/chapter9/9.1.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Rishi ne kahani shuru ki.

Sab kuch shuru hua
Bhagwan Vishnu se—

Unke naabhi se ek kamal nikla,
jisme Brahma ji ka janm hua.

Phir Brahma se Marichi,
phir Kashyap,
aur phir Aditi ke ghar janm hua—

Vivasvat (Surya dev).

Vivasvat ke bete the—
Vaivasvata Manu.

Unke kai putra the,
jinme Ikshvaku sabse famous tha.

Lekin ek twist hua.

Manu ko ek beta chahiye tha.

Isliye unhone yagya karwaya.

Unki wife ne secretly ek daughter maangi.

Galti se yagya ka result change ho gaya…

Aur ek ladki paida hui—

Ila.

Manu thoda upset ho gaye.

Tab Rishi Vashishtha ne kaha,

“Main ise beta bana deta hoon.”

Bhagwan Vishnu ki kripa se
Ila ban gayi—

Sudyumna.

Sudyumna ek brave king bana.

Ek din woh hunting ke liye gaya.

Woh ek special forest me ghus gaya—

Jo Lord Shiva aur Parvati ka area tha.

Jaise hi woh andar gaya…

Ek strange cheez hui—

Woh ladki ban gaya!

Uska ghoda bhi mare ban gaya.

Uske saare soldiers bhi women ban gaye.

Sab shock me aa gaye.

Yeh sab kyun hua?

Kyunki Lord Shiva ne
us jagah par curse diya tha:

“Jo bhi male yahan aayega,
woh female ban jayega.”

Ab Sudyumna (ab Ila) jungle me bhatakne laga.

Tab ek devta mile—

Budha (Mercury).

Unhe Ila se pyaar ho gaya.

Aur Ila ko bhi.

Dono ne shaadi ki.

Aur unka ek beta hua—

Pururavas.

Lekin Sudyumna apni asli identity bhool nahi paaya.

Usne apne guru Vashishtha ko yaad kiya.

Guru turant aa gaye.

Unhone Shiva se request ki.

Shiva ne solution diya:

“Sudyumna ek mahine male rahega…”

“aur ek mahine female.”

Sudyumna ne is condition me bhi rajya chalaya.

Lekin logon ko yeh system pasand nahi aaya.

Aakhir me usne apna rajya
apne bete Pururavas ko de diya.

Aur khud jungle me tapasya ke liye chala gaya.

Moral:
Life unpredictable hoti hai—
lekin wisdom yeh hai ki har situation me
balance aur acceptance ke saath jeena seekho."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 2
    with st.expander("Chapter 2 - History of Karūṣa and other four sons of Manu"):
        text1 = """ 
        Rishi ne kahani aage badhai.

Jab Sudyumna jungle chala gaya,
tab Manu ne socha—

“Mujhe aur putra chahiye.”"""
        create_image_text_layout(
            "attached_assets/chapter9/9.2.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Manu ne Yamuna ke kinare
100 saal tak tapasya ki.

Phir Bhagwan Vishnu ko prasann kiya.

Aur unhe 10 putra mile—
jinme sabse bada tha Ikshvaku.

Inhi me se ek tha—Prishadhra

Usse duty di gayi—
gaayon ki raksha karne ki.

Woh raat bhar jag kar
gaayon ki dekhbhaal karta tha.

Ek raat heavy rain ho rahi thi.

Andhera itna tha
ki kuch dikh nahi raha tha.

Tab ek tiger gaushala me ghus gaya.

Gaayen dar kar bhaagne lagi.

Prishadhra ne awaaz suni
aur talwar lekar daud pada.

Andhere me usne attack kiya…

Lekin galti ho gayi—

Usne tiger nahi,
ek gaay ko maar diya.

Subah jab usne dekha…

Toh woh shock ho gaya.

Usse bahut guilt hua.

Tab uske guru Vashishtha aaye.

Unhone kaha,

“Tumne paap kiya hai…”

“Isliye tum Shudra ban jaoge.”

Prishadhra ne argue nahi kiya.

Usne calmly curse accept kar liya.

Usne decide kiya—

“Main simple life jeeyunga.”

“Main bhakti aur dhyaan karunga.”

Woh sab chhodkar
ek saint ki tarah jeene laga.

Na attachment, na desire.

Bas meditation aur shanti.

Ek din jungle me
aag lag gayi.

Woh bhaaga nahi.

Woh shanti se wahin khada raha…

Aur uska sharir jal gaya.

Lekin uski atma
Brahman me merge ho gayi.

Usse moksha mil gaya.

Dusra beta tha—Kavi

Woh bachpan se hi
worldly cheezon me interested nahi tha.

Usne bhi sab chhod diya
aur forest chala gaya.

Aur woh bhi moksha pa gaya.

Baaki Manu ke vansh me
bahut saare raja hue—

Jaise Karusha,
jinke vansh ne north region rule kiya.

Aur baad me ek great king aaya—

Marutta

Marutta ne itna grand yagya kiya
ki sab kuch gold ka tha.

Indra bhi itna soma peeke
mast ho gaya tha.

Devta khud service kar rahe the.

Yeh sab dekhkar
sabko samajh aa gaya—

“Yeh vansh bahut powerful aur dharmik hai.”

Moral:
Galti ho jaaye toh bhi insaan apni life sudhaar sakta hai—
aur bhakti aur self-control se moksha tak pahunch sakta hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 3
    with st.expander("Chapter 3 - The story of Cyavana and Sukanyā"):
        text1 = """ 
        Rishi ne ek aur interesting kahani sunayi.

Ek raja tha—Sharyati

Woh bahut gyaani tha
aur uski ek beti thi—

Sukanya

Uski aankhen bahut sundar thi,
jaise kamal."""
        create_image_text_layout(
            "attached_assets/chapter9/9.3.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Ek din woh apne friends ke saath
forest me ghoom rahi thi.

Wahan usne ek ajeeb cheez dekhi—

Ek anthill (mitti ka dher)
jisme do chamakne wali cheezein thi.

Usne curiosity me
unhe kaante se chhed diya…

Achanak khoon nikalne laga!

Actually…

Woh do “light points”
ek rishi ki aankhen thi—

Rishi Cyavana

Jo meditation me baithe the.

Us moment par
king ke soldiers ko problem hone lagi—

Unka body function ruk gaya!

Sab panic ho gaye.

King ne samajh liya
ki kisi ne rishi ko hurt kiya hai.

Sukanya dar gayi
aur sach bata diya.

King ne turant rishi se maafi maangi.

Rishi gusse me the…

Unhone ek condition rakhi—

“Main tumhari beti se shaadi karunga.”

King majboor tha.

Usne Sukanya ki shaadi
old aur weak Cyavana rishi se kar di.

Sukanya ne complain nahi kiya.

Usne apne husband ki
pure devotion se seva ki.

Woh ek perfect pativrata ban gayi.

Kuch time baad
Ashvini Kumar (dev doctors) wahan aaye.

Rishi ne unse kaha,

“Mujhe young bana do.”

“Main tumhe yagya me Soma ka share dilwaunga.”

Unhone agree kar liya.

Unhone rishi ko ek special pond me le gaye.

Jab woh bahar aaye…

Toh ek nahi,
teen young aur handsome log nikle!

Sukanya confuse ho gayi—

“Kaun mera husband hai?”

Ashvini Kumar uski loyalty se impress ho gaye.

Unhone usse sahi husband dikha diya.

Kuch time baad
King Sharyati wapas aaye.

Unhone apni beti ke paas
ek handsome young man dekha.

Woh gusse me aa gaye.

Unhone kaha,

“Tumne apne husband ko cheat kiya?”

Sukanya muskuraayi
aur boli,

“Yeh hi aapke damaad Cyavana hain.”

King shock ho gaya.

Usne sab suna
aur bahut khush hua.

Phir Cyavana ne ek yagya karwaya
jisme Ashvini Kumar ko Soma diya.

Indra ko yeh pasand nahi aaya.

Usne attack karne ki koshish ki—

Lekin Cyavana ne
uska haath hi freeze kar diya!

End me sab maan gaye—

Ashvini Kumar ko bhi
Soma ka share milne laga.

Moral:
True loyalty aur devotion itni powerful hoti hai
ki woh destiny bhi change kar sakti hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4
    with st.expander("Chapter 4 - The Account of Nābhāga and Ambarīṣa"):
        text1 = """ 
        Rishi ne ek aur powerful kahani sunayi—
Nābhāga aur Ambarīṣa ki kahani.

Sabse pehle baat aati hai Nābhāga ki.

Woh apne gurukul se wapas aaya
aur apna hissa maanga.

Lekin uske bhaiyon ne kaha,

“Humne sab baant liya…
tumhara hissa hai—pitaji ki seva.”"""
        create_image_text_layout(
            "attached_assets/chapter9/9.4.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Nābhāga ne bina argue kiye
yeh accept kar liya.

Usne apne father se poocha,

“Ab main kya karu?”

Father ne advice diya:

“Kuch rishi yagya kar rahe hain…”

“Unhe help karo…”

“Woh tumhe reward denge.”

Nābhāga ne waisa hi kiya.

Rishiyon ne khush hokar
use bahut saara dhan de diya.

Lekin tab ek dark person aaya—

Woh actually Rudra (Shiva) the.

Unhone kaha,

“Yeh dhan mera hai.”

Nābhāga confuse ho gaya.

Usne apne father se poocha.

Father ne kaha,

“Yeh sach me Rudra ka hi hai.”

Nābhāga turant wapas gaya,
aur respectfully bola,

“Yeh sab aapka hai.”

Rudra impressed ho gaye.

Unhone kaha,

“Tumne sach bola hai.”

“Main tumhe gyaan deta hoon.”

Aur saath me
woh dhan bhi use de diya.

Lesson:
Sachchai hamesha reward deti hai.

Ab aati hai kahani
King Ambarīṣa ki—Nābhāga ke bete ki.

Woh bahut bada king tha—

Rich, powerful,
lekin bilkul ego nahi.

Usne apni life ka har part
Bhagwan Vishnu ko dedicate kar diya:

Mind → Bhagwan ke dhyaan me
Words → Bhagwan ki stuti me
Hands → seva me
Ears → stories sunne me

Ek baar usne ek special vrat rakha—
Ekadashi–Dwadashi fast

1 saal tak discipline follow kiya.

Final day par
ek problem aa gayi.

Ek rishi aaye—
Durvasa

King ne unhe khana khilane ke liye bulaya.

Durvasa nahaane chale gaye…

Lekin time nikal raha tha—

Fast todne ka exact moment aa gaya.

Ab dilemma:

👉 Agar khaye → guest ka apmaan
👉 Agar na khaye → vrat toot jayega

King ne smart decision liya:

Usne sirf paani piya—
(jisse fast bhi toot jaye aur meal bhi na ho)

Durvasa wapas aaye…

Unhe gussa aa gaya.

Unhone kaha,

“Tumne mujhe ignore kiya!”

Gusse me unhone
ek dangerous demon create kar diya.

Woh Ambarīṣa par attack karne gaya.

Lekin Bhagwan ka Sudarshan chakra
us demon ko turant destroy kar deta hai.

Aur phir Durvasa ke peeche pad jaata hai!

Durvasa bhaagne lagte hain—

Sky, earth, Brahma ji, Shiva ji—
sab jagah jaate hain…

Lekin koi unhe bachata nahi.

Aakhir me woh Bhagwan Vishnu ke paas jaate hain.

Aur kehte hain,

“Please mujhe bachaiye.”

Bhagwan Vishnu kehte hain:

“Main apne bhakton ke control me hoon.”

“Tumne Ambarīṣa ko hurt kiya hai…”

“Sirf wahi tumhe maaf kar sakta hai.”

Durvasa turant wapas jaate hain
aur Ambarīṣa se maafi maangte hain.

King ne turant unhe maaf kar diya.

Aur Sudarshan chakra bhi shant ho gaya.

Moral:

Sachchai aur vinamrata sabse badi shakti hai
Jo Bhagwan ke bhakt hote hain, unki raksha khud Bhagwan karte hain
Gyaan aur power ka galat use khud par hi wapas aata hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 5
    with st.expander("Chapter 5 - Protection of Durvāsas—The story of Ambarīṣa Concluded"):
        text1 = """ 
        Durvasa Rishi darr ke maare
seedha King Ambarīṣa ke paas laut aaye.

Unhone turant unke pair pakad liye—
aur maafi maangi.

Ambarīṣa ko yeh dekhkar sharm aa gayi.

Unhone socha,
“Ek Brahmana mere saamne jhuk raha hai…”

Unka dil compassion se bhar gaya."""
        create_image_text_layout(
            "attached_assets/chapter9/9.5.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Unhone turant Bhagwan ke Sudarshan chakra se prarthana ki:

“Hey Sudarshan!
Aap sab kuch ho—Agni, Surya, Chandrama…”

“Aap dharm ho, satya ho…”

“Please iss Brahmana ko maaf kar do.”

Unhone aur bhi kaha:

“Agar maine kabhi daan kiya hai…”
“Agar maine dharm follow kiya hai…”
“Agar maine sab logon ko respect diya hai…”

“Toh iss rishi ko bachaa lo.”

Yeh sunte hi Sudarshan chakra shant ho gaya.

Durvasa ko relief mil gaya.

Durvasa Rishi bahut impressed ho gaye.

Unhone kaha,

“Wah! Aaj maine sachchi greatness dekhi hai.”

“Tumne us insaan ko bhi bachaya
jisne tumhe marne ki koshish ki.”

Unhone Ambarīṣa ki bahut tarif ki:

“Bhagwan ke bhakt sab kuch kar sakte hain…”

“Unke liye kuch bhi impossible nahi hai.”

Phir Ambarīṣa ne unhe khana khilaya.

Tab tak…

👉 Ek saal tak
Ambarīṣa ne khud kuch nahi khaya tha

Woh bas Durvasa ka wait kar rahe the!

Durvasa ne khana khaya
aur bahut khush ho gaye.

Unhone blessings diye
aur wahan se chale gaye.

Tab Ambarīṣa ne bhi
bacha hua prasad khaya.

Aur socha,

“Yeh sab Bhagwan ki kripa se hua hai.”

Baad me…

Ambarīṣa ne apna rajya
apne beton ko de diya.

Aur khud forest me chale gaye—

Bhagwan Vishnu ka dhyaan karne.

Aakhir me woh
moksha prapt kar gaye.

Moral:

Forgiveness sabse badi power hai
Saccha bhakt kabhi ghamand nahi karta
Jo dusron ke liye achha chahta hai—even enemies ke liye—
wahi sabse bada insaan hota hai"""
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
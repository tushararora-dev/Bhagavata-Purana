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
    create_image_text_layout("attached_assets/chapter6/chapter6.jpg", layout="full")
    # Book 6 - Sixth Skandha
    text0 = """
    <h2>Book 6 - Sixth Skandha</h2>
    """
    
    # Book 6 - Sixth Skandha

    # Chapter 1
    with st.expander("Chapter 1 - The Story of Ajāmila"):
        text1 = """ 
        
        👑 Raja ka sawaal

Raja Parikshit ne poocha,
“Log paap karte hain…
toh unhe narak se kaise bachaya jaa sakta hai?” 😟

⚖️ Paap aur prayaschit

Śuka rishi bole,
“Agar insaan apne paap ka prayaschit (atonement) nahi karta…”

👉 toh usse narak jana padta hai 😔"""
        create_image_text_layout(
            "attached_assets/chapter6/6.1.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Isliye:

👉 turant apni galti sudharni chahiye
👉 jaise doctor disease ka treatment karta hai 💊

🤔 Raja ki confusion

Raja bola,
“Par log fir se paap kar dete hain…”

👉 toh prayaschit ka kya fayda?

“Yeh toh haathi ke nahaane jaisa hai 🐘
jo baad mein fir mitti mein lot jaata hai!”

🧠 Asli solution

Rishi bole,
“Sirf prayaschit se kaam nahi chalega…”

👉 Asli solution hai — Gyaan (self-realization) ✨

Jab insaan sach samajh leta hai…
tab woh paap karna band kar deta hai.

🔥 Achhe gun ki power

Rishi ne bataya:

👉 truth
👉 charity
👉 self-control
👉 non-violence

Yeh sab milkar paap ko jala dete hain 🔥

Jaise aag bamboo ko jala deti hai.

💖 Bhakti sabse powerful

Par sabse best kya hai?

👉 Bhagwan ki bhakti 🙏

Rishi bole,
“Jo Bhagwan ko sachche dil se yaad karta hai…”

👉 uske paap jad se khatam ho jaate hain ✨

😇 Bhakt ki special power

Jo insaan:

👉 ek baar bhi Bhagwan ka naam leta hai
👉 ya unke charan mein mann lagaata hai

👉 usse Yamraj ka darr nahi hota 😲

📖 Ajāmila ki kahani

Rishi bole,
“Is baat ko samjhane ke liye ek kahani hai…”

👦 Ajāmila ka jeevan

Ek Brahman tha — Ajāmila

Woh pehle:

achha insaan tha 😊
dharmik tha 🙏
sabka respect karta tha
😔 Galat raasta

Ek din usne dekha:

👉 ek aadmi aur ek buri aurat
👉 galat kaam kar rahe the

Uska mann hil gaya 😳
aur woh us aurat ke pyaar mein pad gaya.

💔 Girawat

Phir:

👉 usne apni achhi wife chhod di 😢
👉 galat kaam karne laga
👉 paap se paisa kamaane laga

Jaise:

gambling 🎲
theft
cheating
👨‍👦 Attachment

Uske 10 bachche hue
aur sabse chhota beta tha — Nārāyaṇa ❤️

Ajāmila usse bahut pyaar karta tha.

⏳ Ant ka samay

Jab Ajāmila budha ho gaya…
aur uski death ka time aaya 😨

Usne dekha:

👉 Yamraj ke doot aa gaye 😱
👉 darawne roop mein

😭 Ek naam

Darr ke maare…
usne apne bete ko bulaya:

👉 “Nārāyaṇa!” 😢

Par yeh naam…
Bhagwan ka bhi tha 🙏

⚡ Miracle

Jaise hi usne “Nārāyaṇa” bola…

👉 Vishnu ji ke doot turant aa gaye ✨
👉 aur Yamdooton ko rok diya

😲 Yamdoot ka sawaal

Yamdoot bole:

“Tum kaun ho?
Aur hume kyun rok rahe ho?”

⚖️ Dharma ka debate

Vishnu ke doot bole,
“Tum dharma samajhte ho?”

👉 kaun punishment deserve karta hai?
👉 kaun nahi?

📜 Karma ka rule

Yamdoot bole:

👉 Vedas hi dharma batate hain
👉 jo galat karega → punishment milega

👉 har action ka result hota hai

🔄 Jeevan ka sach
insaan kabhi actionless nahi hota
har koi kuch na kuch karta hi hai

Aur:

👉 uska phal usse zaroor milta hai

🌈 Final twist

Ajāmila ne:

👉 bas ek baar Bhagwan ka naam liya

Aur:

👉 uski life bach gayi 😲

🌟 Moral:

Bhagwan ka naam aur bhakti itni powerful hai
ki woh sabse bade paap ko bhi mita sakti hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 2
    with st.expander("Chapter 2 - Exposition of the Bhāgavata Dharma"):
        text1 = """ 
        ⚖️ Vishnu ke dooton ka jawab

Śuka rishi ne bataya,
“Vishnu ji ke doot Yamdooton ki baat sun kar bole…”

“Yeh galat hai!
Tum ek aise insaan ko punish kar rahe ho
jo ab paapi nahi raha!”"""
        create_image_text_layout(
            "attached_assets/chapter6/6.2.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        😢 Daya aur nyay

Unhone kaha:

👉 “Agar rakshak hi galat kare…
toh aam log kahan jayenge?”

👉 “Log apne leaders ko follow karte hain…
isliye unhe sahi hona chahiye.”

✨ Ek naam ki power

Vishnu ke doot bole:

👉 “Ajāmila ne ‘Nārāyaṇa’ naam liya…”

👉 “Aur ussi se uske saare paap khatam ho gaye!” 😲

Chahe usne apne bete ko bulaya ho…
par naam toh Bhagwan ka hi tha 🙏

🔥 Sab paap mit jaate hain

Unhone samjhaya:

👉 Chori
👉 sharab
👉 dhokha
👉 murder

Jaise bade paap bhi…

👉 Bhagwan ka naam lene se mit jaate hain ✨

🧠 Real purification

Unhone kaha:

👉 rituals se sirf bahar ka paap kam hota hai
👉 par Bhagwan ka naam mann ko bhi saaf karta hai ❤️

😲 Even without knowing!

Sabse interesting baat:

👉 agar koi mazaak mein bhi naam le le
👉 ya galti se bol de

👉 tab bhi paap jal jaate hain 🔥

💊 Example

Jaise:

👉 medicine kaam karti hai
chahe tumhe uska knowledge ho ya nahi

Waise hi:

👉 Bhagwan ka naam apna kaam karta hai ✨

✂️ Ajāmila free ho gaya

Vishnu ke doot ne:

👉 Ajāmila ko bachaya
👉 Yamdooton ko rok diya

Aur Ajāmila ko nayi life mil gayi 🙏

😔 Ajāmila ka regret

Ajāmila ne socha:

“Main kitna galat tha…” 😢

👉 maine apni achhi life barbaad ki
👉 parents ko chhod diya
👉 paap kiya

Usse bahut pachtawa hua 💔

🌊 Nayi shuruaat

Phir Ajāmila:

👉 sab kuch chhod kar
👉 Ganga ke paas gaya 🌊

Aur:

👉 dhyaan aur bhakti shuru ki 🧘‍♂️

🧘‍♂️ Badlav

Usne:

👉 mann control kiya
👉 Bhagwan par focus kiya
👉 attachment chhod diya

Aur dheere dheere pure ho gaya ✨

😇 Ant mein mukti

Aakhir mein:

👉 Vishnu ke doot wapas aaye
👉 Ajāmila ko le gaye

👉 aur woh Bhagwan ke dham (Vaikuntha) pahunch gaya 🌈

🌟 Final sach

Rishi ne kaha:

👉 Bhagwan ka naam sabse powerful hai
👉 yeh paap ko jad se mita deta hai

🌟 Moral:

Bhagwan ka naam sachche dil se lene se
sabse bada paapi bhi sudhar sakta hai aur mukti paa sakta hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 3
    with st.expander("Chapter 3 - Yama explains Viṣṇu’s greatness"):
        text1 = """ 
        😲 Yamdoot ka confusion

Yamdoot apne swami Yama ke paas gaye
aur bole,

“Prabhu, hume samajh nahi aa raha…” 😟

“Humne ek paapi ko pakda tha…
par kuch divine log aaye aur use chhuda diya!”"""
        create_image_text_layout(
            "attached_assets/chapter6/6.3.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        👑 Yama ka jawab

Yama muskuraaye 😊
Aur bole,

“Tumne jo dekha…
woh koi aam log nahi the.”

👉 “Woh Vishnu ji ke doot the!” ✨

🌌 Sabse bada kaun?

Yama ne samjhaya:

👉 “Main sabka judge hoon…
par mere upar bhi ek hai…”

👉 “Woh hain Bhagwan Vishnu 🙏”

Sab kuch unke control mein hai.

🧵 Simple example

Yama bole:

👉 “Jaise bail ko rassi se control kiya jata hai 🐂
waise hi sab log Bhagwan ke control mein hain.”

😮 Devta bhi nahi samajh paate

Yama ne kaha:

👉 “Brahma, Shiva, Indra…
sab Bhagwan ko fully samajh nahi paate!”

Toh normal insaan kaise samjhega?

👼 Vishnu ke doot

Yama bole:

👉 “Vishnu ke doot bahut powerful hain 💥
👉 woh Bhagwan jaise hi dikhte hain”

👉 “Woh bhakton ki hamesha raksha karte hain” ❤️

🛡️ Bhakt safe hai

Yama ne clear bola:

👉 “Jo Bhagwan ke bhakt hain…”

👉 “Unhe na main punish kar sakta hoon
👉 na time (death) unhe touch kar sakta hai!” 😲

📖 Sabse bada dharma

Yama ne kaha:

👉 “Sabse bada dharma kya hai?”

👉 Bhagwan ka naam lena aur bhakti karna 🙏

😲 Ajāmila example

Yama bole:

👉 “Dekho Ajāmila ko…”

👉 usne bas ek baar naam liya
👉 aur bach gaya!

Yeh Bhagwan ke naam ki power hai ✨

⚠️ Important rule

Yama ne apne dooton ko bola:

👉 “Kabhi bhi bhakton ke paas mat jaana!”

👉 “Unhe disturb mat karna!”

❌ Kisko lana hai?

Yama bole:

👉 “Sirf un logon ko lao…”

jo Bhagwan ka naam nahi lete
jo unhe yaad nahi karte
jo unhe respect nahi karte

👉 wahi punishment deserve karte hain ⚖️

🙏 Yama ki vinamrata

Aakhir mein Yama ne bhi kaha:

👉 “Main bhi Bhagwan ko pranam karta hoon”

Unhone bhi accept kiya:

👉 Bhagwan sabse upar hain ✨

🌈 Final sach

👉 Bhakti = sabse powerful
👉 Bhagwan ka naam = sabse bada protection

🌟 Moral:

Jo Bhagwan ka naam leta hai,
use duniya ki koi shakti chhoo nahi sakti."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4
    with st.expander("Chapter 4 - History of Dakṣa, the son of Pracetas"):
        text1 = """ 
        🌳 Pracetas ka gussa

Śuka rishi ne bataya,
“Ek samay Pracetas (raja ke bete) samundar se bahar aaye…” 🌊

Unhone dekha:

👉 poori dharti pedon se bhari hui hai 🌳🌳

Woh gussa ho gaye 😠
Aur bole,

“Yeh sab hata denge!”"""
        create_image_text_layout(
            "attached_assets/chapter6/6.4.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        🔥 Vinash shuru

Gusse mein unhone:

👉 apne muh se aag aur hawa nikali 🔥🌪️
👉 ped jalne lage 😨

Dharti jalne lagi…
sab kuch khatam hone laga.

🌙 Chandra dev ka entry

Tab Chandra dev (Moon God) aaye 🌙
Aur pyaar se bole,

“Hey rajkumaro, yeh galat hai…”

“Tum rakshak ho…
vinash karne wale nahi।”

🌱 Jeevan ka balance

Chandra dev ne samjhaya:

👉 ped aur plants sabke food hain
👉 sab ek doosre par depend karte hain

Jaise:

animals plants par depend
humans animals aur plants par

👉 yeh ek balance system hai ⚖️

🧘‍♂️ Gussa control karo

Unhone kaha:

👉 “Apna gussa control karo”
👉 “Apne purvajon ka raasta follow karo”

Aur yaad dilaya:

👉 sabke andar Bhagwan Hari rehte hain 🙏

💖 Mariṣā ka gift

Phir Chandra dev ne ek sundar ladki di —
Mariṣā 🌸

👉 usse Pracetas ne shaadi ki

Aur sab shaant ho gaya 😊

👶 Dakṣa ka janam

Unse ek beta paida hua —
Dakṣa 👶

Woh bahut powerful aur important bana 💫

👉 uski santaan se hi duniya bhar gayi 🌍

🧘 Dakṣa ki tapasya

Par Dakṣa ne dekha:

👉 creation slow hai

Toh woh gaya ek pavitra jagah
aur tapasya shuru ki 🙏

🙏 Bhagwan ki prarthana

Dakṣa ne Bhagwan se kaha:

👉 “Aap sabke andar ho”
👉 “Aap hi sabka sach ho”
👉 “Aap hi sab kuch ho” ✨

Woh pure dil se prarthana kar raha tha ❤️

🌟 Bhagwan ka darshan

Bhagwan Vishnu khush ho gaye 😊
Aur unke saamne prakat ho gaye ✨

Unka roop:

sundar 😍
chamakdar ☀️
divya aur shant

Sab unhe dekh kar hairaan reh gaye 😲

😢 Khushi ka ehsaas

Dakṣa itna khush hua…

👉 woh kuch bol hi nahi paaya
👉 bas pranam karta raha 🙇‍♂️

🎁 Bhagwan ka vardaan

Bhagwan bole:

👉 “Main tumse khush hoon” 😊
👉 “Tum duniya ko badhane ka kaam karo”

Aur unhe ek patni di — Asiknī ❤️

🌍 Nayi srishti

Bhagwan ne kaha:

👉 ab log family bana kar janam lenge
👉 aur duniya aage badhegi

🌈 Ant mein

Bhagwan apna kaam karke
wahan se gayab ho gaye ✨

Aur Dakṣa ne nayi srishti shuru ki.

🌟 Moral:

Gussa vinash karta hai,
par shanti aur samajh duniya ko aage badhati hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 5
    with st.expander("Chapter 5 - Dakṣa curses Nārada"):
        text1 = """ 
        👶 Dakṣa ke bete

Śuka rishi ne bataya,
“Dakṣa ne apne pehle 10,000 bete paida kiye —
jinhe Haryaśva kehte the.”

Sab acche aur samajhdaar the 😊

Unke pita ne kaha:
“Tum sab milkar duniya ko aage badhao.”"""
        create_image_text_layout(
            "attached_assets/chapter6/6.5.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        🌊 Pavitra jagah

Woh sab gaye ek pavitra jagah —
Nārāyaṇa Saras lake 🌊

Wahan jaate hi…

👉 unka mann shuddh ho gaya ✨
👉 unhe sach ki talash hone lagi

🧙‍♂️ Nārada ka entry

Tab aaye Nārada rishi 🎶

Unhone unse ek ajeeb sawaal poocha:

“Tum duniya banane chale ho…
par kya tumne duniya ko samjha bhi hai?” 🤔

🧠 Sochne wali baat

Nārada ne kaha:

👉 “Pehle yeh samjho ki jeevan kya hai”
👉 “Atma kya hai”
👉 “Sach kya hai”

“Bina samjhe kuch banana…
bewakoofi hai!”

🌟 Bada decision

Yeh baat sunkar
Haryaśva sochne lage 🧠

Aur phir decide kiya:

👉 “Hum pehle sach ko samjhenge”
👉 “Hum moksha ka raasta choose karte hain”

Aur woh sab
wapis kabhi nahi aaye 😲

😡 Dakṣa ka gussa

Jab Dakṣa ko pata chala…

👉 woh dukhi bhi hua 😢
👉 aur bahut gussa bhi 😠

👶 Dusre bete

Phir usne 1000 aur bete paida kiye —
Śabalāśva 👶

Unhe bhi bola:
“Jaao aur srishti badhao!”

😅 Same story again

Woh bhi gaye wahi lake 🌊
Aur phir se Nārada rishi aa gaye 😄

Unhone bola:

👉 “Apne bhaiyon ka raasta follow karo”

Aur guess karo kya hua?

👉 woh bhi moksha ke raaste par chale gaye 😲

😤 Dakṣa ka explosion

Ab Dakṣa ka patience khatam 😤

Woh gusse mein bola:

“Hey Nārada! Tumne mere dono groups ke bete bigaad diye!”

👉 “Unhe ghar chhodne par majboor kiya!”
👉 “Meri family khatam kar di!”

⚡ Shraap (curse)

Gusse mein Dakṣa ne kaha:

👉 “Ab tum kabhi ek jagah nahi ruk paoge!”
👉 “Tum hamesha bhatakoge!” 🌍

😌 Nārada ka reaction

Par Nārada rishi ne shanti se kaha:

👉 “Theek hai…” 😊

Unhone gussa nahi kiya
aur curse accept kar liya 🙏

🌈 Sach kya hai?

Nārada ne dikhaya:

👉 duniya banana important hai
👉 par sach ko samajhna usse bhi important hai

🌟 Moral:

Gyaan aur sach ki khoj sabse bada kaam hai —
aur sachcha insaan gusse mein bhi shant rehta hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6
    with st.expander("Chapter 6 - Progeny of Dakṣa’s Daughters"):
        text1 = """ 
        👧 Dakṣa ki betiyan

Śuka rishi ne bataya,
“Dakṣa ne phir 60 betiyan paida ki” 👧

Woh sab apne pita se bahut pyaar karti thi ❤️"""
        create_image_text_layout(
            "attached_assets/chapter6/6.6.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        💍 Shaadi aur nayi duniya

Dakṣa ne unki shaadi alag-alag logon se kar di:

kuch Dharma ko 🙏
kuch Kaśyapa rishi ko 🧘‍♂️
kuch Chandra dev ko 🌙

Aur is tarah
nayi srishti (creation) shuru hui 🌍

🌱 Alag-alag jeev ka janam

In betiyon ke through duniya mein
alag-alag prani aaye:

👉 Devta ✨
👉 Asur 😈
👉 Insaan 👨
👉 Janwar 🐘
👉 Pakshi 🐦
👉 Saap 🐍

Sab isi se badhne lage।

🐦 Vinatā aur Garuḍa

Ek beti Vinatā thi 👩

Uska beta tha —
👉 Garuḍa 🐦

Woh bahut powerful tha 💥
Aur Bhagwan Vishnu ka vahan (vehicle) bana।

🐍 Kadrū aur saap

Dusri beti Kadrū thi

👉 usse paida hue saare saap (serpents) 🐍

🐄 Surabhi aur gaay

Ek beti Surabhi thi 🐄

👉 usse gaay aur dusre pashu paida hue

🐅 Saramā aur jaanwar

Saramā se:

👉 tiger 🐅
👉 aur dusre carnivorous animals

paida hue।

🐟 Timi aur jal jeev

Timi se:

👉 saare jal ke jeev (aquatic animals) 🐟

paida hue।

🌸 Muni aur apsara

Muni se:

👉 sundar apsara (celestial girls) 💃

janmi।

🌌 Aditi aur devta

Aditi se paida hue:

👉 Indra ⚡
👉 aur aur bhi devta

Aur sabse special —
👉 Vāmana avatar (Bhagwan Vishnu ka roop) ✨

🌙 Chandra ki kahani

Chandra dev ne 27 betiyon se shaadi ki 🌙

Par Dakṣa ne use curse diya 😠
Isliye woh weak ho gaya।

Baad mein usne maafi maangi
aur thoda theek ho gaya।

🌈 Duniya ka expansion

Is tarah:

👉 alag-alag prani
👉 alag-alag praja

poori duniya mein phail gayi 🌍

🌟 Final sach

Sab jeev ek hi source se aaye…
aur sab ek doosre se jude hue hain।

🌟 Moral:

Har jeev ka apna role hai —
aur sab milkar hi duniya complete banti hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7
    with st.expander("Chapter 7 - Bṛhaspati’s Insult and his abandonment of Preceptorship"):
        text1 = """ 
        👑 Indra ka ghamand

Śuka rishi ne bataya,
“Ek baar Indra, devtaon ka raja,
apni shakti aur power par ghamand karne laga…” 😤

Woh apne singhasan par baitha tha 👑
sab uski tareef kar rahe the ✨"""
        create_image_text_layout(
            "attached_assets/chapter6/6.7.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        🙏 Guru ka apmaan

Tab wahan aaye uske guru —
Bṛhaspati 🙏

Par Indra ne:

👉 unhe respect nahi diya
👉 na khada hua
👉 na greet kiya

Yeh bahut bada galat kaam tha 😔

😶 Guru chale gaye

Bṛhaspati sab samajh gaye…
ki Indra ghamandi ho gaya hai

Woh chup-chaap wahan se chale gaye 🚶‍♂️

😢 Indra ka regret

Thodi der baad Indra ko realize hua 😨

Usne kaha,
“Yeh maine kya kar diya…”

👉 “Maine apne guru ka apmaan kiya…”
👉 “Yeh meri sabse badi galti hai!”

🔍 Guru ki talaash

Indra ne apne guru ko dhoondhne ki koshish ki…
par woh kahin nahi mile 😔

Ab uska mann bilkul ashant ho gaya।

⚔️ Asur ka attack

Jab asuro ko pata chala…
ki devtaon ke paas guru nahi hai 😈

👉 unhone attack kar diya 💥

Devta:

👉 ghayal ho gaye 😣
👉 haarne lage

🙏 Brahma ke paas

Phir sab devta milkar
Brahma ji ke paas gaye 🙏

Aur bole,
“Hume bachaiye!”

⚖️ Brahma ka jawab

Brahma ji bole:

👉 “Yeh sab tumhari galti ka result hai”

👉 “Tumne apne guru ka apmaan kiya”

“Isliye tumhe yeh dukh mila.”

💡 Solution

Brahma ji ne kaha:

👉 “Ab tum Viśvarūpa rishi ke paas jao”
👉 “Woh tumhari help karenge”

🙇‍♂️ Devtaon ki request

Devta Viśvarūpa ke paas gaye
aur pyaar se bole:

“Please hume apna guru bana lo 🙏”

🤔 Viśvarūpa ka doubt

Viśvarūpa bole:

👉 “Guru banna easy nahi hota…”
👉 “Isse spiritual power kam ho sakti hai”

Par phir bhi…
unhone help karne ka decide kiya ❤️

🛡️ Protection mantra

Viśvarūpa ne Indra ko ek special protection diya:

👉 Nārāyaṇa Kavacha ✨

Yeh ek divine shield tha 🛡️

💥 Victory

Is power ke saath:

👉 Indra strong ho gaya 💪
👉 aur asuro ko hara diya ⚔️

🌈 Final sach

👉 Ghamand downfall laata hai
👉 Guru ka respect sabse important hai

🌟 Moral:

Jo apne guru aur elders ka respect karta hai,
wahi life mein sachchi jeet paata hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 8
    with st.expander("Chapter 8 - The Nārāyaṇa-Kavaca explained"):
        text1 = """ 
        🛡️ Raja ka sawaal

Raja Parikshit ne poocha,
“Woh kaunsa powerful mantra hai…
jisse Indra ne apne enemies ko hara diya?” 🤔"""
        create_image_text_layout(
            "attached_assets/chapter6/6.8.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        🧘‍♂️ Rishi ka jawab

Śuka rishi bole,
“Yeh hai Nārāyaṇa Kavach —
ek divine protection shield!” ✨

🚿 Shuruaat ka rule

Rishi ne bataya:

👉 Pehle apne haath-pair dholo 🚿
👉 mann shant karo 🧘‍♂️
👉 aur Bhagwan ko yaad karo 🙏

🔤 Mantra ki shakti

Insaan ko yeh mantra bolna chahiye:

👉 “Om Namo Nārāyaṇāya”
👉 “Om Namo Bhagavate Vāsudevāya”

Yeh mantra body ko
spiritual armour bana deta hai 🛡️

🌍 Bhagwan har jagah

Phir insaan ko sochna chahiye:

👉 Bhagwan mere har body part mein hain
👉 woh mujhe protect kar rahe hain

🐟🐗 Bhagwan ke roop

Different situations mein
Bhagwan alag-alag roop se protect karte hain:

👉 Matsya (fish) → paani mein 🌊
👉 Varāha (boar) → dharti par 🌍
👉 Nṛsiṃha (lion-man) → danger mein 🦁
👉 Vāmana → har jagah ✨

🛡️ Har direction se protection

Rishi bole:

👉 Bhagwan har direction se protect karte hain
👉 upar, neeche, andar, bahar… sab jagah ✨

⚔️ Divine weapons

Bhagwan ke weapons bhi protect karte hain:

👉 Sudarshan Chakra 🔥
👉 Gada 💥
👉 Shankh 📯
👉 Talwar ⚔️

Yeh sab evil forces ko destroy kar dete hain.

😈 Darr khatam

Is kavach se:

👉 bhoot, pret, rakshas 👻
👉 animals 🐅
👉 enemies ⚔️

👉 sabka darr khatam ho jaata hai 😲

🧠 Strong mind

Jo insaan:

👉 is mantra ko yaad karta hai
👉 aur dhyaan lagata hai

👉 uska mann strong ho jaata hai 💪

📖 Ek example

Ek Brahman ne yeh kavach use kiya…
aur uski bones bhi powerful ho gayi 😲

Jisne unhe touch kiya…
woh bhi affected ho gaya!

🏆 Indra ki jeet

Indra ne bhi yeh kavach use kiya:

👉 aur asuro ko hara diya ⚔️
👉 aur teenon lok jeet liye 🌍

🌈 Final sach

👉 Bhagwan ka naam = protection
👉 Bhakti = sabse strong shield

🌟 Moral:

Sachchi protection bahar se nahi,
andar ki shraddha aur bhakti se milti hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 9
    with st.expander("Chapter 9 - Viśvarūpa killed—Gods defeated by Vṛtra, advised to approach Dadhīci"):
        text1 = """ 
        ⚔️ Viśvarūpa ki galti

Śuka rishi ne bataya,
“Viśvarūpa devtaon ka guru ban gaya tha…”

Par uske andar ek problem thi 😟

👉 woh secretly asuro ko bhi help karta tha

Kyuki uski maa asur side se thi."""
        create_image_text_layout(
            "attached_assets/chapter6/6.9.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        😠 Indra ka gussa

Jab Indra ko yeh pata chala…

👉 woh gussa ho gaya 😡
👉 aur usne Viśvarūpa ko maar diya ⚔️

⚠️ Paap ka bojh

Par ek problem ho gayi…

👉 Viśvarūpa ek Brahman tha
👉 use maarna bada paap tha 😨

Isliye Indra ne apna paap baant diya:

dharti 🌍
paani 🌊
ped 🌳
aur women
😈 Vṛtra ka janam

Viśvarūpa ke pita Tvaṣṭṛ ne badla lene ke liye
ek yajna kiya 🔥

Aur usse paida hua ek bhayanak asur — Vṛtra 😈

😱 Vṛtra ka roop

Vṛtra:

bahut bada tha 😲
uski aankhen darawni thi 👀
woh aasman ko chhoo raha tha ☁️

Log use dekh kar darr gaye 😨

⚔️ Devta haar gaye

Devtaon ne usse fight ki…

👉 par Vṛtra ne unke weapons bhi nigal liye 😱

Sab devta haar gaye 😔

🙏 Bhagwan se help

Phir sab milkar Bhagwan Vishnu ke paas gaye 🙏

Aur bole,
“Bas aap hi hume bacha sakte ho…”

✨ Bhagwan ka darshan

Bhagwan unke saamne prakat hue 🌟

Sab devta khush ho gaye 😊
Aur unhe pranam kiya।

💡 Bhagwan ka solution

Bhagwan bole:

👉 “Tumhe ek special weapon chahiye” ⚔️

👉 “Iske liye jao rishi Dadhīci ke paas”

👉 “Woh apni haddiyan (bones) denge”

👉 “Unse powerful weapon banega”

🛡️ Ultimate plan

Bhagwan ne kaha:

👉 “Us weapon se tum Vṛtra ko hara sakte ho”

👉 “Aur apni shakti wapas paoge” 💪

🌈 Final sach

👉 Galat kaam ka result hamesha milta hai
👉 par Bhagwan hamesha solution dete hain

🌟 Moral:

Galti se problem aati hai,
par shraddha aur sahi marg se solution milta hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 10
    with st.expander("Chapter 10 - With Vajra forged, Indra fights"):
        text1 = """ 
        🙏 Dadhīci ka balidaan

Śuka rishi ne bataya,
“Devta Dadhīci rishi ke paas gaye…”

Unhone kaha,
“Please hume apni haddiyan de dijiye…
hume Vṛtra ko haraana hai.” 😟"""
        create_image_text_layout(
            "attached_assets/chapter6/6.10.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        😌 Rishi ka jawab

Dadhīci muskuraaye 😊
Aur bole,

“Yeh body toh ek din waise bhi chali jayegi…”

“Toh agar yeh kisi ke kaam aa jaaye…
toh isse achha kya?” ❤️

💖 Sacrifice ka sach

Rishi ne kaha:

👉 “Jo dusron ke liye apni body bhi de de…”
👉 “Wahi sachcha mahaan insaan hai” ✨

🧘‍♂️ Mahaan tyag

Phir Dadhīci ne:

👉 dhyaan lagaya 🧘‍♂️
👉 apni aatma ko Brahman mein mila diya

Aur apna sharir chhod diya 🙏

⚡ Vajra ka janam

Devtaon ne:

👉 unki haddiyan li
👉 aur Viśvakarma ne unse banaya —
👉 Vajra (thunderbolt weapon) ⚡

👑 Indra ready

Ab Indra:

👉 Airāvata par baitha 🐘
👉 haath mein Vajra liya ⚡
👉 aur battle ke liye ready ho gaya 💥

⚔️ Maha yudh

Narmada nadi ke paas
ek bada yudh shuru hua ⚔️

👉 Devta vs Asur 😈

😈 Asuro ka attack

Asuro ne:

👉 talwar ⚔️
👉 teer 🏹
👉 gada 💥

sab kuch use kiya

Par devta sab rok rahe the 💪

😨 Asur dar gaye

Jab unke attacks fail ho gaye…

👉 asur dar gaye 😟
👉 aur bhagne lage

😄 Vṛtra ka speech

Par Vṛtra hansa 😄
Aur bola:

“Darr kyun rahe ho?”

👉 “Death toh sabko aani hai”
👉 “Toh darr kar kyun bhaagna?”

🦁 Warrior ka mindset

Vṛtra bola:

👉 “Best death kya hai?”

Dhyaan mein marna 🧘‍♂️
Ya battlefield mein ladte hue marna ⚔️

👉 “Darr ke bhaagna galat hai!”

🌈 Final sach

👉 Sacrifice se hi jeet milti hai
👉 aur himmat sabse badi power hai

🌟 Moral:

Jo dusron ke liye tyag karta hai aur himmat se ladta hai,
wahi sachcha veer hota hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 11
    with st.expander("Chapter 11 - Vṛtra, Hari’s devotee, fights"):
        text1 = """ 
        Ek baar ek powerful Asura tha, jiska naam Vritra tha. Woh apni sena ko samjha raha tha.

Lekin uski sena darr gayi thi.
Woh sab bhaagne lage aur uski baat nahi suni.

Yeh dekh kar Vritra ko gussa aa gaya.

Usne zor se chillaya,
“Jo bhaag rahe hain, unhe maarne me kya bahaduri hai?”"""
        create_image_text_layout(
            "attached_assets/chapter6/6.11.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        “Agar himmat hai, toh mere saamne aao!”

Uski awaaz itni powerful thi ki devta bhi darr gaye.

Kuch devta toh behosh ho gaye.

Vritra ne apni shakti se sabko daba diya.

Tab Indra wahan aaya.
Usne apna weapon Vritra par pheka.

Lekin Vritra ne use asaani se pakad liya.

Fir usne Indra ke haathi Airavat par attack kiya.
Airavat gir gaya aur injured ho gaya.

Indra thoda weak feel karne laga.

Lekin Vritra ne us waqt attack nahi kiya.

Indra ne apne haathi ko theek kiya aur phir ready ho gaya.

Tab Vritra ne Indra se kaha,
“Tumne mere bhai ko dhokhe se maara tha.”

“Ab main tumhe punishment dunga.”

Vritra gusse me tha, lekin uske words me sach tha.

Phir bhi usne ek alag baat kahi.

Usne bola,
“Main jeet ya haar se nahi darta.”

“Main sirf Bhagwan Hari ko yaad karta hoon.”

“Main unka bhakt hoon.”

Vritra ne kaha ki use power ya kingdom nahi chahiye.

Use sirf Bhagwan ke paas rehna hai.

Usne Indra se bola,
“Agar tum mujhe maaroge, toh bhi main khush rahunga.”

“Kyuki main Bhagwan ke paas chala jaunga.”

Vritra ka dil pure tha.

Woh ek strong warrior bhi tha aur ek true devotee bhi.

Moral:
Asli strength sirf power me nahi hoti, balki faith aur devotion me hoti hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 12
    with st.expander("Chapter 12 - Vṛtra slain by Indra"):
        text1 = """ 
        Vritra ab final battle ke liye ready tha. Usne apna trishul uthaya aur Indra par attack kiya.

Uska attack bahut powerful tha.

Lekin Indra shaant raha.
Usne apne Vajra se Vritra ka trishul aur uska haath kaat diya.

Phir bhi Vritra rukha nahi.
Usne gusse me Indra aur uske haathi Airavat par attack kiya.

Indra ka weapon haath se gir gaya."""
        create_image_text_layout(
            "attached_assets/chapter6/6.12.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Sab log tension me aa gaye.

Tab Vritra ne ek surprising baat boli.
Usne kaha, “Indra, apna weapon uthao aur mujhe maaro.”

“Yeh fight ka time hai, darne ka nahi.”

Vritra ne samjhaya,
“Jeet ya haar sirf hum par depend nahi karti.”

“Sab kuch Bhagwan aur time decide karta hai.”

Uski baatein bahut deep thi.

Indra ne yeh sun kar respect feel kiya.

Phir dono ne fir se fight shuru ki.

Indra ne Vritra ke dusre haath bhi kaat diye.

Vritra fir bhi fight karta raha.

Woh itna bada ho gaya ki usne Indra aur Airavat ko nigal liya.

Sab log darr gaye.

Lekin Indra andar se safe tha.

Usne apne Vajra se Vritra ke andar se attack kiya.

Phir woh bahar nikla aur Vritra ka sir kaat diya.

Vritra gir gaya aur uska end ho gaya.

Sab devta khush ho gaye.
Unhone Indra ki tareef ki aur phool barsaye.

Us samay ek roshni Vritra ke sharir se nikli.
Woh seedha Bhagwan me mil gayi.

Yeh dikha ki Vritra ek sachcha bhakt tha.

Moral:
Sachchi bhakti aur pure dil wale log akhir me Bhagwan tak pahunch hi jaate hain."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 13
    with st.expander("Chapter 13 - The Triumph of Indra"):
        text1 = """ 
        Jab Vritra ka ant hua, tab sab log khush ho gaye.
Teenon lok me shanti aa gayi.

Lekin ek ajeeb baat hui.
Sab khush the, par Indra khush nahi tha.

Raja ne poocha, “Indra dukhi kyun hai?”"""
        create_image_text_layout(
            "attached_assets/chapter6/6.13.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Tab rishi ne bataya,
“Indra ko darr tha ki usne ek Brahman ko maara hai.”

Usse laga ki usne paap kiya hai.

Rishiyon ne usse samjhaya,
“Tum ek bada yagya karo. Sab theek ho jayega.”

Lekin Indra ka darr kam nahi hua.

Jab usne Vritra ko maara, tab paap uske peeche aa gaya.

Woh paap ek darawni aurat ke roop me tha.
Woh Indra ka peecha kar rahi thi.

Indra bahut darr gaya.
Woh har jagah bhaagne laga.

Aakhir me woh ek jheel me chhup gaya.

Wahan woh bahut saalon tak chup raha.
Woh bas sochta raha ki apni galti kaise sudhare.

Tab tak swarg ka rajya kisi aur ne sambhala.

Lekin dheere-dheere Indra ne Bhagwan Vishnu ka dhyaan kiya.

Uski galti ka bojh kam hone laga.

Fir rishiyon ne use wapas bulaya.

Indra ne ek bada yagya kiya aur Bhagwan ki pooja ki.

Uske baad uska paap khatam ho gaya.

Woh phir se apne purane roop me aa gaya.

Moral:
Galti ho jaye, toh use accept karke sudharna hi asli jeet hoti hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 14
    with st.expander("Chapter 14 - The Previous Birth of Vṛtra—King Citraketu"):
        text1 = """ 
        Ek din Raja Parikshit ne poocha,
“Vritra itna bada Rakshasa hote hue bhi Bhagwan ka bhakt kaise tha?”

Rishi ne kaha, “Iske peeche ek purani kahani hai.”

Bahut pehle ek raja tha, jiska naam Citraketu tha.
Woh bahut powerful aur rich tha.

Uske paas sab kuch tha, lekin ek problem thi.
Uske koi santaan nahi thi."""
        create_image_text_layout(
            "attached_assets/chapter6/6.14.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Is wajah se woh hamesha dukhi rehta tha.

Ek din ek rishi uske mahal aaye.
Raja ne unka respect kiya aur unse madad maangi.

Raja bola,
“Mere paas sab kuch hai, par ek bachcha nahi hai.
Mujhe ek santaan chahiye.”

Rishi ne uski madad ki.
Unhone ek special prasad diya.

Raja ki ek rani ne woh prasad khaya.
Kuch time baad usse ek beta hua.

Sab log bahut khush ho gaye.

Raja apne bete se bahut pyaar karta tha.
Woh usi ke saath zyada time spend karta tha.

Baaki raniyan is baat se jealous ho gayi.

Unhone socha,
“Humari koi value nahi hai.”

Jealousy badhti gayi aur unhone ek galat kaam kar diya.

Unhone bachche ko poison de diya.

Bachcha mar gaya.

Jab maa ne dekha, woh shock me aa gayi.
Woh zor-zor se rone lagi.

Sab log dukhi ho gaye.

Raja bhi toot gaya.
Woh apne bete ke paas gir gaya aur ro pada.

Pura mahal dukh se bhar gaya.

Jo raniyan galti kar chuki thi, woh bhi pretend kar rahi thi ki woh dukhi hain.

Sab jagah sirf rona aur dard tha.

Tabhi wohi rishi wapas aaye, apne saath ek aur mahan rishi ko lekar.

Moral:
Jealousy aur ego hamesha dukh aur destruction laate hain."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 15
    with st.expander("Chapter 15 - Consolation of Citraketu"):
        text1 = """ 
        Raja Citraketu apne bete ke paas ro raha tha.
Woh bilkul toot chuka tha.

Tabhi do mahan rishi aaye – Angiras aur Narada.

Unhone pyaar se raja ko uthaya aur samjhaya."""
        create_image_text_layout(
            "attached_assets/chapter6/6.15.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Rishi bole,
“Raja, tum itna dukhi kyun ho?”

“Yeh batao, kya yeh bachcha hamesha tumhara tha?”

Raja chup ho gaya.

Rishi ne kaha,
“Jaise paani me ret ke dane milte aur alag hote hain, waise hi log milte aur bichhadte hain.”

“Sab kuch time ke saath badalta hai.”

“Yeh body alag hai, aur soul alag hai. Soul kabhi nahi marta.”

Raja dhyan se sunne laga.

Rishi ne fir kaha,
“Jo cheezein tumhari lagti hain – jaise family, paisa, power – yeh sab temporary hain.”

“Yeh sab ek sapne ki tarah hain.”

Raja ka dukh thoda kam hone laga.

Usne poocha,
“Aap kaun hain? Aapne mujhe itni gehri baat samjhayi.”

Tab rishi bole,
“Main Angiras hoon. Maine hi tumhe beta diya tha.”

“Aur yeh Narada hain.”

Raja hairaan ho gaya.

Rishi ne kaha,
“Tumne beta maanga tha, isliye humne diya.”

“Ab tum samajh gaye ho ki attachment kitna dukh deta hai.”

“Yeh duniya ki cheezein hamesha ke liye nahi hoti.”

Raja dheere-dheere strong banne laga.

Narada ne kaha,
“Ab tum apna mann Bhagwan par lagao.”

“Dhyaan karo aur sach ko samjho.”

Raja ne unki baat maan li.

Usne apne dukh ko control kiya aur spiritual path par chalna shuru kiya.

Moral:
Attachment kam karo, tabhi dukh kam hoga aur mann shaant rahega."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 16
    with st.expander("Chapter 16 - Citraketu’s Realization of Lord Ananta"):
        text1 = """ 
        Raja Citraketu ab thoda strong ho gaya tha, lekin uska mann ab bhi sach ki khoj me tha.

Rishi Narada ne ek din usse ek special mantra sikhaya.

Raja ne poore mann se us mantra ka dhyaan karna shuru kiya.

Woh sirf paani pe reh kar tapasya karne laga.

7 din tak usne full focus se meditation kiya.

Phir ek din uske saamne ek divine darshan hua."""
        create_image_text_layout(
            "attached_assets/chapter6/6.16.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Usne Bhagwan Ananta ko dekha.

Bhagwan bahut sundar aur powerful lag rahe the.

Unhe dekh kar Citraketu ke aansu nikal aaye.

Uska dil bhakti se bhar gaya.

Woh jhuk kar unhe pranam karne laga.

Kuch der tak woh bol bhi nahi paaya, itna emotional ho gaya tha.

Phir usne shanti se Bhagwan ki stuti ki.

Usne kaha,
“Hey Prabhu, aap sabse bade ho. Sab kuch aapse hi aata hai.”

“Duniya ki sab cheezein temporary hain, par aap hamesha rehte ho.”

Bhagwan Ananta usse dekh kar khush ho gaye.

Unhone kaha,
“Tumne sahi raasta chun liya hai.”

“Main hi sabka soul hoon. Sab kuch mujh me hi hai.”

“Jo mujhe samajh leta hai, use sach me shanti milti hai.”

“Jo log sirf duniya ke peeche bhaagte hain, unhe kabhi true happiness nahi milti.”

Citraketu dhyan se sunta raha.

Usne sab samajh liya.

Ab uska mann bilkul shaant ho gaya tha.

Thodi der baad Bhagwan wahan se antardhyan ho gaye.

Lekin Citraketu ke andar ab ek nayi roshni aa chuki thi.

Moral:
True happiness bahar nahi, andar aur Bhagwan se connection me hoti hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 17
    with st.expander("Chapter 17 - Citraketu cursed by Pārvatī"):
        text1 = """ 
        Citraketu ab ek powerful yogi ban chuka tha.
Woh aasman me ghoomta tha aur Bhagwan Hari ka naam leta tha.

Ek din woh apne vimaan me ja raha tha.

Tab usne ek ajeeb scene dekha.

Bhagwan Shiva sab rishiyon ke beech baithe the.
Aur Maa Parvati unki godh me baithi thi."""
        create_image_text_layout(
            "attached_assets/chapter6/6.17.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Yeh dekh kar Citraketu thoda hans pada.

Usne mazaak me bola,
“Yeh to bade guru hain, phir bhi sabke saamne aise baithe hain.”

Sab log chup ho gaye.

Bhagwan Shiva ne is baat par gussa nahi kiya.
Woh sirf muskura diye.

Lekin Maa Parvati ko yeh baat buri lag gayi.

Unhone gusse me Citraketu ko shraap diya,
“Tum ab ek Rakshasa ke roop me janam loge!”

Sab shock ho gaye.

Lekin Citraketu ne bilkul gussa nahi kiya.

Woh shanti se jhuk gaya aur bola,
“Main aapka shraap accept karta hoon.”

“Jo bhi hota hai, woh Bhagwan ki marzi se hota hai.”

“Na koi dukh deta hai, na koi khushi deta hai. Sab karma ka result hai.”

Uski baat sun kar sab hairaan ho gaye.

Bhagwan Shiva ne Maa Parvati se kaha,
“Dekho, yeh ek sachcha bhakt hai.”

“Isse koi farak nahi padta curse ho ya blessing.”

Maa Parvati ka gussa shaant ho gaya.

Baad me Citraketu ne Rakshasa ke roop me janam liya.
Wahi aage chal kar Vritra bana.

Lekin uske andar bhakti waise hi bani rahi.

Moral:
True bhakt har situation me calm rehta hai, chahe curse ho ya blessing."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 18
    with st.expander("Chapter 18 - The Birth of the Maruts"):
        text1 = """ 
        Ek baar Diti apne dono bete ke marne se bahut dukhi thi.
Uske dil me gussa bhar gaya tha.

Usne socha,
“Mujhe ek aisa beta chahiye jo Indra ko hara sake.”

Isliye usne apne pati Kashyap rishi ki seva shuru ki.

Woh unka bahut dhyaan rakhti thi.
Pyar se baat karti thi aur unhe khush rakhti thi."""
        create_image_text_layout(
            "attached_assets/chapter6/6.18.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Kashyap rishi usse khush ho gaye.

Unhone bola,
“Maang lo jo tumhe chahiye.”

Diti ne turant kaha,
“Mujhe ek aisa beta chahiye jo Indra ko maar sake.”

Yeh sun kar Kashyap rishi thode tension me aa gaye.

Lekin unhone ek condition rakhi,
“Agar tum 1 saal tak ek special vrat follow karogi, tab tumhe aisa beta milega.”

Diti maan gayi aur vrat start kar diya.

Usne bahut strict rules follow kiye.

Udhar Indra ko yeh baat pata chal gayi.

Woh darr gaya ki future me koi usse hara dega.

Isliye woh Diti ke paas seva karne laga.

Lekin asli reason yeh tha ki woh uski galti dhundh raha tha.

Diti almost perfect thi.
Indra ko koi chance nahi mil raha tha.

Phir ek din Diti thak gayi.
Woh bina proper rules follow kiye so gayi.

Bas, Indra ko mauka mil gaya.

Woh magic se uske womb me gaya.

Usne fetus ko tod diya.

Lekin ek miracle hua.
Woh mar nahi paaya.

Woh 49 parts me divide ho gaya.

Woh sab bachche zinda ho gaye.

Woh sab Marut dev ban gaye.

Subah Diti ne dekha ki uske 49 bachche hain.
Woh hairaan ho gayi.

Usne Indra se poocha kya hua.

Indra ne sach bata diya aur maafi maangi.

Diti ne use maaf kar diya.

Sab bachche Indra ke saath devta ban gaye.

Moral:
Gussa aur badla kabhi sahi result nahi deta, lekin maafi aur bhakti se sab theek ho sakta hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 19
    with st.expander("Chapter 19 - The Details of the Vow called Puṃsavana"):
        text1 = """ 
        Raja ne rishi se poocha,
“Yeh Puṃsavana vrat kya hota hai?”

Rishi ne shanti se samjhaya.

Unhone bola,
“Yeh ek special vrat hai jo Bhagwan Vishnu ko khush karta hai.”

“Isse insaan apni wishes poori kar sakta hai.”"""
        create_image_text_layout(
            "attached_assets/chapter6/6.19.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Rishi ne bataya ki yeh vrat ek saal tak follow karna hota hai.

Roz subah naha kar saaf kapde pehenne chahiye.

Phir Bhagwan Vishnu aur Maa Lakshmi ki pooja karni chahiye.

Unhe phool, diya aur food offer karna chahiye.

Dil se unka naam lena chahiye.

Rishi ne kaha,
“Pooja ke baad thoda food agni me chadhana chahiye.”

“Phir bacha hua prasad khana chahiye.”

Yeh sab daily karna hota hai.

Is vrat me discipline bahut important hai.

Husband aur wife dono milkar bhi kar sakte hain.

Agar wife nahi kar paaye, toh husband bhi kar sakta hai.

Rishi ne kaha,
“Is vrat ko kabhi beech me nahi chhodna chahiye.”

“Poore mann se follow karna chahiye.”

Akhri din fast rakhna hota hai.

Phir special pooja karke vrat complete hota hai.

Rishi ne bataya,
“Jo is vrat ko sahi se karta hai, uski wishes poori hoti hain.”

“Life me happiness, health aur good fortune milta hai.”

Raja yeh sab sun kar khush ho gaya.

Usse samajh aa gaya ki faith aur discipline kitne important hain.

Moral:
Faith aur consistency se hi life me success aur blessings milti hain."""
        create_image_text_layout(text_content=text2, layout="full")
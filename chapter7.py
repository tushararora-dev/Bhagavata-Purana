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
    create_image_text_layout("attached_assets/chapter7/chapter7.jpg", layout="full")
    # Book 7 - Seventh Skandha
    text0 = """
    <h2>Book 7 - Seventh Skandha</h2>
    """
    # Book 7 - Seventh Skandha

    # Chapter 1
    with st.expander("Chapter 1 - Conversation between Yudhiṣṭhira and Nārada: Jaya and Vijaya cursed"):
        text1 = """ 
        
        Raja Parikshit ke mann me ek doubt aaya.
Usne rishi se poocha,
“Bhagwan sabke liye same hain, phir woh Asuro ko kyun maarte hain?”

“Unhe toh kisi se na pyaar, na nafrat hoti hai.”

Rishi ne muskura kar jawab diya."""
        create_image_text_layout(
            "attached_assets/chapter7/7.1.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Unhone kaha,
“Bhagwan kisi se partial nahi hote.”

“Woh bas samay aur nature ke hisaab se kaam karte hain.”

“Jab achhai badh rahi hoti hai, toh woh usse support karte hain.”

“Jab burai badh jaati hai, toh woh use rok dete hain.”

Raja dhyan se sun raha tha.

Phir rishi ne ek aur interesting baat batayi.

Unhone bola,
“Insaan Bhagwan ko alag-alag emotions se yaad kar sakta hai.”

“Koi pyaar se, koi darr se, koi dosti se.”

“Chahe nafrat se bhi yaad karo, phir bhi mann Bhagwan par hi rahega.”

Raja hairaan ho gaya.

Usne poocha,
“Kaise?”

Rishi ne example diya,
“Jaise ek keeda wasp ko sochta rehta hai,
toh woh us jaisa ban jaata hai.”

“Waise hi jo bhi Bhagwan ko yaad karta hai,
woh unke paas pahunch jata hai.”

Phir rishi ne ek purani kahani batayi.

Do dwarpal the—Jaya aur Vijaya.

Unhone galti se kuch rishiyon ko rok diya.

Rishiyon ne gusse me unhe shraap de diya.

Woh teen baar asur bankar janam lenge.

Pehle janam me woh Hiranyakashipu aur Hiranyaksha bane.

Phir Ravana aur Kumbhakarna bane.

Aur phir Shishupala aur Dantavakra bane.

Har baar Bhagwan ne unhe hara diya.

Aur aakhir me woh wapas Bhagwan ke paas chale gaye.

Raja ko sab samajh aa gaya.

Moral:
Bhagwan tak pahunchne ke liye mann ka focus zaroori hai—chahe woh pyaar se ho ya kisi aur emotion se."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 2
    with st.expander("Chapter 2 - Hiraṇyakaśipu consoles his mother and kinsmen"):
        text1 = """ 
        Jab Hiranyaksha mar gaya, tab uska bhai Hiranyakashipu bahut gusse aur dukh me tha.

Usne apne saare Asuro ko bulaya aur bola,
“Hum badla lenge!”

Usne kaha,
“Sab log dharti par jao aur achhe logon ko pareshaan karo.”"""
        create_image_text_layout(
            "attached_assets/chapter7/7.2.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Asuro ne uski baat maan li.

Unhone gaon, sheher aur ashram sab barbaad kar diye.

Log bahut dar gaye.

Sab jagah dukh aur darr fail gaya.

Phir Hiranyakashipu apne ghar walo ke paas gaya.

Uski maa aur rishtedaar ro rahe the.

Unhone unhe shanti se samjhaya.

Woh bola,
“Ek veer ki death par itna shok nahi karna chahiye.”

“Yeh duniya ek temporary jagah hai.”

“Jaise log milte hain aur alag ho jaate hain, waise hi life hai.”

“Body temporary hai, lekin soul kabhi nahi marta.”

Sab log dhyan se sunne lage.

Phir usne ek story batayi.

Ek raja tha, jo war me mar gaya.

Uski queens bahut ro rahi thi.

Tab ek chhota ladka wahan aaya.

Woh actually Yamraj the, jo unhe samjhane aaye the.

Unhone kaha,
“Jo chala gaya, woh wapas nahi aayega.”

“Body yahin hai, par soul chala gaya.”

“Jo janam leta hai, woh ek din marta hi hai.”

Phir unhone ek example diya.

Ek pakshi apni partner ke liye ro raha tha.

Lekin uski bhi death ho gayi.

Isse yeh samajh aata hai ki sabka end fix hai.

Yeh sab sun kar sabka dukh kam ho gaya.

Unhone sach ko accept kar liya.

Moral:
Life temporary hai, isliye zyada attachment dukh deta hai—samajh aur acceptance se hi shanti milti hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 3
    with st.expander("Chapter 3 - Hiraṇyakaśipu’s Penance—Brahmā grants Boons"):
        text1 = """ 
        Hiranyakashipu ke mann me ek strong desire tha.
Woh sabse powerful banna chahta tha.

Woh chahta tha ki use kabhi budhapa ya death na aaye.

Isliye woh ek pahad par gaya aur tapasya shuru ki."""
        create_image_text_layout(
            "attached_assets/chapter7/7.3.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Woh bahut hard tapasya kar raha tha.

Kabhi khana nahi, kabhi paani nahi.

Woh ek hi jagah khada raha, haath upar karke.

Time beet ta gaya.

Uski tapasya itni powerful thi ki uske body se aag nikalne lagi.

Puri duniya hilne lagi.

Samundar aur pahad bhi disturb ho gaye.

Devta darr gaye.

Woh Brahma ji ke paas gaye aur bole,
“Please isse rokiye, warna sab kuch destroy ho jayega.”

Brahma ji turant wahan gaye.

Hiranyakashipu ka body almost khatam ho chuka tha.
Sirf bones bache the.

Brahma ji ne apne kamandal ka paani us par dala.

Turant woh wapas strong body me aa gaya.

Woh bahut khush hua aur Brahma ji ko pranam kiya.

Brahma ji bole,
“Maango kya chahte ho.”

Hiranyakashipu ne smartly apni wishes batayi.

Usne bola,
“Mujhe kisi bhi insaan ya janwar se death na ho.”

“Na din me, na raat me.”

“Na ghar ke andar, na bahar.”

“Na zameen par, na aasman me.”

“Koi weapon mujhe maar na sake.”

Aur bhi bahut saari conditions rakhi.

Usne almost har situation cover kar li.

Brahma ji ne usse yeh sab vardaan de diye.

Ab Hiranyakashipu ko lagne laga ki woh invincible hai.

Uska confidence aur ghamand badh gaya.

Moral:
Power milne ke baad bhi vinamr rehna zaroori hai, warna ghamand insaan ko galat raaste par le jaata hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4
    with st.expander("Chapter 4 - Oppression of Hiraṇyakaśipu and Description of Prahlāda’s devotion"):
        text1 = """ 
        Brahma ji se vardaan milne ke baad Hiranyakashipu bahut powerful ban gaya.

Usne dheere-dheere poori duniya par control kar liya.

Devta, rishi, sab usse darrne lage."""
        create_image_text_layout(
            "attached_assets/chapter7/7.4.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Woh Indra ka mahal tak le gaya aur wahan rehne laga.

Sab log uski seva karne lage, chahe unhe pasand ho ya nahi.

Hiranyakashipu ko power mil gayi thi, lekin uska ghamand bhi badh gaya.

Woh Bhagwan Vishnu se nafrat karta tha.

Aur sabko majboor karta tha ki woh sirf uski hi pooja karein.

Log pareshaan ho gaye.

Sab milkar Bhagwan Vishnu se madad maangne lage.

Tab ek awaaz aayi,
“Darr mat, sab theek hoga.”

“Jab woh apne hi bete ko nuksaan pahunchane ki koshish karega, tab uska end hoga.”

Time beet ta gaya.

Hiranyakashipu ke chaar bete the.

Unme se ek tha Prahlad.

Prahlad bilkul alag tha.

Woh shant, kind aur sabse pyaar karne wala tha.

Uske andar bilkul bhi ghamand nahi tha.

Sabse important baat—
Woh Bhagwan Vishnu ka bahut bada bhakt tha.

Chhoti si age me hi woh Bhagwan ko yaad karta rehta tha.

Kabhi hasta, kabhi gaata, kabhi naachta—
Bas Bhagwan ke pyaar me rehta tha.

Usse duniya ki cheezo me interest hi nahi tha.

Woh sabko respect karta tha.

Garib logon ki help karta tha.

Sab usse pasand karte the.

Lekin uska apna father usse pasand nahi karta tha.

Kyunki Prahlad Vishnu ka naam leta tha.

Yeh baat Hiranyakashipu ko bilkul pasand nahi thi.

Yeh ek bade conflict ki shuruaat thi.

Moral:
Sach aur bhakti hamesha powerful hote hain, chahe duniya unke against hi kyun na ho."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 5
    with st.expander("Chapter 5 - The Life of Prahlāda—Hiraṇyakaśipu attempts to kill Prahlāda"):
        text1 = """ 
        Prahlad school jaata tha jahan use politics aur duniya ki baatein sikhayi jaati thi.

Woh sab kuch sunta tha, lekin uska mann in cheezon me nahi lagta tha.

Uska focus sirf Bhagwan Vishnu par tha."""
        create_image_text_layout(
            "attached_assets/chapter7/7.5.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Ek din uske papa Hiranyakashipu ne use pyaar se apni godh me bithaya.

Unhone poocha,
“Beta, tumhe kya sabse achha lagta hai?”

Prahlad ne seedha jawab diya,
“Sabse achha hai Bhagwan Hari ki bhakti karna.”

Yeh sun kar Hiranyakashipu gussa ho gaya.

Usne socha kisi ne Prahlad ko galat sikha diya hai.

Teachers ne kaha,
“Yeh uski apni soch hai.”

Phir ek din Hiranyakashipu ne Prahlad se bola,
“Jo tumne seekha hai, woh batao.”

Prahlad ne calmly kaha,
“Bhagwan ki bhakti ke 9 tarike hote hain.”

“Jaise unka naam sunna, gaana, yaad karna, seva karna aur unhe dost maan lena.”

Yeh sunte hi Hiranyakashipu aur bhi gussa ho gaya.

Usne Prahlad ko apni godh se gira diya.

Aur soldiers ko order diya,
“Isse maar do!”

Rakshas ne Prahlad par attack kiya.

Lekin Prahlad bilkul shaant baitha raha.

Uska mann Bhagwan me laga tha.

Isliye usse kuch nahi hua.

Phir Hiranyakashipu ne bahut attempts kiye.

Kabhi zeher diya,
kabhi aag me dala,
kabhi pahad se gira diya.

Lekin har baar Prahlad bach gaya.

Uski bhakti uski protection ban gayi.

Hiranyakashipu confuse aur darr gaya.

Use samajh nahi aa raha tha ki Prahlad ko kaise roke.

Udhar Prahlad apne friends ko bhi achhi baatein sikhane laga.

Woh sabko bhakti aur sach ka raasta dikha raha tha.

Moral:
Sachchi bhakti aur strong belief se har mushkil ko jeeta ja sakta hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6
    with st.expander("Chapter 6 - Prahlāda’s Teaching"):
        text1 = """ 
        Ek din Prahlad apne school ke friends ke saath baitha tha.
Usne unhe pyaar se bulaya aur bola,
“Doston, meri baat dhyaan se suno.”

“Life sirf khelne ke liye nahi hoti.”"""
        create_image_text_layout(
            "attached_assets/chapter7/7.6.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        “Bachpan se hi hume sach aur Bhagwan ko samajhna chahiye.”

Sab bachche uski baat sunne lage.

Prahlad ne kaha,
“Human life bahut rare hoti hai.”

“Yeh chhoti hai, par isse hum sabse bada goal achieve kar sakte hain.”

“Isliye time waste mat karo.”

Phir usne samjhaya,
“Jo sukh hum duniya me dhoondte hain, woh temporary hai.”

“Dukh bhi apne aap aata hai, sukh bhi.”

“Toh sirf inke peeche bhaagna bekaar hai.”

Bachche thoda confuse ho gaye.

Prahlad ne simple example diya,
“Zindagi 100 saal ki ho toh bhi aadha time sone me nikal jata hai.”

“Bachpan aur budhape me bhi time nikal jata hai.”

“Toh asli time bahut kam bachta hai.”

“Isliye use wisely use karo.”

Phir usne kaha,
“Log family, paisa aur desires me itne busy ho jaate hain ki apna asli goal bhool jaate hain.”

“Woh kabhi free nahi ho paate.”

“Jaise ek silkworm khud hi apna jaal bana kar usme phas jaata hai.”

Sab bachche ab seriously sun rahe the.

Prahlad ne aage kaha,
“Isliye buri sangati se door raho.”

“Aur Bhagwan Vishnu ki sharan me jao.”

“Sabke saath kindness aur friendship rakho.”

“Bhagwan sabke andar hain.”

“Unhe paana mushkil nahi hai.”

Bachchon ko ab samajh aane laga.

Unhone poocha,
“Yeh sab tumne kaise seekha?”

Prahlad muskura diya.

Woh unhe apni story batane wala tha.

Moral:
Time precious hai—use sirf duniya ke peeche waste na karke, sahi cheezon me lagana chahiye."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7
    with st.expander("Chapter 7 - Prahlāda, enlightened while in mother’s womb"):
        text1 = """ 
        Prahlad ke friends ne poocha,
“Tum itni badi baatein kaise jaante ho?”

Prahlad muskuraaya aur bola,
“Main tumhe apni kahani batata hoon.”

Usne kaha,
“Jab mere father tapasya kar rahe the, tab devta Asuro par attack kar rahe the.”

“Us time meri maa ko Indra le ja raha tha.”"""
        create_image_text_layout(
            "attached_assets/chapter7/7.7.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Woh bahut dar gayi thi.

Tab ek mahan rishi aaye—Narada.

Unhone Indra ko roka aur kaha,
“Is mahila ko chhod do.”

“Iske womb me ek mahaan bhakt hai.”

Indra ne unki baat maan li.

Narada ji meri maa ko apne ashram le gaye.

Wahan meri maa safe thi.

Narada ji ne use Bhagwan aur life ka gyaan diya.

Prahlad ne kaha,
“Main tab maa ke womb me tha.”

“Lekin maine woh sab suna aur samajh liya.”

“Woh gyaan abhi tak mere saath hai.”

Bachche hairaan ho gaye.

Prahlad ne aage samjhaya,
“Body change hoti rehti hai—janam, badhna, budhapa, death.”

“Lekin soul kabhi nahi badalta.”

“Woh hamesha same rehta hai.”

“Isliye ‘main’ aur ‘mera’ sochna galat hai.”

Phir usne kaha,
“Sach me hum sab ek hi Supreme power ka part hain.”

“Wahi sabke andar hai.”

“Usse hi samajhna sabse important hai.”

Prahlad ne simple words me bola,
“Bhagwan ko yaad karo, unki kahani suno, aur sabke saath achha behave karo.”

“Yahi sabse best life hai.”

Sab bachche ab inspired feel kar rahe the.

Unhe samajh aa gaya ki Prahlad itna special kyun hai.

Moral:
Sachcha gyaan aur bhakti kabhi waste nahi jaati—woh life bhar saath rehti hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 8
    with st.expander("Chapter 8 - Death of Hiraṇyakaśipu and Praise of Nṛsiṃha"):
        text1 = """ 
        Prahlad ki baatein sun kar sab bachche uski taraf ho gaye.
Unhone uski baat maan li.

Yeh dekh kar teachers darr gaye.
Unhone jaakar Hiranyakashipu ko sab bata diya.

Yeh sunte hi Hiranyakashipu gusse se kaanpne laga."""
        create_image_text_layout(
            "attached_assets/chapter7/7.8.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Usne Prahlad ko bulaya aur zor se daanta,
“Tu meri baat kyun nahi maanta?”

“Tu itna strong kaise hai?”

Prahlad ne calmly jawab diya,
“Sabki power ek hi source se aati hai—Bhagwan se.”

“Woh sab jagah hain.”

Hiranyakashipu aur gussa ho gaya.

Usne poocha,
“Agar Bhagwan har jagah hain, toh kya woh is pillar me bhi hain?”

Prahlad ne bina dare kaha,
“Haan, woh yahan bhi hain.”

Yeh sun kar Hiranyakashipu ne pillar par zor se maara.

Tabhi ek bahut zor ki awaaz hui.

Aur pillar se ek adbhut roop nikla—
na pura aadmi, na pura sher.

Woh tha Narasimha.

Uska roop bahut powerful aur darawna tha.

Hiranyakashipu ne us par attack kiya.

Lekin Narasimha ne use pakad liya.

Usne use na din me mara, na raat me—
shaam ke time.

Na andar, na bahar—
darwaze ke beech.

Na zameen par, na aasman me—
apni godh me bithakar.

Aur bina weapon ke,
apne naakhun se use maar diya.

Is tarah sab conditions follow ho gayi.

Sab devta khush ho gaye.

Woh aasman se phool barsane lage.

Lekin Narasimha ka gussa abhi shaant nahi hua tha.

Koi bhi unke paas jaane ki himmat nahi kar raha tha.

Tab Prahlad aage badha.

Woh bina dare unke paas gaya.

Usne jhuk kar pranam kiya.

Narasimha ka gussa turant shaant ho gaya.

Unhone Prahlad ko ashirwad diya.

Sab log khush ho gaye.

Moral:
Sachchi bhakti aur sachai hamesha jeet ti hai, chahe kitni bhi badi problem kyun na ho."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 9
    with st.expander("Chapter 9 - Prahlāda eulogizes Nṛsiṃha"):
        text1 = """ 
        Hiranyakashipu ke marne ke baad bhi sab log darr rahe the.
Bhagwan Narasimha ka gussa abhi bhi shaant nahi hua tha.

Brahma ji aur baaki devta paas jaane ki himmat nahi kar pa rahe the.

Unhone Maa Lakshmi ko bheja."""
        create_image_text_layout(
            "attached_assets/chapter7/7.9.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Lekin woh bhi unke roop ko dekh kar ruk gayi.

Tab Brahma ji ne Prahlad se kaha,
“Beta, tum hi jao.”

Prahlad dheere-dheere aage badha.

Woh bina dare Bhagwan ke paas gaya.

Usne jhuk kar pranam kiya.

Bhagwan Narasimha ka dil pighal gaya.

Unhone Prahlad ke sir par haath rakha.

Us touch se Prahlad ke andar divine gyaan aa gaya.

Uski aankhon me khushi ke aansu aa gaye.

Woh Bhagwan ki stuti karne laga.

Prahlad ne kaha,
“Main ek Asur family me paida hua hoon.”

“Phir bhi aapne mujh par itni kripa ki.”

“Na paisa, na power, na knowledge—
sirf sachchi bhakti hi aapko khush karti hai.”

Usne aur kaha,
“Log duniya ke sukh ke peeche bhagte hain,
lekin woh sab temporary hai.”

“Real shanti sirf aapki bhakti me hai.”

Prahlad ne apni wish bhi batayi.

Usne bola,
“Mujhe kuch nahi chahiye.”

“Bas mujhe aapki seva karni hai.”

“Main akela moksha nahi chahta.”

“Main chahta hoon sab log aap tak pahunch jayein.”

Bhagwan Narasimha bahut khush ho gaye.

Unhone kaha,
“Main tumse bahut prasann hoon.”

“Jo chaaho maang lo.”

Lekin Prahlad ne phir bhi kuch nahi maanga.

Uski bhakti bilkul nishkaam thi.

Moral:
Sabse shuddh bhakti wahi hoti hai jisme insaan kuch bhi badle me nahi maangta."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 10
    with st.expander("Chapter 10 - Prahlāda enthroned—The conquest of Tripura"):
        text1 = """ 
        Bhagwan Narasimha ne Prahlad se kaha,
“Tum jo chaho maang sakte ho.”

Lekin Prahlad muskura diya.

Usne bola,
“Mujhe koi reward nahi chahiye.”"""
        create_image_text_layout(
            "attached_assets/chapter7/7.10.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        “Main aapka bhakt hoon, koi deal karne wala vyapari nahi.”
“Sachcha bhakt kabhi badle me kuch nahi maangta.”
Bhagwan yeh sun kar bahut khush ho gaye.
Prahlad ne sirf ek hi baat maangi,
“Mere dil me kabhi koi desire na aaye.”
“Bas main hamesha aapki bhakti karta rahu.”
Phir Prahlad ne apne father ke liye bhi prarthana ki.
Usne kaha,
“Please mere pita ko maaf kar dijiye.”
Bhagwan ne pyaar se kaha,
“Tumhare jaise bhakt ke wajah se tumhare pita aur unki puri family ka uddhaar ho gaya.”
Prahlad khush ho gaya.
Phir Bhagwan ne use kaha,
“Ab tum raja banoge.”
“Apne kartavya nibhao, lekin mann hamesha mere paas rakho.”
Prahlad ne sab kuch accept kar liya.
Usne apne pita ke rituals poore kiye.
Phir use raja bana diya gaya.
Sab log usse respect karne lage.
Woh ek acha aur nyay-priya raja bana.
Sab kuch theek chal raha tha.
Baad me Bhagwan wahan se antardhyan ho gaye.
Devta bhi apne-apne lok me wapas chale gaye.
Prahlad apni praja ka dhyaan rakhte hue,
Bhagwan ki bhakti me jeene laga.
Moral:
Sacchi bhakti bina kisi expectation ke hoti hai, aur wahi insaan ko sabse upar le jaati hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 11
    with st.expander("Chapter 11 - The Eternal Path of Religion"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter7/7.11.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 12
    with st.expander("Chapter 12 - Inquiry into the Right Conduct"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter7/7.12.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 13
    with st.expander("Chapter 13 - The Code of Conduct for Saṃnyāsins"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter7/7.13.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 14
    with st.expander("Chapter 14 - The Duties of a householder"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter7/7.14.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 15
    with st.expander("Chapter 15 - Exposition of right Conduct (Concluded)"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter7/7.15.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")
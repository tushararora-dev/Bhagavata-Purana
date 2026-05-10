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
        text1 = """ 
        Rishi Shuka ne Solar Dynasty yani Ikshvaku vansh ki kahani sunani shuru ki.

👑 Ikshvaku ka Janm

Ek din Manu ji ko chheenk aayi 🤧

Aur unki naak se janm hua—

🌞 Ikshvaku

Jo Surya Vansh ke founder bane.

Unke 100 bete the.

Sabse famous the:

Vikukshi
Nimi
Dandaka"""
        create_image_text_layout(
            "attached_assets/chapter9/9.6.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        🐇 Vikukshi aur “Shashada”

Ek baar Ikshvaku ne Shraddha ritual ke liye
Vikukshi ko jungle bheja meat laane.

Woh hunting karke laut raha tha…
lekin bahut bhookha tha 😖

Usne ek khargosh (hare) kha liya. 🐇

Jab woh meat lekar ghar aaya,
Guru Vashishtha ne kaha:

“Yeh impure ho chuka hai.”

Ikshvaku ko gussa aa gaya 😠

Aur unhone Vikukshi ko kingdom se nikaal diya.

Baad me Vikukshi wapas aaya
aur king bana.

Kyunki usne hare khaya tha,
woh famous hua naam se—

🐇 Shashada

(“hare eater”)

🐂 Puranjaya / Kakutstha

Shashada ka beta tha—

⚔️ Puranjaya

Us time devas aur asuras ki huge war chal rahi thi.

Devas haar rahe the 😨

Unhone Puranjaya se help maangi.

Puranjaya ne condition rakhi:

👉 “Main fight karunga
agar Indra mera vehicle bane.”

Bhagwan Vishnu ki advice se
Indra ek huge bull 🐂 ban gaye.

Puranjaya us bull ke hump par baitha.

Isliye uska naam pada:

🐂 Kakutstha

(“bull ke hump par baithne wala”)

Usne terrifying battle me
asuras ko hara diya ⚔️🔥

Aur devas ko victory dilayi.

🌆 Shravasti City

Kakutstha ke descendants me
ek king hua—Shravasta.

Usne famous city banayi:

🏙️ Shravasti
🔥 Kuvalashva aur Dhundhu Asura

Baad me ek powerful king hua—

⚔️ Kuvalashva

Rishi Utanka ne usse request ki:

“Ek dangerous demon hai—Dhundhu.”

“Usse maaro.”

Kuvalashva apne
21,000 sons ke saath gaya 😮

Battle bahut terrifying thi.

Dhundhu ke mouth se fire nikli 🔥

Aur uske almost saare sons jal gaye 😢

Sirf 3 bache.

Lekin Kuvalashva ne finally Dhundhu ko maar diya.

Isliye uska naam pada:

🔥 Dhundhumara

(“Dhundhu ko destroy karne wala”)

👶 Yuvanasva ka Strange Childbirth

Baad me ek king hua—

👑 Yuvanasva

Uske koi child nahi tha.

Rishis ne special yajna kiya
taaki usse beta mile.

Ek raat king ko bahut pyaas lagi 😓

Woh yajna hall me gaya
aur galti se woh sacred water pee gaya
jo queen ke liye tha. 😮

Kuch time baad…

👉 King khud pregnant ho gaya 😳

Aur uske right side se ek baby born hua.

Sab shock me the—

“Yeh baby kya piyega?”

Tab Indra aaye ☀️

Unhone apni finger baby ko di
jisme divine nectar tha.

Aur kaha:

👉 “Mam dhatta” (“mujhse piyo”)

Isliye baby ka naam pada:

🌟 Mandhata

Mandhata bada hokar
world emperor bana 👑

Usne poori earth par rule kiya.

🐟 Sage Saubhari ki Story

Ek sage the—

🧘 Saubhari

Woh Yamuna ke paani me tapasya karte the.

Ek din unhone fish couple ko romance karte dekha 🐟❤️🐟

Aur unke andar desire jag gaya.

Woh King Mandhata ke paas gaye
aur unki daughters se shaadi maangi.

King ne smartly bola:

👉 “Jo princess tumhe choose karegi,
usse shaadi kar lena.”

Saubhari ne apni yogic power se
khud ko super handsome bana liya ✨

Result? 😅

👉 Saari 50 princesses unse shaadi karna chahti thi!

Sab sisters aapas me argue karne lagi 😂

Saubhari ne sabse shaadi kar li 💍💍💍

Aur magical palaces create kar diye.

Woh luxury life enjoy karne lage.

Lekin…

Unki desires kabhi khatam nahi hui.

Unhe realise hua:

👉 “Desires fire ki tarah hoti hain…”
👉 “Jitna fuel do, utni badhti hain.”

Ek din unhe deep regret hua 😔

Unhone socha:

“Sirf ek fish ko dekhkar
main itna attach ho gaya…”

Tab unhone sab chhod diya.

Forest chale gaye 🌲

Unki wives bhi unke saath gayi.

Sabne tapasya ki.

Aur finally…

✨ Sabko moksha mil gaya.

Moral:

Desires kabhi satisfy nahi hoti
Real peace andar ki detachment me hoti hai
Aur even after falling, insaan spirituality ki taraf wapas aa sakta hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7
    with st.expander("Chapter 7 - The Story of King Hariścandra"):
        text1 = """         Rishi Shuka ne Solar Dynasty ki kahani aur aage badhai.

🐍 Purukutsa aur Naga Lok

King Mandhata ka beta tha—

👑 Purukutsa

Ek din Naag logon ne usse help ke liye bulaya.

Unki princess Narmada uski wife bani
aur use Rasatala (underworld) le gayi. 🐍"""
        create_image_text_layout(
            "attached_assets/chapter9/9.7.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
Wahan dangerous Gandharvas trouble kar rahe the.

Bhagwan Vishnu ki power se
Purukutsa ne sabko hara diya ⚔️🔥

Naag log bahut khush hue.

Unhone blessing di:

👉 “Jo bhi iss story ko yaad karega,
usse snakes ka dar nahi rahega.”

🌌 Trishanku ki Strange Story

Purukutsa ke descendants me
ek king hua—

👑 Satyavrata

jo famous hua naam se:

🌌 Trishanku

Uske father ne use curse diya
aur woh Chandala ban gaya. 😔

Lekin Rishi Vishwamitra ne uski help ki.

Trishanku ki wish thi:

👉 “Main apne physical body ke saath heaven jaana chahta hoon.”

Gods ne mana kar diya ❌

Lekin Vishwamitra ne apni tapasya ki power use ki 🔥

Aur Trishanku ko heaven bhej diya.

Gods ne use neeche gira diya 😮

Tab Vishwamitra ne gusse me kaha:

👉 “Ruko!” ✋

Aur Trishanku hawa me hi latak gaya 🌌

Aaj bhi usse sky me symbolic form me yaad kiya jaata hai.

👶 King Harishchandra aur Varuna

Trishanku ka beta tha—

👑 Harishchandra

Woh bahut famous king tha,
lekin uski ek problem thi—

👉 Uska koi child nahi tha 😔

Narada ji ne advice diya:

“Varuna dev ki worship karo.”

Harishchandra ne prayer ki:

👉 “Mujhe beta de do…”
👉 “Main use sacrifice kar dunga.”

Varuna maan gaye.

Aur ek beta paida hua—

👶 Rohita

Lekin jab Varuna ne promise yaad dilaya…

Toh Harishchandra delay karne laga 😅

“Abhi baby chhota hai…”

“Abhi daant nahi aaye…”

“Abhi naye daant aaye hain…”

“Abhi armour pehenne layak nahi hua…”

Woh bas excuses deta gaya 😢

Kyuki woh apne bete se bahut pyaar karta tha.

🌲 Rohita Runs Away

Rohita ko pata chal gaya
ki uski sacrifice hone wali hai 😨

Woh bow lekar forest bhaag gaya.

Meanwhile…

Varuna ne Harishchandra ko disease de diya—

🤒 Dropsy (Mahodara)

Rohita ghar lautna chahta tha,
lekin Indra har saal ek old Brahmana ka disguise lekar aate 😮

Aur bolte:

👉 “Abhi mat jao.”
👉 “Holy places travel karo.”

Yeh 6 saal tak chalta raha.

😢 Sunahshepa

Finally Rohita ko ek poor Brahmana mila—

Ajigarta

Usne apna middle son bech diya—

👦 Sunahshepa

Taaki uski jagah sacrifice ho sake. 😢

Harishchandra ne usse sacrificial victim bana diya.

Us yajna me great sages aaye:

Vishwamitra
Vashishtha
Jamadagni

Sab present the.

Sacrifice complete hua
aur Harishchandra disease se free ho gaya.

Indra ne usse golden chariot bhi diya ✨

🧘 Final Spiritual Wisdom

Baad me Vishwamitra ne
king aur queen ko highest spiritual knowledge diya.

Unhone samjhaya:

👉 Mind ko control karo
👉 Sab elements ko dissolve karo mentally

Earth → Water → Fire → Air → Space → Beyond

Aur finally…

👉 Ego aur ignorance ko destroy karo

Tab insaan apne real self ko realise karta hai. ✨

Yeh state words aur logic se bhi beyond hoti hai.

Moral:

Attachment aur promises ke beech conflict life ka part hai
Desires aur fear insaan ko confuse karte hain
Lekin ultimate peace self-realisation aur truth me hi milti hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 8
    with st.expander("Chapter 8 - The Story of King Sagara"):
        text1 = """ 
        Rishi Shuka ne Surya Vansh ki kahani aur aage sunayi—
aur iss baar focus tha Bhagwan Ram par.

👑 Raghu Vansh

King Khatvanga ke baad aaye:

Dirghabahu
Raghu
Aja
Dasharatha

Aur Dasharatha ke ghar janm liya—"""
        create_image_text_layout(
            "attached_assets/chapter9/9.8.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        🌟 Bhagwan Ram

Bhagwan Vishnu ne khud ko 4 parts me divide kiya:

Ram
Lakshman
Bharat
Shatrughna

Ram main form the,
baaki unke divine expansions.

🌸 Ram aur Sita

Ram ne Vishwamitra ke yagya ko demons se protect kiya.

Single-handedly Maricha aur dusre rakshason ko hara diya ⚔️🔥

Phir Sita swayamvar hua.

Wahan Shiva ji ka gigantic bow rakha gaya tha 🏹

Jise uthana hi impossible tha.

Ram ne us bow ko easily uthaya…

Aur string karte hi—

💥 Bow toot gaya!

Sab shock me aa gaye 😮

Aur Ram ne Sita ji se shaadi ki 💍

🌲 Forest Exile

Kaikeyi ke boons ki wajah se
Dasharatha ko Ram ko exile bhejna pada. 😢

Ram ne bina complain kiye:

Kingdom chhod diya
Palace chhod diya
Luxury chhod di

Bilkul ek yogi ki tarah.

Sita aur Lakshman bhi saath gaye 🌲

😈 Surpanakha aur Ravana

Forest me Surpanakha aayi
aur Ram se attract ho gayi 😅

Lakshman ne uski naak kaat di ✂️

Is insult ka badla lene ke liye
Ravana ne Sita ji ko kidnap kar liya 😨

🦅 Jatayu ki Sacrifice

Ek brave vulture king tha—

🦅 Jatayu

Usne Ravana ko rokne ki koshish ki.

Lekin battle me woh mar gaya 😢

Ram ne uske funeral rites khud kiye.

🐒 Hanuman aur Monkey Army

Ram ki friendship hui Sugriva aur Hanuman se 🐒

Hanuman Lanka gaye,
Sita ji ko dhoonda,
aur Lanka jala di 🔥

🌊 Ram Setu

Ram ocean ke paas aaye.

3 din tak ocean god ne answer nahi diya.

Ram gusse me aa gaye 😠

Ocean god darr gaya
aur saamne aa kar bola:

👉 “Aap bridge bana lijiye.”

Monkey army ne mountains aur trees use karke
Ram Setu bana diya 🌉

Aur army Lanka pahunch gayi.

⚔️ Great War of Lanka

Huge battle start hui.

Rakshasa side:

Indrajit
Kumbhakarna
Prahasta
Atikaya

Monkey side:

Hanuman
Angad
Jambavan
Sugriva

Finally Ram aur Ravana ka face-off hua 🔥

Ravana Pushpaka Vimana me tha.

Ram divine chariot me.

Ram ne Ravana ko warning di:

👉 “Tumne coward ki tarah Sita ko churaya.”

👉 “Ab tumhe apne karma ka phal milega.”

Phir Ram ne divine arrow chhoda 🏹

Arrow seedha Ravana ke heart me laga 💥

Aur Ravana gir gaya.

😢 Lanka ki Women Cry

Ravana ki queens aur women battlefield me aayi.

Sab ro rahi thi 😭

Mandodari boli:

👉 “Tum Sita ji ki purity aur power ko samajh nahi paaye…”

“Isi wajah se tumhara downfall hua.”

🌸 Ram Meets Sita

War ke baad Ram ne Sita ji ko Ashoka Vatika me dekha 🌸

Woh weak aur sad thi separation ki wajah se.

Ram emotionally moved ho gaye 😢

👑 Return to Ayodhya

Ram ne Vibhishana ko Lanka ka king banaya.

Phir Pushpaka Vimana se Ayodhya laut aaye ✨

😭 Bharat’s Love

Bharat itne loyal the
ki 14 saal tak Ram ki sandals ko throne par rakhkar rule kiya 👣

Woh simple clothes pehente the
aur tapasvi jaisi life jeete the.

Jab Ram aaye,
Bharat emotional ho gaye 😭

Aur Ram ko hug kar liya.

👑 Ram Rajya

Vashishtha ne Ram ka coronation kiya 👑

Aur Ram Rajya start hua.

Us time:

No fear
No disease
No sorrow
No injustice

Sab log happy aur dharmic the ✨

Ram ne ek ideal king aur ideal husband ki life jee.

Aur Sita ji perfect devotion aur wisdom ka symbol bani rahi 🌸

Moral:

Truth aur duty ke liye sacrifice karna hi greatness hai
Ego aur desire downfall laate hain
Aur dharma, loyalty aur compassion duniya ko heaven bana sakte hain."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 9
    with st.expander("Chapter 9 - The Descent of the Gaṅgā; The Story of Kalmāṣapāda"):
        text1 = """ 
        Rishi Shuka ne Surya Vansh ki kahani aur aage sunayi—
aur iss baar focus tha Maa Ganga ke dharti par aane par.

🌊 Bhagiratha ka Maha Mission

King Sagara ke vansh me
pehle Anshuman ne tapasya ki…

Phir Dilipa ne bhi try kiya…

Lekin dono Maa Ganga ko dharti par nahi laa paaye 😔"""
        create_image_text_layout(
            "attached_assets/chapter9/9.9.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Finally unke descendant—

👑 Bhagiratha

ne bahut intense tapasya ki 🔥

Aur Maa Ganga unke saamne prakat hui ✨

Ganga ji boli:

👉 “Main dharti par aa sakti hoon…”

“Lekin mera flow itna powerful hai
ki Earth toot jaayegi.” 😮

Phir unhone ek aur concern bataya:

👉 “Log apne paap mujhme dhoyenge…”

“Toh mere paap ka kya hoga?”

Bhagiratha ne respectfully jawab diya:

“Saints aur pure-hearted yogis
aapko bhi purify kar denge.”

“Aur Lord Shiva aapke flow ko sambhal lenge.”

🕉️ Shiva Holds the Ganga

Bhagiratha ne phir Shiva ji ki tapasya ki.

Shiva ji pleased ho gaye 😊

Aur bole:

👉 “Theek hai, main Ganga ko apni jata me rokunga.”

Jab Ganga heaven se neeche aayi 🌊

Shiva ji ne unhe apni matted hair me catch kar liya 🕉️

Aur dheere-dheere Earth par release kiya.

🚩 Bhagiratha Leads the River

Bhagiratha apne chariot me aage-aage chale…

Aur Maa Ganga unke peeche flow karti gayi 🌊

Jahan-jahan woh gayi,
sab land holy aur fertile ho gayi ✨

Finally woh us jagah pahunchi
jahan Sagara ke sons ki ashes thi.

Jaise hi Ganga ji ka paani unhe touch hua…

👉 Sabko moksha mil gaya 🌟

Rishi ne kaha:

“Jab sirf ashes touch hone se moksha mil sakta hai…”

“Toh jo shraddha se Ganga ki worship kare,
uska kitna bhala hoga?”

😈 King Saudasa / Kalmashapada

Bhagiratha ke descendants me
ek king hua—

👑 Saudasa

(also called Kalmashapada)

Ek din hunting ke waqt
usne ek rakshasa ko maar diya ⚔️

Rakshasa ka bhai revenge lena chahta tha 😠

Woh disguise lekar king ka cook ban gaya 🍲

Aur ek din usne
human flesh paka kar
Rishi Vashishtha ko serve kar diya 😨

Vashishtha ne instantly samajh liya.

Woh gusse me aa gaye 😠

Aur curse diya:

👉 “Tum rakshasa ban jaoge!”

Baad me unhe pata chala
ki king innocent tha 😔

Toh unhone curse ko 12 saal tak limit kar diya.

King bhi gusse me
counter-curse dene wale the…

Lekin queen Madayanti ne roka 🙏

King ne curse wala water
apne hi pairon par gira diya.

Isliye uske pair black ho gaye.

Aur uska naam pada:

🌑 Kalmashapada

(black-footed one)

😢 Tragic Brahmana Incident

Curse ki wajah se woh rakshasa nature ka ho gaya.

Ek din usne jungle me
ek Brahmana couple dekha.

Wife ne request ki:

👉 “Mere husband ko mat maaro…”

“Woh saintly aur innocent hain.”

Lekin curse ke influence me
Saudasa ne Brahmana ko kha liya 😨

Brahmana ki wife ne gusse me curse diya:

👉 “Jab bhi tum intimacy ki koshish karoge,
tumhari death ho jayegi.”

Baad me curse khatam ho gaya…

Lekin king ne fear ki wajah se
normal married life chhod di. 😔

👶 Ashmaka’s Strange Birth

Vashishtha ji ki help se
queen ko child hua.

Lekin baby 7 saal tak born nahi hua 😮

Finally Vashishtha ne stone se strike kiya,
tab child born hua.

Isliye uska naam pada:

🪨 Ashmaka

(stone-born)

⚔️ Mulaka – Protected by Women

Ashmaka ka son tha—Mulaka.

Us time Parashurama
Kshatriyas ko destroy kar rahe the 😨

Women ne Mulaka ko protect kiya.

Isliye uska title pada:

👩‍🛡️ Narikavacha

(“protected by women”)

⏳ King Khatvanga’s Final Wisdom

Baad me ek mahaan king hua—

👑 Khatvanga

Usne devas ki help karke demons ko hara diya ⚔️

Gods bahut khush hue
aur bole:

👉 “Mango kya chahiye?”

Khatvanga ne poocha:

“Kitna life bacha hai?”

Gods bole:

👉 “Sirf 1 muhurt”
(~48 minutes) 😮

Khatvanga instantly Earth par laut aaye.

Aur socha:

👉 “Na kingdom permanent hai…”
👉 “Na wealth…”
👉 “Na body…”

“Sirf Bhagwan hi eternal hain.”

Unhone poori devotion se
Bhagwan Vishnu ka dhyan kiya 🕉️

Aur attachment chhod diya.

Finally unhe Brahman-realisation mil gaya ✨

Moral:

True devotion impossible cheez bhi possible bana deti hai
Anger aur curses life destroy kar sakte hain
Aur sabse bada wisdom hai: worldly attachments temporary hain, spiritual truth eternal hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 10
    with st.expander("Chapter 10 - The Story of Rāma"):
        text1 = """ 
        Rishi Shuka ne Bhagwan Ram ki divine story aur detail me sunayi.

👑 Raghu Vansh ka Glory

King Khatvanga ke baad aaye:

Dirghabahu
Raghu
Aja
Dasharatha

Aur Dasharatha ke ghar janm hua—"""
        create_image_text_layout(
            "attached_assets/chapter9/9.10.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        🌟 Bhagwan Ram ka

Bhagwan Vishnu ne khud ko 4 forms me divide kiya:

Ram
Lakshman
Bharat
Shatrughna

Ram main complete form the ✨

🛕 Vishwamitra ka Yagya

Jab demons rishiyon ke yagya disturb karte the 😈

Tab Vishwamitra Ram aur Lakshman ko le gaye.

Ram ne akela hi Maricha aur dusre rakshason ko hara diya ⚔️🔥

Lakshman bas dekhte reh gaye 😮

🏹 Sita Swayamvar

Janaka ji ne Shiva ji ka huge bow rakha tha.

Usse 300 log milkar uthate the 😳

Sab kings fail ho gaye.

Phir Ram aaye…

Aur elephant baby ki tarah easily bow utha liya 🐘

Bow string kiya…

💥 Aur bow beech se toot gaya!

Sab shock ho gaye 😮

Aur Sita ji ne Ram ko husband choose kiya 💍🌸

⚔️ Parashurama ka Pride Break

Wapas aate waqt
Parashurama aaye 😠

Unhe laga koi Shiva bow tod hi nahi sakta.

Lekin Ram ka divine power dekhkar
unka ego calm ho gaya 🙏

🌲 Ram ka Exile

Kaikeyi ne Dasharatha se
2 boons maange:

👉 Bharat ko kingdom
👉 Ram ko 14 years exile

Dasharatha helpless ho gaye 😢

Lekin Ram ne bina complaint ke sab accept kar liya.

Bilkul ek yogi ki tarah—

kingdom chhod diya
palace chhod diya
comforts chhod diye

Sita aur Lakshman bhi saath chale 🌲

😈 Surpanakha aur War

Forest me Surpanakha ne Ram ko propose kiya 😅

Lakshman ne uski nose aur ears cut kar diye ✂️

Uske brothers—Khara, Dushana, Trishira—attack karne aaye.

Ram ne 14,000 rakshason ko destroy kar diya ⚔️🔥

🦌 Golden Deer Trap

Ravana ne Maricha ko golden deer banaya 🦌✨

Sita ji us deer ko dekhkar attract ho gayi.

Ram uske peeche gaye.

Iss chance ka use karke
Ravana ne Sita ji ko kidnap kar liya 😨

Bilkul bhediya sheep ko chura le jaye jaise.

😢 Ram ka Grief

Ram aur Lakshman forest me Sita ko dhoondte rahe.

Ram ne human emotions bhi show kiye—

pain, sadness, longing 😢

Taaki duniya samjhe
attachment kitna painful ho sakta hai.

🦅 Jatayu’s Sacrifice

Vulture king Jatayu ne
Sita ji ko bachane ki koshish ki 🦅

Lekin Ravana ne use maar diya.

Ram ne uske funeral rites khud perform kiye 🙏

🐒 Alliance with Monkeys

Ram ki friendship hui:

Sugriva
Hanuman
Jambavan
Angad

ke saath 🐒

🌊 Ocean aur Ram Setu

Ram ocean ke paas aaye.

3 din tak wait kiya.

Ocean god nahi aaye 😠

Ram gusse me aa gaye.

Ocean god darr kar saamne aaye 🙏

Aur bole:

👉 “Bridge banao.”

Monkey army ne mountains aur trees se bridge banaya 🌉

Aur Lanka ki taraf march kiya.

🔥 Lanka Under Siege

Hanuman pehle hi Lanka jala chuke the 🔥

Ab monkey army ne poori city ko surround kar liya.

gates tod diye
towers gira diye
rooftops destroy kar diye
⚔️ Final War

Ravana ne apni strongest army bheji:

Indrajit
Kumbhakarna
Prahasta
Atikaya
Narantaka

Monkey side me:

Hanuman
Sugriva
Angad
Jambavan
Nila

sab fight kar rahe the ⚔️

👹 Ram vs Ravana

Ravana Pushpaka Vimana me aaya ✨

Ram divine chariot me.

Ravana ne arrows barsa diye 🏹

Ram bole:

👉 “Coward!”

“Tumne meri absence me Sita ko churaya.”

“Ab tumhe punishment milegi.”

Ram ne divine arrow chhoda 🔥🏹

Arrow seedha Ravana ke heart me laga 💥

Aur Ravana gir gaya.

Uske 10 mouths se blood bahne laga 😨

😭 Mandodari’s Lament

Ravana ki queens battlefield me aayi.

Mandodari ro kar boli:

👉 “Tumne Sita ji ki spiritual power ko underestimate kiya…”

“Isi wajah se tum destroy ho gaye.”

🌸 Ram Meets Sita

War ke baad Ram ne
Ashoka Vatika me Sita ji ko dekha 🌸

Woh separation ki wajah se weak ho gayi thi 😢

Ram ka heart compassion se bhar gaya.

👑 Return to Ayodhya

Ram ne Vibhishana ko Lanka ka king banaya 👑

Phir Pushpaka Vimana se Ayodhya laut aaye ✨

Devas flowers barsa rahe the 🌸

Aur Ram ki glory ga rahe the.

😭 Bharat’s Devotion

Bharat ne 14 saal tak
Ram ki sandals ko throne par rakha 👣

Woh simple life jeete rahe,
jaise tapasvi.

Jab Ram aaye—

Bharat ro pade 😭

Aur Ram ke feet me gir gaye.

Ram ne unhe hug kar liya ❤️

👑 Ram Rajya

Vashishtha ji ne Ram ka coronation kiya 👑

Aur Ram Rajya shuru hua ✨

Us time:

no fear
no disease
no sorrow
no injustice

Nature bhi sabko abundance de rahi thi 🌿

Ram ne ek ideal king, ideal husband aur ideal human ki life jee.

Aur Sita ji devotion, intelligence aur purity ka perfect symbol bani rahi 🌸

Moral:

Dharma ke liye sacrifice karna greatness hai
Ego aur desire downfall laate hain
Loyalty, compassion aur truth duniya ko Ram Rajya bana sakte hain."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 11
    with st.expander("Chapter 11 - The Story of Rāma (concluded)"):
        text1 = """ 
        Rishi Shuka ne Bhagwan Ram ki story ka final part sunaya.

👑 Ram’s Grand Sacrifices

Ayodhya wapas aane ke baad
Bhagwan Ram ne bahut bade yajnas perform kiye 🔥

Woh sirf king nahi the—
woh perfect dharmic ruler the."""
        create_image_text_layout(
            "attached_assets/chapter9/9.11.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Yajna complete hone ke baad
Ram ne itni generosity dikhayi 😮

👉 East kingdom priests ko de diya
👉 West bhi donate kar diya
👉 North-South bhi de diya

Aur centre part Guru Vashishtha ko 🙏

End me Ram ke paas
sirf unke kapde aur ornaments bache 😌

Sita ji ne bhi almost sab kuch donate kar diya 🌸

Brāhmanas emotional ho gaye 😢

Aur bole:

👉 “Aap hume kya denge?”

👉 “Aap toh already ignorance ka darkness destroy karte ho.”

🌙 Ram Secretly Checks His Kingdom

Ek raat Ram disguise me city me ghoom rahe the 👀

Woh dekhna chahte the
ki public unke baare me kya sochti hai.

Tab unhone ek aadmi ko apni wife se argue karte suna 😮

Woh bola:

👉 “Main Ram nahi hoon…”

👉 “Jo kisi aur ke ghar rehkar aayi wife ko accept kar loon.”

Indirectly woh Sita ji par doubt kar raha tha 😔

😢 Sita’s Exile

Ram ka heart toot gaya 💔

Unhe pata tha Sita ji pure hain…

Lekin public opinion se woh disturb ho gaye.

Aur dharma ke pressure me
unhone Sita ji ko forest bhej diya 😢

🌲 Valmiki Ashram

Pregnant Sita ji
Rishi Valmiki ke ashram pahunchi 🌸

Wahan unhone twins ko janm diya:

👦 Lava
👦 Kusha

Valmiki ji ne unki upbringing aur education ki.

⚔️ Brothers’ Families

Lakshman ke sons hue:

Angada
Chandraketu

Bharat ke sons:

Taksha
Pushkala

Shatrughna ke sons:

Subahu
Shrutasena
🏙️ Mathura Founded

Shatrughna ne demon Lavana ko maara ⚔️

Aur us jagah:

🏙️ Mathura city

basayi.

🌍 Sita Returns to Earth

Ek din Sita ji ne
apne sons ko Valmiki ji ke care me chhod diya 🌸

Aur Ram ka dhyan karte hue…

👉 Dharti Maa me sama gayi 🌍✨

😢 Ram’s Deep Grief

Bhagwan Ram divine the…

Lekin Sita ji ko yaad karke
woh bhi grief feel karte the 😔

Rishi Shuka ne kaha:

👉 “Agar Ram jaise mahaan being bhi attachment se pain feel kar sakte hain…”

“Toh ordinary humans ka kya kehna.”

🕉️ Ram’s Final Years

Uske baad Ram ne:

strict celibacy follow ki
thousands of years tak yajnas kiye
spiritual discipline maintain rakha 🔥

Phir ek din…

Bhagwan Ram
apne eternal divine form me
wapas chale gaye ✨

🌟 Real Glory of Ram

Rishi Shuka ne kaha:

👉 Ravana ko maarna…
👉 Samundar par bridge banana…

yeh Ram ke liye koi impossible feat nahi tha.

Kyunki woh khud Bhagwan Vishnu the 🌌

Monkey army bhi bas divine play ka part thi 🐒✨

🌸 Ayodhya’s Love for Ram

Jab Ram exile se lautkar aaye थे—

Ayodhya city completely decorate ho gayi 🎉

flowers 🌸
gold domes ✨
flags 🚩
perfumes 🌺
arches & decorations

Sab log rooftops par chadhkar
Ram ko dekh rahe the 😍

Aur flowers barsa rahe the 🌸🌸🌸

🏰 Ram and Sita’s Palace

Ram aur Sita ka palace bahut divine tha ✨

emerald floors 💚
crystal walls
pearl decorations
golden pillars

Sab kuch heavenly lagta tha 😮

Aur Ram-Sita wahan
perfect harmony aur dharma ke saath rahe ❤️

🌟 Final Teaching

Rishi Shuka ne conclude kiya:

👉 “Jo bhi Ram ki story shraddha se sunta hai…”

👉 “Aur apne senses control karta hai…”

Woh karma ke bondage se free ho sakta hai ✨

Moral:

True leadership sacrifice maangti hai
Dharma kabhi-kabhi emotionally painful hota hai
Aur Bhagwan Ram ka life ideal truth, duty, compassion aur self-control ka example hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 12
    with st.expander("Chapter 12 - The Description of Ikṣvāku’s Race (concluded)"):
        text1 = """ 
        Rishi Shuka ne Surya Vansh yani Ikshvaku dynasty ka final chapter sunaya.

👑 Ram ke Baad ka Solar Dynasty

Bhagwan Ram ke son the:

🌟 Kusha

Aur unse Surya Vansh aage chala."""
        create_image_text_layout(
            "attached_assets/chapter9/9.12.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Phir ek long line of kings aaye:

Atithi
Nishadha
Nabha
Pundarika
Kshemadhanva
Devanika
Anīha
Pariyatra
Bala
Sthala
Vajranabha
… aur bahut saare kings 👑
☀️ Vajranabha

Rishi ne mention kiya
ki Vajranabha me Surya dev ka divine portion tha ✨

🧘 Hiraṇyanabha – Master of Yoga

Baad me ek mahaan king hua:

🕉️ Hiraṇyanabha

Woh sirf king nahi,
ek great yogi bhi tha.

Usne famous sage:

🧘 Yajnavalkya

ko deep spiritual yoga sikhaya.

Yeh knowledge:

👉 ego ko destroy karti thi
👉 aur self-realisation tak le jaati thi ✨

🔥 Maru – The Hidden King

Baad me ek mysterious king hua:

🌌 Maru

Usne perfect yogic powers achieve kar li 😮

Aur kaha jaata hai ki:

👉 Woh abhi bhi alive hai
👉 Kalapa naam ki hidden place me rehta hai 🏔️

Rishi Shuka ne future prediction di:

👉 “Kali Yuga ke end me…”

Maru wapas aayega
aur Surya Vansh ko revive karega ✨

⚔️ Brihadbala and Mahabharata

Generations baad ek king hua:

👑 Brihadbala

Woh Mahabharata war ke time tha.

Usne Kauravas ka side liya ⚔️

Lekin battle me:

🔥 Abhimanyu

(ne Arjuna ke son)
usse maar diya.

⏳ Future Kings

Uske baad bhi lineage continue hui:

Brihadraṇa
Urukriya
Vatsavriddha
Bhanu
Divaka
Sahadeva
Bṛhadasva
Bhānumān
… aur kai kings.
🌸 Śākya Line

Baad me ek king hua:

👑 Śākya

Uski line se aage aaye:

Śuddhoda
Lāṅgala
Prasenajit
Kṣudraka
Raṇaka
Suratha
🌑 Last King – Sumitra

Aur finally Surya Vansh ka last king hua:

👑 Sumitra

Rishi Shuka ne future prophecy di:

👉 “Jab Sumitra rule karega…”

👉 “Tab Ikshvaku dynasty ka end ho jayega.”

Yeh sun kar King Parikshit silently sochne laga 😔

Even the greatest dynasties…
ek din end ho jaati hain.

🌌 Deeper Meaning

Rishi indirectly yeh samjha rahe the:

👉 Kingdoms temporary hain
👉 Dynasties temporary hain
👉 Power temporary hai

Lekin:

✨ Dharma
✨ Wisdom
✨ Spiritual truth

yeh eternal hain.

Moral:
Duniya ki sabse glorious dynasties bhi ek din khatam ho jaati hain—
sirf spirituality aur dharma hi truly eternal hote hain."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 13
    with st.expander("Chapter 13 - The Description of the Race of Nimi"):
        text1 = """ 
        Rishi Shuka ne ab ek aur famous royal family ki kahani sunayi—

👑 Mithila ke Janaka Vansh ki Story

Yeh wahi dynasty thi
jahan se Maa Sita ji ka janm hua tha 🌸"""
        create_image_text_layout(
            "attached_assets/chapter9/9.13.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        🔥 King Nimi aur Vashishtha

Ikshvaku ka second son tha—

👑 Nimi

Woh bahut wise aur philosophical king tha.

Ek din usne huge yajna organise kiya 🔥

Aur Guru Vashishtha ko invite kiya.

Lekin Vashishtha ne kaha:

👉 “Main already Indra ka yajna conduct kar raha hoon.”

👉 “Pehle woh complete kar leta hoon,
phir tumhare paas aaunga.”

Nimi chup rahe 🤔

Lekin unhone socha:

👉 “Life bahut short hai…”

👉 “Wait karte-karte time waste nahi karna chahiye.”

Toh unhone dusre priests ke saath yajna start kar diya 🔥

😠 Mutual Curse

Jab Vashishtha wapas aaye
aur dekha ki yajna bina unke start ho gaya 😨

Woh gusse me aa gaye.

Aur curse diya:

👉 “Nimi ka body gir jaaye!”

Nimi bhi upset ho gaya 😠

Aur bola:

👉 “Aap greed ki wajah se dharma bhool gaye.”

👉 “Aapka body bhi fall ho.”

Dono ka physical body destroy ho gaya 😮

✨ Nimi Rejects His Body

Rishis ne Nimi ka body preserve kiya.

Aur gods se request ki:

👉 “Please Nimi ko revive kar do.”

Lekin Nimi ki soul ne mana kar diya 😶

Usne kaha:

👉 “Main dobara body me nahi jaana chahta.”

👉 “Body hi sorrow, fear aur death ka source hai.”

Usne deep spiritual truth samajh liya tha ✨

👁️ Nimi Becomes the Blink of Eyes

Gods impressed ho gaye 😊

Aur bole:

👉 “Theek hai.”

👉 “Tum sab living beings ki eyes me reside karoge.”

Tab se:

👁️ Blinking of eyes

ko “nimiṣa” se connect kiya gaya.

Yani Nimi sab creatures ke eyelids me subtle form me present ho gaya ✨

👶 Birth of Janaka

Lekin kingdom ko king chahiye tha 😨

Toh sages ne Nimi ke preserved body ko churn kiya 🔥

Aur usme se ek child born hua 😮

Uska naam pada:

👑 Janaka

Kyunki woh miraculous birth tha.

Aur usse kaha gaya:

🌌 Vaideha

Kyunki woh body-less being (Videha/Nimi) se born hua tha.

Aur usne build ki famous city:

🏙️ Mithila
🌸 Lineage of Sita

Janaka ke descendants me kai kings aaye:

Udavasu
Nandivardhana
Suketu
Devarata
Brihadratha
… aur bahut generations.

Phir ek king hua:

👑 Hrasvaroma

Uska son tha:

🌾 Siradhvaja Janaka

Yahi the:

👉 Maa Sita ji ke father 🌸

🌱 Discovery of Sita

Ek sacrifice ke liye
Janaka ji khud field plough kar rahe the 🚜

Tab unhe earth ke andar se
ek divine baby girl mili 😮✨

Woh thi:

🌸 Sita

Isliye Janaka ko kaha gaya:

🌾 Siradhvaja

(plough-bannered king)

🧘 Philosopher Kings

Baad ke Mithila kings bhi special the.

Woh sirf rulers nahi the—

👉 Great yogis
👉 Philosophers
👉 Spiritual masters

Ek famous king tha:

🕉️ Keśidhvaja

Woh spiritual wisdom me expert tha.

Dusra:

🔥 Khaṇḍikya

rituals aur karma-path me expert tha.

Rishi Shuka ne conclude kiya:

👉 Mithila ke kings household life jeete hue bhi
spiritually detached rehte the.

Unhone pleasure-pain, gain-loss sabko transcend kar liya tha ✨

Aur unki wisdom ka source tha:

🧘 Yajnavalkya

great yoga master.

King Parikshit yeh sab sunkar amazed ho gaya 😮

Usse samajh aa gaya—

👉 Real greatness sirf kingdom rule karne me nahi…

👉 Apne mind aur ego ko master karne me hai.

Moral:
True wisdom ka matlab duniya chhodna nahi—
balki duniya me rehkar bhi spiritually detached rehna hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 14
    with st.expander("Chapter 14 - The Description of the Lunar Race"):
        text1 = """ 
        Rishi Shuka ne ab ek aur legendary dynasty ki kahani shuru ki—

🌙 Chandra Vansh (Lunar Dynasty)

Yeh Moon-god Soma ki royal line thi."""
        create_image_text_layout(
            "attached_assets/chapter9/9.14.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        🌕 Birth of Soma

Brahma ji ke great son the:

🧘 Atri Rishi

Unki tapasya aur joy se
ek divine child born hua—

🌙 Soma (Chandra Dev)

Woh nectar jaisa glowing tha ✨

Brahma ji ne use bana diya:

stars ka king 🌌
herbs aur plants ka protector 🌿
Brahmanas ka guardian 🙏
👑 Soma Becomes Arrogant

Soma powerful aur famous hota gaya.

Usne 3 worlds conquer kiye 😮

Aur Vishnu ji ke honour me Rajasuya yajna bhi kiya 🔥

Lekin power ke saath
usme ego aa gaya 😔

Usne forcibly kidnap kar li:

🌸 Tara

Jo Brihaspati ki wife thi.

⚔️ Gods vs Demons War

Brihaspati ne baar-baar bola:

👉 “Meri wife wapas karo.”

Lekin Soma ne mana kar diya 😠

Result?

⚔️ Huge war start ho gayi.

Gods → Brihaspati side
Asuras → Soma side

Shukracharya bhi Soma ke side chale gaye 😮

Aur Shiva ji Brihaspati ko support karne aaye 🔱

Poora universe battlefield ban gaya 🌌⚔️

Finally Brahma ji ko intervene karna pada.

👶 Birth of Budha

Brahma ji ne Soma ko force kiya
ki Tara ko return kare.

Lekin Tara pregnant thi 😮

Jab child born hua,
dono claim karne lage:

👉 “Yeh mera beta hai!”

Soma 😠
Brihaspati 😠

Sabne Tara se poocha:

👉 “Asli father kaun hai?”

Woh shame se chup rahi 😔

Child khud gusse me bol pada 😮

👉 “Sach bolo!”

Finally Tara ne slowly confess kiya:

👉 “Soma…” 🌙

Tab Brahma ji ne child ka naam rakha:

🌟 Budha

Yani intelligent aur wise one.

👑 Pururavas and Urvashi

Budha ka son hua:

👑 Pururavas

Woh incredibly handsome, brave aur noble king tha ✨

Swarg ki apsara:

🌸 Urvashi

uske baare me sunkar usse pyaar kar baithi ❤️

Woh heaven se Earth par aayi
aur Pururavas se mili.

King usse dekhkar mesmerized ho gaya 😍

Pururavas bola:

👉 “Please mere saath raho.”

👉 “Hum hamesha saath rahenge.”

🌸 Urvashi’s Conditions

Urvashi ne 3 conditions rakhi:

🐑 Mere 2 lambs protect karna
🧈 Main sirf ghee khaungi
👀 Mujhe tum naked nahi dikhoge except intimacy ke time

Pururavas maan gaya ❤️

❤️ Their Love Story

Dono heavenly gardens me enjoy karne lage 🌸✨

Saalon tak happily rahe.

Pururavas completely Urvashi me lost ho gaya 😍

😢 Gandharvas Separate Them

Indra ko heaven me Urvashi ki kami feel hui 😔

Usne Gandharvas ko bheja.

Ek dark night me
Gandharvas ne Urvashi ke lambs chura liye 🐑😨

Urvashi loudly royi:

👉 “Mera husband coward nikla!”

👉 “Woh sirf daytime hero hai!” 😡

Pururavas hurt aur angry ho gaya 😤

Woh sword lekar naked state me bhaaga.

Tab Gandharvas ne lightning flash ki ⚡

Aur Urvashi ne use naked dekh liya 😮

Condition break ho gayi ❌

Aur woh instantly disappear ho gayi 😢

😭 Pururavas Goes Mad

Pururavas heartbroken ho gaya 💔

Woh pagal ki tarah Earth par bhatakne laga.

Finally usne Urvashi ko
Kurukshetra ke paas Saraswati river bank par dekha 🌊

Woh apni celestial friends ke saath thi ✨

Pururavas begged 😢

👉 “Mujhe chhodkar mat jao…”

👉 “Main tumhare bina mar jaunga.”

🌸 Urvashi’s Wisdom

Urvashi calmly boli:

👉 “Control your senses.”

👉 “Attachment wolves ki tarah insaan ko kha jaata hai.” 🐺

Usne kaha:

👉 “Women aur worldly desires unstable hote hain.”

👉 “True peace attachment me nahi hai.”

Lekin usne promise diya:

👉 “Har saal ek raat ke liye milungi.”

Aur bola ki uske child bhi honge.

🔥 Birth of Sacrificial Fire

Pururavas fir bhi obsessed tha 😔

Gandharvas ne usse ek sacred fire vessel diya 🔥

Woh usse Urvashi samajhkar forest me ghoomta raha 😢

Ek din usse spiritual awakening hui ✨

Usne sacred fire create ki
aur Vedic rituals start kiye.

Rishi Shuka ne explain kiya:

👉 Earlier only ONE Veda tha
👉 ONE divine sound “Om” tha 🕉️
👉 ONE sacred fire tha 🔥

Lekin Pururavas ke time se:

3 Vedas
3 sacred fires
ritualistic sacrifices

properly begin hue.

Pururavas ne finally
sacrificial fire aur devotion ke through
Gandharva realm attain kar liya ✨

Moral:

Desire aur attachment insaan ko restless bana dete hain
Worldly beauty temporary hai
Aur true elevation spiritual realization aur self-control se milti hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 15
    with st.expander("Chapter 15 - The Story of Paraśurāma—Sahasrārjuna Slain"):
        text1 = """ 
        Rishi Shuka ne ab ek fierce aur legendary avatar ki story sunayi—

⚔️ Bhagwan Parashurama

Woh Vishnu ji ka warrior avatar the."""
        create_image_text_layout(
            "attached_assets/chapter9/9.15.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        🌙 Pururavas ke Descendants

Pururavas aur Urvashi ke 6 sons hue.

Unki lineage me generations baad
ek king hua:

👑 Gadhi

Uski daughter thi:

🌸 Satyavati
🧘 Rishi Richika’s Marriage

Ek great sage the:

🔥 Richika Rishi

Woh Satyavati se marriage karna chahte the ❤️

Lekin King Gadhi ko laga:

👉 “Yeh poor sage meri princess ke layak nahi.”

Isliye usne impossible dowry maangi 😮

👉 “1000 white horses…”

👉 “Jinke ek ear black ho.” 🐎

Richika ne Varuna dev ki help se
woh horses arrange kar diye ✨

Aur Satyavati se shaadi ho gayi.

🍚 The Sacred Food Mix-Up

Ek din Richika ne special sacred food (charu) prepare kiya 🔥

Ek Satyavati ke liye
Ek uski mother ke liye

Satyavati ki mother jealous ho gayi 😬

Usne secretly bowls exchange kar diye 😮

Jab Richika ko pata chala
woh shock ho gaye 😨

Unhone kaha:

👉 “Ab tumhara son fierce warrior nature ka hoga…”

👉 “Aur tumhara brother spiritual sage type hoga.”

Satyavati ro padi 😢

Aur request ki:

👉 “Mera son violent na ho.”

Richika bole:

👉 “Theek hai…”

👉 “Tumhara grandson waise nature ka hoga.”

👶 Birth of Jamadagni and Parashurama

Satyavati ka son hua:

🧘 Jamadagni

Aur Jamadagni ki wife thi:

🌸 Renuka

Unke youngest son hue:

⚔️ Rama

(Parashurama)

Woh ordinary human nahi the 😮

👉 Vishnu ji ka avatar the
👉 Axe-wielding warrior sage 🔥

😠 Why Parashurama Hated Corrupt Kings

Us time bahut Kshatriya kings arrogant aur cruel ho gaye the 😔

Woh Brahmanas aur common people ko oppress karte the.

Sabse dangerous king tha:

👑 Sahasrarjuna

(Arjuna of Haihaya clan)

Usne Dattatreya ji ki worship se
incredible powers paayi thi ✨

Uske paas the:

👉 1000 arms 😳
👉 huge strength 💪
👉 mystical powers
👉 unbeatable speed

🌊 Sahasrarjuna vs Ravana

Ek baar woh Narmada river me enjoy kar raha tha 🌊

Aur apni thousand arms se
river ka flow hi rok diya 😮

Us time:

👹 Ravana

nearby camp me tha.

Flood aaya toh Ravana angry ho gaya 😠

Aur Sahasrarjuna ko challenge kiya.

Lekin Sahasrarjuna ne usse easily capture kar liya 😂

Bilkul monkey ki tarah bandh kar diya 🐒

Aur later insult karke release kar diya.

🐄 Kamadhenu Theft

Ek din Sahasrarjuna hunting karte hue
Jamadagni Rishi ke ashram pahunch gaya 🌳

Rishi ke paas thi divine cow:

🐄 Kamadhenu

Jo magically sabke liye food aur luxury create kar deti thi ✨

Rishi ne poori army ki hospitality ki 🙏

Lekin king greedy ho gaya 😔

Usne socha:

👉 “Itni amazing cow mere paas honi chahiye.”

Aur forcefully Kamadhenu ko chura liya 😡

⚔️ Parashurama’s Wrath

Jab Parashurama wapas aaye
aur unhe pata chala 😨

Woh snake ki tarah furious ho gaye 🐍🔥

Unhone uthaya:

divine axe 🪓
bow 🏹
arrows

Aur king ke peeche bhaage ⚡

⚔️ One Man vs Huge Army

Sahasrarjuna ne:

👉 17 massive armies bheji 😮

Elephants, horses, chariots sab.

Lekin Parashurama alone hi
sabko destroy karte gaye 💥

Jahan-jahan woh axe chalate:

heads girte 😨
arms cut hote
chariots toot jaate

Battlefield blood river ban gaya ⚔️🩸

🪓 Thousand Arms Cut Down

Finally Sahasrarjuna khud aaya 😠

Usne ek saath
500 bows use kiye 😳

Lekin Parashurama ne instantly
sab arrows destroy kar diye ⚡

Sahasrarjuna ne mountains aur trees phenke 🌳🪨

Parashurama ne apne axe se:

👉 uski 1000 arms kaat di 😨🪓

Bilkul snake ke hoods ki tarah.

Phir uska head bhi cut kar diya 💥

Uske sons fear me bhaag gaye 😱

🧘 Jamadagni’s Lesson

Parashurama Kamadhenu ko wapas le aaye 🐄

Aur proudly father ko sab bataya.

Lekin Jamadagni happy nahi hue 😮

Unhone calmly kaha:

👉 “Tumne sin kiya hai.”

👉 “King ko maarna bahut serious act hai.”

👉 “Forgiveness hi true Brahman greatness hai.” ✨

Unhone Parashurama ko kaha:

👉 “Holy rivers me jao…”

👉 “Aur Vishnu ji ka meditation karke atonement karo.”

Parashurama silently sunte rahe 😔

Yeh warrior ko diya gaya
compassion aur restraint ka lesson tha.

Moral:

Power jab arrogance ban jaaye toh destruction laati hai
Justice zaroori hai, lekin anger ko wisdom se control karna aur bhi zaroori hai
Forgiveness spiritual strength ka highest form hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 16
    with st.expander("Chapter 16 - The Story of Paraśurāma (concluded)"):
        text1 = """ 
        Rishi Shuka ne Parashurama ki story ka emotional aur intense final part sunaya. ⚔️🔥

🌊 Renuka and the Gandharva King

Ek din Parashurama ki mother:

🌸 Renuka

Ganga se water lene gayi 🌊"""
        create_image_text_layout(
            "attached_assets/chapter9/9.16.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Wahan unhone dekha:

✨ Citraratha

(Gandharva king)

celestial apsaras ke saath water me enjoy kar raha tha 😮

Ek moment ke liye
Renuka ka mind distract ho gaya 😔

Woh bas us beauty aur scene ko dekhte reh gayi.

Aur yajna ka fixed time miss ho gaya ⏳

😨 Jamadagni’s Wrath

Jab woh ashram wapas aayi
toh Rishi Jamadagni instantly samajh gaye
ki unka mind momentarily disturbed hua tha 😠

Gusse me unhone apne sons ko order diya:

👉 “Is sinful woman ko maar do.”

Bade brothers shock me aa gaye 😨

Kisi ne command follow nahi ki.

⚔️ Parashurama Obeys

Lekin:

⚔️ Parashurama

apne father ki spiritual power aur authority ko deeply jaante the.

Unhone bina hesitate kiye 😔

👉 mother
👉 aur brothers

sabko kill kar diya.

😢 Jamadagni Grants a Boon

Jamadagni pleased hue.

Unhone kaha:

👉 “Mango kya chahte ho.”

Parashurama ne immediately bola ❤️

👉 “Meri mother aur brothers wapas alive ho jaayein.”

👉 “Aur unhe yaad bhi na rahe ki maine unhe maara tha.”

Aur instantly sab revive ho gaye ✨

Bilkul deep sleep se uthne jaise.

😠 Sons of Sahasrarjuna Seek Revenge

Lekin dusri side par
Sahasrarjuna ke sons revenge me jal rahe the 😡

Unhe apne father ki death ka dard bhool nahi raha tha.

Ek din jab Parashurama forest me the 🌲

Tab unhone chance dekha.

Aur secretly Jamadagni ke ashram me ghus gaye ⚔️

🩸 Murder of Jamadagni

Rishi Jamadagni peacefully meditation me baithe the 🧘

Unka mind Bhagwan Vishnu me absorbed tha ✨

Lekin un cruel warriors ne 😨

👉 unka head cut kar diya
👉 aur usse le gaye 💀

😭 Renuka’s Cry

Renuka helpless hokar ro padi 💔

Apne chest peette hue chillane lagi:

👉 “Rama! Rama! Jaldi aao!” 😭

⚔️ Parashurama’s Terrible Vow

Door forest me Parashurama ne woh cry suni 😨

Woh immediately ashram wapas aaye.

Aur father ko dead dekha 😔

Woh grief aur rage se bhar gaye 🔥

👉 “O righteous father…”
👉 “Aap hume chhodkar chale gaye…”

Phir unhone ek horrifying vow liya ⚔️

👉 “Main poori corrupt Kshatriya race ko destroy kar dunga.”

🪓 Mass Destruction

Parashurama axe lekar nikle 🔥

Aur city:

🏙️ Mahishmati

par attack kar diya.

Battle itni brutal thi 😨

ki:

👉 unhone heads ka mountain bana diya 💀
👉 blood ki rivers baha di 🩸

Rishi Shuka ne kaha:

👉 Parashurama ne “21 times” Earth ko corrupt Kshatriyas se cleanse kiya ⚔️

🩸 Lakes of Blood

Kurukshetra ke paas:

🌊 Samantapanchaka

me blood-filled pools create hue 😨

Yeh wars ki memory ban gaye.

🙏 Restoring Jamadagni

Parashurama finally apne father ka head recover kar laaye ❤️

Aur usse body se rejoin kiya.

Phir unhone huge sacrifices aur rituals perform kiye 🔥

Aur Earth ka almost sab land priests aur sages ko donate kar diya ✨

🌟 Jamadagni Becomes a Star

Rishi Jamadagni later heavenly form attain kar gaye 🌌

Aur sky me Great Sages ke among shine karne lage ✨

⛰️ Parashurama Still Lives

Rishi Shuka ne reveal kiya 😮

👉 Parashurama abhi bhi alive hain
👉 Mahendra mountain par meditate karte hain 🏔️

Unhone violence chhod diya hai ✨

Aur ab peaceful yogi ban chuke hain.

🌌 Meaning of the Avatar

Bhagwan Vishnu ne Parashurama avatar liya tha:

👉 Earth ka burden kam karne ke liye
👉 corrupt rulers ko stop karne ke liye ⚖️

Lekin story yeh bhi dikhati hai:

👉 revenge aur violence endless suffering laate hain 😔

🌟 Vishwamitra’s Story Begins

Uske baad Rishi Shuka ne ek aur legendary figure ka mention kiya:

🔥 Vishwamitra

Woh originally ek Kshatriya king the 👑

Lekin tapasya aur spiritual power se:

👉 Brahmarishi ban gaye ✨

👦 Shunahshepa / Devarata

Vishwamitra ne ek boy adopt kiya:

🌟 Shunahshepa

jise later:

✨ Devarata

bola gaya.

Woh originally sacrifice ke liye sold hua tha 😨

Lekin divine prayers se bach gaya 🙏

Vishwamitra ne apne sons ko order diya:

👉 “Isse apna eldest brother maano.”

Kuch sons ne refuse kar diya 😠

Toh Vishwamitra ne unhe curse diya:

👉 “Tum outcast tribes ban jaoge.”

Lekin kuch obedient sons maan gaye ❤️

Aur Vishwamitra unse pleased hue.

Is tarah:

🌿 Kaushika lineage

multiple branches me divide hui.

King Parikshit quietly sunte rahe 😮

Unhe samajh aaya:

👉 Spiritual power caste ya birth se nahi…
👉 discipline, tapasya aur character se aati hai.

Moral:

Anger aur revenge destruction laate hain
Obedience without wisdom dangerous ho sakti hai
Aur true greatness birth se nahi, spiritual effort se milti hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 17
    with st.expander("Chapter 17 - The Lunar Dynasty—The Descendants of Āyu, the Son of Purūravas"):
        text1 = """ 
        Rishi Shuka ne ab Lunar Dynasty ki aur branches ki story sunayi 🌙✨

🌙 Sons of Ayu

Pururavas aur Urvashi ke son:

👑 Ayu

ke 5 famous sons hue:

Nahusha
Kshatravriddha
Raji
Rambha
Anenas"""
        create_image_text_layout(
            "attached_assets/chapter9/9.17.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Rishi ne bola:

👉 “Ab main inki different lineages ki kahani bataunga.”

🌟 Kshatravriddha’s Line

Kshatravriddha ka son tha:

👑 Suhotra

Aur uske 3 sons hue:

Kāśya
Kuśa
Gṛtsamada
🧘 Shaunaka Rishi

Gritsamada ki line me born hue:

✨ Shaunaka Rishi

Woh Rigveda ke greatest masters me se ek bane 📖

🩺 Dhanvantari – God of Ayurveda

Kāśya ki line me ek legendary king born hua:

🩺 Dhanvantari

Rishi Shuka ne bataya 😮

👉 Woh Bhagwan Vasudeva ka divine portion the ✨

Aur:

🌿 Ayurveda

(science of medicine)

ke founder maane gaye.

👑 Divodasa and Pratardana

Iss line me later aaye:

Divodasa
Pratardana

Pratardana ke bahut names the 😮

Jaise:

Shatrujit ⚔️
Vatsa
Ritadhvaja
Kuvalayashva
🌟 King Alarka

Phir ek amazing king hua:

👑 Alarka

Rishi ne kaha 😮

👉 Usne 66,000 years tak Earth rule ki 🌍

Aur phir bhi:

👉 Young aur healthy raha ✨

Uski line me later aaye:

Santati
Sunitha
Suketana
Dharmaketu
Satyaketu
Dhṛṣṭaketu
Sukumāra
Vītihotra
Bharga
Bhārgabhūmi
🌊 Rambha’s Line

Ayu ke son:

🌟 Rambha

ki line bhi continue hui.

Uske descendants the:

Rabhasa
Gambhira
Akriya

Rishi ne mention kiya
ki Akriya ki queen se
ek Brahmana lineage start hui ✨

🧘 Anenas’ Line

Ayu ke fifth son:

🌌 Anenas

ki line me aaye:

Śuddha
Śuci
Trikakud

Trikakud ko bola gaya:

⚖️ Dharmasārathi

(charioteer of dharma)

Uska son tha:

🧘 Śāntaraya

Woh itna spiritually detached tha ✨

ki usse kingdom aur dynasty continue karne me interest hi nahi tha.

Uska focus liberation par tha 🌸

⚔️ Raji and the War of Heaven

Ab aayi most dramatic branch 😮

⚡ King Raji

Ayu ka powerful son tha.

Uske:

😳 500 mighty sons

the.

Ek time gods aur demons me huge war chal raha tha ⚔️

Gods defeat ho rahe the 😨

Toh unhone Raji se help maangi.

⚔️ Raji Saves the Gods

Raji ne Asuras ko defeat kar diya 🔥

Aur heaven wapas Indra ko dilaya.

Lekin Indra secretly scared tha 😬

Usne socha:

👉 “Raji bahut powerful ho gaya hai…”

Toh usne diplomacy use ki 😮

👉 Raji ko father ki tarah honour kiya
👉 khud ko uska “son” declare kar diya

😠 Raji’s Sons Seize Heaven

Jab Raji mar gaya 😔

Toh uske 500 sons greedy ho gaye.

Unhone:

👉 Heaven ka throne seize kar liya ⚡

Aur Indra ko wapas nahi diya.

Woh even sacrificial offerings bhi khud lene lage 😮

Jo normally Indra ko milti thi.

🧠 Brihaspati’s Strategy

Indra helpless ho gaya 😨

Toh Guru Brihaspati ne clever plan banaya.

Unhone rituals perform kiye ✨

Aur somehow Raji ke sons ko:

👉 dharma se corrupt kar diya 😔

Jab woh unrighteous ho gaye…

Tab Indra ne attack kiya ⚡

Aur sabko destroy kar diya 😨

Ek bhi son survive nahi hua.

🌿 Another Branch of Kuśa

Kuśa ki line me later kings aaye:

Prati
Sanjaya
Jaya
Krita
Haryashva
Sahadeva
Hina
Jayasena
Saṅkṛti
Jaya

Final king:

⚔️ Kṣātradharmā

Kshatriya dharma ko faithfully follow karta tha ✨

🌌 Transition to Yayati

Rishi Shuka ne finally kaha:

👉 “Ab maine Kshatravriddha ki line explain kar di.”

👉 “Ab next main Nahusha aur Yayati ki famous story sunaoonga.” ✨

King Parikshit silently sunte rahe 😊

Unhe samajh aaya:

👉 Dynasties rise aur fall hoti rehti hain
👉 Power temporary hai
👉 Dharma aur wisdom hi lasting hain 🌸

Moral:

Power without righteousness eventually destroy ho jaati hai
Wisdom aur self-control kings ko truly great banate hain
Aur spiritual detachment worldly success se bhi higher hota hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 18
    with st.expander("Chapter 18 - The History of Nahuṣa’s Line—The Story of Yayāti"):
        text1 = """ 
        Rishi Shuka ne ab Lunar Dynasty ki sabse famous aur emotional stories me se ek sunayi ✨🌙

👑 King Yayati ki Story

Yeh desire, attachment aur human weakness ki deep story thi.

🌙 Sons of Nahusha

King Nahusha ke 6 sons the:

Yati
Yayati
Samyati
Ayati
Viyati
Kriti"""
        create_image_text_layout(
            "attached_assets/chapter9/9.18.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        🧘 Yati Rejects the Throne

Sabse bada son:

🌸 Yati

bahut spiritual tha.

Usne kingdom lene se mana kar diya 😮

Kyunki usse pata tha:

👉 “Kingship aur power insaan ko self-realization se door le jaati hai.”

Isliye throne mila:

👑 Yayati

ko.

😨 Fall of Nahusha

Us time Nahusha bhi ek shocking event se gir chuka tha.

Usne Indra ki wife:

⚡ Indrani

ke saath misconduct kiya 😔

Aur sages ne curse de diya 😨

👉 “Tum giant snake ban jaoge!” 🐍

Uske baad Yayati king bana.

Aur usne apne brothers ko different directions me kingdoms de diye 🌍

🌸 Devayani and Sharmishtha

Ab story me entry hoti hai 2 girls ki 😮

🌸 Devayani

daughter of:

🔥 Shukracharya

(teacher of Asuras)

Aur dusri thi:

👑 Sharmishtha

daughter of demon king Vrishaparva.

Dono friends thi ❤️

Aur ek din apni thousand companions ke saath
garden me water games khelne gayi 🌸🌊

😳 Shiva Suddenly Appears

Jab woh water me thi,

suddenly:

🔱 Shiva and Parvati

wahan se guzre 😮

Sab girls embarrassment me quickly bahar nikli 😳

Aur haste-haste clothes pehenne lagi.

😠 The Dress Incident

Confusion me:

👑 Sharmishtha

galti se Devayani ke clothes pehen leti hai.

Devayani furious ho gayi 😡

Aur insulting tone me boli:

👉 “Tum servant ho!”

👉 “Mere clothes kaise pehen liye?”

👉 “Hum Brahmanas tumse superior hain!”

Woh apni Brahmana lineage aur spiritual superiority boast karne lagi 😬

🐍 Sharmishtha Gets Furious

Sharmishtha insult tolerate nahi kar paayi 😠

Woh snake ki tarah hiss karte hue boli:

👉 “Tum khud beggar jaisi ho!”

👉 “Tumhare father hamare palace me dependent hain!”

Aur anger me 😨

👉 Devayani ke clothes chheen liye
👉 usse well me push kar diya 💥

👑 Yayati Saves Devayani

Coincidentally ussi waqt:

👑 Yayati

hunting karte hue nearby aaye 🌲🏹

Unhe well me ek helpless girl dikhi 😮

Yayati ne apna upper cloth diya 🙏

Aur uska hand pakadkar usse bahar nikala ❤️

❤️ Devayani Falls in Love

Devayani emotionally boli:

👉 “Tumne mera hand hold kiya hai…”

👉 “Ab tum hi mere husband ho.” ❤️

Usne explain kiya:

👉 “Destiny ne hume milaya hai.” ✨

Yayati bhi uski taraf attracted ho gaya 😊

Aur proposal accept kar liya.

😠 Shukra Gets Angry

Devayani crying state me father ke paas gayi 😢

Aur sab bata diya.

Shukracharya furious ho gaye 😡🔥

Unhone demon king Vrishaparva ka kingdom chhodne ka decision le liya.

Vrishaparva panic me aa gaya 😨

Kyunki bina Shukra ke
Asuras weak ho jaate.

🙏 Devayani’s Condition

Shukra ne bola:

👉 “Meri daughter ko satisfy karo.”

Devayani ne condition rakhi 😮

👉 “Sharmishtha aur uski thousand maids…”

👉 “Meri servants bankar rahengi.”

King मजबूर tha 😔

Sharmishtha ne bhi apne people ko bachane ke liye sacrifice accept kar liya ❤️

💍 Marriage of Yayati and Devayani

Finally Devayani ki marriage Yayati se ho gayi 💍✨

Lekin Shukra ne warning di ⚠️

👉 “Kabhi bhi Sharmishtha ke saath relationship mat banana.”

🌸 Secret Relationship

Time passed ⏳

Devayani ko sons hue:

Yadu
Turvasu

Ek din Sharmishtha secretly Yayati ke paas aayi 😮

Aur boli:

👉 “Mujhe bhi children chahiye.”

Yayati confused ho gaya 😔

Usse Shukra ki warning yaad thi.

Lekin usne socha:

👉 “A woman asking for progeny should not be refused.”

Aur destiny ke flow me
usne relation accept kar liya.

Sharmishtha ko 3 sons hue:

Druhyu
Anu
Puru
😡 Devayani Discovers the Truth

Jab Devayani ko pata chala 😨

Woh jealousy aur rage se bhar gayi 😭

Aur directly father ke paas chali gayi.

Yayati uske peeche gaya ❤️

Usne:

apologies ki
sweet promises diye
even uske feet massage kiye 😔

Lekin Devayani calm nahi hui.

⚡ The Curse of Old Age

Shukracharya furious ho gaye 😡🔥

Aur Yayati ko curse diya:

👉 “Tum immediately old ho jaoge!” 👴

Ek second me:

wrinkles 😨
weakness
white hair

sab aa gaya.

😢 Yayati’s Plea

Yayati begged 😔

👉 “Main abhi pleasures se satisfied nahi hua…”

👉 “Please kuch solution do.”

Shukra ne kaha:

👉 “Agar koi willingly apni youth tumhe de…”

👉 “Toh tum exchange kar sakte ho.”

👦 Sons Tested

Yayati ne apne sons ko bulaya ❤️

❌ Yadu Refuses

Usne bola:

👉 “Without enjoying youth properly…”

👉 “Kaise detachment aayega?”

Dusre sons bhi refuse karte gaye 😔

Turvasu
Druhyu
Anu

Sabne mana kar diya.

🌟 Puru’s Great Sacrifice

Finally youngest son:

🌟 Puru

aaya.

Woh deeply respectful tha ❤️

Usne kaha:

👉 “Father ka debt kabhi repay nahi ho sakta.”

👉 “Best son wahi hai jo father ki wish samajhkar fulfill kare.”

Aur happily apni youth de di ✨

👑 Yayati Enjoys for Thousands of Years

Yayati fir young ban gaya 😮

Aur thousands of years tak pleasures enjoy karta raha 🌸

wealth 💰
women ❤️
luxury 👑
power ⚔️

Sab kuch.

Lekin… 😔

Uska desire kabhi end nahi hua.

🔥 The Great Realization

Finally Yayati ko truth samajh aaya ✨

Usne famous wisdom bola:

“Desire kabhi enjoyment se satisfy nahi hoti…”

“Jaise fire me ghee daalne se fire aur badhti hai.” 🔥

Yeh line immortal ho gayi Indian philosophy me 🌸

🌌 Spiritual Shift

Uske baad Yayati ne:

👉 kingdom return kiya
👉 detachment choose kiya
👉 Lord Vishnu ki devotion start ki 🙏

Usne realize kiya:

👉 Mind aur senses endless craving create karte hain 😔

Aur real peace sirf spiritual realization me hai ✨

King Parikshit quietly sunte rahe 😮

Unhe samajh aaya:

👉 Desire fulfill karne se desire khatam nahi hoti…

👉 Woh aur strong hoti jaati hai.

Moral:

Endless pleasure kabhi permanent satisfaction nahi deta
Self-control aur spiritual wisdom hi true peace dete hain
Aur real maturity tab aati hai jab insaan desire ki nature samajh leta hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 19
    with st.expander("Chapter 19 - Yayāti’s Retirement and Final Emancipation"):
        text1 = """ 
        👑 Yayati Finally Gets Tired of Pleasure

Hazaaron saal tak luxury aur pleasures enjoy karne ke baad bhi 😮

👑 King Yayati

andar se empty feel karne laga.

Usse realize hua 😔

👉 “Main spiritually fall ho gaya hoon…”

👉 “Desires ka koi end nahi.”"""
        create_image_text_layout(
            "attached_assets/chapter9/9.19.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Tab usne apni wife:

🌸 Devayani

ko ek deep symbolic story sunayi ✨

🐐 The Story of the Goat

Yayati bola:

👉 “Ek jungle me ek male goat tha…”

Ek din usne dekha 😮

👉 ek female goat well me gir gayi thi 🕳️🐐

Male goat uspar attracted ho gaya ❤️

Aur apne horns se soil hata-hatakar
uske liye escape path bana diya.

❤️ Many Female Goats Gather

Jab female goat bahar aayi
toh woh us male goat se attached ho gayi ❤️

Woh male goat strong aur attractive tha 😎

Isliye aur bhi female goats uske paas aane lagi 😮

Aur woh goat:

👉 lust aur pleasure me itna lost ho gaya 😔

ki apne real self ke baare me sochna hi bhool gaya.

😠 Jealousy and Separation

Ek din pehli female goat ne dekha 😨

ki uska mate dusri goats ke saath enjoy kar raha hai.

Woh hurt aur angry ho gayi 😢

Aur usse chhodkar chali gayi.

Male goat panic me uske peeche bhaaga 🐐💨

Lekin woh mana nahi paaya.

😨 The Castration

Female goat ke owner ne 😳

male goat ko punish kar diya.

👉 uske testicles cut kar diye 😨

Lekin later somehow
unhe wapas restore bhi kar diya ✨

Aur funny-sad part yeh tha 😮

👉 Itne sab ke baad bhi
woh goat pleasures me hi laga raha 😔

Kabhi satisfied nahi hua.

😔 Yayati’s Confession

Yayati ne softly Devayani se kaha ❤️

👉 “Woh goat main hoon…”

👉 “Main bhi desires me itna trapped ho gaya…”

👉 “Ki apne true self ko bhool gaya.”

🔥 The Famous Wisdom

Phir Yayati ne immortal line boli ✨

“Desire enjoyment se kabhi satisfy nahi hoti…”

“Jaise ghee daalne se fire aur badhti hai.” 🔥

Usne realize kiya:

👉 Wealth 💰
👉 gold
👉 women ❤️
👉 luxury 👑

kabhi permanent satisfaction nahi dete.

🧘 Spiritual Realization

Yayati ne kaha:

👉 “Jo sab beings ko equal dekhta hai…”

👉 “Aur attachment chhod deta hai…”

👉 “Usse har direction me peace milti hai.” 🌸

Usne warning bhi di 😮

👉 “Senses bahut powerful hote hain.”

👉 “Wise person bhi mislead ho sakta hai.”

Aur confess kiya:

👉 “1000 saal pleasures enjoy karne ke baad bhi…”

👉 “Meri craving khatam nahi hui.” 😔

🌲 Decision to Renounce

Finally Yayati ne decide kiya ✨

👉 “Ab main forest jaunga.”

👉 “Mind ko Brahman me focus karunga.”

👉 “Pleasure-pain se beyond jeena seekhunga.”

👑 Returning Youth to Puru

Usne apni youth:

🌟 Puru

ko wapas kar di ❤️

Aur khud old age accept kar li 👴

🌍 Division of the Kingdom

Phir usne kingdom divide kiya:

Druhyu → Southeast
Yadu → South
Turvasu → West
Anu → North

Aur:

👑 Puru

ko emperor banaya ✨

Kyunki woh sabse virtuous tha.

🌸 Yayati Leaves Everything

Yayati quietly forest chala gaya 🌲

Bilkul bird ki tarah
jo full-grown hone ke baad nest leave kar deta hai 🕊️

Usne:

senses control kiye
attachments chhode
ego dissolve kiya
meditation ki 🧘

Aur finally:

✨ Supreme Brahman

me merge ho gaya.

Bhagwan Vasudeva ki divine state attain kar li 🌌

🌸 Devayani’s Awakening

Devayani pehle uski goat story ko
sirf emotional joke samajh rahi thi 😅

Lekin baad me usse bhi realization hua ✨

Usne samjha:

👉 Relationships temporary hain
👉 Sab karma aur Maya ke according milte-bichhadte hain 😔

Bilkul travellers ki tarah
jo kuch time ke liye ek water-place par milte hain 🚶‍♂️🚶‍♀️

🙏 Devayani Also Renounces

Devayani ne bhi attachments chhod diye 🌸

Aur apna mind:

✨ Lord Krishna / Vishnu

par focus kar diya ❤️

Aur finally
woh bhi spiritually liberated ho gayi 🌌

🌟 Final Prayer

Rishi Shuka ne end me prayer ki 🙏

👉 “Salutations to Lord Vasudeva…”

👉 “Jo universe ka source hain…”

👉 “Jo sab beings ke inner soul hain…” ✨

King Parikshit silently sunte rahe 😮

Unhe deeply samajh aaya:

👉 Desire endless hai
👉 Attachment temporary hai
👉 Real freedom andar milti hai ✨

Moral:

Pleasure ki chasing kabhi complete satisfaction nahi deti
Self-control aur spiritual wisdom hi true peace dete hain
Aur sab relationships temporary hote hue bhi spiritual growth ka path ban sakte hain."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 20
    with st.expander("Chapter 20 - The History of Pūru’s race—Birth of Bharata"):
        text1 = """ 
        Rishi Shuka ne ab batayi 🌟

👑 Puru Vansh ki Story

Yahi woh royal line thi
jisme later born hue:

Bharata
Kuru
Pandavas
Kauravas

✨"""
        create_image_text_layout(
            "attached_assets/chapter9/9.20.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        👑 Descendants of Puru
Puru ke baad lineage aise chali:


Janamejaya


Prachinvan


Pravira


Namasyu


Charupada


Sudyu


Bahugava


Samyati


Ahamyati


Raudrashva



🌸 Raudrashva and the Celestial Nymph
Raudrashva ne celestial apsara:
✨ Ghritachi
se marriage ki ❤️
Aur unke 10 sons hue 😮

Unme se ek tha:
🌟 Rteyu
jiski line me later born hua:
👑 Dushyanta

🌲 Dushyanta Meets Shakuntala
Ek din King Dushyanta hunting par gaya 🏹🌲
Aur chance se pahunch gaya:
🧘 Kanva Rishi ke Ashram

Wahan usne dekhi ek extraordinary beautiful girl 😮✨
🌸 Shakuntala

Uski beauty itni divine thi
ki Dushyanta instantly attracted ho gaya ❤️
Uski fatigue bhi disappear ho gayi 😳

❤️ Their First Conversation
King softly bola 😊
👉 “Tum kaun ho?”
👉 “Itni beautiful princess jungle me kya kar rahi hai?”

Shakuntala politely boli 🌸
👉 “Main Vishwamitra aur Menaka ki daughter hoon.”
👉 “Rishi Kanva ne mujhe raise kiya hai.”

Usne king ko hospitality offer ki 🍚
Aur bola:
👉 “Aap yahan rest kar sakte hain.”

💍 Gandharva Marriage
Dushyanta ne realize kiya 😮
👉 “Tum royal lineage ki lagti ho.”

Dono ek dusre ko pasand karne lage ❤️
Aur unhone:
💍 Gandharva Marriage
kiya.
Yani mutual love aur consent based marriage ✨

Dushyanta next day capital laut gaya 👑
Aur kuch time baad:
👶 Shakuntala ne ek son ko birth diya

🦁 Child Bharata
Woh child ordinary nahi tha 😮
Usme divine energy thi ✨

Bachpan me hi:
👉 lions pakad leta tha 🦁
👉 wild animals ke saath khelta tha 😳
Sab uski immense power dekhkar amazed ho jaate.

🌸 Shakuntala Goes to the King
Jab boy bada hua,
Shakuntala usse lekar
Dushyanta ke court pahunchi 👑
Aur boli:
👉 “Yeh tumhara son hai.”

😔 Dushyanta Refuses
Lekin king ne public me accept nahi kiya 😨
Shayad reputation ya doubt ki wajah se.

⚡ Divine Voice from Heaven
Tab suddenly heaven se loud voice aayi 🌌⚡
Sabne suna 😮

Voice boli:
👉 “Mother sirf child ko carry karti hai…”
👉 “Son actually father ka extension hota hai.”
👉 “Shakuntala sach bol rahi hai.”

Aur bola:
👉 “Is child ko neglect mat karo.”
👉 “Yeh extraordinary greatness achieve karega.” ✨

👑 Birth of Bharata’s Glory
Dushyanta immediately emotional ho gaya ❤️
Aur Shakuntala aur child ko accept kar liya.

Woh child bana:
🌟 Emperor Bharata

India ka ancient name:
🇮🇳 Bharat
isi great king ke naam par pada ✨

🌍 Bharata’s Greatness
Bharata ke body par divine marks the 😮


hand par chakra symbol ☸️


feet par lotus marks 🌸



Woh incredibly powerful emperor bana 👑
Usne:


many Ashvamedha sacrifices kiye 🔥


huge donations diye 💰


entire Earth conquer ki 🌍



🐘 Massive Donations
Rishi Shuka ne bataya 😮
👉 Bharata ne lakhs of elephants donate kiye
👉 countless cows gift ki
👉 huge sacrifices perform kiye

Uski glory itni great thi ✨
ki future kings bhi uske level tak nahi pahunch sake.

⚔️ Conquests
Bharata ne many tribes defeat kiye:


Hunas


Yavanas


Shakas


Kiratas


Aur unrighteous rulers ko punish kiya ⚔️

🌌 Bharata’s Realization
Lekin after ruling for thousands of years 😮
Bharata ko realization hua ✨
👉 “Kingdom temporary hai.”
👉 “Power, fame aur senses sab unreal hain.”

Aur usne detachment choose kiya 🌸

😢 Tragedy of Bharata’s Sons
Bharata ki 3 queens thi 👑
Unke sons hue…
Lekin Bharata ne feel kiya 😔
👉 “Yeh mere jaise nahi lagte.”

Queens darr gayi 😨
ki king unhe reject kar dega.
Aur fear me unhone apne hi children ko maar diya 😢

😮 Bharata Gets a New Son
Ab dynasty extinction ke danger me thi 😨
Toh Bharata ne sacrifices kiye 🙏
Aur:
🌪️ Marut Gods
ne usse ek child diya.

Woh child tha:
🌟 Bharadvaja

😨 Strange Birth of Bharadvaja
Uski birth story bhi shocking thi 😮
Brihaspati ne forcefully relation banaya:
🌸 Mamata
ke saath
jab woh already pregnant thi 😨

Womb me existing child ne protest bhi kiya 😳
Lekin Brihaspati ne ignore kiya.

Fallen semen se ek child born hua ✨
Lekin dono parents usse accept nahi karna chahte the 😔

Woh literally argue karne lage:
👉 “Tum raise karo!”
👉 “Nahi tum raise karo!” 😅

Isi argument se naam bana:
🌟 Bharadvaja
(“bhara dvajam” type phrase se derived)

👑 Adopted by Bharata
Finally gods ne child ko protect kiya ❤️
Aur later usse Bharata ko de diya.

Uska adopted royal name bana:
👑 Vitatha

Is tarah Bharata ki dynasty continue hui ✨

King Parikshit quietly sunte rahe 😮
Unhe samajh aaya:
👉 Great dynasties bhi suffering aur imperfection se free nahi hoti 😔
👉 Lekin dharma aur destiny lineage ko continue kar dete hain 🌸

Moral:


Fame aur power temporary hain


Truth eventually reveal ho hi jaata hai


Aur greatness birth se nahi, character aur destiny se emerge hoti hai.

"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 21
    with st.expander("Chapter 21 - The Race of Bharata—The History of Rantideva"):
        text1 = """ 
        Rishi Shuka ne ab ek aise king ki story batayi 🌸

jise heaven aur earth dono jagah praise kiya jaata tha ✨

👑 King Rantideva

Woh Bharata dynasty ka king tha 👑

Lekin uski greatness power ya war ki wajah se nahi…

👉 compassion ❤️
👉 sacrifice 🌸
👉 selfless devotion ✨

ki wajah se famous hui."""
        create_image_text_layout(
            "attached_assets/chapter9/9.21.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        🌿 Rantideva’s Nature

Rantideva ka attitude bahut unique tha 😊

Jo bhi wealth uske paas aati 💰

woh instantly donate kar deta tha 🙏

Kyunki woh maanta tha:

👉 “Wealth temporary hai.”

Slowly situation itni extreme ho gayi 😮

ki woh aur uski family khud poor aur hungry ho gaye 😔

😢 Forty-Eight Days Without Food

Ek time aisa aaya 😨

ki:

48 din tak

Rantideva aur uski family ko proper food ya water nahi mila.

Sab:

weak 😵
thirsty 💧
trembling 😔

ho gaye the.

Finally 49th day 🌅

unhe thoda food mila ❤️

ghee
sweet rice
milk preparation
aur thoda water 💧

Family finally relief feel karne lagi 😊

Sab khana khane hi wale the…

🧘 A Brahmana Arrives

Tabhi 😮

ek hungry:

🧘 Brahmana guest

aa gaya.

Ancient tradition ke according 🙏

guest ko sacred maana jaata tha.

Aur Rantideva har being me:

✨ Lord Hari

ko dekhte the.

Isliye unhone respectfully
apna food us Brahmana ko de diya ❤️

😮 Another Guest Appears

Ab jo food bacha tha 🍚

family phir khane baithi.

Lekin tabhi:

🚶 ek Shudra traveller

aa gaya.

Woh bhi hungry tha 😔

Rantideva ne bina hesitation usse bhi food de diya 🌸

🐕 The Man With Dogs

Ab aur bhi little food bacha tha 😮

Tab ek aur stranger aaya:

👉 apne hungry dogs ke saath 🐕🐕🐕

Woh bola 😔

👉 “King… mujhe aur mere dogs ko food do.”

Rantideva ne lovingly 😢

remaining food bhi unhe de diya.

Aur dogs ko bhi respectfully bow kiya ❤️

💧 The Final Test

Ab bas:

😨 ek glass water

bacha tha.

Rantideva khud almost dying tha thirst se 😔

Lekin jaise hi woh water peene laga…

tabhi ek exhausted:

😢 Chandala

(low social status person)

wahan aa gaya.

Woh painful voice me bola:

👉 “Please… mujhe water de do…” 💧

🌌 Rantideva’s Great Declaration

Yeh sunkar Rantideva ka heart compassion se bhar gaya ❤️

Aur usne immortal words bole ✨

👉 “Mujhe supernatural powers nahi chahiye.”

👉 “Mujhe liberation bhi nahi chahiye.”

😮 “I Want To Bear Others’ Suffering”

Woh bola 🌸

👉 “Main bas itna chahta hoon…”

👉 “Ki sab beings ka suffering khatam ho jaaye.”

👉 “Agar mujhe unka pain bear karna pade…”

👉 “Toh bhi main ready hoon.” ❤️

Phir usne kaha 😢

👉 “Is thirsty person ko water dene se…”

👉 “Meri own hunger-thirst bhi meaningful lagne lagi.”

Aur usne apna last water bhi de diya 💧🙏

Khud almost death ke point par hote hue bhi.

✨ The Divine Revelation

Suddenly 😮🌌

woh sab guests transform ho gaye.

Actually woh ordinary people nahi the 😳

👉 gods the
👉 divine beings the

Jo:

🌟 Lord Vishnu

ke instructions par Rantideva ko test kar rahe the.

🙏 Gods Reveal Themselves

Brahma aur dusre devas
apne true divine forms me saamne aaye ✨

Lekin shocking part 😮

👉 Rantideva ne unse koi boon nahi manga.

Na heaven ☁️
Na power 👑
Na moksha 🌌

Uska mind already fully:

❤️ Lord Vasudeva

me absorbed tha.

🌸 Freedom From Illusion

Rishi Shuka ne explain kiya ✨

ki Rantideva ka selfless devotion itna pure tha 😮

ki:

🌌 Maya (illusion)

automatically disappear ho gayi.

Bilkul dream ki tarah.

Aur jo yogis uske saath rehte the 😊

woh bhi inspired hokar:

🙏 Narayana devotion

me deeply immersed ho gaye.

🏰 The Line of Hastinapura Begins

Story ke baad Shuka lineage continue karta hai ✨

Bharata line me later born hua:

👑 Hasti

jisne:

🏰 Hastinapura

city build ki.

Wahi city later:

Kauravas
Pandavas

ki capital bani ⚔️

Uske descendants me hue:

Ajamidha
Dvimidha
Purumidha

aur later many famous lineages 🌸

🌟 Birth of Kripa and Kripi

Story me later ek strange birth bhi aati hai 😮

Warrior sage:

🏹 Sharadvan

ne apsara Urvashi ko dekha ✨

Aur accidentally uska seed reeds par gir gaya.

Usse twins born hue 😳

👦 Kripa
👧 Kripi

King Shantanu ne hunting ke time unhe discover kiya ❤️

Aur compassion se adopt kar liya.

Later:

👧 Kripi

became wife of:

⚔️ Drona

Aur:

👦 Kripa

Mahabharata ka famous warrior aur teacher bana ✨

🌌 Deeper Meaning

Rantideva ki story selfless compassion ka highest example hai ❤️

Usne dikhaya:

👉 Real spirituality sirf meditation nahi hoti.

👉 Dusron ka suffering feel karna bhi divine path hai 🌸

Uska ideal almost Bodhisattva jaisa tha ✨

👉 “Main khud suffer kar lunga…”

👉 “Lekin doosron ka pain kam ho jaaye.” ❤️

🌟 Moral
True greatness sacrifice me hoti hai
Compassion sabse powerful spiritual quality hai
Aur selfless service ego aur illusion ko dissolve kar sakti hai ✨"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 22
    with st.expander("Chapter 22 - The Royal Dynasties of Pāñcāla, Magadha and Kuru"):
        text1 = """ 
        Rishi Shuka ne ab bataya 🌌

🌟 Great Royal Dynasties

ki kaise famous kingdoms aur Mahabharata ke legendary heroes ek dusre se connected the.

👑 Panchala Dynasty

Story start hoti hai:

👑 King Divodasa

se.

Unke descendants me later born hue:"""
        create_image_text_layout(
            "attached_assets/chapter9/9.22.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Mitreyu
Cyavana
Sudasa
Sahadeva
Somaka
👶 Somaka’s Hundred Sons

King Somaka ke 😮

100 sons

the.

Unme:

eldest → Jantu
youngest → Prishata

Prishata ka son bana:

👑 Drupada

Aur Drupada ke children hue 🌸⚔️

🌸 Draupadi
⚔️ Dhrishtadyumna

aur dusre famous warriors.

⚔️ Dhrishtadyumna’s Son

Dhrishtadyumna ki line me later born hua:

⚔️ Dhrishtaketu

Isi lineage ko:

🌟 Panchala Dynasty

bola gaya.

🌞 Birth of King Kuru

Ab Shuka ne explain kiya 😮

ki:

👑 Samvarana

ne marriage ki:

☀️ Tapati

(Sun-god ki daughter)

se ❤️

Unke son hue:

🌟 King Kuru

Wahi legendary king
jiske naam par:

⚔️ Kurukshetra

famous hua ✨

👑 Kuru’s Sons

Kuru ke sons the:

Parikshit
Sudhanu
Jahnu
Nishadhashva

Aur isi line se later
Kauravas aur Pandavas born hue 🌌

🏰 Magadha Dynasty and Jarasandha

Kuru line ke parallel 😮

another powerful kingdom rise hua:

👑 Magadha

Us dynasty me later born hua:

😨 Jarasandha

Uski birth bahut strange thi 😳

King Brihadratha ko:

👉 aadha-aadha child mila 😨

Dono halves alive nahi the.

Queen ne un parts ko throw kar diya 😔

Lekin ek demoness:

👹 Jara

ne playfully unhe join kar diya ✨

Aur suddenly child alive ho gaya 😮

Isliye naam pada:

😨 Jarasandha

(“joined by Jara”)

Later woh Mahabharata ka terrifying king bana ⚔️

👑 Birth of Shantanu

Ab lineage aati hai:

👑 Pratipa

par.

Uske 3 sons hue:

Devapi
Shantanu
Bahlika
🌲 Devapi Leaves the Throne

Eldest brother Devapi kingdom chhodkar forest chala gaya 🌲🧘

Spiritual life choose karke.

Isliye younger brother:

👑 Shantanu

king bana.

✨ Shantanu’s Divine Power

Shantanu ke paas magical blessing thi 😮

👉 Jise woh touch karta…

woh old person bhi young aur healthy feel karne lagta ✨

Isi miracle ki wajah se
uska naam famous hua:

🌟 Shantanu
🌧️ The Twelve-Year Drought

Ek time kingdom me 😨

12 saal tak rain nahi hui

Brahmanas ne explain kiya 😮

👉 “Elder brother living hone ke bawajood…”

👉 “Younger brother ka throne par baithna imbalance create kar raha hai.”

Shantanu ne Devapi ko wapas bulane ki try ki ❤️

Lekin ministers ne secretly Devapi ko Vedas ke against ideas sikha diye 😔

Jab Devapi ne anti-Vedic baatein bolni shuru ki 😨

tab Indra ne finally rain bhej di 🌧️

Kyunki ab Devapi officially throne ke unfit maana gaya.

⚔️ Bhishma Is Born

Ab story ka legendary moment aata hai ✨

Shantanu ne:

🌊 Goddess Ganga

se marriage ki ❤️

Unke son hue:

⚔️ Bhishma

Bhishma extraordinary tha 😮

dharma expert 📜
unmatched warrior ⚔️
great devotee 🙏

Even:

⚡ Parashurama

bhi uski fighting skill se impressed the 😳

🌸 Satyavati and Vyasa

Later Shantanu ne marriage ki:

🌸 Satyavati

se.

Uske sons hue:

Chitrangada
Vichitravirya

Lekin usse pehle 😮

Satyavati ka ek son already tha:

🌌 Vedavyasa

Woh sage:

✨ Parashara

aur Satyavati ka son tha.

Shuka proudly bolta hai 😊

👉 “Maine Bhagavatam directly Vyasa se seekha.”

😔 Death of Vichitravirya

Vichitravirya ne marriage ki:

Ambika
Ambalika

se ❤️

Lekin young age me hi
woh disease se mar gaya 😢

Aur uske koi children nahi hue.

🌌 Birth of Dhritarashtra, Pandu and Vidura

Tab Satyavati ne request ki 🙏

ki Vyasa dynasty continue kare.

Vyasa se born hue:

👑 Dhritarashtra
⚔️ Pandu
🌸 Vidura
⚔️ Kauravas and Pandavas

Dhritarashtra + Gandhari ke 😮

100 sons

hue.

Sabse bada:

😈 Duryodhana

Pandu curse ki wajah se children produce nahi kar sakta tha 😔

Isliye divine blessings se born hue:

🌟 Yudhishthira
💪 Bhima
🏹 Arjuna

through Kunti.

Aur:

✨ Nakula
✨ Sahadeva

through Madri.

🌸 Draupadi’s Sons

Draupadi ke bhi 5 sons hue ❤️

Prativindhya
Sutasena
Shrutakirti
Satanika
Shrutakarma
🐉 Other Famous Sons

Bhima + Hidimba → 🌲 Ghatotkacha

Arjuna + Ulupi → 🌊 Iravan

Arjuna + Chitrangada → 👑 Babhruvahana

🌟 Birth of Abhimanyu

Arjuna + Subhadra ke son hue:

⚔️ Abhimanyu

Wahi heroic warrior
jo Kurukshetra war me legendary bana ✨

Aur Abhimanyu + Uttara ke son hue:

👑 Parikshit
⚡ Krishna Saves the Baby

War ke end me 😨

Ashwatthama

ne Brahmastra launch kiya.

Target tha:

👉 unborn baby Parikshit.

Lekin:

🌟 Shri Krishna

ne divine power se baby ko save kar liya ❤️✨

👑 Future Kings

Shuka ne future lineage bhi batayi 😮

Parikshit ke sons:

Janamejaya
Shrutasena
Bhimasena
Ugrasena
🐍 Snake Sacrifice

Janamejaya later 😡

snake king Takshaka se revenge lene ke liye:

🔥 Sarpa Yajna

perform karega.

Jahan snakes ko sacrificial fire me pull kiya jaayega 😨🐍

🌊 Destruction of Hastinapura

Future me 😮

🌊 Ganga flood

Hastinapura ko wash away kar degi.

Aur kings later:

🏰 Kaushambi

shift ho jayenge.

🌌 End of the Lunar Dynasty

Finally Shuka conclude karta hai ✨

ki Kali Yuga ke end me:

🌙 Lunar Dynasty

gradually extinct ho jayegi.

🌟 Deeper Meaning

Yeh chapter basically:

Mahabharata family tree 🌳
destiny ⚖️
rise and fall of kingdoms 👑
divine intervention ✨

sabko connect karta hai.

It also shows 😮

👉 Great dynasties bhi temporary hoti hain
👉 Even mighty kingdoms disappear ho jaate hain
👉 Lekin dharma aur stories immortal rehte hain 🌸

🌌 Moral
Power aur kingdoms temporary hain
Destiny continuously generations ko shape karti hai
Aur righteousness hi kisi lineage ko true greatness deta hai ✨"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 23
    with st.expander("Chapter 23 - The History of the Dynasties of Anu, Druhyu, Turvasu and Yadu"):
        text1 = """ 
        Rishi Shuka ne ab 🌙 Lunar Dynasty ki aur branches explain karni start ki ✨

Yeh different kingdoms aur famous warriors ki origins ki story thi.

🌟 Descendants of Anu

King Yayati ke son:

👑 Anu

ki line me kai powerful kings born hue."""
        create_image_text_layout(
            "attached_assets/chapter9/9.23.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Sabse pehle aaye:

Sabhanara
Kalanara
Srinjaya
Janamejaya
Mahashila
Mahamanas
👑 Ushinara and Titikshu

Mahamanas ke 2 famous sons hue:

Ushinara
Titikshu
⚔️ King Shibi

Ushinara ke son hue:

🌟 King Shibi

Wahi legendary king 😮

jo later apni flesh tak sacrifice karne ke liye famous hua ❤️

Uske sons the:

Vrishadarbha
Suvira
Madra
Kaikeya
🌍 Eastern Kingdoms Are Born

Ab Titikshu ki line me later born hua:

👑 Bali

Bali childless tha 😔

Toh sage:

🧘 Dirghatamas

ne uski queen se children produce kiye.

Unse born hue 😮

Anga
Vanga
Kalinga
Suhma
Pundra
Andhra

Aur inke names par hi later famous regions bane 🌍✨

👉 Anga
👉 Bengal (Vanga)
👉 Kalinga
👉 Andhra etc.

🌧️ Romapada and Rishyashringa

Iss line me later born hua:

👑 Romapada

Woh Ayodhya king:

👑 Dasharatha

ka close friend tha ❤️

Ek time kingdom me rain band ho gayi 😨🌧️

Sab drought se suffer karne lage.

🧘 The Deer-Horned Sage

Tab sages ne suggest kiya 😮

👉 “Rishyashringa ko lao.”

Woh innocent forest sage tha 🌲

jo women se almost unfamiliar tha 😳

Beautiful courtesans ne:

music 🎶
dance 💃
flirting 😅

use attract kiya
aur kingdom me le aaye.

Jaise hi woh aaya ✨

👉 rain wapas aa gayi 🌧️❤️

Usne sacrifices perform kiye 🔥

Aur:

Romapada ko child diya
Dasharatha ko bhi sons milne ka blessing diya ✨
⚔️ Birth of Karna

Ab lineage me later born hua:

👑 Adhiratha

Ek din woh Ganga river ke paas tha 🌊

Tab usse ek floating basket mili 😮

Andar ek divine baby tha ✨👶

Actually woh child tha:

⚔️ Karna
😢 Karna’s Secret Birth

Kunti ne marriage se pehle
Sun-god ki blessing se Karna ko birth diya tha ☀️

Lekin society ke fear se 😔

usne baby ko river me flow kar diya.

Childless Adhiratha ne lovingly usse adopt kar liya ❤️

Aur raise kiya as his own son.

Later Karna ka son hua:

⚔️ Vrishasena
🌍 Descendants of Druhyu

Yayati ke another son:

👑 Druhyu

ki line bhi continue hui.

Uske descendants north regions me settle hue 🌌

Aur many:

🌍 Mleccha kingdoms

establish kiye.

👑 Descendants of Turvasu

Turvasu ki line me later born hua:

👑 Maruta

Woh childless tha 😔

Isliye usne adopt kiya:

👑 Dushyanta

ko.

Lekin Dushyanta later
wapas apni Puru dynasty me return kar gaya ✨

🌟 Beginning of the Yadu Dynasty

Ab Shuka excited tone me bolta hai 😊

👉 “Ab main Yadu dynasty ki story bataunga.”

Aur special reason bhi diya 😮

👉 “Isi dynasty me Bhagwan Vishnu human form me descend honge.” ✨

Yani:

🌟 Shri Krishna’s Lineage
⚔️ Haihaya Branch

Yadu ke son:

👑 Sahasrajit

ki line me born hua:

⚔️ Kartavirya Arjuna

Woh insanely powerful king tha 😨

Aur:

🙏 Dattatreya

ki grace se yogic powers gain ki thi.

😮 Thousand-Armed King

Kartavirya Arjuna ke baare me legends the 😳

👉 uske 1000 arms the
👉 seven continents rule karta tha 🌍
👉 unmatched warrior tha ⚔️

Usne:

sacrifices
donations
tapasya
victories

sabme extraordinary greatness achieve ki.

⚔️ Battle With Parashurama

Lekin later 😨

⚡ Parashurama

ne uski dynasty destroy kar di.

Uske 1000 sons me se
sirf 5 survive kar paaye 😔

Unme se ek line se later:

🌟 Vrishni clan

start hua.

Aur isi se:

🌟 Yadavas

famous bane ✨

🌸 The Strange Story of Jyamagha

Ab aati hai ek funny-dramatic story 😅

Yadu line me ek king hua:

👑 Jyamagha

Uski wife thi:

🌸 Shaibya

Problem yeh thi 😮

👉 unke koi children nahi the
👉 aur king wife se bahut darta tha 😅

Isliye woh second marriage karne ki himmat nahi karta tha 😨

😳 The Captured Princess

Ek battle ke baad ⚔️

Jyamagha ek beautiful princess ko chariot me le aaya.

Shaibya ne dekha 😠

Aur instantly furious ho gayi:

👉 “Yeh kaun hai?!”

👉 “Meri jagah chariot me kaise baithi hai?”

King panic me aa gaya 😨💦

Aur trembling voice me bola:

👉 “W-Woh… tumhari daughter-in-law hai…” 😳

😅 Shaibya’s Savage Reply

Shaibya sarcastically boli 😏

👉 “Main barren hoon.”

👉 “Mera son hi nahi…”

👉 “Toh daughter-in-law kahan se aa gayi?” 😅

King ne quickly answer diya 😨

👉 “Future me jo son tumse born hoga…”

👉 “Yeh uski wife banegi.”

🌌 Divine Blessing

Actually secretly 😮

Jyamagha gods aur ancestors ko pray kar raha tha 🙏

Aur unhone bless kiya ✨

👉 “So be it.”

Kuch time baad miracle hua 😳

👉 menopause ke baad bhi
Shaibya pregnant ho gayi ❤️

Aur unka son born hua:

👑 Vidarbha

Later usne wahi princess marry ki 🌸

Aur:

🌍 Vidarbha kingdom

establish hua.

🌌 Deeper Meaning

Yeh chapter dikhata hai 😮

ki dynasties sirf politics nahi hoti.

Unme:

destiny ✨
divine intervention 🌌
humor 😅
suffering 😔
love ❤️
fear 😨

sab mix hote hain.

Especially Jyamagha story 😅

human relationships ki awkwardness aur emotional reality ko beautifully show karti hai.

🌟 Moral
Destiny unexpected ways me unfold hoti hai
Fear aur attachment kings ko bhi vulnerable bana dete hain
Aur divine grace impossible situations ko bhi transform kar sakti hai ✨"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 24
    with st.expander("Chapter 24 - The History of the Race of Yadu"):
        text1 = """ 
        Rishi Shuka ne ab 🌟 Yadu Dynasty ki detailed story continue ki.

Yahi woh legendary lineage thi 😮

jisme later:

🌟 Shri Krishna

birth lene wale the."""
        create_image_text_layout(
            "attached_assets/chapter9/9.24.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        👑 Vidarbha’s Descendants
King Vidarbha ke sons hue:


Kusha


Kratha


Romapada



🌸 Chedi Kingdom Begins
Romapada ki line se later born hue:
👑 Chedi kings

Isi dynasty me later famous hua:
😈 Shishupala

Jo Krishna ka enemy bana ⚔️

🌟 The Satvata Clan
Kratha ki lineage me later born hua:
🌟 Satvata

Aur Satvata ke 7 sons hue 😮
jinse different Yadava branches start hui:


Bhajamana


Bhaji


Divya


Vrishni


Devavriddha


Andhaka


Mahabhoja



Isi se later:


Vrishnis


Bhojas


Andhakas


Yadavas


sab famous clans bane ✨

🌸 Devavriddha and Babhru
Shuka specially praise karta hai 😊
🌟 Devavriddha
aur uske son:
🌟 Babhru
ko.

Itna spiritually powerful influence tha 😮
ki:
14,065 people
unke guidance se liberation achieve kar gaye ✨🙏

⚔️ The Vrishni Clan
Vrishni ke descendants me later aaye:


Sini


Anamitra


Nighna



Nighna ke sons hue:


Satrajit


Prasena



💎 Syamantaka Jewel Story Begins
Yahi later:
💎 Syamantaka jewel
wali famous Krishna story ka starting point bana 😮

⚔️ Satyaki’s Line
Another branch me born hua:
⚔️ Satyaki (Yuyudhana)

Wahi Mahabharata ka heroic warrior ✨
jo Krishna aur Pandavas ka loyal ally tha ❤️

🌟 Akrura Is Born
Vrishni line me later born hua:
🌟 Akrura

Woh Krishna ka great devotee aur wise diplomat tha 🌸

Later wahi Mathura se:
🌟 Krishna aur Balarama
ko Vrindavan se le jaayega.

😈 The Line of Kamsa
Andhaka branch me later born hue:
👑 Ahuka
ke sons:


Devaka


Ugrasena



😨 Ugrasena’s Son
tha:
😈 Kamsa

Kamsa ke brothers bhi the:


Sunama


Nyagrodha


Kanka etc.



🌸 Devaki and Her Sisters
Devaka ki 7 daughters thi ✨
Sabse important:
🌸 Devaki

Later:
🌟 Vasudeva
ne Devaki aur uski sisters se marriage ki ❤️

👑 Birth of Vasudeva
Ab Shuka lineage ko Krishna ke father tak laata hai 🌌

Lineage me later born hue:


Shura


Devamidhha


Aur phir:
🌟 Vasudeva

Uske birth par heavenly drums baje 😮🥁
Isliye uska title pada:
🌟 Anakadundubhi

🌸 Kunti’s Secret
Shura ki daughter thi:
🌸 Pritha (Kunti)

Use childless king Kuntibhoja ko adopt kar diya gaya ❤️

🧘 Durvasa’s Blessing
Sage Durvasa usse pleased hue 😊
Aur ek divine mantra diya ✨
👉 jis se gods ko invoke kiya ja sakta tha.

☀️ Birth of Karna
Curiosity me 😮
Kunti ne Sun-god ko invoke kar diya.
Aur instantly:
☀️ Surya
uske saamne appear ho gaye 😳

Kunti scared ho gayi 😨
👉 “Main sirf mantra test kar rahi thi!”

Lekin Surya ne kaha ✨
👉 “Gods ka appearance fruitless nahi hota.”

Aur Kunti ko ek divine son mila:
⚔️ Karna

Woh newborn baby:


golden armor ✨


earrings 💎


ke saath born hua.

Fear aur social shame ki wajah se 😔
Kunti ne usse river me flow kar diya 🌊

😈 Shishupala and Dantavakra
Shura ki other daughters bhi important dynasties me married hui.

Ek daughter se born hua:
😈 Dantavakra

Dusri se born hua:
😈 Shishupala

Dono actually:
🌌 Vishnu’s gatekeepers
(Jaya-Vijaya)
ke cursed incarnations the 😮

🌟 Vasudeva’s Many Wives
Vasudeva ki many wives thi 😊
Sabse important:


🌸 Rohini


🌸 Devaki



🌟 Rohini’s Sons
Rohini se born hue:
💪 Balarama
aur many brothers.

🌟 Devaki’s Sons
Devaki se 8 sons born hue.

Pehle 6 ko 😢
😈 Kamsa
ne kill kar diya.

7th child:
💪 Sankarshana (Balarama)
miraculously Rohini ke womb me transfer hua ✨

Aur:
🌟 8th child
tha:
🌟 Shri Krishna Himself

🌸 Birth of Subhadra
Shuka batata hai 😊
ki Devaki line me later born hui:
🌸 Subhadra

Jo later:
🏹 Arjuna
ki wife bani ❤️
Aur:
⚔️ Abhimanyu
ki mother bani.

🌌 Why Krishna Incarnates
Shuka ab deep philosophy explain karta hai ✨

👉 Jab dharma decline hota hai
👉 Aur evil increase hota hai
Tab:
🌟 Lord Hari
earth par descend karte hain ❤️

Unka purpose hota hai:


devotees ko protect karna 🙏


evil kings destroy karna ⚔️


dharma restore karna ✨



⚔️ Krishna Lightens Earth’s Burden
Earth evil kings aur giant armies se overloaded ho gayi thi 😨
Toh Krishna ne:
⚔️ Mahabharata War
ke through Earth ka burden reduce kiya.

Lekin interestingly 😮
👉 credit Arjuna ko diya gaya.

🌟 Krishna’s Divine Beauty
Shuka emotional tone me Krishna ko describe karta hai ❤️

People Krishna ko dekhkar mesmerized ho jaate the 😮


smiling face 😊


lotus eyes 🌸


shining earrings ✨


sweet speech 🎶



Aur log blink karne wale god:
😠 Nimi
par bhi angry ho jaate the 😂
Kyunki blinking ki wajah se
Krishna ka face ek second ke liye hide ho jaata tha 😅❤️

🌸 Krishna’s Earthly Pastimes
Krishna ne:


Vrindavan me childhood spend kiya 🌿


demons destroy kiye ⚔️


many queens se marriage ki 👑


sons produce kiye ✨


sacrifices perform kiye 🔥


Vedic dharma restore kiya 🌌



🌟 Final Departure
Earth mission complete hone ke baad 😔
Krishna ne:
🌌 Uddhava
ko highest spiritual wisdom diya ✨
Aur phir:
🌟 apne divine abode
wapas chale gaye ❤️

🌌 Deeper Meaning
Yeh chapter sirf genealogy nahi tha 😮
Yeh Krishna ke divine appearance ki preparation thi ✨

Sab lineages, dynasties aur births ultimately:
🌟 Krishna Leela
ki taraf lead kar rahe the.

🌟 Moral


Divine incarnations tab aate hain jab dharma weak ho jaata hai


Great dynasties bhi Bhagwan ki cosmic plan ka part hoti hain


Aur devotion Krishna ki beauty aur actions ko sunne se naturally awaken hoti hai ❤️

"""
        create_image_text_layout(text_content=text2, layout="full")
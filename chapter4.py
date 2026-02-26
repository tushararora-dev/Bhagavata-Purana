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
    create_image_text_layout("attached_assets/chapter4/chapter4.jpg", layout="full")

    text0 = """
    <h2>Book 4 - Fourth Skandha</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")

    # Book 4 - Fourth Skandha
    
    # Book 4 - Fourth Skandha

    # Chapter 1
    with st.expander("Chapter 1 - The Progeny of Svāyambhuva Manu’s Daughters"):
        text1 = """ 
        Chapter 1 — Hinglish Story (Simple Moral Style)
Manu ki Betiyon ka Vistaar

Maitreya Rishi ne Vidura se kaha,

"Manu ke do putra the — Priyavrata aur Uttanapada.
Par unki teen betiyan bhi thi."

Unka naam tha —
🌸 Akuti
🌸 Devahuti
🌸 Prasuti"""
        create_image_text_layout(
            "attached_assets/chapter4/4.1.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        🌼 Akuti ki Kahani

Manu ne Akuti ka vivaah Rishi Ruchi se kiya.

Ek vishesh shart par.

Putrika dharma.

Iska matlab —
jo putra paida hoga,
woh Manu ka vansh badhayega.

Akuti ne judwa bachche paida kiye.

Ek beta.
Ek beti.

Beta tha — Yajna.
Woh swayam Vishnu ka avataar tha.

Beti thi — Dakshina.
Woh Lakshmi ka ansh thi.

Yajna ne Dakshina se vivaah kiya.

Unke 12 putra hue.

Unka naam tha —
Tosha, Pratosha, Santosh, Bhadra, Shanti,
Idaspati, Idhma, Kavi, Vibhu, Svahna,
Sudeva, Rocana.

Ye sab milkar devta bane.

🌿 Devahuti ki Kahani

Devahuti ka vivaah Kardama Rishi se hua.

Unki kahani pehle hi batai ja chuki thi.

Unhi ke ghar Bhagwan Kapila ka janm hua tha.

🌺 Prasuti ki Kahani

Prasuti ka vivaah Daksha Prajapati se hua.

Daksha ke ghar se vansh teenon lokon mein phail gaya.

🌳 Kardama ki Betiyon ka Vansh

Kardama ki 9 betiyan thi.

Sabka vivaah bade Rishiyon se hua.

Unse poori srishti badhi.

🌊 Ganga ka Janm

Kalā ne Rishi Marichi se shaadi ki.

Unka putra tha — Kashyapa.

Aur ek beti thi — Devakulyā.

Wahi Devakulyā agle janm mein bani —
✨ Maa Ganga.

🌙 Atri aur Anasuya

Atri Rishi aur Anasuya ke ghar teen mahan putra hue —

🌙 Chandra (Brahma ka ansh)
🔥 Durvasa (Shiva ka ansh)
🕉️ Dattatreya (Vishnu ka ansh)

Vidura ne poocha,
"Yeh teenon dev ek hi ghar mein kyun aaye?"

Maitreya bole,

"Atri ne kathor tapasya ki thi."

Ek pair par 100 saal khade rahe.
Sirf hawa par jee rahe the.

Unhone prarthana ki:

"Mujhe aisa putra mile jo Bhagwan jaisa ho."

Unki tapasya se teenon lok jalne lage.

Tab Brahma, Vishnu aur Shiva swayam aaye.

Aur bole,

"Hum hi woh ek tattva hain jise tum dhyaan kar rahe ho."

"Hum apne ansh se tumhe putra denge."

Is tarah teenon ka janm hua.

🔥 Dadhichi aur Bhargu Vansh

Aage kai Rishiyon ka vansh phaila.

Bhargu Rishi ke ghar Lakshmi ji ka janm hua.

Pulastya ke vansh se Kubera hua.

Aur usi vansh se —
Ravana, Kumbhakarna aur Vibhishana bhi hue.

🌸 Daksha ki Betiyan

Daksha ne 16 betiyan paida ki.

13 ko Dharma ko diya.
1 ko Agni ko.
1 ko Pitron ko.
1 ko Shiva ko — Sati.

Dharma ki patniyon se
bahut sundar gun paida hue —

Shraddha se Shubh.
Maitri se Prasad.
Daya se Abhaya.
Shanti se Sukha.

Aur Mūrti se janm liya —

✨ Nara aur Narayana.

Unke janm par poora brahmand khush ho gaya.

Phool barse.
Devta gaane lage.
Nadiyan shaant ho gayi.

Baad mein wahi Nara-Narayana
Krishna aur Arjuna ke roop mein aaye.

😔 Sati ki Kahani

Shiva ki patni Sati thi.

Par jab unke pita Daksha ne Shiva ka apmaan kiya,
toh Sati ne yog bal se apna sharir tyag diya.

Unki kahani dukh bhari thi.

✨ Moral

Tapasya aur bhakti se Bhagwan khud prakat hote hain.
Vansh sirf khoon se nahi, gun aur dharma se badhta hai.

Jo shraddha, daya aur shanti ko apnaye,
uska jeevan pavitra ho jata hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 2
    with st.expander("Chapter 2 - The Rift between the God Śiva and Dakṣa"):
        text1 = """ 
        Chapter 2 — Hinglish Story (Simple Moral Style)
Daksha aur Shiv ji ke beech jhagda

Vidura ne hairani se poocha,

“Daksha apni beti Sati se pyaar karta tha.
Phir usne Shiv ji se nafrat kyun ki?”

“Shiv ji toh sabse shaant, sabse pavitra hain.
Woh kisi se dushmani nahi rakhte.”

“Phir aisa kya hua
ki Sati ko apni jaan deni padi?”

Maitreya Rishi ne dheere se kahani shuru ki."""
        create_image_text_layout(
            "attached_assets/chapter4/4.2.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        🌞 Yagya ka Sabha

Ek baar Prajapatis ka bada yagya ho raha tha.

Sab devta aaye the.
Rishi-muni aaye the.
Agni dev bhi wahan the.

Tabhi Daksha pravesh kiya.

Woh Suraj ki tarah chamak rahe the.

Sab log unke tej se prabhavit ho kar khade ho gaye.

Par do vyakti nahi khade hue —

🕉️ Brahma ji
🕉️ Shiv ji

Brahma ji toh pita the.
Par Shiv ji shant baithe rahe.

🔥 Daksha ka Gussa

Daksha ko bahut bura laga.

Unhone gusse se Shiv ji ko dekha.

Aur sabha mein bolna shuru kiya.

“Yeh Shiv ahankari hai!”

“Isne meri beti se shaadi ki,
par mujhe pranam tak nahi kiya!”

“Yeh shamshan mein rehta hai.
Bhasm lagata hai.
Bhooton ke saath ghoomta hai.”

“Yeh pavitra nahi hai.”

Sab chup ho gaye.

Shiv ji shant baithe rahe.

Ek shabd bhi nahi bola.

⚡ Shraap

Daksha ne paani chhua.
Aur shraap de diya.

“Yagya mein Shiv ko kabhi hissa nahi milega!”

Sab ne mana kiya.
Par Daksha sunne ko tayyar nahi tha.

Woh wahan se chala gaya.

😡 Nandi ka Gussa

Shiv ji ke bhakt Nandi ka khoon khol gaya.

Unhone bhi shraap diya.

“Daksha shareer ko hi sab kuch samajhta hai.”

“Woh janwaron jaisa sochta hai.”

“Uska sir bakri ka ho jayega!”

“Jo Shiv ki ninda karega,
woh janam-maran ke chakkar mein phasega.”

🔄 Bhargu ka Pratikar

Rishi Bhargu ko bhi gussa aa gaya.

Unhone ulta shraap diya.

“Jo Shiv ke bhakt hain,
woh Vedo ka apmaan karenge.”

“Woh alag panth apnayenge.”

Sab jagah shraap aur gussa phail gaya.

🌫️ Shiv ji ki Shaanti

Itne sab ke baad bhi…

Shiv ji ne kuch nahi kaha.

Unka dil thoda dukhi hua.

Par woh shant se wahan se chale gaye.

Yagya poora hua.

Sab apne ghar chale gaye.

Par beej bo diya gaya tha.

Aage chal kar yahi jhagda
badi vinash ka kaaran banega.

✨ Moral

Ahankaar se vinash shuru hota hai.
Shaanti sabse bada bal hai.

Jo apmaan par bhi chup rahe,
wahi sachcha Mahadev hota hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 3
    with st.expander("Chapter 3 - Śiva dissuades Satī from attendance at Dakṣa-Yajña"):
        text1 = """ 
        Chapter 3 — Hinglish Story (Simple Moral Style)
Shiv ji ne Sati ko samjhaya

Maitreya Rishi ne kaha,

Daksha aur Shiv ji ke beech ka jhagda lamba chalta raha.

Samay beet gaya.
Par unki dushmani khatam nahi hui."""
        create_image_text_layout(
            "attached_assets/chapter4/4.3.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        🔥 Daksha ka Yagya

Ek din Daksha ne bahut bada yagya rakh diya.

Sab devtaon ko bulaya.
Sab rishiyon ko bulaya.
Sab ko samman diya.

Par ek vyakti ko nahi bulaya —

🕉️ Shiv ji.

Daksha ka ahankaar badh chuka tha.

🌸 Sati ko Pata Chala

Sati ne dekha —

Aakash mein devta apni patniyon ke saath ja rahe hain.

Sab saj-dhaj kar.
Haste hue.
Khush.

Unhone Shiv ji se kaha,

"Prabhu, mere pita ka yagya ho raha hai."

"Sab ja rahe hain."

"Hum bhi chalein?"

"Meri behne hongi,
meri maa hogi."

"Main unhe dekhna chahti hoon."

Unki aankhon mein bachpan ki yaadein thi.

🕊️ Sati ki Vinati

Sati ne pyaar se kaha,

"Log apne pita ke ghar bina bulaye bhi jaate hain."

"Main aapki ardhangini hoon."

"Kripya mujhe jaane dein."

Woh bahut vinamr thi.
Par mann se utni hi utsuk.

🌫️ Shiv ji ka Shaant Uttar

Shiv ji ne halka sa muskura kar dekha.

Unhone Sati ko yaad dilaya,

"Priye, tum sahi keh rahi ho."

"Par jab kisi ka mann ahankaar se bhara ho,
toh wahan jaana theek nahi."

⚖️ Ahankaar ka Vish

Shiv ji bole,

"Gyaan, dhan, sundarta, uchcha janm —
yeh sab achhe logon mein gun hote hain."

"Par bure logon mein yahi cheezein
ahankaar ban jaati hain."

"Daksha mujhe pasand nahi karta."

"Tum wahan jaogi,
toh shayad tumhe samman na mile."

💔 Shabd ka Ghaav

Shiv ji ne gahri baat kahi:

"Sharir par laga teer ka ghaav
ek din bhar jata hai."

"Par apno ke kadve shabd
dil ko saari zindagi dukh dete hain."

"Us dard mein neend bhi nahi aati."

🌺 Pyaar aur Satya

Shiv ji bole,

"Tum Daksha ki sabse priya beti ho."

"Par meri wajah se
woh tumse bhi naraz ho sakta hai."

"Woh mere tejas se jalan karta hai."

"Jahan dvesh ho,
wahan jaane se sukh nahi milta."

🕉️ Sachchi Shraddha

Shiv ji ne aur kaha,

"Sachche bhakt bahari namaskar nahi dekhte."

"Woh sab mein Bhagwan ko dekhte hain."

"Main sirf Vaasudev ko pranam karta hoon,
jo sabke hriday mein hai."

🚫 Antim Salah

Shiv ji ne dheere se kaha,

"Agar tum meri baat nahi manogi
aur wahan jaogi,
toh tumhe dukh hoga."

"Apno ka apmaan
jeevan se bhi bhari lagta hai."

Sati chup ho gayi.

Unke mann mein prem tha.
Par saath hi chot bhi.

Aage kya hoga…
yeh samay batayega.

✨ Moral

Jahan ahankaar ho, wahan prem toot jata hai.
Kadve shabd talwar se bhi gehra ghaav dete hain.

Samajh aur shaanti, dono zaroori hain."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4
    with st.expander("Chapter 4 - Satī’s Self-immolation by Yoga"):
        text1 = """ 
        Chapter 4 — Hinglish Story (Simple Moral Style)
Sati ka Yog se Agni-pravesh

Maitreya Rishi ne dheere se kaha,

Shiv ji ne Sati ko mana kiya tha.
Unhe pata tha —
kuch bura hone wala hai.

Par Sati ka mann dukhi tha.

Woh kabhi bahar jaane ko kadam badhati,
kabhi dar kar ruk jaati.

Jaise dil do hisso mein bant gaya ho."""
        create_image_text_layout(
            "attached_assets/chapter4/4.4.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        😢 Dil ka Dard

Sati apne maayke ko yaad kar rahi thi.

Unki aankhon mein aansu aa gaye.

Woh ro padi.

Unke mann mein pyaar bhi tha,
aur gussa bhi.

Aakhir woh nikal padi.

Shiv ji ko chhod kar.

🐂 Nandi aur Ganon ka Saath

Shiv ji ke gan unke peeche chale.

Nandi ne unhe apne bail par bithaya.

Chhatra, chamara, dhol, shankh —
sab saath le gaye.

Par Sati ka mann bhaari tha.

🔥 Yagya Sthal par Apmaan

Yagya sthal par ved-mantra gunj rahe the.

Sab rishi aur devta wahan the.

Par jab Sati pahunchi…

Kisi ne swagat nahi kiya.

Sirf unki maa aur behne gale lag kar ro padi.

Daksha ne nazar tak nahi uthayi.

Sati ne dekha —

Yagya mein Shiv ji ka hissa hi nahi rakha gaya.

Unka apmaan khule aam ho raha tha.

⚡ Sati ka Krodh

Sati ka chehra tej se chamak utha.

Jaise poori duniya ko jala degi.

Unhone sabha mein zor se kaha:

"Jo sabka mitra hai,
tum usse dushmani rakhte ho?"

"Shiv kisi se dvesh nahi karte."

"Unka naam tak paap mita deta hai."

"Tum unki ninda karte ho!"

🌺 Mahaan ka Apmaan

Sati boli,

"Bure log hamesha achhon mein bhi dosh dhoondte hain."

"Par sachche log,
chhoti si achchai ko bhi bada bana dete hain."

"Main tumhari beti ho kar sharminda hoon."

💔 Antim Faisla

Sati ki awaaz kaamp rahi thi.

Unhone kaha,

"Yeh shareer tumse mila hai."

"Par main ise nahi rakhoongi."

"Jaise ashuddh bhojan ko bahar nikal dete hain,
waise hi main is shareer ko chhod dungi."

Sab sann ho gaye.

🧘‍♀️ Yog ka Agni

Sati zameen par baith gayi.

Uttar ki taraf mukh kiya.

Aankhen band ki.

Pran ko niyantrit kiya.

Mann ko Shiv ji ke charanon mein laga diya.

Unka sharir dheere-dheere
yog ki agni se jalne laga.

Kisi ne chhua nahi.

Koi aag bahar se nahi thi.

Sab unki tapasya ki agni thi.

😭 Sabka Shok

Aakash mein cheekh uthi —

"Haay! Haay!"

Sab ro padi.

"Apne pita ke apmaan se Sati ne pran de diye!"

Shiv ji ke gan krodhit ho gaye.

Woh Daksha par toot pade.

Par Rishi Bhrigu ne yagya ki raksha ke liye mantra bal se devtaon ko bulaya.

Shiv ji ke gan haar kar wapas chale gaye.

Yagya sthal dukh se bhar gaya.

✨ Moral

Ahankaar aur apmaan ka parinaam vinash hota hai.
Sachcha prem apmaan seh nahi pata.

Par gussa aur dukh milkar kabhi-kabhi sab kuch jala dete hain."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 5
    with st.expander("Chapter 5 - Destruction of Dakṣa’s Sacrifice"):
        text1 = """ 
        Chapter 5 — Hinglish Story (Simple Moral Style)
Daksha ke Yagya ka Vinash

Maitreya Rishi ne kaha,

Jab Shiv ji ko pata chala
ki Sati ne apmaan ke dukh mein
apna shareer chhod diya…

Aur unke gan bhi hara diye gaye…

Tab Shiv ji ka gussa
aasmaan ko chhoo gaya."""
        create_image_text_layout(
            "attached_assets/chapter4/4.5.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        ⚡ Shiv ka Krodh

Shiv ji ne apne honth daba liye.

Unhone apni jata ka ek bada guchha
zor se tod kar zameen par patka.

Woh bijli ki tarah chamka.

Aag ki tarah jal utha.

Dharti hil gayi.

🔥 Veerabhadra ka Janm

Us jata se ek bhayanak roop nikla.

Woh tha — Veerabhadra.

Bahut bada.

Aasmaan ko chhoota hua.

Hazaar baahen.

Teen aankhen.

Daant tez.

Gale mein khopdiyon ki mala.

Haath mein talwaar, trishul,
aur kai bhayankar hathiyaar.

🗡 Shiv ka Aadesh

Shiv ji bole,

"Veerabhadra,
tum mere hi roop ho."

"Jaao.
Daksha aur uske yagya ko nasht kar do."

Veerabhadra ne pranam kiya.

Aur garajte hue chal pada.

Unke saath hazaaron gan the.

🌪 Yagya mein Ashubh Sanket

Daksha ke yagya sthal par
achanak dhool ka bada baadal utha.

Sab log ghabra gaye.

"Yeh kya ho raha hai?"

"Kya pralay aane wala hai?"

Aasmaan mein ajeeb sanket dikhne lage.

Daksha ki patni Prasuti boli,

"Yeh sab Daksha ke paap ka phal hai."

"Usne Sati ka apmaan kiya."

💥 Aakraman

Achanak Veerabhadra aur gan
yagya sthal mein ghus aaye.

Unhone sab tod diya.

Yagya ka mandap toot gaya.

Bartans toot gaye.

Agni bujha di gayi.

Kuch log bhaag gaye.

Kuch chillaane lage.

Sab jagah afra-tafri mach gayi.

😡 Saza

Veerabhadra ne Bhrigu rishi ki daadhi pakad kar
noch di.

Bhaga ki aankhen nikaal di.

Pusha ke daant tod diye.

Sabko unke apmaan ka phal mila.

⚔ Daksha ka Ant

Phir Veerabhadra ne Daksha ko pakda.

Use zameen par gira diya.

Uska sir kaatne ki koshish ki…

Par talwaar kaam nahi kar rahi thi.

Tab Veerabhadra ne
yagya mein jaanwar ko maarne ka tareeka yaad kiya.

Usi vidhi se
Daksha ka sir kaat diya.

Sab sann ho gaye.

Veerabhadra ne
Daksha ka sir yagya ki agni mein daal diya.

🔥 Ant mein

Yagya jal kar khak ho gaya.

Sab kuch nasht ho gaya.

Veerabhadra aur Shiv ke gan
Kailash laut gaye.

✨ Moral

Ahankaar ka ant hamesha vinash hota hai.
Jo bhakt aur sachchai ka apmaan karta hai,
use apne karm ka phal zaroor milta hai.

Shanti ko todoge,
to prakriti swayam nyaay karegi."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6
    with st.expander("Chapter 6 - Appeasement of Rudra—Revival of Dakṣa"):
        text1 = """ 
        Chapter 6 — Hinglish Story (Simple Moral Style)
Rudra ko Shaant Karna aur Daksha ka Jeevan Lautna

Maitreya Rishi bole,

Yagya toot chuka tha.
Devta haar gaye the.
Unke sharir ghaayal the.

Dar ke maare sab
Brahma ji ke paas gaye.

Unhone haath jod kar
saari kahani sunayi."""
        create_image_text_layout(
            "attached_assets/chapter4/4.6.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        🕊 Brahma ka Updesh

Brahma ji ne shaant swar mein kaha,

"Jo tumse zyada shaktishaali ho,
usse badla lena kabhi achha nahi hota."

"Tumne Shiv ji ko yagya mein hissa nahi diya.
Yahi tumhari galti thi."

"Ab vinamrata se unke paas jao.
Unse maafi maango."

"Woh jaldi prasann ho jaate hain."

Sab devta sharminda ho gaye.

🏔 Kailash ki Yatra

Brahma ji sabko lekar
Kailash parvat gaye.

4

Kailash sundar tha.

Nadiyan beh rahi thi.
Pushp khil rahe the.
Pakshi madhur gaana gaa rahe the.

Hawa sugandhit thi.

Sab jagah shanti thi.

🌳 Bargad ke Neeche

Ek bade bargad ke ped ke neeche
Shiv ji baith kar dhyaan laga rahe the.

Unka chehra shaant tha.

Mastak par chandrama.
Sharir par bhasm.
Jata baandhi hui.

Woh Narad ji ko
Brahman ka gyaan samjha rahe the.

🙏 Brahma ka Namra Prarthana

Brahma ji ne jhuk kar pranam kiya.

Shiv ji ne bhi vinamrata se unka swagat kiya.

Brahma ji bole,

"Prabhu,
aap hi sabke karta-dharta ho."

"Yagya ki vyavastha bhi aapne hi banayi."

"Daksha ne galti ki."

"Par daya karna bhi aapka hi gun hai."

"Kripya yagya ko phir se shuru hone dein."

"Daksha ko jeevan de dein."

"Bhaga ki aankhen laut aayein.
Bhrigu ki daadhi wapas ho.
Pusha ke daant laut aayein."

"Jo yagya mein hissa bachega,
woh sab aapka hoga."

Sab ne haath jod kar
Shiv ji ki taraf dekha.

🌸 Shiv ki Kripa

Shiv ji ka hriday
krodh se zyada daya se bhara tha.

Woh shaant ho gaye.

Unhone sabko maaf kar diya.

Daksha ko jeevan mila.
Par uska sir nahi tha.

Isliye uske shareer par
ek bakri ka sir laga diya gaya.

Daksha ne sharm se jhuk kar
Shiv ji ko pranam kiya.

Yagya phir se shuru hua.

Aur is baar
Shiv ji ka hissa pehle diya gaya.

✨ Moral

Ahankaar todta hai.
Vinamrata jodti hai.

Galti ho jaaye,
to maafi maang lena hi sabse bada bal hai.

Shiv jaise mahan log,
badle se nahi —
daya se jeet te hain."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7
    with st.expander("Chapter 7 - Completion of Dakṣa’s Sacrifice"):
        text1 = """ 
        Chapter 7 — Hinglish Story (Simple Moral Style)
Daksha ke Yagya ka Poora Hona

Maitreya Rishi bole,

Jab sab devta aur Brahma ji
Shiv ji ko mana kar le aaye…

Tab Shiv ji muskura diye.

Unka gussa shaant ho chuka tha."""
        create_image_text_layout(
            "attached_assets/chapter4/4.7.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        🐐 Daksha ka Naya Sir

Shiv ji bole,

"Daksha ka jala hua sir wapas nahi aa sakta."

"Isliye uske sharir par
ek bakre ka sir laga diya jaaye."

"Bhaga dusre devta ki aankhon se dekhega."

"Pusha daant ke bina aata khaayega."

"Bhrigu ki daadhi bhi bakre jaisi hogi."

Sab ne kaha —
"Waah! Waah!"

🌸 Daksha ka Jeevan Lautna
4

Jab bakre ka sir joda gaya…

Shiv ji ne kripa bhari nazar daali.

Daksha jaise neend se jaag gaya.

Usne saamne Shiv ji ko dekha.

Uska mann badal chuka tha.

Jaise sharad ritu mein paani saaf ho jaata hai.

😢 Pachtava

Daksha kuch bol nahi pa raha tha.

Use apni beti Sati yaad aa gayi.

Uski aankhen bhar aayi.

Phir haath jod kar bola:

"Prabhu,
maine aapka apmaan kiya."

"Par aapne mujhe saza dekar bhi bachaya."

"Aap aur Hari alag nahi ho."

"Aap mahan ho."

Shiv ji ne use maaf kar diya.

🔥 Vishnu ka Aagman

Yagya dobara shuru hua.

Is baar poore shraddha se.

Tab aakash se prakash chha gaya.

Bhagwan Vishnu Garud par aaye.

Neel varna sharir.
Haath mein shankh, chakra, gada, padma.

Lakshmi ji unke vaksh par virajmaan.

Sab devta khade ho gaye.

Haath jod liye.

🙏 Sabki Stuti

Brahma, Indra, Shiv —
sab ne unki stuti ki.

Daksha ne bhi kaha:

"Aap hi yagya ho."

"Aap hi havan samagri ho."

"Aap hi agni ho."

"Sab kuch aap hi ho."

Vishnu bole,

"Main hi Brahma hoon."

"Main hi Shiv hoon."

"Jo teenon mein bhed dekhta hai,
woh sach nahi samajhta."

"Jo sab mein ekta dekhta hai,
use hi shanti milti hai."

🌼 Yagya Sampann

Daksha ne pehle Vishnu ko hissa diya.

Phir Shiv ji ko.

Phir sab devtaon ko.

Yagya shanti se poora hua.

Sab ne pavitra snaan kiya.

Devta apne lok wapas chale gaye.

🌺 Sati ka Naya Janm

Maitreya bole,

Sati ne apna purana shareer chhod diya tha.

Par woh phir janmi.

Is baar Himavan ki beti — Parvati ke roop mein.

Phir se Shiv ji ko hi apna pati banaya.

Prem kabhi marta nahi.

👶 Kartikeya ka Janm

Baad mein Shiv ji ka tej
Ganga ne dharan kiya.

Usse ek balak janma.

Chhe mukh wala.

Isliye naam pada — Shanmukh.

Wahi Kartikeya bana.

Devtaon ka senapati.

✨ Moral

Ahankaar todta hai.
Daya jodti hai.

Jo teen roop mein ek ko dekhe,
vah sachcha gyaani hai.

Prem aur satya,
hamesha jeet te hain."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 8
    with st.expander("Chapter 8 - Story of Dhruva"):
        text1 = """ 
        Chapter 8 — Dhruva ki Kahani (Hinglish Story Style)
Ek Chhote Rajkumar ki Badi Tapasya

Maitreya Rishi bole,

Raja Uttanapad ki do patniyan thi —
Suniti aur Suruchi.

Suruchi raja ki pasandida thi.
Suniti ko zyada pyaar nahi milta tha.

Suniti ka beta tha — Dhruva."""
        create_image_text_layout(
            "attached_assets/chapter4/4.8.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        👑 Ek Din Ka Apmaan

Ek din raja Suruchi ke bete Uttam ko
godi mein bithakar pyaar kar rahe the.

Chhota Dhruva bhi daud kar aaya.

Woh bhi papa ki godi mein baithna chahta tha.

Par raja ne use roka nahi…
bas chup rahe.

Tab Suruchi ne teekhe shabd bole:

"Yeh singhasan ya godi tumhare liye nahi hai."

"Tum mere garbh se paida nahi hue."

"Agar rajgaddi chahiye,
to Bhagwan ki tapasya karo."

"Phir mere garbh se janm lena."

Yeh shabd teer ki tarah lage.

😢 Maa ka Updesh

Dhruva rota hua apni maa Suniti ke paas gaya.

Suniti ne use gale laga liya.

Woh khud bhi ro padi.

Par unhone shant hokar kaha:

"Beta, doosron ko dosh mat do."

"Jo milta hai, woh karmon ka phal hota hai."

"Agar sabse ooncha sthaan chahiye,
to Bhagwan Vishnu ki sharan jao."

"Unke charan sabse bade hain."

"Unhe paakar hi sab kuch milta hai."

Dhruva ke mann mein aag jal uthi.

Par ab woh gusse ki nahi,
sankalp ki aag thi.

🌲 Van ki Ore

Sirf 5 saal ka bachcha.

Par hausla pahaad jaisa.

Dhruva mahal chhod kar
van ki taraf chal pada.

Raaste mein Rishi Narad mile.

🎶 Narad ka Pariksha

Narad ji bole,

"Beta, tum abhi chhote ho."

"Yeh sab bhool jao."

"Samay aane par tapasya karna."

Par Dhruva ne kaha,

"Mera dil toot gaya hai."

"Mujhe sabse ooncha sthaan chahiye."

"Jo kisi ne na paaya ho."

Narad ji muskura diye.

Unhone samajh liya —
yeh bachcha aam nahi hai.

🕉 Mantra ka Vardan

Narad ji bole,

"Yamuna ke kinare Madhuvan jao."

"Snan karo."

"Dhyaan lagao."

Aur mantra diya:

“Om Namo Bhagavate Vasudevaya.”

"Is mantra ka jap karo."

"Bhagwan ka roop man mein dekho."

🌟 Bhagwan ka Roop
4

Narad ji ne bataya:

"Bhagwan neele megh jaise hain."

"Char bhujaen."

"Haath mein shankh, chakra, gada, padma."

"Peetambar pehne hue."

"Unke mukh par komal muskaan."

"Unke charan kamal jaise sundar."

🧘 Dhruva ki Kathor Tapasya

Dhruva Madhuvan pahunch gaya.

Pehle mahine —
har teesre din phal khaya.

Doosre mahine —
har chhatthe din sukhi ghaas.

Teesre mahine —
sirf paani.

Chauthe mahine —
sirf hawa.

Paanchve mahine —
ek pair par khade hokar
saans bhi rok li.

Dhyaan itna gahra tha
ki teenon lok hilne lage.

Devta ghabra gaye.

Unki saans rukne lagi.

Woh Bhagwan Vishnu ke paas gaye.

🙏 Devtaon ki Pukar

Devta bole,

"Prabhu, humein bachaiye!"

"Kisi ki tapasya se
hamari saans ruk gayi hai!"

Bhagwan bole,

"Darro mat."

"Woh Raja Uttanapad ka beta Dhruva hai."

"Usne apne mann ko mujh mein laga diya hai."

"Main uski tapasya todne ja raha hoon."

✨ Moral

Apmaan se tootna nahi chahiye.
Usse sankalp banana chahiye.

Umar chhoti ho sakti hai,
par irade bade hone chahiye.

Jo Bhagwan par sachche mann se tik jaye,
uska naam Dhruv tara ki tarah amar ho jaata hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 9
    with st.expander("Chapter 9 - Viṣṇu’s boon and Dhruva’s Coronation"):
        text1 = """ 
        Chapter 9 — Vishnu ka Vardan aur Dhruva ka Rajyabhishek
Chhote Balak ka Amar Sthaan

Maitreya Rishi bole,

Jab Devta shaant ho gaye,
tab Bhagwan Vishnu khud
Garud par baith kar
Madhuvan aaye.

Woh apne bhakt ko dekhna chahte the."""
        create_image_text_layout(
            "attached_assets/chapter4/4.9.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Dhruva apne hriday mein
Bhagwan ka roop dekh raha tha.

Achanak woh roop
andar se gayab ho gaya.

Usne aankhen kholi…

Bhagwan samne khade the.

Neel megh jaisa sharir.
Char bhujaen.
Haath mein shankh, chakra, gada, padma.

Dhruva ka dil bhar aaya.

Woh zameen par dandvat gir gaya.

Jaise lakdi seedhi girti hai.

Uski aankhen Bhagwan ko pee rahi thi.

Par woh bol nahi pa raha tha.

Tab Bhagwan ne
apne shankh se
uske gaal ko sparsh kiya.

Aur turant…

Dhruva ko divya vaani mil gayi.

🙏 Dhruva ki Stuti

Dhruva bola,

"Prabhu,
aap hi sabke andar virajmaan ho."

"Aap hi meri vaani ko shakti dete ho."

"Aap hi sab kuch ho."

"Aap ek ho,
par sab mein dikhte ho."

"Mujhe aapke bhakton ka sang chahiye."

"Unke saath rehkar
main sansar sagar paar karna chahta hoon."

Par uske mann mein
abhi bhi ek chhoti si ichchha thi.

Sabse ooncha sthaan paane ki.

🎁 Vishnu ka Vardan

Bhagwan muskura kar bole,

"Dhruva,
mujhe pata hai tum kya chahte ho."

"Main tumhe ek aisa sthaan deta hoon
jo kisi ko nahi mila."

"Sab grah, tare, rashi
tumhare chaaron taraf ghoomenge."

"Woh sthaan kabhi naash nahi hoga."

Wahi sthaan bana — Dhruv Tara.

Aakash ka sabse sthir tara.

👑 Rajya ka Samay

Bhagwan ne kaha,

"Tum 36,000 saal tak
dharti par raj karoge."

"Nyay aur dharma se raj karna."

"Phir mere paas aaoge."

Bhagwan wapas chale gaye.

Dhruva kuch sochne laga.

😔 Dhruva ka Pachtava

Usne socha,

"Maine kya maanga?"

"Bhagwan ne to Moksha dena chaha."

"Par maine sirf raj aur pad maanga."

"Jaise koi gareeb
raja se sirf anaaj maange."

Uska dil halka ho gaya.

Ab usme gussa nahi tha.

🏰 Ghar Wapsi

Raja Uttanapad ko
jab pata chala Dhruva aa raha hai…

Unhe vishwas nahi hua.

Par jab sach jaana,
woh khushi se ro pade.

👨‍👦 Pita ka Gale Lagana
4

Raja ne rath se utar kar
Dhruva ko gale laga liya.

Aankhon se aansu behne lage.

Unhone uske sir ko baar-baar chuma.

Maa Suniti ne use gale lagaya.

Khushi ke aansuon se
unke stanon se doodh bahne laga.

Suruchi bhi pighal gayi.

Usne kaha,
"Beta, dirghayu ho."

Sab nagar saj gaya.

Galiyon mein phool,
deepak,
sandal jal,
mangal geet.

👑 Rajyabhishek

Jab Dhruva bada hua,
Raja ne use rajgaddi de di.

Khud van ko chale gaye.

Dhruva ne dharma se raj kiya.

Aur baad mein
Dhruv Tara ban kar
aakash mein amar ho gaya.

✨ Moral

Apmaan se shuru hua safar
Amarata par khatam hua.

Bhagwan sachche bhakt ko
uski ichchha bhi dete hain,
aur usse seekh bhi dete hain.

Jo mann ko Bhagwan mein sthir kare,
wahi Dhruv ban jaata hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 10
    with st.expander("Chapter 10 - Dhruva invades Alakā"):
        text1 = """ 
        Chapter 10 — Dhruva ka Alakā par Hamla
Gusse ki Aag aur Maya ka Andhera

Maitreya Rishi bole,

Dhruva ne vivah kiya.

Uski do patniyan thi.

Uske ghar mein sab theek chal raha tha.

Par ek din…
buri khabar aayi."""
        create_image_text_layout(
            "attached_assets/chapter4/4.10.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        ⚔️ Bhai ki Mrityu

Dhruva ka bhai Uttam
Himalaya mein shikar karne gaya tha.

Wahan ek shaktishaali Yaksha ne
use maar diya.

Uski maa Suruchi
dukh se jal kar
uske peeche chal basi.

Yeh sunte hi
Dhruva ka hriday gusse se bhar gaya.

Aankhon mein aansu bhi the.

Par andar badle ki aag jal uthi.

🏔️ Alakā ki Ore Yudh
4

Dhruva ne apna vijayi rath chadh liya.

Woh uttar disha mein
Himalaya ki ghaatiyon ki taraf badha.

Wahan thi Yakshon ki rajdhani — Alakā.

Shehar pahaadon ke beech tha.

Rudra ke gan wahan ghoomte the.

Dhruva ne apna shankh bajaya.

Aakash goonj utha.

Yaksha sainik bhadak gaye.

🏹 Teer ki Barish

Yaksha talwar, bhala, gada lekar
bahar nikle.

Dhruva ne ek saath
har yoddha par teen teer chala diye.

Unke maathe par teer lage.

Sab chauk gaye.

Yakshon ne bhi
chhe-chhe teer chala diye.

Phir ek lakh se zyada Yaksha
ek saath toot pade.

Lohe ke hathiyaar,
bhale, talwarein,
pathar,
sab Dhruva par barsne lage.

Kuch pal ke liye
Dhruva dikhai hi nahi diya.

Jaise pahaad
baarish mein chhup jaata hai.

Devta chillaye,

"Haaye! Dhruva doob gaya!"

Par tabhi…

🌞 Sooraj ki Tarah Wapas

Dhruva ka rath
badalon ke peeche se nikle suraj jaisa
phir chamka.

Usne apne dhanush ki taar khinchi.

Aawaz se hi dushman ka dil kaanp gaya.

Uske teer
vajra ki tarah
kavach cheer gaye.

Ranbhoomi mein
sir, bhujayein, mukut, gehne
bikhre pade the.

Bache huye Yaksha
bhag gaye.

🧙 Yakshon ki Maya

Dhruva ne shehar mein ghusne se mana kiya.

Usne kaha,

"Ye log jadugar hain.
Inki maya samajhna mushkil hai."

Tabhi achanak…

Aakash kaala ho gaya.

Bijli chamki.

Garajna hone lagi.

Khoon, maans, ganda paani
aasman se barasne laga.

Bina sir ke shareer
girne lage.

Aakash mein pahaad dikha.

Har taraf se pathar, gada, talwar barasne lage.

Aag ugalte saap
uski taraf badhe.

Hathi, sher, bagh
ek saath toot pade.

Samundar jaisa
bhayanak shor hua.

Yeh sab tha
Yakshon ki kala jadoo ki maya.

🙏 Rishiyon ki Pukar

Yeh dekh kar rishi ghabra gaye.

Unhone prarthana ki:

"Hey Dhruva!"

"Bhagwan Vishnu ka naam lo!"

"Unka sharan lo!"

"Unka astra hi
is maya ko tod sakta hai!"

✨ Moral

Gussa andha kar deta hai.

Badla kabhi kabhi insaan ko
dharma se door le jaata hai.

Shakti ke saath vivek bhi zaroori hai.

Jab andhera chha jaye,
tab Bhagwan ka naam hi roshni deta hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 11
    with st.expander("Chapter 11 - Svāyambhuva Manu Dissuades Dhruva from Fighting"):
        text1 = """ 
        Chapter 11 — Svāyambhuva Manu Dissuades Dhruva from Fighting
⚔️ Dhruva’s Fierce Counterattack

Maitreya said:

Sages ki baat sun kar Dhruva ne ācamana kiya aur apne dhanush par Nārāyaṇa-astra chadha diya.

Jaise gyaan ke prakaash se andhkaar mit jata hai, waise hi Yakṣon ki māyā turant samaapt ho gayi.

Sone ke nok wale teer bijli ki tarah nikle.
Yakṣa sena cheer di gayi.
Ve krodh se bhare hue Dhruva par toot pade —
jaise saanp Garuḍa par hamla karte hain."""
        create_image_text_layout(
            "attached_assets/chapter4/4.11.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Lekin Dhruva ne unke:

Baahu

Jaangh

Gardan

Udhar

sab kaat daale.

Anak innocent Yakṣa mare gaye.

👴 Svāyambhuva Manu ka Pravesh

Tab Dhruva ke pitamah, Svāyambhuva Manu,
daya se pighal kar rishiyon ke saath aaye.

Unhone Dhruva ko roka.

🗣️ Manu ka Upadesh

Manu bole:

"Hey putra, bas karo."

"Yeh krodh paap ka dwar hai."

"Ek Yakṣa ke dosh mein tumne anek nirdoshon ko maar diya."

"Yeh hamare vansh ke layak nahi."

Unhone samjhaya:

Deh ko ātman samajhna bhranti hai

Janm aur mrityu daiva (destiny) se hote hain

Bhagavan sab mein samaan roop se virajmaan hain

Krodh moksha ka sabse bada shatru hai

🕊️ Darshan ka Tatva Gyaan

Manu ne aur gahra tattva samjhaya:

Srishti, sthiti, laya sab Bhagavan ki Māyā se hota hai

Paramātma nirguṇa hote hue bhi sab ka kāraṇ hai

Samay (Kāla), Karma, Prakriti — sab usi ki shaktiyan hain

Bhagavan na kisi ke apne hain, na shatru

Jaise hawa ke peeche dhool chalti hai,
waise hi sab jeev uski ichchha se chal rahe hain.

💭 Dhruva ko Yaad Dilaya

Manu bole:

"Tum wahi ho jo paanch saal ki umar mein van gaye the."

"Tumne Bhagavan ko prasann kiya."

"Tumhe Viṣṇu ka param pad mila."

"Phir tum kaise krodh mein aakar dharm bhool gaye?"

🧘 Sādhana ka Marg

Manu ne antim upadesh diya:

Kṣamā (forgiveness)

Dayā (compassion)

Maitrī (friendliness)

Samatā (equanimity)

Inse Bhagavan prasann hote hain.

"Apne krodh ko aushadhi ki tarah niyantrit karo."

"Kubera ko prasann karo, kyunki tumne uske sevakon ko maara hai."

Dhruva ne shraddha se pranam kiya.

Manu wapas chale gaye.

✨ Moral

Krodh sabse bada shatru hai.

Ek vyakti ke dosh ke liye samuhik dand adharma hai.

Jo bhagavat-bhakta hai, use sab mein Bhagavan dekhna chahiye.

Shakti se bada hai — kṣamā.

Sahi veer wahi hai jo apne krodh ko jeet le."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 12
    with st.expander("Chapter 12 - Kubera’s Boon and Dhruva’s Attainment of Viṣṇu’s Realm"):
        text1 = """ 
        Chapter 12 — Kubera ka Vardan aur Dhruva ka Viṣṇu Lok Prapti
💎 Kubera ka Aagman

Maitreya bole:

Jab Dhruva ne krodh chhod diya,
tab dhan ke devata Kubera wahan aaye."""
        create_image_text_layout(
            "attached_assets/chapter4/4.12.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Dhruva ne vinamrata se haath jod diye.

Kubera bole:

"Hey pavitra kshatriya putra,
tumne dushmani chhod di.
Main tumse bahut prasann hoon."

Unhone kaha:

Na tumne Yakṣon ko maara.

Na unhone tumhare bhai ko maara.

Sab kuch Kaal (Time) karta hai.

"I" aur "You" ka bhav
sirf sharir se judne ki bhranti hai.
Isi se dukh paida hota hai.

🌿 Sabse Bada Vardan

Kubera bole:

"Tum Viṣṇu ke bahut priya ho.
Mujhse koi bhi vardan maango."

Dhruva ne dhan, rajya, ya shakti nahi maangi.

Unhone kaha:

"Mujhe Hari ka sadaiv smaran mile."

Bas.

Kubera muskuraaye.
Unhone vardan diya.
Aur antardhaan ho gaye.

👑 Dhruva ka Rajya

Dhruva ne:

Yajña kiye

Daan diye

Praja ki raksha ki

Sabko apne bachchon ki tarah maana

36,000 saal tak dharm se rajya kiya.

Phir ek din unhe samajh aaya:

"Yeh sab maya hai.
Sharir, dhan, rajya — sab nashvar hai."

Unhone rajya apne putra ko de diya.
Aur Badarikāśram chale gaye.

🧘 Tapasya aur Bhakti

Dhruva ne:

Snan kiya

Yog kiya

Pranayama kiya

Man ko ekagr kiya

Unka hriday bhakti se pighal gaya.
Aankhon se prem ke aansu behne lage.
Sharir ka bhaav bhi bhool gaye.

🚀 Divya Viman

Ek din unhone dekha:

Aakash se ek tejomay viman utar raha hai.
Jaise poornima ka chand.

Usmein do divya purush the:

Chaar bhuja

Shyam varna

Mukut aur abhushan se alankrit

Ve the Sunanda aur Nanda,
Bhagavan ke do sevak.

Unhone kaha:

"Hey Dhruva,
aapne paanch saal ki umar mein Bhagavan ko prasann kiya.
Aapko Viṣṇu lok prapt hua hai.
Chaliye."

🌸 Maa ka Prem

Dhruva viman mein baithne lage.

Tab unhe maa Sunīti yaad aayi.

"Main maa ko chhod kar kaise jaaun?"

Bhagavan ke sevakon ne dikhaya —
Unki maa pehle se hi ek aur divya viman mein ja rahi thi.

Dhruva ka hriday khushi se bhar gaya.

🌟 Mrityu par Vijay

Jab Dhruva viman mein chadhe,
Mrityu dev saamne aaye.

Dhruva ne unke sir par pair rakha.
Aur upar chadh gaye.

Iska arth tha:

Bhakta mrityu se bhi upar hota hai.

✨ Dhruva Lok

Dhruva teenon lok paar karke
Saptarshi mandal ke upar gaye.

Wahan ek amar sthaan mila.

Aaj bhi:

Surya

Chandra

Grah

Taare

sab Dhruva ke charo taraf ghoomte hain.

Wahi hai Dhruva Tara.

🎶 Nārada ka Geet

Rishi Nārada ne kaha:

"Jo sadhak saalon mein nahi paa sakte,
woh Dhruva ne bachpan mein paa liya."

"Sirf ek cheez se —
Nishkapat Bhakti."

🌼 Moral

Sahi bhakta dhan nahi maangta, Bhagavan ka smaran maangta hai.

Krodh chhodne se hi kripa milti hai.

Jo sab mein Bhagavan dekhta hai, woh mrityu se pare chala jata hai.

Sachchi bhakti se asambhav bhi sambhav ho jata hai.

✨ Dhruva ki kahani humein sikhati hai —
Umar chhoti ho sakti hai,
par bhakti badi honi chahiye."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 13
    with st.expander("Chapter 13 - Dhruva’s descendants: King Aṅga’s Abdication"):
        text1 = """ 
        Chapter 13 — Dhruva ke Vanshaj aur Raja Aṅga ka Vanaprasth
🌿 Dhruva ke Baad

Sūta ne bataya:

Jab Dhruva Vaikuṇṭh chale gaye,
Vidura aur bhi utsuk ho gaye.

Unhone pucha:
“Dhruva ke vansh mein kya hua?”"""
        create_image_text_layout(
            "attached_assets/chapter4/4.13.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        👑 Utkala ka Tyag

Dhruva ka bada beta Utkala tha.

Lekin usne rajgaddi lene se mana kar diya.

Woh bachpan se hi:

Shaant

Asakta (detached)

Samdrishti wala

Usne sab mein apne aap ko dekha.
Aur apne andar poori duniya ko.

Log use pagal samajhte the.
Par woh andar se brahma-gyani tha.

Isliye uske chhote bhai Vatsara ko raja bana diya gaya.

🌳 Vansh ka Vistar

Vatsara ke vansh mein kai raja aaye.
Unhi mein se ek the Aṅga.

Aṅga dharmik aur dayalu raja the.
Praja unse bahut prem karti thi.

😢 Vena ka Janm

Raja Aṅga ne yajña kiya.
Unhe putra chahiye tha.

Bhagavan ki kripa se unhe ek beta mila — Vena.

Par bachpan se hi Vena:

Nirdai

Kathor

Ahankari

Woh jungle mein nirdosh jaanwaron ko marta.
Bachchon ko satata.

Log use dekh kar darte the.

💔 Raja Aṅga ka Dukh

Raja ne use samjhaya.
Dand diya.
Par Vena nahi badla.

Raja ka hriday toot gaya.

Unhone socha:

“Nirputra rehna shayad behtar tha.”
“Bura beta ghar ko narak bana deta hai.”

Unki raaton ki neend chali gayi.

🌌 Chupchaap Vidai

Ek raat,
sab so rahe the.

Raja Aṅga chupchaap mahal chhod kar chale gaye.

Na kisi ko jagaya.
Na kisi ko bataya.

Woh van mein chale gaye.

😭 Praja ka Shok

Subah jab logon ko pata chala,
sab ro pade.

Mantri, purohit, praja —
sabne har jagah khoja.

Par Raja Aṅga nahi mile.

Rajya bina raja ke reh gaya.

🌼 Moral

Gyani hamesha shant dikhta hai, par andar se gehra hota hai.

Bura sang aur galat pravritti ghar ko dukhi kar deti hai.

Putra ya sampatti se bada hai — dharma aur shanti.

Raja bhi dukhi ho sakta hai.

Ghar tabhi sukhmay hai jab sanskaar sahi ho.

✨ Kahani humein sikhati hai —
Sampatti aur vansh se bada hai charitra."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 14
    with st.expander("Chapter 14 - The Story of Vena: Pṛthu’s Birth"):
        text1 = """ 
        Chapter 14 — Vena ki Kahani aur Pṛthu ka Janm
👑 Vena ko Raja Banaya Gaya

Maitreya bole:

Raja Aṅga ke chale jaane ke baad,
desh mein anarchy phail gayi.

Rishiyon ne socha:

“Raja ke bina praja pashu jaise ho jaati hai.”

Isliye unhone Vena ko raja bana diya,
chahe log aur mantri khush na the.

Shuru mein chor darr gaye.
Jaise saanp ko dekh kar chuhe chup jaate hain."""
        create_image_text_layout(
            "attached_assets/chapter4/4.14.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        😡 Vena ka Ahankaar

Gaddi milte hi Vena ghamandi ho gaya.

Woh bola:

“Koi yajña nahi hoga.”
“Koi daan nahi hoga.”
“Koi devata ki pooja nahi hogi.”

Woh kehta tha:

“Main hi sab devata hoon.”
“Mujhe hi poojo.”
“Aur kisi ko nahi.”

Uska hriday kathor ho chuka tha.

🧘 Rishiyon ka Samjhana

Rishi shanti se uske paas gaye.

Unhone kaha:

“Dharma se hi rajya tikta hai.”
“Praja ki raksha raja ka kartavya hai.”
“Yajña aur pooja rokna adharm hai.”

Par Vena hans pada.

“Tum murkh ho.”
“Main hi sab kuch hoon.”

Usne Viṣṇu ki ninda ki.

⚡ Rishiyon ka Krodh

Rishi bole:

“Yeh raja adharmi hai.”
“Agar yeh jiyega, duniya barbaad karega.”

Unhone “Hum” ki dhvani ki.

Unke tapasya ke tej se
Vena wahin gir kar mar gaya.

🌪️ Fir se Anarchy

Par raja ke bina desh phir ashant ho gaya.

Chor lutne lage.
Log dara-dara ghoomne lage.

Rishi sochne lage:

“Raja bina praja surakshit nahi reh sakti.”

🌑 Jangha ka Manthan

Unhone Vena ke shareer ko manthit kiya.

Sabse pehle uski jangha (thigh) se
ek chhota, kaala purush nikla.

Uska roop ajeeb tha.

Rishiyon ne kaha:

“Niṣīda” — baith jao.

Isliye woh Niṣāda kehlaaya.

Usne Vena ke paap apne upar le liye.

Uske vanshaj jungle aur pahaadon mein rehne lage.

🌼 Moral

Ahankaar raja ko andha bana deta hai.

Jo dharma ko roke, woh swayam girta hai.

Shakti bina vinamrata ke vinash laati hai.

Adharm ka phal jaldi milta hai.

Sahi neta wahi hai jo dharma ka palan kare.

✨ Kahani sikhati hai —
Rajya shastra se nahi,
dharma se chalta hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 15
    with st.expander("Chapter 15 - Birth of Pṛthu and his Coronation"):
        text1 = """ 
        Chapter 15 — Pṛthu ka Janm aur Rajyabhishek
🌟 Divya Janm

Maitreya bole:

Rishiyon ne Vena ke baahu ka manthan kiya.

Tab wahan se ek divya yugul janma —
ek putra aur ek kanya.

Rishiyon ne turant pehchaan liya.

“Yeh Bhagavan Viṣṇu ka aṃśa hai.”
“Aur yeh Lakṣmī ji ka avataar hai.”

Putra ka naam rakha gaya — Pṛthu.
Kanya ka naam rakha gaya — Arcis.

Arcis hi unki patni bani."""
        create_image_text_layout(
            "attached_assets/chapter4/4.15.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        🎉 Sabka Anand

Aakash mein shankh aur dhol bajne lage.
Gandharv geet gaane lage.
Apsarayein nritya karne lagi.
Devta phool barsane lage.

Sabko samajh aa gaya —
Ek mahan raja janm le chuka hai.

👑 Rajyabhishek

Brahma ji khud aaye.

Unhone dekha:

Pṛthu ke haath mein chakra ka chinh

Pairon mein kamal ka chinh

Unhone kaha:

“Yeh sach mein Viṣṇu ka ansh hai.”

Tab Pṛthu ka rajyabhishek hua.

🎁 Devtaon ke Upahar

Har devta kuchh lekar aaya:

Kubera ne sona ka singhasan diya

Varuṇa ne chhatra diya

Vāyu ne chamara diye

Indra ne mukut diya

Yama ne dand diya

Lakṣmī ne anant sampatti di

Hari ne Sudarshan chakra diya

Rudra ne talwar di

Agni ne dhanush diya

Surya ne teer diye

Samudra ne shankh diya

Prithvi ne raste diye.
Pahaad aur nadiyon ne sahyog diya.

Sab prani khush the.

🎶 Bardo ki Prashansa

Sūta, Māgadha aur Bandin gaane lage.

Par Pṛthu muskuraye.

Unhone kaha:

“Abhi maine koi kaarya nahi kiya.”
“Meri prashansa kyun?”
“Jab tak gun prakat na ho, tab tak stuti nahi.”

Unhone aur kaha:

“Sachche gun ho tabhi prashansa achhi lagti hai.”
“Jhoothi tareef sharm ki baat hai.”

Sab log unki vinamrata dekh kar prabhavit ho gaye.

🌼 Moral

Sachcha neta vinamra hota hai.

Mahaan log apni tareef se door rehte hain.

Shakti aur sampatti tabhi pavitra hai jab saath mein namrata ho.

Bhagavan ka ansh hone ka matlab hai — seva aur dharma.

✨ Kahani sikhati hai —
Asli mahanta shor se nahi,
charitra se dikhai deti hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 16
    with st.expander("Chapter 16 - The Eulogy of Pṛthu by Bards"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter4/4.16.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 17
    with st.expander("Chapter 17 - Pṛthu subjugates the Earth"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter4/4.17.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 18
    with st.expander("Chapter 18 - Milking of the Earth in the form of a Cow"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter4/4.18.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 19
    with st.expander("Chapter 19 - Pṛthu’s Horse-sacrifices and Conflict with Indra"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter4/4.19.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 20
    with st.expander("Chapter 20 - Pṛthu initiated by Viṣṇu"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter4/4.20.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 21
    with st.expander("Chapter 21 - Pṛthu explains Dharma to his subjects"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter4/4.21.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 22
    with st.expander("Chapter 22 - Sanatkumāra’s Sermon to Pṛthu"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter4/4.22.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 23
    with st.expander("Chapter 23 - Pṛthu’s penance and ascension to Heaven"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter4/4.23.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 24
    with st.expander("Chapter 24 - Pṛthu’s Descendants and the Hymn of Rudra"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter4/4.24.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 25
    with st.expander("Chapter 25 - The Story of Purañjana—Introduction"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter4/4.25.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 26
    with st.expander("Chapter 26 - Purañjana’s Hunting Expedition and His Queen‘s Wrath Pacified"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter4/4.26.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 27
    with st.expander("Chapter 27 - Invasion of Caṇḍavega—The Episode of Kālakanyā"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter4/4.27.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 28
    with st.expander("Chapter 28 - Purañjana’s Rebirth as a Woman and Attainment of Liberation"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter4/4.28.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 29
    with st.expander("Chapter 29 - The Purañjana allegory explained"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter4/4.29.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 30
    with st.expander("Chapter 30 - The Marriage of Pracetasas with Māriṣā and the birth of Dakṣa"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter4/4.30.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 31
    with st.expander("Chapter 31 - The Story of Pracetasas: Their Renunciation and Liberation"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter4/4.31.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")
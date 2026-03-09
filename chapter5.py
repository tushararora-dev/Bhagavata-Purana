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
    create_image_text_layout("attached_assets/chapter5/chapter5.jpg", layout="full")
    # Book 5 - Fifth Skandha
    text0 = """
    <h2>Book 5 - Fifth Skandha</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")
    # Chapter 1
    with st.expander("Chapter 1 - The Life of Priyavrata"):
        text1 = """ 
        
        Chapter 1 — Priyavrata ki Jeevan Kahani (Hinglish Story)

Raja Parikshit ne ek din rishi Shukadeva se prashna kiya.

Unhone kaha:

“Priyavrata to Bhagwan Vishnu ke bade bhakt the.
Unka mann Atma ki shanti mein laga hua tha.

Phir aisa kaise hua ki woh grihastha jeevan mein aa gaye?
Kya family life to karmo ke bandhan ka kaaran nahi hoti?”"""
        create_image_text_layout(
            "attached_assets/chapter5/5.1.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Narada ka Shishya

Shukadeva bole:

“Hey Raja, tumhara prashna sahi hai.”

Prince Priyavrata bahut pavitra aur bhaktimay the.
Unhone rishi Narada ki seva karke atma ka gyaan prapt kiya tha.

Unka mann tapasya aur dhyan mein hi lagta tha.
Woh duniya ke kaam chhodkar sirf Bhagwan ka dhyan karna chahte the.

Manu ka Aadesh

Tab unke pita Svayambhuva Manu aaye.

Unhone kaha:

“Beta, tumhe duniya par rajya karna hoga.
Tumhi is dharti ko sambhalne ke yogya ho.”

Priyavrata ka mann is baat se khush nahi hua.
Unhe laga ki rajya karne se unka dhyan Bhagwan se hat jayega.

Brahma ka Aagman

Tab swayam Brahma swarg se aaye.

Unke saath:

devata

rishi

gandharva

sab the.

Brahma ne Priyavrata se prem se kaha:

“Hey putra, is duniya mein sab kuch Bhagwan ki ichchha se hota hai.
Hum sab bhi unke aadesh ke adheen hain.”

Phir unhone samjhaya:

“Yadi koi vyakti apne mann aur indriyon ko control kar le,
to grihastha jeevan bhi usse bandhan mein nahi baandh sakta.”

Rajya Grahan

Priyavrata ne vinamrata se Brahma ki baat maan li.

Unhone rajya sambhala.

Baad mein unhone Viśvakarma ki beti Barhishmati se vivaah kiya.

Unke:

10 putra hue

aur 1 beti hui.

Unke teen putra:

Kavi

Mahavira

Savana

bachpan se hi sanyasi ban gaye.

Unhone Bhagwan Vishnu ki bhakti ki aur moksha prapt kiya.

Priyavrata ka Adbhut Karya

Ek din Priyavrata ne dekha:

Surya jab Meru par ghoomta hai,
to dharti ka aadha hissa roshan hota hai
aur aadha andhere mein rehta hai.

Unhe ye theek nahi laga.

Tab unhone apne tej se bhare rath par baithkar
Surya ke peeche peeche saat baar dharti ka chakkar lagaya.

Unke rath ke pahiyon ke nishaan se
saat bade samundar ban gaye.

Is tarah dharti saat dvipo mein baant gayi:

Jambu

Plaksha

Shalmali

Kusha

Krauncha

Shaka

Pushkara

Har dvip ka alag raja banaya gaya.

Priyavrata ka Vairagya

Bahut saalon tak rajya karne ke baad
Priyavrata ke mann mein ek din vairagya jag gaya.

Unhone socha:

“Main indriyon ke peeche kyon bhaag raha hoon?
Yeh sab to maya hai.”

Unhone apne rajya aur dhan ko chhod diya.

Sab kuch apne putron ko dekar
woh phir se Narada ke dikhaye hue spiritual path par chal pade.

Adhyay ka Saar

Is kahani ka simple message hai:

Bhakti wale vyakti ko duniya ke kaam bhi karne pad sakte hain.

Lekin agar mann Bhagwan mein laga ho, to duniya bandhan nahi banti.

Aakhir mein sabse bada sukh vairagya aur bhakti mein hi hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 2
    with st.expander("Chapter 2 - The History of Agnīdhra"):
        text1 = """ 
        Chapter 2 — Agnīdhra ki Kahani (Hinglish Story)

Rishi Shukadeva ne kahani aage batayi.

Raja Priyavrata ke rajya tyag karne ke baad,
unke putra Agnidhra ne Jambudvipa ka rajya sambhala.

Agnīdhra ek achhe raja the.
Woh apni praja ka dhyan bilkul apne bachchon ki tarah rakhte the."""
        create_image_text_layout(
            "attached_assets/chapter5/5.2.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        🌿 Putra ki Ichchha

Ek din Agnīdhra ne socha:

“Main bhi ek putra paida karna chahta hoon
jo mere baad rajya sambhale.”

Isliye woh Mandara parvat ki ghati mein tapasya karne chale gaye.

Wahan unhone Brahma ki bhakti aur pooja shuru ki.

🌸 Swarg ki Apsara

Brahma ne Agnīdhra ki ichchha samajh li.

Unhone ek sundar apsara Purvacitti ko bheja.

Purvacitti dheere dheere ek sundar garden mein aayi
jo Agnīdhra ke ashram ke paas tha.

Wahan:

kamal ke talab

hans aur pakshi ki madhur awaaz

sugandhit phool

sab jagah ko swarg jaisa bana rahe the.

💫 Pehli Nazar

Purvacitti ke payal ki chan-chan ki awaaz sun kar
Agnīdhra ne apni aankhen kholi.

Unhone us sundar apsara ko dekha.

Uski chal, hasi aur madhur awaaz
sab kuch bahut hi manmohak tha.

Agnīdhra ka mann turant us par aa gaya.

😊 Agnīdhra ki Baat

Agnīdhra ne muskura kar kaha:

“Hey sundari, tum kaun ho?
Kya tum kisi devta ki shakti ho?

Tumhari aankhen to kamal ki pankhudi jaise teer hain
jo seedha dil ko chhoo lete hain.”

Unhone mazaak aur prem se bhari baatein karte hue
Purvacitti ki bahut tarif ki.

❤️ Prem aur Vivaah

Purvacitti bhi Agnīdhra se prabhavit ho gayi.

Usne dekha ki Agnīdhra:

buddhimaan hai

bahadur hai

sundar hai

aur dayalu hai

Dono ek dusre se prem karne lage.

Phir dono ne vivah jaisa sambandh bana liya
aur bahut saalon tak saath rahe.

👑 Nau Putra

Purvacitti ne Agnīdhra ko 9 putra diye:

Nābhi

Kimpuruṣa

Harivarṣa

Ilāvṛta

Ramyaka

Hiraṇmaya

Kuru

Bhadrāśva

Ketumāla

Baad mein Purvacitti wapas Brahma ke lok chali gayi.

🌍 Jambudvipa ka Vibhajan

Agnīdhra ne apne 9 putron mein
Jambudvipa ke alag alag kshetra baant diye.

Har putra apne region ka raja ban gaya.

Unke naam par hi woh regions jane gaye.

🌌 Agnīdhra ka Ant

Agnīdhra apni patni Purvacitti ko bahut yaad karte the.

Isliye jab unka jeevan samapt hua
toh woh usi lok mein pahunch gaye
jahan Purvacitti rehti thi.

🌿 Adhyay ka Saar

Is kahani se yeh seekh milti hai:

Tapasya se ichchha puri ho sakti hai.

Prem aur sambandh bhi jeevan ka ek hissa hain.

Raja ka kartavya hota hai praja ko bachchon ki tarah sambhalna."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 3
    with st.expander("Chapter 3 - The History of Nābhi—Incarnation of Ṛṣabha"):
        text1 = """ 
        Chapter 3 – The History of Nābhi and the Incarnation of Ṛṣabha

Ek samay ki baat hai. King Nābhi aur unki queen Merudevī ke paas koi santaan nahi thi.
Dono ek achha aur dharmic child chahte the.

Isliye unhone pure mann se Bhagwan Vishnu ki pooja aur yajna kiya.
Unka mann bahut shuddh tha.
Woh bas Bhagwan ki kripa chahte the."""
        create_image_text_layout(
            "attached_assets/chapter5/5.3.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Bhagwan ko paana aasaan nahi hota.
Bahut dhan, mantra, aur bade yajna bhi kabhi kabhi kaafi nahi hote.

Lekin Bhagwan apne bhakton se bahut pyaar karte hain.
Jab unhone dekha ki King Nābhi sachche dil se prarthana kar rahe hain,
to Bhagwan ka dil bhi pighal gaya.

Yajna ke dauran ek adbhut chamatkar hua.

Achanak Bhagwan Vishnu apne divya roop mein prakat ho gaye.
Unke chaar haath the.
Woh sunehre rang ke silk vastra pehne hue the.

Unke haath mein shankh, chakra, gada aur kamal tha.
Unke gale mein vanamala thi.
Unke seene par Shrivatsa ka pavitra chinh chamak raha tha.

Unka roop itna sundar tha ki sab log unhe dekh kar hairaan aur khush ho gaye.

Yajna karne wale rishiyon aur purohiton ne turant Bhagwan ko pranam kiya.
Unhone Bhagwan ko arghya jal diya aur bade samman se swagat kiya.

Unhone vinamrata se kaha:

“Hey Prabhu!
Hum aapki mahima ko poori tarah describe nahi kar sakte.
Aap sabse upar hain.
Aap prakriti aur sabhi cheezon ke swami hain.

Hum bas itna jaante hain ki aapki bhakti sabse bada dhan hai.

Aapko simple cheezein bhi bahut pasand hain.
Jaise jal, tulsi ke patte, aur sacchi prarthana.

Prabhu, sach kahen to aapko kisi cheez ki zaroorat nahi hai.
Yeh yajna bhi aapke liye zaroori nahi hai.

Phir bhi hum log apni chhoti ichchhaon ke liye aapko bula lete hain.

King Nābhi ek santaan chahte hain.
Aur woh chahte hain ki unka beta aapke jaise mahaan ho.

Shayad yeh hamari chhoti soch hai.
Phir bhi Prabhu, kripya humein maaf kijiye.”

Bhagwan Vishnu sab kuch shant mann se sun rahe the.

Phir Bhagwan muskuraye aur bole:

“Hey rishiyon, tumne ek bahut mushkil vardaan maanga hai.
Tum chahte ho ki King Nābhi ka beta mere jaisa ho.

Lekin sach yeh hai ki mere jaisa koi nahi hai.

Isliye main khud hi unka beta ban kar janm loonga.”

Yeh sunkar sab log bahut prasann ho gaye.

Bhagwan Vishnu ne yeh baat kahi
aur phir antar-dhyaan ho gaye.

Kuch samay baad, Queen Merudevī ke garbh se ek divya putra ka janm hua.

Uska naam tha Ṛṣabha.

Woh Bhagwan ka hi avatar the.

Ṛṣabha ka janm ek mahaan uddeshya ke liye hua tha.
Woh duniya ko sanyas, tapasya aur brahmacharya ka path sikhane wale the.

Aur is tarah Bhagwan Vishnu ne King Nābhi ki ichchha poori ki.

✨ Moral:
Jab koi bhakt sachche mann aur shraddha se prarthana karta hai,
to Bhagwan uski sunte hain aur uski madad zaroor karte hain."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4
    with st.expander("Chapter 4 - The miraculous history of Ṛṣabha"):
        text1 = """ 
        Chapter 4 – The Miraculous History of Ṛṣabha

Śrī Śuka ne kahani aage batayi.

Jab Ṛṣabha ka janm hua, tabhi se unme divya lakshan dikhne lage.
Unke pairon ke talvo par vajra aur ankush jaise pavitra chinh the.

Jaise jaise woh bade hue, unki mahima bhi badhti gayi.
Woh sabke saath barabari aur daya se vyavahar karte the."""
        create_image_text_layout(
            "attached_assets/chapter5/5.4.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Unhone apne mann aur indriyon par poora control rakha.
Unhe bhog-vilas aur sukh-samagriyon se koi lagav nahi tha.

Unke andar bahut yog shakti aur adhyatmik bal tha.
Isliye raja ke mantri, praja aur brahman sab chahte the
ki Ṛṣabha hi dharti ke raja bane.

Unki shakti, tejas aur mahima dekh kar
King Nābhi ne unka naam rakha Ṛṣabha,
jiska matlab hota hai sabse uttam.

Lekin ek baar kuch ajeeb hua.

Indra, jo devtaon ke raja the,
Ṛṣabha se thoda jealous ho gaye.

Isliye unhone Ṛṣabha ke desh Ajanābha mein baarish nahi hone di.

Jab Ṛṣabha ko yeh pata chala,
toh woh bas halka sa muskuraye.

Apni yog shakti se unhone khud hi
poore desh mein achhi baarish karva di.

Sab log hairaan reh gaye.

King Nābhi apne putra ko paakar bahut khush the.
Woh aksar unhe pyaar se godh mein uthate.

Kabhi kabhi pyaar mein kehte,
“Oh mere pyare bacche!”

Bhagwan ka avatar hone ke baad bhi
Ṛṣabha unke liye ek pyara beta hi the.

Kuch samay baad King Nābhi ne socha
ki ab Ṛṣabha ko raja bana dena chahiye.

Unhone praja ki ichchha bhi dekhi.
Sab log Ṛṣabha ko raja chahte the.

Isliye Nābhi ne Ṛṣabha ko rajya ka raja bana diya.

Uske baad King Nābhi aur Queen Merudevī
jungle chale gaye.

Wahan unhone Badarikāśrama mein rehkar
Bhagwan ki tapasya aur dhyan kiya.

Dheere dheere unhone moksha ki avastha prapt kar li.

Log aaj bhi King Nābhi ki bahut tareef karte hain.

Log kehte hain:

“Kaun sa raja itna pavitra ho sakta hai
ki Bhagwan khud uska beta ban kar janm lein?”

Aur kaun itna bhagyashali ho sakta hai
jo brahmanon ki seva aur yajna se
Bhagwan ko prakat kar de?

Ab Ṛṣabha dharti par ek adarsh raja ban gaye.

Unhone duniya ko dikhaya
ki ek insaan ko kaise jeevan jeena chahiye.

Sabse pehle woh gurukul gaye aur shiksha li.
Fir apne guru ki permission se
unhone grihastha jeevan shuru kiya.

Unki shaadi Jayantī se hui,
jo Devraj Indra ki beti thi.

Unke 100 putra hue.

Unka sabse bada beta tha Bharata.
Bharata ek mahaan yogi aur dharmic raja bane.

Unhi ke naam par is desh ka naam
Bhārata (India) pada.

Baaki putron mein se
9 putra bade yogi aur bhakt bane.

Unhone duniya ko bhakti aur dharm ka gyaan diya.

Baaki 81 putra bhi bahut gyani the.
Woh ved padhte aur yajna karte the.
Log unhe brahman jaise gyani mante the.

Bhagwan Ṛṣabha sab kuch hone ke baad bhi
bahut simple aur vinamra the.

Woh duniya ke raja the,
lekin ek aam insaan ki tarah jeete the.

Unhone logon ko sikhaya
ki ek grihastha ko dharma, dhan, khushi aur moksha
sab ka balance rakhna chahiye.

Ek bahut important baat bhi hai.

Log aksar leaders ko follow karte hain.
Jo raja karta hai, praja bhi wahi karti hai.

Isliye Ṛṣabha ne sahi example set kiya.

Unhone rajya ko nyay aur dharm se chalaya.

Unhone brahmanon ki salah se
100 yajna bhi kiye.

Unke rajya mein log bahut khush aur santusht the.

Koi kisi aur ki cheez par lalach nahi karta tha.

Sabke dil mein bas
apne raja Ṛṣabha ke liye prem aur respect tha.

Ek din Ṛṣabha apne rajya ka daura karte hue
Brahmāvarta naam ke sthan par aaye.

Wahan bahut bade rishi aur brahman ikattha hue the.

Ṛṣabha ne socha
ab samay aa gaya hai ki woh
apne putron ko jeevan ka sachcha gyaan dein.

Isliye sabke saamne
unhone apne putron ko mahan updesh dena shuru kiya.

Aur wahi se ek bahut gehri aur pavitra siksha shuru hui.

✨ Moral:
Ek sachcha leader wahi hota hai
jo sirf shabd se nahi,
apne jeevan ke example se logon ko sikhata hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 5
    with st.expander("Chapter 5 - Ṛṣabha’s discourse on the Path of Liberation"):
        text1 = """ 
        Chapter 5 – Ṛṣabha’s Discourse on the Path of Liberation

Ek din Lord Ṛṣabha ne apne sabhi putron ko bulaya.
Unhone unhe jeevan ka sabse bada gyaan dena shuru kiya.

Ṛṣabha ne pyaar se kaha:

“Mere pyare putro,
yeh human body bahut special hoti hai.

Iska use sirf bhog aur pleasures ke liye nahi karna chahiye.
Agar koi sirf pleasures ke piche bhagta hai,
toh woh janwaron jaise jeevan jeeta hai."""
        create_image_text_layout(
            "attached_assets/chapter5/5.5.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Human life ka asli purpose hai
tapasya aur Bhagwan ki realization.

Jab mann shuddh ho jata hai,
tab insaan anant sukh aur shanti paata hai.”

Phir Ṛṣabha ne ek aur important baat batayi.

“Mahaan logon ki seva karna
moksha ka darwaza hota hai.

Lekin jo log sirf indriya sukh aur vasna mein lage rehte hain,
unki sangati dukh aur narak ki taraf le jaati hai.”

Ṛṣabha ne kaha ki sachche mahan log kaise hote hain.

Woh shant, dayalu aur gussa na karne wale hote hain.
Woh sabke saath prem aur samta se vyavahar karte hain.

Unhone apne putron ko samjhaya:

“Jab insaan apni indriyon ko khush karne ke liye jeeta hai,
toh woh dheere dheere galat kaam karne lagta hai.

Aur wahi galat karm usse
dukh aur bandhan mein daal dete hain.”

Phir Ṛṣabha ne ek gehri baat batayi.

Unhone kaha:

“Jab tak insaan atma ka sach nahi samajhta,
tab tak woh ignorance (avidya) mein phansa rehta hai.

Aur jab tak mann karmo mein uljha rehta hai,
tab tak atma body ke bandhan mein bandhi rehti hai.”

Phir Ṛṣabha ne grihastha jeevan ke baare mein bhi bataya.

Unhone kaha ki jab ek aadmi aur aurat ka rishta banta hai,
toh unke dil ek majboot knot se band jate hain.

Iske baad insaan sochne lagta hai:

“Yeh mera ghar hai,
yeh meri property hai,
yeh mere bacche hain.”

Aur is tarah woh maya ke jaal mein phans jata hai.

Lekin jab insaan ego aur attachment ko chhod deta hai,
tab uska mann free ho jata hai.

Aur phir woh moksha pa sakta hai.

Ṛṣabha ne moksha ka raasta bhi bataya.

Unhone kaha:

Bhagwan ki bhakti karo

Mahaan logon ki seva karo

Sukh aur dukh ko same samjho

Sach ki talash karo

Bhagwan ki katha suno aur sunao

Gussa aur dushmani chhod do

Self-control seekho

Yeh sab cheezein insaan ko
atma gyaan aur mukti ki taraf le jaati hain.

Phir Ṛṣabha ne ek aur important baat kahi.

Unhone kaha:

“Ek raja, guru ya pita ka farz hai
ki woh logon ko sachcha raasta dikhaye.

Agar woh logon ko galat raaste par le jata hai,
toh woh sachcha leader nahi hai.”

Unhone kaha ki duniya mein log aksar
chhote pleasures ke liye ladte hain.

Lekin unhe pata nahi hota
ki yeh sab akhir mein dukh hi deta hai.

Phir Ṛṣabha ne apne putron ko kaha:

“Tum sab mere dil se janme ho.
Isliye tum sab apne bade bhai Bharata ka samman karo.

Unki seva karna
mere hi seva karne ke barabar hai.”

Ṛṣabha ne ek aur gehri baat samjhayi.

Unhone kaha:

“Har jeev, chahe woh insaan, janwar ya ped ho,
un sab mein Bhagwan ka hi vaas hai.

Agar tum sabhi jeevon ko
respect aur daya se dekho,
toh wahi meri sachchi pooja hai.”

Yeh sab gyaan dene ke baad
Ṛṣabha ne apne sabse bade putra Bharata ko
rajya ka raja bana diya.

Uske baad Ṛṣabha ne sab kuch tyaag diya.

Unhone sanyas ka raasta chuna.

Woh ek avadhuta ki tarah jeene lage.
Unhone kapde tak chhod diye.

Kabhi woh bilkul chup rehte,
kabhi logon ko lagta woh pagal ya bewakoof hain.

Log unka mazaak bhi banate the.
Koi un par dhool, pathar aur gaaliyan bhi fenkta tha.

Lekin Ṛṣabha ko koi farq nahi padta tha.

Kyunki unka mann
poori tarah Bhagwan mein sthir tha.

Unhone apna jeevan
param yogi aur mahaan tapasvi ki tarah jeeya.

Unke paas bahut divya yog shaktiyan bhi thi.
Jaise hawa mein chalna,
ya door ki cheezein dekhna.

Lekin unhone kabhi bhi
in powers ka ghamand nahi kiya.

Woh bas atma gyaan aur Bhagwan mein hi sthir rahe.

✨ Moral:
Human life ka asli purpose sirf pleasure nahi hai.
Asli sukh milta hai bhakti, gyaan aur detachment se."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6
    with st.expander("Chapter 6 - Ṛṣabha quits His body"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter5/5.6.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7
    with st.expander("Chapter 7 - The Life of Bharata"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter5/5.7.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 8
    with st.expander("Chapter 8 - Bharata reborn as a deer"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter5/5.8.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 9
    with st.expander("Chapter 9 - Bharata, reborn as a Brāhmaṇa, saved by Bhadrakālī"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter5/5.9.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 10
    with st.expander("Chapter 10 - Bharata’s Life: King Rahūgaṇa accepts discipleship"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter5/5.10.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 11
    with st.expander("Chapter 11 - Bharata imparts spiritual knowledge to Rahūgaṇa"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter5/5.11.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 12
    with st.expander("Chapter 12 - Dialogue between Bharata and Rahūgaṇa"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter5/5.12.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 13
    with st.expander("Chapter 13 - The Saṃsāra—a forest: An allegory"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter5/5.13.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 14
    with st.expander("Chapter 14 - Explanation of the Allegory of Saṃsāra—Forest"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter5/5.14.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 15
    with st.expander("Chapter 15 - Description of Bharata’s Dynasty"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter5/5.15.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 16
    with st.expander("Chapter 16 - Mythological Geography—The Terrestrial Globe"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter5/5.16.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 17
    with st.expander("Chapter 17 - The Descent of the Gaṅgā"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter5/5.17.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 18
    with st.expander("Chapter 18 - Description of Various Continents (Varṣa)"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter5/5.18.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 19
    with st.expander("Chapter 19 - Description of Kimpuruṣa and Bhārata Varṣas"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter5/5.19.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 20
    with st.expander("Chapter 20 - Description of the remaining six Dvīpas"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter5/5.20.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 21
    with st.expander("Chapter 21 - The Stellar Region"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter5/5.21.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 22
    with st.expander("Chapter 22 - Description of the Moon and other Planets"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter5/5.22.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 23
    with st.expander("Chapter 23 - Description of Viṣṇupada and Śiśumāra-cakra"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter5/5.23.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 24
    with st.expander("Chapter 24 - Rāhu’s Position and the Subterranean Regions"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter5/5.24.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 25
    with st.expander("Chapter 25 - Description of Saṅkarṣaṇa—the Serpent Śeṣa"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter5/5.25.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 26
    with st.expander("Chapter 26 - Description of Hells (Naraka)"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter5/5.26.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")
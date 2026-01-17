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
    create_image_text_layout("attached_assets/chapter1/chapter1.jpg", layout="full")

    text0 = """
    <h2>Book 1 - First Skandha</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")
    
    # Chapter 1
    with st.expander("Chapter 1 - Dialogue between Sūta and Śaunaka in the Naimiśa forest"):
        text1 = """ 
        Shlok 1 – Mangal Ācharaṇ

Aao hum us Param Satya ka dhyān karein.
Jis se srishti paida hoti hai,
jismein srishti tikti hai,
aur jismein sab kuch ant mein mil jata hai.

Wahi sab jagah maujood hai.
Wahi sab kuch jaanta hai.
Wahi swayam-prakāshit hai.

Usi ne Brahmā ke hriday mein
Vedo ka gyaan prakat kiya.
Jise bade-bade vidvān bhi
samajhne mein ulajh jaate hain.

Uske tej se māyā nasht ho jaati hai.
Wahi ek param satya hai."""
        create_image_text_layout(
            "attached_assets/chapter1/1.1.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Shlok 2 – Bhāgavata ka Mahattva

Is Śrīmad Bhāgavata mein
sabse shuddh Dharma bataya gaya hai.

Yeh Dharma:

chal-kapat se mukt hai

swarth se pare hai

aur moksha ke lobh se bhi upar hai

Yeh granth:

param ānanda deta hai

teen prakār ke dukh mita deta hai

Aise gyaan ko
dusre granthon se turant paana mushkil hai.
Par Bhāgavata sunte hi,
bhagwān hriday mein prakat ho jaate hain.

Shlok 3 – Amrit-phal

Bhāgavata
Vedo ke kalp-vriksh ka pakka hua phal hai.

Yeh phal:

Śuka muni ke mukh se gira

poora ka poora amrit-ras se bhara hai

Hey rasik jan!
Is Bhāgavata ka ras
is lok mein bhi peeyo,
aur param gati mein bhi.

Shlok 4–5 – Naimiśāraṇya

Naimiśāraṇya van mein,
jo Viṣṇu ko priya hai,
Śaunaka ji ke netritva mein
rishiyon ne 1000 varsh ka yajña kiya.

Ek din,
subah ke karma poore karke,
sab rishi milkar
Sūta ji se prashn karte hain.

Shlok 6–9 – Sūta ji ki Mahima

Rishiyon ne kaha:
“Sūta ji,
aapne Purāṇ, Itihās,
aur Smṛti granth sab padh rakhe hain.

Vyāsa ji ka jo gyaan hai,
aur anya rishiyon ka jo gyaan hai,
wo sab aap jaante hain.

Is Kali-yug ke logon ke liye
jo sabse shreshṭh ho,
wo aap humein batayein.”

Shlok 10–11 – Kali Yug ka Dukh

Rishi bole:
“Kali yug mein log:

chhoti aayu wale

alasya se bhare

kam samajh wale

aur rogon se peedit hote hain

Isliye,
bahut saare karmon mein se
jo saar ho,
wahi humein batayein.”

Shlok 12–18 – Bhagwān ka Mahatmya

Sūta ji,
aap jaante hain ki
Bhagwān Kṛṣṇa ka janm
sabke kalyān ke liye hua.

Jo vyakti:

sansār ke chakr mein phans kar

sirf Hari ka naam leta hai,
wo turant mukta ho jata hai.

Hari ke bhakton ka darshan hi
pavitr kar deta hai.
Ganga ko to sparsh chahiye,
par bhakt ko nahi.

Shlok 19–21 – Ras aur Leela

Hari ki kathā:

har pal aur madhur hoti jaati hai

kabhi trupti nahi deti

Kṛṣṇa ne:

manushya roop mein

alaukik leelayein ki hain

Balarāma ke saath

Isliye rishi keh rahe hain:
“Humein poora samay hai,
humein Hari ki kathā sunni hai.”

Shlok 22–23 – Antim Prashn

Rishi bole:
“Kali yug ke is bhayanak samundar ko
paar karne ke liye
aap hamare naavik hain.

Ab jab Śrī Kṛṣṇa
apne lok ko chale gaye hain,
to batao—

👉 Dharma ab kis ka āśray le raha hai?”

Bhāv 🌸

Bhāgavata = prem + gyaan + bhakti ka saar

Sunna hi mukti ka raasta hai

Kali yug mein Hari-kathā hi nauka hai"""
        create_image_text_layout(
            text_content=text2,
            layout="full"
        )

    # Chapter 2
    with st.expander("Chapter 2 - Merits of Devotion to Hari"):
        text1 = """ 
        Shuruaat – Sūta ji bolte hain

Brāhmaṇon ke sundar prashn sun kar,
Sūta ji bahut prasann hue.
Unhone pyaar se unki baat ko saraha
aur shant mann se uttar dena shuru kiya."""
        create_image_text_layout(
            "attached_assets/chapter1/1.2.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Śuka muni ko namaskar

Main Śuka muni ko pranam karta hoon.
Jo bachpan mein hi
ghar chhod kar chal diye the.

Jab Vyāsa ji ne pyaar se pukara—
“Putra! Putra!”
toh van ke ped bhi
us awaz ka uttar dene lage.
Kyunki Śuka sabke hriday mein baste the.

Bhāgavata ka prakāsh

Śuka muni ne
sansār ke andhkar mein bhatakte logon ke liye
Bhāgavata Purāṇa ka deep jalaya.

Yeh granth:

Vedo ka saar hai

shuddh gyaan se bhara hai

aur moksha ka ekmatra deepak hai

Nārāyaṇa aur Nara ka smaran

Pehle Nārāyaṇa,
phir Nara (shreshṭh manav),
aur Sarasvatī maa ko smaran karke
Bhāgavata ki kathā kahi jaati hai.

Sachcha Dharma kya hai

Sūta ji bole:
“Tumhara prashn bahut shubh hai.
Kyunki tumne Kṛṣṇa ke baare mein poocha hai.”

Wahi sachcha Dharma hai
jo:

Hari ke prati nishkām bhakti paida kare

bina ruke, bina swarth ke chale

aur aatma ko shant kar de

Bhakti se kya hota hai

Jo Vāsudeva ki bhakti karta hai:

uske mann mein vairāgya aata hai

aur usse sahaj gyaan milta hai

Agar koi dharm:

bahut mehnat se kiya jaaye

par Kṛṣṇa-kathā se prem na jagaye

toh wo sirf thakaan hai,
sachcha phal nahi.

Jeevan ka asli lakshya

Dharma ka lakshya:

dhan nahi

bhog nahi

swarg ka lobh bhi nahi

Jeevan ka lakshya hai:
👉 Satya ki khoj (Tattva-jijñāsā)

Sirf utna bhog chahiye
jitna sharir chalane ke liye zaroori ho.

Tattva kya hai

Jo gyaani hain,
wo Satya ko kehte hain:

Brahman

Paramātman

Bhagavān

Naam alag ho sakte hain,
par Satya ek hi hai.

Bhakti ka safar

Jab koi:

shraddha se sunta hai

santon ki seva karta hai

aur Hari-kathā mein ras leta hai

toh Kṛṣṇa
uske hriday mein aa jaate hain
aur sab ashubh gun hila dete hain.

Mann ki shuddhi

Bhakti se:

rajas (lobh, chanchalta)

tamas (alas, andhkar)
dheere-dheere shant ho jaate hain.

Mann sattva mein sthir hota hai.
Shant hota hai.
Saaf hota hai.

Antim anubhav

Jab hriday shant ho jaata hai:

ahankaar ki gāanth toot jaati hai

sab sanshay mit jaate hain

purane karm jal jaate hain

Tab Bhagavān
andar hi andar
darshan de dete hain.

Teen gun aur Bhagavān

Prakṛti ke teen gun hote hain:

tamas

rajas

sattva

Bhagavān:

Hari (sattva)

Brahmā (rajas)

Śiva (tamas)

Par moksha
sirf sattva-roop Hari se milta hai.

Isliye kya karein

Isliye rishiyon ne kaha:

Viṣṇu ki pooja karo

Nārāyaṇa ka smaran karo

Hari-bhakti mein mann lagao

Jo aisa karta hai,
wo antim gati paata hai.

Sab kuch Vāsudeva ke liye

Vedo ka saar → Vāsudeva

Yajña → Vāsudeva

Yoga → Vāsudeva

Gyaan → Vāsudeva

Tapasya → Vāsudeva

Moksha → Vāsudeva

👉 Vāsudeva hi sab ka ant aur aarambh hain.

Bhāv 🌿

Bhakti = shuddhi + shanti + gyaan

Hari-kathā = hriday ka deepak

Moksha ka raasta = prem bhari bhakti"""
        create_image_text_layout(
            text_content=text2,
            layout="full"
        )

    # Chapter 3
    with st.expander("Chapter 3 - Description of twenty-four incarnations of Lord Viṣṇu"):
        text1 = """ 
        Sṛṣṭi ki shuruaat

Sūta ji bole—
Jab sṛṣṭi banana tha,
Bhagavān ne Puruṣa-roop dharan kiya.

Unke sharīr se:

buddhi

mann

indriyaan
sab prakat hui.

Unke naabhi-kamal se Brahmā ka janm hua,
jab Bhagavān jal par yog-nidrā mein the."""
        create_image_text_layout(
            "attached_assets/chapter1/1.3.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Bhagavān ka vishāl roop

Yogī dekhte hain—

hazāron sir

hazāron haath

hazāron charan

Yeh Ādi-Nārāyaṇa ka roop hai.
Sab avatār isi se nikalte hain.

24 Avatāron ki kathā (Short & Clear)
1. Kumār (Sanaka–Sanandana)

Bhagavān ne bachche-brāhmaṇ roop mein
akhand brahmacharya sikhaya.

2. Varāha

Varaha
Prithvī Rasātal mein gir gayi.
Bhagavān ne suar (boar) ban kar
use upar uthaya.

3. Nārada

Narada
Bhagavān ne devarṣi ban kar
Pañcarātra bhakti-mārga bataya.

4. Nara–Nārāyaṇa

Nara-Narayana
Badarikāśram mein kathor tapasya.
Shuddh vairāgya ka darshan.

5. Kapila

Kapila
Sāṅkhya darshan ka updesh diya.
Tatvon ka gyaan samjhaya.

6. Dattātreya

Dattatreya
Atri–Anasūyā ke putra.
Ātm-gyaan ka updesh.

7. Yajña

Yajna
Svāyambhuva Manu ke yug ki rakṣā.

8. Ṛṣabha

Rishabha
Sannyās aur vairāgya ka rāsta dikhaya.

9. Pṛthu

Prithu
Prithvī se ann aur auṣadhi nikali.
Lok-kalyāṇ.

10. Matsya

Matsya
Pralay mein Vaivasvata Manu ko bachaya.

11. Kūrma

Kurma
Samudra-manthan mein
Mandar parvat ko sambhāla.

12. Dhanvantari

Dhanvantari
Amṛt aur Ayurveda ka daata.

13. Mohinī

Mohini
Devon ko amṛt dilaya,
asuron ko mohit kiya.

14. Nṛsiṁha

Narasimha
Hiraṇyakaśipu ka vināś,
Prahlāda ki rakṣā.

15. Vāmana

Vamana
Teen kadam mein
Bali se swarg wapas liya.

16. Paraśurāma

Parashurama
Adharmī kṣatriyon ka ant (21 baar).

17. Vyāsa

Vyasa
Vedon ko vibhaajit kiya.
Mahābhārata aur Purāṇ rachit.

18. Rāma

Rama
Maryādā Puruṣottam.
Samudra par setu, Rāvaṇ-vadh.

19–20. Balarāma aur Kṛṣṇa

Balarama
Krishna
Prithvī ka bhār utaara.
Bhakti, gyaan aur līlā ka prakāsh.

21. Buddha

Buddha
Kali-yug mein
ahimsā aur karuṇā ka sandesh.

22. Kalki

Kalki
Kali-yug ke ant mein.
Adharm ka nash, dharm ki punarsthapana.

Mukhya Siddhānt

Avatār anant hain

Par Śrī Kṛṣṇa swayam Bhagavān hain

Baaki sab unke aṁś aur kalā hain

Phal (Reward)

Jo vyakti:

subah-shaam shraddhā se

in avatāron ka smaran karta hai

Uske:

duḥkh nasht hote hain

bhay mit jaata hai

aur mukti ka rāsta khulta hai

Antim Bhāv

Bhagavān:

janm-rahit

karm-rahit

phir bhi līlā ke liye avatār lete hain

Jab Bhagavān Kṛṣṇa chale gaye,
toh Bhāgavata Purāṇa
Kali-yug ka sooraj ban kar utra."""
        create_image_text_layout(
            text_content=text2,
            layout="full"
        )

    # Chapter 4
    with st.expander("Chapter 4 - Arrival of Nārada"):
        text1 = """ 
        Sabhā mein prashna

Vyāsa ji bolte hain—
Naimiśāraṇya ke van mein
hazāron varshon ka yajña chal raha tha.

Sabse varishṭh ṛṣi Śaunaka
Sūta ji ke vachanon se prasann hue.

Unhone vinamr bhāv se puchha—"""
        create_image_text_layout(
            "attached_assets/chapter1/1.4.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Śaunaka ke prashna

“Hey Sūta!
Humein wahi pavitra kathā sunaiye
jo Śrī Śuka ne kahi thi.

Yeh kathā kab shuru hui?

Kahaan hui?

Aur kis uddeshya se?

Aur yeh batayiye—
Vyāsa ji ko is granth ko likhne ki
prerṇā kisne di?”

Śuka ka adbhut svabhāv

Śaunaka kehte hain—

Śuka ji mahān yogī the.
Unka mann sirf Brahman mein sthir tha.

Woh:

sharīr ki sudh-budh se pare

samājik bhed-bhāv se mukt

duniya ke liye jaise “pagal” se lagte

Ek adbhut baat hui—

Jab Śuka nagn avasthā mein ja rahe the,
apsarāon ne apne vastra nahin badle.

Par jab Vyāsa ji pichhe aaye,
apsarāon ne turant vastra dharan kar liye.

Kyon?
Kyoki Vyāsa ji mein
purush–stri ka bhed tha,
par Śuka ji ki dr̥ṣṭi bilkul shuddh thi.

Parīkṣit ki kathā

Śaunaka puchhte hain—

“Kaise Śuka ji
Hastināpura aaye?

Kaise unki aur
Rājā Parīkṣit ki kathā hui?

Aur aisa kyun hua
ki itna mahān samrāṭ
Ganga ke kināre
upvās karke
mr̥tyu ka intezār karne laga?”

Sūta ji ka uttar – Vyāsa ka janm

Sūta ji bole—

Dvāpara yug ke ant mein
Vyāsa ji ka janm hua.

Woh:

Parāśara ke putra

Hari ke kalā-avatār

bhūt–bhaviṣya ke gyaatā

Ek din
Sarasvatī nadi ke kināre
ekānt mein baithkar
unhone manan kiya.

Kali yug ka darshan

Vyāsa ji ne dekha—

logon ki āyu kam hoti ja rahi hai

buddhi aur shakti ghat rahi hai

dharm ka bal kam ho raha hai

Tab unhone socha—
“Sab ke liye kya hitkari hoga?”

Vedon ka vibhaajan

Vyāsa ji ne—

Ek Veda ko chaar mein baanta

Ṛg

Yajur

Sāma

Atharva

Aur Itihās–Purāṇ ko
“Pañcham Veda” kaha.

Shiṣyon ko zimmedāri di:

Paila → Ṛgveda

Jaimini → Sāmaveda

Vaiśampāyana → Yajurveda

Sumantu → Atharvaveda

Aur Purāṇon ka bhār
Romaharṣaṇa ko diya.

Phir bhi mann ashānt

Itna sab karne ke baad bhi
Vyāsa ji ka mann shānt nahi hua.

Unhone socha—
“Shāyad maine
Bhagavān ki nirgun bhakti
poori tarah se nahi kahi.”

Isi chintan mein
woh Sarasvatī ke kināre
udas baithe the.

Tab Nārada aaye

Isi samay
devarṣi Narada
Vyāsa ji ke āśram aaye.

Devon ke pūjya Nārada ko dekhkar
Vyasa
turant khade hue,
unhe ādar se bithaya
aur pūjan kiya.

Yahin se
Bhāgavata Purāṇa ki
mahān kathā ka
asli pravāh shuru hota hai 🌸"""
        create_image_text_layout(
            text_content=text2,
            layout="full"
        )

    # Chapter 5
    with st.expander("Chapter 5 - The Dialogue Between Vyāsa and Nārada"):
        text1 = """ 
        Samvād ka ārambh

Sūta ji kehte hain—

Divya ṛṣi Narada,
haath mein veena liye,
muskurāte hue baithe the.

Unke saamne
Vyasa
shaant bhāv se virājmān the."""
        create_image_text_layout(
            "attached_assets/chapter1/1.5.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Nārada ka prashna

Nārada bole—

“Hey Parāśara-putra!
Kya tumhara mann shānt hai?

Kya jo jaan’na chahte the,
woh sab jaan liya?

Mahābhārata likh diya,

Vedon ka saar samjha,

Phir bhi tum
kyon udaas ho?”

Vyāsa ka dukh

Vyāsa ji bole—

“Sab kuch hote hue bhi
mera hr̥day santusht nahi.

Main jaanta hoon—
par ānand mehsoos nahi karta.

Aap sab jaante hain—
is ashaanti ka kaaran
mujhe spasht bataiye.”

Nārada ka mool updesh

Nārada bole—

“Vyāsa!
Tumne Bhagavān ke gun
poori tarah se nahi gaaye.

Tumne dharm, arth, kāma, mokṣa
sab bataye—
par Hari ki mahimā
kendr mein nahi rakhi.”

Bhakti ke bina gyaan adhoora

Nārada ne kaha—

Sundar shabd,
alankār,
vidvatā—

Agar unmein
Hari-kathā nahi,
toh woh—

sansārik logon ko bhā sakti hai

par santon ko nahi

Jaise:

Hans kabhi
kaag ke talab mein nahi rehte 🦢

Hari-naam ka bal

Nārada bole—

Aisi kathā bhi
jo vyākaraṇ se poori na ho—
par jismein
Bhagavān ka naam ho,

woh:

paap naash karti hai

hr̥day ko shuddh karti hai

Par gyaan—
agar bhakti ke bina ho,
toh woh bhi shushk ho jaata hai.

Vyāsa ki chūk

Nārada ne spasht kaha—

“Tumne logon ko
karm aur phal bataye,

Par jo log pehle se hi
bhogon mein uljhe the,
woh usi ko dharm samajh baithe.

Isliye tumhara mann
kahin tik nahi pa raha—
jaise hawa mein dolti naav 🚣‍♂️”

Asli maarg

Nārada bole—

Jo vyakti
Hari ke charanon mein sharan leta hai,
agar beech mein gir bhi jaaye—
toh uska nuksaan nahi hota.

Par jo bhakti ke bina
sirf karm karta rahe—
use kya milta hai?

Sukh aur dukh
samay ke saath
apne-aap aate jaate hain.

Isliye:
🎯 Antim lakshya = Bhagavān anubhav

Nārada apni kathā batate hain

Nārada bole—

“Pichhle janm mein
main ek daasi ka putra tha.

Chhota sa bachcha,
par santon ki seva karta tha.

Unke jhoothe bhojan se
mera mann shuddh hua.

Roz main
Kṛṣṇa-kathā sunta tha—
dhyaan se, prem se.”

Bhakti ka janm

Nārada kehte hain—

Sun’te sun’te—

meri bhakti jagi

buddhi sthir hui

maya ka bandhan dheere-dheere toota

Aur ek din
mujhe spasht ho gaya—
“Main sharīr nahi hoon,
main ātmā hoon.”

Seva + Bhakti + Gyaan

Nārada bole—

Jo karm
Bhagavān ko samarpit hote hain,
wahi bandhan todte hain.

Jaise:

shuddh ki hui dava
hi rog mitaati hai 💊

Waise hi:

Bhagavān ko arpit karm
sansār-roop rog ka ilaaj hai.

Antim sandesh

Nārada ne Vyāsa se kaha—

“Tum Bhagavān ke liye
janme ho.

Ab:
📜 Hari ki leelāon ko
poori mahimā ke saath likho.

Yahi:

tapasyā ka phal hai

gyaan ka saar hai

aur jagat ka kalyāṇ bhi.”

Yahin se
Śrīmad Bhāgavata Purāṇa
ka divya pravāh
poori shakti se behne lagta hai 🌊✨"""
        create_image_text_layout(
            text_content=text2,
            layout="full"
        )

    # Chapter 6
    with st.expander("Chapter 6 - The Dialogue Between Vyāsa and Nārada (continued)"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter1/1.6.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(
            text_content=text2,
            layout="full"
        )

    # Chapter 7
    with st.expander("Chapter 7 - Punishment of Āśvatthāman"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter1/1.7.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(
            text_content=text2,
            layout="full"
        )

    # Chapter 8
    with st.expander("Chapter 8 - Kuntī’s Eulogy of Kṛṣṇa and Yudhiṣṭhira’s Repentance"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter1/1.8.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(
            text_content=text2,
            layout="full"
        )

    # Chapter 9
    with st.expander("Chapter 9 - Yudhiṣṭhira’s Acquisition of Kingdom"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter1/1.9.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(
            text_content=text2,
            layout="full"
        )

    # Chapter 10
    with st.expander("Chapter 10 - Kṛṣṇa’s Departure to Dvārakā"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter1/1.10.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(
            text_content=text2,
            layout="full"
        )

    # Chapter 11
    with st.expander("Chapter 11 - Kṛṣṇa’s Entrance into Dvārakā"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter1/11.1.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(
            text_content=text2,
            layout="full"
        )

    # Chapter 12
    with st.expander("Chapter 12 - Birth of Parīkṣit"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter1/12.1.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(
            text_content=text2,
            layout="full"
        )

    # Chapter 13
    with st.expander("Chapter 13 - Discourse of Nārada"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter1/13.1.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(
            text_content=text2,
            layout="full"
        )

    # Chapter 14
    with st.expander("Chapter 14 - Conjectures of Yudhiṣṭhira"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter1/14.1.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(
            text_content=text2,
            layout="full"
        )

    # Chapter 15
    with st.expander("Chapter 15 - Ascent of the Pāṇḍavas to Heaven"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter1/15.1.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(
            text_content=text2,
            layout="full"
        )

    # Chapter 16
    with st.expander("Chapter 16 - Dialogue between the Earth and Dharma"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter1/16.1.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(
            text_content=text2,
            layout="full"
        )

    # Chapter 17
    with st.expander("Chapter 17 - Punishment and Control of Kali"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter1/17.1.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(
            text_content=text2,
            layout="full"
        )

    # Chapter 18
    with st.expander("Chapter 18 - Curse of the Brāhmaṇa"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter1/18.1.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(
            text_content=text2,
            layout="full"
        )

    # Chapter 19
    with st.expander("Chapter 19 - Arrival of Śuka"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter1/19.1.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(
            text_content=text2,
            layout="full"
        )

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
        text1 = """ 
        Vyāsa ka agla prashna

Sūta ji kehte hain—

Sab sunne ke baad
Vyasa
phir bole—

“Hey Devaṛṣi!
Jab tumhe gyaan dene wale sannyāsī
chale gaye,
toh tumne aage kya kiya?

Apna jeevan kaise jiya?

Aur sharīr ka tyāg kaise hua?

Itna samay beetne par bhi
tumhari smriti kaise bani rahi?”"""
        create_image_text_layout(
            "attached_assets/chapter1/1.6.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Nārada apna jeevan sunāte hain

Narada bole—

“Main us samay
sirf 5 saal ka bachcha tha.

Meri maa
ek gareeb daasi thi.
Main uska
iklauta sahāra tha.

Prem mein bandhi hui maa
chaahte hue bhi
meri raksha nahi kar paayi.

Sab kuch
Bhagavān ki icchā se hota hai—
insaan toh
lakdi ki putli jaisa hai.”

Maa ka virah – bhakti ka dwaar

Nārada bole—

“Ek raat
meri maa gaay ka doodh nikaalne gayi.
Raaste mein
saap ne kaat liya.

Meri maa chali gayi.

Maine ise
Bhagavān ki kripā maana.
Bandhan toot gaya.

Aur main
uttar disha ki taraf
akela chal pada.”

Jungle ka safar

Nārada kehte hain—

Main akela chalta raha—

gaon

shehar

pahaad

nadi

ghane jungle

Beech mein
bhookh, pyaas, thakaan hui.

Ek nadi mein snaan kiya.
Paani piya.
Aur shaant hua.

Pīppal ke ped ke neeche dhyān

Nārada bole—

Ek sunsaan jungle mein
main pīppal ke ped ke neeche baitha.

Jo gyaan
maine santon se suna tha,
usi anusaar
main antar-dhyān mein baith gaya.

Mann Hari ke
charanon mein doob gaya.
Aankhon se aansu behne lage.

Bhagavān ka darshan

Nārada kehte hain—

Us gehre dhyān mein
Krishna
mere hriday mein
dhire-dhire prakat hue.

Rom-rom khada ho gaya.
Main anand ke saagar mein doob gaya.

Par—
agle hi pal
woh roop antardhyaan ho gaya.

Virah aur Bhagavān ki vaani

Nārada bole—

Main udaas ho gaya.
Phir dhyān kiya—
par darshan nahi hue.

Tab ek
gehri, madhur awaaz aayi—

“Is jeevan mein
tum mujhe poori tarah
nahi dekh sakte.

Par prem ke kaaran
maine ek jhalak di.

Tumhara mann
ab mujhmein sthir ho chuka hai.

Agla janm tumhara
mera paarshad hoga.
Aur tumhari smriti
kabhi nasht nahi hogi.”

Jeevan ka antim charan

Nārada kehte hain—

Main dharti par
Hari-naam gaata hua ghoomta raha.

na laalach

na ahankaar

na irshya

Sirf bhakti.

Samay aane par
mrityu bijli ki chamak jaise aayi—
aur sharīr chhoot gaya.

Divya yatra

Nārada bole—

Main Brahmā ke saath
Nārāyaṇa mein lin ho gaya.

Kalp ke ant mein
phir naya sṛṣṭi ka aarambh hua.

Aur main
punah devṛṣi ke roop mein
janma.

Vīṇā aur Hari-kathā

Nārada kehte hain—

Bhagavān ne mujhe
yeh vīṇā di.

Main teenon lokon mein
ghoomta hoon
aur Hari ke leelā-gun gaata hoon.

Jab main gaata hoon—
Bhagavān turant
mere hriday mein prakat hote hain.

Antim updesh

Nārada bole—

“Yog, niyam, kathor sādhanā bhi
mann ko itna shaant nahi karti—
jitna
Kṛṣṇa-seva aur Kṛṣṇa-kathā karti hai.

Yehi
sansār-samudra ko paar karne ki
sabse saral nauka hai 🚣‍♂️”

Samāpan

Nārada ne kaha—

“Vyāsa!
Tumne jo poocha tha,
sab bata diya.

Ab tum
nirbhay hokar
Bhagavān ki mahimā likho.

Yahi
lok-kalyāṇ ka maarg hai ✨”"""
        create_image_text_layout(
            text_content=text2,
            layout="full"
        )

    # Chapter 7
    with st.expander("Chapter 7 - Punishment of Āśvatthāman"):
        text1 = """ 
        Nārada ke jaane ke baad

Shaunaka ne poocha—
“Hey Sūta ji,
Nārada ke updesh ke baad
Vyasa ne kya kiya?”

Vyāsa ka dhyān aur Bhāgavata ka janm

Sūta ji bole—

Sarasvatī nadi ke kinare
Vyāsa ji apne āśram mein baithe.
Pavitra jal ka ācamana kiya.
Aur gehra dhyān lagaya."""
        create_image_text_layout(
            "attached_assets/chapter1/1.7.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Unhone dekha—

Paramātmā

aur uski Māyā

Tab samjhe—
Jīv Māyā ke kaaran
dukh bhogta hai.

Isliye Vyāsa ji ne
Bhāgavata Purāṇa racha—
taaki bhakti se
sabke dukh shānt ho jaayein.

Fir yeh granth
apne putra Shuka ko padhaya.

Yuddh ke baad ka andhera paap

Kurukṣetra yuddh samāpt ho chuka tha.
Duryodhana gira hua tha.

Us raat—
Ashwatthama
ne ek bhayānak paap kiya.

Sote hue
Draupadī ke paanch putron
ka vadh kar diya.

Yeh karm
na veerta tha,
na dharm.

Draupadī ka vilāp

Maa Draupadī toot gayi.
Aansoo rukte nahi the.

Arjuna ne kaha—
“Main tumhare putron ke hatyāre
ko tumhare saamne launga.”

Aur Krishna ko saarthi banaakar
Arjuna nikla
Āśvatthāmā ke peeche.

Brahmāstra ka bhay

Āśvatthāmā bhaagne laga.
Jab koi raasta na bacha—
usne Brahmāstra chala diya.

Aag har disha phail gayi.
Lagaa jaise
Pralaya aa gaya ho.

Arjuna ghabra gaya.
Usne Krishna se kaha—
“Yeh kaunsi bhayānak shakti hai?”

Krishna bole—
“Yeh Brahmāstra hai.
Tum bhi apna astra chalao
aur fir dono ko wāpas lo.”

Arjuna ne
dono astron ko shānt kar diya.

Āśvatthāmā pakda gaya

Fir Arjuna ne
Āśvatthāmā ko pakad liya.
Rassi se baandh diya.

Krishna bole (kathor swar mein)—
“Isne sote hue bachchon ko maara.
Iska vadh hona chahiye.”

Par Arjuna ruk gaya.

Karunā ki jeet – Draupadī

Āśvatthāmā ko
Draupadī ke saamne laaya gaya.

Draupadī ne use dekha—
aur jhuk gayi.

Woh boli—
“Yeh Droṇa-putra hai.
Guru-putra ka apmaan
mujhse nahi hoga.

Iski maa bhi maa hai.
Usse bhi
mere jaise aansoo na milein.”

Yeh sun kar
Yudhishthira,
Nakula, Sahadeva, Sātyaki
sab sahmat hue.

Bhīma ka krodh

Par Bhima bola—
“Isne bachchon ko maara.
Yeh daya ke layak nahi.”

Sabki nazar
Krishna par gayi.

Krishna muskuraaye—
“Dono baatein satya hain.
Brahman-vadh bhi paap hai,
aur is paapi ko dand bhi chahiye.”

Dharm aur nyāy ka santulan

Arjuna samajh gaya.

Usne—

Āśvatthāmā ka sir ka ratna nikaala

Baal kaat diye

Apmaanit karke
use shivir se bahar kar diya

Yeh
Brahman ke liye
sabse bada dand tha.

Antim karm

Fir Pandav aur Draupadī ne
apne putron ka
antim sanskār kiya.

Dukh tha.
Par dharm zinda tha.

Kahani ka saar 🌱

Krodh se paap hota hai

Karunā se dharm chamakta hai

Krishna hamesha
dharm aur nyāy ke beech
santulan sikhate hain"""
        create_image_text_layout(
            text_content=text2,
            layout="full"
        )

    # Chapter 8
    with st.expander("Chapter 8 - Kuntī’s Eulogy of Kṛṣṇa and Yudhiṣṭhira’s Repentance"):
        text1 = """ 
        Gaṅgā tat par śrāddha aur shok

Yuddh ke baad
Pandava
Krishna ke saath
Gaṅgā ke kināre gaye.

Jal-tarpan kiya.
Phir snān.
Par mann abhi bhi bhari tha.

Krishna ne samjhaya—

Kāl (Samay) sab par vijayi hai.
Koi bhi usse nahi bach sakta."""
        create_image_text_layout(
            "attached_assets/chapter1/1.8.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Uttarā aur Brahmaśira ka sankat

Jab Krishna Dvārakā jaane lage,
Uttara
ghabraayi hui daudi aayi.

“Prabhu!
Mujhe nahi,
mere garbh ke shishu ko bachaiye!”

Yeh Āśvatthāmā ka
antim paap tha—
Brahmaśira astra,
jo Kuru-vaṁś ko mitaane ke liye chala.

Krishna ne
Sudarśana Chakra se
garbh ko āvarit kiya.

Astra shaant ho gaya.
Parīkṣit bach gaye.
Kuru-vaṁś zinda raha.

✨ Bhagavān bhakt-rakṣak hain—
garbh mein bhi, pralay ke beech bhi.

Maa Kuntī ka adbhut stavan

Ab Kunti boli.
Yeh sirf prārthanā nahi—
yeh vedānt aur bhakti ka saar hai.

Kuntī ke shabd (saar):

Aap janm-rahit hokar bhi janm lete ho

Aap Māyā ke parde ke peeche chhupe ho

Gyānī bhi aapko poorn roop se nahi jaante

Woh Krishna ko yaad karti hai—

Devakī ke putra

Gopāla, Govinda

Kamalanayan

Hṛṣīkeśa

Sankat-bhakti ka rahasya

Kuntī ke sabse gehre shabd:

“Hey Prabhu,
agar aap hamesha dikhte ho
toh mujhe sankat chahiye.”

Kyun?

Kyōnki:

Sankat mein Bhagavān yaad aate hain

Sukh mein ahankār aa jaata hai

Yeh hai param-bhakti ka rahasya 🌱

Krishna – Leelā aur Tattva

Kuntī kehti hai:

Aap Kāl bhi ho

Aap Sam-darśī ho

Aap kisi ke paksh mein nahi

Sab karmon ka phal nyāy se dete ho

Aur fir ek pyārā smaraṇ—

Yaśodā ka Krishna ko daantna,
rassi se baandhna,
aankhon mein aansu…

Jo Bhaya se pare hai,
wahi bhaya ka abhinay karta hai.

Antim prārthanā

Kuntī ki antim maang:

Mera mann sirf aap mein bahta rahe

Jaise Gaṅgā samundar ki ore

Rishte-naate bhi toot jaayein
agar woh aap se door karein

Yeh poorn vairāgya nahi,
yeh poorn samarpan hai.

Krishna ka muskurana

Krishna muskuraaye.
Aashīrvād diya.
Par jaane lage…

Yudhiṣṭhira ka pashchātāp

Ab Yudhishthira bole—

“Main paapi hoon”

“Mere liye itne log mare”

“Bachche, guru, bandhu—sab gaye”

Unhe lagta hai:

Yuddh ka paap kabhī dhul nahi sakta

Yajña, dān, tapas—sab vyarth

Yeh rājā ka ahankār nahi,
yeh hriday ka pighalna hai.

Is pashchātāp ke baad hi
Bhīṣma-upadeś sambhav hoga
(agla adhyāy).

Is adhyāy ka saar ✨

Bhagavān bhakt-rakṣak hain (garbh tak)

Sankat bhakti ko gehra karta hai

Sukh ahankār laata hai

Sachcha dharm yuddh ke baad shok se guzarata hai

Yudhiṣṭhira ka dukh = adhyātmik pakvata"""
        create_image_text_layout(
            text_content=text2,
            layout="full"
        )

    # Chapter 9
    with st.expander("Chapter 9 - Yudhiṣṭhira’s Acquisition of Kingdom"):
        text1 = """ 
        Yudhiṣṭhira ka bojhil mann

Yuddh jeet chuke the.
Par Yudhishthira ka mann shant nahi tha.

Unhe dar tha—

“Log mujhse narāz na ho jaayein.”

Isliye woh
dharma ka saar jaanna chahte the."""
        create_image_text_layout(
            "attached_assets/chapter1/1.9.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Kurukṣetra ki yātrā

Yudhiṣṭhira
sab bhāiyon ke saath
Kurukṣetra gaye.

Saath mein the:

Krishna

Vyāsa, Nārada, aur kai ṛṣi

Wahan
Bhishma
bāṇon ki shaiyyā par lete hue the.

Bhīṣma ka darśan

Bhīṣma ko dekhkar
sab ne mastak jhukaya.

Bhīṣma jaante the—
yeh jo paas baithe hain,
yeh sādhāraṇ insaan nahi.

Unhone pehchān liya:

“Yeh Krishna hi Nārāyaṇa hain.”

Bhīṣma ka satya-vachan

Bhīṣma bole:

Tum dharm ke putra ho

Tumhare saath Krishna hain

Phir bhi tumhe dukh mila

Kyun?

Kyonki sab kuchh Kāl (Samay) ke adheen hai.

Bhagavān ke irāde
sabse bhi pare hote hain.
Unhe samajhna
sabke bas ki baat nahi.

Rājya ka kartavya

Bhīṣma ne kaha:

“Ab tum rājā ho.
Logon ki rakshā karo.
Yeh bhi Bhagavān ki āgya hai.”

Krishna ko tum
mitra samajhte rahe,
par sach yeh hai—
woh sabke antar-yāmī hain.

Bhīṣma ke antim upadeś

Ab Yudhiṣṭhira ne
dharma par prashn kiye—

Bhīṣma ne bataya:

Rāj-dharm

Dān

Varṇ-āśram-dharm

Pravṛtti aur Nivṛtti

Bhakti-dharm

Yeh sab
sirf pustakon ka gyaan nahi tha—
yeh jeevan ka niyam tha.

Uttarāyaṇ aur yogi-mṛtyu

Jab Uttarāyaṇ aaya,
Bhīṣma ne sharīr chhodne ka nirṇay liya.

Unka mann poori tarah
Krishna mein sthir ho gaya.

Bhīṣma ki bhakti (adarsh drishya)

Bhīṣma Krishna ko yaad karte hain:

Arjun ke sārathi roop mein

Yuddh ke maidan mein

Paseene aur rath ke dhool se bhare hue

Bāṇon se ghaayal, phir bhi prem se bhare

“Wahi Krishna mera āshraya hain.”

Yahi kehkar
Bhīṣma ne
saans tyāg di.

Antim shānti

Aakash se phool barse 🌸
Dev aur ṛṣi stuti karne lage.
Sab shant ho gaye.

Bhīṣma
Brahman mein lin ho gaye.

Rājya-grahan

Antyeshṭi ke baad
Yudhiṣṭhira
Hastināpura laute.

Dhṛtarāṣṭra aur Gāndhārī ko santvana di.
Krishna ki anumati se
Yudhiṣṭhira ne
dharm ke anusaar rājya sambhāla.
Is adhyāy ka saar ✨

Dharm sirf jeet se nahi, dayitva se aata hai

Krishna mitra bhi hain, Nārāyaṇa bhi

Bhakti + Gyaan + Kartavya = sachcha rāj-dharm

Bhīṣma ka maran = adarsh yogi-mṛtyu"""
        create_image_text_layout(
            text_content=text2,
            layout="full"
        )

    # Chapter 10
    with st.expander("Chapter 10 - Kṛṣṇa’s Departure to Dvārakā"):
        text1 = """ 
        Yudhiṣṭhira ka dhārmik rājya

Yuddh ke baad
Yudhishthira
ne rājya sambhāla.

Bhīṣma aur
Krishna
ke upadeś se
unka bhram door ho chuka tha.

Woh Indra jaise
dharm se rāj karte the."""
        create_image_text_layout(
            "attached_assets/chapter1/1.10.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Prakṛti bhi prasann

Yudhiṣṭhira ke rāj mein—

Samay par baarish hoti

Dharti anaj deti

Gaayein doodh se bhari hoti

Nadi, parvat, van sab phalte

Kisi ko
sharīrik ya mānasik peeda nahi thi.

Yeh dharm-rājya tha 🌿

Krishna ka rukna

Krishna ne
Hastināpura mein kuchh samay bitaya—

Mitra ka dukh door karne

Behen Subhadrā ko sukh dene

Phir
prasthān ka samay aa gaya.

Vidāi ka pal 😔

Jab Krishna ne
prasthān ki anumati maangi—

Yudhiṣṭhira ne gale lagaya

Sabki aankhon mein aansu aa gaye

Kuntī, Draupadī, Subhadrā, Uttarā, Gāndhārī
sab vichlit ho gayin.

Achhi sangati chhodna
kabhi aasaan nahi hota.

Alag hona asambhav

Pāṇḍav sochte—

“Jin ke har kaam, har saans,
har bhojan mein Krishna ho,
woh alag kaise rahein?”

Sab
Krishna ko
palak jhapkaye bina dekh rahe the.

Shobhayātrā

Jaise hi Krishna nikle—

Shankh, nagāde, dhol baje

Mahal ki chhaton se phool barse

Kuru-striyan prem se muskurayin

Arjuna
ne Krishna par
safed chhatra dhāra.

Uddhava aur Sātyaki
chaur dhula rahe the.

Krishna
aur bhi tejomay lag rahe the ✨

Nagri ki baatein

Hastināpura ki striyan
aapas mein keh rahi thi—

“Yahi woh Purush hai
jo srishti se pehle bhi tha,
aur pralaya ke baad bhi rahega.”

“Yahi Vedo ka saar hai.”

Unki baatein
sunne walon ka mann shant kar deti thi.

Krishna ka tattva

Wahi Krishna—

Srishti karta hai

Palan karta hai

Laya bhi wahi

Par phir bhi
unse asakt nahi hota.

Jab jab dharm girta hai,
woh roop dharan karte hain.

Dvārakā ki mahimā

Log keh rahe the—

“Dwarka
swarg se bhi sundar hai.”

Wahan ke log
roz Bhagavān ke
muskurate darshan karte hain.

Yudhiṣṭhira ka prem

Yudhiṣṭhira ne
chinta se sena bhejni chahi—

“Kahin Krishna ko
koi kasht na ho.”

Par Krishna ne
sabko samjhaya—

“Ab laut jao.”

Prem se mana karke
woh aage badh gaye.

Yātrā ka varṇan

Krishna ka rath
in deshon se guzra—

Kuru

Panchāl

Matsya

Kurukshetra

Yamunā tat

Van, marusthal

Shaam ke samay
Surya samudra mein doob raha tha 🌅

Aur Krishna
pashchim disha mein
aage badhte gaye.

Is adhyāy ka saar 🌸

Dhārmik rājya se prakṛti bhi khush hoti hai

Bhagavān ka viyog sabse kathin hota hai

Krishna saath na hokar bhi saath hi rehte hain

Dvārakā sirf nagri nahi, Bhagavān ka nivas hai"""
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

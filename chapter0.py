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
    create_image_text_layout("attached_assets/introduction/chapter0.jpg", layout="full")

    text0 = """
    <h2>Introduction: Bhāgavata-Māhātmya (The Glory of Bhāgavata Purāṇa)</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")
    
    # ==================================================
    # Introduction
    # ==================================================
    with st.expander("Introduction"):

        # --------------------------------------------------
        # Part 1
        # --------------------------------------------------
        with st.expander("Part 1 – Bhāgavata Purāṇa with Ten Characteristic Topics"):
            text1 = """ 
            (1) Purāṇa ka matlab

Purāṇa ka matlab hota hai—
bahut purani kahani.
Jo cheezein pracheen kaal se
chali aa rahi hain,
unka record.

Vedo ke time se
Purāṇa aur itihāsa
saath-saath milte hain.
Baad mein inhe
“Paanchva Veda”
bhi kaha gaya.

Purāṇa sirf kahani nahi,
yeh jeevan samajhne ka
ek tarika hai."""
            create_image_text_layout(
                "attached_assets/introduction/0.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            (2) Purāṇa ke 5 mool vishay (Pañca-lakṣaṇa)

Pehle Purāṇon mein
yeh 5 cheezein hoti thi—

Sarga – srishti ki shuruaat

Pratisarga – vinash ke baad phir srishti

Vaṃśa – rajaon ki vanshavali

Manvantara – Manu ke yug

Vaṃśānucarita – Surya aur Chandra vansh ki kathayein

Par samay ke saath
Purāṇa badalte gaye.
Logon ki zarurat ke hisaab se
unmein aur bhi gyaan joda gaya.

(3) 18 Mahāpurāṇa

Samay ke saath
18 bade Purāṇa mashhoor hue—
jaise Viṣṇu, Śiva, Bhāgavata,
Skanda, Padma, Matsya etc.

Inmein se
Bhāgavata Purāṇa
sabse zyada
prem, bhakti aur
mokṣa ki baat karta hai.

Isse kaha gaya—
“Vedo ka pakka hua meetha phal.”

(4) Bhāgavata ke 10 Lakṣaṇa (Daśa-lakṣaṇa)

Bhāgavata Purāṇa ne
Purāṇa ko naye tareeke se
samjhaya—
10 vishesh lakṣaṇon ke saath:

Sarga – sūkṣma srishti

Visarga – sthool srishti

Sthāna – niyam aur vyavastha

Poṣaṇa – bhagwan ki rakṣā

Ūti – karm karne ki ichchha

Manvantara – Manu ke yug

Īśānukathā – bhagwan ki kathayein

Nirodha – vinash

Mukti – bandhan se chhutkara

Āśraya – antim satya (Bhagwan)

Yeh 10 vishay
insaan ko
Bhagwan tak le jaane ke
steps jaise hain.

(5) Skandha aur Lakṣaṇa

Bhāgavata ke
12 Skandha hain.
Har Skandha
kisi ek lakṣaṇa ko
zyaada samjhata hai.

Sabse khaas hai
Skandha X—
jisme Shri Krishna ki
līlāen hain.

Yahi Āśraya hai—
jahan sab kuch
aakar tik jaata hai.

Baaki sab kathayein
isi antim sach tak
le jaane ke liye hain.

(6) Ant mein kya sikh milti hai

Bhāgavata Purāṇa
koi dry textbook nahi.
Yeh ek jeevit granth hai—
jo samay ke saath
badhta gaya.

Ismein thoda repetition hai,
thoda overlap bhi.
Par iska matlab yeh hai ki—
baat dil tak pahunchane ke liye
baar-baar samjhai gayi.

Yeh granth humein
yeh sikhata hai—

✨ Sab gyaan ka antim saar
bhakti, vairagya
aur Bhagwan mein
man lagana hai."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Part 2
        # --------------------------------------------------
        with st.expander("Part 2 – The Date and Authorship of the Bhāgavata Purāṇa"):
            text1 = """ 
            Bhāgavata Purāṇa kab likha gaya?

Iska exact date
aaj bhi clear nahi hai.
Scholars ke beech
kaafi alag-alag opinions hain.

Koi kehta hai
13th century A.D.,
koi 10th century,
aur koi ise
bahut zyada purana maanta hai.

Sach yeh hai—
ek fixed date decide karna mushkil hai."""
            create_image_text_layout(
                "attached_assets/introduction/0.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Purana theory jo galat sabit hui

Kuch scholars ne kaha—
“Kyuki Ramanuja
ne Bhāgavata Purāṇa ka naam nahi liya,
isliye yeh unke baad likha gaya.”

Par yeh baat
galat nikli.

Kyunki—

Madhvacharya
ne Bhāgavata Purāṇa ko
5th Veda maana.

Arab scholar Al Biruni
(11th century)
ne bhi Bhāgavata Purāṇa ka zikr kiya.

Iska matlab—
Bhāgavata Purāṇa
Ramanuja se pehle se exist karta tha.

900 B.C. wali theory kyun galat hai

Kuch log kehte hain—
Bhāgavata Purāṇa
900 B.C. ka hai.

Par problem yeh hai—

Iski language
Vedic Sanskrit se
kaafi modern hai.

Agar Parikshit
900 B.C. mein raaj karte the,
toh granth unse pehle
kaise likha ja sakta hai?

Isliye—
900 B.C. wali date
accept nahi hoti.

Sabse safe conclusion

Ek Jain granth
Nandī Sūtra
(5th century A.D.)
mein Bhāgavata Purāṇa ka
naam milta hai.

Iska matlab—
Bhāgavata Purāṇa
5th century se pehle
zaroor likha ja chuka tha.

Isliye scholars ka maanna hai—
👉 Around 400–600 A.D.
yeh granth
final form mein aaya.

Author kaun tha?

Tradition kehta hai—

Vyasa

Shuka

aur Sūta

Par sach yeh hai—
granthon ko ek hi aadmi
ne ek baar mein nahi likha.

Yeh ek
“epic of growth” hai.

Samay ke saath—

kahaniyan judi

bhakti badhi

teachings deep hoti gayi

Alag-alag Paramparā (Traditions)

Bhāgavata Purāṇa
4 guru-paramparāon ka
mel lagta hai:

Vishnu → Brahma → Narada → Vyasa → Shuka

Narayana → Narada → Vyasa → Shuka

Narayana → Narada → Prahlada

Sankarshana → Maitreya → Vidura

Iska matlab—
yeh granth
collective spiritual effort hai.

South India ka influence

Bhāgavata Purāṇa mein
South India ka
strong effect dikhta hai:

Kaveri, Tamraparni jaise rivers

Dravida desh ka mention

Bhakti ko Dravida bhoomi se joda gaya

Isse lagta hai—
last redaction
South India mein hui.

Bhāgavatism Bhāgavata se bhi purana

Bhāgavata Purāṇa
chahe 400 A.D. ka ho,
par Krishna-bhakti
usse bahut purani hai.

Proof dekho—

Panini (500 B.C.)
ne Vāsudeva-bhakti ka zikr kiya

Heliodorus pillar (2nd century B.C.)
mein Krishna-Vāsudeva ki pooja

Greek historians ne bhi
Krishna worship note ki

Matlab—
Krishna bhakti logon ke dil mein
Bahut pehle se thi.

Final learning 🌱

Bhāgavata Purāṇa—

ek date ka granth nahi

ek author ka granth nahi

Yeh ek jeevit parampara hai.
Jo bhakti, gyaan
aur prem ko
generation se generation
pahunchata raha.

✨ Iska asli mahatva
date nahi,
uska sandesh hai—
Bhagwan se prem."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Part 3
        # --------------------------------------------------
        with st.expander("Part 3 – The Bhāgavata Purāṇa and Pāñcarātra"):
            text1 = """ 
            Pāñcarātra kya hai?

Pāñcarātra
ek ancient Vaiṣṇava system hai.
Yeh 5 main cheezon ka gyaan deta hai:

Tattva – duniya aur brahmaṇḍ ka gyaan

Mukti – liberation

Bhakti – Bhagwan se prem

Yoga – man aur indriyon ka control

Indriya-vishay – senses aur unke objects

Iska naam aaya
Pañcarātra Sattra se—
yaani 5 din ka yagna
jo Nārāyaṇa se joda gaya.

Iska deep idea tha—
Bhagwan apne aap ko
5 roopon mein dikhate hain:
Para, Vyūha, Vibhava, Antaryāmin, Arcā."""
            create_image_text_layout(
                "attached_assets/introduction/0.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Pāñcarātra mein kya-kya hota hai?

Is system mein kaafi practical cheezein thi:

Philosophy

Mantra aur Yantra

Yoga aur sādhana

Mandir banana

Murti-pratiṣṭhā

Grihastha rituals

Varṇāśrama rules

Bade public festivals

Yeh system
logon ke daily jeevan se
directly juda hua tha.

Vedic logon ko Pāñcarātra pasand kyun nahi tha?

Purane Vedic scholars
Pāñcarātra ko
non-Vedic maante the.

Kuch granthon mein toh
inke followers ko
“paapi” tak kaha gaya.

Yahan tak ki
Adi Shankaracharya
ne bhi
Pāñcarātra ke Vyūha-vāda
(para se nikle roop)
ka virodh kiya.

Par Pāñcarātrins ne
shant tareeke se
Purāṇon ke andar
apni baatein ghusa di.

Bhāgavata Purāṇa ka role

Yahin par
Bhāgavata Purāṇa
bahut important ho jaata hai.

Yeh na pure Pāñcarātra jaisa hai,
na pure Vedic jaisa.

Yeh bridge ban gaya.

Isne—

Vyūha-vāda ko
Avatāra-vāda mein badal diya

Tantric worship ko accept kiya

Par sirf murti-pūja ko
highest bhakti nahi maana

Bhāgavata kehte hai—
sirf idol worship se
upar bhi bhakti hoti hai.

Viṣṇu Purāṇa ka impact

Viṣṇu Purāṇa
ek pro-Pāñcarātra granth tha.

Isi se
Bhāgavata Purāṇa ne
kaafi kahaniyan li.

Baad mein
Yamunacharya
aur
Ramanujacharya
ne Pāñcarātra ko
Vedānta ke saath
successfully jod diya.

Dono systems mein main differences

Samajhne ke liye
simple points dekho:

Bhāgavata system
→ Vedic roots
→ Bhagavad Gītā se juda

Pāñcarātra system
→ Āgamic (non-Vedic)
→ Foreigners ke liye bhi open

Bhāgavata mantra:
Om Namo Bhagavate Vāsudevāya

Pāñcarātra mantra:
Om Namo Nārāyaṇāya

Bhāgavata focus:
Avatāra (incarnations)

Pāñcarātra focus:
Vyūha (emanations)

Dono ka milan (Fusion)

Time ke saath—

Vāsudeva-Kṛṣṇa

Viṣṇu

Nārāyaṇa

sab ek hi Bhagwan ke roop ban gaye.

Is fusion ki wajah se—

Mandir-pūja

Yantra

Festivals

Murti-prāṇa-pratiṣṭhā

sab Bhāgavatism ka
hissa ban gaye.

Logon ko yeh
visible aur joyful bhakti
bahut pasand aayi.

Final learning 🌸

Bhāgavata Purāṇa
na sirf ek granth hai,
balki samanvay ka example hai.

Yeh sikhata hai—

Sirf rule important nahi

Sirf ritual bhi kaafi nahi

👉 Prem, bhakti aur gyaan
jab mil jaate hain,
tab dharm jeevit banta hai.

✨ Isliye Bhāgavata Purāṇa
Vedic aur Pāñcarātra—
dono ko jod kar
ek balanced raasta dikhata hai."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Part 4
        # --------------------------------------------------
        with st.expander("Part 4 – The Teaching of the Bhāgavata Purāṇa"):
            text1 = """ 
            Bhāgavata Purāṇa ka nature

Bhāgavata Purāṇa
ek bahut layered granth hai.
Isme kai readings, additions, aur interpretations milte hain.

Isi wajah se
Vedānta ke alag-alag schools
isko apna authority maante hain.

Par is explanation ka base hai—
Śrīdhara Svāmin ki Bhāvārtha Dīpikā
jo sabse purana aur trusted commentary hai."""
            create_image_text_layout(
                "attached_assets/introduction/0.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Do thought streams ka milan

Bhāgavata Purāṇa
do dharaon ko jodta hai:

Vedic stream
– Nasadīya Sūkta
– Puruṣa Sūkta
– Upaniṣads ka Brahman

Āgamic stream
– Pāñcarātra
– Tantra
– Āḻvārs ki bhakti poetry

Last redactor ne
in dono ko
ek hi flow bana diya.

Supreme Reality kya hai?

Bhāgavata Purāṇa kehta hai:

👉 Ek hi Supreme Reality hai
jo:

duniya se andar bhi hai (immanent)

aur duniya se upar bhi hai (transcendent)

Wahi Reality:

duniya ko paida karti hai

wahi chalati hai

aur wahi wapis apne andar sama leti hai

Is Reality ko kaha gaya:

Brahman

Paramātman

Bhagavān

Yeh non-dual consciousness hai.
Koi do nahi—sirf Ek.

Reality ke 4 aspects (simple samjho)
1️⃣ Brahman – Absolute Reality

Shant

Nirvikaar

Nirgun

Beyond description

Yeh sirf existence + bliss hai.
Kuch chahiye nahi.
Sab ka source yahin se hai.

2️⃣ Bhagavān – Blissful Reality

Jab wahi Absolute
apni shakti ke saath khelta hai,
use kehte hain Bhagavān.

Bhāgavata kehta hai:
👉 Kṛṣṇa = Bhagavān himself

Is level par:

Prem hai

Aanand hai

Līlā hai

Yahi Bhāgavata Purāṇa ka heart hai.

3️⃣ Paramātman – Viṣṇu

Yeh woh roop hai
jo har jeev ke andar baitha hai.

Sab ko chalata hai

Sab ko jeevan deta hai

Viṣṇu ka har symbol
(Shankha, Chakra, Kaustubha, Vanamālā)
deep spiritual meaning rakhta hai.

4️⃣ Māyā aur Līlā

Duniya real bhi hai,
par ultimate nahi.

Bhagavān ki Māyā se:

naam

roop

bhed

sab dikhta hai.

Par Bhagavān
hamesha usse upar rehta hai.

Rāsa-līlā ka real meaning

Sabse zyada misunderstood topic.

Bhāgavata clear karta hai:

Rāsa-līlā
👉 historical Kṛṣṇa ka kaam nahi
👉 metaphysical Bhagavān Kṛṣṇa ka līlā hai

Yeh Yoga-Māyā se hui

Yeh sexual act nahi

Yeh spiritual play hai

Message simple hai:

Strong emotion + Bhagavān
= Liberation

Chahe:

prem ho

bhay ho

dwesh ho

bhakti ho

Akhirkaar
sab mokṣa tak jaata hai.

Divine Grace (Anugraha)

Bhāgavata kehta hai:

Bhagavān ko
tumhari pooja ki zarurat nahi.

Par jab tum:

sab mein Bhagavān dekhte ho

sab se maitrī rakhte ho

👉 Grace apne aap behne lagti hai.

Kabhi grace
kasht ke roop mein bhi aati hai,
par bhakta jaanta hai—
yeh bhi daya hai.

Avatāra-vāda (Incarnation)

Bhagavān avatar kyu leta hai?

👉 Līlā ke liye
👉 Dharma ko sambhalne ke liye
👉 Bhakton ke liye

Avatar ka matlab:

Bhagavān niche nahi girta

Woh bas play karta hai

Bhāgavata kehta hai:
👉 Līlā-avatāra sabse shreshṭh hai

Bhakti = Sabse saral raasta

Bhāgavata Purāṇa ka verdict:

Karma karo

Jñāna seekho

Yoga bhi karo

Par final shortcut hai:
👉 Bhakti

Navadhā Bhakti (9 steps)

Bhakti ke 9 simple roop:

Śravaṇa – Sunna

Kīrtana – Naam gāna

Smaraṇa – Yaad karna

Pāda-sevana – Charanon ka sahara

Arcana – Pooja

Vandana – Namaskar

Dāsya – Sevak bhāv

Sakhya – Dost bhāv

Ātma-nivedana – Pura samarpan

Ek bhi kaafi hai.
Sab karna zaroori nahi.

Naam ka mahātva

Bhāgavata bolta hai:

👉 Hari ka naam
agni jaise paap jala deta hai.

jaan-boojhkar

mazaak mein

ya anjaane mein

Naam ka power kaam karta hi hai.

Ajāmila ki kahani
isi baat ka proof hai.

Bhāgavata Dharma kya sikhata hai?

Maitrī (friendliness)

Karuṇā (compassion)

Tyāga (detachment)

Shānti (peace)

Bhakti (love)

Par sabse upar:
👉 Hari-nāma smaraṇa

Final Message 🌸

Bhāgavata Purāṇa
sirf philosophy nahi,
jeevan jeene ka raasta hai.

Bhagavān:

maangta kuch nahi

sirf bulata hai

🎶 Bansuri baj rahi hai…
Bas ek kadam badhao.

“Puri tarah se samarpit ho jao.
Naam lo.
Hari tumhara dukh mita denge.”

🙏"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Part 5
        # --------------------------------------------------
        with st.expander("Part 5 – Commentators on the Bhāgavata Purāṇa"):
            text1 = """ 
            Bhāgavata Purāṇa par itne commentaries kyun?

Bhāgavata Purāṇa
India ka sabse popular aur loved granth hai.

Isliye:

alag-alag Vedānta schools

apni-apni philosophy
Bhāgavata Purāṇa ke through samjhana chahte the.

Is process mein
bahut saare great commentators aaye."""
            create_image_text_layout(
                "attached_assets/introduction/0.5.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Sabse pehle aur sabse mahan: Śrīdhara Svāmin

Sabse purane aur respected commentator the
Śrīdhara Svāmin.

Unki commentary ka naam hai
👉 Bhāvārtha Dīpikā

Yeh Advaita (Śaṅkara school) ko follow karti hai

Simple, clear aur to-the-point hai

Traditional meaning ko faithfully explain karti hai

Log kehte hain:

Vyāsa ne Bhāgavata likha,
Śuka ne sunaya,
par uska poora gehra arth Śrīdhara Svāmin ne samjhaaya.

Bhāvārtha Dīpikā ki special respect

Ek kahani milti hai:

Kāśī ke Bindu-Mādhava Bhagavān

ne Bhāvārtha Dīpikā ko
👉 official aur authentic explanation maana.

Isliye:

baaki schools ke commentators bhi
Śrīdhara Svāmin ko respect dete hain

kai log apni commentary ko
“sirf unki baat ko aur clear karne ke liye”
batate hain.

Caitanya Mahāprabhu ka asar

Caitanya Mahāprabhu ne bhi
Bhāvārtha Dīpikā ko bahut maan diya.

Isi wajah se:

Gauḍīya Vaiṣṇava scholars

apni Radha-bhakti wali explanations ke saath bhi
Śrīdhara Svāmin se argue nahi karte.

Śrīdhara Svāmin ka time maana jaata hai
👉 14th century A.D.

Bhāvārtha Dīpikā ko samjhane wale

Kuch scholars ne
Bhāvārtha Dīpikā ko aur clear banane ke liye
alag commentaries likhi:

Rādhā Ramaṇa Gosvāmī

Unki commentary ka naam: Dīpinī

Gauḍīya touch hai

Par base phir bhi Śrīdhara Svāmin hi hai

Vaṃśīdhara

Radha-cult se jude hue

Bahut scholarly aur detailed work

Mathurā ke scholars ke kehne par likha

Unka bhāv:

“Śrīdhara Svāmin hi asli arth jaante hain.”

Gaṅgā Sahāya

Commentary: Anvitārtha-prakāśikā

Har word, har grammar ko explain karta hai

Students ke liye bahut useful

Viśiṣṭādvaita school ke commentators
Sudarśana Sūri

Short par deep commentary

Rāmānuja tradition ko follow karta hai

Vīrarāghava

Commentary: Bhāgavata Candrikā

Chandni jaisi soft aur clear explanation

Textual details bahut strong

Dvaita school
Vijayadhvaja

Commentary: Padaratnāvalī

Madhva tradition follow karta hai

Grammar aur Purāṇic references se
naye meanings nikaalta hai

X Skandha mein
alag-alag readings bhi record karta hai

Nimbārka school
Śukadeva

Commentary: Siddhānta-pradīpa

Bhāgavata ke through
Nimbārka philosophy samjhata hai

Vallabha aur Puṣṭimārga
Vallabha Ācārya

Commentary: Subodhinī

Pura Bhāgavata cover nahi karti

Par jo karti hai, bahut beautiful karti hai

Founder of Śuddhādvaita aur Puṣṭimārga

Gujarat mein bahut popular

Subodhinī:

padhna ek anand hai

clarity + depth dono milte hain

Baad mein:

Subodhinī-Prakāśa

Bāla-Prabodhinī
jaise easy explainers bhi aaye.

Bengal (Gauḍīya) school
Jīva Gosvāmī

Caitanya Mahāprabhu ke grand-disciple

Commentary:

Krama-Sandarbha

Vaiṣṇavatoṣaṇī (X Skandha)

Unhone:

Gauḍīya Vaiṣṇavism ko
strong Vedāntic base diya.

Radha-Kṛṣṇa bhakti mein
unka kaam bahut gehra hai.

Viśvanātha Cakravartī

Commentary: Sārārtha-darśinī

Jīva Gosvāmī ko follow karta hai

Par language aur explanation
common readers ke liye easy hai

Aur bhi commentators

Translator ne kuch aur bhi commentaries use ki:

Bhakta-manorañjanī
(Svāminārāyaṇa tradition)

Par zyada tar commentators
apni personal life ke baare mein
kam hi likhte hain.

Final simple samjho 🌸

Bhāgavata Purāṇa
ek hi granth hai,
par uske bahut saare darshan hain.

Har commentator:

apni bhakti

apni philosophy
ke rang se usse samjhata hai.

Par sab ka goal ek hi hai:
👉 Bhagavān Kṛṣṇa ko samajhna
aur bhakti ka raasta dikhana 🙏"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


    # ==================================================
    # Bhāgavata-Māhātmya
    # ==================================================
    with st.expander("Bhāgavata-Māhātmya – The Glory of Bhāgavata Purāṇa"):

        # --------------------------------------------------
        # Chapter 1
        # --------------------------------------------------
        with st.expander("Chapter 1 – Nārada Meets Bhakti (Devotion in Human Form)"):
            text1 = """ 
            Is chapter ka core idea

Yeh chapter Bhakti (Devotion) ko ek jeevit strī-rūp mein dikhata hai.
Isme bataya gaya hai ki Kali-yuga mein sab kuch kamzor ho gaya, par Bhāgavata Purāṇa aur Hari-nāma hi asli upāy hain.

Shuruaat: Pranām aur prashna

Sabse pehle Krishna ko pranām—jo Sat–Chit–Ānanda hain aur teenon prakār ke dukh mita dete hain.

Phir Shuka ko vandan—jo bachpan se hi virāgī the.

Naimiśāraṇya mein Shaunaka, Suta se poochte hain:

Kali-yuga mein sabse shreshṭh upāy kya hai?

Bhakti, jñāna aur vairāgya kaise badhein?

Jo seedha Hari tak le jaaye, woh kaunsa raasta?"""
            create_image_text_layout(
                "attached_assets/introduction/0.6.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Sūta ka uttar (seedha aur saaf)

Bhāgavata Purāṇa Kali-yuga ka amogh upāy hai.

Isko sunne–padhne se man shuddh hota hai aur Vaikuṇṭha milta hai.

Devtāon ne amṛt laaya, par Bhāgavata-kathā amṛt se bhi zyada pavitra hai.

Parikshit ne sirf Bhāgavata sun-kar mokṣa paaya—yeh dekhkar Brahma bhi chakit hue.

Nārada ka prasang (main kahani)

Narada dharti par ghoomte hue dukhi hote hain:

Kali-yuga mein satya, dayā, tapasya kam ho gaye.

Log pet bharne ke liye jhooth bolte hain.

Sanyāsī bhi ghar–sampatti mein uljhe hain.

Teerth aur āśramon ki pavitrata ghatti ja rahi hai.

Yamunā ke kināre, Vṛndāvana ke paas, Nārada ek yuvati ko rote dekhte hain—

Do boodhe puruṣ uske paas behosh pade hain.

Kai nadi-deviyān use sewa de rahi hain.

Sachchai ka khulāsa

Yuvati bolti hai:

“Main Bhakti hoon.”

Mere do putra: Jñāna aur Vairāgya—Kali-yuga mein boodhe aur thake ho gaye.

Main Drāviḍa desh mein paida hui, Karnataka mein badi hui; Gujarat tak aate-aate kamzor ho gayi.

Vṛndāvana aate hi main phir yuvā ho gayi—par mere putra abhi bhi thake hue hain.

Nārada ka gyaan (why Kali-yuga?)

Nārada samjhate hain:

Krishna ke prithvī chhodne ke baad Kali-yuga aaya.

Parikshit ne Kali ko isliye jeene diya kyunki:

Isi yug mein Hari-nāma se woh phal milta hai jo anya yugo mein kathin sādhanā se bhi nahi milta.

Kali-yuga ki khaas baat:

Naam–kīrtan sabse shaktishāli upāy hai.

Sab kuch kamzor kyun lagta hai?

Teerth, tapasya, dhyān—sab apni tākat kho rahe hain kyunki:

Laalach, dikhāva, adharma badh gaye.

Par dosh kisi vyakti ka nahi—yug ka swabhāv hai.

Antaryāmī Hari phir bhi sahansheel bane rehte hain.

Ant mein Bhakti ka vandan

Bhakti, Nārada ko pranām karti hai:

Aap jaise santon ka darshan hi uddhār hai.

Prahlāda aur Dhruva—Hari-nāma aur kripā se tar gaye—yeh sab Aapke margdarshan ka phal hai.

One-line takeaway 🌼

Kali-yuga mein sabse seedha, sabse shaktishāli raasta:
👉 Bhāgavata-sravaṇ aur Hari-nāma-kīrtan—isi se Bhakti jawaan hoti hai, aur mokṣa milta hai 🙏"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Chapter 2
        # --------------------------------------------------
        with st.expander("Chapter 2 – Conversation between Nārada and the Kumaras"):
            text1 = """ 
            Chapter ka mool sandesh

Is adhyāya mein yeh spaṣṭ hota hai ki Kali-yuga ka ek hi pakka upāy hai—Śrīmad Bhāgavata Purāṇa ka śravaṇ (sunna) aur kīrtan.
Yahi Bhakti ko majbūt karta hai, aur uske saath Jñāna aur Vairāgya ko phir se jeevit karta hai.

Nārada ka upadeś Bhakti ko

Narada Bhakti se kehte hain:

Chinta chhod do—Krishna kahin gaye nahi hain.

Jo Draupadī ki rakṣā kar sakta hai, woh Bhakti ko kabhi nahi chhodta.

Pehle yugon mein jñāna + vairāgya se mokṣa milta tha,
par Kali-yuga mein sirf Bhakti hi kaafi hai.

Bhagavān ne Bhakti ko apni priya shakti banaya:

Mukti ko uski sevika,

Jñāna aur Vairāgya ko uske putra banaya."""
            create_image_text_layout(
                "attached_assets/introduction/0.7.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Problem: Jñāna aur Vairāgya kyun nahi jaag rahe?

Kali-yuga ke prabhāv se Jñāna aur Vairāgya bujh gaye, thak gaye.

Vedoṃ, Upaniṣadoṃ aur Bhagavad-Gītā ke pāṭh se bhi woh poori tarah jag nahi pa rahe.

Nārada chintit hote hain aur Bhagavān Viṣṇu ko smaran karte hain.
Aakashvānī hoti hai:

“Sant log tumhe sahi upāy batāenge.”

Badarikāśrama mein Kumāroṃ se milan

Nārada ko Sanaka, Sanandana, Sanātana, Sanat-kumāra (sāmūhik rūp se Kumāra) milte hain—
yeh hameshā yuvā rehte hain, kyunki Hari-nāma mein hi jeete hain.

Nārada poochte hain:

Bhakti, Jñāna aur Vairāgya ko kaise punarjīvit kiya jaaye?

Woh kaunsa karm hai jo sab kuch theek kar de?

Kumāroṃ ka final nishkarṣ (Golden Answer)

Kumāra kehte hain:

🔑 Upāy sirf ek hai

👉 Śrīmad Bhāgavata Purāṇa ka śravaṇ aur pāṭh

Yeh Vedoṃ aur Upaniṣadoṃ ka sar (essence) hai,
jaise:

doodh se nikla ghee,

gannā se nikli shakkar,

vrikṣ se pakka phal.

Veda gyaan dete hain,
Bhāgavata gyaan ko rasa aur anubhav bana deta hai.

Isi Bhāgavata ne:

Vyasa ke man ka dukh mitaya,

Bhakti ko majbūt kiya,

Jñāna aur Vairāgya ko phir se shakti di.

Antim saar (Takeaway 🌼)

Kali-yuga mein:

Yagya, tapasya, kathin yoga mushkil hain,

Par Bhāgavata-kathā sabke liye saral aur prabhāvi hai.

Jahan Bhāgavata ka śabda goonjta hai,

wahan Kali ke dosh bhaag jaate hain,

Bhakti ghar-ghar phail jaati hai,

aur mokṣa ka raasta khul jaata hai 🙏"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Chapter 3
        # --------------------------------------------------
        with st.expander("Chapter 3 – Removal of Bhakti’s Miseries"):
            text1 = """ 
            Chapter ka mool bhaav

Is adhyāya mein yeh saakshāt roop se pramāṇit hota hai ki
👉 Śrīmad Bhāgavata Purāṇa ka śravaṇ (Bhāgavata-saptāh)
hi Kali-yuga mein Bhakti ke sab dukh mitaane, aur Jñāna–Vairāgya ko punarjīvit karne ka ekmātra upāy hai।

Nārada ka sankalp (Jñāna-Yajña)

Narada kehte hain:

Main Śuka-pranīt Bhāgavata ka pāṭh karke
Bhakti, Jñāna aur Vairāgya ko sthāpit karūṅgā.

Yeh ek Jñāna-yajña hai—agni nahi, śabda aur rasa se hone wala yajña."""
            create_image_text_layout(
                "attached_assets/introduction/0.8.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Kumāroṃ ka nirdesh: Sthān aur vidhi

Sanaka aur anya Kumār batāte hain:

📍 Sthān

Gaṅgādvāra (Haridvār) ke paas Ānanda nāmak sthān,
jahan:

ṛṣiyoṅ aur devatāoṅ ka vāsa hai,

vair-bhaav nahi,

Bhāgavata kathā svataḥ hi madhur aur rasamay ho jaati hai.

📜 Phal

Jahan Bhāgavata kathā hoti hai:

Bhakti swayam aati hai,

Jñāna aur Vairāgya uske saath jaagte hain,

teeno nava-yuvā ho jaate hain.

Divya sabhā ka varṇan

Gaṅgā ke tat par:

Mahāṛṣi (Vyāsa, Vasiṣṭha, Viśvāmitra, Mārkaṇḍeya, Dattātreya),

Veda–Upaniṣad,

Purāṇa, Darśan,

Nadiyāṅ, Parvat, Devatā,
sab ekatr hote hain 🌺

Har taraf:

“Jaya! Jaya!”

śaṅkha-nāda,

puṣp-varṣā.

Bhāgavata Purāṇa ki Mahimā (Core Teaching)

Kumāra kehte hain:

Bhāgavata = Vedoṅ ka saar
(jaise doodh se ghee, gannā se shakkar)

18,000 śloka, 12 skandh,

Parīkṣit–Śuka samvād ka amṛt.

🔑 Mahattvapūrṇ ghoṣṇā:

Ghar jahan Bhāgavata hota hai → tīrth ban jaata hai

Hazāroṅ yajñ aur tapasya
→ Bhāgavata-śravaṇ ke 1/16 ke barābar bhi nahi.

Mrityu-kāl mein Bhāgavata ka ek vākya sun liya → Vaikuṇṭha nishchit.

Kyun Saptāh (7 din)?

Kumāra spasht karte hain:

Kali-yuga mein:

man chanchal hai,

āyu chhoti hai,

niyam kathin hain.

Isliye 7 din ka Bhāgavata-śravaṇ
→ pūre jeevan ke śravaṇ ka phal deta hai.

👉 Bhāgavata-Saptāh:

yajñ se shreshṭh,

tapasya se uttam,

yoga se upar,

tīrth se bhi shreshṭh.

Uddhava–Kṛṣṇa sambandh: Antim rahasya

Uddhava ne Krishna se kaha:

“Aap jaa rahe ho, Kali aa rahi hai—bhaktoṅ ka kya hoga?”

Bhagavān ka uttar (tatva):

Main apni poori shakti aur chetanā
👉 Bhāgavata Purāṇa mein sthāpit kar deta hoon.

Ab Bhāgavata hi Hari ka śabda-rūp hai.

Isliye:

Sunna, padhna, dekhna bhi → paap-nāśak.

Chamatkār: Bhakti ka punarjanm

Kathā ke madhya:

Bhakti prakat hoti hai ✨

Uske saath:

Jñāna aur Vairāgya,

yuvā, tejasvī, Hari-nāma ucharan karte hue.

Bhakti ka vachan:

“Main bhaktoṅ ke hriday mein vaas karūṅgī.”

Aur turant:

Bhakti Hari-bhaktoṅ ke hriday mein sthit ho jaati hai 💛

Antim saar (Ultimate Takeaway 🌼)

Kali-yuga ka ekmātra dharma:
👉 Śrīmad Bhāgavata Purāṇa ka śravaṇ

Yahi:

Bhakti ko jeevit karta hai,

Jñāna–Vairāgya ko majbūt karta hai,

aur bhakta ko Hari se ek kar deta hai।

“Bhāgavata ko sunne wala aur sunāne wala—
dono Kṛṣṇa ko praapt karte hain.”"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Chapter 4
        # --------------------------------------------------
        with st.expander("Chapter 4 – Salvation of Brāhmaṇa Ātmadeva"):
            text1 = """ 
            Bhagavān ka avtaran (Divine Presence)

Bhaktoṅ ke hriday mein jab asādhāraṇ Bhakti jagi, tab
Krishna swayam Vaikuṇṭha chhodkar
unke shuddh hriday mein vaas karne lage 💛

Shyām varṇ, peet-vastra,

gale mein van-mālā,

haath mein bansuri,

Kaustubha mani se alankrit.

Sab log ānand mein doob gaye, apna tan-man bhool gaye।

Narada bole:
👉 “Kali-yuga mein Bhāgavata-saptāh jaisa pavitra koi upāy nahi.”"""
            create_image_text_layout(
                "attached_assets/introduction/0.9.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Ātmadeva ki Kahani (Mool Katha)
🌿 Ek nagar, ek Brāhmaṇa

Tuṅgabhadrā nadi ke kināre ek nagar tha.
Wahan rehta tha Ātmadeva –

Vedoṅ ka gyātā,

dharmic, daani,

par santān-hīn.

Uski patni Dhundhulī:

sundar thi,

par ziddi, chugalkhor aur chalāk bhi.

Donoṅ ne bahut daan–punya kiya,
par santān nahi hui 😔

Van mein milan: Sannyāsī ka var

Dukh se bhare Ātmadeva van gaye.
Wahan ek yogī-sannyāsī mile.

Sannyāsī ne kaha:

“Agale 7 janmoṅ tak tumhe santān nahi milegi.”

Par Ātmadeva ne zidd ki 😢
Ant mein yogī ne ek phal diya:

Patni agar vrat rakhe aur phal khaye,
to putra hoga.

Dhundhulī ka chhal (Deceit)

Dhundhulī ne:

phal khaya nahi,

behen ko de diya,

aur gaay ko bhi phal khilaya 🐄

Natija:

Behen ke ghar se ek balak aaya → Dhundhukārī

Gaay se ek divya balak janma → Gokarṇa

Do bhai – bilkul vipreet
🌼 Gokarṇa

shaant,

gyānī,

Bhāgavata ka premi,

dharm aur Bhakti se bhara.

🔥 Dhundhukārī

atyant pāpi,

chor, hinsaak,

vyabhichārī,

maata-pita ko peetne wala 😨

Usne:

saari sampatti uda di,

ghar barbaad kar diya.

Ātmadeva toot gaye…
“Putra-hīntā behtar thi, par aisa beta nahi!”

Gokarṇa ka updesh (Turning Point)

Gokarṇa ne pita se kaha:

“Yeh sansār asaar hai.”

“Putra aur dhan par moh narak deta hai.”

“Hari-kathā hi sachcha amṛt hai.”

Ātmadeva ka hriday badal gaya 💫

Antim badlav: Bhāgavata ka prabhāv

60 saal ke baad:

Ātmadeva ne ghar chhod diya,

van mein gaye,

Bhāgavata Purāṇa ka nitya pāṭh kiya,

visheshkar 10va Skandha 📖

👉 Dheere-dheere:

moh toot gaya,

man shuddh hua,

aur ant mein Kṛṣṇa se aikya (mokṣa) prāpt hua 🕉️

Chapter ka Saar (Core Moral 🌱)

Janm se nahi, sanskār se mahan bante hain.

Ziddi icchā vināś laati hai.

Bhāgavata Purāṇa:

pāpi ko bhi shuddh karta hai,

grihasth ko vairāgya deta hai,

aur ant mein mokṣa deta hai.

“Bhāgavata ki kathā sunne se
bhakti jagti hai,
aur bhakti se Hari milte hain.”"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Chapter 5
        # --------------------------------------------------
        with st.expander("Chapter 5 – Gokarṇa Attains Goloka"):
            text1 = """ 
            Dhundhukārī ka patan

Pita ke van jaane ke baad, Dhundhukārī aur bhi nirdayi ho gaya 😔
Usne apni maa ko itna sataya ki
maa kuaan mein kood kar apni jaan de baithi.

Yeh paap ka phal tha.

Gokarṇa ka jeevan

Gokarṇa yog aur Bhakti mein sthir the.
Woh tirth-yatra par nikal gaye.
Unke mann mein na shatru tha, na mitra.
Sirf Hari ka smaran tha 🌸"""
            create_image_text_layout(
                "attached_assets/introduction/0.10.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Dhundhukārī ka bhayankar ant

Dhundhukārī galat sangat mein pada.
Chori, paap, lobh – sab badh gaya.

Ant mein:

veśhyāon ne use maar diya,

aur woh pret (bhūt) ban gaya 👻

Na bhookh shaant,
na pyaas bujhi,
na kahin shanti.

Bhaiyon ka milan

Ek raat, pret-roop mein Dhundhukārī
Gokarṇa ke saamne aaya.

Woh bhayankar roop badalta raha –
kabhi haathi, kabhi bhains, kabhi agni 🔥

Gokarṇa ne jal chhidka,
aur bhūt bol utha:

“Main tumhara bhai hoon…
apne paapon se is haal mein hoon.
Mujhe bachao 🙏”

Shrāddh bhi asafal

Gokarṇa ne:

Gayā mein Shrāddh kiya,

bahut upaay kiye,

par mokṣa nahi mila.

Tab Surya Dev ki aakashvaani hui ☀️:

“Iska uddhār Śrīmad Bhāgavata se hoga.”

Bhāgavata Saptāh

Gokarṇa ne 7 din Bhāgavata kathā shuru ki 📖
Sab log aaye –
buddhe, bimar, andhe, garib… sab.

Pret Dhundhukārī
7 gāanth wali baans mein jaakar baith gaya.

Har din:

ek gāanth toot-ti,

paap dheere-dheere jalte gaye 🔥

Saatve din:
👉 saari gāanth toot gayi
👉 bhūt ka sharir chhoot gaya
👉 woh divya roop mein badal gaya ✨

Mokṣa aur Vaikuṇṭha

Ab Dhundhukārī:

peela vastra,

tulsi mala,

divya tej ke saath
Vaikuṇṭha rath par chadh gaya 🚩

Usne kaha:

“Bhāgavata kathā
sabse bada uddhār hai.”

Gokarṇa ka Goloka gaman

Agli Bhāgavata Saptāh ke baad,
Krishna swayam prakat hue 💙

Shankh baja,

Gokarṇa ko gale lagaya,

aur bole:

“Tum mere ho.”

Gokarṇa ko Goloka le jaaya gaya 🌼
Gaon ke log, pashu, yahan tak ki chāṇḍāl bhi
sab par kripa hui 🙌

Is Adhyay ka Saar (Moral 🌱)

Paap kitna bhi bada ho, Bhāgavata use jala deti hai.

Sirf sunna nahi, shraddha se sunna zaroori hai.

Bhakti se Hari bandhte hain.

Bhāgavata kathā = mokṣa ka saral raasta.

“Jo Bhāgavata ko hriday se sunta hai,
woh dobara saṃsār mein nahi aata.” 🌸"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Chapter 6
        # --------------------------------------------------
        with st.expander("Chapter 6 – Procedure of Listening to the Bhāgavata"):
            text1 = """ 
            Bhāgavata sunna ek pavitra yatra hai

Rishiyon ne kaha 🌼
Bhāgavata sunna sirf baithkar sunna nahi hota.
Yeh mann, sharir aur bhav – teenon ka safar hota hai.

Isliye iski vidhi (rules) batayi gayi.

Shubh taiyari

Bhāgavata shuru karne se pehle:

shubh din aur samay dekha jata hai

ghar aur jagah saaf aur pavitra ki jati hai

sab logon ko prem se nimantran diya jata hai 💌

Ameer–garib, purush–stree, sab ko bulaya jata hai.
Kyuki Hari ki kathā sabke liye hoti hai."""
            create_image_text_layout(
                "attached_assets/introduction/0.11.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Jagah aur vyavastha

Bhāgavata:

mandir mein,

ghar mein,

ya ped–paudhon ke beech bhi ho sakti hai 🌳

Ek sundar pandal banta hai.
Beech mein Bhāgavata granth ko samman ke saath rakha jata hai 📖✨

Kathā kehne wala kaisa ho?

Kathā sunane wala:

lalach se door ho

Vishnu-bhakt ho

shant aur gyaan se bhara ho

Jo khud bhramit ho,
woh Bhāgavata nahi suna sakta ❌

Sunne wale ka bhav

Sunne wala:

chinta chhod deta hai

mann ko shant rakhta hai

poori shraddha se sunta hai 🙏

Rishiyon ne kaha:

“Zyada upvaas se zyada zaroori hai dhyaan se sunna.”

Agar bhookh dhyaan todti hai,
to halka bhojan bhi chalega 🍎🥛

Saat din ki kathā

Roz kathā hoti hai.
Beech mein:

Hari ka naam,

bhajan,

kirtan 🎶

Saat din mein:

mann halka ho jata hai

paap dheere-dheere jalne lagte hain 🔥

Acharan (behaviour)

Bhāgavata sunte samay:

gussa, ghamand, irshya chhod do

sach, daya, namrata apnao 🌸

kisi ki burai mat karo

Yahi sachchi Bhakti hai.

Ant ka anand

Jab Bhāgavata poori hoti hai:

Bhakti,

Jñāna,

aur Vairāgya
phir se yuva aur tej se bhare dikhte hain ✨

Sab milkar:

kirtan karte hain

Hari ka naam lete hain

prem mein doob jate hain 💙

Nārada ka anubhav

Nārada ji ke netron mein aansu aa gaye 😌
Unhone kaha:

“Bhāgavata sunna
sabse bada dharm hai.”

Tabhi Krishna swayam prakat hue
aur bole:

“Jahan Bhāgavata hoti hai,
main wahan avashya hota hoon.”

Is Adhyay ka Saar (Moral 🌱)

Bhāgavata sirf granth nahi, Hari ka swaroop hai

Sunna tabhi safal hota hai jab shraddha ho

Bhakti se mann shuddh hota hai

Bhāgavata = Kali yug ka sabse saral raasta

“Jo Bhāgavata sunta hai,
uske hriday mein Hari swayam baste hain.” 🌼"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

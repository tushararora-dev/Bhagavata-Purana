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
    create_image_text_layout("attached_assets/chapter2/chapter2.jpg", layout="full")

    text0 = """
    <h2>Book 2 - Second Skandha</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")

    # Chapter 1
    with st.expander("Chapter 1 - The Discourse of Śuka—Description of the Cosmic Form of the Lord"):
        text1 = """ 
        “Oh King Parīkṣit,
tumhara sawaal bahut hi khaas hai.
Yeh sawaal sirf tumhare liye nahi,
poori duniya ke bhale ke liye hai.”

Śuka bole:
“Log hazaar baatein sunte hain.
Par zyadaatar baatein unke liye hoti hain
jo ghar-grihasthi aur moh mein phanse rehte hain.”

Raat jaati hai neend aur kaamna mein,
Din jaata hai paisa aur zimmedaari ke peeche.
Is tarah, zindagi chupchaap nikal jaati hai."""
        create_image_text_layout(
            "attached_assets/chapter2/2.1.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Insaan
apne sharir, parivaar, bachchon se chipak jaata hai.
Woh sach nahi dekhta,
chahe roz kisi ko marte hue hi kyun na dekhe.

Isliye, Śuka ne kaha:
“Jo bhi dar se mukt hona chahta hai,
use Hari (Bhagwān) ko
sunna chahiye,
unka gun-gaan karna chahiye,
aur unka smaran karna chahiye.”

“Ant samay par Nārāyaṇa ka smaran
insaan ki zindagi ki sabse badi safalta hai.”

Chahe koi
Gyaan, Yoga, ya Kartavya ke raaste se aaye—
ant mein sabka saar Hari hi hai.

Śuka muskura kar bole:
“Yeh baat sab jaante hain—
jo mahaan rishi nirgun Brahman mein bhi lage rehte hain,
unhe bhi Hari ki leela sunna pasand hota hai.”

Phir Śuka ne kaha:
“Mainne yeh Bhāgavata Purāṇa
apne pita se padha tha.
Main toh nirgun dhyaan mein tha,
par Bhagwān ki leelaon ne mera mann kheench liya.”

“King Parīkṣit,
main tumhe yeh katha isliye sunaunga
kyunki tum sachche bhakt ho.
Isse nishkaam bhakti turant janam leti hai.”

Śuka ne spasht kaha:
“Hari ka naam hi
mokṣ ka sabse asaan raasta hai.”

“Lambi zindagi ka kya fayda,
agar woh andhere mein guzar jaaye?”

“48 minute ka jeevan bhi kaafi hai,
agar usmein Bhagwān ka smaran ho.”

Unhone ek kahaani sunayi:
“King Khaṭvāṅga ko pata chala
ki unke paas sirf ek muhūrt bacha hai.
Unhone sab chhod diya
aur Hari ko pakad liya.
Wahi unki jeet thi.”

Śuka bole:
“Tumhare paas 7 din hain.
Inhe vyarth mat jaane do.”

“Ant samay par,
insaan ko apna darr chhodna chahiye.
Sharir aur sukh se alag hona chahiye.”

“Ghar chhod kar,
pavitra sthaan par,
shaant mann se baitho.”

OM ka smaran karo.
Saans ko shaant karo.
Mann ko vash mein lao.

“Jab mann bhatakne lage,
use Bhagwān ke roop par tikao.”

“Unke charan, mukh, ya kisi ek ang par dhyaan lagao.”

“Dheere-dheere,
rajas aur tamas kam ho jaayenge.
Mann pavitra ho jaayega.”

Aur jab bhakti jud jaati hai,
toh Yoga bhi asaan ho jaata hai.

🌼 Saar (Moral of the Story)

Zindagi lambi nahi, sahi honi chahiye

Ant samay ka smaran hi asli pariksha hai

Hari ka naam sabse seedha raasta hai

Mann ko ek hi satya par tikana seekho

Bhakti se hi shanti aur mukti milti hai"""
        create_image_text_layout(
            text_content=text2,
            layout="full"
        )

    # Chapter 2
    with st.expander("Chapter 2 - Liberation by the Yogic Path: Instantaneous and Gradual Liberation"):
        text1 = """ 
        🌼 Chapter 2 – Yogic Path se Mukti (Hinglish Kahani Style)

(Instant aur Gradual Liberation – Simple, Moral, Story Tone)

Śrī Śuka bole:

“King Parīkṣit,
jab sahi dhāraṇā hoti hai,
toh Hari ki kripa se
sab kuchh yaad aa jaata hai.”

Isi kripa se Brahmā ji ne bhi
pralaya ke baad apni bhooli hui smriti paayi
aur duniya ko phir se rach diya."""
        create_image_text_layout(
            "attached_assets/chapter2/2.2.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Par Śuka ne samjhaya:

“Sirf shabdon ke peeche bhaagna,
sirf swarg ke sapne dekhna—
yeh sab Māyā hai.”

Jaise sapne me insaan khushi dekhta hai
par subah uthte hi sab gayab,
waise hi karm ke falon ke peeche bhaagna
asli ānand nahi deta.

Isliye buddhimaan insaan kya karta hai?

Woh sirf utna hi leta hai
jitna jeene ke liye zaroori ho.
Usse chipakta nahi.
Aur jab samajh jaata hai
ki yeh sab bekaar mehnat hai,
toh woh peeche hat jaata hai.

Śuka muskura kar bole:

“Jab dharti hai,
toh bistar kyun chahiye?
Haath hain,
toh takiya kyun?

Ped phal dete hain,
nadiyaan paani deti hain,
gufaayein aashray deti hain.

Toh phir abhimaani ameer logon
ki seva kyun?”

Jis din insaan ko sach ka bodh ho jaata hai,
us din woh apne hi hriday mein
rehne wale Ātman ka dhyaan karta hai.

Wahi Ātman
Hari hai—
amar, pyaara aur satya.

Yahin se ajnān ka ant hota hai
aur mukti ka raasta khulta hai.

Śuka ne kaha:

“Jo log sansaar ki dukh bhari nadi
(Vaitaraṇī) me doob rahe hain,
unhe dekh kar bhi
agar koi Bhagwān ka dhyaan na kare,
toh usse bada murkh kaun?”

Kuchh yogi
apne hriday ke andar
chaar bhujaon wale Hari ka dhyaan karte hain—
shankh, chakra, gada aur kamal ke saath.

Jab tak mann shaant rahe,
tab tak usi roop ko dekho.

Śuka ne Hari ka roop bataya:

Badi-badi kamal jaisi aankhein,
peele vastra,
ratno se chamakte gehne,
vanmala,
aur pyaari si muskaan.

Unki muskaan hi
bhakton ko bharosa deti hai
ki “Main hoon.”

Dhyaan ka tareeqa simple hai:

Pehle charanon par dhyaan

Phir dheere-dheere upar

Aur ant mein muskurate chehre par

Jitna mann pavitra hota jaaye,
utna hi dhyaan gehra hota jaata hai.

Jab tak prem bhari bhakti na aaye,
tab tak roz apna kartavya karke
Bhagwān ke virāṭ roop ka dhyaan karo.

Ant samay ke liye Śuka ne kaha:

“Jab jeevan chhodna ho,
toh na samay dekho,
na jagah.”

Bas shaant baitho,
saans sambhalo,
aur mann ko poori tarah
Paramātmā mein mila do.

Us sthiti mein:

Kaal ka koi zor nahi

Devta bhi prabhavi nahi

Na sukh, na dukh

Sirf shuddh shanti

Kuchh yogi
dheere-dheere upar jaate hain
(chakron ke maarg se),
aur kuchh seedha
Paramātmā mein mil jaate hain.

Yeh dono raaste
Vedo mein bataye gaye hain.

Śuka ne ant mein kaha:

“Is sansaar mein
sabse pavitra aur seedha raasta
Vāsudeva ki bhakti hai.”

Brahmā ji ne bhi
Vedo ko teen baar padhkar
yahi nishchay kiya
ki prem bhari bhakti hi saar hai.

🌸 Kahani ka Saar (Moral)

Sirf bhog aur sapne asli khushi nahi dete

Zarurat bhar lo, lalach mat rakho

Hari har jagah, har samay maujood hain

Bhakti + Dhyaan = Mukti

Ant mein yaad wahi aata hai
jisse humne sach mein prem kiya"""
        create_image_text_layout(
            text_content=text2,
            layout="full"
        )

    # Chapter 3
    with st.expander("Chapter 3 - Devotion to Hari—the only path of Liberation"):
        text1 = """ 
        🌼 Chapter 3 – Hari ki Bhakti: Mukti ka Ekmatra Raasta

(Hinglish Kahani Style • Short • Simple • Moral Tone)

Śrī Śuka bole:

“King Parīkṣit,
jo raasta maine tumhe bataya,
yeh sirf tumhare liye nahi,
balki un sab ke liye hai
jo samajhdaar hain
aur khaaskar unke liye
jo jeevan ke ant ke kareeb hain.”"""
        create_image_text_layout(
            "attached_assets/chapter2/2.3.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Phir Śuka ne ek gehri baat kahi:

“Insaan jo chahe,
uske hisaab se devta poojta hai.”

Gyaan chahiye? → Brahmā ki pooja

Indriyon ki shakti? → Indra ki pooja

Santaan? → Prajāpati

Dhan-sampatti? → Māyā (Durgā)

Tej aur roshni? → Agni

Bal aur shakti? → Rudra

Sabki apni-apni ichchha,
aur uske hisaab se pooja.

Kisi ko achha roop chahiye,
kisi ko sundar jeevan saathi,
kisi ko raaj,
kisi ko naam aur shohrat.

Sab alag-alag cheezein maangte hain.

Par Śuka ne shant swar mein kaha:

“Par jo insaan
sab ichchhaon se mukti chahta hai,
use kisi chhote devta ki nahi,
Pūrṇ Purush – Hari ki bhakti karni chahiye.”

Phir unhone ek aur gehri baat boli:

“Chaaho tum:

kuchh bhi na chahna

sab kuchh chahna

ya seedhi mukti chahna

Teeno ke liye
ek hi raasta hai—
Hari ki nishkaam bhakti.”

Śuka bole:

“Dusre devta denge
sirf seemit phal.
Par Hari ke bhakt
tumhe woh sangat dete hain
jahan se atal bhakti paida hoti hai.”

Aur wahi bhakti
aakhirkaar
moksha ban jaati hai.

Phir unhone kaha:

“Kya koi aisa ho sakta hai
jo ek baar Hari ki kathaa sun le
aur phir use prem na ho?”

Hari ki kathaa:

mann ko shaant karti hai

vasnaon ko dheere-dheere mita deti hai

vairagya paida karti hai

aur bhakti ko janm deti hai

Aur wahi bhakti
is lok aur parlok dono mein
mukti ban jaati hai.

Yahan Śaunaka rishi bole:

“Hey Sūta ji,
itna sab sunne ke baad
king Parīkṣit ne
phir kya poocha?”

“Hum bhakton ki sabha mein
jo baat hogi,
woh Hari ki hi hogi.”

Śaunaka bole:

“Jis jeevan mein
Kṛṣṇa ki baatein nahi,
woh jeevan jaise bekaar beh jaata hai.”

Suraj ugta hai,
suraj dhoobta hai,
aur jeevan dheere-dheere khatam ho jaata hai—
siwaay us samay ke
jo Kṛṣṇa-kathaa mein laga ho.

Phir bahut kathor par sach baat kahi:

“Ped bhi jeete hain.
Bhains bhi khati-peeti hai.
Janwar bhi bhog karte hain.”

“Toh agar insaan ne
Kṛṣṇa ka naam hi nahi suna,
toh usme aur jaanwar mein
farq kya?”

Jis kaan ne Hari ki kathaa nahi suni → khaali gaddhe

Jis jeebh ne Kṛṣṇa ka naam nahi liya → medhak jaisi

Jo sir Mukunda ko nahi jhuka → bojh

Jo haath Hari ki pooja na kare → laash ke haath

Aankhen jo Viṣṇu ko na dekhein,
woh mor ke pankh ke daag jaise.

Paon jo Viṣṇu ke teerth na jaayein,
woh pedon jaise.

Jo jeev
bhakton ke charanon ki dhool
nahi paata,
woh jeeta hua bhi
murdā hi hai.

Aur jisne kabhi
Tulsi ki sugandh
Hari ke charanon par nahi soonghi,
woh sirf saans leta shav hai.

Ant mein Śaunaka bole:

“Hey Sūta ji,
aapki har baat
hamare hriday ko choo rahi hai.”

“Kripya bataiye—
jab Śuka jaise maha-bhāgavata
king Parīkṣit se baat kar rahe the,
toh aage kya kaha?”

🌸 Is Adhyay ka Saar (Moral)

Har ichchha ke liye alag pooja hoti hai

Par moksha ke liye sirf Hari ki bhakti

Hari ki kathaa mann ko shuddh karti hai

Bhakti hi gyaan, vairagya aur mukti ka mool hai

Kṛṣṇa ke bina jeevan, jeevan nahi—sirf jeevit sharir hai"""
        create_image_text_layout(
            text_content=text2,
            layout="full"
        )

    # Chapter 4
    with st.expander("Chapter 4 - Creation of the Universe (Prayers to Hari)"):
        text1 = """ 
        🌸 Chapter 4 – Srishti ka Janm (Hari ki Stuti)

(Hinglish Kahani Style • Short • Simple • Moral Tone)

Sūta bole:

Śuka ke shabd sun kar,
jo aatma ka sach batate the,
King Parīkṣit ka mann
bilkul shant aur pavitra ho gaya.

Unka mann
poori tarah Kṛṣṇa mein bas gaya."""
        create_image_text_layout(
            "attached_assets/chapter2/2.4.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Parīkṣit ne dheere-dheere
sab kuch chhod diya—

apna sharir

patni aur bachche

mahal

dhan-daulat

pashu

rishtedaar

aur rajya

Jo cheez kabhi “meri” lagti thi,
ab woh sab bojh lagne lagi.

Unka mann ekdum saaf tha.
Unka vishwas gehra tha.

Isliye unhone wahi sawaal poocha
jo har sachcha bhakt poochta hai.

Unhone kaha:

“Main samajh chuka hoon
ki mrityu paas aa rahi hai.

Ab dharma, artha aur kaam—
yeh teeno mere liye bekaar ho gaye hain.

Ab main sirf
Vāsudeva mein aatma-gyan chahata hoon.”

Phir Parīkṣit bole:

“Hey Brāhmaṇa,
aapke shabd amrit jaise hain.

Jab aap Hari ki kathaa sunate ho,
toh meri agyaan ki raat khatam ho jaati hai.”

Unhone phir poocha:

“Bhagavān ne
is poore brahmāṇḍ ko
apni Māyā shakti se kaise racha?

Jise bade-bade devta bhi
poori tarah samajh nahi paate.”

“Woh kaun si shakti hai
jisse Hari
is duniya ko
banate, sambhalte
aur phir mita dete hain?”

“Woh kaise
kabhi seedhe
aur kabhi devtaon ke zariye
leela karte hain?”

“Yeh sab mujhe samjhaaiye,
kyunki aap hi
is gyaan ke sachche janne wale ho.”

Sūta bole:

King ki baat sun kar,
Śuka ne pehle
apna mann Kṛṣṇa mein lagaya,
phir bolna shuru kiya.

Śrī Śuka bole:

“Main us Pūrṇ Purush ko pranām karta hoon,
jo apni leela se
is sansaar ko
banata, sambhalta aur mitata hai.”

“Wahi ek hai
jo teen shaktiyon ka roop leta hai,
taaki srishti chalti rahe.”

“Main baar-baar pranām karta hoon
us Hari ko—

jo sajjanon ka dukh door karta hai

jo adharma ko rokta hai

jo devtaon ko bhi niyantrit karta hai

aur jo gyaan ka deep jalaata hai”

“Woh bhakton ka rakshak hai.
Woh ahankaari logon se door rehta hai.
Woh apne swabhav mein hi
poorn aur anandit hai.”

“Uska naam lena,
uska smaran karna,
usko dekhna,
uske aage jhukna—

yeh sab
pal bhar mein paap dhota hai.”

“Jo log
uske charanon ka sahara le lete hain,
woh bina kasht ke
sab bandhan tod dete hain
aur sachchi shanti paate hain.”

“Chahe koi tap kare,
daan de,
yog kare,
ya bade mantra jaane—

agar Hari ko samarpan nahi,
toh asli shanti nahi.”

“Yahan tak ki
sabse giray hue log bhi
agar uske bhakton ka sahara le lein,
toh pavitra ho jaate hain.”

“Bhakt use
aatma ke roop mein dekhte hain.

Karmkandi use
Vedon ka roop maante hain.

Dharmik use
dharma hi samajhte hain.

Tapasvi use
lakshya maante hain.”

“Devta bhi
uske roop ko dekh kar
hairaan reh jaate hain.”

“Wahi Lakshmi ka swami hai.
Wahi yagyon ka adhipati hai.
Wahi buddhi ka niyantrak hai.
Wahi sab lokon ka rakshak hai.”

“Uske charanon ka dhyaan
buddhi ko shuddh karta hai.
Aur aatma ka sach dikha deta hai.”

“Wahi pehle-pahle
Brahmā ke hriday mein
srishti ka gyaan jagata hai.
Aur vaani ko Ved ka roop deta hai.”

“Wahi har sharir mein
andar bas kar
use jeevit rakhta hai.”

“Main us mahān guru ko bhi pranām karta hoon,
jinke mukh se
yeh gyaan-amrit
shishyon ne piya.”

“Hey King,
yeh gyaan pehle
Hari ne Brahmā ko diya,
Brahmā ne Nārada ko,
aur Nārada se
yeh aage chala.”

🌼 Is Adhyay ka Saar (Moral)

Mrityu paas ho toh sab moh chhoot jaata hai

Sirf Hari ka smaran reh jaata hai

Srishti, sthiti aur pralaya – sab usi ki leela hai

Bina samarpan ke koi sadhana poori nahi

Hari bhakti hi gyaan, shanti aur mukti ka mool hai"""
        create_image_text_layout(
            text_content=text2,
            layout="full"
        )

    # Chapter 5
    with st.expander("Chapter 5 - Creation of the Universe (Dialogue between Nārada and Brahmadeva)"):
        text1 = """ 
        🌿 Chapter 5 – Srishti ka Janm

(Nārada aur Brahmā ka Samvaad)
(Hinglish Kahani Style • Short • Simple • Moral Tone)

Nārada bole:

“Hey Devon ke Dev,
Hey sab jeevon ke rachayita,
main aapko pranām karta hoon.

Mujhe woh gyaan bataiye
jo aatma ka sach dikha de.”"""
        create_image_text_layout(
            "attached_assets/chapter2/2.5.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        “Yeh jo duniya dikh rahi hai,
yeh asal mein kya hai?

Iska aadhaar kya hai?
Yeh kahan se bani?
Aur ant mein kahan jaati hai?”

“Sab kuch aap jaante ho,
past, present, future—sab.
Aapke liye toh yeh sansaar
haath par rakhe phal jaisa hai.”

“Par mujhe ek baat pareshaan karti hai,”
Nārada bole.

“Aapne kathor tapasya ki.
Toh kya aapse bhi upar
koi aur shakti hai?”

Brahmā muskura kar bole:

“Beta Nārada,
tumhara sawaal bahut pavitra hai.

Tum sab ke hit ke liye pooch rahe ho,
isliye main sach bataata hoon.”

“Jo tum mujhe samajhte ho,
woh poora sach nahi hai.

Mujhe jo bhi shakti mili hai,
woh mujhse upar se aayi hai.”

“Jaise Suraj ki roshni se
chand, taare aur aag chamakte hain,
waise hi main bhi
Hari ki roshni se kaam karta hoon.”

“Log Māyā ke chakkar mein padkar
mujhe srishti ka karta maan lete hain.
Par asal mein sab kuch
Vāsudeva ka hai.”

“Māyā logon ki aankhon par
parda daal deti hai.

Phir jeev bolta hai—
‘Yeh mera hai’
‘Main karta hoon’.”

“Sach yeh hai,”
Brahmā bole,

“Padarth ho,
karma ho,
samay ho,
prakriti ho,
ya jeev ho—

sab Vāsudeva hi hai.”

“Ved bhi aakhir mein
Nārāyaṇa ka hi gungaan karte hain.

Yagya bhi usi ke liye hote hain.
Tapasya bhi usi ke liye hoti hai.
Mukti bhi usi se milti hai.”

“Main jo kuch bhi rachata hoon,
woh usi ke sankalp se hota hai.

Main sirf ek madhyam hoon.”

“Woh gunon se pare hai,
phir bhi apni Māyā se
teen gun banata hai—

sattva (paalan)

rajas (rachna)

tamas (vinash)”

“In teen gunon ke jaal mein
jeev bandh jaata hai.
Aur bhool jaata hai
apna asli roop.”

“Usi se phir
ahankaar paida hota hai—
‘main’ aur ‘mera’.”

“Phir dheere-dheere
akash bana,
phir hawa,
phir aag,
phir paani,
aur phir prithvi.”

“Inhi se sharir bane,
indriyaan bani,
mann bana,
aur jeev sansaar mein aa gaya.”

“Jab tak yeh sab
alag-alag the,
tab tak kuch bhi chal nahi raha tha.”

“Par Hari ke ichha se
sab ek saath aaye,
aur jeevan shuru hua.”

“Phir us Viraat Purush ne
brahmāṇḍ ke ande ko toda.

Uske hazaar sir,
hazaar haath,
hazaar pair the.”

“Uske sharir se
sab lok bane—

neeche ke lok bhi,
upar ke lok bhi.”

“Uske mukh se
Brāhmaṇa bane.
Baahon se Kṣatriya.
Janghon se Vaiśya.
Aur charnon se Śūdra.”

“Yeh poora sansaar
usi ka sharir hai.”

🌼 Kahani ka Saar (Moral):

Brahmā bhi poorn nahi, Hari par nirbhar hain

Jo dikh raha hai, sab usi ki leela hai

Ahankaar Māyā ka phal hai

Srishti Hari ki ichha se chalti hai

Sachcha gyaan tab milta hai jab “main” mit jaata hai"""
        create_image_text_layout(
            text_content=text2,
            layout="full"
        )

    # Chapter 6
    with st.expander("Chapter 6 - Description of the Virāṭ Puruṣa—Exposition of the Puruṣa Sūkta"):
        text1 = """ 
        Chapter 6 – Virāṭ Puruṣa ki Kahani (Hinglish Story Version)

Bahut pehle ki baat hai.
Ek bahut bada Divine Being tha.
Usse Virāṭ Puruṣa kaha jaata tha.
Poora universe uske body ka hissa tha."""
        create_image_text_layout(
            "attached_assets/chapter2/2.6.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        🌸 Uska muh aur awaaz

Virāṭ Puruṣa ka mouth hi sab bolne ki shakti tha.
Usse aag (Fire) ka janm hua.
Uski body ke har element se Vedic meters bane.
Uski tongue se food, taste aur bhog aaye.
Meetha, khatta, kadwa – sab usi se nikla.

🌬️ Saans aur khushboo

Uski naak se saari prāṇa vāyu nikli.
Hawa ka devta Vāyu wahin se aaya.
Smell se ausadhi, herbs aur plants bane.
Jo bhi healing hai, uska source wahi tha.

👀 Aankhen aur roshni

Uski aankhon se roshni nikli.
Suraj aur aasmaan wahi se bane.
Har rang, har roop uski aankhon ka khel tha.
Uske kaan se directions aur pavitra jagah bani.

🤲 Body aur sparsh

Uski skin se touch ka ehsaas aaya.
Sacrifice aur yagna bhi wahi se aaye.
Uske baal se ped, paudhe aur jungle bane.
Uske nakhun aur daadhi se pahad aur bijli bani.

🦶 Haath aur pair

Uske arms duniya ki raksha karte the.
Uske steps teen lokon ka sahara bane –
Bhū, Bhuva aur Svar.
Jo bhi sharan leta, use safety milti.

🌧️ Creation ka raaz

Uske sharir se paani, baarish aur creation hui.
Bachchon ki khushi bhi wahi se aayi.
Par kuch jagah se dukh aur andhera bhi nikla.
Ye batata hai ki duniya mein achha aur bura dono hote hain.

🌍 Poora jagat usi ka roop

Devta, insaan, jaanwar, pakshi, ped –
Sab Virāṭ Puruṣa ka hi hissa hain.
Past, present, future –
Sab uske andar samaaya hua hai.

Jaise Suraj apne andar aur bahar dono jagah roshni deta hai,
Waise hi Virāṭ Puruṣa andar aur bahar dono jagat ko jagmata hai.

🧘 Mukti ka rasta

Virāṭ Puruṣa moksha ka swami hai.
Usse koi dar nahi.
Usse karm ka bandhan bhi nahi.
Wo sabke andar rehta hai, par sabse upar bhi.

🌟 Sab kuch usi se

Brahma create karta hai,
Shiv destroy karta hai,
Aur Vishnu protect karta hai –
Par power Virāṭ Puruṣa ki hi hoti hai.

🙏 Ant mein

Brahma bhi kehta hai,
“Main bhi nahi jaanta main kahan se aaya.”
Virāṭ Puruṣa ki Māyā itni gehri hai
Ki usse koi poori tarah samajh nahi sakta.

Isliye sab uske charnon mein natmastak hote hain.
Kyuki wahi sach, shakti aur shanti hai.

✨ Moral (Seekh):

Jo humein alag-alag lagta hai,
asal mein sab ek hi shakti ka roop hai.
Jab hum ye samajh jaate hain,
to dar khatam ho jaata hai."""
        create_image_text_layout(
            text_content=text2,
            layout="full"
        )

    # Chapter 7
    with st.expander("Chapter 7 - Some Līlāvatāras and their work"):
        text1 = """ 
        Chapter 7 – Bhagwān ke Līlāvatār (Hinglish Story Version)

Brahmā ji bole:

Bahut samay pehle,
Bhagwān ne alag-alag roop liye.
Har roop ka ek kaam tha.
Har kaam mein daya, shakti aur nyāy chhupa tha."""
        create_image_text_layout(
            "attached_assets/chapter2/2.7.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        🐗 Varāha Avatar

Jab dharti samundar mein doob rahi thi,
Bhagwān Varāha bane.
Unhone dharti ko utha liya.
Aur ek hi vaar mein Hiraṇyākṣa ka ant kar diya.

🔥 Suyajña aur Kapila

Phir Bhagwān Suyajña bane.
Teenon lokon ka dukh door kiya.
Isliye logon ne unhe Hari kaha.

Ek baar wo Kapila bane.
Unhone apni maa ko ātman ka gyaan diya.
Maa ne isi janam mein moksha pa li.

🧘 Dattātreya aur Sanat Kumar

Atri rishi ke ghar Bhagwān Datta bane.
Unke charnon ki dhool se log pavitra ho gaye.

Srishti ke shuru mein,
Bhagwān Sanat Kumar aur unke bhai bane.
Unhone bhool chuke gyaan ko wapas diya.

❄️ Nara–Nārāyaṇa

Bhagwān Nara aur Nārāyaṇa bane.
Unki tapasya itni gehri thi
Ki Kāma dev bhi unhe hila na saka.

⭐ Dhruva aur Pṛthu

Chhote se Dhruva ko maa ke shabd chub gaye.
Wo jungle gaya.
Bhagwān ne use amarlok diya.

King Pṛthu ke roop mein,
Bhagwān ne dharti ko dhan se bhara.

🐎 Hayagrīva, Matsya aur Kūrma

Ek baar Bhagwān Hayagrīva bane.
Unki saans se Vedic shabd nikle.

Phir Matsya bane.
Pralay mein sabko bachaya.
Vedo ko sambhala.

Aur jab samudra manthan hua,
Wo Kūrma bane.
Mandar parvat ko peeth par uthaya.

🦁 Nṛsiṃha Avatar

Jab devta dare hue the,
Bhagwān Nṛsiṃha bane.
Unhone Hiraṇyakaśipu ka ghamand tod diya.
Bhakt Prahlād ko bachaya.

🐘 Gajendra Moksha

Ek haathi musibat mein tha.
Usne Bhagwān ko yaad kiya.
Hari aaye.
Chakra chalaya.
Aur haathi ko bachaya.

👣 Vāmana Avatar

Bhagwān Vāmana bane.
Teen kadmon mein teenon lok naap liye.
Raja Bali ne sab kuch de diya.
Bhagwān khush ho gaye.

⚕️ Dhanvantari

Bhagwān Dhanvantari bane.
Unhone Āyurveda diya.
Naam lene se bhi rog door ho jaate.

🪓 Paraśurāma

Jab adharm badha,
Bhagwān Paraśurāma bane.
Unhone ahankari rājāon ka ant kiya.

🏹 Rāma Avatar

Phir Bhagwān Rāma bane.
Pitā ki baat maani.
Van gaye.
Rāvaṇ ka vināsh kiya.
Dharma jeet gaya.

🦚 Kṛṣṇa aur Balarāma

Phir wo Balarāma aur Kṛṣṇa bane.
Bachpan mein hi asuron ka ant kiya.
Govardhan utha liya.
Kāliyā ko shant kiya.
Gopālon ko bachaya.

Maa Yaśodā ne unke muh mein
14 lok dekhe.
Tab samjhi –
Ye sirf bacha nahi, Bhagwān hain.

📜 Ved aur Kalki

Insaan kam samajhne lage,
Toh Bhagwān ne Ved baant diye.

Aur jab Kali Yug badhega,
Bhagwān fir aayenge.
Adharm ko khatam karenge.

🌈 Ant mein

Bhagwān ke kaam ginne nahi ja sakte.
Unki Māyā ko koi poori tarah nahi samajh sakta.

Bas wahi samajh paata hai
Jo prem aur bhakti se unke charnon mein jhukta hai.

✨ Moral (Seekh):

Jab jab dharti par dukh badhta hai,
tab tab Bhagwān kisi na kisi roop mein aate hain.
Bhakti, sachchai aur dharma
hamesha jeette hain."""
        create_image_text_layout(
            text_content=text2,
            layout="full"
        )

    # Chapter 8
    with st.expander("Chapter 8 - Queries regarding the relation between the body, Soul and God, etc."):
        text1 = """ 
        Chapter 8 – Shareer, Aatma aur Bhagwān ke Beech ka Rishta (Hinglish Story Version)

Raja Parīkṣit ne shant man se kaha:

“O Brahman Dev,
Aap Nārada ji ke shishya ho.
Nārada ji Bhagwān ke gunon ko sabko dikhate hain.
Unhone bahuton ko Parmatma ka sach samjhaya.

Main bhi wahi sach jaanna chahta hoon.
Hari ki kathayein bahut shubh aur pavitra hoti hain.”"""
        create_image_text_layout(
            "attached_assets/chapter2/2.8.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        🌿 Antim ichchha

Raja bole,
“Mujhe aisa gyaan dijiye
ki main apna man Kṛṣṇa mein laga kar
shanti se apna sharir chhod saku.”

Jo log shraddha se
Bhagwān ki kathayein sunte hain,
Bhagwān jaldi hi unke hriday mein bas jaate hain.

Jaise sharad ritu gande pani ko saaf kar deti hai,
Waise hi Kṛṣṇa
dil ke saare paap dho dete hain.

Aur jiska dil saaf ho jaata hai,
wo Kṛṣṇa ke charnon ko
kabhi nahi chhodta.
Jaise koi musafir
ghar laut kar fir kahin nahi jaata.

🤔 Gehre sawal

Parīkṣit ne poocha:

“Aatma jo tattvon se bani nahi hai,
wo shareer mein kaise bandh jaati hai?
Kya ye bina kaaran hota hai
ya karma ki wajah se?”

“Bhagwān ka roop insaan jaisa kyon lagta hai?
Agar roop milta-julta hai,
toh bhagwān aur insaan mein antar kya hai?”

“Jab Bhagwān apni Māyā hata dete hain,
toh wo kahaan rehte hain?”

⏳ Samay aur Srishti

Unhone aur poocha:

Kalpa kitna lamba hota hai?

Samay kab lamba lagta hai, kab chhota?

Devta, pitṛ aur insaan
kitni umar jeete hain?

“Karma humein
kaunse lok mein le jaata hai?
Swarg, narak ya dharti?”

🌍 Jagat ke raaz

Raja ne poocha:

“Dharti, aakash, grah, nadi, pahad –
sab ka janm kaise hua?”

“Varṇa aur āśram kaise bane?
Dharma har yug mein kaise badalta hai?”

“Bhagwān ke avatār kaunse hain
aur unke kaam kya hain?”

🧘 Mukti ka rasta

Unhone poocha:

“Yoga ka sahi raasta kya hai?
Aatma ka bandhan kaise toot-ta hai?
Aur moksha kaise milti hai?”

“Māyā kya hai?
Aur Bhagwān uske saath kaise khelte hain?”

🙏 Vinamr prarthna

Ant mein Raja ne kaha:

“Main vinamr hoon.
Mujhe sab kuch kram se samjhaiye.
Aap hi meri sharan ho.”

“Meri saans chahe chali jaaye,
par jab tak main
Hari ki kathayein peeta rahunga,
tab tak mujhe koi bhay nahi.”

🌸 Śuka ji ka uttar

Parīkṣit ke shabd sun kar
Śuka ji bahut prasann hue.

Unhone kaha,
“Main tumhe Bhāgavata Purāṇa sunaunga.
Ye Ved ke samaan pavitra hai.”

Aur phir,
Parīkṣit ke har prashn ka uttar
katha ke roop mein
aage badhne laga.

✨ Moral (Seekh):

Jab insaan sachche mann se
prashn karta hai,
aur ahankār chhod deta hai,
tab gyaan khud chal kar aata hai.

Bhagwān ko paane ka sabse saral rasta
shraddha, bhakti aur kathā hai."""
        create_image_text_layout(
            text_content=text2,
            layout="full"
        )

    # Chapter 9
    with st.expander("Chapter 9 - Śuka‘s discourse—Catuḥślokī Bhāgavata (Chatushloki Bhagwat)"):
        text1 = """ 
        Chapter 9 – Śuka ji ki Kathā (Catuḥślokī Bhāgavata) – Hinglish Story Version

Śrī Śuka ji bole:

🌱 Shareer aur Aatma ka sach

“Oh Raja,
Shareer aur Aatma ka rishta seedha nahi hota.
Ye sirf Māyā ke through dikhta hai.
Jaise sapne mein sab real lagta hai,
par uthte hi sab khatam.”"""
        create_image_text_layout(
            "attached_assets/chapter2/2.9.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Māyā ke saath rehkar,
Aatma kai roop le leti hai.
Kabhi bacha, kabhi jawaan,
kabhi devta, kabhi insaan.

Aur phir wo sochne lagti hai:
“Ye main hoon.”
“Ye mera hai.”

🌼 Asli mukti

Jab Aatma
apni asli shaan mein jeene lagti hai,
Time aur Māyā se upar uth jaati hai.
Tab “main” aur “mera”
dono chhoot jaate hain.

Aur Aatma
apni poori roshni mein
shant khadi ho jaati hai.

🌸 Brahmā ji ki uljhan

Bhagwān ne
Brahmā ji ko apna asli roop dikhaya.
Taaki wo samajh saken
ki Parmatma aur Jīva alag hote hain.

Brahmā ji kamal par baithe.
Srishti banana chahte the.
Par unhe raasta samajh nahi aa raha tha.

🔔 “Tapa” ka sandesh

Ek din,
paane ke andar se
ek awaaz aayi:
“Tapa… Tapa…”

Sirf do akshar.
Par bahut gehra arth.

Brahmā ji ne chaaron taraf dekha.
Koi nahi tha.
Tab unhone samjha –
ye updesh hai.

🧘 Kathor tapasya

Brahmā ji ne
man aur saans ko control kiya.
Indriyon ko shant kiya.
Aur hazaar divya varsh tak tapasya ki.

Is tapasya se
unhe srishti ka gyaan mila.

🌈 Vaikuṇṭha ka darshan

Bhagwān prasann hue.
Unhone Brahmā ji ko
Vaikuṇṭha lok dikhaya.

Wahan na dukh tha,
na bhay,
na bhram.

Wahan Time ka zor nahi chalta.
Wahan Māyā ka raaj nahi.

✨ Bhagwān ke sevak

Wahan Bhagwān ke sevak the.
Chamakte hue.
Hari rang jaise panna.
Chaar bhujaayein.
Peeli vastra.
Sone ke gehne.

Unki chamak se
Vaikuṇṭha aur roshan lagta tha.
Jaise bijli se aasmaan chamak jaaye.

🌺 Lakṣmī ji aur Hari

Wahan Lakṣmī ji
Bhagwān ke charnon ki seva karti hain.
Jhoole par baith kar
unke gun gaati hain.

Bhramar bhi
unki stuti mein gun-gun karte hain.

🙏 Bhagwān ka roop

Brahmā ji ne
Bhagwān ko dekha.

Chaar bhujaayein.
Mukha par komal muskaan.
Laal kamal jaise netra.
Peela vastra.
Chhaati par Śrīvatsa chinh.

Wo apni hi shakti
aur aanand mein magn the.

💖 Brahmā ji ka prem

Brahmā ji ka dil
prem se bhar gaya.
Aankhon se aansu behne lage.
Rom-rom khil utha.

Unhone Bhagwān ke
charno mein pranām kiya.

🌟 Bhagwān ka sparsh

Bhagwān prasann hue.
Unhone Brahmā ji ko
apne haath se sparsh kiya.

Aur muskurate hue bole –
jaise koi
apne priya ko
sach ka raasta dikhata hai.

✨ Moral (Seekh):

Jab insaan tapasya, shraddha aur shant man se
sach ko dhoondhta hai,
to Bhagwān khud
raasta dikha dete hain.

“Main aur mera” chhoot jaaye,
wahi asli gyaan hai."""
        create_image_text_layout(
            text_content=text2,
            layout="full"
        )

    # Chapter 10
    with st.expander("Chapter 10 - The Ten Characteristics of the Bhāgavata Purāṇa"):
        text1 = """ 
        Chapter 10 – Bhāgavata Purāṇa ke Das Lakṣaṇ (Hinglish Story Version)

Śrī Śuka ji bole:

“Oh Raja,
Bhāgavata Purāṇa ek aisi kathā hai
jisme poori srishti ka raaz chhupa hai.”"""
        create_image_text_layout(
            "attached_assets/chapter2/2.10.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        🔟 Das baatein jo Bhāgavata sikhata hai

Bhāgavata Purāṇa mein 10 main vishay hote hain:

Sarga – sookshm srishti

Visarga – sthool srishti

Sthāna – niyam aur vyavastha

Poṣaṇa – sabki raksha

Ūti – karmon se paida ichchha

Manvantara – Manu ka samay

Īśānukathā – Bhagwān ki kathayein

Nirodha – sab ka lay

Mukti – bandhan se chhutkara

Āśraya – sabka aakhri sahara

In pehle 9 ko samajhkar hi
10ve satya tak pahuncha ja sakta hai.

🌱 Srishti ka aaram se janm

Jab guṇon ka santulan bigadta hai,
tab paanch tattva bante hain.
Indriyaan banti hain.
Man aur buddhi banti hai.
Ise kehte hain Sarga.

Jab Virāṭ Puruṣa se
poori duniya dikhti hai,
wo Visarga hota hai.

⚖️ Raksha aur niyam

Bhagwān jab
niyam chalate hain,
use Sthāna kehte hain.

Jab wo daya se
sabki raksha karte hain,
use Poṣaṇa kehte hain.

🔄 Manu aur Karma

Har yug mein
Manu aata hai.
Wo dharma ka raasta dikhata hai.
Is samay ko Manvantara kehte hain.

Karm se jo ichchha banti hai,
use Ūti kehte hain.

📖 Bhagwān ki kathā

Bhagwān ke avatār,
unke kaam,
aur bhakton ki kahaniyaan –
ye sab Īśānukathā hai.

🌊 Lay aur Mukti

Jab sab kuch
Bhagwān mein hi mil jaata hai,
use Nirodha kehte hain.

Jab jhootha roop chhoot jaata hai
aur aatma apne sach mein tik jaati hai,
use Mukti kehte hain.

🌟 Sabka mool

Jis se srishti nikli,
jisme palan hua,
aur jisme lay hua –
wo hi Āśraya hai.
Wahi Parabrahma hai.

👁️ Teen drishti

Bhagwān teen roop mein dikhte hain:

Adhyātmik – andar ki aatma

Adhidaivik – devta roop

Adhibhautik – sharirik roop

Teenon milkar hi
jeevan chalate hain.

🌊 Nārāyaṇa ka janm

Virāṭ Puruṣa ne
Cosmic Egg ko toda.
Shuddh jal banaya.
Us jal par shayan kiya.

Isliye unka naam pada
Nārāyaṇa –
jo jal mein vas karte hain.

🧘 Indriyon ka janm

Jab bhookh lagi –
muh bana.
Bolna chaha –
vaani aayi.

Sunnā chaha –
kaan bane.
Dekhna chaha –
aankhen aayi.

Chalna chaha –
pair bane.
Kaam chaha –
haath bane.

Sochna chaha –
man aur hriday bana.

Sab kuch
ichchha se hi bana.

🔥 Teen guṇ

Karma teen guṇon se chalta hai:

Sattva – shanti

Rajas – gati

Tamas – andhera

Inse swarg, dharti
aur narak ka raasta banta hai.

🔄 Srishti, palan aur vināsh

Bhagwān hi:

banate hain

bachate hain

aur mitaate hain

Kabhi dharma bankar,
kabhi kaal bankar.

🌈 Par sach kya hai?

Sach ye hai –
Bhagwān karta bhi hain aur nahi bhi.
Ye sab Māyā ka khel hai.

Parabrahma
sab se pare hai.
Naam, roop, kaam –
sab se upar.

🌺 Ant mein

Śuka ji bole:

“Raja,
maine tumhe srishti ka roop dikhaya.
Aage samay ka gyaan bhi dunga.”

Aur phir kahani
Vidura aur Maitreya ki taraf
aage badhne lagi.

✨ Moral (Seekh):

Bhāgavata humein sikhata hai
ki sab kuch badalta rehta hai,
par jo sabka sahara hai,
wahi kabhi nahi badalta.

Usi mein tikna
hi shanti aur mukti hai।"""
        create_image_text_layout(
            text_content=text2,
            layout="full"
        )


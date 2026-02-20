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
    create_image_text_layout("attached_assets/chapter3/chapter3.jpg", layout="full")

    text0 = """
    <h2>Book 3 - Third Skandha</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")

    # Book 3 - Third Skandha

    # Chapter 1
    with st.expander("Chapter 1 - Meeting of Vidura and Uddhava"):
        text1 = """ 
        Chapter 1 – Vidura aur Uddhava ki Mulakaat

(Hinglish Story Version)

Shri Shuka bole:

Yeh baat purane samay ki hai.
Jab Vidura ne apna bhara-pura ghar chhod diya.

Wahi ghar,
jahan Bhagwan Krishna
Pandavon ke doot ban kar aaye the.
Aur jahan woh apno ki tarah rahe the."""
        create_image_text_layout(
            "attached_assets/chapter3/3.1.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ 
        Par jab adharm badhne laga,
Vidura ka mann dukhi ho gaya.
Aur woh rajmahal chhod kar
van ki taraf nikal pade.

🕊️ Parikshit ka sawaal

Raja Parikshit ne poocha:

“Hey Maharshi,
Vidura aur Maitreya ki mulakaat
kahan hui?
Aur kis vishay par baat hui?”

“Vidura ka sawaal
bahut pavitra tha.
Isliye woh zaroor
bahut gehra hoga.”

📜 Suta bole

Suta ji bole:

“Raja Parikshit,
dhyaan se suno.
Main poori kahani sunata hoon.”

🔥 Adharm ka samay

Us samay
andhe raja Dhritarashtra
apne bure beton ka saath de rahe the.

Unhone Pandavon ko
jalakar maarne ki saazish ki.
Lakshagriha banwayi
aur aag lagwa di.

Phir bhi woh ruke nahi.

Jab Draupadi ke baalon ko
sabha mein ghasita gaya,
Dhritarashtra chup rahe.

Yeh dekh kar
dharma ro pada.

Pandav jua haar gaye.
Unka rajya chala gaya.
Vanvaas mila.

Aur jab vanvaas ke baad
Yudhishthira ne apna haq maanga,
toh bhi use lautaaya nahi gaya.

🪔 Krishna ki baat bhi na suni

Bhagwan Krishna khud doot ban kar aaye.
Unki baatein amrit jaisi thi.

Bhishma jaise mahaan log
sun kar pighal gaye.

Par Dhritarashtra ne
sunne se inkaar kar diya.

🧠 Vidura ka updesh

Tab Vidura ne sabha mein kaha:

“Yudhishthira ko
unka rajya lauta do.

Tum jis Bhim se darte ho,
woh ab zeher bhara saanp ban chuka hai.”

“Krishna Pandavon ke saath hain.
Devgann aur Brahman bhi unke saath hain.”

“Duryodhan tumhara beta ho sakta hai,
par woh ghar ke liye
ashubh hai.”

“Parivaar ke bhale ke liye
use roko.”

⚡ Apmaan aur tyag

Vidura ki baat
Duryodhan ko chubh gayi.

Gusse mein bola:

“Is daasi-putra ko
yahan kisne bulaya?”

“Ise shehar se nikaal do!”

Sabha mein hi
Vidura ka apmaan hua.

Par Vidura shant rahe.
Unhone maya ko samjha.

Aur bina gussa kiye
apna dhanush
darwaze par rakh kar
sabha chhod di.

🌍 Teerth yatra

Vidura Hastinapur chhod gaye.
Unke saath
Kauravon ka bhagya bhi
chala gaya.

Woh akela chale.
Nadiyon, parvaton,
vanon aur mandiron mein.

Hari ke charnon se
pavitra sthal ghoome.

Simple jeevan jiya.
Zameen par soye.
Ped ki chhaal pehni.

Apne hi log
pehchaan nahi paaye.

🌊 Prabhas aur Saraswati

Waqt ke saath
woh Prabhas pahuche.

Wahi unhe
apne vansh ke vinaash ka
samachar mila.

Unka mann dukhi ho gaya.
Aur woh Saraswati nadi ke kinare aaye.

Wahan kai pavitra sthalon ka darshan kiya.

🤝 Uddhava se milan

Aage chalkar
woh Yamuna ke paas pahuche.

Wahin unki mulakaat hui
Uddhava se.

Vidura ne Uddhava ko
pyaar se gale lagaya.

Aur poocha:

“Kya Krishna aur Balaram
sukhi hain?”

“Kya Vasudev kushal se hain?”

“Kya Pradyumna, Samba,
Satyaki sab theek hain?”

“Kya Dharmaraj Yudhishthira
rajya ki raksha kar rahe hain?”

“Kya Bhim ka gussa
ab bhi saanp jaisa hai?”

“Kya Arjuna,
jise Shiv ne bhi pariksha li,
sukhi hai?”

“Kya Nakula aur Sahadeva
apna rajya paa chuke?”

🌼 Vidura ka gyaan

Vidura bole:

“Maine jo kuch saha,
usme mujhe aashcharya nahi hua.

Hari ki leela hi aisi hai.
Woh manushya roop mein aakar
mann ko bhramit kar dete hain.”

“Woh sab kuch kar sakte hain,
phir bhi chup rehte hain.”

“Unka avtaar
adharm ko sahi raah par laane ke liye hota hai.”

🙏 Ant mein prarthna

Vidura ne kaha:

“Hey mitra,
mujhe Krishna ki leela sunao.

Unki kahani
jo sabka kalyaan karti hai.”

✨ Moral (Seekh):

Jab sach bolne wale ko
apmaan milta hai,
tab bhi use
shant rehna chahiye.

Tyag aur dhairya
hi sachchi shakti hai."""
        create_image_text_layout(
            text_content=text2,
            layout="full"
        )


    # Chapter 2
    with st.expander("Chapter 2 - The Dialogue between Uddhava and Vidura"):
        text1 = """ 
        Chapter 2 – Uddhava aur Vidura ka Samvaad

(Hinglish Story Version)

Shri Shuka bole:

Jab Vidura ne
prem se Uddhava se poocha,
“Krishna kaise hain?”
toh Uddhava chup ho gaye.

Unke hoth kuch keh na paaye.
Dil bhar aaya.
Aankhon mein aansu aa gaye."""
        create_image_text_layout(
            "attached_assets/chapter3/3.2.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ 
        🌱 Bachpan ki yaadein

Uddhava ko
Krishna ka bachpan yaad aa gaya.

Jab woh sirf
5 saal ke the,
aur khel-khel mein
Krishna ki pooja karte the.

Maa bulati thi khane ke liye,
par Uddhava kehte the,
“Abhi nahi.”
Pehle Krishna.

Aaj wahi Krishna
yaadon mein hi reh gaye the.

🕯️ Maun ka kshan

Ek muhurat tak
Uddhava bilkul chup rahe.

Mann Krishna ke charnon mein doob gaya.
Unke sharir ke rom-rom
khade ho gaye.

Aankhen band thi.
Aansu beh rahe the.
Lag raha tha jaise
jeevan ka uddeshya
poora ho gaya ho.

🌊 Virah se vachan tak

Dheere-dheere
Uddhava hosh mein aaye.

Aankhen ponchi.
Aur Vidura se bole.

☀️ Krishna ke bina shunya

“Vidura,” Uddhava bole,
“main kya shubh samachar doon?”

“Jab Krishna roopi Suraj
is duniya se ast ho gaya.”

“Hamare ghar
ab andhere mein doob gaye hain.”

“Samay ek ajgar ki tarah
sab kuch nigal gaya.”

🐟 Nazdeek hokar bhi na pehchaan

Uddhava bole:

“Yeh duniya ka durbhagya hai.”

“Yadavo ne Krishna ke saath rehkar bhi
unhe pehchana nahi.”

“Jaise machhli
samundar mein rehkar bhi
chand ko nahi jaanti.”

🌸 Roop jo aankhon ko bandh le

Krishna ka roop
sirf sundar nahi tha.

Woh roop
yog-maya ka chamatkar tha.

Insaani kaam ke liye
insaani roop.

Itna sundar
ki gehne bhi
us roop se sajte the.

👑 Rajasuya ki yaad

Rajasuya yagya mein,
jab sab ne Krishna ko dekha,
toh laga—

“Vidhaata ne
aaj apni poori kala
isi roop mein kharch kar di.”

💃 Vraj ki gopiyan

Vraj ki gopiyan
jab Krishna ki muskaan dekhti,
toh sab kaam bhool jaati.

Unki aankhen
Krishna ke peeche chal padti.
Mann bhi.

🔥 Avtaar ka rahasya

Krishna janme nahi the.
Woh prakat hue the.

Jaise lakdi mein aag
pehle se hoti hai,
bas gharsan se
bahar aati hai.

🏠 Manav jaise vyavhaar

Uddhava bole:

“Mujhe dukh hota hai jab yaad karta hoon—”

“Woh Vasudev ke ghar janme.”
“Gokul mein rahe, jaise bhay ke kaaran.”

“Apne hi shehar se
chupchaap chale gaye.”

🙏 Maa–baap ke charnon mein

“Unhone apne maa–baap ke charan chue.”
Aur kaha—

‘Hum aapki seva na kar paaye.
Humein maaf karna.’

Yeh yaad karke
mera hriday bhar aata hai.”

🌼 Charn raj ka sparsh

“Jo ek baar bhi
Krishna ke charnon ki raj
mehsoos kar le,”
“woh unhe kaise bhool sakta hai?”

“Unki bhauhon ki halki si gati se
prithvi ka bojh
door ho jaata tha.”

🕊️ Shishupaal ka uddhar

Vidura, tumne dekha tha—

Shishupaal,
jo Krishna ka shatru tha,
unke samne mukti pa gaya.

Wahi mukti
jiske liye yogi
saalon tapasya karte hain.

⚔️ Yuddh ke veer

Yuddh ke maidan mein,
jo veer Krishna ke mukh ko
aakhri baar dekh gaye,
woh bhi unke charnon tak
pahunch gaye.

👑 Sevak jaisa Bhagwan

“Wahi Bhagwan,” Uddhava bole,
“jo teenon lokon ke swami hain,”

“Ugrasena jaise raja ke samne
vinamr hokar khade ho jaate.”

“Yeh dekhkar
humein dukh hota hai.”

🌺 Putana par bhi kripa

“Putana,” Uddhava bole,
“zehar laayi thi.”

Par Krishna ne
use bhi maa ka darja diya.

“Isse zyada dayaalu
koi aur devta ho sakta hai kya?”

🐍 Shatru bhi bhakt

“Asur bhi,” Uddhava bole,
“Krishna ke bhakt jaise hi hain.”

“Gusse mein hi sahi,
par unka mann
Krishna par tika hota hai.”

🐄 Gokul ki leela

Krishna Devaki aur Vasudev se janme.
Phir Gokul gaye.

11 saal tak
apni shakti chhupa kar rahe.

Gaiyaan charaayi.
Bansuri bajaayi.
Yamuna ke kinare khele.

😄 Baal leelayein

Kabhi haste.
Kabhi rote.

Bilkul
nanhe sher ke bachche jaise.

🎶 Govardhan aur Raas

Govardhan uthaya.
Indra ka ghamand toda.

Aur phir
poornima ki raaton mein
Raasa rachaya.

Gaan gaaya.
Nritya kiya.
Sab ke mann ka shringar bane.

✨ Moral (Seekh):

Jo Bhagwan ko
apne paas paakar bhi
pehchaan na sake,
woh sachcha bhagyashaali nahi.

Virah bhi bhakti hai,
aur yaad hi
prem ka sabse gehra roop hai 🌸"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 3
    with st.expander("Chapter 3 - Glorious deeds of Kṛṣṇa"):
        text1 = """ 
        Chapter 3 – Shri Krishna ke Divya Karya

(Vidura–Uddhava Samvaad | Hinglish Story Version)

Uddhava bole:

🌸 Mata–Pita ka sukh

Krishna chahte the
ki unke maa–baap khush rahein.

Isliye
Balarama ke saath
Mathura aaye.

Wahan Kansa ko
rajasabha se gira diya.
Aur uska ant kar diya."""
        create_image_text_layout(
            "attached_assets/chapter3/3.3.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ 
        Bura shasan
yahin khatam ho gaya.

📚 Guru ka aadar

Krishna ne
Guru Sandipani se
Veda seekhe.

Sirf ek baar sunke hi
sab yaad kar liya.

Aur guru-dakshina mein
unke mare hue putra ko
wapis lauta diya.

💐 Rukmini ka vivah

Jaise Garuda
amrit le aaya,
waise hi Krishna
Rukmini ko le aaye.

Rajao ke beech se.
Sabke saamne.

Prem se.
Sahas se.

Yeh tha
Gandharva vivah.

🐂 Satyabhama aur shaurya

Ek aur swayamvar mein,
Krishna ne
prabal bailon ko vash mein kiya.

Aur Satyabhama se vivah kiya.

Jo raja phir bhi lade,
unhe parajit hona pada.

Krishna ko
koi chot na pahucha saka.

🌳 Parijaat ka ped

Satyabhama ki ichchha thi
Parijaat ka ped.

Krishna use le aaye.

Indra krodhit ho gaye.
Yuddh hua.

Par Krishna ke aage
devta bhi thehar na sake.

🌍 Narakasur ka ant

Narakasur ne
bahut atyachar kiye the.

Krishna ne
Sudarshan chakra se
uska ant kiya.

Prithvi mata ne
Krishna se prarthna ki.

Krishna ne
uske putra ko
rajya de diya.

👸 Bandhi rajkumariyon ka uddhar

Jo rajkumariyan
bandhi hui thi,
Krishna ko dekh kar
aankhon se khushi jhalak uthi.

Lajja.
Prem.
Aabhar.

Sab ek saath.

Krishna ne
apni yog-maya se
sabse alag-alag
vidhi se vivah kiya.

👶 Santaan aur vistaar

Har rani se
das–das santaan hui.

Sab Krishna jaise hi gunwaan.

Yeh tha
prakriti ka vistaar.

⚔️ Dushton ka vinash

Krishna ne
apne bhakton ke madhyam se
kai dushton ka ant karaya.

Kalayavan.
Jarasandh.
Shalva.

Kuch ko swayam mara.
Kuch ko anyon se.

Dharti ka bojh
kam hota gaya.

🏹 Kurukshetra ka yuddh

Jab sena Kurukshetra chali,
dharti kaanp uthi.

Yuddh hua.
Bhayankar yuddh.

Ant mein
adharm gira.

🧘 Antar ka vichar

Par Krishna santusht nahi hue.

Unhone socha,
“Abhi bhi
dharti ka bojh poora nahi utra.”

Yadavo ki sena
abhi baaki thi.

Aur iska ant
sirf ek tareeke se ho sakta tha—
aapas ke vivad se.

👑 Dharm ka raj

Krishna ne
Yudhishthira ko
rajya par bithaya.

Aur dikhaya—
dharm ka marg.

Abhimanyu ke vansh ko
phir se jeevan diya.

Parikshit ko
raksha di.

🐎 Ashvamedha yagya

Yudhishthira ne
Ashvamedha yagya kiya.

Teen baar.

Krishna ki kripa se
shanti bani rahi.

🌊 Dwarka ka jeevan

Dwarka mein
Krishna ne
ghar-grihasthi ka sukh bhi liya.

Par mann se
kabhi bandhe nahi.

Gyaan mein sthir rahe.
Vairagya mein sthit rahe.

🌙 Prem aur maryada

Krishna muskurate the.
Meethi baatein karte the.

Sabko anand dete the.

Par har cheez
samay ke liye thi.

⏳ Ant ki taiyari

Ek din Krishna ne socha,
“Yeh sukh
sthir nahi hai.”

Bhog bhagya ke adheen hai.
Manushya bhi.

Jo yogeshwar ka bhakt ho,
woh in par bharosa nahi karta.

🔱 Prabhas aur shraap

Prabhas mein
kuch rishiyon ka
apmaan hua.

Rishiyon ne
shraap diya.

Yadavo par
maya chha gayi.

🕊️ Daan aur punya

Prabhas mein
sabne snaan kiya.

Pitraon aur devtaon ko
jal diya.

Brahmanon ko
daan diya.

Gau.
Sona.
Vastra.
Bhojan.

Aur vinamrta se
mastak jhukaya.

✨ Moral (Seekh):

Krishna ne sab kuch paaya,
phir bhi bandhe nahi.

Asli shakti tyag mein hai,
aur asli sukh bhakti mein. 🌸"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4
    with st.expander("Chapter 4 - Destruction of the Yādavas and Kṛṣṇa’s Message"):
        text1 = """ 
        Chapter 4 – Yādavon ka Vināsh aur Shri Krishna ka Antim Sandesh

(Vidura–Uddhava Samvaad | Hinglish Story Version)

Uddhava bole:

🍂 Yādavon ka antim samay

Jab Brāhmanon ne
anumati de di,
toh Yādavon ne
madira ka sevan kiya.

Budhhi bhrasht ho gayi.
Vivek kho gaya."""
        create_image_text_layout(
            "attached_assets/chapter3/3.4.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ 
        Kadve shabd bole gaye.
Aur baat
ladai tak pahunch gayi.

🔥 Aapas ka vinash

Surya ast hone ke baad,
woh yuddh shuru hua.

Bilkul waise hi,
jaise baans aapas mein
ragadne se
jungle ki aag lag jaati hai.

Yādav
apne hi haathon
nasht ho gaye.

🌊 Krishna ka shant roop

Krishna ne
apni māyā ka khel dekha.

Kuch bole nahi.
Sarasvatī ka jal piya.

Aur ek vriksh ke neeche
shant hokar baith gaye.

🌸 Uddhava ko aadesh

Us samay,
jab main Dwarka mein tha,
Krishna ne mujhe bulaya.

Unhone kaha,
“Badarī jao.”

Main samajh gaya
unka sanket.

Par phir bhi
unke charnon se
door jana mushkil tha.

🌿 Antim darshan

Main unhe dhoondhta hua
Sarasvatī ke kinare pahuncha.

Wahan maine dekha—

Krishna akela baithe the.
Neela sharir.
Peet vastra.
Chaar bhujaein.

Aankhen shant.
Mukh par prakash.

Unka daahina paon
baaye jaangh par tha.

Sab bhog chhod kar bhi
poorn anand mein.

🌼 Krishna ka vachan

Krishna ne muskurakar kaha,

“Uddhava,
main tumhare mann ka bhaav jaanta hoon.”

“Tumhari yeh antim janm hai.”

“Mujhe khushi hai
ki tum mujhe
is shant samay mein
dekhne aaye.”

📖 Gyaan ka daan

Krishna bole,

“Yahi woh gyaan hai
jo maine srishti ke aarambh mein
Brahma ko diya tha.”

“Yahi Bhagavat gyaan hai.”

🙏 Uddhava ka prashn

Main kaanpte swar mein bola,

“Prabhu,
mujhe kuch nahi chahiye.”

“Na dharm,
na arth,
na kaam,
na moksh.”

“Mujhe bas
aapki seva chahiye.”

“Mera mann ghabra jaata hai
jab main dekhta hoon—”

“Aap janm lete hain
jabki aap ajanmā hain.”

“Aap karma karte hain
jabki aap akartā hain.”

🕊️ Atma gyaan

Krishna ne
mujhe atma ka gyaan diya.

Satya ka bodh karaya.

Maine unke charnon mein
mastak jhukaya.

Parikrama ki.
Aur aansuon ke saath
wahan se chala aaya.

🏔️ Badarī ki yatra

Ab main
Badarī āshrama jaunga.

Wahi,
jahan Nara aur Narayana
sadiyon se tapasya kar rahe hain.

🌙 Vidura ka dhairya

Uddhava ki baatein sunkar,
Vidura ka hriday bhar aaya.

Par gyaan ne
unke shok ko sambhala.

📜 Antim updesh

Vidura bole,

“Krishna ka gyaan
mujhe bhi chahiye.”

Uddhava ne kaha,

“Yeh gyaan
Maitreya rishi denge.”

“Krishna ne
unhe hi niyukt kiya hai.”

🌊 Virah aur smriti

Uddhava aur Vidura ne
poori raat
Yamuna ke kinare bitaayi.

Krishna ki leelaon ka
amrit peeya.

Phir Uddhava
Badarī ke liye nikal pade.

🌧️ Vidura ka virah

Uddhava ke jaane ke baad,
Vidura Krishna ka smaran karte rahe.

Prem se
aankhen bhar aayi.

Aur phir
Ganga ki or
chalte hue
Maitreya rishi se mile.

✨ Moral (Seekh):

Jo kuch janm leta hai,
woh jaata bhi hai.

Par gyaan aur bhakti
kabhi nasht nahi hote.

Krishna jaate nahi—
woh hriday mein bas jaate hain 🌸"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 5
    with st.expander("Chapter 5 - Dialogue between Vidura and Maitreya—Tattvas and their Deities"):
        text1 = """ 
        Chapter 5 – Vidura aur Maitreya: Srishti ka Rahasya

(Hinglish Moral Story Version)

🌊 Haridwar ka pavitra kinara

Haridwar mein,
Ganga ke shant kinare,
Vidura rishi Maitreya ke paas aaye.

Vidura ka mann shant tha.
Unka hriday bhakti se bhara tha.

Maitreya shaant baithe the.
Unke chehre par daya thi.
Unki aankhon mein gehra gyaan.

Vidura ne vinamrata se prashn kiya."""
        create_image_text_layout(
            "attached_assets/chapter3/3.5.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ 
        ❓ Vidura ka prashn

Vidura bole:

“Gurudev,
log sukh ke liye karm karte hain.
Par sukh nahi milta.

Sirf dukh hi dukh milta hai.
Aisa kyun?”

“Is duniya mein
sahi jeevan ka raasta kya hai?”

“Kaise hum
Sachcha sukh pa sakte hain?”

🌸 Bhakt ka lakshan

Vidura bole:

“Main jaanta hoon,
aap jaise bhakt
is duniya mein
sirf daya ke liye ghoomte hain.”

“Aap humein
woh gyaan dijiye
jo atma ko pehchaanne mein madad kare.”

🌍 Srishti ka rahasya

Vidura ne kaha:

“Bhagwan ne
yeh duniya kaise banayi?”

“Woh kaise
sab kuch paida karte hain,
phir sambhalte hain,
aur phir sama lete hain?”

“Ek hokar
woh anek kaise bane?”

“Devta, lok, jeev —
sab kaise bane?”

❤️ Krishna-katha ka ras

Vidura bole:

“Gurudev,
aur sab baatein
ab feeki lagti hain.”

“Bas Krishna ki kathayein
hi mann ko tript karti hain.”

“Jaise hi Hari ki katha
kaan mein padti hai,
duniya ka moh
khud hi chhoot jaata hai.”

🌺 Maitreya ka uttar

Maitreya muskuraye.

Unhone kaha:

“Vidura,
tumhara prashn
bahut uttam hai.”

“Tumhara mann
Hari mein sthir hai.”

“Isliye tum
is gyaan ke yogya ho.”

✨ Vidura ka satya

Maitreya bole:

“Tum koi sadharan vyakti nahi ho.”

“Tum Yama ho,
jo ek shraap ke kaaran
manushya roop mein aaye.”

“Krishna tumse
bahut prem karte the.”

“Jaate samay
unhone mujhe kaha—
Vidura ko gyaan dena.”

🌌 Srishti ki kahani (Simple)

Maitreya bole:

“Shuru mein
sirf Bhagwan the.”

“Na din tha,
na raat.”

“Na koi duniya,
na koi jeev.”

“Sab kuch
unke andar shant tha.”

🌫️ Maya ka khel

“Bhagwan ki shakti ko
Maya kehte hain.”

“Maya se hi
duniya dikhti hai.”

“Samay (Time) ke chalne se
Maya hilne lagi.”

🧠 Buddhi ka janm

“Maya se pehle
Mahat tattva bana.”

“Phir aaya
Ahamkar — ‘main’ ka bhaav.”

“Phir mann,
indriyaan,
aur devta bane.”

🌬️🔥💧🌍 Panch Mahabhut

Phir Maitreya bole:

Pehle Aakash bana

Phir Vayu

Phir Agni

Phir Jal

Aur aakhir mein Prithvi

“Har tattva
pichhle tattva ka gun
apne andar rakhta hai.”

🙏 Devtaon ki prarthana

Devta Bhagwan ke paas gaye.

Bole:

“Prabhu,
hum alag-alag hain.”

“Hum milkar
srishti ko chala nahi paa rahe.”

“Kripya
humein marg dikhaiye.”

🌸 Bhagwan ke charan

Devta bole:

“Aapke charan
thande chhaav jaise hain.”

“Jo bhi unmein sharan leta hai,
sansaar ka dukh
door ho jaata hai.”

🕊️ Bhakti ka rahasya

Maitreya bole:

“Jo log
Bhagwan ki katha ka amrit peete hain,
unke mann se
moh khud hi chala jaata hai.”

“Bhakti ka raasta
sabse saral hai.”

“Yog kathin hai,
gyan kathin hai.”

“Par prem se ki gayi seva
sabse aasaan hai.”

🌼 Seekh (Moral)

Duniya ko samajhna mushkil hai,
par Bhagwan ko chahna aasaan hai।

Jahan ahankar khatam hota hai,
wahin se shanti shuru hoti hai।

Bhakti — bina bojh ka raasta,
seedha hriday se Bhagwan tak 💛"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6
    with st.expander("Chapter 6 - Cosmology: Creation of the Universe"):
        text1 = """ 
        🌌 Chapter 6 – Brahmand ki Rachna (Creation of Universe)

(Hinglish Moral Story Version – Simple & Emotional Tone)

Bahut purane samay ki baat hai.
Jab kuch bhi exist nahi karta tha… na dharti, na aasman, na insaan.

Sirf Bhagwan the.
Unhone decide kiya ki woh ek nayi duniya banayenge."""
        create_image_text_layout(
            "attached_assets/chapter3/3.6.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ 
        ✨ Universe banane ki shuruaat

Bhagwan ne apni shakti aur Time (Samay) ko saath liya.
Phir unhone 23 basic tattvon (elements) mein entry ki.

Yeh tattv alag-alag the.
Inme creation ki power thi, lekin woh soyi hui thi.

Bhagwan ne unhe jagaya.
Aur unhe ek saath kaam karne ki shakti di.

🧑‍🌟 Virat Purush ka janm

Jab sab tattv ek saath aaye,
Tab ek mahaan cosmic form bana — Virat Purush.

Virat Purush ke andar poori duniya chhupi hui thi.
Woh ek golden glow wala divine roop tha.

Woh Brahmand ke cosmic egg mein hazaar saal tak raha.

💫 Virat Purush ke andar sab kuch tha

Virat Purush ne khud ko kai roop mein divide kiya:

❤️ Ek roop — soul ke form mein heart mein

🌬️ Dus roop — life energies (pranas)

🌍 Teen roop — body, mind aur divine energy

Isi Virat Purush ke andar saare jeev baste hain.

👄 Body ke parts se duniya bani

Bhagwan ne Virat Purush ke body parts se duniya aur indriya banayi.

👉 Mouth se Fire aur Speech bani
👉 Tongue se Taste
👉 Nose se Smell
👉 Eyes se Sight aur Light
👉 Skin se Touch
👉 Ears se Hearing

🧠 Mind aur Heart ka janm

👉 Brain se Intelligence bani
👉 Heart se Mind aur emotions bane
👉 Ego se insaan ko action karne ki feeling mili

🌍 Teen lokon ka creation

Virat Purush ke body se 3 worlds bane:

Head se Heaven

Feet se Earth

Navel se Sky / Space

👥 Samaj ki rachna

Bhagwan ne samaj ke roles bhi create kiye:

👉 Mouth se Brahmins – knowledge aur wisdom
👉 Arms se Kshatriyas – protection aur bravery
👉 Thighs se Vaishyas – farming aur business
👉 Feet se Shudras – service aur support

Sabka role important tha.
Sab milkar society ko strong banate hain.

🌟 Bhagwan ki Maya

Sage ne kaha…

Bhagwan ki power itni mysterious hai
Ki usse samajhna bahut mushkil hai.

Even bade sages bhi unki poori greatness samajh nahi paaye.

🌼 Moral (Seekh)

👉 Har cheez ek dusre se connected hai.
👉 Har insaan ka ek unique role hota hai.
👉 Ego aur greed se door rehna chahiye.
👉 Bhagwan ki creation bahut deep aur magical hai.
👉 Knowledge aur devotion life ko meaningful banate hain."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7
    with st.expander("Chapter 7 - Vidura’s Queries"):
        text1 = """ 
        🌿 Chapter 7 – Vidura ke Sawal (Deep Questions About God & Life)

(Hinglish Moral Story Version – Simple, Emotional, Easy to Read)

Ek din Vidura, jo bahut wise aur calm insaan the,
sage Maitreya ki baatein dhyaan se sun rahe the.

Unhone creation aur Bhagwan ki power ke baare mein bahut kuch suna.
Lekin unke mann mein kuch doubts aa gaye.

Isliye unhone respectfully Maitreya se sawal poochna shuru kiya."""
        create_image_text_layout(
            "attached_assets/chapter3/3.7.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ 
        ❓ Vidura ka Pehla Sawal

Vidura bole,

“Bhagwan toh pure aur perfect hain.
Unme koi change nahi hota.”

“Phir woh kaise duniya banate hain?
Kaise woh activity aur qualities mein involve ho sakte hain?”

🧸 Child Example

Vidura ne samjhaya:

👉 Baccha toys dekhkar khelta hai
👉 Usko khelne ki desire hoti hai

Lekin Bhagwan toh already complete hain.
Unhe kisi cheez ki zarurat nahi.

“Toh phir Bhagwan creation kyun karte hain?”

🌫️ Maya ka Mystery

Vidura ne ek aur important sawal poocha:

“Bhagwan ki Maya duniya banati hai.
Maya logon ko confuse karti hai.”

“Lekin agar soul pure aur immortal hai,
toh woh Maya se kaise effect ho jata hai?”

😔 Human Suffering ka Sawal

Vidura bole,

“Agar Bhagwan har body mein present hain,
toh phir log dukh aur problems kyun face karte hain?”

“Please meri confusion door karo.”

😊 Maitreya ka Wise Answer

Maitreya sage muskuraaye.
Unhone pyaar se samjhaya.

🌙 Dream Example

Maitreya bole:

“Jab insaan sapna dekhta hai,
toh kabhi-kabhi use lagta hai ki uska sar kaat diya gaya.”

Lekin reality mein kuch nahi hota.

Waise hi duniya ka dukh bhi illusion ho sakta hai.

🌊 Reflection Example

Unhone ek aur example diya:

👉 Paani mein moon ka reflection hilta dikhta hai
👉 Lekin asli moon toh sky mein stable hota hai

Waise hi body ke problems
soul ke problems nahi hote.

🧘 Solution kya hai?

Maitreya ne kaha:

👉 Bhagwan ki bhakti
👉 Desire se door rehna
👉 Bhagwan ka naam sunna aur sunana

Ye sab gradually illusion ko hata dete hain.

😌 Peace ka Secret

Jab senses Bhagwan par focus ho jaate hain,
tab insaan ka dukh khatam hone lagta hai.

Jaise deep sleep mein insaan tension bhool jaata hai.

💛 Vidura ki Realisation

Vidura bahut khush ho gaye.

Unhone kaha,

“Ab mujhe samajh aa gaya hai.”

👉 Bhagwan completely independent hain
👉 Humans Bhagwan par depend karte hain

🌍 Vidura ke Bade Sawal

Vidura ne aur knowledge maanga.

Unhone poocha:

👉 Universe ka structure kya hai
👉 Different creatures kaise bane
👉 Kings aur sages ka history kya hai
👉 Life ke goals kaise achieve kare
👉 Dharma aur spirituality kaise follow kare

Unhone teacher-student relationship aur moksha ke baare mein bhi poocha.

🌟 Maitreya ka Reaction

Maitreya sage bahut khush hue.

Unhe laga Vidura sach mein knowledge seekhna chahte hain.
Isliye unhone decide kiya ki woh sab explain karenge.

🌼 Moral (Seekh)

👉 Knowledge tab milta hai jab hum questions poochte hain.
👉 Duniya ke dukh aksar illusion hote hain.
👉 Bhakti aur wisdom life ko peaceful banate hain.
👉 Guru aur teacher ka respect bahut zaruri hai.
👉 Real happiness andar se aati hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 8
    with st.expander("Chapter 8 - Creation of Brahmā—His Vision of Nārāyaṇa"):
        text1 = """ 
        🌸 Chapter 8 – Brahma ki Creation aur Narayana ka Darshan

(Hinglish Moral Story Version – Simple, Emotional, Easy to Read)

🌿 Vidura ki Knowledge Journey Continue Hoti Hai

Sage Maitreya Vidura se bole,

“Tum bahut pavitra aur wise ho.
Tum hamesha Bhagwan ko apna main goal mante ho.”

“Isi liye main tumhe ek divine kahani sunane wala hoon.
Yeh kahani duniya ke creation ke baare mein hai.”"""
        create_image_text_layout(
            "attached_assets/chapter3/3.8.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ 
        🌌 Universe Shuru Hone Se Pehle

Bahut purane samay ki baat hai.

Sab kuch paani se bhara hua tha.
Na zameen thi… na sky… na insaan.

Sirf Bhagwan Narayana the.

👉 Woh cosmic ocean par
👉 Shesh Naag ke upar
👉 Shaanti se rest kar rahe the.

Unki power hidden thi.
Jaise lakdi ke andar fire hoti hai, par dikhti nahi.

⏳ Long Cosmic Sleep

Bhagwan bahut lambe samay tak soye rahe.
Unhone apne andar poora universe store karke rakha tha.

Phir time ki power activate hui.
Aur creation ka process shuru hua.

🌺 Divine Lotus Ka Janm

Bhagwan ke navel (nabhi) se
ek sundar golden lotus nikla.

Woh lotus poore ocean ko roshan kar raha tha.

Aur us lotus ke andar ek divine being paida hua…

👉 Brahma ji

👀 Brahma Ji Ka Confusion

Brahma ji jab paida hue,
toh woh confuse ho gaye.

Unhone socha:

“Main kaun hoon?”
“Main yahan kyun hoon?”
“Yeh lotus kahaan se aaya?”

🔍 Source Dhundhne Ki Koshish

Brahma ji lotus ke stem ke andar gaye.
Woh uska root dhundhne lage.

Lekin unhe kuch nahi mila.
Bahut lambe time tak woh search karte rahe.

Finally woh thak gaye.

🧘 Meditation Ka Decision

Brahma ji wapas lotus par baith gaye.
Unhone apna mind control kiya.

Aur deep meditation karna shuru kiya.

Unhone 100 saal tak meditation ki.

✨ Divine Vision Milta Hai

Meditation ke baad
Brahma ji ke heart mein divine knowledge jag gaya.

Aur tab unhe ek amazing darshan mila…

🌊 Narayana Ka Darshan

Brahma ji ne dekha:

👉 Bhagwan Narayana
👉 Shesh Naag par rest kar rahe hain
👉 Unka body bright aur divine hai
👉 Unke kapde golden shine kar rahe hain
👉 Unki garland aur ornaments heavenly the

Unki beauty itni powerful thi
ki poora universe unme samaya hua lag raha tha.

🌙 Bhagwan Ki Compassion

Bhagwan ke face par ek sweet smile thi.
Woh apne bhakton ka dukh door karte hain.

Unke feet lotus jaise soft aur shining the.
Aur unhe dekhkar Brahma ji emotional ho gaye.

💡 Creation Knowledge Milta Hai

Bhagwan ko dekhte hi
Brahma ji ko samajh aa gaya:

👉 Universe kaise create karna hai
👉 Life kaise start karni hai

Unhone samjha ki sab Bhagwan se hi shuru hota hai.

🙏 Brahma Ji Ka Gratitude

Brahma ji ne Bhagwan ki praise karni shuru ki.
Unhone creation start karne ka decision liya.

🌼 Moral (Seekh)

👉 Jab hum confuse hote hain, meditation clarity deta hai.
👉 Sab creation ek divine source se aata hai.
👉 Knowledge patience aur focus se milta hai.
👉 True wisdom andar se jagta hai.
👉 Bhagwan hamesha apne bhakton ko guide karte hain."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 9
    with st.expander("Chapter 9 - Brahmā’s Prayer and Viṣṇu’s Boon"):
        text1 = """ 
        🌸 Chapter 9 – Brahma ki Prarthana aur Vishnu ka Ashirvaad

(Hinglish Moral Story Version – Simple + Emotional + Easy to Understand)

🌿 Brahma Ji Ko Divine Realisation

Bhagwan Narayana ka darshan milne ke baad
Brahma ji bahut emotional ho gaye.

Unhone samjha:

👉 Bhagwan hi sab kuch hain
👉 Universe mein jo kuch bhi dikhta hai
👉 Sab unki Maya ka part hai"""
        create_image_text_layout(
            "attached_assets/chapter3/3.9.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ 
        🙏 Brahma Ji Ki Prarthana

Brahma ji bole:

“Hey Prabhu, bahut tapasya ke baad aaj mujhe aapka darshan mila hai.”

“Log aapko samajh nahi paate,
kyunki woh body aur duniya mein phas jaate hain.”

“Sach mein sirf aap hi exist karte ho.”

🌺 Vishnu – Sab Avatars Ka Source

Brahma ji ne kaha:

👉 Bhagwan ka divine form
👉 Har avatar ka source hai
👉 Usi se universe create hota hai

Aur woh bole:

“Main bhi aapke nabhi ke lotus se paida hua hoon.”

❤️ Bhagwan Devotees Ke Dil Mein Rehte Hain

Brahma ji ne ek important baat boli:

👉 Bhagwan un logon ke heart mein rehte hain
👉 Jo unki stories sunte hain
👉 Jo devotion se unka naam lete hain

😔 Sansar Ka Dukh

Brahma ji bole:

“Jo log Bhagwan ko ignore karte hain,
woh duniya ke dukh mein phas jaate hain.”

Unhone bataya:

Log suffer karte hain —
👉 Fear
👉 Desire
👉 Anger
👉 Greed
👉 Attachment

🌍 Maya Ka Illusion

Brahma ji samjhate hain:

👉 Body aur world temporary hai
👉 Soul permanent hai
👉 Maya logon ko confuse karti hai

🧘 Devotion Ki Power

Brahma ji bolte hain:

👉 Bhagwan ko yaad karna
👉 Unki stories sunna
👉 Unka naam lena

Ye sab insaan ko fear aur sin se free karta hai.

⏳ Time Ka Fear

Brahma ji kehte hain:

“Time sabko destroy karta hai.”

“Even main bhi time se darta hoon.”

Isliye unhone Bhagwan ki tapasya ki.

🌟 Brahma Ji Ki Wish

Brahma ji ne Bhagwan se request ki:

👉 Mujhe knowledge do
👉 Mujhe power do
👉 Main universe properly create kar sakoon
👉 Main ego aur sin se bach sakoon

🌼 Vishnu Ka Reply

Bhagwan Vishnu ne Brahma ji ko console kiya.

Woh bole:

👉 “Dar mat.”
👉 “Tum already capable ho.”
👉 “Meditation aur tapasya continue karo.”

🔥 Vishnu Ka Biggest Teaching

Bhagwan ne kaha:

👉 Jab tum mujhe sab jagah dekhoge
👉 Tab tum creation ko samajh jaoge

👉 Jab log samjhenge ki Bhagwan sab mein hai
👉 Tab unka dukh khatam ho jayega

💡 True Knowledge

Bhagwan ne Brahma ji ko ek deep secret bataya:

👉 Soul body se alag hai
👉 Soul Bhagwan ka part hai
👉 Jo ye samajh leta hai
👉 Woh divine state achieve karta hai

🌸 Vishnu Ka Blessing

Bhagwan ne Brahma ji ko bless kiya:

👉 Creation mein success milega
👉 Ego tumhe control nahi karega
👉 Tum divine knowledge ke saath kaam karoge

🌈 Final Instruction

Bhagwan Vishnu bole:

“Tum mere dwara hi create hue ho.”
“Ab tum universe create karo.”

Aur phir Bhagwan apne divine form mein disappear ho gaye.

🌼 Moral (Seekh)

👉 True knowledge devotion se milta hai.
👉 Ego spiritual growth ka biggest enemy hai.
👉 Bhagwan sabke andar exist karte hain.
👉 Meditation clarity deta hai.
👉 Time sabse powerful force hai.
👉 Devotion insaan ko fear se free karta hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 10
    with st.expander("Chapter 10 - Brahmā’s Penance and Ten-fold Creation"):
        text1 = """ 
        🌸 Chapter 10 – Brahma ki Tapasya aur Dus Prakar ki Srishti

(Hinglish Moral Story Style – Simple + Easy + Deep Meaning)

🌿 Vidura Ka Question

Vidura ne Maitreya Rishi se poocha:

👉 Brahma ji ne Universe kaise create kiya?
👉 Kitne prakar ki srishti (creation) hui?
👉 Creation ka process kya tha?"""
        create_image_text_layout(
            "attached_assets/chapter3/3.10.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ 
        🧘 Brahma Ji Ki Tapasya

Bhagwan Vishnu ke disappear hone ke baad:

👉 Brahma ji ne 100 divine years tak meditation ki
👉 Unhone apna mind completely God par focus kiya

Tapasya se unki:

✔ Knowledge increase hui
✔ Creation power strong hui

🌊 Cosmic Situation

Brahma ji ne dekha:

👉 Universe water aur wind se disturbed tha
👉 Deluge (pralaya) ke baad sab unstable tha

Phir unhone apni divine power se:

👉 Water aur wind ko control kar liya

🌸 Lotus Se Creation

Brahma ji lotus par baithe the
Jo Vishnu ji ke nabhi se nikla tha

Unhone decide kiya:

👉 Isi lotus se universe recreate karna hai

Unhone lotus ko divide kiya
Aur worlds ka structure banaya

⏳ Time Ka Concept

Maitreya Rishi ne bataya:

👉 Time Bhagwan ki divine power hai
👉 Time beginning aur end ke bina hota hai
👉 Creation aur destruction dono Time se hote hain

🌍 Universe Ki 10 Types Ki Creation
⭐ 1. Mahat Tattva Creation

👉 Ye universal intelligence hai
👉 Universe ka first blueprint

⭐ 2. Ahamkara Creation

👉 Ego aur individuality ka creation
👉 “Main” ka feeling

⭐ 3. Tanmatra Creation

👉 Subtle elements create hue
👉 Sound
👉 Touch
👉 Form
👉 Taste
👉 Smell

⭐ 4. Sense Organs Creation

👉 Knowledge organs
👉 Action organs

Jaise:

👁 Eyes
👂 Ears
✋ Hands
👣 Legs

⭐ 5. Gods & Mind Creation

👉 Sense organs ke presiding gods
👉 Mind ka creation

⭐ 6. Ignorance Creation

👉 Maya ka influence
👉 Wrong understanding
👉 Spiritual blindness

👉 Ye first 6 creations Prakriti se related hain

🌿 Vikriti Creation (Physical Living Beings)
⭐ 7. Plants Creation

6 types of plants bane:

🌳 Trees
🌿 Plants
🌱 Creepers
🎍 Bamboo type trees
🌾 Strong vines
🌲 Fruit trees

⭐ 8. Animals & Birds Creation

28 types ke animals create hue

🐄 Cloven Hoof Animals

Cow
Goat
Buffalo
Camel
Sheep
Deer
Pig

🐎 Single Hoof Animals

Horse
Donkey
Mule

🐕 Five Nail Animals

Dog
Tiger
Lion
Monkey
Elephant
Tortoise
Shark

🐦 Birds

Peacock
Swan
Crow
Owl
Hawk
Crane
Vulture

⭐ 9. Humans Creation

👉 Humans most active species bane
👉 Rajo-guna dominant
👉 Actions aur desires se driven

⭐ 10. Divine & Semi-Divine Beings

8 categories create hui:

✨ Gods
✨ Pitrs (ancestors)
✨ Asuras
✨ Gandharvas & Apsaras
✨ Yaksha & Rakshasa
✨ Siddha & Charana
✨ Ghosts & Spirits
✨ Kinnar & Vidyadhara

🌌 Special Creation

Sanatkumara jaise sages
👉 Spiritual knowledge ke symbol hain
👉 Mixed divine creation ke part hain

🌈 Important Spiritual Teaching

👉 Creation fixed order mein nahi hoti
👉 Maya sabko confuse karti hai
👉 Universe cyclic hai
👉 Same creation baar-baar hoti hai

🌼 Moral & Life Lessons
💡 1. Meditation Power

Tapasya knowledge aur clarity deti hai

💡 2. Ego Creation Ka Part Hai

But ego control karna zaroori hai

💡 3. Nature Divine System Hai

Plants, animals, humans
Sab interconnected hain

💡 4. Time Supreme Force Hai

Sab kuch Time ke under hai

💡 5. Universe Cyclic Hai

End aur beginning ek continuous cycle hai

💡 6. Human Life Special Hai

Kyuki spiritual realization possible hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 11
    with st.expander("Chapter 11 - The concept of Time: Manvantaras and life-spans of Men and Gods"):
        text1 = """ 
        Chapter 11 – Time ka Mahaan Siddhant (Manvantaras aur Jeevan ki Avadhi)

Is adhyay mein Maitreya rishi Vidura ko samay (Time) ka bahut gehra aur cosmic concept samjhate hain — sabse chhote kshan se lekar Brahma ke jeevan tak. Yeh batata hai ki Hindu cosmology mein time kitna vistrit aur chakrakar maana gaya hai.

Neeche simple language mein iska saar diya hai:"""
        create_image_text_layout(
            "attached_assets/chapter3/3.11.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ 
        🕉️ 1) Samay ki Sabse Chhoti Ikai – Atom se Time tak

Maitreya batate hain:

Sabse chhota padarth = Paramāṇu (atom)

Jab atoms milte hain → tab bada vastu banta hai

Insaan ko “poori cheez” ka illusion hota hai

Time bhi isi tarah samjha jaata hai:

Chhote padarth → chhota time

Bade padarth → bada time

Iska matlab:

Time sab jagah vyapt hai aur Bhagwan ki shakti hai jo creation ko chalati hai.

⏳ 2) Prachin Time Units (Bahut Interesting)

Yeh ancient Indian time system hai:

Smallest → Biggest

2 paramanu = 1 anu

3 anu = 1 trasarenu

3 trasarenu ka time = 1 truṭi

Phir aage:

100 truṭi = 1 vedha

3 vedha = 1 lava

3 lava = 1 nimeṣa (blink)

3 nimeṣa = 1 kṣaṇa

5 kṣaṇa = 1 kāṣṭhā

15 kāṣṭhā = 1 laghu

15 laghu = 1 nāḍikā

2 nāḍikā = 1 muhūrta

Aur:

1 day + night = 8 prahar

15 days = 1 pakṣa (Shukla + Krishna)

2 pakṣa = 1 month

12 months = 1 year

Human life span (ideal):

100 years

☀️ 3) Devta aur Pitṛ Time

Yeh bahut interesting concept hai:

1 human month = Pitṛs ka 1 day + night

6 months = Devta ka 1 day

6 months = Devta ki night

Iska matlab:

Devtaon ka time human time se bilkul alag scale par chalta hai.

🧭 4) Yuga Cycle – Dharma ka Ghatna

Ek maha cycle = 4 Yugas:

1️⃣ Satya Yuga
2️⃣ Treta Yuga
3️⃣ Dwapar Yuga
4️⃣ Kali Yuga

Total duration:

12,000 divine years

Dharma ki condition:

Satya Yuga → 100% dharma

Treta → 75%

Dwapar → 50%

Kali → 25%

Isliye Kali Yuga mein paap aur ashanti zyada hoti hai.

🌍 5) Brahma ka Ek Din

Yeh sabse bada concept hai:

1 Brahma ka 1 day =

1000 yuga cycles

1 Brahma ki night =

utni hi lambi

Day ke dauraan:

Creation hoti hai

Night ke dauraan:

Universe so jata hai

👑 6) Manvantara kya hota hai?

Brahma ke ek din mein:

14 Manus rule karte hain

Har Manu ka period ≈ 71 yuga cycles

Manu ke dauraan:

Naye kings

Naye rishis

Naye devta

Isko hi Manvantara kehte hain.

🌊 7) Brahma ki Night – Pralaya

Jab Brahma sota hai:

3 worlds destroy ho jate hain

Fire + water sabko cover kar leta hai

Vishnu Sheshnag par so jate hain

Rishis unki stuti karte hain

Phir next day:

Creation fir se shuru

🧓 8) Brahma ki Life Span

Brahma ki total life:

100 divine years

Iska aadha:

Parardha

Abhi:

Pehla aadha khatam ho chuka

Dusra aadha chal raha hai

Current kalpa:

Varaha Kalpa

🪐 9) Universe ka Size

Scripture ke hisaab se:

Universe = ek “cosmic egg”

Bahar 7 layers se covered

Har layer pichhli se 10x badi

Aur:

Vishnu ke andar aise crores universes hain.

🧘 10) Sabse Deep Thought

Time:

Sabko control karta hai

Sab kuch destroy karta hai

Lekin:

Bhagwan par Time ka koi asar nahi hota.

🌌 Core Philosophy

Yeh chapter basically yeh keh raha hai:

Time infinite hai

Creation cyclic hai

Sab kuch repeat hota rehta hai

Brahma bhi permanent nahi hai

Sirf Vishnu/Paramatma eternal hai

Agar Simple Line Mein Samjhein:

Human life → years
Devta life → yugas
Brahma life → kalpas
God → beyond time"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 12
    with st.expander("Chapter 12 - Creation of Rudra, the mind-born Sons and of Manu and Śatarūpā"):
        text1 = """ 
        Chapter 12 – Rudra ka Janm, Brahmā ke Manas Putra aur Manu–Śatarūpā ki Kahani

(Hinglish children-style simple kahani tone)

Ek baar Vidura ne Maitreya rishi se poocha, “Brahmā ji ne duniya ko kaise basaya?”
Tab Maitreya rishi ne dheere-dheere ek sundar aur gehri kahani sunani shuru ki."""
        create_image_text_layout(
            "attached_assets/chapter3/3.12.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ 
        🌑 Pehli Rachna – Agyanta ka Janm

Shuruaat mein Brahmā ji ne kuch aisi cheezein banayi jo andhera aur agyanta failati thi.
Unhone dekha ki yeh rachna achchi nahi hai.

Unka mann udaas ho gaya.
Phir unhone dhyaan lagaya aur dobara achchi rachna karne ka socha.

👶 Chaar Kumaron ka Janm

Is baar Brahmā ji ne chaar pavitra putron ko janm diya:

Sanaka

Sanandana

Sanātana

Sanatkumāra

Yeh chaaron bahut gyani the.
Unhe duniya ke kaam ya parivaar basane mein koi interest nahi tha.

Brahmā ji ne kaha,
“Beta, tum log duniya ko aage badhao.”

Par unhone shanti se mana kar diya.
Woh sirf Bhagwan ki bhakti karna chahte the.

🔥 Gusse se Rudra ka Janm

Unki baat na maanne par Brahmā ji ko thoda gussa aaya.
Unhone gusse ko rokne ki koshish ki, par phir bhi unke bhru (forehead) se ek shaktishaali balak paida hua.

Woh ro raha tha.

Brahmā ji ne kaha:
“Tum roye ho, isliye tumhara naam hoga Rudra.”

Yahi Rudra baad mein Shiva ke roop mein jaane gaye.

Brahmā ji ne unhe kaha:

Tum jagah-jagah reh sakte ho

Tumhari kai roopen hongi

Tum srishti ko aage badhane mein madad karoge

Rudra ne bahut saare apne jaise shaktishaali jeev paida kar diye.
Woh sab itne bhayankar the ki duniya hilne lagi.

Brahmā ji ghabra gaye.
Unhone kaha:

“Bas! Ab tapasya karo. Shanti se rehkar srishti mein madad karo.”

Rudra maan gaye aur jungle mein tapasya karne chale gaye.

🧠 Brahmā ke Manas Putra

Phir Brahmā ji ne apne mann se dus mahan rishiyon ko janm diya:

Marichi

Atri

Angiras

Pulastya

Pulaha

Kratu

Bhrigu

Vasistha

Daksha

Narada

Yeh sab duniya ko basane wale mahan purvaj bane.

🌍 Aur Bhi Cheezein Paida Hui

Brahmā ji ke sharir se alag-alag cheezein paida hui:

Dil se → ichchha (desire)

Bhru se → krodh (anger)

Muh se → vaani (speech)

Peeth se → adharm

Hriday se → dharm

Yeh sab milkar insaan ki nature ko banate hain.

📖 Vedo ka Janm

Phir Brahmā ji ke chaar muh se nikle:

Rigveda

Yajurveda

Samaveda

Atharvaveda

Saath hi nikli:

Ayurveda (medicine)

Dhanurveda (war science)

Gandharvaveda (music)

Sthapatyaveda (architecture)

Yani duniya ka gyaan wahi se shuru hua.

🧍‍♂️🧍‍♀️ Manu aur Śatarūpā ka Janm

Phir Brahmā ji ne socha:

“Abhi bhi log kam hain. Duniya kaise badhegi?”

Tab ek adbhut baat hui.

Unka sharir do hisson mein baant gaya:

Ek hissa → Purush bana

Doosra hissa → Stree bani

Purush ka naam pada Svayambhuva Manu
Stree ka naam pada Śatarūpā

Yeh dono pehle manav joda bane.

👨‍👩‍👧‍👦 Unke Bachche

Manu aur Śatarūpā ke paanch bachche hue:

Priyavrata

Uttānapāda

Ākūti

Devahūti

Prasūti

In sabki shaadi hui aur unse duniya bhar gayi.

Yahin se insani vansh shuru hua.

🌼 Kahani ka Saar (Moral Style)

Gyaan se achchi rachna hoti hai

Gussa se vinash bhi ho sakta hai

Tapasya se shakti milti hai

Purush aur stree milkar hi duniya ko aage badhate hain
Aur sabse bada sach:

Duniya ek din mein nahi bani.
Dheere-dheere, pyaar aur dhairya se bani."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 13
    with st.expander("Chapter 13 - The Boar (Varāha) Incarnation"):
        text1 = """ 
        Chapter 13 – Varāha Avtaar ki Kahani (Bhagwan ka Boar Roop)

Ek din Vidura ne Maitreya rishi se pyaar se poocha,
“Svayambhuva Manu ne shaadi ke baad kya kiya? Aur duniya kaise aage badhi?”

Rishi muskuraaye aur ek adbhut kahani sunane lage."""
        create_image_text_layout(
            "attached_assets/chapter3/3.13.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ 
        👑 Manu ka Prashna

Manu apni patni ke saath Brahmā ji ke paas gaye.
Haath jod kar bole:

“Prabhu, hum aapke bachche hain.
Batayiye hum kya karein, jisse duniya ka bhala ho?”

Brahmā ji khush hue.
Unhone kaha:

Praja (logon) ki raksha karo

Dharm se rajya chalao

Bhagwan ki puja karo

Achhe bachche paida karo

Phir Brahmā ji ne ek bada sach bataya:

“Sabse badi seva hai logon ki raksha karna.”

🌊 Dharti ka Doobna

Manu ne phir kaha:

“Prabhu, ek samasya hai…
Dharti to paani mein doob gayi hai.
Hum kahaan rahenge?”

Yeh sunkar Brahmā ji soch mein pad gaye.

“Dharti ko kaise bachaya jaye?”

🐗 Ek Chhota Sa Boar

Jab Brahmā ji soch hi rahe the,
Tab ek chhota sa jaanwar unki naak se nikla.

Woh ek boar (suar) tha.
Shuru mein woh anguthe jitna chhota tha.

Sab dekh kar hairaan reh gaye.

Phir achanak…

Woh badhne laga!
Aur kuch hi pal mein haathi jitna bada ho gaya.

Sab samajh gaye —
Yeh koi aam jaanwar nahi hai.

Yeh khud Bhagwan Vishnu ka roop tha.
Unka naam pada — Varāha Avtaar.

🌩️ Bhagwan ka Garajna

Bhagwan Varāha zor se garje.
Unki awaaz se saari dishaayein goonj uthi.

Rishiyon ne turant unki stuti karni shuru kar di.
Sab ke dil mein khushi bhar gayi.

🌊 Samundar Mein Chhalang

Phir Varāha Bhagwan seedha samundar mein kood pade.
Jaise ek bada haathi paani mein ghusta hai.

Unhone dharti ko dhoondhna shuru kiya.
Woh paani ke bahut neeche, Rasātal mein chali gayi thi.

🌍 Dharti Ko Bachana

Bhagwan ne apne tez daanton (tusks) se dharti ko pakda.
Pyaar se use uthaya.

Jab woh dharti ko lekar upar aaye,
Woh drishya bahut sundar tha.

Jaise ek bada haathi kamal ka phool utha kar la raha ho.

Sab devta aur rishi khush ho gaye.
Unhone haath jod kar Bhagwan ki stuti ki.

⚔️ Ek Rakshas se Yudh

Tabhi ek balshali rakshas ne unhe roka.
Woh Bhagwan par hamla karne laga.

Par Bhagwan Varāha bahut shaktishaali the.
Unhone us rakshas ko aasani se hara diya.

Jaise sher haathi ko gira deta hai.

🌎 Dharti Ko Wapas Basana

Phir Bhagwan ne dharti ko sambhaal kar paani ke upar rakha.
Use fir se logon ke rehne layak bana diya.

Sab log bahut khush hue.
Duniya fir se jeene lagi.

Aur Bhagwan apna kaam poora karke chupchaap chale gaye.

💫 Kahani ka Saar (Moral)

Jab bhi duniya mushkil mein hoti hai, Bhagwan madad karte hain

Bhagwan kisi bhi roop mein aa sakte hain

Chhoti cheez bhi bada kaam kar sakti hai

Achchai hamesha burai par jeet paati hai

Aur sabse pyari baat:

Jo log Bhagwan ki kahaniyaan sunte hain,
unke dil mein shanti aur himmat aa jaati hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 14
    with st.expander("Chapter 14 - Diti’s Conception"):
        text1 = """ 
        Chapter 14 – Diti ka Garbh (Diti’s Conception) – Saral Kahani

Śrī Śuka ne bataya ki Varāha avtaar ki kahani sunne ke baad bhi Vidura ka mann aur jaanna chahta tha. Unhone ek aur prashna poocha.

🤔 Vidura ka Prashna

Vidura bole:

Hiraṇyākṣa naam ka ek bada daitya tha jise Bhagwan ne maara

Woh Bhagwan se kyun ladha?

Uski paidaish kaise hui?

Maitreya rishi ne kaha — yeh bahut pavitra kahani hai. Isse jeevan ka gyaan milta hai. Phir unhone shuru se sab bataya."""
        create_image_text_layout(
            "attached_assets/chapter3/3.14.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ 
        🌆 Diti ki Ichchha

Diti, Daksha ki beti thi aur rishi Kaśyapa ki patni.
Ek shaam ka samay tha. Kaśyapa apni sandhya puja kar rahe the.

Tab Diti unke paas aayi.
Uska mann ichchha aur kaamna se bhara hua tha. Usne kaha:

“Mujhe santaan chahiye.”

“Meri saheliyon (co-wives) ke bachche hain, main unki khushi dekh kar dukhi ho jaati hoon.”

“Kripya meri ichchha poori kijiye.”

⏳ Kaśyapa ka Samjhana

Kaśyapa ne pyaar se samjhaya:

Patni pati ka aadha hissa hoti hai

Grihastha jeevan sabhi dharmon ko sambhalta hai

Main tumhari ichchha poori karunga

Lekin unhone ek zaroori baat kahi:

“Abhi shaam ka samay hai. Yeh shubh samay nahi hai.”

Unhone bataya:

Is samay bhuton ke swami Shiva apne ganon ke saath ghoomte hain

Yeh pavitra aur bhayanak samay hota hai

Is waqt santaan ka garbh dharan karna uchit nahi

😔 Diti ka Zidd

Par Diti ka mann kaamna se bhar gaya tha.
Woh ruk na paayi.

Usne apne pati se zidd ki aur ant mein Kaśyapa maan gaye.
Baad mein Diti ko apni galti ka ehsaas hua.

Woh dar gayi aur boli:

“Hey Prabhu, mere garbh ko Shiva nuksaan na pahunchaye. Maine galti ki hai.”

⚠️ Kaśyapa ka Shraap-jaisa Vachan

Kaśyapa ne kaha:

“Tumne galat samay par, ashuddh mann se aur meri baat na maan kar yeh kaam kiya hai.
Isliye tumhare do putra paida honge — bahut hi shaktishaali par atyant krur.”

Woh duniya ko satayenge

Logon ko dukh denge

Devta bhi pareshan honge

Aur ant mein:

Bhagwan khud avtaar lekar unhe maarenge.

Yahi do putra the:
Hiraṇyākṣa aur Hiraṇyakaśipu

🙏 Diti ki Prarthana

Diti ne shanti se kaha:

“Thik hai, agar mere bete marenge,
toh Bhagwan ke haath se maren.
Brahmanon ke shraap se na maren.”

Kyunki rishi ka shraap bahut bhayanak maana jaata tha.

🌟 Ek Achhi Bhavishyavaani

Kaśyapa ne phir kaha:

“Tum pachtayi ho, isliye tumhare vansh mein ek mahaan bhakt paida hoga.”

Woh tha:

👉 Prahlad

Bahut bada Vishnu bhakt

Sabse dayaalu

Kisi se dushmani nahi

Dusron ki khushi mein khush

Dusron ke dukh mein dukhi

Uski bhakti se Bhagwan khud prasann honge.

💫 Kahani ka Saar

Is kahani se kuch bade sabak milte hain:

Galat samay aur galat mann se kiya kaam bura phal deta hai

Pachtawa (repentance) se bhavishya sudhar sakta hai

Bure vansh mein bhi mahaan sant paida ho sakta hai

Bhagwan ke haath se mrityu bhi moksha ka raasta hoti hai

Aur sabse bada sach:

Hiraṇyākṣa aur Hiraṇyakaśipu jaise daityon ke ghar bhi Prahlad jaisa mahaan bhakt paida ho sakta hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 15
    with st.expander("Chapter 15 - Sanaka and Others curse Jaya and Vijaya"):
        text1 = """ 
        Chapter 15 – Sanaka aur Jaya-Vijaya ka Shraap (Saral Hinglish Kahani)

Rishi Maitreya ne Vidura ko ek aur gahri kahani sunayi.

🌑 Diti ke Garbh ka Asar

Diti apne garbh ko 100 saal tak sambhaal kar rakhti rahi.
Uska garbh itna powerful tha ki:

Suraj ki roshni kam padne lagi

Duniya andhere se bhar gayi

Devta kamzor mehsoos karne lage

Dar kar sab devta Brahma ji ke paas gaye aur bole:

“Prabhu, har taraf andhera chha gaya hai. Yeh kya ho raha hai? Hume bachaiye.”"""
        create_image_text_layout(
            "attached_assets/chapter3/3.15.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ 
        🧠 Brahma ne Sach Bataya

Brahma ji muskuraaye aur bole:

“Iska kaaran Diti ke garbh mein pal rahe do shaktishaali bachche hain.
Par main tumhe ek purani kahani sunata hoon, jo is sab se judi hai.”

🌸 Vaikunth ki Sundar Duniya

Brahma ji ne bataya:

Ek baar Sanaka, Sanandana, Sanatana aur Sanatkumara – ye chaar chhote bacchon jaise dikhne wale mahaan rishi – Vaikunth gaye.

Vaikunth kaisa tha?

Har jagah shanti aur prem

Log Vishnu jaise roop wale

Sab log bhakti mein magan

Har jagah phool, sugandh aur geet

Lakshmi ji wahan sadaa Vishnu ji ki seva karti thi.
Wahan koi dukh, gussa ya lalach nahi tha.

🚪 Saatve Dwaar Par Rukawat

Rishiyon ne Vaikunth ke 6 gates bina kisi rok-tok ke paar kar liye.
Lekin 7th gate par do pehredaar khade the:

Jaya aur Vijaya

Bahut shaktishaali

Vishnu ji ke sabse vishwasniya sevak

Unhone rishiyon ko roka aur andar jaane nahi diya.

Unhone socha:

“Yeh chhote bacchon jaise lag rahe hain. Kaun jaane kaun hain.”

😠 Rishiyon ka Gussa

Sanaka aur baaki rishi Vishnu se milne aaye the.
Roke jaane se unka dil dukha.

Unhone kaha:

“Vaikunth mein toh sab barabar hote hain.
Yahan koi bhed-bhaav nahi hota.
Phir tumne hume kyun roka?”

Unka gussa badh gaya.

Aur unhone shraap de diya:

“Tum dono Vaikunth chhod kar neeche ki duniya mein janam loge.
Wahan tumhe kaam, krodh aur lobh se bhari zindagi jeeni padegi.”

😢 Jaya-Vijaya ka Pachtawa

Jaya aur Vijaya turant samajh gaye ki unse galti ho gayi.

Woh rishiyon ke pair pakad kar bole:

“Hum apni sazaa sweekar karte hain.
Bas ek kripa kijiye —
Bhagwan ko hum bhool na jaayein.”

🌟 Vishnu Ji ka Aana

Tabhi Vishnu ji khud Lakshmi ji ke saath wahan aaye.

Unka roop bahut sundar tha:

Neela sa sharir

Peeli vastra

Chamakta mukh

Gale mein vanmala

Seene par Lakshmi ji

Rishiyon ne unhe dekha aur unki aankhon mein aansu aa gaye.
Unka mann poori tarah shant ho gaya.

🙏 Rishiyon ki Prarthana

Rishiyon ne kaha:

“Hey Prabhu, aaj humari aankhon ko sachcha sukh mila.
Aap hamesha hamare dil mein the, par aaj saamne dikh gaye.”

Unhone ye bhi kaha:

“Jo log aapki kahani sunte hain, unhe swarg ya moksha ki bhi parwah nahi rehti.
Unke liye sirf aapka prem hi sab kuch hota hai.”

💫 Kahani ka Gehraa Arth

Is ghatna ke kaaran:

Jaya aur Vijaya ko Vaikunth chhodna pada

Unka janam daitya ke roop mein hua

Wahi aage chal kar bane:

Hiranyaksha

Hiranyakashipu

Yaani Diti ke garbh wale bachche!

📖 Moral (Seekh)

Is kahani se kuch important baatein samajh aati hain:

Ahankaar ya shak kabhi kabhi galti karwa deta hai

Bade log bhi galti kar sakte hain

Bhagwan ke sevak bhi kabhi kabhi pariksha se guzarte hain

Jo Bhagwan ko sachche dil se yaad kare, woh unhe kabhi nahi bhoolta

Aur sabse bada sach:

Jo bhi hota hai, Bhagwan ki badi yojna ka hissa hota hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 16
    with st.expander("Chapter 16 - The Fall of Jaya and Vijaya"):
        text1 = """ 
        Chapter 16 – Jaya aur Vijaya ka Patan (Fall)
Brahma ji ne kahani batayi:
Jab rishiyon ne Bhagwan Vishnu ki stuti ki, tab Bhagwan unke saamne aaye.
Unhone unka bahut pyaar se swagat kiya aur shant swar mein bole.
Bhagwan Vishnu ne kaha:
“Hey rishiyon, mere do sevak Jaya aur Vijaya ne tumhara apmaan kiya.
Isliye tumne jo unhe shraap diya, main usse sweekar karta hoon.
Unki galti ko main apni galti maanta hoon.”
Unhone aur bhi kaha:
“Jo sevak galti karta hai, log uske malik ko dosh dete hain.
Isliye main tumse maafi maangta hoon.
Brahman mere liye sabse adhik poojya hain.”
Bhagwan ka swabhav bahut vinamra tha.
Woh kehte hain ki jo log sadhus, Brahman aur nirbal logon ka samman karte hain,
woh unhe bahut priya hain."""
        create_image_text_layout(
            "attached_assets/chapter3/3.16.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ 
        Rishiyon ka Uttar

Rishi Bhagwan ke shabd sunkar hairaan ho gaye.
Unhone haath jod kar kaha:

“Prabhu, aap sabse bade hain.
Aapko kisi se maafi maangne ki zarurat nahi.
Aap hi dharm ka mool hain.
Aap sabka sahara hain.”

Unhone kaha:

“Jo yogi aapko pa lete hain,
woh janam–maran ke chakkar se paar ho jaate hain.”

Bhagwan ka Faisla

Phir Bhagwan Vishnu ne shant swar mein kaha:

“Ye sab mere hi ichchha se hua hai.
Jaya aur Vijaya ab kuch samay ke liye prithvi par janam lenge.
Woh asur ke roop mein paida honge.
Par woh jaldi hi wapas mere paas laut aayenge.”

Bhagwan jaante the ki ye sab ek badi leela ka hissa hai.

Vaikunth se Girna

Bhagwan ka aadesh paakar,
Jaya aur Vijaya Vaikunth se gir gaye.

Swarg ke log unhe girta dekh kar dukhi ho gaye.
Har taraf se awaaz aayi,
“Alas! Alas!”

Par yeh sab Bhagwan ki ichchha se ho raha tha.

Naya Janam

Woh dono rishi Kashyap ke tej ke roop mein
Diti ke garbh mein pravesh kar gaye.

Ab woh asur ke roop mein janam lene wale the.

Yahi aage chal kar do shaktishaali rakshas bane,
jinse devta bhi darrne lage.

Par sach yeh tha:
Unka patan bhi Bhagwan ki yojna ka hissa tha.
Taaki woh phir se unke paas laut sakein.

Moral (Seekh)

Kabhi-kabhi buri ghatna bhi kisi bade kaam ka hissa hoti hai.
Har girna hamesha haar nahi hota.
Kabhi-kabhi girkar hi insaan apne asli ghar tak pahunchta hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 17
    with st.expander("Chapter 17 - The Birth of Hiraṇyākṣa and Hiraṇyakaśipu"):
        text1 = """ 
        Chapter 17 – Hiranyaksha aur Hiranyakashipu ka Janm aur Unki Shakti
Maitreya Rishi ne kahani aage batayi:
Jab Brahma ji ne sab sach bataya, tab devtaon ka dar thoda kam ho gaya.
Woh sab apne swarg lok wapas chale gaye.
Par Diti ka mann shant nahi tha.
Use pata tha ki uske bachche duniya mein pareshani la sakte hain.
Isi darr ke saath usne 100 saal baad do judwa putron ko janam diya."""
        create_image_text_layout(
            "attached_assets/chapter3/3.17.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ 
        Janm ke Samay Ashubh Sanket

Jab dono bachche paida hue, tab duniya mein ajeeb ghatnayein hone lagi.

Zameen zor se hilne lagi.
Pahad kaanpne lage.
Aasmaan mein bijli chamki aur andhera chha gaya.

Samundar zor se garajne laga.
Nadiyan aur talab bhi bechain dikhne lage.

Kutton ne ajeeb awaaz mein bhonkna shuru kar diya.
Gadhe zor zor se cheekhne lage.
Ullu aur lomdiyaan daraavni awaaz karne lagi.

Gaayen dar gayin, ped bina hawa ke girne lage.
Murtiyon ki aankhon se aansu behte dikhe.

Log bahut dar gaye.
Unhe laga shayad duniya ka ant aa gaya hai.

Do Balwan Asur

Samay ke saath woh dono bachche bade hone lage.
Unke sharir pahadon ki tarah mazboot the.
Unki lambai aasmaan ko chhoone jaise thi.
Har kadam se zameen hilti thi.

Rishi Kashyap ne unke naam rakhe:

Bade bhai ka naam tha Hiranyakashipu

Chhote bhai ka naam tha Hiranyaksha

Hiranyakashipu ko Brahma ji se vardaan mila tha.
Isliye use maut ka darr nahi tha.
Woh bahut ghamandi ho gaya.

Usne apni taqat se teenon lokon par kabza kar liya.

Hiranyaksha ka Ghamand

Hiranyaksha apne bhai ko bahut pyar karta tha.
Par use ladai ka bahut shauk tha.
Har din woh gada lekar kisi se ladne nikal padta.

Ek din woh swarg pahunch gaya.
Uski chal aur shakti dekh kar devta darr gaye.
Sab chhup gaye, jaise Garud ko dekh kar saamp chhup jaate hain.

Jab use koi ladne wala nahi mila,
toh woh zor se hansa aur garja.

Samundar ki Ore

Phir woh samundar mein ghus gaya.
Uski saanson aur gada ki taqat se bade bade lehr uthne lage.

Samundar ke sab jeev darr kar bhaag gaye.

Kai saalon tak woh samundar mein ghoomta raha,
kisi takkar ke dushman ki talash mein.

Aakhir woh Varun dev ke shehar pahunch gaya.

Varun Dev se Chunauti

Hiranyaksha ne Varun dev ka mazaak udaya aur bola:

“Tum bade yoddha ho. Mujhse ladho!”

Varun dev gusse mein the, par unhone apne aap ko sambhala.
Unhone shant swar mein kaha:

“Main ab buddha ho chuka hoon.
Main tumse ladne layak nahi.”

Phir unhone sach bataya:

“Sirf ek hi yoddha hai jo tumse lad sakta hai.
Woh hai Adi Purush – Bhagwan Vishnu.”

“Unhi ke paas jao.
Wahi tumhara ghamand tod sakte hain.”

Moral (Seekh)

Jab insaan ya koi bhi jeev bahut ghamandi ho jata hai,
toh woh hamesha kisi na kisi se takraane ki sochta hai.

Par sachchi shakti hamesha vinamrata mein hoti hai.
Ghamand ka anth hamesha nishchit hota hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 18
    with st.expander("Chapter 18 - Hiraṇyākṣa’s Fight with Varāha"):
        text1 = """ 
        Chapter 18 – Hiranyaksha aur Varaha ka Maha-yuddh

Maitreya Rishi ne Vidura ko aage ki ghatna batayi:

Varaha ko Chunauti

Jab Hiranyaksha ne Varun dev ki baat suni, to usne usse ignore kar diya.
Narad se usse pata chala ki Bhagwan Vishnu Varaha roop me prithvi ko bachane aaye hain.
Ye sunte hi woh turant Rasatal (patal lok) ki taraf daud pada.

Wahan usne ek adbhut drishya dekha:

Bhagwan Varaha apne bade daanton (tusks) par dharti ko uthakar paani se bahar la rahe the.
Unki aankhen tej se chamak rahi thi.

Hiranyaksha hans pada aur bola:

“Ye kya hai? Ek jangli janwar!
Dharti chhod do. Ye hamare lok ki hai.
Tum ise yahan se nahi le ja sakte.”

Usne Bhagwan ka mazaak udaya aur unhe ladai ki khuli chunauti di."""
        create_image_text_layout(
            "attached_assets/chapter3/3.18.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ 
        Varaha ka Dhairya

Hiranyaksha ne bahut kathor aur apmaan bhare shabd bole.
Par Bhagwan Varaha ne pehle uski baat ko nazarandaaz kiya.

Kyun?

Kyuki unki pehli zimmedari thi dharti ko surakshit jagah par rakhna.

Jaise ek hathi pehle apni saathi ko bachata hai,
waise hi Varaha prithvi ko surakshit jagah par rakh kar bahar nikle.

Phir unhone prithvi ko paani par sthir kar diya aur usme apni shakti daal di,
taaki woh tik sake.

Devta aur Brahma ji ne un par phool barsaye.

Yuddh ki Shuruaat

Ab Bhagwan Varaha ne Hiranyaksha ki taraf dekh kar halka sa vyangya kiya:

“Tum jaise jangli praniyon se hi ladne ke liye main aaya hoon.
Jo maut ke paas bandhe hote hain, wahi itna ghamand karte hain.”

Ye sunkar Hiranyaksha aur gusse se bhar gaya.

Usne apni bhari gada uthai aur zor se Varaha par hamla kiya.

Bhayankar Gada-Yuddh

Hiranyaksha ne gada se zor ka vaar kiya

Varaha ne bahut asani se side hoke us vaar ko taal diya

Phir Varaha ne bhi apni gada se us par prahar kiya

Dono ek dusre par lagatar vaar karne lage

Unke sharir se khoon nikalne laga.
Gusse me dono aur bhayankar ho gaye.

Unka yuddh bilkul do balwan saandon ki tarah lag raha tha jo ek hi gaay ke liye lad rahe hon.

Brahma ji ka Aana

Is maha-yuddh ko dekhne ke liye Brahma ji aur bahut se rishi wahan aa gaye.

Brahma ji ne Bhagwan Varaha se kaha:

“Ye bahut hi khatarnak asur hai.
Isne devtaon, rishiyon aur nirbal jeevon ko bahut sataya hai.”

“Isse halka mat lo.
Bachche ki tarah isse khel mat samjho.
Ye maya ka gyani aur bahut ghamandi hai.”

Phir unhone chetavani di:

“Abhi sandhya ka samay aane wala hai.
Us samay ye aur bhi shaktishaali ho sakta hai.”

“Isse jaldi maar do,
taaki devtaon ka kalyan ho aur duniya me shanti wapas aaye.”

Is Adhyay ka Arth

Is part me teen baatein samajh aati hain:

Bhagwan pehle dharma ka kaam karte hain, baad me yuddh.
– Varaha ne pehle prithvi bachayi, phir asur se lade.

Ghamand andha bana deta hai.
– Hiranyaksha ko laga koi uska muqabla nahi kar sakta.

Buraai ka anth nishchit hota hai.
– Jab adharm badhta hai, tab Bhagwan swayam aate hain use rokne."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 19
    with st.expander("Chapter 19 - Varāha kills Hiraṇyākṣa"):
        text1 = """ 
        Chapter 19 – Varaha dwara Hiranyaksha ka vadh (antim yuddh)

Maitreya Rishi ne Vidura ko bataya ki Brahma ji ki baat sunkar Bhagwan Varaha muskuraye.
Unhe kisi shubh muhurat ki zarurat nahi thi, kyunki samay swayam unka hi roop hai.
Phir bhi, unhone prem se Brahma ki baat sweekar ki aur yuddh shuru hua."""
        create_image_text_layout(
            "attached_assets/chapter3/3.19.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ 
        Gada se yuddh

Varaha ji ne seedha Hiranyaksha par hamla kiya aur apni gada se uske thodi (chin) par prahar kiya.
Lekin ek ajeeb ghatna hui:

Asur ne bhi zor ka prahar kiya

Varaha ki gada unke haath se gir gayi

Yeh dekhkar sab chakit ho gaye.

Sabse chaukane wali baat:
Hiranyaksha ne bina hathiyaar ke khade Bhagwan par vaar nahi kiya.
Usne yuddh ke niyam ka samman kiya.

Bhagwan ne uski is maryada ko saraha,
lekin phir apna divya Sudarshan chakra yaad kiya.

Yuddh aur tez ho gaya

Ab Varaha chakra lekar khade the.
Hiranyaksha gusse se kaamp raha tha.

Usne zor se chillakar phir hamla kiya.
Apni gada se Bhagwan par vaar kiya.

Varaha ne asani se us vaar ko pair se hata diya

Fir bole: “Apna hathiyaar uthao, phir se koshish karo”

Par jab uski shakti kam padne lagi,
to usne trishul uthaya aur Bhagwan ke seene par phenka.

Varaha ne turant Sudarshan se us trishul ko tukde-tukde kar diya.

Asur ki maya

Ab Hiranyaksha ne kala jaadu (asuri maya) ka sahara liya.

Achanak:

Tez aandhiyaan chalne lagi

Andhera chha gaya

Patthar barasne lage

Aasmaan se khoon, haddiyan, gandagi girne lagi

Pahadon se hathiyaar girte dikhe

Bhayanak rakshasiyan nazar aane lagi

Sab log dar gaye.
Aisa lagne laga jaise pralay aa gaya ho.

Lekin Varaha ne Sudarshan chakra chala kar
uski saari maya turant samaapt kar di.

Antim pal

Ab Hiranyaksha bilkul gusse me Bhagwan par jhapta
aur unhe pakadne ki koshish ki.

Par wo unhe pakad nahi paaya.

Phir usne mukke se Bhagwan ke seene par prahar kiya.
Varaha par iska koi asar nahi hua.

Tab Bhagwan ne ek hi zor ka prahar kiya —
apne haath se uske kaan ke neeche.

Bas, wahi antim pal tha.

Hiranyaksha:

Jad se ukhaade hue bade ped ki tarah gir pada

Uska sharir toot gaya

Aankhen bahar aa gayin

Haath-pair bikhar gaye

Ek hi prahar me uska ant ho gaya.

Asur ki antim sthiti

Jab wo mar raha tha,
uski nazar Bhagwan ke mukh par tik gayi.

Yeh bahut gehri baat hai:

Jo yogi saalon tak tapasya karke
Bhagwan ka darshan chahte hain,
Hiranyaksha ko wahi darshan mrityu ke samay mil gaya.

Isliye rishiyon ne kaha:

“Kitni mahaan mrityu hai ye!”

Jaya–Vijaya ka rahasya

Rishiyon ne bataya:

Ye asur asal me Bhagwan ke dwarpal the
(Jaya aur Vijaya).

Shraap ke kaaran unhe asur roop me janam lena pada.
Is janam me Hiranyaksha aur Hiranyakashipu bane.

Kuch aur janmon ke baad wo phir Vaikunth laut jayenge.

Devtaon ki stuti

Devta bole:

“Prabhu, aapne duniya ko bachaya.
Ye asur sabko satata tha.
Aaj hum aapke charnon me sharan paakar khush hain.”

Bhagwan Varaha phir Vaikunth laut gaye.

Is kahani ka phal

Is adhyay ka bada mahatva bataya gaya:

Jo vyakti:

Is kahani ko sunta hai

Ya sunata hai

Ya isme bhakti se man lagata hai

Uske:

Paap kam hote hain

Yash, dhan, aur ayu badhti hai

Yuddh ya mushkil samay me raksha hoti hai

Ant me Bhagwan Narayan ki prapti hoti hai

Gehri samajh

Ye poora prasang ek bada sandesh deta hai:

Adharm kitna bhi shaktishaali ho, ant me dharm jeetta hai

Bhagwan jab chahen, tab ek pal me sab badal sakte hain

Ghamand ka anth nishchit hai

Bhagwan ke shatru bhi ant me unhi tak pahunch jaate hain

Yahi Varaha avatar ki mahaan leela ka samapan hai."""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 20
    with st.expander("Chapter 20 - Various Creations of Brahmā"):
        text1 = """ 
        Chapter 20 – Brahma ji ki alag-alag srishti (Creation ki kahani)

Shaunaka Rishi ne Suta se poocha,
“Jab prithvi ko sthir kar diya gaya, tab Manu ne aage ki srishti kaise badhai?
Aur Vidura ne Maitreya se kya-kya prashn kiye?”

Suta ne shant mann se kahani shuru ki."""
        create_image_text_layout(
            "attached_assets/chapter3/3.20.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ 
        Vidura ka prashn

Vidura Bhagwan ke bade bhakt the.
Unhone Maitreya Rishi se poocha:

“Brahma ji ne prajapatiyon ko paida karne ke baad
is duniya ko aage kaise rachaa?
Kya unhone apni patniyon ke saath milkar srishti banayi?
Ya alag-alag banayi?”

Maitreya ne dheere se samjhaya.

Srishti ki shuruaat

Sabse pehle prakriti se “Mahat tattva” nikla.
Phir usse “ahankaar” bana.
Usse dheere-dheere sab kuch bana:

Panch tattva (jal, agni, vayu, aakash, prithvi)

Indriyaan

Devta jo unka niyantran karte hain

Jab sab cheezein ek saath aayi,
tab ek bada sona jaisa anda bana.
Usme Bhagwan ki shakti pravesh hui.

Phir us anda se ek kamal nikla.
Us kamal par Brahma ji prakat hue.
Unhone fir poori duniya ko dobara rachna shuru ki.

Agyan ki rachna

Sabse pehle Brahma ji ne agyan (ignorance) ke roop banaye.
Ye andhera aur bhram failate the.

Unhe ye pasand nahi aaya,
to unhone apna wo roop chhod diya.

Us roop ko Yaksh aur Rakshas ne apna liya.
Unme bhook aur pyaas bahut zyada thi.

Woh Brahma ji par hi toot pade.
Brahma ji ghabra gaye aur bole:

“Main tumhara hi pita hoon, mujhe mat khaao!”

Din aur raat ka janm

Phir Brahma ji ne roshni se devta banaye.
Unhone din ko apna maana.

Phir neeche ke hisse se kuch asur paida hue.
Woh bahut bhog aur vasna se bhare the.
Woh Brahma ji ke peeche pad gaye.

Brahma ji darr kar Bhagwan Hari ke paas gaye
aur unse madad maangi.

Bhagwan ne kaha,
“Apna ye sharir chhod do.”

Jaise hi Brahma ji ne wo roop chhoda,
wo “sandhya” yani shaam ka roop ban gaya.

Asur use ek sundar stri samajh kar usme phans gaye.
Aur Brahma ji wahan se bach nikle.

Aur bhi prajatiyon ka janm

Phir Brahma ji ne alag-alag roop se kai prajatiyan banayi:

Gandharv aur Apsara – apni sundarta se

Bhoot-pret – apni thakan se

Nidra (sleep) – jab unhone aankhen band ki

Pitru aur Sadhya – apni adhyatmik shakti se

Siddh aur Vidyadhar – apni gupt shakti se

Kinnar aur Kimpurush – apni pratibimb (reflection) se

Yeh sab dheere-dheere duniya ko bharne lage.

Saanp ka janm

Ek baar Brahma ji ne gusse me ek roop chhod diya.
Us roop ke baal zameen par gire
aur unse saanp paida ho gaye.

Kuch bade hood wale naag bane.
Kuch tez aur bhayanak bane.

Manu ka janm

Akhir me Brahma ji ne apne mann se
Manu ko paida kiya.

Manu logon ki sankhya badhane wale the.
Unhone Brahma ji ka roop apnaya
aur dharm ke saath duniya ko basana shuru kiya.

Sab prani khush ho gaye aur bole:

“Brahma ji, aapne bahut achha kiya.
Ab sab kuch sahi tarah se chal raha hai.”

Rishiyon ki srishti

Ant me Brahma ji ne rishiyon ko paida kiya.

Unhe diya:

Tapasya

Gyaan

Yog

Dhyan

Vairagya

Ye rishi duniya ko sahi raasta dikhane ke liye bane.

Is kahani ka arth

Ye kahani batati hai:

Srishti ek hi baar me nahi bani

Dheere-dheere alag-alag roop me bani

Har cheez ka apna kaam hai

Roshni, andhera, din, raat, sab ek balance ka hissa hai

Aur sabse bada sach:

Sab kuch Bhagwan ki ichchha se hi chal raha hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 21
    with st.expander("Chapter 21 - Kardama’s Penance—Viṣṇu’s Boon"):
        text1 = """ 
        Chapter 21 – Kardama ki Tapasya aur Vishnu ka Vardan (Hinglish Kahani)

Ek din Vidura ne Maitreya Rishi se pucha,
“Hey Mahatma, mujhe Svayambhuva Manu ke vansh ke baare mein batao. Unke bachche kaise hue aur Kardama Rishi ne Devahuti se kitne santan paaye?”

Maitreya muskuraaye aur kahani shuru ki."""
        create_image_text_layout(
            "attached_assets/chapter3/3.21.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ 
        Kardama ki kathin tapasya

Brahma ji ne Kardama Rishi ko kaha tha,
“Tum praja badhao. Sansar ko aage badhao.”

Is aadesh ko maan kar Kardama Saraswati nadi ke kinare chale gaye.
Wahan unhone 10,000 saal tak tapasya ki.

Woh shant, dhyani aur bhakti se bhare hue the.
Unka mann sirf Bhagwan Vishnu me laga rehta tha.

Din-raat unhone ek hi prarthana ki:
“Hey Prabhu, mujhe darshan do.”

Vishnu ka divya darshan

Ek din unki tapasya safal hui.

Achanak aasman me tej prakash chha gaya.
Kardama ne dekha — Bhagwan Vishnu saamne khade hain.

Unka roop bahut sundar tha:

Neel rang jaisa shant sharir

Komal kamal jaisa chehra

Sir par mukut

Haath me shankh, chakra, gada aur kamal

Garud par virajmaan

Seene par Lakshmi ka chinh

Unki muskaan dekh kar Kardama ka dil khushi se bhar gaya.

Woh turant zameen par gir kar pranam karne lage.

Kardama ki vinamra prarthana

Kardama bole:

“Hey Prabhu, aaj meri aankhon ka sachcha upyog ho gaya.
Aapke darshan se hi jeevan safal ho gaya.

Aapke charan samundar se paar karne wali naav jaise hain.
Jo aapko pa leta hai, use sab kuch mil jata hai.”

Phir unhone sharmate hue apni ichchha batayi:

“Prabhu… mujhe ek patni chahiye.
Aisi jo dharmik ho, shaant ho, aur ghar ko sambhale.
Mujhe grihastha jeevan jeena hai aur apne kartavya nibhaane hain.”

Vishnu ka pyara vachan

Bhagwan Vishnu muskuraaye.

Unhone kaha:

“Kardama, tumhari tapasya kabhi bekaar nahi jaati.
Mujhe tumhari ichchha pehle se pata thi.”

Phir unhone bataya:

“Do din baad Raja Manu yahan aayenge.”

“Woh apni beti Devahuti ko tumse shaadi ke liye denge.”

“Tum dono se 9 betiyan paida hongi.”

“Unse rishi aur mahaan vansh aage badhega.”

Phir Vishnu ne ek bada rahasya bataya:

“Main khud tumhare ghar janam loonga.
Tumhare putra ke roop me.
Aur duniya ko sachchai ka gyaan sikhaunga.”

(Kapil Dev ka janm isi ka sanket tha.)

Kardama ka mann anand se bhar gaya.

Vishnu ka antardhaan

Vishnu ji ne ashirvad diya aur Garud par baithkar chale gaye.
Kardama wahi khade unhe jaate dekhte rahe.

Ab woh shanti se Manu ke aane ka intezar karne lage.

Manu ka aagman

Kuch din baad Raja Manu apni patni aur beti Devahuti ke saath rath me baith kar Kardama ke ashram pahunche.

Ashram bahut sundar tha:

Ped, phool aur phal har taraf the

Pakshi madhur awaaz me ga rahe the

Hiran, haathi aur mor aas paas ghoom rahe the

Saraswati ka pavitra jal chamak raha tha

Ye wahi jagah thi jahan Vishnu ki kripa ke aansu gir kar ek pavitra sarovar ban gaya tha — Bindusar.

Kardama aur Manu ki mulaqat

Manu ne Kardama ko dekha.

Rishi ka sharir tapasya se tejomay tha.
Unke baal jataon me the.
Kapde saade the.
Par unka chehra shanti se bhara tha.

Kardama ne Raja ka satkaar kiya aur kaha:

“Hey Rajan, aap dharti par Vishnu ke pratinidhi ho.
Aap dharm ki raksha karte ho aur bure logon ko rokte ho.

Agar raja apna kaam na kare,
to duniya me paap badh jaata hai.”

Phir pyaar se pucha:

“Aap yahan kis kaam se aaye ho?
Main aapki madad karne ko tayyar hoon.”

Kahani ka saar

Is adhyay ka message simple hai:

Sachi tapasya kabhi bekaar nahi jaati.

Bhagwan bhakti se khush hote hain.

Jo sachcha mann se prarthana karta hai, uski ichchha poori hoti hai.

Aur kabhi-kabhi, Bhagwan khud uske ghar janam lene ka vachan dete hain.

Yahan se Devahuti aur Kardama ki shaadi ki kahani shuru hoti hai…
Aur aage chal kar unke ghar Bhagwan Kapil ka janm hota hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 22
    with st.expander("Chapter 22 - Marriage of Kardama and Devahūti"):
        text1 = """ 
        Chapter 22 – Kardama aur Devahuti ki Shaadi (Hinglish Kahani)

Maitreya Rishi ne kahani aage badhayi.

Raja Manu ne jab Kardama Rishi ki baatein suni, to woh thoda sharma gaye.
Unhe apni beti ke liye achha jeevan saathi chahiye tha.
Unhone dheere se apni baat rakhi."""
        create_image_text_layout(
            "attached_assets/chapter3/3.22.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ 
        Raja Manu ki vinamra prarthana

Manu bole:

“Hey Rishi, Brahma ji ne Brahmanon ko gyaan aur tapasya ke liye banaya.
Aur hum Kshatriya log unki raksha ke liye bane hain.
Hum ek dusre ka sahara hain.”

Phir unhone pyaar se kaha:

“Meri ek beti hai — Devahuti.
Woh sundar hai, vinamra hai aur achhe gunon se bhari hai.
Usne Narad ji se aapki mahanta ke baare mein suna hai.”

Manu ne halka sa muskura kar kaha:

“Usne mann hi mann aapko apna pati maan liya hai.
Agar aap sweekar karein, to main uska haath aapko dena chahta hoon.”

Unki awaaz me pyaar aur chinta dono the.
Ek pita ka dil bol raha tha.

Kardama ka jawab

Kardama Rishi ne shant mann se jawab diya:

“Rajan, main bhi shaadi karna chahta hoon.
Aapki beti pavitra aur gunvaan hai.
Main usse sweekar karta hoon.”

Phir unhone ek baat aur kahi:

“Main uske saath tab tak grihastha jeevan jeeyunga jab tak hume ek santan na ho jaye.
Uske baad main fir se tapasya aur gyaan ke raaste par chalunga.”

Devahuti yeh sab sun rahi thi.
Kardama ki muskaan dekh kar uska dil shant ho gaya.
Usne chup-chaap unhe apna pati maan liya.

Shaadi ka pavitra samay

Manu aur Rani Shatarupa bahut khush hue.
Unhone apni pyari beti ki shaadi Kardama Rishi se kar di.

Rani ne pyaar se beti ko:

Sundar kapde

Gehne

Ghar ke upyogi saaman

sab diya.

Par shaadi ke baad jab vidai ka samay aaya,
to Manu ka dil bhar aaya.

Unhone Devahuti ko gale lagaya.
Unki aankhon se aansu ruk nahi rahe the.

“Hey beti… meri pyari bachchi…”
Kehte hue unhone uske baal aansuon se bhigo diye.

Yeh ek pita ka dard tha.
Khushi bhi thi… aur judai ka dukh bhi.

Manu ka wapas jana

Vidai ke baad Manu aur Shatarupa rath me baith kar apne mahal laut gaye.
Raaste me unhone Saraswati nadi ke kinare sundar ashram dekhe.
Santo ka shaant jeevan dekh kar unka mann prasann ho gaya.

Jab woh apne rajya pahunchhe,
to logon ne gaane gaakar unka swagat kiya.

Manu ne wahan dharm ke saath rajya chalaya.
Roz subah woh Bhagwan Vishnu ki kahaniyan sunte the.
Unka mann hamesha bhakti me laga rehta tha.

Isi bhakti ki wajah se:

Unhe dukh chhoo nahi paata tha

Unka jeevan shant aur pavitra tha

Kahani ka saar

Is adhyay me hume 3 sundar baatein milti hain:

Ek pita hamesha apni beti ke liye best chahta hai.

Shaadi sirf rishta nahi, ek dharm aur zimmedari hai.

Jo bhakti aur sachchai se jeeta hai, uska jeevan sukh se bhara hota hai.

Ab kahani aage badhegi…
Devahuti ke jeevan me kya hua, aur kaise unka bhagya chamka."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 23
    with st.expander("Chapter 23 - Married Life of Kardama and Devahūti"):
        text1 = """ 
        Chapter 23 – Kardama aur Devahuti ka Grihastha Jeevan (Simple Hinglish Summary)

Jab Devahuti ke maa-baap wapas chale gaye, tab usne apne pati Kardama Rishi ki seva poore prem aur shraddha se karni shuru ki — bilkul waise hi jaise Parvati ji Shiv ji ki seva karti hain.

Devahuti ki seva aur tapasya

Devahuti ne:

Gussa, lalach, ahankar aur buri aadatein chhod di

Apne mann aur sharir ko pavitra rakha

Hamesha vinamrata se baat ki

Pati ki seva mein khud ko samarpit kar diya

Woh itni tapasya aur seva karti rahi ki uska sharir kamzor aur patla ho gaya.

Kardama Rishi uski bhakti aur seva dekhkar bahut prabhavit hue."""
        create_image_text_layout(
            "attached_assets/chapter3/3.23.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ 
        Kardama ka vardaan

Ek din Kardama ne prem se kaha:

“Tumne apne sharir tak ki parwah nahi ki aur meri itni seva ki.
Meri tapasya aur yog se jo bhi divya shakti aur sukh mila hai, us sab par tumhara bhi adhikaar hai.”

Unhone Devahuti ko divya drishti dene ka vachan diya aur kaha ki ab woh swarg jaise sukh bhog sakti hai.

Devahuti ki ichchha

Devahuti ne sharmate hue kaha:

“Hey prabhu, aap sab kuch kar sakte hain.
Aapne vachan diya tha ki hume santan prapt hogi.
Kripya uske liye ek sundar grih (mahal) bana dijiye.”

Yog shakti se bana hawa mein udne wala mahal

Kardama Rishi ne dhyaan lagaya aur apni yog shakti se ek adbhut vimaan-mahal bana diya:

Jo mann ke hisaab se kahin bhi ja sakta tha

Ratno se saja hua tha

Sone, heere aur motiyon se chamakta tha

Alag-alag kamre, bistar, baag aur manoranjan ke sthal the

Har mausam mein sukh dene wala tha

Woh kisi swarg se kam nahi tha.

Devahuti ka roop parivartan

Kardama ne kaha:
“Pehle tum pavitra kund mein snaan karo.”

Jab Devahuti ne snaan kiya, tab:

Hazaar sundar dasiyan wahan mil gayin

Unhone usse nahaya, sajaya aur naye kapde pehnaye

Gehno se saja diya

Aaine mein dekhkar Devahuti ne apne aap ko pehchaan hi nahi paayi.
Woh phir se apne purane sundar roop mein aa gayi.

Dono ka sukhmay jeevan

Kardama aur Devahuti us vimaan mein baithkar:

Meru parvat ke sundar sthalon par ghoome

Swarg jaise bagichon mein rahe

Bahut saalon tak sukh aur prem se jeevan bitaya

Yog shakti ke kaaran unhe samay ka pata hi nahi chala.
100 saal ek pal jaise beet gaye.

Nau betiyon ka janm

Kardama Rishi ne apni yog shakti se apne aap ko 9 roop mein baant diya.
Iske baad Devahuti ne ek hi samay 9 sundar betiyon ko janm diya.

Sab betiyan kamal ki sugandh jaisi pavitra aur sundar thi.

Devahuti ka dar

Devahuti ko mehsoos hua ki ab Kardama Rishi jaldi sanyas lene wale hain.
Woh andar se dukhi ho gayi, par bahar se muskurakar boli:

“Apne sab vachan poore kar diye.
Par jab aap chale jaoge, to meri dekhbhaal kaun karega?
Mujhe ek putra chahiye jo mujhe sahara de.”

Phir usne ek gehri baat kahi:

“Main indriya sukhon mein hi uljhi rahi aur aapki asli mahanta ko nahi samajh paayi.
Aapke saath rehkar mujhe moksha ke baare mein sochna chahiye tha.”

Usne samjha:

Bure logon ka sang = dukh aur janm-mrityu ka chakra

Achhe logon ka sang = vairagya aur mukti ka raasta

Is adhyay ka saar

Yeh chapter 3 main baatein sikhata hai:

Sachi seva aur prem se divya kripa milti hai

Yog aur tapasya se kuch bhi sambhav hai

Sansarik sukh milne ke baad bhi antim lakshya moksha hi hota hai

Aage ke chapter mein Devahuti ko ek aisa putra milta hai jo mahaan rishi banta hai — Kapil Muni."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 24
    with st.expander("Chapter 24 - Kapila-Incarnation"):
        text1 = """ 
        Chapter 24 – Kapila Avatar (Hinglish Moral Story)

Devahūti jab dukhi mann se boli,
toh dayaalu Kardama Rishi ne Bhagwan Vishnu ke vachan yaad karke use shaant kiya.

Rishi ka vachan

Kardama ne pyar se kaha:
“Hey nirdosh rajkumari,
apne mann ko itna kasht mat do.
Avinashi aur shashvat Prabhu khud tumhare garbh mein aane wale hain."""
        create_image_text_layout(
            "attached_assets/chapter3/3.24.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ 
        Tumne vrat rakhe hain, sanyam rakha hai,
daan, tapasya aur shraddha se bhakti ki hai.
Isi se prasann hokar Bhagwan Vishnu
tumhare putra ke roop mein janm lenge.

Woh tumhe Brahma-gyan denge
aur tumhare hriday ka ahankar aur bandhan tod denge.”

Devahūti ne apne pati ki baat poori shraddha se maan li
aur apna jeevan Ishwar-bhakti mein laga diya.

Kapila ka janm

Kuch samay baad,
bilkul waise hi jaise lakdi mein aag prakat hoti hai,
waise hi Bhagwan Vishnu ne Kapila ke roop mein janm liya.

Us din:

Aakash mein badal garajne lage

Devtaon ke vaady bajne lage

Gandharv gaane lage

Apsarayein nritya karne lagi

Aakash se phool barasne lage

Sab dishaayein shuddh ho gayi.
Paani nirmal ho gaya.
Logon ke mann shaant ho gaye.

Brahma ji ka aagaman

Bhagwan Brahma,
Marichi jaise rishiyon ke saath aaye.

Brahma ji ne kaha:
“Hey Kardama,
tumne meri aagya ka palan kiya.
Yeh putra swayam Param Purush hai
jo gyaan ke liye avatar lekar aaye hain.

Yeh Kapila ke naam se prasiddh honge.
Yeh Sankhya gyaan ka prachar karenge
aur logon ko moksha ka raasta dikhayenge.”

Kardama ka nivedan

Sab betiyon ka vivaah mahan rishiyon se karwane ke baad,
Kardama Rishi ne akele mein Kapila ke charanon mein pranam kiya aur kaha:

“Prabhu,
aapne mere ghar janm lekar
mera har rin chuka diya.

Ab main sansaar chhodkar
aapka dhyaan karte hue van ki or jaana chahta hoon.”

Bhagwan Kapila ka updesh

Kapila bole:
“Tum nishchint ho jao.
Tumhara jeevan safal ho chuka hai.

Is avatar ka uddeshya hi yahi hai
ki main atma-gyan ka raasta phir se sthapit karoon.

Tum apne karm mujhe samarpit karke
bhay aur mrityu ke bandhan se mukt ho jaoge.

Aur main apni maa Devahūti ko bhi
aisa gyaan doonga
jisse woh bhi sansaar ke dukh se paar ho jaayengi.”

Kardama ka sanyas aur moksha

Kapila ki aagya paakar,
Kardama Rishi ne sab kuch chhod diya.

Ghar

Agni

Bandhan

Ahankar

Woh van-van bhatak kar sirf Parmatma ka dhyaan karne lage.

Unhone:

Sukh-dukh ko samaan dekha

Sab praniyon mein ek hi atma dekhi

Apne aap ko Ishwar mein aur Ishwar ko apne aap mein dekha

Ant mein,
bhakti aur gyaan ke bal par
Kardama Rishi ne moksha prapt ki.

Is adhyay ka sandesh 🌱

Sachi bhakti ka phal khud Bhagwan hote hain

Gyaan aur vairagya se hi bandhan toot-te hain

Achha sang moksha ki or le jaata hai

Mata Devahūti aur Kapila ka sambandh maa aur guru dono ka hai

Agle adhyay mein,
Kapila apni maa Devahūti ko gyaan dete hain,
jo bhakti aur Sankhya darshan ka saar hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 25
    with st.expander("Chapter 25 - Dialogue between Kapila and Devahūti: Importance of the Bhakti-yoga"):
        text1 = """ 
        Chapter 25 – Kapila aur Devahūti ka Samvad (Bhakti-Yoga ki Mahima)

Kardama Rishi van chale gaye the.
Kapila apni maa Devahūti ke saath Bindusar mein rehne lage.
Unka mann ek hi baat mein tha —
apni maa ko sachcha gyaan dena.

Devahūti ka dukh

Ek din Devahūti ne pyar se kaha:"""
        create_image_text_layout(
            "attached_assets/chapter3/3.25.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ 
        “Mere beta,
ab main indriyon ke sukh se thak chuki hoon.
In sab ke peeche bhaagte-bhaagte
main andhere mein kho gayi hoon.

Bahut janmon ke baad
mujhe tum mile ho.
Tum meri aankhon ka sachcha ujala ho.

Mujhe batao,
kaise is moh-maya se bahar niklu?
Kaise ‘main’ aur ‘mera’ ka jo jadoo hai
woh toot sakta hai?”

Unhone haath jodkar kaha:
“Main tumhari sharan aayi hoon.
Mujhe sachcha raasta dikhao.”

Kapila muskura diye.
Unhe apni maa ki sachchi ichchha dekh kar khushi hui.

Kapila ka gyaan

Kapila ne shant swar mein kaha:

“Ma,
jo Yoga atma ko pehchaan leta hai,
wahi moksha ka raasta hai.

Dukh aur sukh dono ka ant wahi karta hai.

Sabse bada raaz ye hai:
Mann hi bandhan hai, aur mann hi mukti.

Jab mann indriyon ke peeche bhaagta hai → bandhan

Jab mann Bhagwan mein lagta hai → mukti

Jab mann se lobh, kaam aur ahankar nikal jata hai,
tab woh shant ho jata hai.
Tab insaan apni asli atma ko jaan leta hai.”

Bhakti ka sabse bada raasta

Kapila ne aage kaha:

“Ma,
Bhagwan ki bhakti se bada koi raasta nahi.

Jo asakti duniya se hoti hai,
woh jeev ko baandh leti hai.
Par agar wahi asakti
sant logon se ho jaye,
toh wahi mukti ka darwaza ban jaati hai.”

Unhone santon ke gun bataye:

Woh dayaalu hote hain

Sabke dost hote hain

Kisi se dushmani nahi rakhte

Shant aur pavitra hote hain

Woh sirf Bhagwan ki baatein sunte aur sunate hain.
Isse mann saaf hota hai
aur dheere-dheere shraddha aur prem badhta hai.

Bhakti se kya hota hai?

Kapila bole:

“Jab koi mere baare mein sunta, sochta aur yaad karta hai,
toh uska mann dheere-dheere duniya ke sukh se door ho jata hai.

Gyaan, vairagya aur bhakti se
insaan mujhe isi jeevan mein paa sakta hai.”

Devahūti ne phir pucha:
“Kaunsi bhakti sabse achchi hai?
Main kaise jaldi moksha paa sakti hoon?”

Sachchi bhakti kya hai?

Kapila ne kaha:

“Jab mann bina kisi swarth ke
sirf Bhagwan mein lag jaye,
usse hi sachchi bhakti kehte hain.

Yeh bhakti itni shaktishaali hoti hai
ki yeh insaan ko moksha se bhi upar le jaati hai.”

Unhone bataya:

Kuch bhakt moksha bhi nahi maangte

Unhe sirf Bhagwan ki seva mein khushi milti hai

Woh ek-dusre ko Bhagwan ki kahaniyaan sunate hain

Unka mann sada shant rehta hai

Aise bhakt Bhagwan ke sabse kareeb hote hain.

Bhagwan ka vaada

Kapila bole:

“Jo sab kuch chhodkar
sirf mujhe apna lete hain,
main unhe khud sansaar ke darr se paar le jata hoon.

Hawa chalti hai,
Suraj chamakta hai,
Agni jalti hai,
sab mere hi bhay se apna kaam karte hain.

Isliye jo bhakti mein mann laga leta hai,
uska mann shant ho jata hai
aur wahi sabse bada sukh paata hai.”

Is kahani ka saar 🌸

Mann hi bandhan hai, mann hi mukti

Duniya ki asakti dukh deti hai

Santon ka sang jeevan badal deta hai

Bhakti sabse aasan aur sabse bada raasta hai

Jo Bhagwan ko sachche mann se yaad karta hai,
uska jeevan shant ho jata hai

Yeh adhyay sikhata hai:
Prem aur bhakti se hi andhera door hota hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 26
    with st.expander("Chapter 26 - Kapila’s description of Creation (Sāṃkhya Cosmology)"):
        text1 = """ 
        Chapter 26 – Srishti ka Rahasya (Kapila explains Creation – Sāṃkhya Cosmology)

Kapila ne apni maa Devahūti ko dheere aur shant swar mein kaha:

“Ab main tumhe batata hoon ki ye duniya kaise bani.
Jo insaan is sach ko samajh leta hai,
woh prakriti ke bandhan se free ho jata hai.”"""
        create_image_text_layout(
            "attached_assets/chapter3/3.26.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ 
        Puruṣa aur Prakriti ka raaz

Kapila bole:

Puruṣa = Atma, jo hamesha se hai, shuddh hai, aur sabko roshni deta hai.

Prakriti = Nature, jisme teen gun hote hain — sattva, rajas, tamas.

Jab atma prakriti se jud jaati hai,
toh woh bhool jaati hai ki woh alag hai.
Tab usse lagta hai:
“Main hi sab kuch kar raha hoon.”

Par asal mein:

Kaam prakriti karti hai

Atma sirf dekhne wali hai

Isi bhool ki wajah se
janam-mrityu ka chakra chalta rehta hai.

24 tattvon ka gyaan

Kapila ne samjhaya:

Is duniya ki rachna 24 tattvon se hui hai.

5 mahabhoot (elements):

Prithvi (earth)

Jal (water)

Agni (fire)

Vayu (air)

Aakash (space)

5 subtle gun (tanmatra):

Sound

Touch

Form

Taste

Smell

10 indriyaan:

5 gyaan indriyaan (ear, skin, eye, tongue, nose)

5 karm indriyaan (speech, hands, feet, organ of creation, organ of excretion)

4 antar ke tattva:

Mann (mind)

Buddhi (intelligence)

Ahamkar (ego)

Chitta (memory/awareness)

Aur ek aur shakti hoti hai — Time (Kaal).
Woh sabko chalata hai.

Creation ka shuruaat kaise hui

Kapila ne kaha:

Shuru mein sab kuch shant tha.
Prakriti ke teen gun balance mein the.

Phir Time ne unhe hila diya.
Tab sabse pehle ek bada tattva bana — Mahat
(ye hi intelligence ka beej hai).

Mahat se paida hua — Ahamkar (ego)
Aur ego teen tarah ka hota hai:

Sattvik → Mann bana

Rajasic → Indriyaan bani

Tamasic → Elements bane

Phir dheere-dheere sab kuch bana:

Sound se → Aakash

Aakash se → Vayu

Vayu se → Agni

Agni se → Jal

Jal se → Prithvi

Aur inhi se pura sansar bana.

Virat Purush ka janm

Kapila ne bataya:

Jab sab tattva alag-alag the,
tab bhi duniya nahi bani.

Tab Bhagwan ne un sab mein pravesh kiya.
Tab ek bada cosmic roop bana — Virat Purush.

Uske sharir se sab kuch nikla:

Mouth → Speech

Nose → Smell

Eyes → Sun aur vision

Ears → Directions

Skin → Plants aur hair

Heart → Mind

Mind → Moon

Buddhi → Brahma

Par phir bhi woh jeevit nahi hua.

Jab tak Atma (Kshetrajna)
uske andar nahi aayi,
tab tak woh nahi utha.

Jaisi body bina soul ke nahi chalti,
waise hi creation bhi bina atma ke nahi chalti.

Sabse important baat

Kapila ne ant mein kaha:

“Insaan ko samajhna chahiye ki
woh sirf body ya mind nahi hai.
Woh atma hai.

Jab bhakti, gyaan aur yoga se
mann shant ho jata hai,
tab insaan apne andar
us atma ko dekh sakta hai.”

Is kahani ka saar 🌿

Atma alag hai, prakriti alag hai

Ego hi sabse bada dhokha hai

Creation dheere-dheere tattvon se bani

Body tab tak bekaar hai jab tak atma na ho

Bhakti aur gyaan se insaan apni asli pehchaan paata hai

Yeh adhyay hume sikhata hai:
“Tum sirf shareer nahi ho. Tum ek roshni ho jo sabke andar hai.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 27
    with st.expander("Chapter 27 - The Sāṃkhya Philosophy—Prakṛti and Puruṣa"):
        text1 = """ 
        Chapter 27 — Hinglish Story (Simple Moral Style)
The Sāṃkhya Philosophy — Prakṛti and Puruṣa

Ek din, Bhagwan ne bahut shant swar mein samjhaya.

Unhone kaha,
"Atma (Puruṣa) sharir mein rehti hai, lekin us par sharir ke sukh-dukh ka asar nahi padta. Bilkul us Suraj ki tarah jo paani mein dikhai deta hai, par paani ki lehron se badalta nahi."

Yeh baat bahut gehri thi."""
        create_image_text_layout(
            "attached_assets/chapter3/3.27.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ 
        Bhagwan ne aage kaha,
"Jab jeev Prakriti ke gunon se chipak jata hai, tab ahankaar paida hota hai. Phir woh sochta hai — ‘Main hi karta hoon.’"

Isi galat soch se problem shuru hoti hai.

Ahankaar ke kaaran,

jeev apni asli azadi bhool jata hai

karmon ke jaal mein phans jata hai

kabhi devta, kabhi manushya, kabhi neeche janm leta hai

Yeh hi sansar ka chakra hai.

Bhagwan ne samjhaya,
"Asal mein Atma kuch karti hi nahi. Isliye us par karm ka bandhan sach mein hota hi nahi."

Par phir bhi problem kyun?

"Kyuki jab tak mann baar-baar indriyon ke vishayon ko sochta rahega, tab tak sansar khatam nahi hoga — bilkul sapne ki tarah. Sapna jhootha hota hai, par jab tak aadmi sota hai, dukh sach lagta hai."

Pandit log chup-chaap sun rahe the.

Bhagwan ne upay bataya:

"Isliye mann ko dheere-dheere control karo. Bhakti yoga aur vairagya se use sambhalo."

Phir unhone bataya ki kaun sa vyakti sachcha yogi hota hai.

Woh vyakti:

niyam aur sanyam follow karta hai

Bhagwan se sachcha prem karta hai

sab jeevon ko samaan dekhta hai

kisi se dvesh nahi karta

santosh mein rehta hai

akela rehkar dhyaan karta hai

‘mera–tera’ ka ahankaar chhod deta hai

Prakriti aur Puruṣa ka sach jaan leta hai

Aisa gyani vyakti apne andar Atma ko dekh leta hai — bilkul aankh se Suraj dekhne jaise.

Aur phir…

Woh Param Brahma ko paa leta hai.

Bhagwan ne ek aur udaharan diya:

"Jaise pehle hum paani mein Suraj ka reflection dekhte hain, phir asli Suraj ko samajhte hain — waise hi ahankaar ke reflection se asli Atma ko pehchana ja sakta hai."

Yeh sun kar sabko thodi clarity mili.

Phir Bhagwan ne neend ka raaz bataya.

"Jab insaan sota hai, tab sharir, indriyan, mann — sab Prakriti mein chup ho jaate hain. Par ek cheez jaagti rehti hai…"

👉 Woh hai Atma.

Lekin ahankaar ke kaaran jeev sochta hai —
"Main kho gaya hoon."

Bilkul us aadmi ki tarah jo dhan kho kar dukhi ho jata hai.

Bhagwan bole,
"Jo vyakti gehra soch-vichar karta hai, woh samajh leta hai ki Atma hi sabka prakashak hai."

Devahuti ka Prashna

Tab Devahuti ne vinamrata se poocha:

"Prabhu, Prakriti aur Puruṣa dono anadi hain aur ek doosre se jude lagte hain — jaise mitti aur uski khushboo, ya paani aur uska swaad."

"Toh phir mukti kaise milegi? Jab tak Prakriti ke gun hain, bandhan kaise khatam hoga?"

Unka prashna bahut gehra tha.

Bhagwan ne dhairya se jawab diya.

Unhone kaha:

"Sirf soch lene se darr thodi der ke liye kam hota hai. Par jab tak uska kaaran — Prakriti ke gun — kamzor nahi hote, tab tak darr wapas aa jata hai."

Phir unhone mukti ka seedha raasta bataya:

bina phal ki ichha ke apna kartavya karo

mann ko shuddh rakho

lambe samay tak Hari ki katha suno

sachcha gyaan pao

duniya se gehra vairagya lao

yoga aur tapasya karo

Atma par gehra dhyaan karo

"Dheere-dheere Prakriti ki pakad jalti hui lakdi ki tarah khatam ho jaati hai — isi janm mein."

Bhagwan ne ek sundar baat kahi:

"Jo jag gaya hai, use sapna dara nahi sakta."

"Waise hi, jo Atma ko jaan leta hai aur mujh mein mann lagata hai, use Prakriti nuksan nahi pahucha sakti."

Phir Bhagwan bole,

"Bahut janmon ke baad jab yogi sab jagah se virakt ho jata hai aur mera bhakt ban jata hai, tab meri kripa se woh apni asli avastha — Kaivalya — ko paa leta hai."

Yeh antim shanti ki avastha hai.

Wahan se wapas sansar mein nahi aana padta.

Ant mein Bhagwan ne kaha,

"Hey mata, jab siddha purush yog ki shaktiyon mein bhi asakt nahi hota, tab woh meri param avastha ko paa leta hai — jahan maut bhi us par haavi nahi ho sakti."

Sab jagah gehri shanti chha gayi.

Moral:
Jab ahankaar chhoot jata hai aur bhakti jagti hai, tab jeev apni asli azadi ko paa leta hai. ✨"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 28
    with st.expander("Chapter 28 - Exposition of the Aṣṭāṅga-Yoga (the eightfold Path of Yoga)"):
        text1 = """ 
        Chapter 28 — Hinglish Story (Simple Moral Style)
Exposition of the Aṣṭāṅga Yoga

Bhagwan ne pyaar se kaha,

"Hey rajkumari, ab main tumhe Yoga ka woh raasta bataunga jisse mann shaant aur pavitra ho jata hai. Isi raaste se jeev Brahman tak pahunchta hai."

Sab dhyaan se sunne lage."""
        create_image_text_layout(
            "attached_assets/chapter3/3.28.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ 
        Bhagwan bole,

"Sabse pehle, insaan ko apna kartavya apni shakti ke hisaab se karna chahiye. Adharm se door rehna chahiye. Jo Bhagwan ki kripa se mile, usmein santosh rakhna chahiye."

"Aur jo log Atma ko jaan chuke hain, unke charanon ki seva karni chahiye."

Phir Bhagwan ne kuch zaroori niyam bataye:

Dharma, artha aur kaam mein zyada na uljho

Moksha dene wale karm karo

Saaf aur saatvik bhojan kam matra mein lo

Shaant aur surakshit jagah par raho

Yeh sab mann ko taiyaar karta hai.

Bhagwan ne Ashtanga Yoga ke gun bataye:

ahimsa (hinsa na karna)

satya (sach bolna)

asteya (chori na karna)

aparigraha (sirf zaroorat bhar lena)

brahmacharya (indriya sanyam)

tapas (sanyam aur mehnat)

shauch (shuddhata)

shastra adhyayan

Bhagwan ki pooja

Yeh sab yogi ki buniyad hain.

Bhagwan bole,

"Chup rehna seekho. Seedha aur sthir baithna seekho. Dheere-dheere saans ko control karo. Phir indriyon ko bahar se hata kar mann mein le aao."

Yeh hi pratyahara hai.

"Phir mann aur saans ko ek bindu par lagao. Mere leelaon ka dhyaan karo. Mann ko baar-baar Bhagwan par tikao."

Agar mann bhatak jaye to?

Bhagwan ne kaha,
"Use pyaar se wapas lao. Baar-baar."

🧘 Baithne ka tareeka

Bhagwan ne step-by-step samjhaya:

saaf pavitra jagah par baitho

shareer seedha rakho

aaraam se baitho

saans ko andar lo, roko, bahar chhodo — dhang se

Isse mann shaant ho jata hai.

Jaise…

👉 hawa aur aag se sona pighal kar saaf ho jata hai,
waise hi pranayama se mann saaf ho jata hai.

Bhagwan bole,

"Pranayama se sharir ki ashuddhi jalti hai. Dharana se paap kam hote hain. Pratyahara se indriya-vasana kam hoti hai. Dhyaan se andar ki buraiyan mit jaati hain."

Jab mann bilkul shaant ho jaye…

Tab kya karein?

🌟 Bhagwan ka Dhyaan

Bhagwan ne kaha,

"Ab meri sundar murti ka dhyaan karo — aankhen naak ke aage tikakar."

Unhone bahut pyar se apna roop bataya:

kamal jaisa komal mukh

neeli kamal jaisi deh

haath mein shankh, chakra aur gada

peele resham ke vastra

seene par Shrivatsa ka chinh

gale mein chamakta Kaustubha mani

vanamala se saja hua roop

mukut, kundal, kangan se alankrit

"Main hamesha apne bhakton par kripa barsata hoon."

Bhagwan ne dhyaan ka secret bataya:

"Pehle mere poore roop ka dhyaan karo. Phir dheere-dheere ang-ang par mann tikao."

👣 Charanon ka Dhyaan

"Sabse pehle mere kamal jaisa charan dekho — jinke nakhon ki chamak andhkaar mita deti hai."

"Unhi charanon ko dhote hue Ganga nikli thi. Shiv ji ne use apne sir par dharan kiya."

Yeh sunkar sabka mann bhavuk ho gaya.

Bhagwan ne aage bataya:

mere ghutne — jinhe Lakshmi seva karti hain

meri janghein — Garuda ke kandhe par tikti hain

meri naabhi — jahan se Brahma ka kamal nikla

mera vaksha — jahan Mahalakshmi rehti hain

meri baahen — jo sabki raksha karti hain

mera Sudarshan chakra

mera shankh

meri gada Kaumodaki

Aur phir…

"Mera muskurata hua mukh dhyaan karo."

Bhagwan bole,

"Jo bhakt prem se mera dhyaan karta hai, uska dil pighal jata hai. Uske rom khade ho jate hain. Aankhon se khushi ke aansu behne lagte hain."

Yeh bhakti ka anand hai.

Phir sabse gehri baat aayi.

"Jab mann poori tarah indriyon se alag ho jata hai, tab woh Brahman mein vilin ho jata hai — bilkul tel khatam hone par diye ki jyoti jaise."

Us samay yogi seedhe apni Atma ko dekh leta hai.

Bhagwan bole,

"Tab yogi sukh-dukh se pare ho jata hai. Woh samajh leta hai ki dard aur sukh ka karta ahankaar hai — Atma nahi."

Ek sundar udaharan diya gaya:

"Jaise sharabi ko apne kapde ka hosh nahi rehta, waise hi siddh yogi ko shareer ki chinta nahi rehti."

Woh apne asli roop mein sthit ho jata hai.

Bhagwan ne ant mein kaha,

"Jab tak purane karm chal rahe hain, tab tak shareer chalta rahega. Par jo yogi samadhi paa leta hai, woh phir shareer ko apna nahi maanta — bilkul sapne ki tarah."

"Jaise beta aur dhan tumse alag hain, waise hi Atma shareer se alag hai."

Sabse antim satya:

"Atma sab mein ek hi hai. Shareer ke hisaab se alag-alag dikhti hai — bilkul alag-alag lakdi mein ek hi aag jaise."

Bhagwan ne shaant swar mein samapt kiya:

"Jo meri is adbhut Prakriti ko jeet leta hai, woh apne asli, shuddh roop mein sthit ho jata hai."

Sab jagah gehri shanti chha gayi.

Moral:
Jab mann niyantrit, bhakti gehri, aur drishti andar ki taraf ho — tab yogi apni asli pehchaan paa leta hai. ✨"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 29
    with st.expander("Chapter 29 - The Path of Bhakti (Bhaktiyoga) and The Power of Time"):
        text1 = """ 
        Chapter 29 — Hinglish Story (Simple Moral Style)
The Path of Bhakti and the Power of Time

🌸 Devahuti ka Prashna

Devahuti ne vinamrata se kaha,

"Prabhu, aapne Prakriti aur Purusha ka sach bahut achhe se samjhaya. Kaha jata hai ki isi se Bhakti Yoga ka janm hota hai. Kripya mujhe Bhakti ka raasta detail mein batayein."

Phir unhone ek aur gehra prashna poocha:

"Hey Kapila, mujhe janmon ke prakar bhi batayein — jisse sun kar insaan duniya se asakti chhod de."

Aur phir boli:

"Mujhe Time (Kaal) ki shakti bhi samjhaiye. Log uske dar se hi achhe karm karte hain."

Unki baat bahut sacchi thi."""
        create_image_text_layout(
            "attached_assets/chapter3/3.29.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ 
        🌿 Maitreya ka Varnan

Maitreya ne kaha,

"Kapila muni ne apni maa ki sundar baat sun kar bahut khushi mehsoos ki. Dayalu hokar unhone jawab diya."

🌼 Bhagwan ka Uttar — Bhakti ke Prakar

Bhagwan ne pyaar se kaha,

"Hey maa, Bhakti ke kai roop hote hain. Kyunki logon ki soch aur swabhav alag-alag hote hain."

⚫ Tāmasik Bhakti

"Jo vyakti dusron ko nuksan pahunchane ki soch se, dikhave se, jalan se, ya gusse mein meri bhakti karta hai — woh tāmasik bhakt hai."

👉 Ismein andhkaar zyada hota hai.

🔴 Rājasik Bhakti

"Jo vyakti sukh, fame, ya power paane ke liye meri pooja karta hai — woh rājasic bhakt hai."

👉 Ismein ichchha zyada hoti hai.

⚪ Sāttvik Bhakti

"Jo vyakti apne karm shuddh karne ke liye ya bina phal ki ichchha ke meri pooja karta hai — woh sāttvik bhakt hai."

👉 Yeh zyada pavitra hota hai.

✨ Nirguṇa Bhakti — Sabse Uchch

Phir Bhagwan ne sabse unchi bhakti batayi.

"Jaise Ganga ka paani bina rukke samundar ki taraf behta hai, waise hi jo mann mere gun sunte hi meri taraf behne lage — wahi nirguṇa bhakti hai."

"Is bhakti mein koi swarth nahi hota."

Bhagwan ne ek adbhut baat kahi:

"Aise bhakt ko agar main moksha ke sab roop bhi doon —"

mere lok mein rehna

mere jaisa vaibhav

mere paas rehna

mera roop paana

mujh mein ek ho jana

"— tab bhi woh kuch nahi chahte. Unhe sirf meri seva chahiye."

Yeh sun kar Devahuti ka hriday pighal gaya.

🌺 Shuddh Bhakti ka Raasta

Bhagwan ne bataya ki mann kaise pavitra hota hai:

nishkaam karm karo

bina kisi ko dukh diye pooja karo

meri murti ka darshan karo

mujhe sparsh, pranam, stuti karo

sab jeevon mein mujhe dekho

dhairya rakho

asakti chhodo

dukhiyon par daya karo

sabse mitrata rakho

satsang karo

ahankaar chhodo

"Jaise hi aisa bhakt mere gun sunta hai, uska mann turant meri taraf khinch jata hai."

⚠️ Ek Bahut Important Warning

Bhagwan ki awaaz thodi gambhir ho gayi.

"Main har jeev ke andar Atma roop mein rehta hoon."

"Jo mujhe sab jeevon mein na dekhkar sirf murti ki pooja karta hai — uski pooja adhuri hai."

Unhone ek tez udaharan diya:

"Yeh bilkul aisa hai jaise koi aag ki jagah raakh mein ahuti de."

Sab chup ho gaye.

Bhagwan bole,

"Jo vyakti dusron se dvesh karta hai aur mujhe alag-alag shariron mein alag samajhta hai — uska mann kabhi shaant nahi hota."

"Main usse prasann nahi hota jo sab jeevon ka apmaan karta hai."

🌍 Sab Mein Bhagwan

Bhagwan ne kaha,

"Jab tak insaan sab jeevon mein mujhe mehsoos na kare, tab tak use murti pooja karni chahiye."

"Par jo mujh mein aur apne mein bhed dekhta hai — uske liye main Mrityu roop mein bhay paida karta hoon."

Is baat ne sabko hila diya.

📈 Jeevon ki Unnati ki Seedhi

Bhagwan ne jeevon ki ek seedhi samjhayi — kaun kis se uchch hai.

Seedhi dheere-dheere upar badhti hai:

jad padarth se jeev

jeev se praan wale

praan walon se mann wale

mann walon se indriya wale

phir taste, smell, hearing, sight…

phir do pair wale

phir chaar varna

phir brahman

phir ved jaane wale

phir ved samajhne wale

phir shanka door karne wale

phir nishkaam karm karne wale

Aur sabse upar kaun?

👉 Woh jo sab kuch mujhe samarpit kar de aur sabko samaan dekhe.

Bhagwan bole:

"Mujhe usse bada koi nahi lagta."

⏳ Time (Kaal) ki Mahashakti

Ab Bhagwan ne Time ka raaz khola.

"Yeh mera hi roop hai."

"Isi se sabka janm aur vinash hota hai."

Unki awaaz gambhir ho gayi.

"Time ke dar se:"

hawa chalti hai

Suraj chamakta hai

Indra varsha karta hai

grah chamakte hain

ped phal dete hain

nadiyan behti hain

samundar seema mein rehta hai

agni jalti hai

devta apna kaam karte hain

Sab kuch Time ke niyam se chal raha hai.

Ant mein Bhagwan bole,

"Time anant hai — par sabka ant karta hai. Uska koi shuru nahi — par sabki shuruat usse hoti hai."

Gehri shanti chha gayi.

Moral:
Jo sab mein Bhagwan ko dekhta hai aur nishkaam prem karta hai — wahi sachchi bhakti aur sachchi mukti paata hai. ✨"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 30
    with st.expander("Chapter 30 - Saṃsāra and Sufferings in Hell"):
        text1 = """ 
        Chapter 30 — Hinglish Story (Simple Moral Style)
Saṃsāra aur Narak ki Peeda

Kapila Bhagwan ne gambhir swar mein kaha,

"Jaise badalon ko tez hawa ki taakat ka pata nahi hota — chahe hawa unhe uda hi kyon na de — waise hi log Time (Kaal) ki shakti ko nahi samajhte, jabki sab uske adheen hain."

Yeh baat sun kar sab chup ho gaye."""
        create_image_text_layout(
            "attached_assets/chapter3/3.30.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ 
        Bhagwan bole,

"Insaan bahut mehnat se sukh ki cheezein jodta hai. Par samay aate hi sab chhin jata hai — aur phir woh rohta hai."

Kyun?

"Kyunki moorkh vyakti is nashwar sharir aur uske sambandhon ko permanent samajh leta hai — ghar, paisa, zameen, parivaar… sab kuch."

🔄 Janm ka Moh

Bhagwan ne kaha,

"Jeev jis bhi janm mein paida hota hai, use wahi achha lagta hai. Use kabhi us se virakti nahi hoti."

Yeh Maya ka jaal hai.

"Itna bhram ho jata hai ki agar jeev narak mein bhi ho — tab bhi apna narak ka sharir chhodna nahi chahta."

Socho… kitna gehra moh hai.

🏠 Grihastha ka Jaal

Bhagwan ne aage bataya,

"Vyakti ka dil chipak jata hai —"

sharir se

patni se

bachchon se

ghar se

dhan se

rishtedaron se

"Phir woh sochta hai — ‘Main bahut bada aur khush hoon.’"

Par andar kya hota hai?

👉 Chinta ki aag jal rahi hoti hai.

Un sabko paalne ke liye…

"Woh paap karta rehta hai."

Bhagwan ne ek dukhad tasveer dikhayi.

"Uska mann indriyon ke jaal mein phans jata hai — chanchal striyon ke akarshan mein, bachchon ki meethi baaton mein."

"Woh galat tareeke se paisa kamata hai aur ghar chalata hai — aur isi ko sukh samajhta hai."

Par sach kya hai?

👉 Yeh dukh ka ghar hai.

💔 Jab Paisa Saath Chhod De

Bhagwan bole,

"Jab baar-baar koshish ke baad bhi uski kamai band ho jati hai, tab lobh use pakad leta hai."

"Woh kamzor ho kar dusron ki cheezon par nazar daalne lagta hai."

Phir…

gareebi

beizzati

chinta

gehra dukh

Sab uske paas aa jate hain.

👴 Budhape ki Karuna

Bhagwan ne bahut karuna se kaha,

"Jaise kisaan buddhe bail ko chhod dete hain, waise hi uski patni aur apne log use izzat dena band kar dete hain."

"Ab woh kamane layak nahi raha."

Phir bhi…

👉 uska moh nahi chhoot ta.

Ab uski halat:

budhapa

bimari

bhook kam

chalna dheere

dusron par nirbhar

"Jo kabhi sabko khilata tha — ab ghar mein kutte ki tarah pada rehta hai, jo pheka hua khana khata hai."

Yeh sunkar dil bhar aata hai.

⚰️ Mrityu ka Samay

Bhagwan ne kaha,

"Jab praan nikalne lagte hain —"

aankhen bahar aa jati hain

gale mein balgam atak jata hai

saans ruk-ruk kar chalti hai

gala se ajeeb awaaz aati hai

Woh apne rote hue rishtedaron se ghira hota hai…

Par kuch bol nahi pata.

Aur phir…

👉 woh mar jata hai.

👹 Yamadut ka Darshan

"Mrityu ke baad," Bhagwan bole,

"woh do bhayanak Yamadut ko dekhta hai — laal aankhon wale."

Dar ke maare…

👉 uska sharir control kho deta hai.

Yamadut use pakad lete hain.

🔗 Bhayanak Yatra

"Us jiva ko ek dukh bhara sharir dekar, gale mein phanda daal kar ghaseeta jata hai — bilkul apradhi ki tarah."

Raaste mein:

narak ke kutte kaatte hain

bhookh aur pyaas satati hai

garam ret jalaati hai

tez dhoop jalaati hai

garam hawa maarti hai

peeth par chabuk padte hain

Kabhi woh behosh hota hai… phir uthaya jata hai.

Yeh raasta bahut lamba hai.

🔥 Narak ki Peeda

Bhagwan ne kathor sach bataya.

Narak mein:

sharir ko aag se jalaya jata hai

kabhi apna hi maans khilaya jata hai

kabhi kutte aur giddh andar ke ang nikaalte hain

kabhi saanp, bichchu kaatte hain

kabhi haath-pair kaat diye jate hain

kabhi haathi se kuchla jata hai

kabhi pahaad se giraaya jata hai

kabhi paani ya andheri gufa mein band kiya jata hai

Yeh sab paapon ka phal hai.

Bhagwan bole,

"Jo purush ya stri vyabhichar karte hain, woh Tāmisra, Andhatāmisra, Raurava jaise narakon mein jaate hain."

Sab ka mann kaamp gaya.

🌍 Ek Gehri Soch

Phir Bhagwan ne kaha,

"Kuch log kehte hain — swarg aur narak isi duniya mein bhi dikhta hai."

Kyunki…

👉 yahan bhi log waise hi dukh jhelte hain.

⚖️ Antim Nyay

Bhagwan bole,

"Jo vyakti paap karke sirf parivaar paalta hai — use sharir chhodkar narak jaana padta hai."

"Jo doosron ko dukh dekar sharir palta hai — use akela andhkaar ke narak mein jaana padta hai."

🌱 Phir Kya Hota Hai?

Ant mein Bhagwan ne thodi aasha di.

"Bahut dukh bhog kar, dheere-dheere jeev shuddh hota hai…"

Aur phir…

👉 use phir se manushya janm milta hai.

Yeh ek nayi shuruat hoti hai.

Sab jagah gehri sannata chha gaya.

Moral:
Moh aur paap ka raasta aakhir dukh hi deta hai — par sudhar ka darwaza hamesha khula rehta hai. ✨"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 31
    with st.expander("Chapter 31 - Sufferings of the Jīva—The Rājasī Gati"):
        text1 = """ 
        Chapter 31 — Hinglish Story (Simple Moral Style)
Sufferings of the Jīva — The Rājasic Path

Bhagwan Kapila ne gambhir swar mein kaha,

"Jeev apne karmon ke bal se chalaya jata hai — aur in karmon par bhi Bhagwan ka niyantran hota hai."

"Apna naya sharir paane ke liye, jeev purush ke veery ke madhyam se stree ke garbh mein pravesh karta hai."

Yeh sansar ka chakkar hai."""
        create_image_text_layout(
            "attached_assets/chapter3/3.31.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ 
        🤰 Garbh ki Pehli Avastha

Bhagwan ne samjhaya:

1 raat mein veery aur rakt milte hain

5 raat mein bulbule jaisa roop

10 din mein ber ke phal jaisa sakht

phir maans ka gola ban jata hai

Dheere-dheere sharir banne lagta hai.

📅 Mahine ke hisaab se vikas

1 mahina → sir banta hai

2 mahine → haath-pair

3 mahine → nakhun, baal, haddiyan, twacha

4 mahine → sharir ke tattva

5 mahine → bhookh-pyaas

6 mahine → jarayu se dhak jata hai

Garbh mein jeev hilna shuru karta hai.

😣 Garbh ki Peeda

Kapila Bhagwan bole,

"Jeev ek bahut gandi jagah mein rehta hai — mootra aur mala se bhari hui."

"Wahan keede use kaat-te rehte hain."

Uska naram sharir:

👉 har taraf se dukh paata hai
👉 baar-baar behosh jaisa ho jata hai

Aur jab maa:

teekha

khatta

garam

kadwa

khana khati hai…

👉 uski jalan bachche tak pahunchti hai.

Garbh mein bachcha:

jhuk kar pada hota hai

pet ki taraf sir

gardan tedhi

"Jaise pinjre mein band pakshi."

Bilkul bebas.

🧠 Saatve Mahine ki Jagruti

Bhagwan bole,

"Saathve mahine se jeev ko thodi chetna aati hai."

Aur tab…

👉 use apne pichhle kai janmon ki yaad aati hai.

Woh dukh se bhar jata hai.

🙏 Garbh mein Jeev ki Prarthana

Garbh mein jeev ro kar prarthana karta hai:

"Prabhu, yeh dukh mujhe milna sahi hai — kyunki main paapi tha."

"Main aapke kamal charanon mein sharan leta hoon."

Jeev aage kehta hai:

"Main asal mein is sharir se alag hoon — par karmon ne mujhe bandh diya hai."

"Hey Prabhu, aap hi mujhe is sansar se nikaal sakte hain."

Uska dil pighal jata hai.

Phir jeev vinati karta hai:

"Hey Prabhu, main yahan khoon, mala aur mootra se bhare is garbh mein jal raha hoon."

"Woh din kab aayega jab main bahar nikalunga?"

Yeh pukaar bahut karun thi.

😨 Bahar Aane ka Dar

Phir jeev ek gehri baat kehta hai:

"Prabhu, main bahar bhi nahi jana chahta…"

Kyun?

"Kyuki bahar aate hi Maya mujhe phir bhula degi."

Woh dar gaya hai.

Phir bhi…

🌪️ Janm ka Pal

Kapila Bhagwan bole,

"Jab jeev prarthana kar raha hota hai — tabhi prasav ki hawa use zor se neeche dhakel deti hai."

Woh:

ghutne lagta hai

tadapta hai

aur…

👉 apni saari yaadein bhool jata hai.

Phir woh janm leta hai — sir ke bal.

👶 Janm ke Baad ki Dasha

Bachcha:

khoon aur gandagi mein girta hai

keede jaisa hilta hai

zor-zor se rota hai

Ab use kuch yaad nahi.

Uski majboori:

jo diya jaye wahi khana

mana bhi nahi kar sakta

gande bistar par sona

machhar, makkhiyan kaat-te hain

khujla bhi nahi sakta

Bilkul bebas.

🔥 Jawani ka Moh

Bhagwan bole,

"Bachpan ke baad, jawani mein —"

ichchha badhti hai

gussa badhta hai

ahankaar badhta hai

Woh doosre logon se ladta hai.

Aur phir…

👉 barbaadi ki taraf badhta hai.

❗ Sabse Badi Galti

Kapila Bhagwan bole,

"Moorkh vyakti is paanch tattvon se bane sharir ko hi ‘main’ samajhta rehta hai."

Isi se bandhan banta hai.

⚠️ Buri Sangat ka Khatra

Bhagwan ne sakht chetavni di:

"Agar dharm par chalne wala bhi buri sangat mein pad jaye — to phir se andhkaar mein gir jata hai."

Buri sangat se:

satya kam hota hai

daya kam hoti hai

shanti kam hoti hai

buddhi kam hoti hai

yash kam hota hai

Sab dheere-dheere girta hai.

🚪 Narak ka Dwaar

Bhagwan ne ek kathin satya kaha (adhyatmik sandarbh mein):

"Jo yogi mukti chahta hai — use kaam-vasna se bachna chahiye."

"Vasana hi bandhan ka bada kaaran hai."

Unhone kaha:

"Meri Maya bahut shaktishaali hai — ek bhav se hi bade-bade jeetne wale log bhi haar jate hain."

Yeh ek gehri spiritual warning thi.

🔄 Jeev ka Chakra

Bhagwan bole,

"Jeev apne sukshma sharir ke saath ek sharir se doosre sharir mein ghoomta rehta hai."

"Jab sthool sharir kaam karna band kare — use mrityu kehte hain."

"Jab naya sharir mil jaye — use janm kehte hain."

Par yaad rakho…

👉 Atma na kabhi janm leti hai, na marti hai.

🕊️ Gyani ka Raasta

Ant mein Kapila Bhagwan ne shanti se kaha,

"Samajhdar vyakti ko na zyada shok karna chahiye, na ghabrana chahiye."

"Use jeev ka sach samajhkar, bina asakti ke jeena chahiye."

"Vivek, yoga aur vairagya se — woh Maya se upar uth sakta hai."

Sab jagah gehri shanti chha gayi.

Moral:
Jo apne aap ko sirf sharir samajhta hai, woh bandhan mein rehta hai — jo apne aap ko Atma samajhta hai, woh azaadi ki taraf badhta hai. ✨"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 32
    with st.expander("Chapter 32 - Excellence of the Bhaktiyoga"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter3/3.32.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 33
    with st.expander("Chapter 33 - Devahūti’s Enlightenment and Liberation"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter3/3.33.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")

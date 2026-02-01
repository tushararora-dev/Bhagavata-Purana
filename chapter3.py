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
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter3/3.6.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7
    with st.expander("Chapter 7 - Vidura’s Queries"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter3/3.7.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 8
    with st.expander("Chapter 8 - Creation of Brahmā—His Vision of Nārāyaṇa"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter3/3.8.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 9
    with st.expander("Chapter 9 - Brahmā’s Prayer and Viṣṇu’s Boon"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter3/3.9.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 10
    with st.expander("Chapter 10 - Brahmā’s Penance and Ten-fold Creation"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter3/3.10.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 11
    with st.expander("Chapter 11 - The concept of Time: Manvantaras and life-spans of Men and Gods"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter3/3.11.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 12
    with st.expander("Chapter 12 - Creation of Rudra, the mind-born Sons and of Manu and Śatarūpā"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter3/3.12.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 13
    with st.expander("Chapter 13 - The Boar (Varāha) Incarnation"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter3/3.13.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 14
    with st.expander("Chapter 14 - Diti’s Conception"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter3/3.14.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 15
    with st.expander("Chapter 15 - Sanaka and Others curse Jaya and Vijaya"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter3/3.15.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 16
    with st.expander("Chapter 16 - The Fall of Jaya and Vijaya"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter3/3.16.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 17
    with st.expander("Chapter 17 - The Birth of Hiraṇyākṣa and Hiraṇyakaśipu"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter3/3.17.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 18
    with st.expander("Chapter 18 - Hiraṇyākṣa’s Fight with Varāha"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter3/3.18.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 19
    with st.expander("Chapter 19 - Varāha kills Hiraṇyākṣa"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter3/3.19.jpg",
            text1,
            layout="side",
            image_position="left"
        )

        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


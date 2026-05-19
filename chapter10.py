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
    create_image_text_layout("attached_assets/chapter10/chapter10.jpg", layout="full")
    # Book 10 - Tenth Skandha
    text0 = """
    <h2>Book 10 - Tenth Skandha</h2>
    """
    
    # Book 10 - Tenth Skandha

    # Chapter 1
    with st.expander("Chapter 1 - Introduction: Kaṃsa kills Devakī’s Sons"):
        text1 = """ 
        🌟 Beginning of Krishna’s Divine Story

King:

👑 Parikshit

ab bahut emotional aur excited ho gaya 😊

Usne sage:

🌌 Shukadeva

se kaha:

👉 “Aapne Solar aur Lunar dynasties ki amazing stories sunayi…”

👉 “Ab please mujhe Krishna ki divine life detail me bataiye!” ❤️"""
        create_image_text_layout(
            "attached_assets/chapter10/10.1.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        🌊 Krishna as the Savior

Parikshit lovingly yaad karta hai 😮

ki:

🌟 Krishna

ne kaise Pandavas ko protect kiya.

Woh kehta hai ⚔️

👉 “Mere grandfathers ne Krishna ko raft bana kar…”

👉 “Kaurava army ke ocean ko cross kiya.”

Aur phir emotional moment 😢

Parikshit yaad karta hai:

⚡ Ashwatthama ka Brahmastra

Jab woh abhi mother Uttara ke womb me tha 👶

tab Krishna ne personally uski protection ki ❤️✨

🌌 Questions About Krishna

Parikshit curiosity se poochta hai 😊

👉 “Krishna Vraja kyun gaye?”

👉 “Mathura aur Dwaraka me kya kya hua?”

👉 “Kamsa ko kyun mara?”

👉 “Kitne years Earth par rahe?”

👉 “Unki wives kitni thi?”

❤️ “Hari’s Stories Remove Hunger”

Parikshit fasting par tha 😮

water bhi nahi pee raha tha.

Lekin woh kehta hai ✨

👉 “Mujhe bhookh-pyaas feel hi nahi hoti…”

👉 “Kyuki main Krishna ki stories ka nectar pee raha hoon.” ❤️

🌍 Earth Burdened by Evil Kings

Shukadeva story start karta hai 🌌

Earth 😢

evil kings aur demonic armies ke burden se crush ho rahi thi.

Toh:

🌍 Mother Earth

cow ka form lekar 🐄

crying condition me:

🌟 Brahma

ke paas gayi.

🌌 Gods Pray to Vishnu

Brahma then gaya:

🌊 Ocean of Milk

ke shore par.

Saath me the:

🌟 Shiva
other gods
crying Earth

Wahan sabne together:

🙏 Lord Vishnu

ki prayer ki.

✨ Divine Message From the Sky

Meditation ke baad 😮

Brahma ne heavenly voice suni 🌌

Voice ne kaha:

👉 “Lord Vishnu khud Earth par descend karenge.”

👉 “Yadu dynasty me birth lenge.”

👉 “Tum sab gods bhi Earth par birth lo.”

🌟 Balarama’s Arrival

Voice ne explain kiya 😮

👉 “Ananta Shesha bhi…”

💪 Balarama

ke form me aayenge.

Aur:

🌸 Yogamaya

bhi divine mission ke liye descend karegi.

🏰 Mathura Under Kamsa

Us time:

🏰 Mathura

par rule karta tha:

😈 Kamsa

Woh Bhoja dynasty ka cruel prince tha ⚔️

💍 Devaki’s Marriage

Ek din huge royal celebration hua ✨

🌸 Devaki

ki marriage hui:

🌟 Vasudeva

ke saath ❤️

Wedding bahut grand thi 😮

elephants 🐘
horses 🐎
gold chariots ✨
maidservants 👸
music 🎶

sab included tha.

😨 The Terrifying Prophecy

Marriage procession ke waqt 😮

suddenly sky se divine voice aayi ⚡

👉 “O Kamsa!”

👉 “Devaki ka eighth son…”

⚔️ “Tumhari death ka cause banega.”
😡 Kamsa Turns Monstrous

Yeh sunte hi 😨

Kamsa instantly mad ho gaya.

Usne sword nikala ⚔️

aur directly:

🌸 Devaki

ke baal pakad liye 😢

Aur wahi usse kill karne laga.

🙏 Vasudeva’s Wisdom

Tab:

🌟 Vasudeva

calmly forward aaye.

Woh Kamsa ko reason aur philosophy samjhane lage ✨

🌌 “Death Is Inevitable”

Vasudeva bole ⚖️

👉 “Har insaan ke saath death born hoti hai.”

👉 “Chahe aaj aaye ya 100 years baad…”

👉 “Death unavoidable hai.”

🐛 The Caterpillar Analogy

Woh beautiful example dete hain 😊

👉 “Jaise caterpillar ek grass leaf se dusri par move karta hai…” 🐛🌿

👉 “Waise soul bhi body change karta hai.”

🌙 Dream Analogy

Aur woh kehte hain 😮

👉 “Mind jis cheez me deeply attached hota hai…”

👉 “Death ke baad soul usi direction me move karta hai.”

⚖️ “Don’t Kill Your Sister”

Finally Vasudeva emotionally bolte hain 😢

👉 “Yeh tumhari younger sister hai.”

👉 “Abhi abhi shaadi hui hai…”

👉 “Isse marna tumhe shameful bana dega.”

😨 Kamsa Still Doesn’t Trust

Kamsa temporarily ruk gaya 😮

Lekin fully convinced nahi hua.

Tab Vasudeva ek painful promise karta hai 😔

👉 “Devaki ke jitne children honge…”

👉 “Main sab tumhe hand over kar dunga.” 💔

😢 The First Son Is Born

Time pass hua ⏳

Aur Devaki ka first son born hua 👶

🌟 Vasudeva’s Truthfulness

Vasudeva promise break nahi kar paaya 😔

Huge pain ke saath 💔

woh baby ko khud Kamsa ke paas le gaya.

😮 Kamsa Temporarily Spares the Child

Kamsa surprisingly bola 😊

👉 “Mujhe danger eighth child se hai.”

👉 “Yeh first child le jao.”

Lekin:

🌌 Narada

later secretly Kamsa ke paas aaye 😮

😨 Narada Increases Kamsa’s Fear

Narada ne bataya ⚡

👉 “Yadavas aur cowherds mostly divine beings hain.”

👉 “Gods already Earth par birth le chuke hain.”

Yeh sunkar 😨

Kamsa paranoid ho gaya.

Usne imagine karna start kiya 😳

👉 “Har child Vishnu ho sakta hai.”

⛓️ Devaki and Vasudeva Imprisoned

Fear me 😨

Kamsa ne:

Devaki 🌸
Vasudeva 🌟

dono ko chains me baandh diya ⛓️

aur prison me daal diya.

😢 Murder of the Children

Ab jo bhi child born hota 😭

Kamsa usse kill kar deta.

Rishi sadly explain karte hain 😔

👉 power-hungry kings apne relatives tak ko destroy kar dete hain.

😈 Kamsa’s Demonic Nature

Shuka reveal karta hai 😮

ki Kamsa actually previous birth ka demon tha:

😨 Kalanemi

Jise Vishnu pehle bhi destroy kar chuke the ⚔️

👑 Kamsa Seizes the Throne

Finally Kamsa ne 😨

apne own father:

👑 Ugrasena

ko bhi imprison kar diya.

Aur poori:

🏰 Mathura kingdom

par violent control le liya.

🌌 Deeper Meaning

Yeh chapter Krishna avatar ka dramatic setup hai ✨

Ek side 😢

fear, tyranny aur cruelty hai.

Dusri side ❤️

divine hope secretly descend kar rahi hai.

Kamsa destiny se bachna chahta tha 😨

Lekin wahi fear usko aur evil bana raha tha.

🌟 Moral
Fear insaan ko monster bana sakta hai
Destiny ko violence se avoid nahi kiya ja sakta
Aur jab darkness extreme ho jaati hai…
tab divine light descend hoti hai ✨"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 2
    with st.expander("Chapter 2 - The Lord’s descent in Devakī’s womb"):
        text1 = """ 
        🌌 Darkness Begins to Spread
😈 Kamsa

ab aur bhi dangerous ho chuka tha.

Uske saath powerful demons bhi join ho gaye 😨

jaise:

👹 Putana
🐂 Arishta
🐴 Keshi
🌪️ Trinavarta
🐂 Dhenuka
👊 Mushtika
👹 Aghasura

aur bahut saare Asuras."""
        create_image_text_layout(
            "attached_assets/chapter10/10.2.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Usne alliance bana liya:

⚔️ Jarasandha
🌌 Bana
🌊 Bhauma

jaise evil kings ke saath.

😢 Yadavas Forced to Flee

Kamsa ka terror itna badh gaya 😨

ki many Yadavas disguise me different kingdoms bhaag gaye.

Koi:

Kurus
Panchalas
Kosalas
Videhas

ki taraf chala gaya.

Mathura fear aur oppression me dubne lagi 😔

😭 Devaki’s First Six Sons Killed

Kamsa ne 😨

Devaki ke first six babies ko brutally kill kar diya. 💔

Prison ka atmosphere hopeless ho chuka tha 😢

Lekin isi darkness ke beech ✨

divine plan secretly start ho raha tha.

🌟 The Arrival of Balarama

Devaki ke seventh child ke roop me 😮

🐍 Ananta Shesha

khud enter hue.

Yehi later bane:

💪 Balarama

Lekin Krishna ne dekha 😮

ki Kamsa ka fear bahut dangerous hai.

Toh unhone command diya:

🌸 Yogamaya

ko.

🌸 Krishna Commands Yogamaya

Krishna ne kaha ✨

👉 “Vraja jao.”

👉 “Wahan Nanda aur Yashoda rehte hain.”

👉 “Rohini bhi wahin hidden hai.”

Phir Krishna ne divine instruction diya 😮

👉 “Devaki ke womb se Shesha ko transfer karo…”

👉 “Aur Rohini ke womb me place karo.”

Isi miraculous transfer ki wajah se 😮

Balarama ka naam pada:

🌌 Sankarshana

(yani “transferred one”).

Aur kyunki woh sabko joy denge ❤️

unhe kaha gaya:

💪 Rama

Aur unki immense strength ke kaaran:

⚔️ Bala-rama
🌸 Yogamaya’s Future Names

Krishna ne Yogamaya ko future reveal kiya ✨

People Earth par usse worship karenge 😮

different names se:

🌸 Durga
⚔️ Bhadrakali
🌌 Narayani
📚 Sharada
🌺 Ambika

aur many more divine forms.

😢 “Devaki Miscarried…”

Yogamaya ne silently miracle perform kiya ✨

aur Balarama ko Rohini ke womb me shift kar diya.

Mathura ke log sadly bolne lage 😔

👉 “Devaki ka miscarriage ho gaya…”

Unhe asli divine secret ka pata nahi tha.

🌟 Krishna Enters Vasudeva’s Heart

Ab most sacred moment aata hai ✨

🌌 Supreme Lord Krishna

pehle:

🌟 Vasudeva

ke heart me enter hue.

Vasudeva suddenly radiant ho gaye ☀️

itne divine lagne lage 😮

ki koi unke paas properly aa bhi nahi paa raha tha.

🌸 Krishna Enters Devaki

Phir spiritual process ke through ✨

Krishna:

🌸 Devaki

ke womb me enter hue.

Rishi beautiful comparison dete hain 😍

👉 “Jaise East direction moon ko hold karti hai…” 🌙

👉 “Waise Devaki ne Lord ko hold kiya.”

✨ Devaki Begins to Shine

Devaki prison me thi ⛓️

Lekin ab woh divine radiance se glow karne lagi 🌟

Rishi compare karte hain 😮

👉 “Jaise ek lamp earthen pot ke andar hidden ho.” 🪔

World us glow ko fully nahi dekh pa raha tha…

kyunki woh prison me band thi. 😢

😨 Kamsa Realizes the Truth

Jab:

😈 Kamsa

ne Devaki ko dekha 😳

woh shock ho gaya.

Usne instantly feel kiya 😨

👉 “Hari uske womb me aa chuka hai.”

👉 “Meri death aa gayi…”

Usko laga 😮

jaise lion kisi cave me enter kar gaya ho 🦁

⚖️ Kamsa’s Inner Conflict

Kamsa seriously sochne laga 😨

👉 “Kya mujhe Devaki ko abhi maar dena chahiye?”

Lekin phir uska conscience thoda awaken hua 😮

Woh sochta hai ⚖️

👉 “Pregnant sister ko kill karna…”

👉 “Meri reputation destroy kar dega.”

👉 “Mera punya bhi khatam ho jayega.”

😔 Kamsa Lives in Fear

Isliye woh Devaki ko immediately nahi marta.

Lekin ab 😨

har second fear me jeene lagta hai.

🌌 Krishna Everywhere

Rishi amazing line bolte hain ✨

👉 Kamsa:

baithte waqt
khate waqt
sote waqt
chalte waqt

har jagah Krishna ko feel karta tha. 😳

Fear ki wajah se 😨

uska mind continuously Krishna me absorbed ho gaya.

🙏 Gods Visit the Prison

Tab heaven se aaye 😮

🌟 Brahma
🔱 Shiva
🎶 Narada
many gods

Sab secretly prison aaye ✨

aur unborn Krishna ki stuti karne lage ❤️

🌳 The Cosmic Tree Philosophy

Gods universe ko compare karte hain:

🌳 Cosmic Tree

se.

Us tree me:

3 roots = sattva, rajas, tamas
2 birds = soul & Supersoul
9 gates = body openings
10 leaves = life airs

Aur woh declare karte hain 🌌

👉 “Krishna hi entire universe ke cause aur support hain.”

🚣 Krishna’s Feet = Boat Across Samsara

Gods kehte hain ❤️

👉 “Jo Krishna ke lotus feet ko pakad leta hai…”

👉 “Woh samsara ocean easily cross kar leta hai.”

Jaise:

🐄 calf ke footprint ko cross karna easy hota hai.

😮 Even Great Yogis Can Fall

Gods warn karte hain ⚖️

👉 “Sirf dry knowledge enough nahi hai.”

👉 “Bhakti ke bina even yogis bhi fall ho sakte hain.”

Lekin Krishna devotees 😍

fearlessly obstacles cross kar lete hain.

🌟 Why God Takes Form

Gods explain karte hain ✨

👉 “Bhagavan body isliye lete hain…”

👉 “Taaki beings unki worship aur realization kar sakein.”

🐟 Past Avatars Remembered

Gods Krishna ko yaad dilate hain ❤️

ki woh pehle bhi aaye the as:

🐟 Matsya
🐢 Kurma
🐗 Varaha
🦁 Narasimha
👑 Vamana
🪓 Parashurama
🏹 Rama

Aur ab 😮

phir se Earth ko save karne aaye hain.

🌸 Gods Comfort Devaki

Finally gods lovingly Devaki se kehte hain ❤️

👉 “Fear mat karo.”

👉 “Kamsa ki death near hai.”

👉 “Tumhara son Yadavas ko protect karega.”

Aur stuti complete karke 🌌

sab gods heaven laut gaye.

🌟 Deeper Meaning

Yeh chapter darkness aur divine hope ka perfect contrast hai ✨

Ek side:

😈 fear
😈 tyranny
😈 murders

Dusri side:

🌸 divine descent
🌌 hidden miracles
❤️ cosmic protection

Most beautiful irony 😮

👉 Kamsa hatred me Krishna ko constantly remember karta tha…

aur devotees love me Krishna ko remember karte hain.

🌟 Moral
Divine plans silently unfold hote hain
Evil power temporary hoti hai
Fear bhi insaan ko God-centered bana sakta hai
Aur Bhagavan darkest prison me bhi light la sakte hain ✨"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 3
    with st.expander("Chapter 3 - Description of the Birth of Śrīkṛṣṇa"):
        text1 = """ 
        🌌 The Night Krishna Was Born

Finally 😮

woh sacred night aa gayi…

🌟 Krishna Janma

ki divine midnight ✨

Us raat pura universe unusual peace se bhar gaya 😍"""
        create_image_text_layout(
            "attached_assets/chapter10/10.3.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        ✨ Auspicious Signs Everywhere

Sky crystal clear ho gaya 🌌

Stars brightly shine karne lage ✨

Aur:

🌟 Rohini Nakshatra

ascendant tha.

Earth bhi strangely joyful lag rahi thi 😊

rivers clear ho gayi 💧
lotus bloom karne lage 🌸
cool fragrant breeze chalne lagi 🌿
birds sweet sounds karne lage 🎶

Even sacred fires automatically bright burn karne lage 🔥

😍 Heaven Celebrates

As Krishna descend karne wale the ✨

heavens me celebration start ho gaya.

Gandharvas singing 🎶
Apsaras dancing 💃
gods flowers shower kar rahe the 🌸
clouds softly rumble kar rahe the ☁️

Sirf ek insaan 😨

fear me jal raha tha:

😈 Kamsa
🌙 The Divine Midnight

Midnight hua 🌌

Aur darkness deepest point par pahunch gayi.

Usi sacred moment 😮

🌟 Lord Vishnu

Devaki ke womb se manifest hue ✨

Rishi compare karte hain 😍

👉 “Jaise full moon East me rise karta hai…” 🌕

waise Krishna appear hue.

😮 Krishna’s Divine Form

Vasudeva ne baby ko dekha…

Lekin woh ordinary baby nahi tha 😨✨

Krishna appear hue with:

4 arms 👐
conch 🐚
discus ⚡
mace ⚔️
lotus 🌸

Unke chest par tha:

✨ Srivatsa mark

Aur neck me shine kar raha tha:

💎 Kaustubha jewel

Unka complexion 😍

rain clouds jaisa deep blue tha ☁️🌌

Aur yellow silk clothes me woh unbelievably beautiful lag rahe the.

😭 Vasudeva Overwhelmed

Vasudeva amazement me freeze ho gaye 😢

Unhe samajh aa gaya:

👉 “Yeh khud Supreme Lord hain.”

Joy me unka heart flood ho gaya ❤️

Aur mentally unhone thousands of cows donate ki 🐄✨

🙏 Vasudeva’s Prayer

Folded hands ke saath 🌟

Vasudeva Krishna ko pray karte hain.

Woh kehte hain 😮

👉 “Aap Supreme Brahman hain…”

👉 “Universe ke witness hain…”

👉 “Actually kabhi kisi womb me enter bhi nahi karte…”

Kyuki Krishna sab jagah already present hain 🌌

⚖️ “The World Is Like an Illusion”

Vasudeva deep philosophy explain karte hain ✨

👉 “Log world ko independently real samajhte hain…”

👉 “Lekin sab ultimately Bhagavan par dependent hai.”

Aur woh fearfully warn karte hain 😨

👉 “Kamsa ne aapke brothers ko already kill kar diya…”

👉 “Agar use pata chal gaya…”

👉 “Woh immediately yahan aa jayega.”

🌸 Devaki’s Prayer

Ab:

🌸 Devaki

Krishna ko lovingly pray karti hain ❤️

Woh kehti hain 😮

👉 “Aap Supreme Reality ho…”

👉 “Time aur creation ke beyond ho…”

Lekin motherly fear bhi strong tha 😢

Woh request karti hain 🙏

👉 “Please apna divine form hide kar lijiye…”

👉 “Kamsa ko pata nahi chalna chahiye.”

🌌 Krishna Reveals Their Past Lives

Tab Krishna softly smile karte hain 😊✨

Aur ek amazing secret reveal karte hain.

🌟 First Birth

Krishna kehte hain 😮

👉 “Ek previous age me…”

👉 “Tum dono Prishni aur Sutapa the.”

Unhone thousands of divine years tak severe tapasya ki 🔥

sirf Krishna jaisa son paane ke liye.

🌟 Second Birth

Phir Krishna explain karte hain 😍

👉 “Second birth me…”

👉 “Tum Aditi aur Kashyapa bane.”

Aur Krishna born hue as:

👑 Vamana
🌟 Third Birth

Ab third time 😮

same promise fulfill karne ke liye:

🌌 Krishna

Devaki aur Vasudeva ke son bane.

❤️ “You Asked for Me, Not Liberation”

Krishna lovingly kehte hain 😊

👉 “Tum liberation maang sakte the…”

👉 “Lekin tumne sirf mujhe son ke roop me chaha.”

Isliye Bhagavan personally aaye ❤️✨

👶 Krishna Becomes a Human Baby

Conversation ke baad 🌌

Krishna apni divine four-armed form withdraw kar lete hain ✨

Aur ek ordinary human baby ban jaate hain 👶

🌸 Yogamaya’s Miracle Begins

Same time 😮

🌸 Yogamaya

Yashoda ke ghar birth leti hain.

Aur prison me miracle start ho jata hai ✨

🔓 The Prison Opens Automatically

Guards suddenly deep sleep me chale gaye 😴

Chains khul gayi ⛓️

Doors automatically open ho gaye 🚪✨

Jaise darkness sunrise par disappear ho jaati hai ☀️

waise obstacles vanish ho gaye.

🌧️ The Midnight Journey

Vasudeva baby Krishna ko head par lekar 🌌

stormy night me prison se bahar nikle.

Heavy rain ho rahi thi ☔

Lekin suddenly 😮

🐍 Shesha Naga

appear hue.

Unhone apne huge hoods spread kiye ☂️

aur Krishna ko rain se protect karne lage.

🌊 Crossing the Yamuna

Ab Vasudeva pahuche:

🌊 Yamuna River

ke paas.

River flooded thi 😨

waves violent thi 🌊

whirlpools dangerous the.

Lekin Krishna ke liye 😍

Yamuna respectfully path create kar deti hai.

Rishi compare karte hain ✨

👉 “Jaise ocean ne Rama ko path diya tha.”

🏡 Arrival at Gokula

Finally Vasudeva pahuche:

🐄 Gokula

Sab cowherds deep sleep me the 😴

Wahan:

🌸 Yashoda

ne ek baby girl ko janam diya tha.

Vasudeva silently 😮

Krishna ko Yashoda ke bed par rakh dete hain 👶✨

Aur baby girl ko lekar wapas nikal padte hain.

⛓️ Return to the Prison

Vasudeva prison wapas aa gaye 😮

Aur instantly:

doors close 🚪
chains lock ⛓️
prison normal ban gaya

Sab kuch aisa lag raha tha 😨

jaise kuch hua hi nahi.

😴 Yashoda Never Knew

Poor exhausted:

🌸 Yashoda

bas vaguely feel kar paayi 😴

ki unhone child birth diya hai.

Lekin Yogamaya ke effect ki wajah se ✨

unhe pata hi nahi chala:

👉 baby boy tha ya girl.

🌌 Deeper Meaning

Yeh chapter divine mystery aur compassion ka peak hai ✨

Krishna:

👉 prison me born hote hain
👉 darkness me light laate hain
👉 fear ke beech hope ban kar aate hain ❤️

Aur sabse beautiful symbolism 😮

👉 locks khul jaate hain
👉 chains toot jaati hain
👉 river raasta de deti hai

jab Bhagavan arrive karte hain. 🌌

🌟 Moral
Divine grace impossible paths open kar sakti hai
True devotion Bhagavan ko personally attract karti hai
Aur darkest midnight ke baad hi divine dawn aata hai ✨"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4
    with st.expander("Chapter 4 - Yoga-Māyā’s Prophecy and Kaṃsa’s Order to Slaughter all Children"):
        text1 = """ 
        🌌 The Cry of the Divine Child

Jaise hi:

🌸 Yogamaya

ko prison me laya gaya 👶✨

sab gates automatically phir se band ho gaye 🚪⛓️

Aur suddenly 😮

baby loudly rone lagi."""
        create_image_text_layout(
            "attached_assets/chapter10/10.4.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        😨 Guards Wake Up

Palace guards instantly jag gaye 😳

Aur quickly bhaagte hue gaye:

😈 Kamsa

ke paas.

Woh panic me bole ⚡

👉 “Devaki ka eighth child born ho gaya!”

😨 Kamsa Rushes in Terror

Yeh sunte hi 😳

Kamsa fear se almost mad ho gaya.

Rishi describe karte hain 😨

👉 uske baal bikhar gaye
👉 steps unstable ho gaye
👉 woh panic me running start kar diya

Kyuki usse lag raha tha 😰

👉 “Meri death aa chuki hai.”

😢 Devaki Begs for Mercy

Kamsa prison room me enter hua 😨

Aur:

🌸 Devaki

baby ko chest se tightly hug karke 😭

usse plead karne lagi.

Woh ro kar boli 💔

👉 “Brother… yeh girl child hai…”

👉 “Isse mat maaro…”

Devaki broken voice me yaad dilati hai 😢

👉 “Tum mere saare sons already kill kar chuke ho…”

👉 “At least is last child ko spare kar do.”

😭 A Sister’s Last Plea

Devaki completely helpless thi 😔

Woh kehti hai:

👉 “Main already ruined ho chuki hoon…”

👉 “Please meri last baby mujhe de do…”

Lekin 😨

fear aur selfishness ne Kamsa ko completely blind kar diya tha.

😈 Kamsa Snatches the Baby

Kamsa ne harshly Devaki ko push kiya ⚡

Aur baby ko forcefully grab kar liya 😨

Rishi kehte hain 😔

👉 uska affection destroy ho chuka tha
👉 self-preservation ne humanity ko overpower kar diya tha

💥 The Attempted Murder

Kamsa ne 😨

baby ko pairon se pakda…

Aur stone slab par smash karne ke liye utha liya 💀

Lekin next moment 😳✨

miracle ho gaya.

🌸 Yogamaya Reveals Herself

Baby suddenly 😮

Kamsa ke hands se slip hokar sky me rise kar gayi 🌌

Aur instantly transform ho gayi:

⚔️ Divine Goddess

me.

Woh appear hui with:

8 arms 👐
bow 🏹
sword ⚔️
discus ⚡
conch 🐚
mace

aur heavenly ornaments ✨

🌌 The Gods Praise Her

Sky me:

Gandharvas 🎶
Siddhas ✨
Apsaras 💃
Kinnaras

sab goddess ki worship karne lage 🌸

⚡ Yogamaya’s Prophecy

Phir goddess ne loudly warn kiya 😨

👉 “O fool Kamsa!”

👉 “Mujhe maar kar kya mila?”

👉 “Tera destroyer already kahin aur born ho chuka hai.” ⚡

Aur phir warning di 😮

👉 “Innocent children ko unnecessarily mat maar.”

Itna bolkar 🌌

goddess vanish ho gayi.

😨 Kamsa Completely Shaken

Yeh sab dekhkar 😳

Kamsa ka confidence toot gaya.

Usne instantly:

🌟 Vasudeva
🌸 Devaki

ko chains se free kar diya ⛓️✨

😭 Kamsa’s Sudden Repentance

Shock aur guilt me 😔

Kamsa emotional ho gaya.

Woh ro kar bola 💔

👉 “Main monster ban gaya…”

👉 “Maine tumhare innocent children kill kar diye…”

Woh khud ko compare karta hai 😨

👉 “Jaise koi rakshasa apne hi relatives ko kha jaaye.”

⚖️ Kamsa Talks Philosophy

Fear aur guilt ke beech 😮

Kamsa suddenly spiritual philosophy bolne lagta hai.

👉 “Bodies temporary hain…”

👉 “Soul eternal hai…”

👉 “People sirf karma ka result face karte hain.”

Woh kehta hai 😔

👉 “Ignorance hi suffering ka cause hai.”

😢 He Begs Forgiveness

Finally 😮

Kamsa tears ke saath 🙏

Devaki aur Vasudeva ke feet pakad leta hai.

Woh sincerely request karta hai:

👉 “Please mujhe forgive kar do…”

🌸 Devaki Forgives Him

Devaki ka anger 😔

bhai ki repentance dekhkar soften ho gaya.

Aur:

🌟 Vasudeva

calmly reply karte hain ⚖️

👉 “Haan, ignorance hi suffering ka root hai.”

Woh explain karte hain 😮

👉 “Jab log body ko self samajhne lagte hain…”

👉 “Tab attachment, fear, greed aur hatred born hote hain.”

😨 But the Peace Doesn’t Last

Kamsa temporarily calm ho gaya 😔

Aur palace return kar gaya.

Lekin next morning 😮

usne apne demon ministers ko sab bata diya.

😈 Demonic Counsel Begins

Ministers ne prophecy sunkar 😨

immediately evil plan bana liya.

Woh bole ⚡

👉 “Aaj hi saare newborn babies ko kill kar dete hain.” 💀

Cities… villages… cowherd camps…

kahin bhi koi baby safe nahi hona chahiye 😨

😈 “Destroy the Root”

Demons ne further advise diya ⚡

👉 “Gods ko directly defeat karna difficult hai…”

👉 “Toh unke roots destroy karo.”

Aur phir horrifying list di 😳

👉 kill:

🐄 cows
📜 Vedas
🙏 Brahmanas
🔥 sacrifices
🧘 sages

Kyuki woh kehte hain 😨

👉 “Ye sab Hari ka body hain.”

⚔️ Hatred Against Dharma

Demons samajh gaye the 😮

ki:

🌌 Vishnu

ka support system hai:

truth
penance
dharma
compassion

Toh unhone decide kiya 😈

👉 “Dharma ko hi destroy karo.”

😔 Kamsa Accepts Evil Advice

Kamsa ab destiny ke trap me phas chuka tha 😨

Usne demons ko command diya ⚔️

ki woh everywhere terror spread karein.

Aur Asuras 😈

different forms lekar

holy people aur innocent beings ko persecute karne lage.

🌌 Deeper Meaning

Yeh chapter ek huge contrast show karta hai 😮

Ek side:

🌸 Yogamaya
✨ divine protection
🙏 forgiveness

Dusri side:

😈 fear
⚔️ tyranny
💀 innocent slaughter

Most tragic irony 😔

👉 Kamsa temporarily truth samajhta hai…

Lekin bad company aur fear usse phir darkness me kheench lete hain.

🌟 Moral
Fear aur selfishness humanity destroy kar sakte hain
Evil advisors downfall ko accelerate kar dete hain
Dharma ko attack karna ultimately self-destruction ban jaata hai
Aur divine truth ko violence se kabhi destroy nahi kiya ja sakta ✨"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 5
    with st.expander("Chapter 5 - Celebration of Kṛṣṇa’s Birth: Meeting of Nanda and Vasudeva"):
        text1 = """ 
        🌸 Krishna Janmotsav Begins in Gokul

Jaise hi 👶✨

🌌 Shri Krishna

ka birth hua…

poora:

🐄 Gokul

khushi se bhar gaya."""
        create_image_text_layout(
            "attached_assets/chapter10/10.5.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        😊 Nanda Baba’s Joy

Noble-hearted:

👑 Nanda Baba

itne happy hue 😭✨

ki unhone immediately sacred bath liya aur pure rituals start kar diye.

Woh beautifully dress hue 👑

Aur astrologer Brahmanas ko bulaya 📜✨

🔥 Sacred Ceremonies

Nanda Baba ne:

🕉️ Vedic blessings
👶 Jatakarma ceremony
🙏 Pitru worship
🌸 Devata puja

sab properly perform karvaya.

🐄 Massive Charity

Khushi me 😮✨

Nanda Baba ne Brahmanas ko donate kiya:

👉 2 lakh decorated cows 🐄🐄🐄

Aur huge mountains jaisa:

sesame seeds
gold cloth
precious gems 💎
🌸 Spiritual Teaching

Rishi ek deep truth bhi batate hain 😮

Different cheezein different ways se purify hoti hain:

body → water se 🚿
wealth → charity se 🎁
mind → contentment se 😊
soul → self-knowledge se 🕉️
🎶 Celebration Everywhere

Poore Vraja me:

drums 🥁
conches 🐚
songs 🎶
blessings ✨

har taraf festive atmosphere tha.

🌈 Gokul Decorated Like Heaven

Har house:

cleaned 🧹
decorated with flags 🚩
flower garlands 🌸
colorful cloths ✨

Gokul heaven jaisa lag raha tha 😍

🐄 Even the Cows Were Decorated

Cows aur calves ko bhi beautifully decorate kiya gaya ✨

turmeric paste 🌼
peacock feathers 🦚
gold chains ✨
flower garlands 🌸

Kyuki Gokul me cows family ki tarah treat hoti thi ❤️🐄

👑 Cowherds Arrive with Gifts

Gopas beautifully dressed hokar 🎁

Nanda Baba ko congratulations dene aaye.

Sab expensive clothes aur ornaments pehne hue the ✨

🌸 Gopis Rush to See Baby Krishna

Jaise hi:

👩 Gopis

ko news mili 😍

woh excitement me ready hone lagi.

kajal 👁️
ornaments 💎
colorful dresses 🌈
saffron paste 🌸

Sab haste-haste Nanda ke house ki taraf bhaagi 😄✨

😍 Divine Beauty of the Gopis

Rishi bahut poetic description dete hain 🌸

Unke:

swinging earrings ✨
moving necklaces 💎
flower-decorated hair 🌺

unhe heavenly bana rahe the.

👶 Blessings for Baby Krishna

Gopis loudly blessings dene lagi 😍

👉 “Yeh child long life paaye!”

👉 “Bhagwan ise protect kare!”

Aur phir playful style me 😄

sab logon par:

turmeric water
oil
curd
milk

sprinkle karne lage.

🥛 Butter Festival

Cowherds ek dusre par 😆

butter
curd
milk
ghee

throw kar rahe the.

Almost Holi jaisa joyful celebration tha 😄✨

🎁 Nanda Baba’s Generosity

Nanda Baba ne 😍

sabko gifts diye:

clothes 👗
ornaments 💎
cows 🐄
wealth ✨

Aur specially musicians, bards aur artists ko reward kiya 🎶

🌸 Rohini Shines Brightly
🌼 Rohini Mata

(Balarama ki mother) bhi celebration me beautifully dressed thi ✨

Aur poore palace me gracefully move kar rahi thi.

🌌 Gokul Becomes Blessed

Rishi kehte hain 😮✨

Us din se:

🐄 Gokul

Lakshmi ka playground ban gaya 🌸

Kyuki:

👶 Hari Himself

wahan reside kar rahe the.

🏛️ Nanda Goes to Mathura

Thodi der baad 😮

Nanda Baba annual tax pay karne:

🏰 Mathura

gaye.

Wahan:

🌟 Vasudeva

ko pata chala ki Nanda aaye hue hain.

🤗 Emotional Reunion

Vasudeva instantly unse milne pahunch gaye 😭

Rishi compare karte hain 😮

👉 “Jaise dead body me life wapas aa jaaye.”

Itna emotional tha unka reunion ❤️

🌸 Vasudeva Hugs Nanda

Vasudeva ne Nanda ko tightly embrace kiya 🤗

Kyuki secretly 😭

unhe pata tha:

👉 Krishna actually unka own son hai.

😢 Vasudeva’s Hidden Emotions

Woh politely poochte hain 😊

👉 “Brother, finally tumhe old age me son mila…”

👉 “Kitni great fortune hai.”

Lekin andar se 😔

woh Krishna ke liye deeply emotional the.

🌊 Philosophy of Life

Vasudeva ek deep truth bolte hain 😮

👉 “Life me loved ones ka milna bahut rare hai.”

Aur compare karte hain 🌊

👉 “Jaise river me floating logs thodi der milte hain… phir alag ho jaate hain.”

🐄 Concern About Gokul

Phir Vasudeva carefully poochte hain 😨

👉 “Gokul safe hai na?”

👉 “Cows healthy hain?”

👉 “Sab peaceful hai?”

Actually 😮

woh indirectly Krishna ki safety ke baare me pooch rahe the.

🌼 Asking About Balarama

Vasudeva specially poochte hain 😊

👉 “Mera son Balarama kaisa hai?”

Kyuki:

🌼 Rohini & Balarama

already Nanda ke ghar me safely reh rahe the.

😔 Nanda Mentions Devaki’s Tragedy

Nanda sadly kehte hain 💔

👉 “Kamsa ne Devaki ke saare sons maar diye…”

👉 “Sirf ek daughter survive hui… aur woh bhi heaven chali gayi.”

🌌 Destiny Philosophy

Nanda calmly kehte hain 😔

👉 “Sab destiny ke control me hai.”

👉 “Wise person destiny ko samajhkar disturbed nahi hota.”

⚠️ Vasudeva’s Secret Warning

Finally 😨

Vasudeva serious tone me kehte hain:

👉 “Ab tumhe immediately Gokul return karna chahiye…”

👉 “Mujhe bad omens dikh rahe hain.” ⚡

Kyuki unhe pata tha 😰

Kamsa demons bhejne wala hai.

🐄 Return to Gokul

Yeh warning sunkar 😮

Nanda aur cowherds quickly carts me baithkar 🚜

wapas:

🌸 Gokul

laut gaye.

🌌 Deeper Meaning

Yeh chapter sirf celebration nahi hai 😮✨

Isme hidden emotions bhi hain:

😊 Gokul ki innocent joy
😢 Vasudeva ka hidden pain
⚠️ coming danger
🌸 divine protection

Most emotional part 😭

👉 Krishna ke real father Vasudeva…

apne hi son ko openly “mera beta” nahi keh pa rahe.

🌟 Moral
True joy sharing aur charity se badhta hai
Divine presence ordinary place ko heaven bana deta hai
Destiny mysterious hoti hai
Aur parental love kabhi disappear nahi hota ❤️"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6
    with st.expander("Chapter 6 - Pūtanā emancipated"):
        text1 = """ 
        👶 Krishna aur Pūtanā ki Kahani

Ek din Nanda Baba Mathura se wapas aa rahe the. Unhe Vasudeva ki baatein yaad aa rahi thi. Unka mann ajeeb fear se bhar gaya tha, isliye woh Bhagwan Hari ko yaad karne lage.

Usi time Kans ne ek dangerous rakshasi Pūtanā ko bheja tha. Woh alag-alag gaon aur shahron mein jaakar chhote babies ko maar rahi thi."""
        create_image_text_layout(
            "attached_assets/chapter10/10.6.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Ek din Pūtanā sky se udkar Gokul pahunch gayi. Apni magic power se usne ek bahut beautiful woman ka roop le liya. Uske face par sweet smile thi aur sab log use dekhkar sochne lage ki shayad Lakshmi Mata khud aayi hain. Isliye kisi ne usse roka nahi.

Pūtanā seedha Nanda Baba ke ghar pahunchi. Wahan chhote Krishna peacefully bed par lete hue the. Krishna sab samajh gaye ki yeh ek evil demoness hai, lekin woh chupchaap aankhen band karke lete rahe.

Yaśodā aur Rohiṇī bhi Pūtanā ki fake beauty dekhkar confuse ho gayin. Pūtanā ne Krishna ko godh mein uthaya aur unhe poisoned milk pilane lagi.

Lekin Krishna ordinary baby nahi the.

Unhone zor se Pūtanā ka breast pakad liya aur sirf milk hi nahi, uski life force bhi kheench li.

Pūtanā pain se zor zor se chillane lagi,

“Bas! Mujhe chhod do!”

Uski scream itni loud thi ki earth aur sky dono hil gaye. Fir woh apne asli giant demon form mein gir padi. Uska huge body itna bada tha ki girte waqt bahut saare trees toot gaye.

Gokul ke log darr gaye. Lekin sabne dekha ki chhote Krishna bilkul fear ke bina Pūtanā ke body par khel rahe the.

Yaśodā aur Gopa women turant Krishna ko uthakar protection rituals karne lagi. Unhone cow dust, cow urine aur Bhagwan ke holy names se Krishna ki safety ke liye prayers ki.

Thodi der baad Nanda Baba aur dusre Gopas wapas aaye. Pūtanā ka giant body dekhkar sab shock ho gaye. Unhe samajh aa gaya ki Vasudeva ki warning sach thi.

Fir villagers ne Pūtanā ke body ko jalaya. Surprisingly, uske body se sweet fragrance aane lagi, kyunki Krishna ke touch se uske saare sins destroy ho gaye the.

Śrī Śuka ne kaha,

“Pūtanā Krishna ko maarne aayi thi, fir bhi Krishna ne usse moksha de diya. Toh jo log sachche love aur devotion se Krishna ko yaad karte hain, unhe kitni badi blessing milegi!”

Nanda Baba ne Krishna ko godh mein uthaya aur unhe tightly hug kar liya. Unka heart happiness aur relief se bhar gaya."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7
    with st.expander("Chapter 7 - Destruction of the Cart and Tṛṇāvarta"):
        text1 = """ 
        🌪️ Krishna aur Tṛṇāvarta ki Kahani

Śrī Śuka ne kaha,

Chhote Krishna dheere dheere bade ho rahe the aur apni cute playful acts se Gokul ke sab logon ko khush karte the.

Ek din Krishna ke turning ceremony ka celebration ho raha tha. Gokul mein music baj raha tha, songs gaaye ja rahe the aur sab log bahut happy the. Yaśodā ne Krishna ko nahlaaya aur lovingly ek cart ke neeche cradle mein sula diya."""
        create_image_text_layout(
            "attached_assets/chapter10/10.7.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Thodi der baad Krishna ko bhookh lagi aur woh rokar apne tiny feet hilane lage. Unke chhote se kick se woh bada cart achanak ulat gaya. Pots toot gaye aur poora cart bikhar gaya.

Sab log shock ho gaye.

Paas khel rahe children bole,

“Krishna ne apne pair se cart giraya hai!”

Lekin bade logon ko yakeen nahi hua. Unhe laga bachche bas funny stories bana rahe hain.

Yaśodā ne Krishna ko uthaya aur protection prayers karwayi. Nanda Baba ne bhi Brahmanas ko bulaakar blessings dilwayi aur charity di.

Kuch din baad Yaśodā Krishna ko godh mein lekar pyaar kar rahi thi. Suddenly Krishna ka weight itna heavy ho gaya jaise mountain ho. Surprise hokar Yaśodā ne unhe neeche bitha diya.

Usi waqt Kans ka servant demon Tṛṇāvarta whirlwind ka form lekar Gokul aaya. Woh huge storm bankar Krishna ko sky mein utha le gaya.

Poora Gokul dust aur darkness se bhar gaya. Kisi ko kuch dikh nahi raha tha. Yaśodā panic mein Krishna ko dhoondhne lagi. Jab woh unhe nahi mili, toh woh dukhi hokar zameen par gir padi aur zor zor se rone lagi.

Tṛṇāvarta Krishna ko lekar bahut upar sky mein gaya. Lekin suddenly Krishna ka weight bahut zyada heavy ho gaya. Demon unhe sambhal hi nahi paaya.

Krishna ne uska gala tightly pakad liya. Tṛṇāvarta saans nahi le paaya aur helpless hokar sky se neeche gir gaya. Girte hi uska body toot gaya aur woh mar gaya.

Sab Gopīs aur Gopas bhaagkar aaye. Unhone dekha Krishna bilkul safe hain aur demon ke body par happily baithe hue hain. Sab log relief aur happiness se bhar gaye.

Sab kehne lage,

“Yeh sach mein miracle hai! Krishna baar baar danger se bach jaate hain.”

Ek din Yaśodā Krishna ko milk pila rahi thi. Krishna cute smile kar rahe the. Fir achanak unhone yawning ki.

Jaise hi Yaśodā ne unke mouth ke andar dekha, woh shock ho gayi.

Unhe Krishna ke mouth mein poora universe dikhai diya — sky, stars, moon, sun, mountains, rivers, oceans aur saari duniya.

Yaśodā fear aur surprise se kaanpne lagi. Woh samajh hi nahi paayi ki yeh sab kya tha."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 8
    with st.expander("Chapter 8 - Kṛṣṇa’s Sports—Display of Viśvarūpa"):
        text1 = """ 
        🌌 Krishna ke Cute Pranks aur Viśvarūpa

Śrī Śuka ne kaha,

Ek din sage Garga secretly Nanda Baba ke ghar aaye. Nanda Baba ne unka bahut respect se welcome kiya aur kaha,

“Please mere dono sons ke naming rituals kar dijiye.”

Garga Muni ne quietly ceremony ki, taki Kans ko koi doubt na ho."""
        create_image_text_layout(
            "attached_assets/chapter10/10.8.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Unhone Rohiṇī ke son ka naam rakha “Rāma” aur “Balarāma,” kyunki woh bahut strong aur sabko happy karne wale the.

Fir unhone Krishna ke baare mein kaha,

“Yeh child har age mein different forms leta hai. Ab yeh dark complexion mein aaya hai, isliye iska naam Krishna hoga. Yeh bahut special hai aur sabko protect karega.”

Yeh sunkar Nanda Baba bahut happy ho gaye.

Thode time baad Krishna aur Balarāma crawling karte hue poore Gokul mein ghoomne lage. Unke tiny anklets ki sweet sound sabko bahut cute lagti thi.

Kabhi dono calves ki tails pakad lete aur unke peeche peeche ghiste chale jaate. Gokul ki ladies yeh dekhkar zor zor se hansne lagti thi.

Lekin Krishna bahut naughty bhi the.

Woh secretly butter aur curd chura lete, monkeys ko khila dete, aur kabhi kabhi pots bhi tod dete. Agar kuch na mile toh dusre babies ko rula kar bhaag jaate.

Gopīs daily Yaśodā ke paas complaints lekar aati thi,

“Tumhara Krishna bahut mischief karta hai!”

Lekin Yaśodā Krishna ka innocent face dekhkar kabhi unhe punish nahi kar paati thi.

Ek din Balarāma aur dusre boys bhaagte hue aaye aur bole,

“Maiya! Krishna ne mitti kha li!”

Yaśodā ne Krishna ka haath pakadkar poocha,

“Tumne earth kyun khaayi?”

Krishna ne cute face banakar kaha,

“Nahi Maiya, maine nahi khaayi. Agar aapko doubt hai toh mera mouth dekh lo.”

Yaśodā ne kaha,

“Achha, mouth kholo.”

Krishna ne jaise hi mouth khola, Yaśodā shock ho gayi.

Unhone Krishna ke mouth ke andar poora universe dekha — sky, stars, sun, moon, rivers, mountains, oceans aur poora Gokul bhi. Unhone khud ko bhi Krishna ke mouth ke andar dekha.

Yaśodā ka heart fear aur surprise se bhar gaya. Woh sochne lagi,

“Kya yeh dream hai? Ya koi divine power?”

Lekin Krishna ki divine magic ne fir Yaśodā ko normal motherly love se bhar diya. Woh sab bhool gayi aur Krishna ko fir se apni godh mein lekar pyaar karne lagi.

Śuka ne bataya ki Nanda aur Yaśodā ne past life mein Bhagwan se yahi blessing maangi thi ki unhe Krishna ke parents banne ka chance mile. Isliye Krishna ne unke ghar janam lekar sabko happiness di."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 9
    with st.expander("Chapter 9 - Grace upon the Gopī (Yaśodā) (Kṛṣṇa tied to the mortar)"):
        text1 = """ 
        🧈 Krishna ki Butter Mischief aur Yaśodā ka Love

Śrī Śuka ne kaha,

Ek din Yaśodā Maiya khud curd churn kar rahi thi. Kaam karte waqt woh Krishna ki cute naughty stories ga rahi thi aur smile kar rahi thi.

Tab chhote Krishna wahan aaye. Unhe milk peena tha, isliye unhone churning rod pakadkar Maiya ka kaam rok diya.

Yaśodā ne pyaar se Krishna ko godh mein bithaya aur milk pilane lagi. Krishna happily unka face dekh rahe the."""
        create_image_text_layout(
            "attached_assets/chapter10/10.9.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
Lekin tabhi stove par rakha milk ubalne laga. Yaśodā jaldi se Krishna ko chhodkar milk bachane chali gayi.

Krishna ko gussa aa gaya.

Unhone lips bite kiye, ek stone uthaya aur curd ka pot tod diya. Fir chupke se andar jaakar butter khane lage aur monkeys ko bhi khilane lage.

Jab Yaśodā wapas aayi, unhone broken pot dekha aur samajh gayi ki yeh Krishna ki mischief hai.

Thodi der baad unhone Krishna ko ek ulte mortar par khade dekha. Krishna monkeys ko butter de rahe the aur idhar-udhar dekh rahe the ki koi pakad na le.

Yaśodā quietly unke peeche gayi.

Jaise hi Krishna ne Maiya ko stick ke saath dekha, woh darr kar bhaagne lage. Yaśodā bhi unke peeche bhaagi.

Finally bahut effort ke baad Yaśodā ne Krishna ko pakad liya.

Krishna ro rahe the, apni eyes rub kar rahe the aur fear se Maiya ko dekh rahe the. Yeh dekhkar Yaśodā ka heart melt ho gaya. Unhone stick phenk di.

Fir Yaśodā ne socha ki Krishna ko punishment ke liye mortar se baandh diya jaaye.

Lekin jab bhi woh rope baandhti, rope har baar bas “do fingers” chhoti reh jaati. Woh aur rope jodti gayi, fir bhi same problem hoti rahi.

Gokul ki ladies yeh funny scene dekhkar hansne lagi. Yaśodā bhi surprise ho gayi.

Finally Krishna ne dekha ki Maiya bahut tired ho gayi hain aur unke forehead par sweat aa gaya hai. Tab Krishna ne pyaar se khud ko tie hone diya.

Śrī Śuka ne kaha,

“Jo Bhagwan poore universe ko control karte hain, woh bhi apne devotees ke love ke saamne surrender ho jaate hain.”

Yaśodā ko jo special love Krishna se mila, woh even great gods ko bhi easily nahi milta.

Usi time Krishna ne paas khade do bade Arjuna trees ko dekha. Woh actually Kubera ke sons the, jo ek curse ki wajah se trees ban gaye the."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 10
    with st.expander("Chapter 10 - Uprooting of Arjuna Trees—Redemption of Nalakūbara and Maṇigrīva"):
        text1 = """ 
        🌳 Krishna aur Do Arjuna Trees ka Miracle

King Parīkṣit ne poocha,

“Nalakūbara aur Maṇigrīva ko tree banne ka curse kyun mila?”

Śrī Śuka ne kaha,

Nalakūbara aur Maṇigrīva Kubera ke sons the. Woh bahut rich aur powerful the. Dheere dheere unhe apne wealth aur luxury ka bahut pride ho gaya."""
        create_image_text_layout(
            "attached_assets/chapter10/10.10.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Ek din woh heavenly river ke paas wine peekar dancing girls ke saath enjoy kar rahe the. Tabhi sage Nārada wahan aaye.

Dancing girls ne respectfully apne clothes pehen liye, lekin dono brothers itne arrogant the ki woh waise hi khade rahe.

Yeh dekhkar Nārada ne calmly kaha,

“Pride aur wealth insaan ko andha bana dete hain. Jo log sirf pleasure mein doobe rehte hain, woh right aur wrong bhool jaate hain.”

Fir Nārada ne unhe curse diya,

“Tum dono trees banoge, taki tumhara arrogance khatam ho. Lekin meri blessing se tumhe apni mistake yaad rahegi. Aur ek din Krishna tumhe free karenge.”

Kuch time baad Gokul mein chhote Krishna abhi bhi mortar se tied the. Krishna slowly crawling karte hue do bade Arjuna trees ke beech chale gaye.

Mortar trees ke beech atak gaya.

Krishna ne zor se pull kiya.

Suddenly dono huge trees ek loud crash ke saath gir pade. Poora Gokul shock ho gaya.

Trees ke andar se do shining divine beings bahar aaye. Woh Nalakūbara aur Maṇigrīva the.

Dono ne Krishna ko fold hands karke pranam kiya aur bole,

“O Krishna, aap Supreme Lord ho. Hamara arrogance destroy karne aur hume save karne ke liye thank you.”

Unhone prayer ki,

“Hamara mind hamesha aapko yaad kare, hamare ears aapki stories sune aur hamare hands hamesha good deeds kare.”

Krishna muskura kar bole,

“Nārada ka curse actually tumhare liye blessing tha. Ab tum dono ke hearts mein true devotion aa gayi hai. Ab tum peacefully apne heavenly home wapas jao.”

Dono brothers ne Krishna ko baar baar pranam kiya aur happiness ke saath heaven ki taraf chale gaye."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 11
    with st.expander("Chapter 11 - Exodus from Gokula—Destruction of demons Vatsa and Baka"):
        text1 = """ 
        🌿 Krishna’s Move to Vṛndāvana and the Defeat of Demons
Śrī Śuka ne kaha,
Jab Arjuna trees girne ki loud sound aayi, tab Nanda Baba aur sab cowherds darr kar wahan bhaage. Unhone dekha ki dono huge trees zameen par gire hue hain aur Krishna mortar ko drag kar rahe hain. 
Chhote boys bole,
“Krishna ne hi trees giraye!”
Lekin bade logon ko yakeen nahi hua. Unhe laga itna chhota child yeh kaise kar sakta hai. """
        create_image_text_layout(
            "attached_assets/chapter10/10.11.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Nanda Baba smile karte hue Krishna ko rope se free kar diya. Fir Krishna apni cute child-like activities se sabko happy karne lage. Kabhi dance karte, kabhi songs gaate aur kabhi Gopīs ke kehne par chhoti chhoti cheezein laakar dete.

Ek din ek fruit seller aayi aur awaaz lagayi,

“Fruits le lo!”

Krishna jaldi se apne tiny hands mein grains lekar uske paas gaye. Unke hands se grains gir rahe the, lekin fruit seller ne pyaar se unhe fruits de diye. Miraculously uski basket precious gems se bhar gayi.

Kuch time baad Gokul mein baar baar strange dangers aane lage. Isliye Upananda ne sabko advice di,

“Hume yeh place chhodkar Vṛndāvana move ho jaana chahiye. Wahan forests, grass aur cows ke liye sab kuch perfect hai.”

Sabne uski baat maan li.

Next day poora Gokul carts, cows aur families ke saath Vṛndāvana ki taraf nikal pada. Trumpets aur horns baj rahe the. Gopīs happily Krishna ki stories ga rahi thi.

Yaśodā aur Rohiṇī bhi Krishna aur Balarāma ko godh mein lekar journey enjoy kar rahi thi.

Vṛndāvana pahunchkar Krishna aur Balarāma bahut happy ho gaye. Wahan woh calves charane lage aur friends ke saath games khelte the — flute bajana, fruits se ball games aur birds ki sounds imitate karna.

Ek din ek demon calf ka form lekar calves ke beech aa gaya. Krishna ne usse pehchaan liya.

Woh slowly uske paas gaye, uski tail aur legs pakadkar usse hawa mein ghumaya aur tree par phenk diya. Demon turant mar gaya.

Sab boys excited hokar bole,

“Bravo Krishna!”

Gods ne bhi sky se flowers barsaaye.

Ek aur din Krishna aur unke friends calves ko paani pilane le gaye. Wahan ek huge scary crane jaisa demon tha — Baka.

Suddenly Baka ne Krishna ko nigal liya.

Sab boys fear se freeze ho gaye.

Lekin Krishna demon ke throat mein fire ki tarah burn karne lage. Baka ne turant Krishna ko bahar nikaal diya aur fir attack karne ki koshish ki.

Krishna ne calmly uski beak pakdi aur easily usse do pieces mein tod diya, jaise ek grass blade todte hain.

Heaven ke gods ne phir flowers aur music se Krishna ki victory celebrate ki. Cowherd boys shock aur happiness se Krishna ko hug karne lage.

Jab sab Vraja wapas aaye aur yeh story sunayi, toh Gopas aur Gopīs Krishna ko pyaar aur relief se dekhne lage. Woh bolne lage,

“Jo bhi Krishna ko harm karna chahta hai, wahi khud destroy ho jaata hai.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 12
    with st.expander("Chapter 12 - Slaying of Aghāsura"):
        text1 = """ 
        🐍 Krishna aur Aghāsura ki Kahani

Śrī Śuka ne kaha,

Ek subah Krishna jaldi uth gaye aur apne horn ki sweet sound se sab cowherd boys ko bulaaya. Sab boys happily calves ke saath forest ki taraf nikal pade.

Woh sab raste bhar games khel rahe the — flute bajana, birds ki awaaz imitate karna, monkeys ke saath masti karna aur streams mein koodna.

Sabke beech Krishna sabse zyada charming lag rahe the. Boys unke saath khelkar bahut happy the."""
        create_image_text_layout(
            "attached_assets/chapter10/10.12.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Lekin us din ek dangerous demon unhe dekh raha tha — Aghāsura. Woh Pūtanā aur Baka ka younger brother tha aur Kans ne use Krishna ko maarne bheja tha.

Aghāsura ne socha,

“Krishna ne mere brother aur sister ko maara hai. Aaj main Krishna aur uske friends sabko khatam kar dunga.”

Fir usne ek giant python ka form le liya. Uska body mountain jaisa huge tha aur uska open mouth ek giant cave ki tarah lag raha tha.

Cowherd boys us huge mouth ko dekhkar bole,

“Wow! Yeh toh kisi giant serpent ka mouth lag raha hai!”

Dusra boy bola,

“Agar yeh sach mein serpent hua aur hume kha gaya, toh Krishna ise bhi Bakāsura ki tarah destroy kar denge!”

Sab boys laughing aur clapping karte hue uske mouth ke andar chale gaye.

Krishna samajh gaye ki yeh ek demon hai. Woh apne friends ko bachana chahte the, lekin tab tak boys aur calves andar ja chuke the.

Krishna ne socha,

“Kaise main apne friends ko bhi bachaun aur is demon ko bhi khatam karun?”

Fir Krishna bhi Aghāsura ke mouth ke andar chale gaye.

Gods fear se chillane lage, jabki Kans aur demons khush ho gaye.

Lekin suddenly Krishna ne apna body huge kar diya. Aghāsura ka breathing path block ho gaya. Demon pain se tadapne laga aur finally uski life force uske head se bahar nikal gayi.

Uske baad Krishna ne apni divine glance se sab boys aur calves ko safely revive kar diya aur sabko lekar serpent ke mouth se bahar aa gaye.

Tab ek bright divine light Aghāsura ke body se nikli aur directly Krishna mein merge ho gayi. Sab gods yeh miracle dekhkar shock ho gaye.

Heaven se flowers ki rain hone lagi. Gandharvas songs gaane lage aur celestial beings Krishna ki praise karne lage.

Even Brahmā ji bhi yeh amazing event dekhne aaye aur wonder mein pad gaye.

Śrī Śuka ne kaha,

“Krishna itne merciful hain ki ek dangerous demon Aghāsura ko bhi unhone liberation de di.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 13
    with st.expander("Chapter 13 - Infatuation of God Brahmā"):
        text1 = """ 
        🌟 Brahmā Becomes Confused by Krishna’s Divine Power
Śrī Śuka ne kaha,
Aghāsura ko defeat karne ke baad Krishna apne cowherd friends ko river ke sandy bank par le aaye aur bole,
“Yeh place kitni beautiful hai! Chalo yahin lunch karte hain. Calves nearby grass kha lenge.” 
Sab boys happily circle mein baith gaye. Koi leaves ko plate bana raha tha, koi fruits use kar raha tha. Sab apna food share karte hue jokes aur laughter mein lunch enjoy karne lage. 
Beech mein Krishna baithe the — flute unke waist ke paas thi, ek hand mein curd-rice ka morsel tha aur woh funny jokes se sabko hasa rahe the. Gods bhi sky se yeh cute scene dekhkar amazed ho rahe the."""
        create_image_text_layout(
            "attached_assets/chapter10/10.13.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Tabhi calves dheere dheere forest ke andar chale gaye.

Cowherd boys darr gaye, lekin Krishna ne smile karke kaha,

“Tum log tension mat lo. Main calves ko le aata hoon.”

Krishna calves ko dhoondhne gaye, lekin wapas aaye toh boys bhi missing the.

Actually Brahmā ji Krishna ki divine powers dekhkar curious ho gaye the. Unhone secretly calves aur cowherd boys ko hide kar diya tha.

Krishna sab samajh gaye.

Fir unhone ek amazing miracle kiya.

Krishna khud hi har calf aur har cowherd boy ka exact form ban gaye — same clothes, same voice, same habits aur same personality.

Is tarah Krishna hi sab calves aur boys ban kar Vraja wapas gaye.

Mothers apne “children” ko hug karne lagi aur cows bhi apne “calves” ko extra love se milk pilane lagi. Sabka affection pehle se bhi zyada badhne laga, kyunki actually woh sab Krishna hi the.

Poora ek saal aise hi beet gaya.

Ek din Balarāma ko surprise hua ki sab log apne children aur calves ko unusual amount mein love kyun kar rahe hain. Fir apni spiritual vision se unhone dekha ki har boy aur calf actually Krishna hi hain.

Meanwhile Brahmā ji ek moment baad wapas aaye — lekin earth par ek poora year beet chuka tha.

Woh shock ho gaye.

Jin boys aur calves ko unhone hide kiya tha, woh ab bhi hidden the. Lekin Krishna fir bhi unhi boys aur calves ke saath happily khel rahe the.

Brahmā confuse ho gaye ki yeh sab kaise possible hai.

Tab suddenly sab cowherd boys aur calves divine four-armed Viṣṇu forms mein transform ho gaye. Har form ke hands mein conch, discus, mace aur lotus tha.

Poora universe un divine forms ki worship kar raha tha. Brahmā ki senses bhi overwhelm ho gayi. Woh samajh gaye ki Krishna ordinary child nahi, Supreme Lord hain.

Krishna ne fir apni divine illusion hata di.

Brahmā turant apne swan se neeche utar gaye aur Krishna ke feet par gir pade. Tears of joy ke saath unhone Krishna ko pranam kiya aur folded hands se unki praise karne lage."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 14
    with st.expander("Chapter 14 - God Brahmā eulogizes Kṛṣṇa"):
        text1 = """ 
        🙏 Brahmā Praises Little Krishna

Śrī Śuka ne kaha,

Brahmā ji Krishna ki divine power dekhkar completely amazed ho gaye. Folded hands ke saath woh Krishna ki praise karne lage.

Unhone Krishna ko dekha — dark raincloud jaisa beautiful complexion, yellow clothes, peacock feather, forest flowers aur hand mein little food morsel. Krishna ek simple cowherd child ki tarah lag rahe the, lekin actually Supreme Lord the.

Brahmā ji ne humbly kaha,"""
        create_image_text_layout(
            "attached_assets/chapter10/10.14.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        “Main creator hoke bhi aapko fully samajh nahi sakta. Aapki divine power mind aur words se bahar hai.”

Fir unhone kaha,

“Jo log sirf knowledge ke peeche bhaagte hain aur devotion ko ignore karte hain, unki mehnat empty husk peetne jaisi hai. Real path devotion ka hai.”

Brahmā ne accept kiya ki unhone arrogance mein Krishna ko test karne ki mistake ki.

Unhone shame se kaha,

“Main bahut foolish tha. Main aapko apni māyā se confuse karna chahta tha, jabki aap toh sab māyā ke master ho.”

Fir Brahmā ji ne Krishna se forgiveness maangi.

Unhone kaha,

“Jaise ek baby maa ke womb mein kick karta hai aur maa usse offence nahi maanti, waise hi please meri mistakes ko forgive kar dijiye.”

Brahmā Krishna ki Vraja family ko dekhkar bhi emotional ho gaye.

Unhone kaha,

“Gokul ki cows aur mothers kitni blessed hain! Krishna unka milk itne love se peete hain. Even great sacrifices bhi Krishna ko itna satisfy nahi kar paate.”

Fir woh bole,

“Nanda Baba aur Vraja ke cowherds kitne lucky hain ki Supreme Brahman unka friend bankar unke saath khelte hain.”

Brahmā ji ne ek aur beautiful wish maangi,

“Mujhe next life mein kuch bhi bana do — even grass in Vṛndāvana — taki mujhe devotees ke feet ki dust mil sake.”

Unhone kaha,

“Pūtanā ne fake motherly love dikhaya tha, fir bhi Krishna ne usse liberation de di. Toh jo log sach mein Krishna se love karte hain, unki blessing kitni great hogi!”

Finally Brahmā ji ne Krishna ko baar baar pranam kiya aur permission lekar apne loka wapas chale gaye.

Uske baad Krishna fir se apne cowherd friends ke paas aaye.

Boys ko laga Krishna bas ek moment ke liye gaye the. Sab happily saath mein lunch complete karne lage.

Shaam ko Krishna flute aur horns ki sweet sounds ke saath Vraja wapas aaye. Cowherd boys excitement se sabko batane lage,

“Aaj Krishna ne ek giant serpent ko maara aur hume bachaya!”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 15
    with st.expander("Chapter 15 - Slaying the demon Dhenuka"):
        text1 = """ 
        🐴 Krishna aur Balarāma Defeat Dhenukāsura

Śrī Śuka ne kaha,

Jab Krishna aur Balarāma thode bade hue, tab unhe cows charane ki permission mil gayi. Dono brothers apne cowherd friends ke saath Vṛndāvana ke forests mein happily ghoomte the.

Krishna flute bajate, birds ki sounds imitate karte aur kabhi peacocks ki tarah dance karte. Kabhi woh cows ko loudly naam lekar bulate aur sab friends hansne lagte.

Kabhi Krishna tired Balarāma ke feet press karte aur kabhi friends ke saath wrestling aur games khelte. Sab boys Krishna ke saath bahut happy rehte the.

Ek din Śrīdāma aur dusre boys ne Krishna aur Balarāma se kaha,"""
        create_image_text_layout(
            "attached_assets/chapter10/10.15.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        “Nearby ek huge palm forest hai. Wahan bahut sweet fruits hain, lekin ek dangerous demon Dhenuka unhe kisi ko khane nahi deta.”

Boys ne fear se kaha,

“Woh demon donkey ka form lekar rehta hai aur humans ko bhi maar deta hai. Isliye koi wahan nahi jaata.”

Krishna aur Balarāma smile karne lage aur bole,

“Chalo, chalte hain.”

Dono brothers friends ke saath palm forest pahunch gaye.

Wahan Balarāma ne ek huge palm tree ko zor se shake kiya. Sweet fruits dhad-dhad karke neeche girne lage.

Yeh sound sunkar Dhenukāsura gusse mein daudta hua aaya. Woh ek giant donkey jaisa scary demon tha. Earth tak shake hone lagi.

Usne Balarāma ko apni hind legs se kick kiya aur loudly bray karne laga.

Lekin Balarāma bilkul fear nahi hue.

Jaise hi demon fir attack karne aaya, Balarāma ne uski dono hind legs pakad li aur use hawa mein fast ghumaya. Fir unhone usse ek tall palm tree par phenk diya. Demon turant mar gaya.

Uska body trees par itni force se gira ki ek ke baad ek bahut saare palm trees girne lage, jaise storm aa gaya ho.

Dhenuka ke dusre donkey-demons bhi gusse mein attack karne aaye.

Tab Krishna aur Balarāma ne sabko pakad-pakadkar trees par phenk diya aur easily defeat kar diya.

Gods heaven se flowers barsane lage aur Krishna-Balarāma ki praise karne lage.

Ab forest safe ho gaya tha.

Villagers aur animals fear ke bina wahan jaane lage aur sweet palm fruits enjoy karne lage.

Shaam ko Krishna aur Balarāma flute bajate hue Vraja wapas aaye. Gopīs unhe dekhkar bahut happy ho gayin.

Yaśodā aur Rohiṇī ne dono brothers ko lovingly nahlaaya, achhe clothes pehnaaye aur tasty food khilaaya. Fir Krishna aur Balarāma peacefully so gaye.

Kuch din baad Krishna apne friends aur cows ke saath Yamunā river gaye. Bahut garmi thi aur sabko pyaas lagi thi.

Lekin river ka water poison se polluted tha.

Jaise hi cows aur boys ne paani piya, sab zameen par gir pade.

Krishna ne apni divine glance se sab par nazar daali.

Unki nectar jaisi glance se sab instantly wapas alive ho gaye.

Sab boys shock aur relief se ek dusre ko dekhne lage. Unhe samajh aa gaya ki Krishna ne hi unki lives save ki hain."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 16
    with st.expander("Chapter 16 - Expulsion of Kāliya"):
        text1 = """ 
        🐍 Krishna aur Kāliya Nāga ki Kahani

Śrī Śuka ne kaha,

Yamunā river ka ek part bahut dangerous ho gaya tha. Wahan Kāliya naam ka poisonous serpent rehta tha. Uske poison se water ubal raha tha aur uske upar se udne wale birds bhi mar jaate the.

River ke paas ke plants aur animals bhi poisonous hawa ki wajah se suffer kar rahe the. Yeh dekhkar Krishna ne decide kiya ki ab Kāliya ko rokna hoga."""
        create_image_text_layout(
            "attached_assets/chapter10/10.16.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Krishna ek tall Kadamba tree par chadhe, apni waist cloth tight ki aur heroically poisonous water mein jump kar gaye. Splash itna powerful tha ki huge waves har side fail gayin.

Kāliya ko laga koi uske home par attack kar raha hai.

Woh gusse mein hiss karta hua Krishna ke paas aaya aur unhe apni giant coils mein tightly baandh liya.

Krishna ke friends aur cows yeh dekhkar fear se ro pade. Sabko laga Krishna danger mein hain.

Gokul mein bhi strange bad omens dikhne lage. Nanda Baba, Yaśodā aur sab villagers panic mein Yamunā ki taraf daud pade.

Sabne Krishna ko serpent ke coils mein dekha toh woh almost unconscious ho gaye. Gopīs tears bahaane lagi aur Yaśodā Krishna ke paas bhaagna chahti thi, lekin Balarāma ne sabko calmly rok diya. Unhe pata tha Krishna safe hain.

Thodi der baad Krishna ne apna body suddenly expand kar diya.

Pressure itna zyada tha ki Kāliya ko Krishna ko chhodna pada. Fir serpent ne apne huge hoods uthaaye aur fire jaisa poison nikaalne laga.

Krishna fearlessly uske around move karne lage, jaise Garuḍa apne prey ke saath play karta hai. Fir Krishna ne ek jump mein Kāliya ke giant hood par chadhkar divine dance shuru kar diya.

Har step ke saath Kāliya weak hota gaya. Krishna uske har raised hood par dance karke uska pride tod rahe the.

Heaven ke Gandharvas, Siddhas aur Apsarās sky mein aakar drums aur music ke saath Krishna ki victory celebrate karne lage. Flowers ki rain hone lagi.

Kāliya ka body tootne laga aur woh blood vomit karne laga. Finally uska arrogance completely destroy ho gaya aur usne Krishna ko Supreme Lord maan liya.

Tab Kāliya ki wives apne children ko lekar Krishna ke paas aayi. Woh folded hands ke saath pray karne lagi,

“O Lord, aapka punishment bhi blessing jaisa hai. Please hamare husband ko forgive kar dijiye.”

Unhone kaha,

“Kāliya evil nature mein born hua hai, lekin aapki touch se uska life blessed ho gaya.”

Fir Kāliya ne bhi humbly Krishna se kaha,

“Hum serpents naturally angry aur cruel hote hain. Please jo aapko theek lage wahi punishment ya mercy dijiye.”

Krishna ne calmly kaha,

“Tum ab yahan nahi reh sakte. Yamunā ka water cows aur people ke liye safe hona chahiye. Apni family ke saath samundar chale jao.”

Kāliya fearfully bola,

“Lekin Garuḍa mujhe maar dega.”

Krishna muskuraaye aur bole,

“Ab Garuḍa tumhe harm nahi karega, kyunki tumhare hoods par mere footprints rahenge.”

Yeh sunkar Kāliya aur uski wives bahut grateful ho gaye. Unhone Krishna ko divine clothes, jewels aur lotus garlands offer kiye. Fir respectfully unke around parikrama karke pranam kiya.

Uske baad Kāliya apni family ke saath Ramaṇaka island chala gaya.

Krishna ki grace se Yamunā ka water phir se pure aur sweet ho gaya. Sab Vraja-vāsīs relief aur happiness se bhar gaye."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 17
    with st.expander("Chapter 17 - Rescue from the Forest Conflagration"):
        text1 = """ 
        🔥 Krishna Saves Vraja from the Forest Fire

King Parīkṣit ne poocha,

“Kāliya originally Nāgas ke island Ramaṇaka mein rehta tha. Fir woh Yamunā mein kyun aaya? Uska Garuḍa se kya problem tha?”

Śrī Śuka ne kaha,"""
        create_image_text_layout(
            "attached_assets/chapter10/10.17.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Pehle sab Nāgas Garuḍa ko respect ke saath monthly offerings dete the, taki woh unhe attack na kare. Lekin Kāliya apne poison aur power par bahut proud ho gaya tha.

Ek din usne Garuḍa ke liye rakhe offerings khud hi kha liye. Yeh dekhkar Garuḍa bahut gusse mein aa gaya aur Kāliya par attack kar diya.

Kāliya ne fight karne ki koshish ki, lekin Garuḍa ki power ke saamne woh tik nahi paaya. Fear mein woh Yamunā ke ek special pool mein chhup gaya.

Us pool mein Garuḍa enter nahi kar sakta tha, kyunki sage Śaubhari ne curse diya tha ki agar Garuḍa wahan fish khayega, toh uski death ho jayegi. Sirf Kāliya ko yeh secret pata tha.

Krishna ne jab Kāliya ko defeat karke Yamunā se bahar nikala, tab unka body divine ornaments, jewels aur sandal paste se shine kar raha tha.

Sab cowherds aur Gopīs unhe dekhkar relief aur happiness se bhar gaye. Woh Krishna ko tightly hug karne lage, jaise unhe life wapas mil gayi ho.

Yaśodā Maiya ne Krishna ko godh mein bithakar baar baar hug kiya aur tears of joy bahaane lagi. Nanda Baba ne Brahmanas ko cows aur gold donate kiya.

Balarāma quietly smile kar rahe the, kyunki woh Krishna ki divine power already jaante the.

Us din sab log Yamunā ke paas hi rest karne lage. Sab thake hue the aur dheere dheere raat mein so gaye.

Lekin midnight mein ek terrible forest fire suddenly jungle mein fail gaya. Dry trees aur grass ki wajah se fire bahut fast spread hone laga aur poore Vraja ko surround kar liya.

Heat aur smoke se sab log panic mein uth gaye.

Sab fear mein Krishna aur Balarāma ko pukarne lage,

“O Krishna! O Rāma! Please hume save kijiye! Yeh deadly fire hume destroy kar dega!”

Villagers crying voice mein bole,

“Hum aapke devotees hain. Hum aapke feet kabhi nahi chhod sakte. Please hume protect karo.”

Krishna ne dekha ki sab completely helpless aur terrified hain.

Tab Supreme Lord Krishna ne calmly us huge terrifying fire ko ek hi moment mein swallow kar liya.

Poora forest instantly safe ho gaya.

Sab Vraja-vāsīs Krishna ko wonder aur gratitude ke saath dekhne lage."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 18
    with st.expander("Chapter 18 - Slaying of the Demon Pralamba"):
        text1 = """ 
        🌳 Balarāma Defeats the Demon Pralamba

Śrī Śuka ne kaha,

Kāliya aur forest fire ke incidents ke baad Krishna aur Balarāma happily cows ke saath Vraja wapas aaye. Sab villagers unki glory gaate hue bahut joyful the.

Summer season aa gaya tha, lekin Vṛndāvana itna beautiful tha ki woh spring jaisa lagta tha. Waterfalls ki sound, cool breeze, flowers ki fragrance aur green forests har taraf happiness faila rahe the."""
        create_image_text_layout(
            "attached_assets/chapter10/10.18.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Krishna aur Balarāma apne cowherd friends ke saath forest mein games khelte, flute bajate aur dance karte the. Kabhi wrestling, kabhi jumping aur kabhi hide-and-seek khelte.

Kabhi woh birds aur animals ki funny sounds imitate karte aur sab boys zor zor se hansne lagte.

Ek din ek dangerous demon Pralamba secretly cowherd boy ka disguise lekar unke group mein aa gaya. Uska plan Krishna aur Balarāma ko kidnap karna tha.

Krishna sab jaante the, lekin unhone pretend kiya jaise kuch pata hi nahi. Woh demon ko game mein include kar liya.

Krishna ne sab boys se kaha,

“Chalo teams banaakar game khelte hain!”

Ek side Krishna captain bane aur doosri side Balarāma. Rule yeh tha ki jo lose karega, woh winners ko apni back par carry karega.

Game start hua aur Balarāma ki team jeet gayi.

Rules ke according Krishna ne Śrīdāmā ko carry kiya aur Pralamba ko Balarāma ko apni back par bithana pada.

Pralamba slowly Balarāma ko group se bahut door le gaya. Fir suddenly usne apna giant demon form dikha diya.

Uska body dark cloud jaisa huge tha, eyes fire ki tarah burn kar rahi thi aur golden ornaments shine kar rahe the. Woh sky mein fast speed se bhaagne laga.

Ek moment ke liye Balarāma surprise hue.

Lekin next second unhe apni divine strength yaad aa gayi. Woh bilkul fearless ho gaye.

Balarāma ne apna fist tightly bandhkar Pralamba ke head par ek terrifying punch maara — bilkul Indra ke thunderbolt ki tarah.

Impact itna powerful tha ki demon ka head toot gaya. Woh blood vomit karta hua loudly roar karte hue zameen par gir gaya aur turant mar gaya.

Cowherd boys yeh dekhkar shock aur excitement se chillane lage,

“Bravo Balarāma! Wah!”

Sab friends happiness aur love se Balarāma ko hug karne lage, jaise woh death se wapas aaye hon.

Heaven ke gods ne bhi flowers barsaaye aur Balarāma ki victory celebrate ki."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 19
    with st.expander("Chapter 19 - Swallowing up of a Forest-conflagration"):
        text1 = """ 
        🔥 Krishna Swallows Another Forest Fire

Śrī Śuka ne kaha,

Ek din Krishna, Balarāma aur cowherd boys games mein itne busy ho gaye ki cows bahut door jungle ke andar chali gayin. Fresh green grass dekhkar woh aur bhi deep forest mein pahunch gayin.

Thodi der baad cows thirsty aur tired hokar loudly lowing karne lagi. Woh reeds aur thick grass ke dangerous area mein phans gayin."""
        create_image_text_layout(
            "attached_assets/chapter10/10.19.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Jab boys ko cows nahi mili, toh sab worried ho gaye.

Krishna aur Balarāma ke saath sabne unke footprints aur grass ke marks follow kiye.

Finally unhe cows mil gayin.

Krishna ek tall tree par chadh gaye aur dark raincloud jaisi sweet voice mein har cow ko uske naam se bulaane lage.

Krishna ki voice sunkar cows happiness se loudly respond karne lagi aur unke paas aa gayin.

Lekin usi waqt suddenly forest mein ek huge fire lag gaya.

Strong wind ki wajah se fire har side fast spread hone laga. Flames itni dangerous thi ki lag raha tha poora forest destroy ho jayega.

Cowherd boys aur cows fear se kaanpne lage. Sab Krishna aur Balarāma ke paas bhaagkar aaye aur bole,

“O Krishna! O powerful Balarāma! Please hume save kijiye! Yeh fire hume jala dega!”

Unhone folded hands se kaha,

“Hum aapke apne log hain. Humne aapko hi apna protector maana hai.”

Krishna ne calmly sabko assure kiya,

“Fear mat karo. Sab apni eyes band kar lo.”

Sabne turant Krishna ki baat maani aur eyes close kar li.

Usi moment Krishna ne apni divine yogic power se poori terrifying forest fire ko swallow kar liya.

Jab sabne eyes open ki, toh woh shock ho gaye.

Na fire thi, na danger.

Sab cows aur boys bilkul safe the aur Bhāṇḍīra tree ke paas khade the.

Ab cowherd boys ko aur strongly feel hone laga ki Krishna koi ordinary child nahi hain. Unke andar divine power hai.

Shaam ko Krishna aur Balarāma flute bajate hue cows ke saath Vraja wapas aaye. Cowherd boys unki praise gaate hue chal rahe the.

Gopīs Krishna ko dekhkar supreme happiness se bhar gayin, kyunki unke liye Krishna se ek moment ki separation bhi bahut long lagti thi."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 20
    with st.expander("Chapter 20 - Description of the Rainy Season and the Autumn"):
        text1 = """ 
        🌧️ Rainy Season and Autumn in Vṛndāvana

Śrī Śuka ne kaha,

Cowherd boys ghar jaakar sabko batane lage ki Krishna ne kaise forest fire se sabko bachaya aur Balarāma ne Pralamba demon ko kaise defeat kiya.

Yeh stories sunkar Gopas aur Gopīs bahut amazed ho gaye. Dheere dheere sabko feel hone laga ki Krishna aur Balarāma ordinary children nahi, divine beings hain."""
        create_image_text_layout(
            "attached_assets/chapter10/10.20.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Uske baad rainy season aa gaya.

Sky dark blue clouds se bhar gaya. Thunder ki loud sounds aur lightning se atmosphere magical lagne laga.

Parched earth par jab rain girne lagi, tab poori nature fresh aur green ho gayi. Dry lands phir se alive lagne lagi, jaise koi weak person suddenly strength pa le.

Raat ko fireflies shine karte the aur frogs rain ki sound sunkar loudly croak karne lagte the. Rivers aur streams overflow hokar har taraf behne lagi.

Fields green grass se bhar gaye, mushrooms ug aaye aur red insects earth ko colorful bana rahe the. Farmers khush the kyunki crops bahut achhi ho rahi thi.

Peacocks clouds dekhkar happily dance karne lage. Trees bhi fresh water peeke naye leaves, flowers aur fruits se bhar gaye.

Kabhi kabhi Krishna cows aur friends ke saath forest mein ghoomte. Cows Krishna ki voice sunkar jaldi jaldi unke paas daud aati aur joy mein milk tak leak hone lagta.

Krishna forest ki beauty enjoy karte — honey dripping trees, waterfalls ki sound aur caves ki echoes sabko magical bana deti thi.

Jab heavy rain hoti, Krishna aur Balarāma kisi tree ke neeche ya cave mein shelter lete aur fruits, roots aur simple food enjoy karte.

Kabhi woh stone slab par baithkar curd-rice apne friends ke saath share karte. Nearby cows aur calves green grass par peacefully rest karte rehte.

Is tarah rainy season happiness aur beauty se bhar gaya.

Fir dheere dheere autumn season aa gaya.

Sky bilkul clear aur bright ho gaya. Lakes aur rivers ka water crystal jaisa transparent lagne laga aur lotuses khilne lage.

White clouds clean aur peaceful dikh rahe the, jaise sages sab desires chhodkar calm ho gaye hon. Cool breezes forests ki fragrance lekar chal rahi thi.

Autumn nights mein stars brightly shine karte the aur full moon sky mein bahut beautiful lagta tha.

Villages aur cities mein harvest festivals celebrate hone lage. Fields ripe crops se golden shine kar rahi thi.

Sab creatures nature ki beauty enjoy kar rahe the.

Lekin Gopīs ke hearts mein ek alag feeling thi.

Cool autumn breeze sabko comfort de rahi thi, lekin Krishna se separation ki feeling unke hearts mein aur strong ho rahi thi."""
        create_image_text_layout(text_content=text2, layout="full")
        
        # Chapter 21
    with st.expander("Chapter 21 - The Song of Gopīs (cowherd-women)"):
        text1 = """ 
        🎶 The Gopīs Sing About Krishna’s Flute

Śrī Śuka ne kaha,

Autumn season mein Vṛndāvana bahut beautiful lag raha tha. Clear lakes, lotus flowers aur cool fragrant breeze har taraf sweetness faila rahe the.

Krishna cows, Balarāma aur cowherd boys ke saath deep forest mein ghoomte hue flute bajane lage. Forest birds, bees, rivers aur mountains unki flute ki sound se magical lagne lage."""
        create_image_text_layout(
            "attached_assets/chapter10/10.21.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Jab Vraja ki Gopīs ne distance se Krishna ki flute suni, unke hearts love aur longing se bhar gaye. Woh apni friends ke saath Krishna ki beauty aur sweetness ki baatein karne lagi.

Lekin Krishna ko yaad karke woh itni emotional ho gayin ki properly bol bhi nahi pa rahi thi.

Unke minds mein Krishna ka beautiful form aa gaya —

Peacock feather crown, yellow clothes, flower garland aur lips par flute. Cowherd boys unki glory gaate hue unke saath chal rahe the.

Gopīs lovingly boli,

“Friends, eyes ka real purpose sirf Krishna ko dekhna hai. Isse bada blessing aur kya ho sakta hai?”

Unhone kaha,

“Krishna aur Balarāma jab forest mein flowers aur peacock feathers pehenkar dance aur sing karte hain, tab woh stage actors se bhi zyada beautiful lagte hain.”

Fir Gopīs flute ko dekhkar jealous hone lagi.

Woh boli,

“Yeh flute kitni lucky hai! Yeh freely Krishna ke lips ka nectar enjoy karti rehti hai, jo actually hamara right hona chahiye tha!”

Unhone imagine kiya ki bamboo trees aur rivers bhi flute ki good fortune par happy hain. Rivers lotuses khilaakar joy express kar rahi hain aur bamboo trees dew drops ke through tears of happiness baha rahe hain.

Fir Gopīs ne Vṛndāvana ki glory praise ki.

“Vṛndāvana earth ka sabse blessed place hai, kyunki Krishna ke lotus feet usko touch karte hain.”

Unhone dekha ki peacocks Krishna ki flute sunkar happily dance kar rahe hain aur dusre animals quietly unhe dekh rahe hain.

Gopīs boli,

“Even deer kitne blessed hain! Woh apne husbands ke saath Krishna ko loving glances se worship kar paati hain.”

Heaven ki celestial women bhi Krishna ki flute sunkar enchanted ho jaati thi. Unke flower garlands aur hair tak loose ho jaate the.

Cows bhi Krishna ki flute sunkar motionless ho jaati thi. Calves apne mouths mein milk hold karke bas Krishna ko stare karte rehte the. Tears of joy unki eyes se nikalte the.

Gopīs ne birds ko dekhkar kaha,

“Yeh birds surely great sages honge. Woh silently branches par baithkar bas Krishna ki flute sunte rehte hain, bilkul deep meditation ki tarah.”

Rivers bhi Krishna ki taraf slowly flow karte hue apni waves se unke feet ko hug karne ki koshish karti thi.

Clouds Krishna ko sun se protect karne ke liye umbrella ki tarah unke upar shadow bana dete aur flower-like rain barsaate.

Gopīs ne Govardhana Hill ko bhi praise kiya.

“Govardhana sabse great servant hai, kyunki woh Krishna, Balarāma, cows aur cowherd boys ko water, caves, grass aur fruits provide karta hai.”

Is tarah Krishna ki flute aur forest pastimes ki baatein karte karte Gopīs completely Krishna mein absorbed ho gayin."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 22
    with st.expander("Chapter 22 - Cowherd-maids Pray to Kātyāyanī"):
        text1 = """ 
        🌸 The Gopīs Pray to Goddess Kātyāyanī

Śrī Śuka ne kaha,

Winter season ke first month mein Vraja ki young Gopīs ek special vow observe karne lagi. Unki ek hi wish thi — Krishna unke husband banein.

Roz subah bahut early woh sab Yamunā river par jaati thi. Wahan river bank ki sand se Goddess Kātyāyanī ki murti banaakar unki worship karti thi."""
        create_image_text_layout(
            "attached_assets/chapter10/10.22.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Woh sandal paste, flowers, incense, lamps, fruits aur grains offer karti aur ek prayer repeat karti thi:

“O Goddess Kātyāyanī, please Nanda Baba ke son Krishna ko hamara husband bana dijiye.”

Ek poore month tak Gopīs simple pure food khaakar yeh vow karti rahi. Roz ek dusre ko naam se bulaakar Yamunā jaati aur Krishna ki glory gaate hue bath leti thi.

Ek din vow ke last day par sab Gopīs apne clothes river bank par rakhkar happily water mein play karne lagi. Unka mind completely Krishna mein absorbed tha.

Krishna sab samajh gaye.

Woh apne cowherd friends ke saath quietly wahan aaye aur sab Gopīs ke clothes lekar ek Kadamba tree par chadh gaye.

Fir laughingly bole,

“O girls! Agar tumhe apne clothes chahiye, toh yahan aakar le lo.”

Cowherd boys bhi Krishna ke saath hansne lage.

Gopīs sharm aur love se confuse ho gayin. Woh cold water mein neck tak chupkar khadi rahi.

Woh pleading voice mein boli,

“O Krishna, please hamare saath aisa mat karo. Hum thand se kaanp rahe hain. Aap Vraja ke most loved boy ho, please hamare clothes wapas de do.”

Unhone softly threaten bhi kiya,

“Agar aapne clothes return nahi kiye, toh hum Nanda Baba ko bata denge.”

Krishna mischievously smile karke bole,

“Agar tum meri servants ho aur meri baat maanti ho, toh bahar aakar apne clothes le lo.”

Finally Gopīs shivering body ke saath water se bahar aayi. Woh apne hands se khud ko cover karne ki koshish kar rahi thi.

Krishna ne lovingly unki purity aur devotion dekhi aur smile karne lage.

Fir unhone playfully kaha,

“Tumne sacred vow observe karte hue nude bath liya hai. Pehle folded hands se respectfully bow karo, fir apne clothes le lo.”

Gopīs ne obediently Krishna ko pranam kiya.

Krishna unki sincere devotion se very pleased ho gaye aur unke clothes wapas de diye.

Gopīs ko Krishna ke saath yeh time itna precious laga ki woh bilkul angry nahi hui. Woh bas shy smiles aur loving glances se Krishna ko dekhti rahi.

Tab Krishna ne gently kaha,

“Main tumhari wish already jaanta hoon. Tumhari devotion mujhe pasand hai aur future mein tumhari desire fulfill hogi.”

“Tum autumn nights mein mere saath joyful pastimes enjoy karogi.”

Yeh sweet words sunkar Gopīs ka heart happiness se bhar gaya. Woh Krishna ke lotus feet ko mind mein yaad karti hui dheere dheere Vraja wapas laut gayin.

Uske baad Krishna, Balarāma aur cowherd boys cows ko lekar forest mein aur deep chale gaye.

Raste mein Krishna ne apne friends ko trees ki greatness samjhayi.

Woh bole,

“Trees kitne noble hote hain. Yeh heat, rain aur storms khud bear karte hain, lekin dusron ko shade, fruits, flowers aur shelter dete hain.”

“Ek truly good life wahi hai jo dusron ke benefit ke liye use ho.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 23
    with st.expander("Chapter 23 - Spiritual Emancipation of the Wives of Brāhmaṇa Sacrificers"):
        text1 = """ 
        🍚 The Wives of the Brāhmaṇas Meet Krishna

Śrī Śuka ne kaha,

Ek din Krishna, Balarāma aur cowherd boys forest mein cows chara rahe the. Bahut der tak ghoomne ki wajah se sab boys ko zor ki bhookh lag gayi.

Cowherd boys Krishna se bole,

“O Krishna! O powerful Balarāma! Hume bahut bhookh lagi hai. Please kuch food arrange kijiye.”"""
        create_image_text_layout(
            "attached_assets/chapter10/10.23.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Krishna smile karke bole,

“Nearby kuch Brāhmaṇas ek big sacrifice perform kar rahe hain. Tum log wahan jao aur hamare naam se cooked food maango.”

Cowherd boys respectfully Brāhmaṇas ke paas gaye aur folded hands se bole,

“Krishna aur Balarāma nearby cows chara rahe hain. Unhe aur hume bhookh lagi hai. Please thoda food dijiye.”

Lekin woh Brāhmaṇas rituals aur sacrifices mein itne busy the ki unhone boys ki baat ignore kar di. Woh spiritually proud the aur Krishna ko ek ordinary village boy samajh rahe the.

Disappointed hokar cowherd boys Krishna ke paas wapas aa gaye aur sab bata diya.

Krishna lightly hans pade aur bole,

“Ab Brāhmaṇas ki wives ke paas jao. Woh mujhe bahut love karti hain. Woh zaroor food dengi.”

Boys Brāhmaṇa ladies ke paas gaye aur respectfully bole,

“Krishna aur Balarāma nearby hain aur hungry hain.”

Jaise hi ladies ne Krishna ka naam suna, unke hearts excitement aur devotion se bhar gaye. Woh pehle se hi Krishna ki stories sunkar unse deeply attached thi.

Woh immediately delicious food — rice, sweets, fruits aur many dishes — vessels mein bharne lagi aur Krishna ki taraf daud padi.

Unke husbands, brothers aur relatives ne unhe rokne ki koshish ki, lekin unhone kisi ki baat nahi maani.

Finally woh Yamunā ke bank par Krishna ko dekh paayi.

Krishna dark-blue complexion mein shine kar rahe the. Peacock feathers, flower garlands aur yellow silk clothes mein woh unbelievably beautiful lag rahe the.

Ladies Krishna ko dekhkar itni overwhelmed ho gayin ki unka saara sorrow aur separation instantly disappear ho gaya.

Krishna lovingly bole,

“Welcome! Tumhara yahan aana bahut auspicious hai. Batao, main tumhare liye kya kar sakta hoon?”

Fir Krishna ne gently samjhaya,

“True wise people without selfish motives mujhme devotion rakhte hain, kyunki main sabka real beloved Self hoon.”

Uske baad Krishna ne kaha,

“Ab tum apne homes wapas jao. Tumhare husbands tumhe reject nahi karenge.”

Lekin Brāhmaṇa ladies emotional hokar boli,

“O Krishna, hum sab kuch chhodkar aapke paas aaye hain. Please hume reject mat kijiye.”

Krishna ne kindly reassure kiya,

“Fear mat karo. Sab tumhe accept karenge. Aur agar tum apna mind hamesha mujhme fix rakhogi, toh tum jaldi hi mujhe attain kar logi.”

Krishna ki command maan kar woh ladies reluctantly wapas chali gayin. Unke husbands surprisingly unse angry nahi hue aur sacrifice peacefully continue hua.

Ek lady jo forcefully roki gayi thi, woh Krishna ko deeply meditate karte karte apna body hi leave kar gayi aur spiritually Krishna ko attain kar liya.

Krishna ne fir cowherd boys ko delicious food khilaya aur baad mein khud bhi khaya.

Meanwhile Brāhmaṇas ko apni mistake realize hui.

Woh shame se bole,

“Fie upon our scholarship aur rituals! Hum Vedas jaante hue bhi Krishna ko pehchaan nahi paaye.”

Unhone accept kiya,

“Hamaari wives humse zyada blessed hain, kyunki unki devotion pure aur true hai.”

Fir woh Krishna se heart mein forgiveness maangne lage, lekin Kans ke fear ki wajah se unke paas personally ja nahi paaye."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 24
    with st.expander("Chapter 24 - Prevention of Sacrifice to Indra"):
        text1 = """ 
        ⛰️ Krishna Stops the Worship of Indra

Śrī Śuka ne kaha,

Ek time Vṛndāvana mein cowherds rain-god Indra ke liye big sacrifice prepare kar rahe the. Krishna sab jaante the, lekin unhone innocent child ki tarah act kiya.

Krishna politely Nanda Baba aur elder Gopas se bole,

“Father, aap sab itni busy preparations kyun kar rahe ho? Yeh sacrifice kisliye hai?”

Nanda Baba ne explain kiya,"""
        create_image_text_layout(
            "attached_assets/chapter10/10.24.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        “Indra rain ka lord hai. Rain se crops aur grass grow hoti hain. Isliye hum uski worship karte hain.”

“Hum cowherds aur farmers sab uski blessings par depend karte hain.”

Krishna ne calmly answer diya,

“People ko apne actions aur nature ke according results milte hain. Sirf Indra hi sab kuch control nahi karta.”

Fir Krishna ne cowherds ko important lesson diya.

Woh bole,

“Har person ko apna natural duty follow karna chahiye. Hum forest-dwellers hain. Hum cows, mountains aur forests par depend karte hain.”

“Isliye hume Govardhana mountain, cows aur Brāhmaṇas ki worship karni chahiye.”

Krishna ne suggest kiya,

“Indra ke liye jo food aur preparations ready hain, unhe Govardhana festival mein use karo.”

Fir Krishna ne detail mein bataya kya kya prepare karna hai.

“Sweet rice, puddings, cakes, milk preparations aur many delicious foods banao. Brāhmaṇas ko charity do, cows ko grass khilao aur sab log happily feast karo.”

“Uske baad ornaments aur nice clothes pehenkar Govardhana mountain ki circumambulation karo.”

Nanda Baba aur sab Gopas ko Krishna ki baat bahut achhi lagi.

Sabne happily kaha,

“Bilkul sahi!”

Fir unhone Krishna ke instructions follow kiye.

Brāhmaṇas ne prayers aur blessings diye. Delicious foods huge quantity mein prepare hue. Cows ko feed kiya gaya aur Govardhana mountain ko offerings diye gaye.

Gopīs Krishna ki glories gaate hue decorated bullock carts par mountain ke around parade karne lagi.

Tab Krishna ne ek amazing miracle kiya.

Unhone ek gigantic divine form appear kiya aur loudly announce kiya,

“Main hi Govardhana mountain hoon!”

Us huge form ne saari offerings happily consume kar li.

Cowherds yeh dekhkar shock aur wonder se bhar gaye.

Krishna fir apne normal form mein bhi sabke saath mountain ko bow karne lage aur bole,

“Dekho! Govardhana mountain ne hamari worship accept kar li.”

Sab Gopas aur Gopīs joyfully Govardhana ko pranam karne lage.

Is tarah Krishna ne Vraja-vāsīs ko Govardhana, cows aur Brāhmaṇas ki worship karna sikhaya aur indirectly Indra ke pride ko challenge kiya."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 25
    with st.expander("Chapter 25 - Lifting up of Mount Govardhana"):
        text1 = """ 
        ⛰️ Krishna Lifts Govardhana Mountain

Śrī Śuka ne kaha,

Jab Indra ko pata chala ki Vraja-vāsīs ne uski worship stop karke Govardhana festival celebrate kiya hai, toh woh bahut angry ho gaya.

Usne proudly socha,

“Yeh simple cowherds ek mortal boy Krishna ki baat maan kar mujhe insult kar rahe hain!”

Gusse mein Indra ne destructive Saṁvartaka clouds ko bulaya — woh same clouds jo universe destruction ke time use hote hain.

Indra ne order diya,"""
        create_image_text_layout(
            "attached_assets/chapter10/10.25.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        “Jaao! Vraja ko storms aur floods se destroy kar do. In arrogant cowherds aur unki cows ko punish karo!”

Fir terrifying storm start hua.

Sky dark clouds se bhar gaya. Thunder loudly roar karne laga, lightning flash hone lagi aur giant hailstones girne lage.

Rain itni heavy thi ki poori earth flood hone lagi. Strong winds sab kuch udaane lage.

Cows cold aur fear se kaanpne lagi. Gopas aur Gopīs apne children aur calves ko cover karke Krishna ke paas bhaage.

Sab crying voice mein bole,

“O Krishna! Aap hi hamare protector ho. Please hume Indra ke anger se bachaiye!”

Krishna samajh gaye ki yeh sab Indra ke pride ki wajah se ho raha hai.

Unhone calmly socha,

“Indra ko lagta hai ki woh supreme ruler hai. Ab uska pride todna zaroori hai.”

Fir Krishna ne apni divine yogic power use ki.

Sabke saamne unhone Govardhana mountain ko ek haath se uproot kar liya — bilkul aise jaise koi child mushroom uthata ho.

Krishna ne little finger par poora mountain hold kar liya.

Fir loudly bole,

“O Mother! O Father! O people of Vraja! Fear mat karo. Sab cows aur belongings ke saath mountain ke neeche aa jao.”

“Mountain meri hand se kabhi nahi girega.”

Vraja-vāsīs Krishna ki baat sunkar quickly mountain ke neeche shelter lene lage. Cows, carts, grains, families — sab safely andar aa gaye.

Krishna continuously seven days aur seven nights tak Govardhana ko hold kiye rahe. Woh bilkul tired nahi hue.

Sab Gopas aur Gopīs bas Krishna ko wonder aur love se dekhte rahe. Hunger aur thirst tak bhool gaye.

Indra yeh impossible miracle dekhkar shock ho gaya.

Uska pride completely break hone laga. Finally usne storms aur clouds ko rok diya.

Sky clear ho gaya. Sun shine karne laga aur floods dheere dheere disappear ho gaye.

Tab Krishna ne gently kaha,

“Ab danger khatam ho gaya hai. Sab bahar aa sakte ho.”

Cowherds slowly apni cows aur carts ke saath mountain ke neeche se bahar aaye.

Fir Krishna ne playfully Govardhana mountain ko uski original place par wapas rakh diya.

Sab Vraja-vāsīs love aur gratitude se Krishna ke paas daud pade. Gopīs ne curd aur rice se unki worship ki aur blessings dene lagi.

Yaśodā, Nanda Baba, Rohiṇī aur Balarāma ne Krishna ko tightly hug kiya.

Sky mein gods, Gandharvas aur heavenly beings flowers barsaane lage aur Krishna ki glory gaane lage.

Finally Krishna Balarāma aur cowherd boys ke saath happily Gokula wapas chale gaye, jabki Gopīs poore raste Krishna ke amazing miracle ke songs gaati rahi."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 26
    with st.expander("Chapter 26 - Conversation between Nanda and Cowherds"):
        text1 = """ 
        🐄 The Cowherds Wonder About Krishna

Śrī Śuka ne kaha,

Govardhana mountain lift karne ke baad Vraja ke cowherds completely amazed ho gaye. Unhe samajh hi nahi aa raha tha ki little Krishna itne impossible miracles kaise kar pa rahe hain.

Sab Nanda Baba ke paas gaye aur bole,"""
        create_image_text_layout(
            "attached_assets/chapter10/10.26.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        “Yeh child ordinary nahi ho sakta. Hum jaise simple cowherds ke ghar aisa divine boy kaise born ho sakta hai?”

Woh wonder se bole,

“Sirf seven years ka child itna huge Govardhana mountain ek hand par kaise hold kar sakta hai?”

Fir cowherds Krishna ke purane miracles yaad karne lage.

“Jab woh tiny baby the, tab unhone Pūtanā demoness ka life suck kar liya tha.”

“Ek month ke baby hoke bhi unhone kick maar kar heavy cart overturn kar diya tha.”

“Unhone Tṛṇāvarta demon ko sky mein hi kill kar diya.”

“Mother Yaśodā ne jab unhe mortar se baandha tha, tab crawling karte hue unhone do huge Arjuna trees gira diye.”

Cowherds aur excited hokar bole,

“Krishna ne Baka demon ka beak phaad diya, Dhenuka aur uske donkey friends ko destroy kar diya aur Kāliya serpent ko bhi defeat kar diya.”

“Unhone forest fire se bhi sabko save kiya!”

Fir sab lovingly Nanda Baba se bole,

“O Nanda, hum sab Krishna se deeply attached hain aur Krishna bhi hum sabko bahut love karte hain.”

“Lekin ab hume lagta hai ki Krishna ki real nature kuch divine hai.”

Tab Nanda Baba smile karke bole,

“Main tum sabko ek secret batata hoon jo sage Garga ne Krishna ke baare mein kaha tha.”

Nanda Baba ne explain kiya,

“Garga Muni ne kaha tha ki different yugas mein Krishna white, red aur yellow forms mein appear hue hain, aur ab woh dark-complexioned form mein aaye hain.”

“Unhone yeh bhi kaha tha ki Krishna pehle Vasudeva ke son ke roop mein born hue the, isliye wise people unhe Vāsudeva bhi kahenge.”

Nanda Baba ne proudly kaha,

“Krishna ke countless names aur forms hain. Woh Gokula ko happiness aur protection dene aaye hain.”

“Jo bhi Krishna se love karega, woh enemies aur dangers se protected rahega.”

Fir Nanda Baba calmly bole,

“Garga Muni ne kaha tha ki Krishna qualities aur power mein Lord Nārāyaṇa jaise hain. Isliye unke miracles par surprise nahi hona chahiye.”

Yeh sab sunkar Vraja-vāsīs ka fear aur confusion disappear ho gaya.

Ab woh Krishna ko aur bhi zyada love aur respect karne lage.

Sabke hearts gratitude se bhar gaye, kyunki Krishna ne Indra ke storm se poore Gokula ko protect kiya tha — bilkul ek playful child ki tarah mushroom uthaakar Govardhana mountain hold karke."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 27
    with st.expander("Chapter 27 - Indra coronates Kṛṣṇa"):
        text1 = """ 
        👑 Indra Apologizes to Krishna

Śrī Śuka ne kaha,

Jab Krishna ne Govardhana mountain lift karke poore Vraja ko save kar liya, tab Indra ka pride completely break ho gaya.

Usse realize hua ki Krishna koi ordinary child nahi, supreme divine Lord hain."""
        create_image_text_layout(
            "attached_assets/chapter10/10.27.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Tab heavenly wish-fulfilling cow Surabhi Goloka se Krishna ke paas aayi. Indra bhi shame aur regret ke saath wahan pahunch gaya.

Indra quietly Krishna ke paas gaya aur apna shining crown Krishna ke feet par rakhkar bow karne laga.

Folded hands ke saath woh deeply emotional voice mein bola,

“O Lord, aap pure spiritual existence ho. Aap par ignorance ya pride ka effect kabhi nahi hota.”

Indra ne accept kiya,

“Main apni power aur kingship ke pride mein blind ho gaya tha. Isi arrogance mein maine Vraja ko destroy karne ki foolish attempt ki.”

Woh regret se bola,

“Please mujhe forgive kar dijiye. Main aapki real greatness nahi samajh paaya.”

Indra ne samjha ki Krishna duniya ke protector hain aur proud people ka ego todkar unhe right path par laate hain.

Fir Krishna smilingly reply karne lage. Unki voice thundercloud jaisi deep thi.

Krishna bole,

“O Indra, tum apni heavenly power ke pride mein intoxicated ho gaye the. Isliye maine tumhari worship stop karwayi taki tum mujhe yaad rakho.”

Krishna ne calmly samjhaya,

“Jab kisi person ko apni wealth aur power ka too much pride ho jaata hai, tab kabhi kabhi main uska arrogance remove kar deta hoon — yeh bhi meri grace hoti hai.”

Fir Krishna ne gently kaha,

“Ab peacefully apne heavenly duties par wapas jao aur future mein pride mat karna.”

Uske baad celestial cow Surabhi Krishna ke saamne aayi aur boli,

“O Krishna! Aap hi cows, Brāhmaṇas aur saintly people ke real protector ho.”

“Aap hi hamare true Lord ho.”

Fir Surabhi ne Krishna ka special coronation karne ka decide kiya.

Surabhi ne apne divine milk se Krishna ka abhiṣeka kiya.

Indra ne bhi Airāvata elephant ke through heavenly Gaṅgā water laakar Krishna ko ceremonially bathe kiya. Gods, sages aur celestial beings bhi wahan gather ho gaye.

Tab Indra loudly announce karne laga,

“Main gods ka Indra hoon, lekin Krishna cows ke supreme Lord hain. Isliye duniya inhe Govinda ke naam se jaane gi!”

Yeh sunkar Gandharvas songs gaane lage, heavenly dancers dance karne lagi aur gods flowers barsaane lage.

Us divine moment mein poori creation happiness se bhar gayi.

Cows earth par milk bahaane lagi, rivers sweet drinks ki tarah flow karne lagi aur trees honey drip karne lage.

Even naturally violent animals bhi peacefully behave karne lage.

Finally Indra ne Krishna ko pranam kiya aur gods ke saath heaven wapas chala gaya."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 28
    with st.expander("Chapter 28 - Nanda rescued from Varuṇa"):
        text1 = """ 
        🌊 Krishna Rescues Nanda from Varuṇa

Śrī Śuka ne kaha,

Ekādaśī ke sacred day par Nanda Baba ne full fast rakha aur Lord Viṣṇu ki worship ki.

Next morning, yani Dvādaśī ke time, woh Yamunā river mein bath karne gaye.

Lekin unhe pata nahi tha ki woh dangerous night-time period tha jo demons ke liye reserved maana jaata tha.

Jaise hi Nanda Baba water mein gaye, Varuṇa ka ek servant unhe pakadkar underwater kingdom mein le gaya."""
        create_image_text_layout(
            "attached_assets/chapter10/10.28.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Jab cowherds ko Nanda Baba nahi mile, sab panic mein chillane lage,

“O Krishna! O Balarāma!”

Krishna immediately samajh gaye ki kya hua hai.

Apne devotees ki protection ke liye woh instantly Varuṇa ke realm mein pahunch gaye.

Varuṇa ne Krishna ko aate hi dekh liya.

Woh excitement aur devotion se bhar gaya aur respectfully Krishna ko worship karne laga.

Varuṇa folded hands ke saath bola,

“O Lord, aaj mera life successful ho gaya. Oceans ke treasures bhi aapke darshan ke saamne kuch nahi hain.”

Usne deeply humble voice mein kaha,

“Mera servant ignorant tha. Usne mistake se aapke father ko yahan le aaya. Please uski fault forgive kar dijiye.”

Fir Varuṇa lovingly bola,

“O Krishna, yeh aapke father hain. Please inhe apne saath wapas le jaiye.”

Krishna peacefully Nanda Baba ko lekar Vraja wapas aa gaye.

Sab cowherds Nanda Baba ko safe dekhkar bahut happy ho gaye.

Nanda Baba excitement aur amazement se sabko Varuṇa ke divine underwater kingdom ke baare mein bataane lage.

Woh bole,

“Varuṇa aur dusre great gods bhi Krishna ko supreme respect dete hain!”

Yeh sunkar Vraja-vāsīs aur bhi zyada wonder mein bhar gaye.

Unhone socha,

“Krishna definitely supreme divine Lord hain. Kaash hum bhi unka eternal spiritual world dekh paayein.”

Krishna sabke hearts ki wish samajh gaye.

Out of compassion, unhone decide kiya ki woh Vraja-vāsīs ko apna divine eternal realm dikhaayenge.

Krishna ne unhe ek special spiritual state experience karwayi — jo ignorance aur material suffering se completely beyond thi.

Fir unhone apna eternal divine abode reveal kiya.

Wahan everything eternal, self-luminous aur full of pure spiritual bliss tha. Great sages meditation ke through jis state ko realize karte hain, Vraja-vāsīs ne Krishna ki grace se directly uska darshan kiya.

Nanda Baba aur dusre cowherds ne wahan Krishna ko divine hymns aur Vedas ke praises ke beech glorified hota hua dekha.

Sab overwhelming joy aur amazement se bhar gaye."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 29
    with st.expander("Chapter 29 - Lord Kṛṣṇa’s Rāsa with Gopīs"):
        text1 = """ 
🌕 Krishna Calls the Gopīs with His Flute

Śrī Śuka ne kaha,

Autumn season ki beautiful full-moon nights aa gayin. Jasmine flowers ki fragrance aur cool moonlight se Vṛndāvana magical lag raha tha.

Krishna ne apni divine Yogamāyā power se rāsa pastime karne ka decide kiya.

Moon sky mein rise hua aur uski soft silver light forests aur Yamunā ko beautify karne lagi.

Usi time Krishna ne apni flute bajaani shuru ki."""
        create_image_text_layout(
            "attached_assets/chapter10/10.29.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Unki flute ki sweet melody sunkar Vraja ki Gopīs ke hearts completely Krishna ki taraf khinch gaye.

Woh itni attracted ho gayin ki sab apna kaam beech mein hi chhodkar Krishna ki taraf daudne lagi.

Koi cows milk kar rahi thi aur kaam aadha chhod diya. Koi stove par milk boil kar rahi thi aur waise hi chhod diya.

Koi husbands ko food serve kar rahi thi, koi babies ko feed kar rahi thi, koi khud kha rahi thi — lekin sab instantly sab kuch bhoolkar Krishna ki taraf bhaag gayin.

Kuch Gopīs jaldi mein ulte-seedhe ornaments aur clothes pehenkar hi nikal padi.

Families ne unhe rokne ki koshish ki, lekin Krishna ke love mein absorbed Gopīs kisi ki baat nahi maani.

Kuch Gopīs ko ghar mein lock bhi kar diya gaya.

Woh bahar nahi aa paayin, toh unhone eyes close karke Krishna ka deep meditation kiya. Krishna ki separation ki intense feeling mein unhone material bondage tak transcend kar diya.

Finally Gopīs Krishna ke paas forest mein pahunch gayin.

Krishna ne loving smile ke saath unka welcome kiya, lekin playfully unki devotion test karne lage.

Woh bole,

“Welcome, O beautiful ladies! Itni raat ko tum sab yahan kyun aayi ho?”

Krishna ne teasing tone mein kaha,

“Yeh forest dangerous hai. Wild animals yahan ghoomte hain. Tumhe ab ghar wapas jaana chahiye.”

“Tumhare parents, husbands aur relatives tumhe dhoondh rahe honge.”

Fir Krishna ne kaha,

“Good women ko apne husbands, children aur family ki service karni chahiye.”

“Sirf physically mere paas rehna hi devotion nahi hota. Mere stories sunna, mujhe remember karna aur meri glories gaana bhi enough hai. Isliye ab wapas jao.”

Krishna ki yeh baatein sunkar Gopīs deeply sad ho gayin.

Unki eyes tears se bhar gayin aur woh silence mein ground ko toe se scratch karne lagi.

Fir trembling voice mein unhone Krishna se kaha,

“O Lord, aap humse itni harsh baat kaise kar sakte ho? Hum sab kuch chhodkar sirf aapke paas aaye hain.”

Gopīs boli,

“Aap sabke real soul aur dearest beloved ho. Jab aap mil gaye, toh worldly husbands aur relatives kya value rakhte hain?”

Unhone helplessly kaha,

“Hamaare hearts, hands aur feet sab aapne chura liye hain. Ab hum ghar jaakar bhi kya kar sakte hain?”

Fir woh emotional prayer karne lagi,

“Aapki flute, smiles aur glances ne hamaare hearts mein intense longing jaga di hai. Please hume reject mat kijiye.”

“Aapke lotus feet ki dust tak Goddess Lakṣmī desire karti hain. Hum bhi bas aapki servants banna chahti hain.”

Krishna unki sincere love aur devotion dekhkar smile karne lage.

Out of mercy unhone Gopīs ko accept kiya aur unke saath forest mein joyful pastimes karne lage.

Krishna flowers ki Vaijayantī garland pehne hue full moon ki tarah shine kar rahe the, aur Gopīs stars ki tarah unke around gathered thi.

Woh sab Yamunā ke cool sandy banks par ghoomne lage. Gentle breeze aur lotus fragrance atmosphere ko aur sweet bana rahi thi.

Krishna jokes, smiles, playful glances aur loving gestures se Gopīs ko happiness dene lage.

Lekin dheere dheere kuch Gopīs ko apni special fortune par pride feel hone laga.

Har Gopī sochne lagi ki Krishna usse sabse zyada love karte hain.

Krishna ne unke hearts ka yeh pride samajh liya.

Aur unka ego remove karne ke liye suddenly Krishna un sabke beech se disappear ho gaye."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 30
    with st.expander("Chapter 30 - Search after Kṛṣṇa"):
        text1 = """ 
        🌌 The Gopīs Search for Krishna

Śrī Śuka ne kaha,

Jab Krishna suddenly disappear ho gaye, tab Gopīs deeply heartbroken ho gayin. Woh bilkul un female elephants ki tarah distressed thi jinse unka leader bichhad gaya ho.

Krishna ki smiles, loving glances, sweet talks aur playful pastimes unke minds mein continuously chal rahe the."""
        create_image_text_layout(
            "attached_assets/chapter10/10.30.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Separation mein woh itni absorbed ho gayin ki Krishna ki actions imitate karne lagi.

Koi Gopī proudly bolti,

“Main Krishna hoon!”

Sab milkar Krishna ke songs gaane lagi aur forests mein unhe search karne lagi — bilkul lovesick people ki tarah.

Woh trees aur plants se bhi poochne lagi,

“O Aśvattha tree! O Kadamba tree! Kya tumne Nanda ke son Krishna ko dekha?”

“Kya woh yahan se apni charming smile ke saath guzre the?”

Tulasi plant se woh lovingly boli,

“O blessed Tulasi! Tum Krishna ko bahut dear ho. Kya tumne Govinda ko yahan dekha?”

Fir woh Earth se poochne lagi,

“O Earth, tumne kaunsi tapasya ki thi jo Krishna ke lotus feet tumhe touch karte hain?”

Searching ke dauraan Gopīs Krishna ke old childhood pastimes bhi act karne lagi.

Ek Gopī Pūtanā ban gayi aur doosri baby Krishna bankar uska milk peene lagi.

Koi cart demon Śakaṭāsura ka role play karne lagi aur doosri Krishna bankar usse kick maarne lagi.

Koi Govardhana-līlā imitate karte hue apna cloth uthaakar boli,

“Fear mat karo! Main tum sabko storm se protect karungi!”

Ek Gopī flute bajane ka acting karne lagi aur baaki sab happily clap karne lagi.

Koi forest fire pastime imitate karke boli,

“Sab eyes close karo! Main tumhe fire se save karti hoon!”

Is tarah Krishna ki remembrance mein woh completely lost ho gayin.

Suddenly searching karte karte unhe ground par Krishna ke footprints dikhayi diye.

Gopīs excitement se boli,

“Yeh definitely Krishna ke footprints hain! In par lotus, flag aur vajra ke divine marks hain.”

Lekin kuch distance baad unhone notice kiya ki Krishna ke footprints ke saath ek woman ke footprints bhi hain.

Sab thodi jealous aur sad hokar boli,

“Kaunsi lucky Gopī hai jise Krishna apne saath le gaye?”

“Usne definitely Krishna ko special devotion se please kiya hoga.”

Fir woh clues dekhte hue imagine karne lagi ki Krishna us special Gopī ke saath kya kar rahe honge.

Kisi ne kaha,

“Dekho, yahan us Gopī ke footprints missing hain. Shayad Krishna ne uske soft feet ko grass se bachane ke liye use shoulders par utha liya.”

Dusri boli,

“Yahan Krishna flowers gather kar rahe the uske hair decorate karne ke liye.”

Aage jaakar unhe wahi special Gopī akeli aur crying condition mein mili.

Usne sadly bataya,

“Krishna mujhe alone le gaye the. Mujhe pride ho gaya aur maine kaha ki main chal nahi sakti.”

“Krishna ne bola, ‘Mere shoulders par chadh jao,’ lekin jaise hi maine try kiya… woh suddenly disappear ho gaye.”

Woh regret aur sorrow mein Krishna ko pukaarne lagi,

“O beloved Krishna! Please wapas aa jao!”

Moonlight dheere dheere disappear hone lagi, isliye Gopīs forest search stop karke Yamunā river ke sandy banks par wapas aa gayin.

Wahan baithkar woh sirf Krishna ke baare mein baat karne, unki glories gaane aur unke return ka wait karne lagi."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 31
    with st.expander("Chapter 31 - Gopīs’ song (prayer for Kṛṣṇa’s return)"):
        text1 = """ 
        🌙 The Gopīs Sing in Separation from Krishna

Śrī Śuka ne kaha,

Yamunā ke sandy banks par baithkar Gopīs Krishna ki separation mein deeply sad ho gayin.

Unke hearts sirf Krishna ke thoughts se filled the.

Fir one by one woh Krishna ke liye emotional songs gaane lagi.

Gopīs boli,"""
        create_image_text_layout(
            "attached_assets/chapter10/10.31.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        “O Krishna! Aapke birth ki wajah se Vraja blessed aur prosperous ban gaya hai.”

“Hum sirf aapko dekhne ki hope mein zinda hain. Please hume apna darshan dijiye.”

Fir woh painful voice mein boli,

“O beloved! Aapki lotus-like eyes aur beautiful glances hume love se fill kar dete hain. Ab hume ignore karke kya aap hume maarna chahte ho?”

Gopīs Krishna ke past protections yaad karne lagi.

“Aapne hume poisonous water, Aghāsura serpent, storms, lightning, forest fire aur many demons se bachaya tha.”

“Toh ab humari protection kyun nahi kar rahe?”

Fir unhone Krishna ki divine nature ko remember kiya.

“Aap sirf Yaśodā ke son nahi ho. Aap sab living beings ke hearts mein present Supreme Lord ho.”

Gopīs folded hands ke saath pray karne lagi,

“Please apna lotus hand humare heads par rakhiye aur hume fear aur sorrow se protect kijiye.”

“O Vraja ke protector! Apni sweet smiling face ka darshan dijiye.”

Woh intensely emotional hokar boli,

“Apne lotus feet humare hearts par rakhiye — wahi feet jo cows ke piche forests mein chalte hain aur Kāliya serpent ke heads par dance kar chuke hain.”

“Unhi feet se humare hearts ka burning pain remove ho sakta hai.”

Fir Gopīs Krishna ki sweet speech aur lips ko remember karne lagi.

“Aapki words aur smile humari life hain. Please hume apne lips ka nectar dijiye aur hume revive kijiye.”

Ek Gopī lovingly boli,

“Blessed hain woh log jo Krishna ki stories gaate hain. Unki kathā nectar se bhi sweeter hai aur sab sorrow destroy kar deti hai.”

Fir sab Krishna ki playful acts yaad karke aur emotional ho gayin.

“Aapke laughs, loving glances aur secret jokes humare hearts ko completely restless bana dete hain.”

Gopīs worried voice mein boli,

“Jab aap cows graze karne forests mein jaate ho, hum sochte rehte hain ki soft lotus feet ko sharp grass aur stones hurt toh nahi kar rahe.”

Evening return ka scene yaad karke woh aur emotional ho gayin.

“Jab aap curly hair aur cow-dust se covered face ke saath wapas aate ho, humari love aur bhi increase ho jaati hai.”

Fir woh sadly complain karne lagi,

“Brahmā ne eyelids kyun banaye? Blink karne ki wajah se hum ek moment ke liye bhi aapko dekh nahi paate.”

Gopīs boldly boli,

“Humne husbands, children aur relatives sab kuch chhodkar sirf aapke paas aana choose kiya.”

“O Krishna, ab hume abandon mat kijiye.”

Woh Krishna ke loving promises aur smiles yaad karke aur bhi overwhelmed ho gayin.

“Aapka broad chest, sweet glances aur charming smile humare hearts mein endless longing jagate hain.”

Finally sab Gopīs deeply humble voice mein boli,

“O Krishna, aapka appearance duniya ka sorrow remove karne ke liye hua hai.”

“Please humari separation pain bhi remove kijiye.”

“Humare hearts aur lives completely aapke hain.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 32
    with st.expander("Chapter 32 - Kṛṣṇa comforts Gopīs"):
        text1 = """ 
        🌙 Krishna Comforts the Gopīs

Śrī Śuka ne kaha,

Krishna ki separation mein Gopīs loudly ro rahi thi, unka naam gaa rahi thi aur pain mein kabhi kabhi incoherent baatein bhi karne lagi thi.

Tabhi suddenly Krishna unke beech appear ho gaye."""
        create_image_text_layout(
            "attached_assets/chapter10/10.32.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Unka lotus-like smiling face, yellow clothes aur flower garland dekhkar woh Cupid ko bhi enchant karne wale lag rahe the.

Krishna ko dekhte hi weak aur sorrowful Gopīs instantly joy se bhar gayin — bilkul dead body mein life wapas aa jaaye waise.

Woh Krishna ki beauty ko apni eyes se continuously drink karne lagi, lekin fir bhi unka heart satisfy nahi ho raha tha.

Ek Gopī happily Krishna ka lotus-hand pakadne lagi.

Dusri ne lovingly unka sandal-paste smeared arm apne shoulder par rakh liya.

Ek aur Gopī ne Krishna ka chewed betel apne hands mein receive kiya, jabki dusri love mein trembling condition mein unke lotus-feet apne chest par rakhne lagi.

Koi Gopī fake anger se Krishna ko side-glances dene lagi aur lips bite karne lagi.

Ek dusri Gopī Krishna ke face ko bina blink kiye bas dekhti hi rahi.

Ek aur Gopī ne Krishna ko apni eyes ke through heart mein imagine kiya aur eyes close karke mentally unhe hug karne lagi. Uska body spiritual bliss se thrill hone laga.

Krishna ko dekhkar sab Gopīs ka separation pain disappear ho gaya.

Krishna un sabke beech bilkul moon surrounded by stars ki tarah shine kar rahe the.

Fir Krishna unhe Yamunā ke beautiful sandy banks par le gaye.

Cool breeze jasmine flowers ki fragrance lekar chal rahi thi aur autumn moonlight poore atmosphere ko magical bana rahi thi.

Gopīs ne lovingly Krishna ke liye saffron-stained clothes se ek special seat prepare ki.

Krishna us par baith gaye aur poori gathering aur bhi divine lagne lagi.

Fir smiling aur playful glances ke saath Gopīs ne Krishna se slightly angry tone mein poocha,

“O Krishna, kuch log sirf unse love karte hain jo unhe love karte hain.”

“Kuch log unse bhi love karte hain jo unhe love nahi karte.”

“Aur kuch kisi se bhi love nahi karte. Aap batayiye inmein difference kya hai?”

Krishna gently smile karke reply karne lage.

Woh bole,

“Jo log sirf return mein love karte hain, unka love mostly self-interest par based hota hai.”

“Lekin jo unhe bhi love karte hain jo unse love nahi karte — jaise parents — unka love truly compassionate aur pure hota hai.”

Fir Krishna ne explain kiya,

“Kuch log kisi se bhi attachment nahi dikhate. Koi spiritual bliss mein absorbed hota hai, koi fully satisfied hota hai, koi ungrateful hota hai aur koi naturally cruel.”

Uske baad Krishna lovingly Gopīs ki taraf dekhkar bole,

“Lekin main in categories mein nahi aata.”

“Main kabhi kabhi apne devotees se temporarily hidden ho jaata hoon taki unka mind aur deeply mere thoughts mein absorbed ho jaaye.”

Krishna ne example diya,

“Jaise koi poor man apna lost treasure continuously remember karta hai, waise hi devotees mujhe intensely remember karte hain.”

Fir Krishna emotional voice mein bole,

“Tum sabne mere liye family, social customs aur worldly attachments tak chhod diye.”

“Main tumhari pure devotion ka debt kabhi repay nahi kar sakta.”

“Even gods ki long life bhi enough nahi hogi.”

Finally Krishna lovingly bole,

“Tumhari own pure devotion hi tumhara reward banegi.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 33
    with st.expander("Chapter 33 - Description of Rāsa Krīḍā"):
        text1 = """ 
        🌕 The Divine Rāsa Dance of Krishna

Śrī Śuka ne kaha,

Krishna ki sweet comforting words sunkar Gopīs ka separation pain completely disappear ho gaya.

Unka joy aur bhi increase ho gaya jab woh personally Krishna ke saath rehne lagi.

Yamunā ke sandy banks par Lord Govinda ne divine Rāsa dance start kiya."""
        create_image_text_layout(
            "attached_assets/chapter10/10.33.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Beautiful Gopīs circle banaakar Krishna ke saath dance karne lagi.

Tab Krishna ne apni amazing yogic power dikhayi.

Woh har do Gopīs ke beech ek alag form mein appear ho gaye.

Har Gopī ko laga,

“Krishna sirf mere saath dance kar rahe hain.”

Sky mein heavenly gods aur their wives bhi aerial chariots mein aakar yeh divine scene dekhne lage.

Drums bajne lage aur flowers ki rain hone lagi.

Gandharvas Krishna ki glory gaane lage.

Rāsa circle jingling bangles, anklets aur sweet music se bhar gaya.

Krishna golden Gopīs ke beech emerald jewel ki tarah shine kar rahe the.

Gopīs graceful dance steps, smiles aur playful eyebrow movements ke saath Krishna ki praise kar rahi thi.

Dance karte waqt unke hair loosen hone lage aur faces par tiny sweat drops sparkle karne lage.

Kuch Gopīs Krishna ke saath loudly different melodies mein songs gaane lagi.

Ek Gopī ne Krishna ke saath higher musical note mein sing kiya. Krishna happily bole,

“Well done!”

Ek dusri Gopī dance se tired hokar Krishna ke shoulder par lean kar gayi.

Dusri ne Krishna ke sandal-scented arm ko kiss kiya aur bliss se thrill ho gayi.

Ek aur Gopī ne Krishna ke cheek se apna cheek touch kiya, toh Krishna ne lovingly usse apna half-chewed betel diya.

Koi Gopī singing aur dancing se tired hokar Krishna ka lotus-hand apne chest par rakhne lagi.

Gopīs Krishna ko paakar endless happiness feel kar rahi thi.

Unke ornaments aur flower garlands loosen hokar girne lage, lekin joy mein woh unhe fix karna bhi bhool gayin.

Even celestial ladies Krishna ke divine love-sports dekhkar amazed aur enchanted ho gayin.

Moon-god bhi wonder mein ruk sa gaya.

Krishna har Gopī ke saath individually dance aur play kar rahe the, phir bhi fully self-controlled aur divine the.

Jab Gopīs dance se tired ho gayin, Krishna lovingly apne blissful hands se unke faces ka sweat wipe karne lage.

Fir Krishna aur Gopīs Yamunā river mein water-sports karne chale gaye.

Gods sky se flowers shower karte hue Krishna ki praise karne lage.

Krishna Gopīs ke saath cool fragrant groves mein happily wander karte rahe.

Śrī Śuka ne kaha,

In sab nights mein Krishna ne divine joy enjoy kiya, lekin unka mind completely controlled aur pure raha.

Tab King Parīkṣit confused hokar poochne lage,

“Krishna toh dharma establish karne aaye the. Fir unhone dusron ki wives ke saath aisa divine dance kyun kiya?”

Śrī Śuka calmly explain karne lage,

“Great divine beings ke actions ordinary humans jaise nahi hote.”

“Jaise fire impure cheezein consume karke bhi impure nahi hoti, waise hi Supreme Lord bhi untouched rehte hain.”

“Ordinary people ko unki imitation kabhi nahi karni chahiye.”

“Lord Krishna sabke hearts mein present Supreme Controller hain. Woh sab par grace shower karne ke liye human form mein aaye.”

Śrī Śuka ne finally kaha,

“Jo person faith aur devotion se Krishna ki Rāsa-līlā sunta ya narrate karta hai, uska heart gradually lust aur worldly desires se purified ho jaata hai.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 34
    with st.expander("Chapter 34 - Sudarśana emancipated and slaying of Śaṅkhacūḍa"):
        text1 = """ 
        🐍 Krishna Saves Nanda from the Giant Serpent

Śrī Śuka ne kaha,

Ek baar Vraja ke cowherds ne decide kiya ki woh Lord Śiva aur Goddess Pārvatī ke sacred place Ambikāvana ki pilgrimage karenge.

Sab bullock carts mein baithkar happily journey par nikle."""
        create_image_text_layout(
            "attached_assets/chapter10/10.34.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Wahan pahunchkar unhone Sarasvatī river mein bath liya aur devotion se Śiva aur Pārvatī ki worship ki.

Unhone Brahmanas ko cows, gold, clothes, honey aur sweets bhi donate kiye.

Nanda Baba aur dusre elders ne full-day fast rakha aur raat ko Sarasvatī river ke bank par rest karne lage.

Lekin late night ek huge hungry python wahan aa gaya.

Woh directly sleeping Nanda Baba ko nigalne laga.

Fear mein Nanda loudly chillaye,

“O Krishna! Krishna! Yeh giant serpent mujhe kha raha hai! Please mujhe bachao!”

Unki scream sunkar sab cowherds shock mein uth gaye.

Woh burning sticks lekar serpent ko maarne lage, lekin python ne Nanda Baba ko chhoda nahi.

Tab Lord Krishna quickly wahan pahunch gaye.

Krishna ne calmly us serpent ko apne lotus-foot se touch kiya.

Jaise hi Krishna ka divine touch mila, serpent ka curse instantly break ho gaya.

Woh ugly snake-body chhodkar ek shining heavenly being ban gaya.

Uska naam Sudarśana tha — ek Vidyādhara.

Krishna ne poocha,

“Tum kaun ho? Aur tumhe yeh horrible serpent form kyun mila?”

Sudarśana respectfully folded hands ke saath bola,

“Main pehle ek handsome heavenly Vidyādhara tha.”

“Mujhe apni beauty par bahut pride tha.”

“Ek baar maine ugly-looking sages ka insult aur mockery ki.”

“Un sages ne mujhe curse de diya ki main serpent ban jaaun.”

Lekin fir woh gratefully bola,

“Ab mujhe samajh aa gaya ki woh curse actually blessing tha.”

“Aapke lotus-feet ke touch se mere saare sins destroy ho gaye.”

“Jo sirf aapka name chant karta hai woh bhi purified ho jaata hai.”

“Toh jise aap personally touch karein, uska toh kya kehna!”

Sudarśana Krishna ko bow karke heaven wapas chala gaya.

Nanda Baba safe dekhkar sab Vraja-vāsīs Krishna ki divine power dekhkar amazed ho gaye.

Sab Krishna ki glories discuss karte hue Vraja wapas laut aaye.

💎 Krishna Slays Śaṅkhacūḍa

Ek dusri raat Krishna aur Balarāma Vraja ki Gopīs ke saath forest mein walk kar rahe the.

Moon aur stars sky mein shine kar rahe the aur cool fragrant breeze chal rahi thi.

Krishna aur Balarāma sweet melodies gaa rahe the.

Unki music sunkar Gopīs trance-like joy mein chali gayin.

Tabhi suddenly Kubera ka servant Śaṅkhacūḍa wahan aa gaya.

Woh boldly Gopīs ko forcefully north direction mein le jaane laga.

Gopīs fear mein loudly chillane lagi,

“O Krishna! O Balarāma! Save us!”

Krishna aur Balarāma immediately furious hokar uske piche daud pade.

Dono ne huge Śāla trees weapons ki tarah utha liye aur loudly assure kiya,

“Fear mat karo!”

Śaṅkhacūḍa jab un dono brothers ko death-gods ki tarah apni taraf aate dekha, toh woh terrified ho gaya.

Usne instantly Gopīs ko chhod diya aur khud bhaagne laga.

Balarāma Gopīs ko protect karne ke liye wahin ruk gaye, jabki Krishna directly Śaṅkhacūḍa ke piche bhaage.

Krishna ne quickly us evil Yakṣa ko catch kar liya.

Ek powerful punch se Krishna ne uska head aur uske shining jewel dono separate kar diye.

Śaṅkhacūḍa instantly mar gaya.

Krishna ne woh brilliant jewel uthaya aur affection se apne elder brother Balarāma ko de diya — sab Gopīs ke saamne."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 35
    with st.expander("Chapter 35 - Gopīs’ Song (in pairs of verses)"):
        text1 = """ 
        🎶 The Gopīs Sing About Krishna’s Flute

Śrī Śuka ne kaha,

Jab Krishna cows ko graze karane forest chale jaate the, tab Gopīs ka heart bhi unke saath chala jaata tha.

Separation mein woh poora din Krishna ke sweet pastimes aur flute ki glories gaati rehti thi.

Gopīs ek dusri se boli,"""
        create_image_text_layout(
            "attached_assets/chapter10/10.35.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        “O friends! Jab Krishna apni flute lips par rakhte hain aur eyebrows dance karte hue sweet melody bajate hain, tab even heavenly women bhi enchanted ho jaati hain.”

“Woh apne husbands ke saath sky mein travel kar rahi hoti hain, lekin Krishna ki flute sunkar love mein completely lost ho jaati hain.”

Fir Gopīs wonder se boli,

“Dekho Krishna ki flute ka magic!”

“Jab Nanda ka son smiling face ke saath flute bajata hai, tab cows aur deer bhi motionless ho jaate hain.”

“Unke mouths mein half-chewed grass tak ruk jaata hai, aur woh bas ears khade karke Krishna ko sunte rehte hain.”

Ek Gopī ne lovingly kaha,

“Jab Krishna peacock feather aur colorful forest decorations pehenkar flute bajate hain, tab rivers bhi flow karna stop kar deti hain.”

“Woh apni waves ke arms se Krishna ke lotus-feet ki dust touch karna chahti hain.”

Dusri Gopī Govardhana hill ki taraf dekhkar boli,

“Jab Krishna cows ko flute se naam lekar bulaate hain, tab trees aur creepers joy se bhar jaate hain.”

“Unki branches fruits aur flowers se bend ho jaati hain aur honey drip hone lagta hai.”

Fir ek Gopī ne lake ki birds ko notice kiya.

“Dekho swans aur cranes ko! Krishna ki flute sunkar woh eyes close karke silent meditation mein chale jaate hain.”

“Jaise great sages Lord Hari ka dhyān karte hain.”

Ek aur Gopī smilingly boli,

“Jab Krishna aur Balarāma mountain tops par flute aur songs perform karte hain, tab clouds bhi respectfully unke upar umbrella ki tarah spread ho jaate hain.”

“Clouds softly thunder karte hain — bilkul flute ki rhythm follow karte hue.”

Fir kuch Gopīs Yaśodā Maiyā se boli,

“O blessed Yaśodā! Aapka son kitna amazing hai.”

“Jab Krishna flute bajate hain, tab even Brahmā, Śiva aur Indra bhi unki music ko fully understand nahi kar paate.”

“Woh bas wonder mein sunkar khade reh jaate hain.”

Ek Gopī deeply emotional hokar boli,

“Jab Krishna lotus-feet se earth par chalte hain aur flute bajate hain, hum love mein completely stunned ho jaate hain.”

“Hume apne clothes aur hair tak ka hosh nahi rehta.”

Fir dusri Gopī happily boli,

“Jab Krishna cows count karte hue flute bajate hain aur friend ke shoulder par hand rakhte hain, tab female deer bhi unke piche chalne lagti hain.”

“Woh ghar wapas jaana tak bhool jaati hain — bilkul humari tarah.”

Ek aur Gopī Yamunā river ko dekhkar boli,

“Jab Krishna friends aur cows ke saath Yamunā bank par games khelte hain, tab cool fragrant breeze bhi lovingly unki service karti hai.”

“Even heavenly beings sky se aakar songs aur instruments ke saath unki worship karte hain.”

Fir Gopīs proudly Govardhana-līlā yaad karne lagi.

“Krishna ne cows aur Vraja-vāsīs ko protect karne ke liye Govardhana mountain lift kiya tha.”

“Woh truly sabke protector hain.”

Evening return ka thought aate hi Gopīs aur emotional ho gayin.

“Jab Krishna cows ke saath flute bajate hue ghar lautte hain, tab cow-dust unki flower garlands ko cover kar deti hai.”

“Us time woh evening moon ki tarah shine karte hain.”

Ek Gopī dreamy voice mein boli,

“Unki rolling eyes, golden earrings aur elephant-jaisi graceful walk humara poora day-long sorrow remove kar deti hai.”

Śrī Śuka ne kaha,

Is tarah Vraja ki blessed Gopīs Krishna ke flute aur pastimes gaate hue apna separation pain happily pass karti thi."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 36
    with st.expander("Chapter 36 - Akrūra deputed to bring Kṛṣṇa and Balarāma to Mathurā"):
        text1 = """ 
        🐂 Krishna Kills the Bull Demon Ariṣṭa

Śrī Śuka ne kaha,

Ek din Vraja mein suddenly ek terrifying demon aaya jo giant bull ke form mein tha. Uska naam Ariṣṭa tha.

Uska huge hump aur sharp horns dekhkar sab fear mein aa gaye.

Woh apne hoofs se earth ko tod raha tha aur loud terrifying roars kar raha tha.

Uski roar itni horrible thi ki cows aur women fear se tremble karne lagi."""
        create_image_text_layout(
            "attached_assets/chapter10/10.36.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Kuch pregnant cows aur women tak fear ki wajah se miscarriages suffer karne lagi.

Cattle panic mein Gokula chhodkar bhaagne lage.

Sab loudly Krishna ko pukaarne lage,

“O Krishna! Save us!”

Krishna calmly sabko reassure karte hue bole,

“Fear mat karo.”

Fir Krishna Ariṣṭa ke saamne khade ho gaye aur loudly challenge kiya,

“O wicked fool! Poor cowherds aur cows ko terrorize karke tumhe kya mil raha hai?”

“Main evil proud demons ka arrogance crush karne ke liye yahan hoon.”

Krishna ne apne arms clap karke us demon ko aur provoke kiya.

Furious Ariṣṭa bloodshot eyes ke saath thunderbolt ki tarah Krishna par charge karne laga.

Lekin Krishna ne uske horns pakad liye aur usse eighteen steps tak push back kar diya — bilkul elephant apne rival ko push karta hai waise.

Ariṣṭa phir bhi rukka nahi.

Woh fir se rage mein Krishna ki taraf dauda.

Tab Krishna ne uske horns pakadkar usse ground par violently phek diya.

Ek foot se usse press karke Krishna ne uska body twist kiya — bilkul wet cloth ko wring karte hain waise.

Fir Krishna ne uska ek horn todkar usi se usse strike kiya.

Ariṣṭa blood vomit karta hua, pain mein legs kick karta hua ground par gir gaya aur mar gaya.

Sky se gods flowers shower karne lage aur Krishna ki praise karne lage.

Krishna aur Balarāma victorious condition mein Gokula wapas aaye. Gopīs unhe dekhkar happiness se bhar gayin.

😨 Nārada Reveals Krishna’s Secret to Kaṃsa

Ariṣṭa ke death ke baad sage Nārada Kaṃsa ke paas gaye.

Unhone Kaṃsa ko truth bata diya,

“Krishna Devakī aur Vasudeva ke real son hain.”

“Balarāma Rohiṇī ke son hain.”

“Tumhare bheje hue demons ko in dono ne hi kill kiya hai.”

Yeh sunkar Kaṃsa extreme rage se bhar gaya.

Woh sword lekar Vasudeva ko maarne ke liye ready ho gaya.

Lekin usse roka gaya.

Fir Kaṃsa ne Vasudeva aur Devakī ko iron chains mein imprison kar diya.

Usne Keśī demon ko bhi order diya,

“Jaao aur Krishna-Balarāma ko maar do.”

🏟️ Kaṃsa’s Evil Plan

Kaṃsa ne apne wrestlers Cāṇūra aur Muṣṭika ko bulaya.

Woh bola,

“Krishna aur Balarāma mere death ka cause banne wale hain.”

“Jab woh Mathurā aayenge, tum wrestling match mein unhe kill kar dena.”

Usne giant elephant Kuvalayāpīḍa ko bhi arena entrance par ready rakhne ka order diya taki Krishna-Balarāma ko crush kiya ja sake.

Fir Kaṃsa ne apni hatred explain ki aur bola ki woh Vasudeva, Ugrasena aur Yadavas sabko destroy kar dega.

Woh proudly bola,

“Jarāsandha mera support karega. Śambara, Naraka aur Bāṇa bhi mere allies hain.”

“Main poori earth enjoy karunga.”

🚩 Akrūra is Sent to Bring Krishna to Mathurā

Finally Kaṃsa ne Akrūra ko bulaya.

Usne politely bola,

“O Akrūra, mujhe tum par trust hai. Please Vraja jaao aur Krishna-Balarāma ko Mathurā le aao.”

“Unhe bolo ki woh bow-sacrifice aur Mathurā city dekhne aayein.”

Lekin secretly Kaṃsa unhe kill karne ka plan bana raha tha.

Akrūra calmly reply karne lage,

“O King, man plans bahut kuch karta hai, lekin final result destiny decide karti hai.”

“Main aapka order follow karunga.”

Śrī Śuka ne kaha,

Iske baad Kaṃsa apne palace chala gaya aur Akrūra bhi apne home wapas laut gaya — Krishna se milne ki journey ki preparation karte hue."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 37
    with st.expander("Chapter 37 - Slaying of Asuras Keśin and Vyoma"):
        text1 = """ 
        🐎 Krishna Kills the Horse Demon Keśin

Śrī Śuka ne kaha,

Kaṃsa ne ek terrifying demon Keśin ko Krishna ko maarne ke liye bheja.

Keśin ne gigantic horse ka form liya.

Uski speed mind jaisi fast thi aur uski loud neighing se poora Vraja fear se tremble karne laga.

Uske huge mane ki movement se clouds aur heavenly chariots tak scatter ho rahe the."""
        create_image_text_layout(
            "attached_assets/chapter10/10.37.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Big eyes, giant mouth aur dark-cloud jaisi neck wala woh demon directly Nanda Baba ke Vraja ki taraf dauda.

Sab log fear mein aa gaye.

Tab Krishna calmly uske saamne khade ho gaye aur usse challenge karne lage.

Furious Keśin loudly roar karta hua Krishna ki taraf charge hua.

Woh apne hind legs se Krishna ko hard kick karna chahta tha.

Lekin Krishna ne easily dodge karke uske dono hind legs pakad liye.

Fir Krishna ne usse fast spin karke bahut door throw kar diya — bilkul Garuḍa snake ko phekta hai waise.

Keśin thodi der baad phir uth gaya.

Extreme anger mein usne huge mouth khola aur Krishna par dubara attack kiya.

Krishna fearlessly smile karte hue apna left arm uske mouth mein daal diya.

Jaise hi Keśin ne Krishna ka arm bite karna chaha, uske teeth red-hot iron touch karne jaise instantly tootkar gir gaye.

Krishna ka arm gradually huge hone laga aur Keśin ki breathing block ho gayi.

Woh pain mein legs kick karne laga, body sweat se bhar gayi aur eyes roll hone lagi.

Finally woh ground par girkar mar gaya.

Krishna ne calmly apna arm uske body se bahar nikala — bilkul ripe cucumber nikalte hain waise.

Gods sky se flowers shower karne lage aur Krishna ki praise karne lage.

Lekin Krishna ko slightest pride bhi nahi hua.

🌟 Nārada Praises Krishna

Keśin ke death ke baad sage Nārada Krishna ke paas aaye.

Woh respectfully bole,

“O Krishna! Aap sabke hearts mein present Supreme Lord ho.”

“Aap earth par demons ko destroy karne aur devotees ko protect karne aaye ho.”

Fir Nārada future events predict karne lage.

Woh bole,

“Main jaldi hi Kaṃsa, Cāṇūra, Muṣṭika aur Kuvalayāpīḍa elephant ka destruction dekhunga.”

“Main aapki many heroic deeds bhi dekhunga.”

Nārada ne Krishna ko bow kiya aur permission lekar wahan se chale gaye.

Krishna meanwhile happily cowherd boys ke saath cows graze karte rahe aur Vraja-vāsīs ko joy dete rahe.

🏔️ Krishna Saves the Cowherd Boys from Vyoma

Ek din Krishna aur cowherd boys mountain ke upar cows graze kar rahe the.

Wahan sab hide-and-seek jaisa game khelne lage.

Kuch boys thieves bane, kuch guards aur kuch sheep ka role play karne lage.

Tabhi secretly Vyoma naam ka demon wahan aaya.

Woh Maya demon ka son tha aur black magic mein expert tha.

Usne cowherd boy ka disguise liya aur game join kar liya.

Lekin secretly woh boys ko kidnap karne laga.

Woh har captured boy ko mountain cave mein daal deta aur huge rock se entrance close kar deta.

Thodi der mein sirf four-five boys hi bahar bache.

Krishna ne instantly us demon ki evil activity notice kar li.

Woh lion ki tarah quickly Vyoma ko pakadne daude.

Vyoma ne apna original giant mountain-like form le liya aur escape karne ki try ki, lekin Krishna ki grip se free nahi ho paaya.

Krishna ne usse ground par violently phek diya aur sacrifice animal ki tarah kill kar diya.

Gods sky se yeh heroic act dekh rahe the.

Uske baad Krishna ne cave entrance block karne wala huge rock tod diya aur sab cowherd boys ko safely bahar nikaal liya.

Gods aur cowherds sab Krishna ki loudly praise karne lage.

Fir Krishna sabke saath happily Gokula wapas laut aaye."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 38
    with st.expander("Chapter 38 - The Arrival of Akrūra to Gokula"):
        text1 = """ 
        🚩 Akrūra’s Joyful Journey to Meet Krishna

Śrī Śuka ne kaha,

Mathurā mein ek raat rukne ke baad Akrūra apni chariot par baithkar Nanda Baba ke Vraja ki taraf nikal pade.

Journey ke dauraan unka heart Krishna-bhakti se completely filled tha.

Woh khud se emotional thoughts karne lage,

“Maine kaunsa great punya kiya hoga ki aaj mujhe Lord Krishna ka darshan milega?”

“Krishna ka darshan paana bahut rare blessing hai.”

Akrūra deeply humble feel karte hue bole,"""
        create_image_text_layout(
            "attached_assets/chapter10/10.38.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        “Main toh ordinary aur material desires mein attached person hoon. Fir bhi shayad aaj mujhe Krishna ka audience mil jaaye.”

Woh happily sochne lage,

“Kaṃsa ne unknowingly mujh par bahut bada favor kiya hai.”

“Uske order ki wajah se hi main Krishna ke lotus-feet dekh paunga.”

Akrūra Krishna ke feet ko remember karte hue emotional ho gaye.

“Wahi lotus-feet jinko Brahmā, Śiva aur Lakṣmī worship karte hain…”

“Wahi feet jo Vṛndāvana forests mein cows ke saath walk karte hain aur Gopīs ke saffron se tinged hue hain.”

Fir unhone sky aur surroundings mein auspicious signs notice kiye.

Woh happily bole,

“Aaj mujhe definitely Krishna ka smiling lotus-face dekhne ko milega.”

“Curly hair, reddish eyes aur sweet smile wala woh divine face…”

Akrūra Krishna ki divine nature ko remember karte hue bole,

“Lord Krishna hi Supreme Soul hain jo sabke hearts mein secretly present hain.”

“Aur unki kathā duniya ke sins aur sorrow destroy karti hai.”

Fir woh lovingly imagine karne lage,

“Jaise hi main Krishna aur Balarāma ko dekhunga, main instantly chariot se utar kar unke feet mein bow karunga.”

“Shayad Krishna apna lotus-hand mere head par rakhen…”

“Shayad woh mujhe lovingly ‘Uncle Akrūra’ kehkar bulaayein.”

Yeh thoughts karte karte Akrūra evening time Vraja pahunch gaye.

Wahan unhone Krishna ke sacred footprints dekhe — jinpar lotus, flag, thunderbolt aur goad ke marks bane hue the.

Un footprints ko dekhkar Akrūra ka devotion uncontrollable ho gaya.

Unki eyes tears se bhar gayin aur body thrill se kaanpne lagi.

Woh chariot se jump karke Krishna ke foot-dust mein roll karne lage.

Akrūra repeatedly bol rahe the,

“Kitni blessed hai yeh dust jo Lord ke feet ko touch karti hai!”

Fir woh cows ke milking area mein pahuche.

Wahan unhone Krishna aur Balarāma ko dekha.

Krishna yellow clothes mein the aur Balarāma blue garments mein shine kar rahe the.

Dono ki eyes autumn lotuses ki tarah beautiful thi.

Krishna dark-blue emerald mountain jaise lag rahe the aur Balarāma silver mountain jaise shine kar rahe the.

Unke smiling eyes compassion aur sweetness se filled the.

Akrūra overwhelming devotion mein unke feet par full-length prostrate ho gaye.

Emotion ki wajah se woh properly apna introduction tak nahi de pa rahe the.

Krishna ne lovingly unhe apne hands se uthaya aur warmly hug kiya.

Balarāma ne bhi smile ke saath Akrūra ko embrace kiya aur respectfully ghar le gaye.

Wahan unhone perfect hospitality di.

Akrūra ke feet wash kiye gaye, unhe comfortable seat di gayi aur delicious food serve kiya gaya.

Meal ke baad unhe sweet betel, perfumes aur flower garlands bhi offer kiye gaye.

Sab formalities complete hone ke baad Nanda Baba sadly bole,

“O Akrūra, tum log cruel Kaṃsa ke rule mein kaise peacefully reh paate ho?”

“Woh toh apni own sister ke children tak ko maar chuka hai.”

“Hume samajh nahi aata uske kingdom mein koi safe kaise reh sakta hai.”

Akrūra Nanda Baba ki sweet hospitality aur loving words sunkar deeply touched ho gaye."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 39
    with st.expander("Chapter 39 - Akrūra returns with Kṛṣṇa and Balarāma"):
        text1 = """ 
        😢 The Gopīs Hear Krishna is Leaving for Mathurā

Śrī Śuka ne kaha,

Akrūra ko Krishna aur Balarāma ne great respect ke saath welcome kiya.

Dinner ke baad Krishna lovingly unse poochne lage,

“O dear uncle, kya Mathurā mein sab safe hain?”

“Kaṃsa hamare relatives ke saath kaise behave kar raha hai?”

Krishna sadly bole,"""
        create_image_text_layout(
            "attached_assets/chapter10/10.39.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        “Hamare innocent parents Vasudeva aur Devakī ne mere liye bahut suffering endure ki hai.”

“Unke children tak ko Kaṃsa ne maar diya.”

Fir Krishna ne gently poocha,

“Please batayiye aap kis purpose se yahan aaye hain?”

Tab Akrūra ne Kaṃsa ka full evil plan explain kiya.

Unhone bataya ki Kaṃsa Krishna-Balarāma ko Mathurā bulaakar wrestlers aur elephant ke through kill karna chahta hai.

Krishna aur Balarāma yeh sunkar bas smile karne lage.

Fir Nanda Baba ne sab cowherds ko announce kar diya,

“Kal hum Mathurā jaayenge aur king ko milk products aur gifts tribute mein denge.”

Yeh news sunte hi Gopīs ka heart toot gaya.

Krishna unki very life the, aur ab woh Vraja chhodkar jaane wale the.

Kuch Gopīs grief mein itni disturbed ho gayin ki unke clothes loose ho gaye aur hair dishevelled ho gaya.

Kuch toh Krishna ke thoughts mein itni absorbed ho gayin ki unhe outside world ka hosh hi nahi raha.

Sab Gopīs groups mein milkar tears ke saath complain karne lagi.

Woh sadly boli,

“O Creator! Tum kitne cruel ho.”

“Pehle tum loving people ko milate ho, fir bina reason unhe separate kar dete ho.”

Ek Gopī emotional hokar boli,

“Tumne hume Krishna ka beautiful smiling face dikhaya… aur ab usse humse cheen rahe ho.”

Dusri Gopī angrily boli,

“Akrūra ka naam actually galat hai.”

“Woh ‘not cruel’ nahi, bahut cruel hai. Woh humari life hi humse le ja raha hai.”

Fir woh Mathurā ki women ko imagine karne lagi.

“Mathurā ki ladies kitni fortunate hongi.”

“Woh Krishna ka sweet smiling face aur loving side-glances dekh paayengi.”

Ek Gopī fearfully boli,

“Krishna new people aur new company ko easily love karte hain.”

“Mathurā ki refined ladies unhe apni sweet talks aur shy smiles se attract kar lengi.”

“Fir woh hum simple village girls ko yaad bhi karenge?”

Woh crying voice mein boli,

“Humne Krishna ke liye homes, relatives aur husbands tak chhod diye…”

“Ab woh hume abandon karke ja rahe hain.”

Morning hote hi Akrūra ne chariot ready kar diya.

Krishna aur Balarāma comfortably us par baith gaye.

Cowherds bhi bullock carts mein unke piche chalne lage.

Gopīs desperately Krishna ke piche bhaagne lagi.

Krishna baar baar lovingly mudkar unki taraf dekh rahe the.

Unka affectionate glance dekhkar Gopīs ko thodi hope mili.

Krishna ne secretly ek messenger ke through promise bheja,

“Main jaldi wapas aaunga.”

Fir bhi Gopīs motionless khadi rahi.

Jab tak chariot ka flag aur dust visible tha, woh painted statues ki tarah bas Krishna ko dekhti rahi.

Finally jab Krishna completely out of sight ho gaye, tab woh hopeless aur heartbroken condition mein Vraja wapas laut gayin.

Apna sorrow kam karne ke liye woh continuously Krishna ki glories aur pastimes gaane lagi.

🌊 Akrūra Sees Krishna’s Divine Form

Krishna, Balarāma aur Akrūra noon tak Yamunā river ke paas pahuche.

Krishna aur Balarāma nearby grove mein rest karne lage, jabki Akrūra Yamunā mein bath karne gaye.

Jab Akrūra sacred mantras chant karte hue water mein dip liya, tab unhone amazing vision dekha.

Unhone Krishna aur Balarāma ko water ke andar divine form mein dekha.

Shock mein woh immediately water se bahar aaye aur chariot ki taraf dekha.

Krishna-Balarāma toh wahan pehle ki tarah peacefully baithe the!

Confused Akrūra dubara river mein gaye.

Is baar unhone thousand-headed Śeṣa Nāga ko dekha.

Uske coils par Lord Viṣṇu divine form mein seated the.

Unka complexion dark rain-cloud jaisa tha aur woh yellow silk garments pehne hue the.

Unke four hands mein conch, discus, mace aur lotus shine kar rahe the.

Kaustubha jewel aur Śrīvatsa mark unke chest par glow kar rahe the.

Brahmā, Śiva, Nārada, Prahlāda aur many sages unki praise kar rahe the.

Lakṣmī aur many divine goddesses bhi unki service kar rahi thi.

Yeh divine vision dekhkar Akrūra devotion aur joy se completely overwhelmed ho gaye.

Unki eyes tears se fill ho gayin aur folded hands ke saath woh Lord ki prayers karne lage."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 40
    with st.expander("Chapter 40 - Akrūra’s Hymn (in praise of the Lord)"):
        text1 = """ 
        🙏 Akrūra’s Divine Prayer to Krishna

Śrī Śuka ne kaha,

Yamunā ke water mein Krishna ka divine form dekhkar Akrūra ka heart pure joy aur devotion se bhar gaya.

Unki eyes tears se fill ho gayin aur folded hands ke saath woh Lord ki prayer karne lage.

Akrūra बोले,

“O Lord Krishna, main aapko bow karta hoon.”"""
        create_image_text_layout(
            "attached_assets/chapter10/10.40.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        “Aap hi sab causes ke ultimate cause ho.”

“Aap hi Nārāyaṇa ho, jo sabke hearts mein present ho.”

“Aapke navel se lotus nikla, aur us lotus se Brahmā appeared, jisne universe create kiya.”

Fir Akrūra ne kaha,

“Earth, water, fire, air, sky, mind, senses aur sab gods — yeh sab aapse hi originate hue hain.”

“Aap hi sabke source ho.”

Woh respectfully bole,

“Even Brahmā aur great gods bhi aapki real divine nature ko fully understand nahi kar paate.”

“Kyuki aap material qualities se completely beyond ho.”

Fir Akrūra different spiritual paths explain karne lage.

“Kuch people sacrifices aur Vedic rituals ke through aapki worship karte hain.”

“Kuch meditation aur spiritual knowledge ke through.”

“Kuch aapko Nārāyaṇa form mein worship karte hain, aur kuch Śiva form mein.”

“Lekin sab paths ultimately aap tak hi pahunchte hain.”

Akrūra ne beautiful example diya,

“Jaise sab rivers finally ocean mein mil jaati hain, waise hi sab worship aur devotion aap tak hi aati hai.”

Fir woh Krishna ke universal form ko describe karne lage.

“Fire aapka mouth hai.”

“Earth aapke feet hai.”

“Sun aapki eyes hai.”

“Oceans aapka belly hain aur mountains aapki bones.”

“Poora universe aapke divine body mein exist karta hai.”

Akrūra lovingly बोले,

“Lord, jab bhi aap different incarnations lete ho, aap duniya ka sorrow remove karte ho.”

Fir woh Krishna ke many avatāras ko bow karne lage.

“Main Matsya avatār ko bow karta hoon.”

“Kurma, Varāha aur Narasiṁha ko bow karta hoon.”

“Vāmana, Paraśurāma aur Lord Rāma ko bow karta hoon.”

“Buddha aur future Kalki avatār ko bhi bow karta hoon.”

Fir Akrūra emotional hokar बोले,

“Lord, māyā ki wajah se duniya ‘me’ aur ‘mine’ mein trapped hai.”

“Log temporary things ko permanent samajhte hain.”

“Main bhi foolishly body, family, wealth aur house mein attached raha.”

Woh sadly बोले,

“Jaise koi mirage ko real water samajhkar uske piche bhaagta hai, waise hi main bhi unreal things ke piche bhaagta raha.”

“My uncontrolled senses mujhe idhar-udhar kheenchti rahi.”

Fir Akrūra full surrender ke saath बोले,

“O Krishna! Aaj main aapke lotus-feet ki shelter mein aaya hoon.”

“Saintly devotees ki association se hi aapke feet mein attachment develop hota hai.”

“Aap hi pure consciousness aur all knowledge ke source ho.”

“Please mujhe protect karo.”

“Main completely aapki shelter mein hoon.”"""
        create_image_text_layout(text_content=text2, layout="full")
        
        
        # Chapter 41
    with st.expander("Chapter 41 - Kṛṣṇa’s Arrival at Mathurā"):
        text1 = """ 
        🏙️ Krishna Arrives at Mathurā

Śrī Śuka continued,

Akrūra ko divine vision dikhane ke baad Lord Krishna ne apna Viṣṇu form suddenly withdraw kar liya — bilkul ek actor ki tarah jo role finish karke stage se disappear ho jaata hai.

Akrūra amazed aur emotional state mein water se bahar aaye.

Krishna smilingly unse poochne lage,"""
        create_image_text_layout(
            "attached_assets/chapter10/10.41.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        “Kya tumne land, sky ya water mein koi wonderful thing dekhi?”

Akrūra folded hands ke saath बोले,

“Lord, poori universe ke saare wonders aapke andar hi exist karte hain.”

“Jisne aapko directly dekh liya, uske liye aur kya miracle baaki reh sakta hai?”

Fir Akrūra Krishna aur Balarāma ko chariot mein lekar evening tak Mathurā city ke paas le aaye.

Road ke side gathered villagers Krishna-Balarāma ko dekhkar mesmerized ho gaye.

Koi bhi unse apni eyes hata nahi paa raha tha.

Meanwhile Nanda aur Vraja ke cowherds already city ke nearby park mein wait kar rahe the.

Krishna lovingly Akrūra ka hand pakadkar बोले,

“Tum pehle city chale jao.”

“Hum thodi der rest karke baad mein Mathurā enter karenge.”

Lekin devoted Akrūra emotional hokar बोले,

“Main aap dono ko yahan chhodkar city nahi ja sakta.”

“Please mere ghar ko apne lotus feet se sanctify kijiye.”

“Jinke feet wash karne se Bali ko glory aur liberation mili, unhi divine feet ki dust mere home ko bless kare.”

Krishna kindly बोले,

“Pehle main Kaṁsa ko defeat karunga.”

“Uske baad main definitely tumhare ghar aaunga.”

Akrūra slightly disappointed hokar city chale gaye.

🌸 The Beauty of Mathurā

Next day Krishna aur Balarāma cowherd boys ke saath Mathurā city enter karne lage.

Mathurā dazzling beauty se filled thi.

Huge crystal gateways, golden doors, decorated mansions aur deep moats city ko magnificent bana rahe the.

Roads water aur flowers se sprinkled the.

Har ghar festive decorations, lamps, banana trees aur colorful flags se decorated tha.

Jaise hi city women ne Krishna aur Balarāma ke arrival ki news suni, sab excited hokar gharon se bahar daudne lagi.

Koi ek hi earring pehenkar aa gayi.

Koi ek eye mein hi collyrium laga paayi.

Koi half meal chhodkar bhaagi.

Koi babies ko feed karte hue hi terrace par daud gayi.

Sab Krishna ko directly dekhna chahti thi.

Krishna royal elephant jaisi majestic walk karte hue city mein move kar rahe the.

Unke smiles aur glances sabke hearts capture kar rahe the.

Mathurā women mentally unhe apne hearts mein embrace karne lagi.

Terraces se flowers rain hone lage.

Brāhmaṇas joyfully sandal paste, garlands aur gifts se Krishna-Balarāma ka worship karne lage.

Women ek dusre se lovingly boli,

“Vraja ki gopīs ne zaroor extraordinary austerities ki hongi…”

“Tabhi unhe daily Krishna aur Balarāma ko dekhne ka fortune mila hai.”

👕 Krishna Punishes the Washerman

Road par Krishna ne ek royal washerman ko dekha jo Kaṁsa ke expensive clothes carry kar raha tha.

Krishna smilingly बोले,

“Hume kuch beautiful clothes de do.”

“Tumhe great prosperity milegi.”

Lekin arrogant washerman angrily insult karne laga.

“Tum jungle-dwellers royal clothes pehenne layak nahi ho!”

“King ke servants tum jaise insolent logon ko punish karte hain.”

Yeh rude words sunkar Krishna slightly angry ho gaye.

Unhone sirf fingertips se us washerman ka head body se separate kar diya.

Baaki servants fear mein clothes chhodkar bhaag gaye.

Krishna aur Balarāma ne apne favorite garments pehne aur remaining clothes cowherd boys ko de diye.

🧵 The Weaver and Florist Sudāmā

Uske baad ek humble weaver Krishna-Balarāma ke paas aaya aur lovingly unhe colorful royal garments pehnaye.

Beautiful dress aur ornaments mein Krishna aur Balarāma festival elephants ki tarah radiant lag rahe the.

Krishna pleased hokar weaver ko blessings diye — wealth, strength, memory aur future liberation tak ka boon diya.

Fir dono brothers florist Sudāmā ke house pahuche.

Sudāmā immediately ground par bow hokar unka welcome karne laga.

Usne garlands, sandal paste aur hospitality offer ki.

Emotionally woh bola,

“Aaj meri life successful ho gayi.”

“Aap dono poori universe ke soul aur protectors ho.”

“Please mujhe command dijiye ki main aapki kya service kar sakta hoon.”

Sudāmā ne specially fragrant flower garlands Krishna aur Balarāma ko dedicate kiye.

Lord dono brothers usse extremely pleased hue.

Sudāmā ne sirf teen cheezein maangi:

“Unwavering devotion…”

“Devotees ke saath friendship…”

“Aur sab beings ke prati compassion.”

Krishna ne happily usse blessings, prosperity, long life aur glory grant ki — aur fir Balarāma ke saath city mein aage badh gaye."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 42
    with st.expander("Chapter 42 - Description of the Wrestling Arena"):
        text1 = """ 
        🌺 Krishna Meets Kubjā in Mathurā

Śrī Śuka continued,

Royal road par chalte hue Krishna ne ek young woman ko dekha jo sandal paste aur perfumes ka vessel carry kar rahi thi.

Uska body three places par bent tha, isliye uska naam Tri-vakrā (Kubjā) tha.

Krishna smilingly usse bole,"""
        create_image_text_layout(
            "attached_assets/chapter10/10.42.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        “O beautiful lady, tum kaun ho?”

“Yeh fragrant sandal paste kis ke liye hai?”

“Hume bhi thoda sandal paste do.”

“Tum bahut blessed ho jaogi.”

Kubjā shyly boli,

“Main King Kaṁsa ki maidservant hoon.”

“Main special ointments aur perfumes prepare karti hoon jo king ko bahut pasand hain.”

“Lekin honestly… aapse zyada koi in fragrances ka worthy nahi hai.”

Krishna aur Balarāma ki beauty, smiles aur loving glances dekhkar Kubjā ka heart completely melt ho gaya.

Usne lovingly dono brothers ko sandal paste se anoint kar diya.

Sandal paste lagne ke baad Krishna aur Balarāma aur bhi radiant lagne lage.

Krishna Kubjā ki devotion se pleased ho gaye.

Unhone decide kiya ki woh uska crooked body straight karenge — taaki duniya ko dikhe ki Lord ka darśan kya fruit deta hai.

Krishna ne gently apne feet se uske feet press kiye aur do fingers se uska chin lift kiya.

Instantly miracle ho gaya.

Kubjā ka bent body perfectly straight aur beautiful ho gaya.

Woh suddenly extraordinarily gorgeous young woman ban gayi.

Krishna ke touch se uske heart mein deep love awaken ho gaya.

Woh smilingly Krishna ka cloth pakadkar boli,

“O hero, please mere ghar chaliye.”

“Main aapke bina nahi reh sakti.”

Krishna loudly laugh karne lage aur teasing tone mein बोले,

“Kaṁsa ko defeat karne ke baad main definitely tumhare ghar aaunga.”

“Tum toh homeless travelers jaise hum logon ka only shelter ho.”

Sweet words sunkar Kubjā blissfully unhe dekhte reh gayi.

🏹 Krishna Breaks the Great Bow

Krishna aur Balarāma market streets se aage badhe.

Merchants unhe gifts, perfumes, pearl garlands aur betel leaves offer karne lage.

Mathurā ki women unki beauty dekhkar itni overwhelmed ho gayin ki kuch motionless khadi reh gayin — bilkul painted pictures ki tarah.

Fir Krishna ne people se Bow-Sacrifice arena ka direction poocha aur wahan enter kiya.

Andar ek gigantic jeweled bow rakha hua tha — rainbow ki tarah shining.

Bahut saare armed guards usse protect kar rahe the.

Guards ne Krishna ko rokne ki try ki, lekin Krishna casually aage badh gaye.

Unhone sportively sirf left hand se giant bow utha liya.

Fir uski string chadha kar usse full stretch kiya…

CRACK!!!

Krishna ne us massive bow ko instantly do pieces mein tod diya.

Sound itna loud tha ki sky aur all directions vibrate karne lage.

Mathurā ke log shock mein reh gaye.

Kaṁsa ne jab yeh sound suna, woh terror se freeze ho gaya.

Guards rage mein chillane lage,

“Pakdo unhe! Bind them!”

Lekin Krishna aur Balarāma angry ho gaye.

Unhone broken bow ke pieces ko hi weapons bana liya aur soldiers ko defeat kar diya.

Entire battalion destroy ho gaya.

Citizens Krishna-Balarāma ki fearless power aur beauty dekhkar unhe divine beings samajhne lage.

Evening tak dono brothers city roam karte rahe aur finally cowherd camp mein wapas aa gaye.

😨 Kaṁsa’s Terrifying Omens

Krishna ke heroic acts ki reports sunkar Kaṁsa panic aur fear se bhar gaya.

Usse neend hi nahi aa rahi thi.

Usne terrifying death omens dekhne start kiye.

Kabhi mirror mein apna reflection dekhta toh head missing lagta.

Kabhi ek lamp ke do-do reflections dikhte.

Kabhi apne shadow mein holes nazar aate.

Kabhi footsteps hi visible nahi hote.

Dreams mein woh dead logon ko hug karta hua dikhta.

Kabhi donkey ride karta hua.

Kabhi poison peeta hua.

Kabhi naked aur oil-smeared wandering karta hua.

Kaṁsa fully terrified ho gaya.

Woh poori raat death fear mein jagta raha.

🏟️ The Wrestling Arena is Prepared

Morning hote hi Kaṁsa ne grand wrestling festival organize karne ka order diya.

Arena garlands, flags aur decorations se beautifully decorate kiya gaya.

Trumpets aur drums loudly bajne lage.

Citizens, Brāhmaṇas, princes aur kings apni-apni seats par baith gaye.

Kaṁsa royal throne par baitha tha — lekin andar se anxiety aur fear uska heart torture kar rahe the.

Great wrestlers bhi arena mein aa gaye:

Cāṇūra, Muṣṭika, Kūṭa, Śala aur Tośala.

Meanwhile Nanda aur Vraja ke cowherds bhi invited guests ki tarah alag platform par baith gaye.

Sabko wait tha us moment ka…

jab Krishna aur Balarāma arena mein enter karenge."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 43
    with st.expander("Chapter 43 - Killing of the elephant Kuvalayāpīḍa"):
        text1 = """ 
        🐘 Krishna Kills the Elephant Kuvalayāpīḍa

Śrī Śuka continued,

Next morning Krishna aur Balarāma ne bath aur morning rituals complete kiye.

Wrestling arena se drums, trumpets aur cheering ki loud sounds aa rahi thi.

Dono brothers excitedly tournament dekhne ke liye nikle."""
        create_image_text_layout(
            "attached_assets/chapter10/10.43.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Arena ke entrance par ek gigantic terrifying elephant khada tha — Kuvalayāpīḍa.

Kaṁsa ne specially us elephant ko Krishna ko kill karne ke liye wahan station kiya tha.

Krishna calmly ready hue.

Unhone apna waist-cloth tight kiya aur curly hair ko upper garment se baandh liya.

Fir thunder-like voice mein elephant driver se बोले,

“Side ho jao.”

“Hume passage do.”

“Nahi toh main tumhe aur tumhare elephant dono ko Yama ke paas bhej dunga.”

Driver rage mein aa gaya aur usne elephant ko Krishna par charge kar diya.

Huge elephant furiously Krishna ki taraf dauda aur trunk se unhe pakad liya.

Lekin Krishna instantly uski grip se slip hokar uske legs ke beech disappear ho gaye.

Elephant confused ho gaya.

Smell se Krishna ko locate karne ki try karne laga.

Tab Krishna ne suddenly elephant ki tail pakad li aur us giant beast ko easily drag karne lage — bilkul Garuḍa snake ko kheenchta hai waise.

Kabhi elephant right turn leta, toh Krishna usse opposite side ghuma dete.

Kabhi left turn leta, toh Krishna usse spin kar dete.

Scene bilkul aisa lag raha tha jaise koi boy calf ke saath play kar raha ho.

Fir Krishna directly elephant ke saamne aaye aur powerful punch maara.

Elephant repeatedly Krishna ko crush karne ki try karta raha, lekin Krishna lightning speed se dodge karte rahe.

Ek moment par Krishna playful way mein ground par girte hue dikhe.

Infuriated elephant ne socha Krishna neeche hi hain aur apne tusks se earth ko pierce kar diya.

Lekin Krishna already side mein jump kar chuke the.

Finally Krishna directly charging elephant ki taraf daude.

Unhone uski trunk pakadkar poore elephant ko ground par slam kar diya.

Fir lion ki tarah uske body par foot rakhkar ek tusk forcibly nikaal liya.

Usi tusk se Krishna ne elephant aur uske drivers ko kill kar diya.

Blood aur ichor se stained body, shoulder par giant tusk aur lotus-like smiling face ke saath Krishna unbelievably heroic lag rahe the.

Balarāma aur cowherd boys ke saath Krishna arena mein enter hue.

🏟️ Krishna Enters the Arena

Jab Krishna arena mein enter hue, har group ne unhe different way se perceive kiya.

Wrestlers ko woh thunderbolt jaise lage.

Ordinary men ko superhuman hero lage.

Women ko Cupid incarnate lage.

Cowherds ko beloved relative lage.

Parents ko innocent child lage.

Yogīs ko Supreme Brahman dikhe.

Aur Kaṁsa ko…

khud Death nazar aaye.

Kaṁsa ka fear aur bhi intense ho gaya.

Meanwhile Mathurā ke citizens Krishna-Balarāma ko fascinated hokar dekh rahe the.

Unki beauty aur heroism ko dekhkar log ek dusre se stories discuss karne lage.

“Kṛṣṇa ne Pūtanā ko maara…”

“He subdued Kāliya serpent…”

“He lifted Govardhana mountain for seven days…”

“He protected Vraja from Indra’s storm…”

“Kṛṣṇa aur Balarāma definitely divine beings hain!”

Sabke hearts devotion aur wonder se fill ho gaye.

🤼 Cāṇūra Challenges Krishna

Trumpets ke loud sounds ke beech giant wrestler Cāṇūra arena mein aaya.

Woh Krishna aur Balarāma se बोला,

“O Krishna, O Balarāma! King Kaṁsa ne specially aap dono ko wrestling dekhne ke liye invite kiya hai.”

“Subjects ko king ki wishes obey karni chahiye.”

“Hume pata hai ki aap dono wrestling aur combat mein experts ho.”

Krishna politely बोले,

“Hum forest cowherd boys hain.”

“Hume apne equal strength walon ke saath wrestle karna chahiye.”

“Fair match hi proper dharma hai.”

Lekin Cāṇūra loudly laugh karke बोला,

“Tum ordinary boys nahi ho!”

“Tumne thousand elephants jitni strength wale elephant ko sport ki tarah kill kiya hai.”

“Isliye koi injustice nahi hai.”

“Krishna, tum mere saath wrestle karoge…”

“Aur Balarāma Muṣṭika ke saath.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 44
    with st.expander("Chapter 44 - Slaying of Kaṃsa"):
        text1 = """ 
        🤼 Krishna and Balarāma Enter the Wrestling Match

Śrī Śuka continued,

Cāṇūra aur Muṣṭika ke challenge accept karne ke baad Krishna ne firmly Cāṇūra ko pakad liya, aur Balarāma Muṣṭika ki taraf badhe.

Dono sides victory ke liye determined the.

Wrestlers ek dusre ke hands, legs aur shoulders lock karke violently pull aur push karne lage.

Kabhi fists se strike karte…

kabhi knees se…

kabhi heads aur chests se collide hote.

Kabhi ek dusre ko whirl karte, kabhi ground par slam karte, kabhi tightly crush karne ki try karte.

Entire arena thunderous combat se vibrate hone laga."""
        create_image_text_layout(
            "attached_assets/chapter10/10.44.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        😢 Women of Mathurā Protest

Arena mein present women yeh unequal fight dekhkar deeply disturbed ho gayin.

Woh groups mein discuss karne lagi,

“Yeh totally unfair hai!”

“Yeh wrestlers mountain jaise giant aur powerful hain…”

“Aur Krishna-Balarāma toh abhi delicate young boys lagte hain.”

“Such injustice ko tolerate karna bhi sin hai.”

Fir women Krishna ki beauty aur Vraja life ko lovingly remember karne lagi.

“Kya blessed land hogi Vraja…”

“Jahan Lord Krishna wild flower garlands pehenkar flute bajate hue cows graze karte hain.”

“Gopīs ne zaroor unimaginable tapasya ki hogi…”

“Tabhi woh har roz Krishna ke smiling lotus-face ko dekh paati hain.”

Women emotionally Vraja women ki devotion glorify karne lagi:

“Woh milking, churning, sweeping aur lullabies gaate hue bhi Krishna ka naam gaati rehti hain.”

“Unka heart completely Krishna mein absorbed rehta hai.”

Meanwhile Devakī aur Vasudeva bhi fearful ho gaye.

Unhe abhi tak Krishna-Balarāma ki divine strength ka full realization nahi tha.

Par Krishna ne decide kar liya tha — ab evil wrestlers ka end hona hi hai.

💥 Krishna Kills Cāṇūra

Fight aur intense ho gayi.

Cāṇūra repeatedly Krishna par thunderbolt-like punches aur attacks use kar raha tha.

Ek moment par woh hawk ki speed se jump karke dono fists Krishna ke chest par de maarta hai.

Lekin Krishna ek inch bhi move nahi hue.

Bilkul elephant par flower-garland strike karne jaisa effect hua.

Fir Krishna ne suddenly Cāṇūra ke dono arms pakad liye.

Unhone us giant wrestler ko rapidly spin karna start kar diya.

Speed itni terrifying thi ki Cāṇūra ki life-force hi extinguish hone lagi.

Finally Krishna ne usse violently ground par smash kar diya.

Uske ornaments scatter ho gaye, hair dishevelled ho gaya, aur woh dead pad gaya — bilkul broken flagstaff ki tarah.

💪 Balarāma Defeats Muṣṭika

Same time Balarāma aur Muṣṭika ka battle bhi raging tha.

Muṣṭika ne powerful punch maara, lekin Balarāma ne usse violent palm-strike diya.

Muṣṭika internally crushed feel karne laga.

Woh blood vomit karta hua storm se uprooted tree ki tarah gir gaya — dead.

Uske baad Balarāma ne casually left fist se Kūṭa ko kill kar diya.

Krishna ne Śala aur Tośalaka ko kicks se instantly finish kar diya.

Remaining wrestlers fear se arena se bhaag gaye.

🎉 Arena Rejoices

Krishna aur Balarāma happily apne cowherd friends ko arena mein le aaye.

Trumpets aur drums loudly bajne lage.

Dono brothers dancing aur sporting karne lage, unke anklets sweetly jingle kar rahe the.

Entire audience except Kaṁsa joy se bhar gayi.

Brāhmaṇas loudly cheer karne lage:

“Excellent!”

“Bravo!”

Lekin Kaṁsa rage aur terror se explode ho gaya.

Usne angrily orders dene start kiye:

“Krishna aur Balarāma ko city se nikaalo!”

“Cowherds ki wealth confiscate karo!”

“Nanda ko arrest karo!”

“Vasudeva aur Ugrasena ko immediately kill kar do!”

👑 Krishna Slays Kaṁsa

Kaṁsa ke cruel orders sunkar Krishna furious ho gaye.

Woh lightning speed se royal platform ki taraf leap kar gaye.

Kaṁsa ne Krishna ko approaching Death ki tarah dekha.

Woh instantly sword aur shield lekar defensive stance mein aa gaya.

Lekin Krishna unstoppable the.

Garuḍa snake ko pakadta hai waise Krishna ne Kaṁsa ko firmly seize kar liya.

Unhone uska crown gira diya aur hair se pakadkar usse high throne se neeche arena floor par throw kar diya.

Fir Lord Krishna — universe ke support aur Supreme Viṣṇu — directly uske upar jump kar gaye.

Us impact se Kaṁsa ki life instantly leave ho gayi.

Entire arena screams aur shock se bhar gaya.

Krishna ne dead Kaṁsa ko lion ki tarah ground par drag kiya.

🌸 Kaṁsa’s Liberation

Śrī Śuka explained,

Kaṁsa continuously Krishna ke fear mein jeeta tha.

Eating, sleeping, walking — har moment woh Krishna ko remember karta rehta tha.

Isliye death ke baad bhi usse rare spiritual liberation mila.

⚔️ Kaṁsa’s Brothers are Killed

Kaṁsa ke eight brothers revenge lene ke liye attack karne lage.

Lekin Balarāma ne elephant tusk ko club ki tarah use karke sabko lion ki tarah destroy kar diya.

Sky mein heavenly drums bajne lage.

Brahmā, Śiva aur gods flowers rain karne lage.

Celestial women dance karne lagi.

😭 Kaṁsa’s Queens Lament

Kaṁsa aur uske brothers ki widows crying condition mein arena mein aayi.

Woh apne husbands ke bodies ko hug karke loudly lament karne lagi.

“Mathurā ab joyless ho gayi…”

“Cruelty toward innocents hi tumhari downfall ka cause bani…”

“Koi bhi Krishna ke against jaakar happy nahi reh sakta.”

🙏 Krishna Meets His Parents

Krishna ne royal women ko console kiya aur proper funeral rites perform karvaye.

Uske baad Krishna aur Balarāma jail mein gaye aur Devakī-Vasudeva ko chains se free kar diya.

Dono brothers ne deeply respectfully unke feet touch kiye.

Lekin Devakī aur Vasudeva fully realize kar chuke the ki unke sons actually Supreme Lords hain.

Is divine awe aur reverence ki wajah se woh initially Krishna-Balarāma ko normal parents ki tarah hug bhi nahi kar paaye."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 45
    with st.expander("Chapter 45 - Restoration of Preceptor Sāndīpani’s son"):
        text1 = """ 
        👨‍👩‍👦 Krishna Comforts His Parents

Śrī Śuka continued,

Devakī aur Vasudeva ko Krishna-Balarāma ki divine nature realize ho chuki thi.

Unke heart mein parental affection ki jagah awe aur reverence aa gaya tha.

Yeh dekhkar Lord Krishna ne apni Yogamāyā use ki — taaki unke parents phir naturally unse apne children ki tarah love kar sakein.

Fir Krishna aur Balarāma great humility ke saath unke paas gaye aur respectfully बोले,

“O Mother… O Father…”"""
        create_image_text_layout(
            "attached_assets/chapter10/10.45.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Krishna emotional tone mein बोले,

“Unfortunately hum aapko apna infancy aur childhood enjoy nahi kara paaye.”

“Hum aapke paas rehkar parental affection receive nahi kar sake.”

“Parents ka debt toh hundred years mein bhi repay nahi ho sakta.”

“Jo son capable hoke bhi parents ki service nahi karta, woh spiritually dead jaisa hai.”

“Kaṁsa ke terror ki wajah se hum aapki properly service nahi kar paaye.”

“Please hume forgive kijiye.”

Krishna ke sweet humble words sunkar Devakī aur Vasudeva ka heart melt ho gaya.

Woh Krishna aur Balarāma ko lap mein lekar tightly embrace karne lage.

Unki eyes tears se fill ho gayin aur emotion ki wajah se woh properly speak bhi nahi kar pa rahe the.

👑 Ugrasena Becomes King Again

Parents ko comfort karne ke baad Krishna ne apne maternal grandfather Ugrasena ko Yadus ka king bana diya.

Krishna respectfully बोले,

“O great king, please hum sabko rule kijiye.”

“Yadu dynasty par ancient curse hai, isliye hum throne occupy nahi karenge.”

“Jab main aapka servant bankar stand karta hoon, toh even gods bhi aapko honour karenge.”

Fir Krishna ne Kaṁsa ke fear se exile hue Yadus, Vṛṣṇis, Andhakas aur other relatives ko wapas bulaaya.

Unhe homes, wealth aur security provide ki.

Entire Mathurā Krishna-Balarāma ki protection mein joyful aur prosperous ho gayi.

Log daily Krishna ke smiling lotus-face ko dekhkar bliss feel karte the.

Even old people rejuvenated aur energetic feel karne lage.

🐄 Krishna Says Goodbye to Nanda

Uske baad Krishna aur Balarāma Nanda Bābā ke paas gaye.

Unhone lovingly Nanda ko embrace karke कहा,

“O Father, aap aur Mother Yaśodā ne hume unimaginable love diya.”

“True parents wahi hote hain jo abandoned children ko bhi apne own kids ki tarah nourish karein.”

“Ab aap Vraja wapas jaiye.”

“Hum Mathurā mein relatives aur kingdom ka welfare settle karke soon aapse milne aayenge.”

Nanda deeply emotional ho gaye.

Eyes tears se filled thi jab unhone Krishna-Balarāma ko hug kiya.

Fir Vraja ke cowherds sadly wapas chale gaye.

🎓 Sacred Thread Ceremony

Vasudeva ne proper Vedic rituals ke saath Krishna aur Balarāma ka sacred-thread ceremony perform karvaya.

Family priest Garga aur many Brāhmaṇas invite kiye gaye.

Huge charity bhi di gayi:

Golden ornaments aur silk-cloth se decorated cows Brāhmaṇas ko gift ki gayin.

Krishna aur Balarāma officially brahmacārī students ban gaye.

📚 Krishna and Balarāma Study Under Sāndīpani

Though Krishna aur Balarāma omniscient the, phir bhi unhone ordinary students ki tarah behave kiya — taaki duniya ko ideal conduct sikhaya ja sake.

Dono brothers Avantī city mein sage Sāndīpani ke gurukul gaye.

Wahan unhone perfect humility aur devotion ke saath guru ki service ki.

Sāndīpani extremely pleased hue aur unhe Vedas, Upaniṣads, military science, law, logic aur politics sab sikhaya.

Amazing baat yeh thi:

Jo bhi lesson guru ek baar bolte, Krishna-Balarāma instantly master kar lete.

Sirf sixty-four days aur nights mein dono ne sixty-four arts aur sciences complete kar liye.

🌊 Guru Dakṣiṇā — Restoring the Guru’s Son

Education complete hone ke baad Krishna aur Balarāma ne respectfully poocha,

“Guruji, aap kya guru-dakṣiṇā chahte hain?”

Sāndīpani aur unki wife ne consult karke ek heartbreaking request rakhi.

“Hamāra son ocean mein Prabhāsa ke paas mar gaya tha…”

“Agar possible ho, usse wapas le aao.”

Krishna aur Balarāma immediately बोले,

“So be it.”

Dono chariot mein Prabhāsa ocean ke shore par gaye.

Ocean deity personally aakar unka worship karne laga.

Krishna ne directly poocha,

“Hamāre guru ka son hume return karo.”

Ocean deity respectfully bola,

“Main responsible nahi hoon.”

“Pañcajana naam ka demon conch-form mein waters mein rehta hai.”

“Usne shayad boy ko carry away kiya.”

Krishna instantly ocean mein dive kar gaye.

Unhone Pañcajana demon ko kill kiya, lekin boy uske body mein nahi mila.

Krishna us demon ke conch-shell ko lekar wapas aaye — jo later famous Pāñcajanya conch bana.

Fir Krishna aur Balarāma Yama’s city Saṁyamanī gaye aur conch loudly blow kiya.

Yama himself deep devotion ke saath unka worship karne laga.

Krishna बोले,

“Hamāre guru ka son yahan ho toh immediately le aao.”

Yama instantly obey kar gaya.

Guru ka dead son alive form mein Krishna-Balarāma ko return kar diya gaya.

Dono brothers us boy ko wapas Sāndīpani ke paas le aaye.

Guru overwhelmed ho gaye.

Woh बोले,

“O Krishna, tumne perfect guru-dakṣiṇā de di.”

“Ab mujhe aur kuch nahi chahiye.”

“Tumhari glory poori world ko purify kare.”

Blessings lekar Krishna aur Balarāma wind-speed chariot mein Mathurā wapas aa gaye.

Unhe dekhkar citizens utne hi joyful hue jitna lost treasure recover hone par log hote hain."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 46
    with st.expander("Chapter 46 - Uddhava deputed for consoling Nanda"):
        text1 = """ 
        💛 Kṛṣṇa Sends Uddhava to Vraja

Śrī Śuka narrated,

Uddhava Vṛṣṇis ka foremost counselor tha aur Lord Kṛṣṇa ka extremely beloved friend bhi.

Woh Bṛhaspati ka direct disciple tha aur extraordinary intelligence rakhta tha.

Ek din Kṛṣṇa ne lovingly Uddhava ka hand pakadkar usse kaha:

“O gentle Uddhava, please Vraja jao.”

“Mere parents — Nanda aur Yaśodā — ko meri message dekar comfort karo.”

“Aur Gopīs jo separation mein suffering kar rahi hain, unhe bhi console karo.”"""
        create_image_text_layout(
            "attached_assets/chapter10/10.46.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        🌸 Kṛṣṇa Describes the Love of the Gopīs

Kṛṣṇa deeply emotional hokar बोले:

“Gopīs ne apna heart aur soul completely mujhe dedicate kar diya hai.”

“Mere liye unhone husbands, sons aur even bodily comforts tak abandon kar diye.”

“They think only of me.”

“Main un logon ko always support karta hoon jo everything sacrifice karke sirf mujhe love karte hain.”

“Mere distant hone ki wajah se woh constant grief aur longing mein live kar rahi hain.”

“Sirf meri return ki hope unhe somehow alive rakhi hui hai.”

🚩 Uddhava Arrives in Gokula

Kṛṣṇa ka sacred message receive karke Uddhava immediately chariot par Vraja ke liye depart hua.

Sunset ke time woh Nanda’s Gokula pahunch gaya.

Entire Vraja beautiful pastoral life se filled tha:

cows returning home
dust clouds rising from hoofs
bulls roaring
calves joyfully jumping
flute music echoing everywhere

🌿 Evening Beauty of Vraja

Gokula heavenly beauty se shine kar raha tha.

Gopīs aur Gopas songs mein Kṛṣṇa aur Balarāma ke exploits glorify kar rahe the.

Everywhere:

lamps glowing
incense burning
sacred worship happening
blossoming groves
humming bees
lotus ponds with swans

Vraja divine paradise jaisa lag raha tha.

🤗 Nanda Welcomes Uddhava

Uddhava ko dekhkar Nanda Mahārāja immense joy se fill ho gaye.

Unhone lovingly embrace karke honour diya — almost as if Kṛṣṇa himself aa gaya ho.

After hospitality aur rest, Nanda emotionally questions poochne lage.

😢 Nanda Remembers Kṛṣṇa

“Dear Uddhava,” Nanda बोले,

“Kya Vasudeva aur sab relatives well hain?”

“Kya Kṛṣṇa humein yaad karta hai?”

“Yaśodā ko…”

“Uske friends ko…”

“Vṛndāvana ko…”

“Govardhana ko…”

“Hamari cows ko…”

“Will he come back even once so that we can see his smiling face again?”

Nanda then remembered all dangers from which Kṛṣṇa had protected Vraja:

forest fire
storms
Kāliya serpent
Ariṣṭa demon
deadly accidents

“Kṛṣṇa ko yaad karte hi hamare actions ruk jaate hain.”

“Yamunā, forests aur playgrounds dekhkar hamara mind automatically usmein absorb ho jata hai.”

⚡ Nanda Realizes Kṛṣṇa’s Divinity

Nanda further बोले,

“Garga Muni ki prophecy mujhe yaad hai.”

“Mujhe lagta hai Balarāma aur Kṛṣṇa ordinary children nahi hain.”

“They seem like great divine beings descended for some cosmic mission.”

Fir unhone Kṛṣṇa’s impossible feats remember kiye:

Kaṃsa’s death
Cāṇūra and Muṣṭika’s destruction
Kuvalayāpīḍa elephant slain
Govardhana lifted for seven days
demons like Pralamba, Dhenuka, Ariṣṭa, Tṛṇāvarta, Baka killed effortlessly

😭 Yaśodā’s Tears

Kṛṣṇa ke childhood exploits sunte-sunte Nanda silent ho gaye, overwhelmed by longing and love.

Meanwhile Yaśodā tears se completely drenched ho gayi.

Maternal affection ki intensity se unke breasts se milk spontaneously flow hone laga.

🌌 Uddhava Reveals Kṛṣṇa’s Divine Nature

Nanda aur Yaśodā ki supreme devotion dekhkar Uddhava deeply moved ho gaya.

Woh बोले:

“O blessed ones, aap dono truly most fortunate beings ho.”

“Kṛṣṇa ordinary child nahi hai.”

“He is Nārāyaṇa himself — source of the universe.”

“Balarāma aur Kṛṣṇa are the primal cause of creation.”

“At death, jo even ek moment ke liye usmein mind fix karta hai, woh all karmas burn karke highest liberation attain karta hai.”

💫 Promise of Reunion

Uddhava lovingly assured them:

“Kṛṣṇa soon Vraja wapas aayega.”

“He will fulfil every promise he made after Kaṃsa’s death.”

“Please grief mein mat doobiye.”

“He eternally lives in the hearts of all beings.”

Fir Uddhava explained Kṛṣṇa’s transcendental nature:

no attachment
equal to all
beyond birth and karma
incarnates only for protecting righteousness

“He is not merely your son…”

“He is the soul, father, mother and essence of everything.”

🌅 Dawn in Vraja

Is spiritual conversation mein poori night pass ho gayi without anyone realizing it.

Morning hote hi Gopīs wake up hui aur:

lamps light kiye
household deities worship ki
curd churning start kiya

Jewels aur earrings lamp-light mein shine kar rahe the.

Unki bangles rhythmic sound create kar rahi thi while they loudly sang Kṛṣṇa’s divine deeds.

Entire heaven un songs aur churning sounds se fill ho gaya, dispelling all inauspiciousness.

🚩 The Gopīs Notice Uddhava’s Chariot

Sunrise ke baad Gopīs ne Nanda’s house ke bahar ek golden chariot dekha.

Woh suspiciously poochne lagi:

“Kya Akrūra phir se aaya hai?”

“Wahi jisne Kṛṣṇa ko Mathurā le jaakar hamse separate kar diya?”

“Kya ab woh hamare bodies ko dead Kaṃsa ke funeral offerings banane aaya hai?”

Isi discussion ke beech Uddhava morning duties complete karke unke paas arrive hua."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 47
    with st.expander("Chapter 47 - Uddhava’s Discourse on the Real Nature of the Lord"):
        text1 = """ 
        🌸 Uddhava Meets the Gopīs

Śrī Śuka continued,

Morning mein jab Gopīs ne Uddhava ko properly dekha, woh stunned reh gayin.

Uski appearance almost Kṛṣṇa jaisi thi:

lotus-like eyes
yellow silk clothes
lotus garland
shining earrings
cheerful smiling face

Sab Vraja maidens curiosity aur longing se uske around gather ho gayin."""
        create_image_text_layout(
            "attached_assets/chapter10/10.47.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Jab unhe pata chala ki woh Kṛṣṇa ka messenger hai, they respectfully welcomed him with shy smiles aur sweet words.

Fir privately usse questions poochne lagi.

💔 The Gopīs Speak Their Pain

Gopīs sadly boli:

“Humein pata chala hai ki tum Kṛṣṇa ke messenger ho aur Nanda-Yaśodā ko comfort dene aaye ho.”

“Lekin honestly… Gokula mein ab uske liye yaad rakhne layak kya bacha hai?”

Fir unhone worldly relationships ki temporary nature explain ki:

courtesans poor lovers ko abandon karti hain
subjects weak king ko leave kar dete hain
birds fruitless trees ko chhod dete hain
guests meal ke baad chale jaate hain

“Exactly waise hi Kṛṣṇa bhi humein leave kar gaya…”

😭 Gopīs Lose Their Shyness

Kṛṣṇa ke childhood aur rāsa memories yaad karke Gopīs openly weep karne lagi.

Social shyness completely disappear ho gayi.

Unki speech, body aur thoughts sab completely Kṛṣṇa mein absorbed thi.

🐝 The Famous “Bhramara-gītā” — Song to the Bee

Ek particular Gopī, Kṛṣṇa ke thoughts mein deeply immersed thi.

Tab usne ek black bee ko dekha.

Usne imagine kiya ki yeh bee actually Kṛṣṇa ka messenger hai.

Then she began speaking to the bee in intense divine madness of love.

😠 “Don’t Touch Our Feet!”

Gopī sarcastically boli:

“O bee! O friend of that rogue Kṛṣṇa!”

“Hamaare feet ko touch mat karo.”

“Tumhari beard-like tentacles Mathurā women ke saffron se stained hain.”

“Jaakar wahi city ladies ko please karo.”

💔 Complaint Against Kṛṣṇa

Fir usne Kṛṣṇa ko compare kiya black bee se:

“Jaise bee flower ka honey drink karke immediately usse abandon kar deta hai…”

“Waise hi Kṛṣṇa ne humein ek baar apne lips ka nectar taste karaya aur instantly leave kar diya.”

“How strange that Lakṣmī still serves him!”

“She must be enchanted by his sweet talks.”

🌲 “Go Sing for the Women of Mathurā”

Gopī continued:

“Humein Kṛṣṇa ki glories mat sunaao.”

“Jaao Mathurā women ke paas.”

“Wahi tumhe rewards dengi, because they now enjoy his embraces and affection.”

“How can any woman resist his charming smiles and dancing eyebrows?”

“We forest girls are nothing before him.”

😢 Love Mixed with Anger

Bee jab uske feet ke paas hover karne laga, she said:

“Humein sweet words se reconcile karne ki koshish mat karo.”

“We abandoned:

husbands
children
social honour
future happiness

sirf Kṛṣṇa ke liye.”

“Aur usne humein abandon kar diya.”

⚡ Gopī Criticizes Previous Avatāras

Divine love-madness mein Gopī ne Kṛṣṇa ke previous avatāras par bhi playful accusations lagaye.

“As Rāma, he secretly killed Vālī.”

“He disfigured Śūrpaṇakhā.”

“As Vāmana he accepted Bali’s worship and then bound him.”

“Enough of friendship with this dark-complexioned trickster!”

Lekin immediately she admitted:

“Still… his stories are too sweet to give up.”

🌌 Kṛṣṇa’s Stories Make People Renounce the World

Gopī said:

“Jo log even once Kṛṣṇa’s līlās ka nectar hear karte hain…”

“Woh homes aur worldly attachments abandon karke wandering ascetics ban jaate hain.”

“Exactly like birds flying free.”

🦌 “We Were Like Innocent Deer”

“We innocent girls hunter ke music se trapped deer ki tarah thi.”

“Kṛṣṇa ke sweet promises ko genuine samajh liya…”

“And now we suffer unbearable pangs of separation.”

💛 Longing for Kṛṣṇa

Finally anger slowly melted into longing.

“O bee…” she softly asked,

“Kya Kṛṣṇa humein remember karta hai?”

“Does he remember Nanda’s house?”

“Uski maidservants?”

“Would that he once again place his sandal-fragrant arm upon my head…”

🌟 Uddhava Praises the Gopīs

Yeh extraordinary love sunkar Uddhava overwhelmed ho gaya.

Woh बोला:

“O Gopīs, you have achieved the highest purpose of human life.”

“Supreme devotion to Kṛṣṇa is attained after:

charity
austerities
Vedic studies
self-control

Lekin tumne naturally attain kar li.”

“You abandoned everything for Kṛṣṇa.”

“Even sages struggle to achieve such devotion.”

🕉️ Kṛṣṇa’s Message Through Uddhava

Then Uddhava delivered Kṛṣṇa’s own message.

Kṛṣṇa said:

“There can never truly be separation between you and me.”

“Just as five elements exist everywhere…”

“I exist within all beings as the Inner Soul.”

Mind, senses aur universe sab uski māyā ke through operate karte hain.

🧘 Purpose of Separation

Kṛṣṇa explained:

“Main physically distant isliye hoon taaki tumhara mind constantly mujh mein absorbed rahe.”

“When beloved is far away, remembrance becomes even deeper.”

“Since you have fully surrendered your hearts to me…”

“You will soon attain me completely.”

🌸 Gopīs Hear the Message

Kṛṣṇa’s message sunkar Gopīs deeply comforted hui.

Fir bhi they continued asking about him:

“Does he ever speak about us in Mathurā?”

“Does he remember those moonlit rāsa nights in Vṛndāvana?”

“Will he return and revive us like rain revives dried forests?”

Some sadly accepted:

“He has now gained kingdom, fame and city wives…”

“Why would he return to forest girls like us?”

🌿 Impossible to Forget Kṛṣṇa

Yet all Gopīs agreed on one thing:

“It is impossible to forget him.”

Everywhere reminded them of Kṛṣṇa:

Yamunā river
Govardhana
Vṛndāvana forests
flute music
his footprints

“Our hearts have been stolen by his smile, gait, glances and words.”

“How can we ever forget him?”

🙏 “Save Gokula from the Ocean of Grief”

At last the Gopīs cried:

“O Lord of Vraja!”

“O destroyer of our suffering!”

“Please rescue Gokula submerged in the ocean of sorrow!”

🌟 Uddhava Glorifies the Gopīs

Uddhava stayed in Vraja for many months, constantly speaking Kṛṣṇa-kathā and reducing everyone’s grief.

Gradually he became awestruck by the Gopīs’ devotion.

Finally he openly praised them:

“Only these Gopīs have truly fulfilled human life.”

“Their love for Kṛṣṇa is what sages and liberated souls aspire for.”

🌱 Uddhava’s Famous Prayer

Uddhava then made one of the most famous prayers in Bhāgavata Purāṇa:

“I wish to become even a shrub, creeper or blade of grass in Vṛndāvana…”

“…so that I may receive the dust of the feet of these Gopīs who abandoned everything for Kṛṣṇa.”

He repeatedly bowed to the dust beneath the feet of the Vraja women.

🚩 Uddhava Returns to Mathurā

Finally Uddhava prepared to leave.

Nanda, Yaśodā aur all cowherds tear-filled eyes ke saath gifts lekar aaye.

They prayed:

“May our minds always stay fixed on Kṛṣṇa’s lotus feet.”

“May our speech always glorify him.”

“May our bodies always bow before him.”

Deeply moved by their devotion, Uddhava returned to Mathurā and reported everything to Kṛṣṇa."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 48
    with st.expander("Chapter 48 - Visit to the Houses of Trivakrā and Akrūra"):
        text1 = """ 
        🌸 Kṛṣṇa Visits Trivakrā

Śrī Śuka continued,

Kṛṣṇa ne realize kiya ki Trivakrā (Kubjā) intense love aur longing mein unke liye pine kar rahi thi.

Being omniscient aur everyone ke indwelling soul, Lord personally uske house gaye taaki uski heartfelt desire fulfil kar sakein."""
        create_image_text_layout(
            "attached_assets/chapter10/10.48.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        🏡 Trivakrā’s Luxurious House

Kubjā ka house extraordinary luxury se decorated tha:

pearl garlands
flags and canopies
rich beds and seats
fragrant incense
scented lamps
flowers and perfumes

Entire atmosphere erotic beauty aur royal elegance se filled tha.

Walls beautiful kāmaśāstra-style paintings se adorned thi.

💛 Trivakrā Welcomes Kṛṣṇa

Jab Trivakrā ne Kṛṣṇa ko arrive hote dekha, woh excitement aur nervous joy se immediately seat se uth gayi.

Apni female companions ke saath aage badhkar usne Kṛṣṇa aur Uddhava ka warm welcome kiya.

High comfortable seats aur worship articles respectfully offer kiye gaye.

Uddhava humility se floor par baith gaye, while Kṛṣṇa worldly etiquette follow karte hue inner chamber ki taraf chale gaye.

🌺 Trivakrā Beautifies Herself

Trivakrā then lovingly prepared herself:

bath liya
cosmetics apply kiye
fine clothes pehne
ornaments aur flower garlands se decorate hui
perfumes aur betel use kiya

Shy smiles aur amorous glances ke saath woh Kṛṣṇa ke paas aayi.

✨ Kṛṣṇa Grants Her Desire

First meeting ki bashfulness ki wajah se woh slightly nervous thi.

Kṛṣṇa ne affectionately uska bracelet-adorned hand pakda aur usse bed par apne paas bithaya.

Lord ne usse woh desired happiness diya jo woh deeply wish karti thi.

Bhāgavata explains ki yeh reward tha us “small act of merit” ka — jab usne Kaṃsa ke liye le ja raha fragrant sandal-paste lovingly Kṛṣṇa ko offer kiya tha.

💞 Trivakrā’s Love-Fever Ends

Kṛṣṇa ke lotus-feet ki fragrance aur touch ne Trivakrā ke separation-pain aur love-fever ko instantly destroy kar diya.

Usne blissfully Kṛṣṇa ko embrace kiya aur long separation ka suffering finally disappear ho gaya.

🙏 Trivakrā’s Request

Even after receiving Kṛṣṇa’s association, Trivakrā emotionally pleaded:

“O beloved Lord…”

“Please kuch din mere house mein stay kijiye.”

“I cannot bear separation from you.”

🌟 Kṛṣṇa Leaves After Blessing Her

Kṛṣṇa ne uski desire fulfil ki aur honour bhi diya.

Then respectful Lord of the Universe Uddhava ke saath wapas palace return kar gaye.

Bhāgavata then remarks:

Jo person Supreme Lord ko worship karke sirf sensual pleasures maangta hai, uski intelligence actually distorted hai — because Lord can grant ultimate liberation itself.

🚩 Kṛṣṇa Visits Akrūra

After this Kṛṣṇa ne decide kiya ki Akrūra ko ek important mission diya jaye.

So Kṛṣṇa, Balarāma aur Uddhava together Akrūra ke house gaye.

Distance se hi Akrūra unhe dekhkar overwhelming joy se bhar gaya.

Woh quickly aage badha aur un sabko lovingly receive kiya.

🙇 Akrūra Worships the Lords

Though older in age, Akrūra knew their divine nature.

Isliye usne respectfully Kṛṣṇa aur Balarāma ko bow kiya.

Then he:

washed their feet
sprinkled that sacred water on his head
offered clothes, perfumes, garlands and ornaments
massaged their feet after placing them in his lap

Deep devotion aur humility ke saath he began glorifying them.

🌌 Akrūra Praises Kṛṣṇa

Akrūra बोले:

“Kaṃsa aur uske followers ko kill karke aapne Yadu race ko endless suffering se rescue kar diya.”

“You are actually:

Pradhāna (Primordial Matter)
Puruṣa (Supreme Self)

Both cause and support of the universe.”

🕉️ Supreme Brahman

Akrūra further explained:

“O Kṛṣṇa, you are Supreme Brahman itself.”

“You create the universe through your powers and then enter it as the Inner Soul.”

“Just as earth, water and fire appear in countless forms…”

“You also manifest in innumerable beings and forms.”

🌠 Beyond Bondage

Akrūra clarified an important spiritual point:

Though Kṛṣṇa appears born like ordinary beings, actually:

no bondage
no limitation
no real birth
no karma

can ever apply to him.

“All such ideas are projections of ignorance.”

⚔️ Purpose of the Incarnation

Akrūra said:

“You incarnated in Vasudeva’s house along with Balarāma to remove Earth’s burden by slaying demonic kings.”

“And also to increase the glory of the Yadu dynasty.”

🙏 “Cut My Bonds of Māyā”

Then Akrūra made a heartfelt prayer:

“O Lord!”

“Please cut away my attachments to:”

sons
wife
wealth
relatives
even my own body

😊 Kṛṣṇa’s Sweet Reply

Hearing these prayers, Kṛṣṇa smiled sweetly and affectionately addressed Akrūra.

“You are our elder relative and well-wisher.”

“We are like your children.”

“Saintly persons like you are greater than even holy places.”

“Tīrthas purify gradually…”

“But saints sanctify immediately merely by their presence.”

📜 Mission to Hastināpura

Finally Kṛṣṇa revealed why he had come.

“O Akrūra, please go to Hastināpura.”

“Investigate the condition of the Pāṇḍavas.”

“We have heard that after Pāṇḍu’s death they are living under Dhṛtarāṣṭra’s care.”

“But blind Dhṛtarāṣṭra is controlled by his wicked son Duryodhana and may not be treating them fairly.”

“Find out the truth carefully.”

“Then we will act for the welfare of our friends.”

🚩 Akrūra Accepts the Mission

Thus briefing Akrūra about the mission, Lord Hari returned with Balarāma and Uddhava back to the palace."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 49
    with st.expander("Chapter 49 - Akrūra’s Mission to Hastinapura"):
        text1 = """ 
        🚩 Akrūra Arrives in Hastināpura

Śrī Śuka continued,

Akrūra finally Hastināpura pahunch gaye — glorious capital of the Puru dynasty.

Wahan unhone many important figures ko dekha:

Dhṛtarāṣṭra
Bhīṣma
Vidura
Kuntī
Droṇa
Kṛpa
Karṇa
Duryodhana
Aśvatthāmā
Pāṇḍavas

aur many royal elders and relatives."""
        create_image_text_layout(
            "attached_assets/chapter10/10.49.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        🤝 Akrūra Meets the Kuru Elders

Akrūra ne sab relatives aur elders ko proper respect aur affection ke saath meet kiya.

Sabne Mathurā ke Yādavas ke welfare ke baare mein poocha aur Akrūra ne bhi unke wellbeing ke baare mein enquire kiya.

🕵️ Akrūra Secretly Investigates

Kṛṣṇa ka real purpose yaad rakhte hue Akrūra Hastināpura mein several months tak ruk gaye.

Woh carefully observe kar rahe the:

Dhṛtarāṣṭra ka behaviour
Duryodhana ki jealousy
Śakuni ka influence
Pāṇḍavas ke against conspiracies
☠️ Poisoning of Bhīma and Other Plots

Vidura aur Kuntī ne Akrūra ko secretly sab truth bataya.

Unhone explain kiya ki Dhṛtarāṣṭra ke sons:

Bhīma ko poison de chuke the
constantly Pāṇḍavas se jealous the
unki popularity aur strength tolerate nahi kar pa rahe the

Subjects ka love bhi Pāṇḍavas ki taraf tha, jis wajah se Kauravas aur insecure ho gaye the.

😭 Kuntī’s Emotional Questions

Jab Kuntī ne apne cousin Akrūra ko dekha, woh deeply emotional ho gayi.

Birthplace aur relatives ko remember karke unki eyes tears se fill ho gayi.

Woh poochne lagi:

“Kya mere parents mujhe yaad karte hain?”

“Kya Vasudeva, Devakī aur sab relatives well hain?”

“Kya Kṛṣṇa aur Balarāma apni paternal aunt aur uske sons ko remember karte hain?”

🐺 “We Live Among Wolves”

Kuntī sadly boli:

“Main yahan enemies ke beech reh rahi hoon…”

“Bilkul wolves ke surrounded deer ki tarah.”

“Mere children fatherless hain.”

“Will Kṛṣṇa ever comfort us?”

🙏 Kuntī’s Prayer to Kṛṣṇa

Then Kuntī directly Kṛṣṇa ko prayer karne lagi:

“Oh Kṛṣṇa! Oh Great Yogin!”

“Oh Soul of the Universe!”

“Please protect me and my children.”

“I have taken refuge in you alone.”

🌌 Supreme Refuge

Kuntī further declared:

“For those terrified by death and saṃsāra…”

“There is no refuge except Kṛṣṇa’s lotus feet.”

She bowed mentally to Kṛṣṇa as:

Supreme Brahman
Supreme Soul
Lord of Yoga
Embodiment of Divine Reality

💛 Akrūra and Vidura Console Kuntī

Kuntī loudly lament karne lagi while remembering Kṛṣṇa and her relatives.

Akrūra aur wise Vidura ne lovingly unhe console kiya.

Unhone remind karaya ki Pāṇḍavas ordinary humans nahi the — they had divine origin and great destiny connected to Kṛṣṇa’s mission.

👑 Akrūra Advises Dhṛtarāṣṭra

Mathurā return karne se pehle Akrūra directly Dhṛtarāṣṭra ke paas gaye.

Sab relatives ke saamne unhone respectful but firm advice diya.

⚖️ “Rule With Impartiality”

Akrūra बोले:

“O son of Vicitravīrya, after Pāṇḍu’s death aap throne par baithe hain.”

“If you govern righteously and treat both your sons and the Pāṇḍavas equally…”

“Then you will gain prosperity and eternal fame.”

🔥 Warning of Destruction

Lekin Akrūra ne warning bhi di:

“Agar partiality aur injustice follow karoge…”

“Toh duniya mein blame milega aur after death hellish suffering bhi.”

“So please behave impartially toward both Kauravas and Pāṇḍavas.”

⌛ Temporary Nature of Relationships

Akrūra then gave deep spiritual wisdom:

“In this world no companionship is eternal…”

“Not even with one’s own body.”

“Then what to say of wives, sons and wealth?”

“Person is born alone…”

“dies alone…”

“and experiences karma alone.”

💰 Wealth and Sons Cannot Save Anyone

Akrūra explained:

Foolish people unrighteously wealth accumulate karte hain thinking:

“These are my sons, my possessions.”

Lekin eventually wahi people unka wealth consume kar lete hain aur unhe abandon bhi kar dete hain.

Then sinful person apne karmas ka burden alone carry karta hai.

🌙 “World Is Like a Dream”

Akrūra finally concluded:

“This world dream, illusion aur imagination ki tarah temporary hai.”

“So control your mind and become calm and impartial.”

😔 Dhṛtarāṣṭra’s Honest Reply

Dhṛtarāṣṭra admitted:

“O Akrūra, your advice nectar jaisa sweet aur beneficial hai.”

“But unfortunately…”

“Mera mind mere sons ke attachment ki wajah se unstable aur partial hai.”

“Your teachings mere heart mein permanently stay nahi kar pa rahi.”

🌌 Dhṛtarāṣṭra Accepts Kṛṣṇa’s Supreme Will

Dhṛtarāṣṭra further reflected:

“Who can oppose Supreme Lord’s will?”

“Kṛṣṇa himself Yadu race mein Earth ka burden remove karne descend hue hain.”

He bowed mentally to Kṛṣṇa as:

creator of the universe
controller of karma
source and end of saṃsāra

🚩 Akrūra Returns to Mathurā

Dhṛtarāṣṭra ka inner mindset properly understand karne ke baad Akrūra sab relatives se farewell lekar Mathurā return ho gaye.

Wahan unhone Kṛṣṇa aur Balarāma ko full report diya regarding:

Dhṛtarāṣṭra’s bias
Kauravas’ jealousy
dangers surrounding the Pāṇḍavas

which was the real purpose of his mission to Hastināpura."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 50
    with st.expander("Chapter 50 - Settlement at the Fort of Dvārakā"):
        text1 = """ 
        👑 Jarāsandha Seeks Revenge

Śrī Śuka continued,

Kaṃsa ki wives — Asti aur Prāpti — apne husband ki death ke baad grief se shattered ho gayin aur apne father Jarāsandha ke paas Magadha chali gayin.

Unhone fully explain kiya ki Kṛṣṇa ne Kaṃsa ko slay kar diya.

Yeh sunkar mighty king Jarāsandha rage aur sorrow se bhar gaya.

Usne immediately decide kiya:

“Main entire Yādava race ko earth se wipe out kar dunga.”"""
        create_image_text_layout(
            "attached_assets/chapter10/10.50.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        ⚔️ Siege of Mathurā

Jarāsandha ne gigantic army assemble ki:

➡️ 23 Akṣauhiṇīs!

Entire Mathurā city ko all four sides se surround kar diya gaya.

Many allied kings bhi uske saath aaye:

Śiśupāla
Śālva
Rukmī
Jayadratha
Śakuni
Drupada
Pauṇḍraka
Ekalavya

aur countless other rulers.

War-drums, conches aur battle-cries ocean ki roaring jaise sound create kar rahe the.

🌌 Kṛṣṇa Understands His Mission

Mathurā panic aur fear se fill ho gayi.

Lekin Kṛṣṇa perfectly calm rahe.

Unhone internally reflect kiya:

“Mera incarnation earth ka burden remove karne ke liye hua hai.”

“Yeh massive armies actually Earth ka heavy burden hain.”

“Main ab in armies ko destroy karunga…”

“Lekin Jarāsandha ko abhi nahi marunga.”

“Woh repeatedly aur armies gather karega — aur Earth ka burden aur reduce hoga.”

☀️ Divine Chariots Descend from Heaven

Jab Kṛṣṇa ye thoughts kar rahe the, suddenly sky se two blazing celestial chariots descend hue.

Saath hi divine weapons bhi manifest hue:

Sudarśana discus
Kaumodakī mace
Śārṅga bow
Nandaka sword
inexhaustible quivers

Balarāma ke liye:

plough weapon
pestle-club

appear hue.

🛡️ Kṛṣṇa Encourages Balarāma

Kṛṣṇa lovingly बोले:

“O respected brother, Yādavas great danger mein hain.”

“Please apne divine weapons lekar unhe protect kijiye.”

“Our incarnation ka purpose hi righteous people ko protect karna hai.”

“Today we must destroy this massive army.”

🚪 Defense of the Four Gates

Kṛṣṇa ne Yādava warriors ko different city gates par deploy kiya:

Eastern Gate
Vasudeva
Kṛtavarmā
Uddhava
Northern Gate
Ugrasena
Sudāman
Western Gate
Sātyaki
Gada
Akrūra

Then Kṛṣṇa aur Balarāma personally northern gate se battlefield ki taraf nikle.

🐚 The Roar of Pāñcajanya

Kṛṣṇa ne apna conch Pāñcajanya loudly blow kiya.

Uski sound ne enemy armies ke hearts mein terror fill kar diya.

Balarāma ne bhi lion-like roar kiya.

Entire battlefield tremble karne laga.

😠 Jarāsandha Insults Kṛṣṇa

Kṛṣṇa aur Balarāma ko dekhkar Jarāsandha mocked Kṛṣṇa:

“I will not fight with a mere boy like you.”

“You coward! You hid from Kaṃsa.”

“You are only a cowherd.”

Fir usne Balarāma ko challenge kiya:

“If you have courage, then fight me!”

🔥 Kṛṣṇa’s Calm Reply

Kṛṣṇa calmly बोले:

“True heroes boast nahi karte.”

“They prove their valour through action.”

“We don’t take seriously the words of those who are delirious or near death.”

⚔️ The Great Battle Begins

Jarāsandha’s gigantic army storm-cloud ki tarah Yādavas ko surround karne lagi.

Mathurā ki women walls aur towers se battle dekh rahi thi.

Jab unhone Kṛṣṇa aur Balarāma ke chariots ko enemy masses mein disappear hota dekha, many women fear se faint ho gayin.

🏹 Kṛṣṇa’s Devastating Archery

Then Kṛṣṇa ne Śārṅga bow stretch kiya.

Bowstring ki thunderous sound battlefield mein echo hone lagi.

Rapid speed se:

arrows nikalna
set karna
release karna

start hua.

Kṛṣṇa continuously:

elephants destroy kar rahe the
horses cut down kar rahe the
chariots shatter kar rahe the
infantry annihilate kar rahe the

Unka bow blazing fire-brand ki tarah whirl ho raha tha.

🐚 Pāñcajanya Terrifies the Kings

Kṛṣṇa ne fir Pāñcajanya conch blow kiya.

Terrifying blast sunkar many kings ka courage break ho gaya.

Meanwhile Yādava warriors inspired hokar all four gates par enemies ko push back karne lage.

⚡ Kṛṣṇa vs Śiśupāla

Śiśupāla loudly challenged:

“Stop, Kṛṣṇa!”

Battle instantly intense ho gaya.

Śiśupāla ne:

Kṛṣṇa ke horses ko hit kiya
charioteer ko strike kiya
many arrows launch kiye

Kṛṣṇa smilingly बोले:

“Well done, Śiśupāla.”

“You truly are a skilled archer.”

Fir suddenly Kṛṣṇa ne:

thirty kings ke bows cut kiye
horses aur charioteers kill kiye
Śiśupāla ka bow, crown aur umbrella destroy kar diya

Enemy army confusion aur panic mein aa gayi.

🩸 River of Blood

Battlefield horrifying scene ban gaya.

Dead:

elephants
horses
soldiers
broken chariots

everywhere scattered the.

Bhāgavata battlefield ko blood-river se compare karta hai:

severed arms = snakes
floating heads = tortoises
bows = ripples
weapons = bushes

🌪️ Balarāma’s Terrifying Power

Meanwhile Balarāma apne pestle aur plough weapons se enemies ko smash kar rahe the.

Unki attacks se blood-streams flow hone lagi.

Cowards terror se freeze ho rahe the…

Lekin brave warriors aur inspired ho rahe the.

🏔️ Balarāma Captures Jarāsandha

Entire army destroy hone ke baad Jarāsandha alone remaining warrior tha.

Fir Balarāma aur Jarāsandha ka mountain-like duel start hua.

Jarāsandha ne giant mace Balarāma par throw ki.

Balarāma smilingly us attack ko dodge karke apne pestle se destroy kar diya.

Fir unhone Jarāsandha ka chariot aur charioteer destroy kar diya.

Finally lion ki tarah Balarāma ne Jarāsandha ko capture kar liya.

✋ Kṛṣṇa Releases Jarāsandha

Balarāma Jarāsandha ko bind karne wale the…

Lekin Kṛṣṇa ne stop kar diya.

Because Kṛṣṇa ka bigger plan tha:

Jarāsandha repeatedly armies gather karega aur Earth ka burden further reduce hoga.

Thus Jarāsandha ko intentionally release kar diya gaya.

😔 Jarāsandha’s Shame

Defeated aur humiliated Jarāsandha initially forest jaakar penance perform karna chahta tha.

Lekin allied kings ne usse samjhaya:

“Victory aur defeat karma ke result hote hain.”

Finally woh sadness ke saath Magadha return kar gaya.

🎉 Victory Celebration in Mathurā

Gods sky se flowers rain karne lage.

Kṛṣṇa victorious state mein Mathurā return hue.

Entire city decorate hui:

flags
flowers
arches
music
Vedic chanting

Women lovingly:

flowers shower kar rahi thi
curd-rice tilak apply kar rahi thi
joyful eyes se Kṛṣṇa ko dekh rahi thi

🔁 Seventeen More Invasions

Bhāgavata states:

Jarāsandha ne total 17 more times same gigantic armies ke saath attack kiya.

Har baar:

Yādavas army destroy kar deti
Jarāsandha escape kar jata

Kṛṣṇa intentionally usse alive leave karte rahe.

⚠️ Kālayavana Appears

18th invasion ke around another danger appear hua:

➡️ mighty Yavana king Kālayavana.

Nārada ne usse bataya tha ki Yādavas uske equal opponents hain.

He invaded Mathurā with:

➡️ 3 crore Mleccha warriors!

🌊 Creation of Dvārakā

Kṛṣṇa realized:

“Agar Jarāsandha aur Kālayavana simultaneously attack karenge…”

“Toh Yādavas danger mein aa jayenge.”

Therefore Kṛṣṇa ne decide kiya:

➡️ sea ke andar ek impregnable fortress-city construct karni hogi.

Using divine yogic power, Lord ne western ocean mein magnificent city build ki:

✨ Dvārakā ✨

🏙️ Beauty of Dvārakā

Dvārakā extraordinary wonder thi:

12 yojanas wide
crystal balconies
golden towers
jeweled palaces
celestial gardens
divine parks
silver and brass storehouses
emerald floors

🌳 Gifts from the Gods

Different gods ne divine gifts offer kiye:

Indra
Sudharmā assembly hall
Pārijāta tree
Varuṇa
thousands of celestial horses
Kubera
eight treasures

Even Siddhas apni powers Kṛṣṇa ko resubmit karne lage.

🚪 Yādavas Shift to Dvārakā

Finally Kṛṣṇa ne apni yogic powers se all Yādavas ko safely Dvārakā transfer kar diya.

Balarāma remaining Mathurā population ki protection handle kar rahe the.

Then lotus-garland pehne hue, completely unarmed, Kṛṣṇa Mathurā gates se bahar nikle — ready to deal personally with Kālayavana."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 50(a)
    with st.expander("Chapter 50(a) - Jarāsandha’s Second Expedition"):
        text1 = """ 
        ⚔️ Jarāsandha’s Humiliation Burns Within Him

Śrī Śuka continued,

Previous defeat ke baad mighty king Jarāsandha day and night humiliation aur anger se burn ho raha tha.

Exactly third month mein usne once again all allied kings ko war ke liye summon kiya."""
        create_image_text_layout(
            "attached_assets/chapter10/10.50a.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        🌍 Massive Alliance of Kings

Jarāsandha ke saath enormous coalition gather hui including rulers of:

Matsya
Mālava
Cedi
Kuru
Pāñcāla
Kerala
Avanti
Kāśī
Gandhāra
Kaliṅga
Andhra
Sindhu
Madra
Sauvīra
Trigarta

and many mountain warriors.

Entire force totaled:

➡️ 23 Akṣauhiṇīs

again.

🏕️ Encampment Near Mathurā

Huge army westward march karke finally Mathurā pahunchi.

Yamunā riverbank par massive war-camp establish hua:

royal tents
elephants
cavalry
chariots
infantry
camp followers

everywhere spread out the.

Jarāsandha relaxed while:

Sūtas
Māgadhas
royal bards

uski praises sing kar rahe the.

🧠 Kṛṣṇa’s Strategic War Council

Enemy preparations sunkar Kṛṣṇa immediately war council convene kiya.

Meeting mein present the:

Balarāma
Vasudeva
Uddhava
Akrūra
Śaineya (Sātyaki)
Āhuka
Sāraṇa

Entire night strategy discuss hoti rahi.

🌅 Surprise Attack at Dawn

Before sunrise Kṛṣṇa ne Yādava army ko mobilize kiya.

He divided the fourfold army into:

elephants
cavalry
chariots
infantry

and arranged them in three divisions.

🛡️ Deployment of the Yādavas
Left Wing

Kṛṣṇa sent:

Balarāma
Hārdikya
Gada
Sāraṇa

Right Wing

He deployed:

Sātyaki
Vipṛthu
Pṛthu
Uddhava

with strong forces.

Center

Kṛṣṇa personally entered from the front directly into Jarāsandha’s vast army.

😴 Enemy Army Completely Unprepared

At that early dawn enemy camp still deeply relaxed and unprepared tha.

Bhāgavata vividly describes:

horses unsaddled the
elephants armourless the
soldiers ne weapons tak nahi uthaye the
hair untied the
coats of mail nahi pehne the
chariots yoked nahi the
battle-flags raised nahi the

Entire army unsuspectingly sleeping ya casually resting thi.

☀️ Kṛṣṇa Enters at Sunrise

As sunrise eastern mountains par glow kar raha tha…

birds singing
lotuses blooming
bees humming

usi moment yellow-clad Kṛṣṇa directly enemy camp ke andar enter hue.

😱 Total Chaos in the Camp

Suddenly three sides se attack hote hi allied kings panic mein aa gaye.

Nobody samajh nahi pa raha tha:

“Kya ho raha hai?”

Some:

rallied together
grabbed weapons
counterattacked

while others fear mein flee kar gaye.

🩸 Brutal Battlefield

Battle instantly horrifying ban gaya.

Some soldiers:

armour shattered
limbs severed
thighs cut
arms destroyed

Even in chaos, brave warriors mounted unsaddled horses aur desperate resistance dene lage.

⚔️ Kṛṣṇa Fights Single-Handedly

Govinda apne chariot par almost single-handedly enemy formations ke andar penetrate kar gaye.

Jo bhi warriors unke against aaye:

➡️ Kṛṣṇa rapidly unhe destroy karte gaye.

🌪️ Balarāma’s Devastation

Meanwhile mighty Balarāma left flank se enemy forces par toot pade.

Unhone Magadhan army ko heavily rout kar diya.

🏹 Sātyaki’s Assault

Right side par Sātyaki ne:

elephants
cavalry
infantry
chariots

ke saath violent attack launch kiya.

Enemy ko “sound drubbing” diya gaya.

🏃 Complete Collapse of Jarāsandha’s Army

Soon entire Magadhan alliance terror se break ho gayi.

Army every direction mein flee karne lagi.

Sātyaki ne fleeing enemies ko:

5 yojanas tak pursue kiya

aur immense destruction ke baad victorious return kiya.

🐘 Immense War Spoils

Kṛṣṇa ne battlefield se huge spoils seize kiye:

giant elephants
weapons
chariots
horses
flags
armour

He also captured:

jewel-studded umbrellas
crowns
belts
earrings
gold ornaments
luxurious garments

👑 Balarāma Seizes Jarāsandha’s Wealth

Kṛṣṇa ke instruction par Balarāma enormous wealth collect kar laaye:

treasury
vehicles
weapons
ornaments
women of Jarāsandha’s harem
captured subjects

Entire spoils finally king Ugrasena ko present kiye gaye."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 50(b)
    with st.expander("Chapter 50(b) - The Third Siege of Mathura: Jarāsandha’s defeat"):
        text1 = """ 
        😠 Jarāsandha Seeks Help from Bāṇa

Śrī Śuka continued,

Second defeat ke baad Jarāsandha ka pride completely wounded ho gaya tha.

Humiliated king directly Śoṇitapura gaya — mighty thousand-armed demon king Bāṇa ke paas help maangne."""
        create_image_text_layout(
            "attached_assets/chapter10/10.50b.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        🏰 Grand Welcome in Śoṇitapura

Jab Bāṇa ko pata chala ki uska close friend Jarāsandha aa raha hai, woh personally huge royal procession ke saath welcome karne nikla.

Procession mein the:

decorated elephants
caparisoned horses
splendid chariots
banners and flags
umbrellas
drums and trumpets
dancers and courtesans
Sūtas and bards

Entire city festival atmosphere se fill ho gayi.

🤝 Friendship Between Bāṇa and Jarāsandha

Bhāgavata emphasizes ki dono rulers extremely close friends aur mutual well-wishers the.

Royal assembly mein respectfully seat lene ke baad Jarāsandha apni humiliation narrate karne laga.

⚡ Jarāsandha Complains About Kṛṣṇa

Jarāsandha bitterly bola:

“That wicked cowherd Kṛṣṇa attacked me through surprise tactics.”

“He plundered my:

elephants
horses
chariots
weapons

and huge war resources.”

Then he added:

“My allied kings prevented me from fighting him single-handedly.”

“So now I seek your military assistance.”

💎 Bāṇa’s Generous Promise

Bāṇa immediately declared:

“Nothing I possess is separate from you.”

“These elephants, horses, subjects, kingdom — all are at your disposal.”

🐘 Massive Reinforcements

Then Bāṇa supplied Jarāsandha with enormous military support:

60,000 elephants
100,000 chariots
1 million swift horses

Aur bhi dangerous:

➡️ 300 expert Dānavas skilled in magical warfare.

👹 Kumbhāṇḍa and Kūpakarṇa

Bāṇa ne apne two powerful ministers bhi bheje:

Kumbhāṇḍa
Kūpakarṇa

These Daityas black magic warfare mein specialists the.

Bhāgavata comments ki unki power Lord Hari ke saamne insignificant thi.

⚔️ Third Siege of Mathurā

Supreme power of Viṣṇu ko na samajh paane ki wajah se all kings again war preparations mein lag gaye.

Jarāsandha gigantic fourfold army lekar phir Mathurā pahunch gaya.

City ko completely surround kar diya gaya.

🏙️ Attack on Mathurā’s Walls

Enemy forces:

spears
clubs
pickaxes
catapults
huge stones

use karke Mathurā ke fortifications destroy karne lage.

🥁 War Drums of the Yādavas

Attack ki news sunkar enraged Kṛṣṇa aur Balarāma ne war-drums beat karwaye.

Army rapidly assemble hui.

Leading Yādava warriors included:

Sātyaki
Kṛtavarmā
Ugrasena
Gada
Āhuka
Vasudeva

Then Kṛṣṇa aur Balarāma lion-like fury ke saath battlefield ki taraf nikle.

🐚 Blast of Pāñcajanya

Mathurā se bahar nikalte hi lotus-eyed Kṛṣṇa ne loudly Pāñcajanya conch blow kiya.

Its terrifying sound enemy hearts mein fear bharne laga.

👹 Demonic Illusion Warfare

Battle begin hote hi Bāṇa ke demon ministers:

Kumbhāṇḍa
Kūpakarṇa

apni māyā-based magical warfare use karne lage.

Illusions aur supernatural tactics ki wajah se Yādava army disturbed hone lagi.

🌟 Kṛṣṇa Destroys the Illusions

Kṛṣṇa ne instantly situation understand kar li.

Using:

“Knowledge-Missile” (Jñāna-astra)

Lord ne ek moment mein saari illusions destroy kar di.

Then he ordered:

“Sātyaki aur Kṛtavarmā — you engage those Daityas.”

⚔️ Fierce Duels Begin

Immediately:

Sātyaki vs Kumbhāṇḍa
Kṛtavarmā vs Kūpakarṇa

terrible battles start hue.

🏹 Kṛṣṇa’s Impossible Archery

Bhāgavata marvelously describes Kṛṣṇa’s combat skill.

With just one bow in hand, he single-handedly fought hundreds of Kṣatriyas simultaneously.

From Śārṅga bow:

10 arrows per soldier
100 per horse
1000 per chariot
10,000 per elephant

release ho rahe the!

The text calls it:

“a tremendously aweful miracle.”
🩸 Battlefield Carnage

Battlefield horrific ban gaya:

trunks of elephants severed
horses neck-cut dead pade the
shattered chariots everywhere scattered the
bleeding soldiers uprooted Kiṃśuka trees jaise lag rahe the

😡 Jarāsandha Challenges Balarāma

Apni army ko collapsing dekhkar Jarāsandha directly Balarāma ki taraf charge hua.

He remembered previous humiliation and shouted:

“Take up your pestle if you dare!”

“Show me your strength before I crush you with my mace!”

⚡ Balarāma’s Terrifying Rage

Challenge sunkar Balarāma’s eyes rage se blaze karne lage.

He grasped his lightning-like pestle exactly like Yama lifting his rod at cosmic destruction.

Then:

thousand circles mein whirl kiya
fiery pestle hurl kiya
lion-like roar kiya

🏔️ The Titanic Duel

Jarāsandha ka chariot shaken ho gaya.

Lekin he jumped down and rushed with giant iron mace.

Balarāma bhi chariot leave karke foot combat mein aa gaye.

Then gigantic duel begin hua:

mace blows
grappling
wrestling
chest collisions
ground rolling

Bhāgavata compares them to:

two maddened elephants.
🌲 Trees and Rocks Pulverized

Dono warriors ek dusre ko drag karte hue battlefield mein move kar rahe the.

Their strength se:

nearby trees
rocks
ground itself

powder banne laga.

😨 Allied Kings Lose Courage

Jarāsandha aur Balarāma ki terrifying duel dekhkar many kings mentally collapse hone lage.

They started thinking:

“Jarāsandha may actually die today.”

Fear ki wajah se unka enthusiasm for battle disappear hone laga.

🏹 Sātyaki Defeats Kumbhāṇḍa

Meanwhile Kumbhāṇḍa ne Sātyaki ko three arrows se wound kiya.

Angry serpent ki tarah breathing karte hue Sātyaki ne:

five iron arrows liye
bowstring ears tak pull ki
Kumbhāṇḍa ko chest, forehead, throat aur crown par strike kiya

Daitya unconscious hoke chariot mein gir gaya.

His frightened charioteer immediately battlefield se usse le gaya.

👹 Daityas Flee the Battlefield

Kumbhāṇḍa ko defeated dekhkar Kūpakarṇa bhi battle abandon kar gaya.

Both demon ministers:

remaining troops lekar
without even informing Jarāsandha

directly Śoṇitapura return kar gaye."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 50(c)
    with st.expander("Chapter 50(c) - Conquest of Karvīrapura"):
        text1 = """ 
        😨 Jarāsandha’s Army Collapses

Śrī Śuka continued,

Jab Bāṇa ke demon forces battlefield abandon karke bhaag gaye, tab remaining allied kings completely demoralized ho gaye.

Yādava weapon-showers ki wajah se entire enemy army exhausted aur terrified feel karne lagi.    """
        create_image_text_layout(
            "attached_assets/chapter10/10.50c.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        ⚡ Balarāma Overpowers Jarāsandha

Battlefield mein Balarāma suddenly realized ki enemy strength almost collapse ho chuki hai.

Enraged Balarāma ne:

➡️ Jarāsandha ke hair pakad liye with his left hand.

Then he prepared to smash Jarāsandha’s head with his terrible pestle.

🌌 Divine Voice from Heaven

Exactly us moment sky se thundercloud-like incorporeal voice sunai di:

“O Balarāma, Jarāsandha tumhare dwara marne ke liye destined nahi hai.”
“Battle se peacefully return karo.”

🙏 Balarāma Obeys the Divine Command

Hearing heavenly order, mighty Balarāma immediately stopped.

He released Jarāsandha and returned to his chariot.

Meanwhile:

Siddhas
sages
bards
singers
Brahmaṇas

unke glory praises karne lage.

😔 Jarāsandha Retreats in Shame

Jarāsandha:

head lowered
tiny surviving force ke saath
defeated kings se surrounded

battlefield leave karke apni capital return kar gaya.

🏹 Kṛṣṇa Continues the Slaughter

While Jarāsandha retreat kar raha tha, Kṛṣṇa still battlefield mein enemy kings ko devastate karte rahe.

Bhāgavata says:

➡️ He routed and killed the majority of hostile kings.

🎉 Triumphant Return to Mathurā

Victory ke baad Kṛṣṇa grand procession ke saath Mathurā return hue.

Unke saath:

Sūtas
Māgadhas
bards
praising Brahmaṇas

constantly victory songs ga rahe the.

🏙️ Mathurā Celebrates

Bhāgavata beautifully describes Mathurā:

high fortification walls
lofty gates
banners waving
lamps shining everywhere

As Kṛṣṇa entered city:

flowers shower kiye gaye
fried grains scatter hue
women rooftops se folded palms ke saath blessings dene lagi

Citizens ne:

garlands
perfumes
gifts
precious presents

offer kiye to Kṛṣṇa aur Balarāma.

👑 Royal Assembly of the Yādavas

Assembly hall mein Kṛṣṇa seated hue together with:

Balarāma
Sātyaki
Ugrasena
Uddhava
Akrūra

Yādavas aur Brahmaṇas ne Lord ko Indra-like honours diye.

🏔️ Desire to Visit Gomanta

Some time later Kṛṣṇa aur Balarāma ne southern direction travel karne ka decision liya.

Unka goal tha:

Mount Gomanta

— famous inaccessible mountain fortress.

🌍 Journey Through Many Lands

Dono brothers crossed:

Yamunā
rivers
hills
mountains
forests
many kingdoms

during their southern journey.

🌲 Encounter with Paraśurāma

Travelling ke dauraan they suddenly saw:

➡️ a radiant sage beneath a tree.

He had:

matted hair
bark garments
deer-skin clothing
kamaṇḍalu beside him
hundreds of disciples

and shone like the Sun itself.

This sage was:

Paraśurāma.

🙏 Kṛṣṇa Greets Paraśurāma

Kṛṣṇa aur Balarāma respectfully bowed before him.

Then Kṛṣṇa said:

“I bow to you, O Paraśurāma, son of Jamadagni.”

“We are known as Balarāma and Kṛṣṇa.”

“Have you heard of us?”

🌟 Paraśurāma Recognizes the Supreme Lord

Paraśurāma lovingly gazed upon both brothers and replied:

“I know you are the Supreme transcendent Lord born in the Yadu dynasty.”

He further glorified Kṛṣṇa:

cause of all creation
ancient supreme person
source of all worlds

❓ Why Have You Come Here?

Paraśurāma then asked:

“What purpose brings you both here?”

Kṛṣṇa replied:

“We desire to see Mount Gomanta and its fortress.”

⚔️ Warning About Karavīra

Paraśurāma warned them:

“At Gomanta’s foot lies city Karavīra.”

“It is ruled by Śṛgāla Vāsudeva.”

“He will not tolerate your presence.”

“So first defeat him in battle.”

🏔️ Arrival at Gomanta and Karavīra

After taking leave of Paraśurāma, both brothers continued southward.

Soon they saw:

gigantic sky-touching trees
Mount Gomanta
fortified city Karavīra

with:

towers
ramparts
palaces
huge gates

🐚 Kṛṣṇa Blows the Conch

Upon arrival Kṛṣṇa loudly blew his conch.

Hearing the blast:

Śṛgāla Vāsudeva became furious.

He immediately marched out with massive:

infantry
cavalry
elephants
chariot divisions

⚔️ Battle at Karavīra

Śṛgāla attacked fiercely and covered Kṛṣṇa-Balarāma with torrents of arrows.

But both Yādava heroes fought calmly on foot and threw enemy formations into confusion.

🌊 Kṛṣṇa Stops Śṛgāla Like a Shore Stops the Sea

Bhāgavata gives a beautiful comparison:

As Śṛgāla rushed forward in rage,

Kṛṣṇa stopped him just as the coastline restrains the ocean tide.

☠️ Śṛgāla Vāsudeva Killed

Then fierce duel begin hua between the two Vāsudevas.

But very quickly:

➡️ Lord Govinda cut off Śṛgāla’s crowned head.

🏃 Enemy Army Flees

Apne king ko dead dekhkar surviving soldiers panic mein every direction bhaag gaye.

👑 Kṛṣṇa Enters Karavīra

After victory:

Kṛṣṇa
Balarāma

entered Karavīra city.

Brāhmaṇas aur merchants ne unhe apne beloved lords ki tarah worship kiya.

💎 Seizure of the Royal Wealth

Finally Kṛṣṇa ordered Śṛgāla’s:

elephants
horses
soldiers
chariots
treasure
royal wealth

to be secured under guard."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 50(d)
    with st.expander("Chapter 50(d) - Kṛṣṇa Crowned: Jarāsandha’s Defeat"):
        text1 = """ 
        🏔️ Kṛṣṇa and Balarāma Ascend Mount Gomanta

Śrī Śuka continued,

Karavīra victory ke baad Kṛṣṇa aur Balarāma magnificent Mount Gomanta par ascend hue.

Bhāgavata mountain ki extraordinary beauty vividly describe karta hai:

towering trees
flowering creepers
waterfalls
cool crystal streams
dense shadows
joyful cuckoos singing
humming bees
monkeys leaping through branches"""
        create_image_text_layout(
            "attached_assets/chapter10/10.50d.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Mountain covered tha with:

Śāla
Tāla
Tamāla
Kadamba
Aśoka
Nimba
Punnāga
plantain groves

Entire landscape heavenly paradise jaisa appear ho raha tha.

🌧️ The Peak Called Pravarṣaṇa

Mountain par dono brothers specially ek famous summit par gaye:

Pravarṣaṇa Peak

Ye peak unique thi because:

➡️ clouds constantly rain karte rehte the there.

Kṛṣṇa aur Balarāma us peak se all directions survey karte hue peacefully enjoy karne lage.

🌊 The Crown of Viṣṇu is Stolen

Meanwhile another extraordinary event simultaneously ho raha tha.

Milk Ocean mein — jo Viṣṇu ka divine abode maana jata hai — mighty Daitya king Bali (son of Virocana) arrived.

There he stole:

the celestial crown of Lord Viṣṇu.

💎 Description of the Divine Crown

Bhāgavata crown ko unbelievably magnificent describe karta hai.

It was adorned with:

sapphires
Gomeda gems
rubies
pearls
corals
Puṣparāga stones
celestial gold

The crown blazed brilliantly like the Sun itself.

🦅 Garuḍa Pursues Bali

Jab crown theft ka pata chala, Garuḍa instantly Bali ke piche chase karne laga.

A terrible aerial battle hua.

Finally:

➡️ Garuḍa defeated Bali and recovered the crown.

👑 Kṛṣṇa is Crowned on Gomanta

Return journey ke dauraan Garuḍa suddenly Mount Gomanta par Kṛṣṇa ko seated dekhta hai beside Balarāma.

Immediately he understood:

“This is the Supreme Lord Himself.”

Then Garuḍa respectfully:

placed the celestial crown on Kṛṣṇa’s head
bowed at His feet
began offering prayers

🙏 Garuḍa Glorifies Kṛṣṇa

Garuḍa declared:

“I repeatedly bow to Lord Nārāyaṇa who has assumed human form for a divine mission.”

“You are the destroyer of the enemies of the gods.”

“You create the universe as Brahmā…”

“You preserve it as Viṣṇu…”

“And ultimately dissolve it through Śiva.”

He openly acknowledged:

“You are that same Supreme Viṣṇu now born in the Yadu race.”
🦅 Garuḍa Offers Service

Then Garuḍa humbly introduced himself:

“I am Garuḍa, son of Vinatā and your servant.”

“O Lord, command me what I should do.”

After saying this he knelt before Kṛṣṇa with folded palms.

🌸 Kṛṣṇa Blesses Garuḍa

Kṛṣṇa affectionately touched Garuḍa’s head with His hand.

Then lovingly said:

“You may go wherever you wish.”

“When I remember you, come immediately.”

Thus Garuḍa respectfully departed.

🌿 Life on Gomanta

Kṛṣṇa aur Balarāma some time tak Mount Gomanta par peacefully rahe.

They lived simply on:

fruits
roots
stream water

while enjoying mountain forests and natural beauty.

🏙️ Return to Karavīrapura

Eventually both brothers descended from the mountain and returned to Karavīrapura.

They remained there for:

four months.

Then with a large army they finally began journey back toward Mathurā.

😠 Jarāsandha Attacks Again

But hearing that Śṛgāla Vāsudeva had been killed…

Jarāsandha once again became furious.

He assembled another vast army and marched against Kṛṣṇa and Balarāma.

⚔️ Seven-Day War

This time intense battle continued for:

seven full days.

Again Jarāsandha’s gigantic forces suffered complete defeat.

🏃 Jarāsandha Flees Once More

After devastating losses:

➡️ Jarāsandha retreated back to Magadha with surviving Kṣatriyas.

Kṛṣṇa aur Balarāma victorious state mein Mathurā return hue while:

Sūtas
Māgadhas
bards

sang their heroic glories everywhere."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 51
    with st.expander("Chapter 51 - Mucukunda’s Eulogy of the Lord"):
        text1 = """ 
        🌙 Kālayavana Sees Kṛṣṇa

Śrī Śuka continued,

Jab Kālayavana ne Mathurā gates se Kṛṣṇa ko bahar aate dekha, woh instantly stunned ho gaya.

Bhāgavata beautifully Lord ka divine form describe karta hai:

dark cloud-like complexion
yellow silk garments
Śrīvatsa mark on chest
Kaustubha jewel shining on neck
four mighty arms
reddish lotus-like eyes
smiling moonlike face
makara-shaped earrings
Vanamālā garland"""
        create_image_text_layout(
            "attached_assets/chapter10/10.51.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Kṛṣṇa rising moon ki tarah appear ho rahe the.

🧠 Kālayavana Recognizes Him

Kālayavana immediately thought:

“This must be Vāsudeva Kṛṣṇa.”

Because Nārada previously usko Kṛṣṇa ke divine signs describe kar chuke the.

Lekin usne notice kiya:

Kṛṣṇa foot par chal rahe hain
unarmed appear ho rahe hain

So Kālayavana decided:

“Main bhi unarmed hi fight karunga.”

🏃 Kṛṣṇa Leads Him Away

Then strange event hua.

Instead of directly fighting…

Kṛṣṇa rapidly running start kar dete hain with Kālayavana chasing behind Him.

Bhāgavata says:

➡️ Lord deliberately appeared always “almost within reach,”

yet Kālayavana kabhi pakad nahi paaya.

⚠️ “Coward! Why Are You Running?”

While chasing, Kālayavana mocked:

“O Kṛṣṇa! Born in Yadu race hokar enemy se kyun bhaag rahe ho?”

Lekin despite insults:

➡️ he still could not catch the Lord.

Bhāgavata explains:

because his sinful karmas were not exhausted.

🕳️ The Mysterious Cave

Finally Kṛṣṇa entered a deep mountain cave.

Kālayavana bhi andar ghus gaya.

Inside cave usne ek sleeping man dekha.

👣 Kālayavana’s Fatal Mistake

Kālayavana foolishly assumed:

“Kṛṣṇa pretending to sleep after luring me here.”

Angrily usne sleeping person ko kick maar diya.

🔥 Mucukunda Burns Kālayavana

Sleeping king slowly awakened and opened his eyes.

The moment uski angry gaze Kālayavana par padi:

fire erupted from his body.

And instantly:

➡️ Kālayavana reduced to ashes.

👑 Who Was Mucukunda?

Parīkṣit curiously asked:

“Ye extraordinary king kaun tha?”

Śuka explained:

He was:

King Mucukunda

— son of mighty emperor Māndhātṛ from Ikṣvāku dynasty.

He was:

truthful
protector of Brahmaṇas
heroic warrior
⚔️ Protector of the Gods

Long ago devas Asuras se heavily oppressed ho rahe the.

Indra aur gods ne Mucukunda se help maangi.

For a very long time:

➡️ Mucukunda continuously protected the gods in celestial wars.

😔 Time Destroyed Everything

Eventually gods obtained Kārttikeya as their new commander.

Then they told Mucukunda:

“You may now rest.”

Lekin tragic truth reveal hua:

During his long absence:

his kingdom vanished
sons died
queens died
ministers died
relatives gone
entire generation destroyed by Time

⏳ The Power of Time

Gods explained:

“Time is stronger than the strongest.”

Just as cowherd cattle ko drive karta hai…

Time effortlessly all beings ko move aur destroy karta hai.

😴 Mucukunda Requests Sleep

Gods offered boon except mokṣa, because only Viṣṇu can grant liberation.

Exhausted Mucukunda requested:

“I only desire long uninterrupted sleep.”

Then another special boon mila:

“Whoever disturbs your sleep will instantly burn to ashes.”

Thus Mucukunda entered the cave and slept for ages.

✨ Kṛṣṇa Reveals Himself

After Kālayavana burned, Kṛṣṇa manifested before Mucukunda.

Mucukunda beheld:

dark blue cloud-like form
yellow silk garments
Kaustubha jewel
Śrīvatsa mark
Vanamālā garland
four arms
smiling compassionate face

Lord’s radiance entire cave ko illuminate kar rahi thi.

🙏 Mucukunda Questions the Lord

Overwhelmed by divine brilliance, Mucukunda respectfully asked:

“Who are You?”

“Are You:

Fire-god?
Sun-god?
Moon-god?
Indra?

or some supreme deity?”

Then he concluded:

“I believe You are Lord Viṣṇu Himself.”

🌌 Kṛṣṇa Explains His Incarnation

Kṛṣṇa replied:

“My incarnations, names and deeds are infinite.”

“No one can fully count them.”

Then He explained His present appearance:

“I have descended in Yadu dynasty as son of Vasudeva.”

“So people call Me Vāsudeva.”

⚔️ Slaying of Demons

Kṛṣṇa declared:

“I have slain:

Kaṃsa
Pralamba
other enemies of dharma.”

“This Yavana too was destroyed through your fiery glance.”

💛 “I Came Here for You”

Then Lord revealed something deeply beautiful:

“Long ago you repeatedly prayed to Me.”

“So out of affection for My devotee…”

“I personally came to this cave to bless you.”
🌸 Kṛṣṇa Offers Boons

Lord lovingly said:

“Ask whatever boon you desire.”

“No one who takes refuge in Me suffers misery again.”

😢 Mucukunda’s Great Realization

Hearing Lord’s words, Mucukunda became overwhelmed with devotion.

He realized:

“This is Nārāyaṇa Himself.”

Then he began offering profound philosophical prayers.

🕸️ Delusion of Material Life

Mucukunda lamented:

“Humans become deluded by Your māyā.”

Thinking family, wealth and worldly pleasures will bring happiness…

they actually enter deeper suffering.

🐄 “Like an Animal Falling Into a Well”

He gave powerful analogy:

Human birth extremely rare hai.

Yet person who ignores Lord’s feet is like:

an animal falling into a grass-covered well while seeking grass.
👑 Regret Over Kingship

Mucukunda confessed:

“My whole life wasted ho gaya.”

“I became intoxicated by:

kingdom
armies
power
wealth
wives
sons.”

He forgot the Lord completely.

☠️ The Horror of Time

He reflected:

Body once praised as:

“god among men”

eventually becomes:

ashes
worms
excrement for animals

Such is inevitable power of Time.

💔 Worldly Success Cannot Satisfy

Even kings who conquer the earth become slaves of:

desire
pride
sensual pleasure

Austerities and heavenly ambitions bhi true peace nahi dete.

🌟 Association with Saints Leads to Liberation

Mucukunda declared:

Only when liberation-time approaches…

person gains association with saints and turns toward God.

He recognized losing his kingdom itself as:

Kṛṣṇa’s hidden grace.
🙏 Mucukunda Rejects All Material Boons

Then he made his final prayer:

“I desire no worldly boon.”

“I only seek service to Your lotus feet.”

“What wise person would ask for temporary pleasures after attaining the Lord of Liberation?”

🌌 Complete Surrender

Mucukunda surrendered fully:

“I take refuge in You alone…”

“You who are:

beyond guṇas
pure consciousness
supreme reality
fearless refuge.”
💎 Kṛṣṇa Praises Mucukunda

The Lord replied lovingly:

“O emperor, your mind is pure and steady.”

“Even when tempted with boons, you were not distracted.”

Kṛṣṇa explained He had actually tested Mucukunda’s devotion.

🧘 True Devotion vs Mere Yoga

Lord said:

Non-devotees may externally control mind through yoga practices…

But hidden desires still remain inside them.

Whereas true devotees remain steady even amidst temptations.

🌿 Final Blessing

Finally Kṛṣṇa blessed him:

“Roam freely on Earth with mind fixed on Me.”

“Your devotion shall remain eternal.”

Then He instructed:

“As a Kṣatriya you accumulated violence through hunting and war.”

“So now perform austerities and meditation.”

🔱 Promise of Liberation

Kṛṣṇa concluded:

“In your next birth you will become a great Brāhmaṇa devoted to all beings…”
“And thereafter you shall attain Me completely.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 52
    with st.expander("Chapter 52 - Kṛṣṇa and Balarāma escape to Dvārakā"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.52.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 52(a)
    with st.expander("Chapter 52(a) - Kṛtavarmā Deputed to Hastināpura"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.52a.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 52(b)
    with st.expander("Chapter 52(b) - Balarāma marries Revatī"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.52b.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 53
    with st.expander("Chapter 53 - Rukmiṇī’s Marriage: Rukmiṇī carried away by Kṛṣṇa"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.53.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 54
    with st.expander("Chapter 54 - Celebration of Rukmiṇī’s Marriage"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.54.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 55
    with st.expander("Chapter 55 - The Story of Pradyumna’s Birth"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.55.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 56
    with st.expander("Chapter 56 - Kṛṣṇa’s marriage with Jāmbavatī and Satyabhāmā"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.56.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 57
    with st.expander("Chapter 57 - Murder of Satājit for Syamantaka"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.57.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 58
    with st.expander("Chapter 58 - Espousals of Lord Kṛṣṇa"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.58.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")
        
        # Chapter 59
    with st.expander("Chapter 59 - Narakāsura slain—The Pārijāta tree brought to Dvārakā"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.59.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 59(a)
    with st.expander("Chapter 59(a) - The Pārijāta Tree Taken by Śrī Kṛṣṇa"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.59a.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 59(b)
    with st.expander("Chapter 59(b) - Satyabhāmā defeats Gods"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.59b.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 59(c)
    with st.expander("Chapter 59(c) - Pārijāta planted in Satyabhāmā’s Palace"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.59c.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 60
    with st.expander("Chapter 60 - Conversation between Kṛṣṇa and Rukmiṇī (A Sweet Quarrel)"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.60.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 60(a)
    with st.expander("Chapter 60(a) - Slaying of Pauṇḍraka and others"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.60a.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 61
    with st.expander("Chapter 61 - Aniruddha s Marriage: Rukmī Slain"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.61.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 62
    with st.expander("Chapter 62 - Aniruddha taken captive by Bāṇāsura"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.62.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 63
    with st.expander("Chapter 63 - Bāṇa Vanquished—Aniruddha brought to Dvārakā"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.63.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 64
    with st.expander("Chapter 64 - The Story of Nṛga"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.64.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 65
    with st.expander("Chapter 65 - Balarāma’s Visit to Gokula—The Course of the Yamunā diverted"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.65.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 66
    with st.expander("Chapter 66 - Slaying of Pauṇḍraka and others"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.66.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 67
    with st.expander("Chapter 67 - Balarāma slays Dvivida"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.67.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 68
    with st.expander("Chapter 68 - Hastināpura dragged by Balarāma"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.68.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 69
    with st.expander("Chapter 69 - Śrī Kṛṣṇa’s Household Life"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.69.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 70
    with st.expander("Chapter 70 - Deputation from Captive Kings of Jarāsandha"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.70.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")
        
        # Chapter 71
    with st.expander("Chapter 71 - Śrī Kṛṣṇa’s visit to Indraprastha"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.71.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 72
    with st.expander("Chapter 72 - Jarāsandha slain"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.72.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 73
    with st.expander("Chapter 73 - Return of Kṛṣṇa and others to Indraprastha"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.73.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 74
    with st.expander("Chapter 74 - Yudhiṣṭhira’s Rājasūya: Śiśupāla slain"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.74.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 75
    with st.expander("Chapter 75 - Discomfiture of Duryodhana"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.75.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 76
    with st.expander("Chapter 76 - Fight with Śālva"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.76.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 77
    with st.expander("Chapter 77 - Slaying of King Śālva"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.77.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 78
    with st.expander("Chapter 78 - Dantavaktra and Vidūratha Slain: Balarāma’s Pilgrimage"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.78.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 79
    with st.expander("Chapter 79 - Balvala Killed: Balarāma’s Pilgrimage"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.79.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 80(a)
    with st.expander("Chapter 80(a) - The Story of the Brāhmaṇa Śrīdāman (introductory)"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.80a.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 80(b)
    with st.expander("Chapter 80(b) - The Story of the Brāhmaṇa Śrīdāman"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.80b.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 81
    with st.expander("Chapter 81 - The Story of the Parched Rice (The story of Śrīdāman continued)"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.81.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 82
    with st.expander("Chapter 82 - Meeting of Vṛṣṇis and Gopas of Vṛndāvana"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.82.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 83
    with st.expander("Chapter 83 - Narration of Their Marriage Episodes by Kṛṣṇa’s Consorts"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.83.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 84
    with st.expander("Chapter 84 - Vasudeva’s Sacrifice"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.84.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 85
    with st.expander("Chapter 85 - Restoration of his Elder Brothers by Kṛṣṇa (from the Realm of Death)"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.85.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 86
    with st.expander("Chapter 86 - Elopement of Subhadrā: The Lord’s Grace on Śrutadeva"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.86.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 87
    with st.expander("Chapter 87 - Śruti Gītā (Hyman of Praise by The Vedas)"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.87.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 88
    with st.expander("Chapter 88 - God Rudra Saved"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.88.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 89
    with st.expander("Chapter 89 - Restoration to Life of Brāhmaṇa’s Sons"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.89.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 90
    with st.expander("Chapter 90 - The Song of Queens: Resume of Kṛṣṇa’s Sports"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.90.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")
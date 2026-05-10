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
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.6.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7
    with st.expander("Chapter 7 - Destruction of the Cart and Tṛṇāvarta"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.7.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 8
    with st.expander("Chapter 8 - Kṛṣṇa’s Sports—Display of Viśvarūpa"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.8.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 9
    with st.expander("Chapter 9 - Grace upon the Gopī (Yaśodā) (Kṛṣṇa tied to the mortar)"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.9.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 10
    with st.expander("Chapter 10 - Uprooting of Arjuna Trees—Redemption of Nalakūbara and Maṇigrīva"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.10.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 11
    with st.expander("Chapter 11 - Exodus from Gokula—Destruction of demons Vatsa and Baka"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.11.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 12
    with st.expander("Chapter 12 - Slaying of Aghāsura"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.12.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 13
    with st.expander("Chapter 13 - Infatuation of God Brahmā"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.13.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 14
    with st.expander("Chapter 14 - God Brahmā eulogizes Kṛṣṇa"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.14.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 15
    with st.expander("Chapter 15 - Slaying the demon Dhenuka"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.15.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 16
    with st.expander("Chapter 16 - Expulsion of Kāliya"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.16.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 17
    with st.expander("Chapter 17 - Rescue from the Forest Conflagration"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.17.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 18
    with st.expander("Chapter 18 - Slaying of the Demon Pralamba"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.18.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 19
    with st.expander("Chapter 19 - Swallowing up of a Forest-conflagration"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.19.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 20
    with st.expander("Chapter 20 - Description of the Rainy Season and the Autumn"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.20.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")
        
        # Chapter 21
    with st.expander("Chapter 21 - The Song of Gopīs (cowherd-women)"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.21.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 22
    with st.expander("Chapter 22 - Cowherd-maids Pray to Kātyāyanī"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.22.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 23
    with st.expander("Chapter 23 - Spiritual Emancipation of the Wives of Brāhmaṇa Sacrificers"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.23.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 24
    with st.expander("Chapter 24 - Prevention of Sacrifice to Indra"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.24.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 25
    with st.expander("Chapter 25 - Lifting up of Mount Govardhana"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.25.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 26
    with st.expander("Chapter 26 - Conversation between Nanda and Cowherds"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.26.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 27
    with st.expander("Chapter 27 - Indra coronates Kṛṣṇa"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.27.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 28
    with st.expander("Chapter 28 - Nanda rescued from Varuṇa"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.28.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 29
    with st.expander("Chapter 29 - Lord Kṛṣṇa’s Rāsa with Gopīs"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.29.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 30
    with st.expander("Chapter 30 - Search after Kṛṣṇa"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.30.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 31
    with st.expander("Chapter 31 - Gopīs’ song (prayer for Kṛṣṇa’s return)"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.31.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 32
    with st.expander("Chapter 32 - Kṛṣṇa comforts Gopīs"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.32.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 33
    with st.expander("Chapter 33 - Description of Rāsa Krīḍā"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.33.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 34
    with st.expander("Chapter 34 - Sudarśana emancipated and slaying of Śaṅkhacūḍa"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.34.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 35
    with st.expander("Chapter 35 - Gopīs’ Song (in pairs of verses)"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.35.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 36
    with st.expander("Chapter 36 - Akrūra deputed to bring Kṛṣṇa and Balarāma to Mathurā"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.36.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 37
    with st.expander("Chapter 37 - Slaying of Asuras Keśin and Vyoma"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.37.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 38
    with st.expander("Chapter 38 - The Arrival of Akrūra to Gokula"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.38.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 39
    with st.expander("Chapter 39 - Akrūra returns with Kṛṣṇa and Balarāma"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.39.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 40
    with st.expander("Chapter 40 - Akrūra’s Hymn (in praise of the Lord)"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.40.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")
        
        
        # Chapter 41
    with st.expander("Chapter 41 - Kṛṣṇa’s Arrival at Mathurā"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.41.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 42
    with st.expander("Chapter 42 - Description of the Wrestling Arena"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.42.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 43
    with st.expander("Chapter 43 - Killing of the elephant Kuvalayāpīḍa"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.43.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 44
    with st.expander("Chapter 44 - Slaying of Kaṃsa"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.44.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 45
    with st.expander("Chapter 45 - Restoration of Preceptor Sāndīpani’s son"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.45.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 46
    with st.expander("Chapter 46 - Uddhava deputed for consoling Nanda"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.46.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 47
    with st.expander("Chapter 47 - Uddhava’s Discourse on the Real Nature of the Lord"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.47.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 48
    with st.expander("Chapter 48 - Visit to the Houses of Trivakrā and Akrūra"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.48.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 49
    with st.expander("Chapter 49 - Akrūra’s Mission to Hastinapura"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.49.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 50
    with st.expander("Chapter 50 - Settlement at the Fort of Dvārakā"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.50.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 50(a)
    with st.expander("Chapter 50(a) - Jarāsandha’s Second Expedition"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.50a.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 50(b)
    with st.expander("Chapter 50(b) - The Third Siege of Mathura: Jarāsandha’s defeat"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.50b.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 50(c)
    with st.expander("Chapter 50(c) - Conquest of Karvīrapura"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.50c.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 50(d)
    with st.expander("Chapter 50(d) - Kṛṣṇa Crowned: Jarāsandha’s Defeat"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.50d.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 51
    with st.expander("Chapter 51 - Mucukunda’s Eulogy of the Lord"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter10/10.51.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
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
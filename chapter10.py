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
Jarāsandha naam ka ek bahut powerful raja tha. Jarāsandha
Pehli haar ke baad bhi woh bahut gusse me tha. Din-raat uske mann me bas badla tha.

Teen mahine baad usne bahut saare rajaon ko bulaya. Sabne milkar ek bahut badi sena tayyar ki. Sena me haathi, ghode, rath aur lakhon sainik the.

Jarāsandha apni vishal sena ke saath Mathurā ki taraf chala. Mathura
Yamunā nadi ke paas usne apna camp lagaya. Yamuna River"""
        create_image_text_layout(
            "attached_assets/chapter10/10.50a.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
Raat ko sab log aaram kar rahe the. Kuch log geet gaa rahe the. Kuch so rahe the. Kisi ko andaza nahi tha ki kya hone wala hai.

Udhar Krishna ne sabhi Yādava veeron ke saath baithkar yudh ki planning ki. Unke saath Balarama, Uddhava aur Sātyaki bhi the.

Subah suraj nikalne se pehle, Kṛṣṇa ne apni sena ko teen hisson me baant diya.

Balarāma aur kuch veer left side se gaye.
Sātyaki aur doosre yoddha right side se gaye.
Aur khud Kṛṣṇa saamne se dushman ki sena me ghus gaye.

Us waqt Jarāsandha ki sena bilkul ready nahi thi.
Ghodo par saddle nahi the.
Haathiyon ne armour nahi pehna tha.
Sainik abhi so kar uthe bhi nahi the.

Tabhi achanak teen taraf se hamla hua.

Sab raja ghabra gaye. Kuch sainik bhaag gaye. Kuch ne jaldi se hathiyaar uthaye aur ladne lage.

Bahut bhayanak yudh hua.
Kṛṣṇa apne rath par akela hi bahut saare yoddhaon ko harane lage.
Balarāma ne bhi apni sena ke saath dushman ko peeche dhakel diya.
Sātyaki ne bhi zor se hamla kiya.

Thodi hi der me Jarāsandha ki sena toot gayi. Dar kar sab alag-alag disha me bhaagne lage.

Sātyaki ne bhaagte hue sainikon ka kaafi door tak peecha kiya aur vijay paakar wapas aaye.

Kṛṣṇa ne bahut saare haathi, rath, ghode aur dhan-daulat jeet li.
Sundar mukut, sone ke gehne aur mehange vastra bhi mile.

Balarāma ne bhi dushman ka khazana aur anya saamaan jeet kar laaya.
Phir sab dhan Yādavo ke raja Ugrasena ko de diya gaya.

Is tarah Kṛṣṇa aur Balarāma ne buddhi aur sahas se Jarāsandha ki doosri sena ko bhi hara diya.
Moral yeh hai ki sirf badi sena se jeet nahi milti, samajhdari aur sahi planning bhi bahut zaroori hoti hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 50(b)
    with st.expander("Chapter 50(b) - The Third Siege of Mathura: Jarāsandha’s defeat"):
        text1 = """ 
Jarāsandha fir se haar gaya tha. Jarāsandha
Uska gussa aur badh gaya.

Is baar woh madad maangne gaya apne dost Bāṇa ke paas. Bana
Bāṇa ek bahut shaktishaali raja tha jiske hazaar haath the.

Jab Bāṇa ko pata chala ki uska dost aa raha hai, toh usne bahut grand welcome kiya.
Haathi sajaye gaye.
Ghode aur rath taiyaar the.
Dhol baj rahe the.
Har taraf jhande aur deepak chamak rahe the."""
        create_image_text_layout(
            "attached_assets/chapter10/10.50b.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
Dono dost ek dusre se mile aur baithkar baat karne lage.

Jarāsandha bola,
“Krishna ne achanak hamla karke meri sena ko hara diya. Mere haathi, ghode aur rath sab loot liye gaye. Mujhe tumhari madad chahiye.”

Yeh sunkar Bāṇa ne turant madad dene ka wada kiya.

Usne Jarāsandha ko hazaaron haathi, lakhon ghode aur bahut bade sainik diye.
Saath hi kuch powerful dānava yoddha bhi bheje jo māyā aur jadui yudh me expert the.

Phir Jarāsandha apni aur bhi badi sena lekar Mathurā pahunch gaya. Mathura

Usne shehar ko charo taraf se gher liya.
Deeware todne ke liye bade-bade hathiyaar use kiye gaye.

Jab Krishna aur Balarama ko yeh pata chala, toh dono gusse me aa gaye.

Turant yudh ke nagade bajne lage.

Sātyaki, Kṛtavarmā aur doosre Yādava veer bhi sena ke saath taiyaar ho gaye.

Kṛṣṇa aur Balarāma do sher ki tarah yudh bhoomi me nikle.

Bahar aate hi Kṛṣṇa ne apna shankh Pāñcajanya zor se bajaya.
Uski awaaz sunkar dushman ki sena darr gayi.

Phir bhayanak yudh shuru hua.

Bāṇa ke dānava jadui māyā se ladne lage.
Kabhi ajeeb cheeze dikhate, kabhi sainikon ko confuse karte.

Lekin Kṛṣṇa ne apni divya shakti se ek pal me sab māyā khatam kar di.

Phir unhone Sātyaki aur Kṛtavarmā ko kaha,
“Tum dono in dānavo se ladho.”

Dono veer turant yudh me kud pade.

Udhar Kṛṣṇa akela hi bahut saare rajaon se lad rahe the.
Unke teer bijli ki tarah chal rahe the.

Haathi girne lage.
Ghode aur rath tootne lage.
Yudh bhoomi puri tarah hil gayi.

Tab Jarāsandha khud gusse me bhar kar Balarāma ke saamne aaya.

Usne challenge diya,
“Aao Balarāma! Apni taakat dikhao!”

Balarāma bhi gusse me aa gaye.
Unhone apna bhayanak gadā uthaya aur sher ki tarah garje.

Dono ke beech zabardast gadā-yudh hua.

Kabhi Jarāsandha hamla karta.
Kabhi Balarāma use zor se dhakka dete.
Kabhi dono zameen par gir jaate aur fir uthkar ladne lagte.

Dono ki takkar do pagal haathiyon jaisi lag rahi thi.

Itni zor ki ladai hui ki aas-paas ke ped aur pathar bhi toot gaye.

Dusri taraf Sātyaki ne dānava Kumbhāṇḍa ko teeron se buri tarah ghayal kar diya.
Dānava behosh hokar gir gaya.

Yeh dekhkar doosra dānava Kūpakarṇa darr gaya aur battlefield chhodkar bhaag gaya.

Dono dānava apni bachi hui sena ke saath wapas Śoṇitapura laut gaye. Sonitapura

Is tarah fir se Jarāsandha ki sena toot gayi.

Moral yeh hai ki ghamand aur buri niyat zyada der tak nahi tikti. Sachchi shakti buddhi, himmat aur dharma me hoti hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 50(c)
    with st.expander("Chapter 50(c) - Conquest of Karvīrapura"):
        text1 = """ 
Yudh bahut bhayanak ho chuka tha.
Jarāsandha ki sena tootne lagi.
Bāṇa ke dānava sainik bhi battlefield chhodkar bhaag gaye.

Yeh dekhkar sab raja dar gaye aur unka hausla toot gaya.

Balarama ko laga ki ab jeet pakki hai.
Woh gusse me Jarāsandha ke paas pahunch gaye.

Unhone Jarāsandha ke baal pakad liye aur apne bhayanak gadā se use maarne wale the."""
        create_image_text_layout(
            "attached_assets/chapter10/10.50c.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
Tabhi aasman se ek zor ki awaaz aayi,
“Balarāma, Jarāsandha ki mrityu tumhare haath se nahi hogi. Use chhod do.”

Yeh sunkar Balarāma ruk gaye.
Unhone Jarāsandha ko chhod diya aur apne rath par wapas laut aaye.

Jarāsandha sharminda ho gaya.
Sir jhukakar woh apni bachi hui sena ke saath wapas apne rajya chala gaya.

Udhar Krishna ne dushman sena par teeron ki baarish kar di.
Bahut saare raja bhaag gaye.

Jab Kṛṣṇa aur Balarāma Mathurā laut kar aaye, toh poore shehar me khushi chha gayi. Mathura

Logon ne phool barsaye.
Mahilaye mahal ki chhaton se unka swagat karne lagi.
Sab log unki jai-jai kar kar rahe the.

Baad me Kṛṣṇa aur Balarāma ne socha ki woh dakshin taraf jaakar prasiddh Gomanta parvat dekhenge. Gomanta

Dono bhai safar par nikal pade.
Raaste me unhone nadiyan, pahaad aur jungle dekhe.

Ek din jungle me unhe ek mahaan rishi dikhe.
Unke baal jataon me the.
Woh ped ke neeche shaant baithkar tapasya kar rahe the.

Woh aur koi nahi, balki Parashurama the.

Kṛṣṇa aur Balarāma ne unhe pranām kiya.

Kṛṣṇa bole,
“Hey Mahārishi, hum Gomanta parvat dekhna chahte hain.”

Paraśurāma muskuraaye aur bole,
“Tum dono aam log nahi ho. Main tumhari asli shakti jaanta hoon.”

Phir unhone kaha,
“Gomanta ke paas Karavīra naam ka ek shehar hai. Wahan Śṛgāla Vāsudeva naam ka ghamandi raja rehta hai. Woh tumhe nahi rokega. Pehle use harana hoga.”

Yeh sunkar dono bhai aage badhe.

Jald hi unhone sundar Karavīra nagari dekhi. Karavirapura
Shehar ke bade dwar aur unche mahal bahut sundar lag rahe the.

Tab Kṛṣṇa ne apna shankh zor se bajaya.

Shankh ki awaaz sunkar Śṛgāla Vāsudeva bahut gusse me aa gaya.
Woh apni badi sena lekar hamla karne aa gaya.

Usne teeron ki tez baarish kar di.
Lekin Kṛṣṇa aur Balarāma bina dare ladte rahe.

Yudh aur bhi tez ho gaya.

Ant me Kṛṣṇa ne ek shaktishaali vaar kiya aur Śṛgāla Vāsudeva ka sir kaat diya.

Apne raja ko marte dekhkar uski sena darr kar bhaag gayi.

Phir Kṛṣṇa aur Balarāma Karavīra shehar me pravesh kiye.
Wahan ke logon ne unka bahut samman kiya.

Kṛṣṇa ne shehar ka dhan, haathi, ghode aur khazana sambhal liya aur sab kuch surakshit kar diya.

Is tarah dono bhaiyon ne apni buddhi, himmat aur dharma se ek aur dusht raja ko hara diya.

Moral yeh hai ki sachchai aur dharma ke saamne ghamand zyada der tak nahi tikta."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 50(d)
    with st.expander("Chapter 50(d) - Kṛṣṇa Crowned: Jarāsandha’s Defeat"):
        text1 = """ 
Krishna aur Balarama Gomanta parvat par chadh gaye. Gomanta

Woh pahaad bahut sundar tha.
Har taraf bade-bade ped the.
Jharnon ka thanda paani beh raha tha.
Pakshi gaane gaa rahe the.
Bandar pedon par kood rahe the.
Madhumakkhiyan gun-guna rahi thi.

Dono bhai prakriti ka anand lene lage."""
        create_image_text_layout(
            "attached_assets/chapter10/10.50d.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
Parvat ke sabse upar ek jagah thi jiska naam Pravarṣaṇa tha.
Wahan hamesha baarish hoti rehti thi.

Kṛṣṇa aur Balarāma wahan kuch samay shaanti se rahe.
Woh phal, jad aur pahaadi paani se apna jeevan chala rahe the.

Isi beech ek ajeeb ghatna hui.

Samudra ke paas ek bahut keemti divya mukut tha jo Bhagavān Viṣṇu ka mana jata tha. Vishnu
Woh mukut heere-moti aur neele ratno se chamak raha tha.

Ek dānava raja Bali us mukut ko lekar bhaag gaya. Mahabali

Yeh dekhkar Garuda turant uske peeche uda.

Garuḍa ne us dānava ko yudh me hara diya aur mukut wapas le liya.

Wapas aate waqt usne Gomanta parvat par Kṛṣṇa ko dekha.

Garuḍa samajh gaya ki Kṛṣṇa koi aam vyakti nahi hain.
Woh Bhagavān Nārāyaṇa ka hi roop hain.

Bahut shraddha se Garuḍa ne woh divya mukut Kṛṣṇa ke sir par rakh diya.

Phir woh jhukkar bola,
“Hey Prabhu, aap sabke rakshak hain. Main aapka sevak hoon.”

Kṛṣṇa muskuraaye aur pyar se Garuḍa ke sir par haath rakha.

Unhone kaha,
“Jab bhi mujhe zarurat hogi, tum aa jana.”

Garuḍa pranām karke wahan se chale gaye.

Kuch samay baad Kṛṣṇa aur Balarāma Gomanta se neeche utar kar Karavīrapura aaye. Karavirapura

Wahan woh chaar mahine tak rahe.
Phir ek badi sena ke saath Mathurā lautne lage. Mathura

Lekin jab Jarāsandha ko pata chala ki Śṛgāla mar gaya hai, toh woh fir se gusse me aa gaya.

Is baar bhi woh bahut badi sena lekar aa gaya.

Phir se bhayanak yudh hua.

Saat din tak lagataar ladai chalti rahi.
Kṛṣṇa aur Balarāma bahaduri se ladte rahe.

Aakhir me Jarāsandha fir haar gaya.
Uski sena toot gayi aur woh sharminda hokar Magadha wapas chala gaya.

Kṛṣṇa aur Balarāma vijay paakar Mathurā laut aaye.
Log unki jai-jai karne lage.
Sab taraf khushi aur utsav ka mahaul tha.

Is tarah dharma aur sachchai ne ek baar fir ahankaar ko hara diya.

Moral yeh hai ki jo vyakti dharma aur sachchai ke saath chalta hai, ant me jeet usi ki hoti hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 51
    with st.expander("Chapter 51 - Mucukunda’s Eulogy of the Lord"):
        text1 = """ 
Ek din Kalayavana naam ka ek bahut khatarnak Yavana raja Mathurā par hamla karne aaya. Mathura

Jab usne Krishna ko dekha, toh woh hairaan reh gaya.

Kṛṣṇa ka roop bahut sundar tha.
Unhone peele vastra pehne the.
Unke gale me chamakta hua Kaustubha mani tha.
Unke chehre par pyari muskaan thi.

Kālayavana samajh gaya,
“Yeh zaroor Vāsudeva Kṛṣṇa hi hain.”"""
        create_image_text_layout(
            "attached_assets/chapter10/10.51.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Woh bina hathiyaar ke Kṛṣṇa ke peeche bhaagne laga.

Lekin Kṛṣṇa usse pakadne nahi de rahe the.
Woh use dheere-dheere ek door pahaadi gufa ki taraf le gaye.

Kālayavana gusse me chillaya,
“Yādava hoke tum bhaag kyun rahe ho?”

Lekin Kṛṣṇa chup-chaap gufa me chale gaye.

Andar ek aadmi gehri neend me so raha tha.

Kālayavana ne socha,
“Kṛṣṇa mujhse bachne ke liye sone ka natak kar rahe hain.”

Gusse me usne soye hue vyakti ko pair se laat maar di.

Jaise hi woh vyakti utha, usne aankhen kholi aur Kālayavana ki taraf dekha.

Uski aankhon me itni tej agni thi ki Kālayavana turant jal kar raakh ban gaya.

Woh soya hua vyakti tha Mucukunda.

Raja Mucukunda bahut purane samay ke mahaan raja the.
Woh sachche, bahadur aur dharmic the.

Kabhi devtaon ne unse madad maangi thi kyunki dānava unhe pareshan kar rahe the.
Mucukunda ne bahut saalon tak devtaon ki raksha ki.

Lekin itni lambi ladai ke baad woh bahut thak gaye the.

Tab devtaon ne unhe ek vardaan diya,
“Tum aaraam se so sakte ho. Jo bhi tumhari neend todhega, woh turant jal kar bhasm ho jayega.”

Isliye Mucukunda us gufa me gehri neend so rahe the.

Kālayavana ke jalne ke baad Kṛṣṇa unke saamne aaye.

Mucukunda ne Kṛṣṇa ko dekha aur hairaan reh gaye.
Unhone itna divya aur shant roop pehle kabhi nahi dekha tha.

Woh bole,
“Aap kaun hain? Aapka tej suraj jaisa chamak raha hai.”

Tab Kṛṣṇa ne muskuraakar kaha,
“Mere roop aur janm anek hain. Main Yadu vansh me Vāsudeva ke ghar janma hoon. Log mujhe Vāsudeva Kṛṣṇa kehte hain.”

Mucukunda samajh gaye ki yeh koi aam vyakti nahi, swayam Bhagavān Nārāyaṇa hain. Narayana

Woh bahut vinamr hokar bole,
“Prabhu, duniya ke log dhan, rajya aur sukh ke peeche bhaagte rehte hain. Lekin yeh sab ek din khatam ho jata hai.”

“Main bhi kabhi apne rajya aur shakti par garv karta tha. Lekin ab samajh aaya ki asli shanti sirf aapki bhakti me hai.”

“Main aapse koi dhan ya rajya nahi maangta. Mujhe sirf aapke charno ki seva chahiye.”

Kṛṣṇa unki baat sunkar bahut prasann hue.

Unhone kaha,
“Mucukunda, tumhara mann ab pavitra ho gaya hai. Tumhari bhakti kabhi kam nahi hogi.”

“Agale janm me tum ek gyani Brāhmaṇa banoge aur ant me mujhe prapt karoge.”

Mucukunda ne khushi se Kṛṣṇa ko pranām kiya.

Is tarah Raja Mucukunda ko samajh aa gaya ki duniya ki shakti aur dhan temporary hote hain, lekin Bhagavān ki bhakti hamesha saath rehti hai.

Moral yeh hai ki asli sukh dhan aur shakti me nahi, vinamrata, bhakti aur sachchai me hota hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 52
    with st.expander("Chapter 52 - Kṛṣṇa and Balarāma escape to Dvārakā"):
        text1 = """ 
        Mucukunda ko aashirvaad dene ke baad Krishna wapas Mathurā laut aaye. Mathura

Wahan Yavana sena ab bhi maujood thi.
Kṛṣṇa ne unhe hara diya aur unka dhan le kar Dvārakā bhejne lage. Dvaraka

Lekin tabhi Jarāsandha fir se bahut badi sena lekar aa gaya."""
        create_image_text_layout(
            "attached_assets/chapter10/10.52.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Usne Kṛṣṇa aur Balarama ko charo taraf se gher liya.

Bahut bhayanak yudh hua.
Kṛṣṇa ne ped ukhaad kar haathiyon aur rathon ko gira diya.
Balarāma ne apni taakat se dushman sena ko hila diya.

Lekin Jarāsandha ki sena bahut zyada thi.

Tab Kṛṣṇa aur Balarāma ne ek alag yojana banayi.
Woh aam insaanon ki tarah battlefield se bhaagne lage.

Jarāsandha unhe dekhkar zor-zor se hasne laga.
Usne socha,
“Ab ye dono dar gaye hain!”

Lekin asal me Kṛṣṇa kuch aur hi soch rahe the.

Dono bhai door bhaagte hue Gomanta parvat pahunch gaye. Gomanta

Wahan woh pahaad ke sabse upar chadh gaye.

Jarāsandha bhi apni sena ke saath wahan pahunch gaya.
Usne poore pahaad ko gher liya.

Bahut saare raja bhi uske saath the.
Sabne milkar pahaad ke ped kaat diye aur charo taraf aag laga di.

Aag bahut tez jalne lagi.
Sabko laga Kṛṣṇa aur Balarāma ab bach nahi payenge.

Lekin dono bhai chupke se pahaad ki unchai se neeche kood gaye aur surakshit bahar nikal aaye.

Kisi ko pata bhi nahi chala.

Phir dono seedhe Dvārakā laut gaye.
Jarāsandha ko laga ki dono jal kar mar gaye hain.

Khush hokar woh apni sena ke saath wapas chala gaya.

Dvārakā me sab log Kṛṣṇa aur Balarāma ko dekhkar bahut khush hue.

Kuch samay baad Balarama ka vivaah Revatī se hua. Revati

Aur phir ek bahut sundar rajkumari ki kahani shuru hui — Rukmini ki.

Vidarbha desh ke raja Bhīṣmaka ki ek sundar aur gunvān beti thi Rukmiṇī. Vidarbha

Woh jab bhi Kṛṣṇa ki bahaduri aur sundarta ki kahani sunti, unhe mann hi mann apna pati maan leti.

Udhar Kṛṣṇa ko bhi lagta tha ki Rukmiṇī ek uttam patni banengi.

Lekin Rukmiṇī ka bhai Rukmi Kṛṣṇa se nafrat karta tha.
Woh chahta tha ki Rukmiṇī ki shaadi Shishupala se ho.

Yeh sunkar Rukmiṇī bahut dukhi ho gayi.

Unhone chupke se ek vishwas-patra Brāhmaṇa ko Kṛṣṇa ke paas bheja.

Woh Brāhmaṇa Dvārakā pahunch gaya.

Kṛṣṇa ne uska bahut samman kiya.
Unhe baithne ko jagah di, bhojan karvaya aur pyar se poocha,
“Aap kis kaam se aaye hain?”

Tab Brāhmaṇa ne Rukmiṇī ka sandesh diya.

Rukmiṇī ne apne patra me likha tha,
“Hey Kṛṣṇa, aap duniya ke sabse uttam purush hain. Main aapko hi apna pati maan chuki hoon.”

“Agar aap mujhe nahi le gaye, toh meri shaadi zabardasti Śiśupāla se kar di jayegi.”

“Kripya vivaah ke din aakar mujhe apne saath le jaiye.”

“Main mandir jaane wali hoon. Wahi se mujhe apne saath le jaiye.”

Patra ke antim shabdon me Rukmiṇī ne likha,
“Agar mujhe aapka saath nahi mila, toh main jeena nahi chahungi.”

Kṛṣṇa ne poora patra dhyan se padha.
Unke chehre par halki si muskaan aa gayi.

Ab ek nayi aur romanchak kahani shuru hone wali thi."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 52(a)
    with st.expander("Chapter 52(a) - Kṛtavarmā Deputed to Hastināpura"):
        text1 = """ 
        Ek din Krishna Dvārakā ki rajsabha me baithe the. Dvaraka
Unke saath Balarama aur Satyaki bhi the.

Bahut saare raja aur Brāhmaṇa wahan maujood the.

Tab kuch Brāhmaṇon ne ek khabar sunayi."""
        create_image_text_layout(
            "attached_assets/chapter10/10.52a.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Unhone bataya ki Drupada, jo Pāñcāla desh ke raja the, unhe Kuntī ke putron ne yudh me hara diya tha. Kunti

Yeh sunkar Kṛṣṇa ke chehre par khushi aa gayi.
Unhe Pāṇḍavo ki bahaduri par garv hua.

Phir unhone Kritavarma ko Hastināpura bheja taaki woh poori sachchai jaan sake. Hastinapur

Kṛtavarmā Hastināpura pahunch gaye.

Wahan unhone sabse pehle buzurg aur gyani Bhishma ko pranām kiya.
Saath hi Drona, Vidura, Dhritarashtra aur Kripa se bhi mile.

Uske baad woh Yudhishthira aur unke chaaron bhaiyon se mile.
Kuntī ko bhi unhone bahut samman diya.

Yudhiṣṭhira ne pyar se poocha,
“Kṛṣṇa kaise hain? Dvārakā me sab theek hai?”

Phir unhone Kālayavana ki haar, Jarāsandha par vijay aur Karavīrapura ki ghatnaon ke baare me bhi poocha.

Kṛtavarmā ne sab kahani detail me sunayi.

Yeh sab sunkar Yudhiṣṭhira bahut prasann hue.
Unhe laga ki dharma aur satya ki shakti badh rahi hai.

Pāṇḍavo aur Kuntī ne Kṛtavarmā ka bahut adar-satkar kiya.
Sabne milkar unse pyar aur apnapan se baat ki.

Kuntī ki aankhon me apne rishtedaron ko yaad karke aansu aa gaye.

Kuch samay baad Kṛtavarmā ne sabse vida li.
Unhone Bhīṣma, Dhṛtarāṣṭra, Vidura, Karna, Ashwatthama aur Duryodhana ko pranām kiya.

Phir woh shaam ke samay Dvārakā laut aaye.

Rajsabha me jaakar unhone Kṛṣṇa ko sab kuch bata diya jo unhone dekha aur suna tha.

Jab Kṛṣṇa ne Pāṇḍavo ki bahaduri aur safalta ke baare me suna, toh woh bahut khush hue.

Unhe pata tha ki aage chal kar Pāṇḍav dharma ka saath denge aur duniya me nyaay ki raksha karenge.

Moral yeh hai ki sachche aur dharmic log hamesha ek dusre ka samman karte hain aur khushi baantte hain."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 52(b)
    with st.expander("Chapter 52(b) - Balarāma marries Revatī"):
        text1 = """ 
        Raja Parīkṣit ne ek din poocha,
“Hey Maharishi, mujhe batayiye ki Revata kaun the aur unki beti Revatī ki shaadi Balarama se kaise hui?”

Tab Śuka Muni ne kahani sunani shuru ki.

Bahut purane samay me Revata naam ke ek buddhimaan aur dharmic raja the.
Unki ek bahut sundar beti thi jiska naam Revati tha.

Revatī itni sundar aur gunvān thi ki bahut saare raja usse shaadi karna chahte the."""
        create_image_text_layout(
            "attached_assets/chapter10/10.52b.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Lekin Raja Revata confuse the.
Unhe samajh nahi aa raha tha ki apni beti ki shaadi kis se karayein.

Isliye woh seedhe Brahma ke paas salah lene chale gaye.

Jab woh Brahmā ji ke lok me pahuche, tab wahan do Gandharva — Hāhā aur Hūhū — madhur sangeet gaa rahe the.

Raja Revata chup-chaap baithkar unka sangeet sunne lage.

Thodi der baad jab sangeet khatam hua, tab unhone Brahmā ji ko pranām kiya aur bole,
“Prabhu, meri beti ke liye sabse accha var kaun hoga?”

Brahmā ji muskuraaye aur poocha,
“Tum kin-kin rajaon ko pasand karte ho?”

Raja Revata ne bahut saare rajaon ke naam bataye.

Yeh sunkar Brahmā ji hans pade.

Woh bole,
“Raja, jab tak tum yahan sangeet sun rahe the, tab tak prithvi par bahut saare yug beet gaye.”

“Jin rajaon ke naam tum le rahe ho, woh sab kab ke ja chuke.”

Raja Revata hairaan reh gaye.

Phir Brahmā ji bole,
“Ab prithvi par Krishna aur Balarāma janm le chuke hain.”

“Tum apni beti Revatī ki shaadi Balarāma se kar do.”

Raja Revata ne khushi se Brahmā ji ko pranām kiya aur wapas laut aaye.

Phir unhone Revatī ka vivaah Balarāma se kar diya.

Lekin ek choti si baat thi.

Revatī bahut purane yug me janmi thi, isliye unki height aur sharir us samay ke logon ke hisaab se bahut bada tha.

Balarāma ne pyar se apna hal unke kandhe par rakha aur unki height ko apne barabar kar diya.

Iske baad dono ka vivaah bahut khushi se hua.

Sab log bahut prasann hue.

Is tarah Revatī aur Balarāma ek pavitra aur sundar jodi ban gaye.

Moral yeh hai ki sahi samay aur sahi margdarshan se hi jeevan ke bade faisle safal hote hain."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 53
    with st.expander("Chapter 53 - Rukmiṇī’s Marriage: Rukmiṇī carried away by Kṛṣṇa"):
        text1 = """ 
        Jab Krishna ne Rukmini ka sandesh suna, toh woh muskura diye.

Unhone Brāhmaṇa ka haath pakadkar kaha,
“Jaise Rukmiṇī ne apna mann mujhpar laga diya hai, waise hi maine bhi use apne hriday me basa liya hai.”

“Kuch raaton se mujhe bhi neend nahi aa rahi.”

Kṛṣṇa samajh gaye the ki Rukmiṇī ka bhai Rukmi hi shaadi me rukawat daal raha hai.

Phir Kṛṣṇa ne turant apne saarathi Dāruka ko rath taiyaar karne ko kaha."""
        create_image_text_layout(
            "attached_assets/chapter10/10.53.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Jaldi hi sundar ghodon se juda hua rath taiyaar ho gaya.

Kṛṣṇa Brāhmaṇa ko saath lekar raat bhar me hi Vidarbha pahunch gaye. Vidarbha

Udhar Kuṇḍina nagari me shaadi ki taiyariyan zor-shor se chal rahi thi. Kundinapura

Sadkon par paani chhidka gaya tha.
Har taraf rang-birange jhande aur phool lage the.
Log naye kapde pehne hue the.

Rukmiṇī ko sundar vastra aur gehno se sajaya gaya.

Lekin uske mann me sirf Kṛṣṇa the.

Woh baar-baar soch rahi thi,
“Kya Kṛṣṇa sach me aayenge?”

“Ya shayad unhe mujh me koi kami lag gayi?”

Yeh sochkar uski aankhon me aansu aa gaye.

Lekin tabhi uska baaya haath aur aankh halki si phadki.
Yeh ek shubh sanket tha.

Thodi der baad wahi Brāhmaṇa wapas aaya.

Uske chehre ki khushi dekhkar hi Rukmiṇī samajh gayi ki Kṛṣṇa aa chuke hain.

Brāhmaṇa ne muskuraakar kaha,
“Kṛṣṇa Vidarbha pahunch gaye hain. Woh apna vachan zaroor nibhayenge.”

Yeh sunkar Rukmiṇī bahut khush ho gayi.

Udhar Shishupala bhi apni sena ke saath shaadi ke liye aa gaya tha.

Uske saath Jarāsandha aur bahut saare raja bhi aaye the.

Sabne milkar faisla kiya,
“Agar Kṛṣṇa Rukmiṇī ko le jaane aaye, toh hum sab milkar unse ladenge.”

Yeh sunkar Balarama bhi badi sena lekar wahan pahunch gaye taaki Kṛṣṇa ki madad kar sakein.

Shaadi se pehle Rukmiṇī mandir me Devi Ambikā ki pooja karne gayi. Parvati

Uske saath sainik, saheliyan aur bahut si mahilaye thi.
Dhol aur shankh baj rahe the.

Mandir me jaakar Rukmiṇī ne aankhen band karke prarthana ki,
“Hey Mata, bas Kṛṣṇa hi mere pati banein.”

Pooja ke baad jab woh mandir se bahar nikli, toh sab raja use dekhkar hairaan reh gaye.

Rukmiṇī bahut sundar lag rahi thi.
Uski chal hans ki tarah komal thi.
Uske chehre par pyari si muskaan thi.

Bahut se raja use dekhkar apne hosh kho baithe.

Lekin Rukmiṇī ki nazar sirf ek vyakti ko dhoondh rahi thi — Kṛṣṇa ko.

Aur tab usne Kṛṣṇa ko dekha.

Agla pal sabke liye chaukane wala tha.

Kṛṣṇa seedhe aage badhe, Rukmiṇī ko pyar se apne rath par bithaya aur sab rajaon ke saamne use lekar chal diye.

Yeh sab itni jaldi hua ki koi kuch samajh hi nahi paya.

Kṛṣṇa sher ki tarah apni priya ko lekar nikal gaye, aur baaki raja bas dekhte reh gaye.

Yeh dekhkar Jarāsandha aur doosre raja gusse se bhar gaye.

Woh chillaye,
“Ek gwala hamare saamne se rajkumari ko le gaya!”

Aur phir ek naya yudh shuru hone wala tha."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 54
    with st.expander("Chapter 54 - Celebration of Rukmiṇī’s Marriage"):
        text1 = """ 
        Jab Krishna Rukmini ko apne rath me bithakar le gaye, tab sab raja gusse se bhar gaye.

Sabne apne kavach pehne aur sena ke saath Kṛṣṇa ka peecha karne lage.

Udhar Yādava sena bhi taiyaar khadi thi.
Balarama, Gaḍa aur doosre veer dhanush lekar saamne aa gaye."""
        create_image_text_layout(
            "attached_assets/chapter10/10.54.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Bahut bhayanak yudh shuru hua.

Dushman sena teeron ki baarish karne lagi.
Haathi, ghode aur rath zor se daudne lage.

Rukmiṇī yeh sab dekhkar thodi dar gayi.
Usne chup-chaap Kṛṣṇa ki taraf dekha.

Kṛṣṇa muskuraaye aur bole,
“Dar mat. Hamari sena jaldi hi sabko hara degi.”

Phir Yādava veeron ne zabardast hamla kiya.
Bahut saare rath toot gaye.
Haathi aur ghode girne lage.

Jarāsandha aur doosre raja haar kar battlefield se bhaag gaye.

Sab raja udaas Shishupala ke paas gaye aur use samjhane lage,
“Jeet aur haar hamesha badalte rehte hain. Dukhi mat ho.”

Lekin Rukmi ka gussa abhi bhi shaant nahi hua tha.

Woh apni sena lekar akela hi Kṛṣṇa ke peeche bhaaga.

Usne kasam khai,
“Jab tak main Kṛṣṇa ko hara kar apni behen ko wapas nahi laata, tab tak Kuṇḍina nahi lautunga.” Kundinapura

Rukmī ne Kṛṣṇa ko Narmadā nadi ke paas pakad liya. Narmada River

Woh chillaya,
“Ruko Kṛṣṇa! Aaj main tumhara ghamand tod dunga!”

Usne teer chala diye.

Lekin Kṛṣṇa shaant rahe.
Unhone aasani se Rukmī ka dhanush tod diya.

Rukmī baar-baar naye hathiyaar uthata, aur Kṛṣṇa unhe turant tod dete.

Aakhir me Rukmī talwar lekar seedha Kṛṣṇa par toot pada.

Kṛṣṇa ne uski talwar bhi tod di aur khud apni talwar lekar uski taraf badhe.

Rukmiṇī yeh dekhkar bahut darr gayi.

Woh turant Kṛṣṇa ke charno me gir padi aur boli,
“Prabhu, mere bhai ko mat maariye.”

Rukmiṇī ka dukh dekhkar Kṛṣṇa ka hriday pighal gaya.

Unhone Rukmī ko jeevit chhod diya.
Lekin saza ke roop me uske baal aur mooch ajeeb tarah se kaat diye.

Tabhi Balarāma wahan aaye.

Unhone Rukmī ki haalat dekhi aur Kṛṣṇa se bole,
“Rishta chahe jaisa bhi ho, apno ko itna apmaanit nahi karna chahiye.”

Phir unhone Rukmiṇī ko samjhaya,
“Dukh aur sukh insaan ko apne karmon se milte hain.”

“Is duniya me sharir alag-alag lagte hain, lekin sabke andar ek hi ātmā hai.”

Balarāma ki baatein sunkar Rukmiṇī ka mann shaant ho gaya.

Rukmī sharminda tha.
Usne wapas Kuṇḍina na jaakar ek naya shehar basaya jiska naam Bhojakaṭa tha. Bhojakata

Udhar Kṛṣṇa Rukmiṇī ko lekar Dvārakā pahunch gaye. Dvaraka

Wahan bahut bada utsav hua.
Har ghar sajaya gaya.
Phool, deepak aur rang-birange jhande har taraf lage the.

Log naye kapde pehne hue the aur sab bahut khush the.

Sabko lag raha tha jaise swayam Lakṣmī ji Dvārakā aayi ho. Lakshmi

Phir shastron ke anusaar Kṛṣṇa aur Rukmiṇī ka vivaah bade dhoom-dhaam se hua.

Poora Dvārakā nagar khushi se jagmaga utha.

Moral yeh hai ki sachcha prem aur dharma har rukawat ko paar kar leta hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 55
    with st.expander("Chapter 55 - The Story of Pradyumna’s Birth"):
        text1 = """ 
        Yeh adhyāya Pradyumna ke janm aur unke adbhut jeevan ki kahani batata hai.
Pradyumna ko Krishna aur Rukmini ka putra bataya gaya hai, aur ve punarjanm liye hue Kāma-deva the. Kamadeva

Pehle Kāma-deva ko Shiva ke krodh se bhasm hona pada tha.
Baad me wahi Kāma-deva Pradyumna ke roop me janme."""
        create_image_text_layout(
            "attached_assets/chapter10/10.55.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Jab Pradyumna sirf kuch din ke the, tab Shambara nām ke asura ne unhe chura liya.
Usse pata tha ki yahi bachcha future me uska vinaash karega.

Usne bachche ko samundar me phenka diya.

Ek badi machhli ne us shishu ko nigal liya.

Baad me machhuaare us machhli ko pakadkar Śambara ke mahal me le aaye.

Jab rasoi me us machhli ko kaata gaya, tab uske andar se ek jeevit sundar bachcha nikla.

Wahan ek stri thi jiska naam Māyāvatī tha. Mayavati

Use bachcha de diya gaya.

Tab divine sage Narada aaye aur unhone Māyāvatī ko sach bataya:

“Yeh koi aam bachcha nahi hai.
Yeh Kṛṣṇa aur Rukmiṇī ka putra Pradyumna hai.
Aur tum asal me Rati ho, Kāma-deva ki patni.” Rati

Māyāvatī ne bahut prem se Pradyumna ko paala.

Samay ke saath Pradyumna jawaan hue aur bilkul Kṛṣṇa jaise sundar dikhne lage.

Sab striyan unhe dekhkar mohit ho jaati thi.

Tab Māyāvatī ne unhe unki asli pehchaan batayi.

Usne kaha:
“Tum Kāma-deva ka punarjanm ho.
Śambara ne tumhe bachpan me churaya tha.”

Usne Pradyumna ko mahā-māyā vidyā bhi sikhayi, jo sabhi jaadu aur illusion ko tod sakti thi.

Pradyumna ne fir Śambara ko yuddh ke liye lalkara.

Bahut bhayanak yuddh hua.

Śambara ne aasman me jaakar kai prakaar ki māyā aur jaadu ka prayog kiya.

Lekin Pradyumna ne sab tod diya.

Aakhir me Pradyumna ne talwar se Śambara ka sir kaat diya.

Devatāo ne phool barsaaye aur Pradyumna vijayi hue.

Uske baad Māyāvatī ke saath ve aakash mārg se Dvaraka laut aaye.

Jab Dvārakā ki mahilāon ne unhe dekha, to ve samajh baithi ki swayam Kṛṣṇa aa gaye hain, kyunki Pradyumna bilkul apne pita jaise dikhte the.

Phir Rukmini ne unhe dekha.

Unka hriday achanak mātr̥-prem se bhar gaya.
Unhe laga:
“Agar mera kho gaya putra zinda hota, to bilkul aisa hi dikhta.”

Tab Narada ne poori kahani sabko sunayi.

Sab log bahut khush hue.

Devaki, Vasudeva, Balarama aur Rukmiṇī ne Pradyumna ko gale laga liya.

Dvārakā me khushi ki lehar daud gayi.

Log kehne lage:
“Jo putra mar gaya samjha ja raha tha, woh phir se jeevit hokar laut aaya hai!”

Is kahani ka ek bada sandesh yeh hai ki bhagya aur divine plan ko koi nahi rok sakta.
Jo Bhagavān ki ichchhā hoti hai, wahi ant me satya hota hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 56
    with st.expander("Chapter 56 - Kṛṣṇa’s marriage with Jāmbavatī and Satyabhāmā"):
        text1 = """ 
        Satrajit ko Surya Dev ne ek magical Syamantaka jewel diya tha. Woh jewel bahut bright tha. Jab bhi Satrajit usse pehenta, log use Surya Dev samajh lete the.

Ek din Krishna ne us jewel ko raja Ugrasena ke liye maanga. Lekin Satrajit bahut greedy tha. Usne mana kar diya."""
        create_image_text_layout(
            "attached_assets/chapter10/10.56.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Baad mein Satrajit ka bhai Prasena jewel pehenkar jungle gaya. Wahan ek sher ne usse maar diya aur jewel le gaya. Phir Jambavan ne sher ko hara diya aur jewel apne ghar le aaya. Uska chhota beta us jewel se toy ki tarah khelne laga.

Jab Prasena wapas nahi aaya, Satrajit ne bina soche Krishna par ilzaam laga diya. Krishna ko bura laga. Sach sabit karne ke liye woh jungle gaye.

Krishna Jambavan ki cave mein gaye. Wahan dono ke beech bahut lambi fight hui. Kai din tak yudh chalta raha. Aakhir mein Jambavan samajh gaya ki Krishna koi aam insan nahi, balki Bhagwan hain.

Jambavan ne respect ke saath jewel Krishna ko de diya aur apni daughter Jambavati ki shaadi bhi Krishna se kar di.

Krishna jewel lekar Dwaraka wapas aaye aur sabko sach bata diya. Satrajit ko apni galti ka bahut pachtawa hua. Usne maafi maangi aur apni daughter Satyabhama ki shaadi Krishna se kar di.

Lekin Krishna ne jewel wapas kar diya. Unhone dikhaya ki sachchai aur daya sabse bada dhan hota hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 57
    with st.expander("Chapter 57 - Murder of Satājit for Syamantaka"):
        text1 = """ 
        Krishna aur Balaram ek din Hastinapur gaye the, kyunki sabko laga tha ki Pandav jal gaye hain. Unke jaane ka fayda uthakar kuch bure logon ne Syamantaka jewel churaane ka plan banaya.

Shatadhanva naam ka ek lalchi aadmi bahut gussa tha. Usne socha ki Satrajit ne uski beizzati ki hai. Ek raat woh chupke se Satrajit ke ghar gaya aur sote waqt uska murder kar diya. Phir Syamantaka jewel lekar bhaag gaya."""
        create_image_text_layout(
            "attached_assets/chapter10/10.57.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Satyabhama ne jab apne pita ko mara hua dekha, woh bahut royi. Woh turant Krishna ke paas gayi aur sab sach bata diya.

Krishna aur Balaram ko bahut dukh hua. Dono turant Dwaraka wapas aaye aur Shatadhanva ko pakadne nikle.

Dar ke maare Shatadhanva ne jewel Akrura ke paas chhupa diya aur khud bhaagne laga. Krishna aur Balaram uske peeche gaye. Aakhir Krishna ne use pakad liya aur apne Sudarshan Chakra se uska ant kar diya.

Lekin jab Krishna ne uske kapde check kiye, jewel wahan nahi tha. Tab unhe samajh aaya ki kisi aur ke paas hai.

Baad mein Krishna ne pyaar aur samajhdari se Akrura se baat ki. Akrura ne sach maan liya aur Syamantaka jewel sabke saamne dikha diya. Isse Krishna par laga har ilzaam khatam ho gaya.

Phir Krishna ne woh jewel wapas Akrura ko de diya. Unhone dikhaya ki sachchai, shanti aur daya hi sabse badi jeet hoti hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 58
    with st.expander("Chapter 58 - Espousals of Lord Kṛṣṇa"):
        text1 = """ 
        Ek baar Krishna Pandavo se milne Indraprastha gaye. Sabhi Pandav unhe dekhkar bahut khush hue. Draupadi ne bhi sharmate hue Krishna ka swagat kiya.

Kunti ne Krishna ko apne purane dukh yaad karke bataya ki unki presence hamesha unhe himmat deti hai. Krishna ne bhi unse pyaar se baat ki aur sabko comfort diya.

Ek din Krishna aur Arjun jungle gaye. Wahan unhe ek sundar ladki mili jiska naam Kalindi tha. Woh Surya Dev ki beti thi aur sirf Krishna ko apna pati banana chahti thi."""
        create_image_text_layout(
            "attached_assets/chapter10/10.58.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Krishna ne Kalindi ki sachchi bhakti dekhi aur usse apne saath le aaye. Baad mein dono ki shaadi ho gayi.

Phir Krishna ne Mitravinda ko bhi swayamvar se apne saath le aaye, kyunki woh dil se Krishna ko hi chahti thi.

Uske baad Krishna Ayodhya gaye. Wahan Raja Nagnajit ki beti Satya rehti thi. Shaadi ke liye ek mushkil challenge tha — saat khatarnak bulls ko control karna.

Bahut se raja fail ho chuke the. Lekin Krishna ne aasani se sab bulls ko shaant kar diya, jaise koi bachcha toys se khel raha ho.

Sab log hairaan reh gaye. Raja bahut khush hua aur Satya ki shaadi Krishna se kar di. Pure rajya mein celebration hua. Music baja, log nachne lage aur sabne khushi manayi.

Baad mein Krishna ne Bhadra aur Lakshmana se bhi shaadi ki. Unhone bahut si rajkumariyon ko buri shaktiyon se bachaya aur unhe respect aur suraksha di. """
        create_image_text_layout(text_content=text2, layout="full")
        
        # Chapter 59
    with st.expander("Chapter 59 - Narakāsura slain—The Pārijāta tree brought to Dvārakā"):
        text1 = """ 
        Raja Parikshit ne ek din poocha, “Krishna ne Narakasura naam ke raakshas ko kaise haraya?”

Narakasura bahut cruel tha. Usne devtaon ki cheezein chura li thi aur bahut si rajkumariyon ko bandi bana rakha tha. Indra ne jaakar Krishna se madad maangi.

Krishna apni wife Satyabhama ke saath Garuda par baithkar Narakasura ke sheher gaye. Sheher bahut strong security se ghira hua tha. Lekin Krishna ne apni shakti se saare traps tod diye."""
        create_image_text_layout(
            "attached_assets/chapter10/10.59.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Sabse pehle Krishna ka saamna Mura naam ke bhayanak demon se hua. Uske paanch sir the aur woh bahut dangerous tha. Lekin Krishna ne himmat se fight ki aur Sudarshan Chakra se uska ant kar diya.

Phir Narakasura aur uski sena yudh ke liye aaye. Bahut bada battle hua. Krishna ne shaant mann se uski saari weapons rok di. Aakhir mein Krishna ne Narakasura ko bhi hara diya.

Dharti Mata Krishna ke paas aayi aur unki praise ki. Unhone Narakasura ke bete ko Krishna ki protection mein de diya.

Jab Krishna mahal ke andar gaye, wahan unhe 16,000 rajkumariyan mili jo Narakasura ne bandi bana rakhi thi. Sabne Krishna ko apna rakshak maana aur unse help maangi.

Krishna ne sabko azaad kar diya aur respect ke saath Dwaraka bhej diya.

Baad mein Krishna Indra ke swarg gaye aur churaayi hui cheezein wapas kar di. Satyabhama ki ichchha par Krishna swarg se Parijata tree bhi Dwaraka le aaye.

Krishna ne sab rajkumariyon se shaadi ki aur sabko pyaar, suraksha aur samman diya. Woh hamesha sabki help karte the aur bure logon ko rok kar duniya mein shanti laate the."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 59(a)
    with st.expander("Chapter 59(a) - The Pārijāta Tree Taken by Śrī Kṛṣṇa"):
        text1 = """ 
        Narakasura ko haraane ke baad Krishna apni wife Satyabhama ke saath Garuda par baithkar swarg gaye. Wahan sab devtaon ne unka respect ke saath swagat kiya.

Krishna Aditi Mata se milne gaye aur unke churaaye hue earrings wapas diye. Aditi bahut khush hui aur Satyabhama ko pyar se aashirwad diya.

Wapas aate waqt Satyabhama ne ek bahut sundar garden dekha. Us garden mein ek magical Parijata tree tha. Uski khushboo aur chamak dekhkar woh hairaan reh gayi."""
        create_image_text_layout(
            "attached_assets/chapter10/10.59a.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Satyabhama ne Krishna se kaha, “Mujhe yeh tree bahut pasand hai. Agar aap mujhse sach mein pyar karte ho, toh ise Dwaraka le chaliye.”

Krishna ne pehle samjhaya ki yeh tree Indra ka hai aur ise le jaana sahi nahi hoga. Unhone kaha ki isse devta naraz ho sakte hain.

Lekin Satyabhama ne zid ki. Tab Krishna ne pyar se uski baat maan li. Unhone Parijata tree ko jad se nikala aur Garuda par rakh diya.

Garden ke guards gussa ho gaye aur Indra ko jaakar sab bata diya. Indra ko laga ki uska apmaan hua hai.

Phir Indra aur bahut se devta apni sena lekar Krishna ko rokne nikle. Sab taraf shankh, dhol aur yudh ki awaazein goonj uthi.

Lekin Krishna bilkul shaant the. Unhone dikhaya ki sachcha bal sirf power mein nahi, balki himmat aur dharma mein hota hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 59(b)
    with st.expander("Chapter 59(b) - Satyabhāmā defeats Gods"):
        text1 = """ 
        Jab Krishna Parijata tree lekar ja rahe the, tab bahut saare devta unhe rokne aaye. Krishna ne muskura kar Satyabhama se kaha, “Dekho, tumhare guests aa gaye.”

Tabhi devtaon ne teer chalane shuru kar diye. Satyabhama bhi bahadur thi. Usne turant dhanush uthaya aur saare arrows rok diye.

Sabse pehle dhan ke devta Kubera attack karne aaye. Woh zor zor se chillate hue battle karne lage. Lekin Satyabhama ne himmat se unka saamna kiya aur unke arrows ka jawab diya."""
        create_image_text_layout(
            "attached_assets/chapter10/10.59b.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Kubera bahut gussa ho gaya aur bola, “Aaj main tumhe hara dunga!” Lekin Satyabhama ne uska bow tod diya. Jab usne bada club pheka, Krishna ne use aasani se pakad liya aur hans pade. Kubera darr kar wahan se bhaag gaya.

Uske baad Varuna dev aaye. Unhone Garuda ko pakadne ki koshish ki. Lekin Garuda bahut powerful tha. Usne Varuna aur unke crocodile ko samundar mein phek diya. Varuna bhi bhaag gaye.

Phir Agni Dev aur Vayu Dev ne milkar Krishna par attack kiya. Krishna ne shaant rehkar unhe bhi hara diya. Dono samajh gaye ki Krishna aam insan nahi hain, aur woh battle chhodkar chale gaye.

Baad mein Yamraj bhi aaye, lekin Krishna ne unka hathiyaar gira diya. Yamraj bhi darr kar wapas chale gaye.

Aakhir mein Bhagwan Shiva bhi apni sena ke saath battle mein aaye. Krishna aur Shiva ke beech bahut powerful yudh hua. Dono ne bahut shakti dikhayi.

Lekin Garuda ne Shiva ke bull ko door phek diya. Tab Shiva samajh gaye ki yeh ladai aur badhana theek nahi hai. Woh shaanti se wapas chale gaye.

Is kahani se yeh seekh milti hai ki himmat aur sachchai ke saath shanti bhi zaroori hoti hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 59(c)
    with st.expander("Chapter 59(c) - Pārijāta planted in Satyabhāmā’s Palace"):
        text1 = """ 
        Indra ne apna crown pehna, dhanush uthaya aur apne bade elephant Airavat par baithkar Krishna ko rokne ke liye battle shuru ki.

Krishna ne shaant hokar shankh bajaya. Indra ne un par teer chalaye, lekin Krishna ne aasani se un sabko rok diya aur muskura kar bola, “Bahut accha, Indra!”

Battle aur tez ho gaya. Indra baar baar attack karta raha, lekin Krishna har baar uske arrows ka jawab dete rahe."""
        create_image_text_layout(
            "attached_assets/chapter10/10.59c.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Phir Indra ne apna sabse powerful weapon Vajra pheka. Lekin Krishna ne use apne haath mein pakad liya aur zor se hans pade.

Yeh dekhkar Indra sharminda ho gaya. Uska elephant bhi Garuda se pareshaan ho chuka tha. Isliye Indra ne battle chhod diya.

Satyabhama ne hasi mein Indra ko chhedte hue kaha, “Itni jaldi wapas ja rahe ho?”

Tab Indra ko samajh aa gaya ki Krishna koi aam raja nahi, balki sabke rakshak hain. Usne haath jodkar Krishna se maafi maangi.

Krishna ne pyar se kaha, “Tumhari koi galti nahi. Hum sab ek hi taraf hain.” Yeh sunkar Indra ka mann shaant ho gaya.

Phir Krishna, Satyabhama aur Garuda Parijata tree lekar Dwaraka laut aaye. Puri nagri ko phoolon, music aur khushi se sajaya gaya tha.

Krishna ne Parijata tree Satyabhama ke mahal mein lagwaya. Sab log us heavenly tree ko dekhkar hairaan aur khush ho gaye.

Is kahani se yeh seekh milti hai ki maafi, vinamrata aur prem sabse bade gun hote hain."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 60
    with st.expander("Chapter 60 - Conversation between Kṛṣṇa and Rukmiṇī (A Sweet Quarrel)"):
        text1 = """ 
        Ek din Rukmini apne mahal mein Krishna ki seva kar rahi thi. Mahal bahut sundar tha, phoolon ki khushboo aur chandni se pura room chamak raha tha.

Krishna Rukmini ko pyaar se dekhkar muskuraaye. Phir mazaak mein bole, “Tum toh kisi bhi bade raja se shaadi kar sakti thi. Phir tumne mujhe kyun chuna?”

Krishna ne hasi hasi mein aur bhi kaha, “Main toh simple hoon, mere bahut enemies bhi hain. Shayad tumhe kisi aur raja ko choose karna chahiye tha.”"""
        create_image_text_layout(
            "attached_assets/chapter10/10.60.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Rukmini ne pehle kabhi Krishna se aisi baat nahi suni thi. Woh bahut dukhi ho gayi. Unki aankhon mein aansu aa gaye aur woh darr gayi ki kahin Krishna unhe chhod na dein.

Krishna ne dekha ki Rukmini sach mein udaas ho gayi hai. Woh turant uthkar unke paas aaye, unke aansu pochhe aur pyaar se unhe sambhala.

Krishna ne softly kaha, “Main sirf mazaak kar raha tha. Main jaanta hoon ki tum mujhse sachcha pyaar karti ho.”

Tab Rukmini ne shanti se jawab diya, “Aap duniya ke sabse special aur mahaan hain. Maine sirf aapko hi apna maana hai.”

Unhone kaha ki Krishna jaise dayalu aur powerful koi nahi hai. Jo unke charnon ka pyaar samajh leta hai, woh kabhi kisi aur ko choose nahi karta.

Krishna Rukmini ki baatein sunkar bahut khush hue. Unhone kaha, “Tumhara pyaar aur vishwas bahut pavitra hai.”

Phir dono haste hue pyaar se baat karne lage. Unka rishta aur bhi strong ho gaya."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 60(a)
    with st.expander("Chapter 60(a) - Slaying of Pauṇḍraka and others"):
        text1 = """ 
        Ek samay Paundraka naam ka ek raja tha. Woh Kashi desh ka raja tha aur bahut proud aur powerful tha.

Uska janm Vasudeva ke ghar hua tha, isliye log use bhi “Vasudeva” bulate the. Dheere dheere uske mann mein ahankaar aa gaya.

Jab Krishna Dwaraka mein nahi the, tab Paundraka ne socha ki yeh sahi mauka hai. Woh apni badi sena lekar Dwaraka par attack karne aa gaya."""
        create_image_text_layout(
            "attached_assets/chapter10/10.60a.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Lekin Dwaraka akeli nahi thi. Balaram, Satyaki aur dusre Yadava warriors ne himmat se sheher ki raksha ki.

Bahut bhayanak yudh hua. Paundraka ki sena ko bhaari nuksaan hua. Uske bahut saare ghode, haathi aur soldiers haar gaye.

Aakhir mein woh darr kar raat ko hi wapas Kashi bhaag gaya.

Subah Krishna Badarikashram se Dwaraka laut aaye. Sab Yadavo ne unka swagat kiya aur unhe poori kahani batayi.

Krishna shaant hokar sab sunte rahe. Unhe pata tha ki ahankaar aur jhooti shaan zyada der tak nahi tikti."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 61
    with st.expander("Chapter 61 - Aniruddha s Marriage: Rukmī Slain"):
        text1 = """ 
        Raja Parikshit ne poocha, “Rukmi toh Krishna se haar chuka tha aur unse dushmani rakhta tha. Phir usne apni beti ki shaadi Krishna ke bete se kaise kar di?”

Rishi Shukadev bole, “Bhagwan Krishna ki har rani ke das putra the. Sabhi bahadur aur gunvaan the. Krishna apni har patni ke saath itne prem se rehte the ki har rani ko lagta tha ki Krishna unhe sabse zyada pyaar karte hain.”

Krishna ki raniyan unki madhur baatein, muskaan aur sundar roop dekhkar bahut khush rehti thi. Woh swayam seva karti thi, jaise unke pair dhona, phool chadhana aur bhojan dena."""
        create_image_text_layout(
            "attached_assets/chapter10/10.61.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Rukmini ke sabse bade putra ka naam Pradyumna tha. Woh bahut sundar aur veer the.

Ek din Rukmi ki beti Rukmavati ka swayamvar hua. Bahut saare raja aur yoddha wahan aaye. Lekin Rukmavati ne Pradyumna ko hi apna pati chuna.

Pradyumna ne sabhi yoddhao ko hara diya aur Rukmavati ko apne saath le gaye.

Rukmi ab bhi Krishna se dushmani rakhta tha, lekin apni behen Rukmini ko khush karne ke liye usne yeh vivaah maan liya.

Baad mein Pradyumna aur Rukmavati ke ghar ek bahadur putra paida hua, jiska naam Aniruddha tha.

Samay beetne ke baad Rukmi ne apni poti Rocana ki shaadi Aniruddha se karne ka faisla kiya. Is shaadi ke liye Krishna, Balarama, Pradyumna aur doosre Yadav Bhojakata nagar gaye.

Shaadi bahut dhoom-dhaam se hui.

Lekin shaadi ke baad kuch ghamandi rajaon ne Rukmi ko bhadkaaya. Unhone kaha, “Balarama ko paasay ke khel mein harao.”

Balarama ko dice ka khel pasand tha, isliye woh maan gaye.

Khel shuru hua. Pehle Rukmi jeeta aur Kalinga ka raja zor-zor se hansne laga. Yeh dekhkar Balarama ko bura laga.

Phir ek bade daav mein Balarama sach mein jeet gaye. Lekin Rukmi jhooth bolkar bola, “Jeet meri hui hai!”

Tab aasman se awaaz aayi, “Is khel mein Balarama hi jeete hain. Rukmi jhooth bol raha hai.”

Lekin Rukmi fir bhi hansne laga aur Balarama ka mazaak udaate hue bola, “Tum toh sirf gwale ho. Rajaon jaise khel tumhe nahi aate.”

Yeh sunkar Balarama ka gussa bahut badh gaya. Unhone lohe ka gada uthaya aur sabke saamne Rukmi ko maar diya.

Phir unhone Kalinga ke raja ko bhi pakadkar uske daant tod diye, kyunki woh hans raha tha.

Baaki raja darr kar wahan se bhaag gaye.

Krishna chup rahe, kyunki woh na toh apne bhai Balarama ko dukhi karna chahte the aur na hi apni patni Rukmini ko.

Uske baad sab log Aniruddha aur Rocana ko saath lekar Dwaraka laut aaye."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 62
    with st.expander("Chapter 62 - Aniruddha taken captive by Bāṇāsura"):
        text1 = """ 
        Raja Parikshit ne poocha, “Aniruddha ki shaadi Banasura ki beti Usha se kaise hui? Aur Bhagwan Shiva aur Krishna ke beech yudh kyun hua?”

Rishi Shukadev bole, “Banasura Raja Bali ka bada beta tha. Woh Bhagwan Shiva ka bahut bada bhakt tha. Shiva ji usse prasann hokar uske nagar Shonitapura ke rakshak ban gaye the.

Banasura ke hazaar haath the. Woh apni shakti par bahut ghamand karta tha. Ek din usne Shiva ji se kaha, “Mere hazaar haath bekaar ja rahe hain, kyunki mujhe koi takkar dene wala milta hi nahi.”

Yeh sunkar Shiva ji thoda naraaz hue aur bole, “Jab tumhara dhwaj tootega, tab tumhe ek aisa yoddha milega jo tumhara ghamand tod dega.”"""
        create_image_text_layout(
            "attached_assets/chapter10/10.62.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Banasura ki ek sundar beti thi, jiska naam Usha tha.

Ek raat Usha ne sapne mein ek sundar rajkumar ko dekha. Uska rang saawla tha, aankhen kamal jaisi thi aur usne peele vastra pehne the. Sapne mein Usha ko usse prem ho gaya.

Subah uthte hi Usha udaas hokar boli, “Woh kahan chale gaye?”

Uski sabse achchi saheli Chitralekha ne poocha, “Kaun?”

Usha ne sapne wale rajkumar ka varnan kiya. Tab Chitralekha ne bahut saare rajkumaron aur devtaon ki tasveerein banaayi.

Jab usne Krishna, Balarama aur Pradyumna ki tasveer banaayi, tab Usha chup rahi. Lekin jaise hi Aniruddha ki tasveer saamne aayi, Usha sharma kar boli, “Yehi hain! Yehi mere sapne wale rajkumar hain!”

Chitralekha ke paas yog shakti thi. Woh hawa mein udkar Dwaraka pahunch gayi. Wahan Aniruddha so rahe the. Chitralekha chupke se unhe utha kar Usha ke mahal mein le aayi.

Aniruddha aur Usha ek doosre ko dekhkar bahut khush hue. Dheere-dheere dono ek doosre se prem karne lage aur mahal mein chupkar rehne lage.

Lekin kuch samay baad mahal ki dasiyon ko shak ho gaya. Unhone Banasura ko jaakar bata diya.

Banasura turant gusse mein Usha ke mahal pahunch gaya. Wahan usne Aniruddha ko dekha. Woh bahut sundar aur veer lag rahe the.

Aniruddha ne dekha ki sainik unhe pakadne aa rahe hain, toh unhone lohe ka gada uthaya aur sabko haraane lage. Bahut saare sainik bhaag gaye.

Lekin Banasura bahut shaktishaali tha. Usne jadui Naagpaash se Aniruddha ko baandh diya.

Yeh dekhkar Usha bahut royi aur dukhi ho gayi."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 63
    with st.expander("Chapter 63 - Bāṇa Vanquished—Aniruddha brought to Dvārakā"):
        text1 = """ 
        Rishi Shukadev bole, “Aniruddha ko bandi banaye hue chaar mahine beet gaye. Dwaraka mein sab log bahut pareshaan the. Kisi ko nahi pata tha ki Aniruddha kahan hain.

Tab Devarshi Narad ne Krishna ko sab sach bataya — kaise Aniruddha ne veerta se yudh kiya aur kaise Banasura ne unhe bandi bana liya.

Yeh sunkar Krishna, Balarama, Pradyumna, Samba aur bahut bade Yadav yoddha sena lekar Shonitapura ki taraf chal pade.

Jab Banasura ne dekha ki Krishna ki sena uske nagar ke dwar aur bageeche tod rahi hai, toh woh gusse se bhar gaya. Woh bhi apni sena lekar yudh ke liye aa gaya."""
        create_image_text_layout(
            "attached_assets/chapter10/10.63.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Bhagwan Shiva bhi apne putra Kartikeya aur apne ganon ke saath Banasura ki madad ke liye aaye, kyunki Banasura unka bhakt tha.

Phir ek mahaan yudh shuru hua.

Krishna aur Shiva ke beech bhayankar yudh hua. Pradyumna ne Kartikeya se yudh kiya aur Balarama ne doosre asuro ko hara diya.

Aasmaan mein Brahma ji, rishi aur devta sab yeh adbhut yudh dekhne aaye.

Krishna ne apne teeron aur astron se Shiva ji ke ganon ko peeche hata diya. Shiva ji bhi divya astr chala rahe the, lekin Krishna har astra ka jawab de rahe the.

Ant mein Krishna ne ek vishesh astra chala kar Shiva ji ko kuch der ke liye sust kar diya. Tab Krishna ne Banasura ki sena ko hara diya.

Banasura bahut gusse mein tha. Usne ek saath apne kai haathon se dhanush uthakar Krishna par teer barsa diye.

Lekin Krishna ne apne Sudarshan Chakra se Banasura ke ek-ek haath kaatne shuru kar diye, jaise ped ki shaakha kaati jaati hai.

Jab Banasura haarne laga, tab Bhagwan Shiva Krishna ke paas aaye aur bole, “Banasura mera bhakt hai. Kripya uspar daya kijiye.”

Krishna muskura kar bole, “Main ise nahi maarunga. Sirf iska ghamand tod raha hoon.”

Krishna ne Banasura ke adhiktar haath kaat diye, lekin chaar haath chhod diye.

Banasura ne vinamrata se sir jhukaya aur Aniruddha ko Usha ke saath Krishna ke paas le aaya.

Phir Krishna, Balarama aur sab Yadav Aniruddha aur Usha ko lekar Dwaraka laut aaye.

Dwaraka nagari ko sundar jhandon aur phoolon se sajaya gaya tha. Sab log khushi se unka swagat karne lage.

Rishi Shukadev bole, “Jo vyakti Krishna aur Shiva ke is mahaan yudh ki kahani shraddha se sunta hai, usse jeevan mein haar ka saamna kam karna padta hai.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 64
    with st.expander("Chapter 64 - The Story of Nṛga"):
        text1 = """ 
        Rishi Shukadev bole, “Ek din Samba, Pradyumna aur Yadu vansh ke doosre rajkumar bagiche mein khelne gaye. Bahut der tak khelne ke baad sabko pyaas lagi.

Woh paani dhoondhne lage. Tab unhe ek sookha kuaan dikha. Jab unhone andar jhaank kar dekha, toh wahan ek bahut bada ajeeb sa girgit jaisa prani pada tha.

Sab rajkumar hairaan ho gaye. Unhone us bechare prani ko bahar nikaalne ki koshish ki. Rassi aur chamde ki pattiyan bhi use nikaal nahi paayi.

Phir woh sab Krishna ke paas gaye aur unhe sab bataya."""
        create_image_text_layout(
            "attached_assets/chapter10/10.64.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Bhagwan Krishna khud kuaan ke paas aaye. Unhone aasani se apne baaye haath se us bade girgit ko bahar nikaal liya.

Jaise hi Krishna ka sparsh hua, woh girgit turant ek sundar devta jaisa purush ban gaya. Uska sharir sone ki tarah chamak raha tha.

Woh Krishna ke charanon mein jhuk gaya.

Krishna ne poocha, “Aap kaun hain? Aur aapko yeh ajeeb janm kyun mila?”

Woh purush vinamrata se bola, “Prabhu, mera naam Raja Nriga hai. Main Ikshvaku vansh ka raja tha. Maine bahut daan aur punya kiye the.”

Raja Nriga ne bataya, “Main hazaaron gaayein Brahmano ko daan mein deta tha. Sab gaayein sundar, swasth aur doodh dene wali hoti thi.”

“Lekin ek din galti se ek Brahman ki gaay meri gaayon mein mil gayi. Mujhe pata nahi tha aur maine wahi gaay doosre Brahman ko daan mein de di.”

“Jab asli malik ne apni gaay dekhi, toh dono Brahman jhagda karne lage. Main bahut pareshaan ho gaya.”

“Maine unse maafi maangi aur badle mein hazaaron gaayein dene ki baat kahi. Lekin dono ne mana kar diya.”

“Kuch samay baad meri mrityu ho gayi. Yamraj ne mujhse poocha, ‘Pehle punya ka phal chahte ho ya paap ka?’”

“Maine kaha, ‘Pehle paap ka phal bhugta hoon.’ Tab mujhe girgit ka janm mila.”

“Lekin Prabhu, main hamesha aapko yaad karta raha. Aaj aapke sparsh se mujhe mukti mil gayi.”

Raja Nriga ne Krishna ko pranam kiya aur swarg jaane ke liye divya vimaan mein baith gaye.

Uske baad Krishna ne sabko seekh dete hue kaha,

“Brahman ya kisi bhi achche vyakti ki cheez galat tareeke se lena bahut bada paap hota hai. Chahe galti se hi kyun na ho, humein hamesha satark rehna chahiye.”

Krishna ne sabko daya, imaandari aur dharma ka paalan karne ki seekh di.

Yeh kahani sunkar sab log gahri soch mein pad gaye."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 65
    with st.expander("Chapter 65 - Balarāma’s Visit to Gokula—The Course of the Yamunā diverted"):
        text1 = """ 
        Rishi Shukadev bole, “Ek din Balarama ji ko apne purane dost aur Gokul ke logon ki yaad aayi. Woh turant rath par baithkar Gokul chale gaye.

Gokul pahunchte hi Nanda Baba aur Yashoda Maiya unhe dekhkar bahut khush hue. Unhone Balarama ko gale lagaya aur aansuon ke saath aashirvaad diya.

Gokul ke sab gop aur gopiyan bhi unse milne aaye. Sabne pyar se unka swagat kiya."""
        create_image_text_layout(
            "attached_assets/chapter10/10.65.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Gop log bole, “Hey Balarama, kya Krishna humein yaad karte hain? Kya woh kabhi Gokul wapas aayenge?”

Gopiyan bhi dukhi swar mein boli, “Humne Krishna ke liye sab kuch chhod diya tha. Lekin woh humein chhodkar chale gaye.”

Kuch gopiyan boli, “Krishna ki baatein bahut madhur thi. Isi liye humne unpar vishwas kiya.”

Yeh sab yaad karke gopiyan ro padi.

Balarama ne sabko shaant kiya aur Krishna ke prem bhare sandesh sunaye. Yeh sunkar gopiyon ka mann halka hua.

Balarama do mahine tak Gokul mein rahe. Woh sabke saath prem aur khushi se samay bitaane lage.

Ek raat poornima ka chand chamak raha tha. Yamuna ke kinare thandi hawa chal rahi thi aur phoolon ki sugandh faili hui thi.

Tab Varun dev ki taraf se ek madhur sugandhit पेय “Varuni” ped ke andar se nikalne laga. Balarama ne gopiyon ke saath uska aanand liya.

Khushi mein Balarama geet gaane lage aur sabke saath van mein ghoomne lage.

Us samay Balarama ne Yamuna ji ko bulaya aur kaha, “Yahan aao, mujhe jal-kreeda karni hai.”

Lekin Yamuna ji turant nahi aayi.

Balarama ko laga ki Yamuna unki baat nahi maan rahi. Woh thoda gusse mein aa gaye.

Unhone apna hal uthaya aur Yamuna ko kheenchna shuru kar diya. Yamuna ka paani zor se mudne laga.

Yamuna devi darr gayi. Woh turant Balarama ke charanon mein girkar boli,

“Hey Prabhu, mujhe maaf kijiye. Main aapki shakti ko pehchaan nahi paayi.”

Balarama ka gussa shaant ho gaya. Unhone Yamuna ko maaf kar diya.

Phir Balarama gopiyon ke saath Yamuna mein jal-kreeda karne lage. Sab log bahut khush the.

Baad mein Lakshmi ji ne Balarama ko sundar neele vastra aur gehne diye. Unhe pehenkar Balarama aur bhi tejomay lagne lage.

Rishi Shukadev bole, “Aaj bhi Yamuna ka pravah usi jagah se mudta hai, jahan Balarama ne use apne hal se kheench liya tha. Yeh unki mahaan shakti ka pramaan hai.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 66
    with st.expander("Chapter 66 - Slaying of Pauṇḍraka and others"):
        text1 = """ 
        Rishi Shukadev bole, “Jab Balarama Gokul gaye hue the, tab Karusha desh ka ek murkh raja Paundraka khud ko asli Vasudeva samajhne laga.

Kuch chaploos log uski tarif karte rehte the. Dheere-dheere usse sach mein lagne laga ki wahi Bhagwan Vasudeva hai.

Usne Krishna ke paas ek doot bheja. Doot ne sabha mein jaakar kaha,

“Mere raja hi asli Vasudeva hain. Tum jhoothi tarah se unka roop dharan kar rahe ho. Shankh, Chakra aur doosre chinh chhod do. Ya phir yudh karo.”

Yeh baat sunkar Ugrasena aur sab log zor se hans pade."""
        create_image_text_layout(
            "attached_assets/chapter10/10.66.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Krishna muskuraaye aur bole, “Jaakar apne raja se kehna ki main jaldi hi uske nakli chinh aur ghamand dono chheen lunga.”

Doot ne jaakar Paundraka ko sab bata diya.

Phir Krishna apna rath lekar Kashi ki taraf chale gaye, jahan Paundraka apne dost Kashi ke raja ke saath tha.

Paundraka bhi yudh ke liye nikla. Usne Krishna ki tarah nakli peele vastra pehne the, nakli Sudarshan Chakra, gada aur shankh bhi liya hua tha. Woh bilkul natak karne wale kalakar jaisa lag raha tha.

Usse dekhkar Krishna zor se hans pade.

Yudh shuru hua. Paundraka aur Kashi ke raja ki sena ne Krishna par teeron aur hathiyaaron ki baarish kar di.

Lekin Krishna ne apne divya astron se poori sena ko tabaah kar diya.

Phir Krishna ne Paundraka se kaha, “Tumne mujhe apne chinh chhodne ko kaha tha. Ab main tumhara jhootha roop khatam karta hoon.”

Itna kehkar Krishna ne Sudarshan Chakra chala diya. Chakra ne Paundraka ka sir kaat diya.

Uske baad Krishna ne Kashi ke raja ka bhi sir kaat diya. Woh sir udta hua Kashi nagar mein ja gira.

Krishna vijay paakar Dwaraka laut aaye.

Kashi ke log bahut dukhi hue. Raja ka beta Sudakshina badla lena chahta tha.

Usne Bhagwan Shiva ki tapasya ki. Shiva ji prasann hue aur usse ek khatarnak yagya karne ka upay bataya.

Sudakshina ne jadui yagya kiya. Yagya se ek bhayanak aag ka rakshas nikla. Uski aankhon aur muh se aag nikal rahi thi.

Woh seedha Dwaraka ki taraf badha.

Dwaraka ke log bahut darr gaye aur Krishna ke paas bhaage.

Krishna shaant hokar bole, “Dar mato. Main sab theek kar dunga.”

Phir Krishna ne apna Sudarshan Chakra bheja.

Sudarshan Chakra suraj ki tarah chamak raha tha. Usne us bhayanak aag ko turant rok diya.

Woh jadui aag wapas mud gayi aur Kashi pahunchkar Sudakshina aur uske purohit ko hi jala diya.

Uske baad Sudarshan Chakra ne poori Kashi nagari ko bhi jala diya aur phir Krishna ke paas laut aaya.

Rishi Shukadev bole, “Jo vyakti Krishna ke in divya kaaryon ko shraddha se sunta ya sunata hai, uske paap dheere-dheere door ho jaate hain.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 67
    with st.expander("Chapter 67 - Balarāma slays Dvivida"):
        text1 = """ 
        Raja Parikshit bole, “Mujhe Balarama ji ke aur adbhut kaam sunne ki ichchha hai. Kripya bataaiye unhone aur kya mahaan kaarya kiye?”

Rishi Shukadev bole, “Dvivida naam ka ek bahut shaktishaali vanar tha. Woh Narakasura ka dost tha aur Sugriva ka mantri bhi reh chuka tha.

Jab Krishna ne Narakasura ko maara, tab Dvivida badla lena chahta tha.

Usne desh bhar mein tabahi machani shuru kar di. Kabhi gaon jala deta, kabhi pahaad ukhaad deta aur kabhi samundar ka paani uchaal kar kinaare waale ilaakon ko dubo deta."""
        create_image_text_layout(
            "attached_assets/chapter10/10.67.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Woh rishiyon ke ashram bhi barbaad karta tha aur logon ko pareshaan karta rehta tha.

Ek din Dvivida ne madhur sangeet suna. Woh Raivataka parvat ki taraf gaya.

Wahan usne Balarama ko dekha. Balarama sundar phoolon ki mala pehne hue the aur gopiyon ke saath khushi se samay bita rahe the.

Dvivida shararat karne laga. Woh pedon par chadhkar unhe zor-zor se hilane laga aur ajeeb awaazein nikaalne laga.

Gopiyan uski harkatein dekhkar hansne lagi.

Lekin Dvivida aur badtameezi karne laga. Woh gopiyon ka mazaak udaane laga aur Balarama ko chidhane laga.

Balarama ko gussa aa gaya. Unhone ek bada pathar uski taraf pheka.

Lekin Dvivida bahut chaalak tha. Woh bach gaya aur neeche aakar Balarama ka madira ka ghada uthakar bhaag gaya.

Usne ghada tod diya aur gopiyon ke kapde bhi kheenchne laga.

Ab Balarama ka gussa bahut badh gaya. Unhone apna hal aur musal uthaya aur Dvivida ko maarne ke liye taiyaar ho gaye.

Dvivida ne ek bada saal ka ped ukhaad liya aur Balarama par hamla kar diya.

Lekin Balarama pahaad ki tarah mazboot khade rahe. Unhone apne musal se Dvivida ke sir par zor se vaar kiya.

Dvivida ke sir se khoon behne laga, lekin woh fir bhi ladta raha.

Woh baar-baar naye ped ukhaadkar Balarama par fekta raha. Balarama har ped ko tod dete.

Poora jungle dheere-dheere pedon se khaali ho gaya.

Phir Dvivida ne bade-bade pathar fekne shuru kiye. Balarama ne sab patharon ko choor-choor kar diya.

Aakhir mein Dvivida ne apni muthi se Balarama ke seene par zor se vaar kiya.

Tab Balarama ne bhi apne dono haathon se uske kandhon par bahut zor se prahar kiya.

Dvivida khoon ugalta hua zameen par gir gaya. Uske girte hi poora pahaad hilne laga.

Aasmaan se devtaon aur rishiyon ne “Bahut achcha!” kehkar phool barsaaye.

Is tarah Balarama ne dusht Dvivida ka ant kiya aur phir apni nagari laut aaye."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 68
    with st.expander("Chapter 68 - Hastināpura dragged by Balarāma"):
        text1 = """ 
        Rishi Shukadev bole, “Jambavati ke putra Samba bahut veer the. Ek din Duryodhana ki beti Lakshmana ka swayamvar tha. Samba usse bahut prem karte the, isliye woh use swayamvar se hi apne rath mein bitha kar le gaye.

Yeh dekhkar Kaurav bahut gusse mein aa gaye. Woh bole, “Yeh ladka hadd paar kar raha hai. Isse pakdo!”

Karna, Shalya aur doosre bade yoddha Samba ke peeche bhaage.

Samba akela tha, lekin sher ki tarah bahaduri se lada. Usne apne teeron se kai yoddhao ko rok diya. Sab uski veerta dekhkar hairaan ho gaye."""
        create_image_text_layout(
            "attached_assets/chapter10/10.68.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Lekin Kaurav bahut zyada the. Unhone milkar Samba ka rath tod diya, ghodon ko maar diya aur use pakad liya. Phir use Lakshmana ke saath Hastinapur le gaye.

Jab Narad ji ne yeh baat Dwaraka mein bataayi, tab Yadav sena yudh ke liye taiyaar ho gayi.

Lekin Balarama shanti chahte the. Woh nahi chahte the ki Kaurav aur Yadavon ke beech bada yudh ho.

Isliye Balarama khud Hastinapur gaye. Unke saath Uddhav aur kuch bade log bhi the.

Balarama ne pehle shanti se sandesh bheja. Unhone kaha,

“Samba ne akela ladte hue bahaduri dikhayi. Tum sabne milkar use pakda, jo dharm ke khilaaf hai. Ab use aur Lakshmana ko humein wapas de do.”

Lekin Kaurav ghamand mein aa gaye. Woh bole,

“Yadav humari wajah se rajsi jeevan jeete hain. Aur ab woh humein aadesh de rahe hain?”

Unhone Balarama ki bhi beizzati kar di.

Yeh sunkar Balarama ko bahut gussa aa gaya.

Woh bole, “Main yahan shanti se baat karne aaya tha. Lekin tum log ghamand mein andhe ho gaye ho.”

Phir Balarama ne apna hal uthaya.

Unhone poori Hastinapur nagari ko apne hal se kheenchna shuru kar diya, jaise use Ganga mein gira denge.

Poora shehar hilne laga. Log darr ke maare kaanpne lage.

Tab Kaurav samajh gaye ki Balarama ki shakti kitni mahaan hai.

Woh turant Samba aur Lakshmana ko lekar Balarama ke paas aaye. Sabne haath jodkar maafi maangi.

Woh bole, “Hey Balarama, humein maaf kar dijiye. Hum aapki shakti ko nahi samajh paaye.”

Balarama ka gussa shaant ho gaya. Unhone sabko maaf kar diya.

Duryodhana ne apni beti Lakshmana ko bahut saare uphaar aur dahej ke saath Samba ko de diya.

Uske baad Balarama, Samba aur Lakshmana ko lekar Dwaraka laut aaye.

Rishi Shukadev bole, “Aaj bhi Hastinapur ki zameen thodi jhuki hui maani jaati hai. Log kehte hain ki yeh Balarama ke us mahaan bal ka pramaan hai.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 69
    with st.expander("Chapter 69 - Śrī Kṛṣṇa’s Household Life"):
        text1 = """ 
        Raja Parikshit ne poocha, “Bhagwan Krishna ek hi samay mein itni saari raniyon ke saath kaise rehte the? Yeh kaise sambhav tha?”

Rishi Shukadev bole, “Yeh Bhagwan Krishna ki divya Yogmaya thi.”

Jab Devarshi Narad ne suna ki Krishna ne 16,000 raniyon se vivaah kiya hai, toh woh bhi hairaan ho gaye. Unhone socha, “Ek vyakti sabko ek saath kaise khush rakh sakta hai?”

Isliye Narad ji Dwaraka gaye.

Dwaraka bahut sundar nagari thi. Wahan bade-bade mahal, sundar bagiche aur kamal se bhare talaab the. Har taraf pakshiyon ki madhur awaaz gunj rahi thi."""
        create_image_text_layout(
            "attached_assets/chapter10/10.69.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Krishna ki raniyon ke 16,000 alag-alag mahal the. Sab mahal heere, moti aur sundar ratnon se sajaaye gaye the.

Narad ji pehle Rukmini ji ke mahal mein gaye.

Wahan unhone dekha ki Krishna Rukmini ji ke saath baithe hain. Rukmini ji swayam Krishna ko pankha kar rahi thi.

Jaise hi Krishna ne Narad ji ko dekha, woh turant khade ho gaye. Unhone Narad ji ko pranam kiya, unke pair dhoye aur bade adar se baithne ko kaha.

Narad ji yeh dekhkar bahut prabhavit hue.

Phir Narad ji doosre mahal mein gaye.

Wahan Krishna Satyabhama ke saath paasay ka khel khel rahe the.

Teesre mahal mein Krishna apne bachchon ke saath khel rahe the.

Kahin woh yagya kar rahe the, kahin Brahmano ko bhojan kara rahe the, kahin dhyaan kar rahe the aur kahin rajya ke kaam sambhaal rahe the.

Kahin woh yudh ki yojana bana rahe the aur kahin shanti ki baat kar rahe the.

Narad ji har mahal mein Krishna ko alag-alag kaam karte dekhkar hairaan reh gaye.

Unhone samajh liya ki Bhagwan Krishna aam manushya nahi, balki sarvashaktimaan Bhagwan hain.

Narad ji muskuraakar bole, “Hey Prabhu, aapki Yogmaya ko samajhna bahut mushkil hai. Aap sach mein adbhut hain.”

Krishna muskuraaye aur bole, “Main duniya ko dharma ka raasta dikhane ke liye manushya jaisa jeevan jeeta hoon.”

Narad ji Krishna ki mahima gaate hue wahan se chale gaye.

Rishi Shukadev bole, “Jo vyakti Krishna ki in divya leelaon ko shraddha se sunta hai, uske mann mein Bhagwan ke prati bhakti badhti hai.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 70
    with st.expander("Chapter 70 - Deputation from Captive Kings of Jarāsandha"):
        text1 = """ 
        Rishi Shukadev bole, “Subah hone par Krishna ki raniyan udaas ho jaati thi, kyunki unhe lagta tha ki ab Krishna unse kuch der ke liye door ho jayenge. Murge ki awaaz sunkar woh mann hi mann use kosne lagti thi.

Bhagwan Krishna Brahma Muhurat mein uth jaate the. Woh haath-muh dhokar shaant mann se dhyaan karte the.

Uske baad woh snaan karte, Sandhya-vandan aur Gayatri mantra ka jap karte. Phir Surya dev, rishi aur apne purvajon ko jal arpit karte."""
        create_image_text_layout(
            "attached_assets/chapter10/10.70.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Krishna har din Brahmano ko hazaaron sundar gaayein daan mein dete the. Gaayon ke singh sone se sajaaye jaate aur unke gale mein motiyon ki mala hoti.

Uske baad Krishna sundar vastra aur gehne pehnte. Woh sabhi logon ki ichchha poori karte aur sabko khush rakhte.

Phir Krishna Satyaki aur Uddhav ke saath Sudharma sabha mein jaate. Wahan gaane, nritya aur purani kahaniyon ka paath hota tha.

Ek din ek anjaan doot sabha mein aaya. Usne haath jodkar kaha,

“Hey Krishna, Magadh ka raja Jarasandh bahut atyachaari ho gaya hai. Usne 20,000 rajaon ko bandi bana rakha hai. Woh sab aapse madad maang rahe hain.”

Doot ne kaha, “Hey Prabhu, hum sab aapki sharan mein hain. Kripya humein Jarasandh ke bandhan se mukt kijiye.”

Jab yeh baat ho hi rahi thi, tab Devarshi Narad wahan aa gaye. Krishna ne turant uthkar unka samman kiya.

Narad ji bole, “Hey Prabhu, Yudhishthira Rajasuya yagya karna chahte hain. Woh chahte hain ki aap us yagya mein aayein.”

Narad ji ne kaha, “Aapki mahima teenon lokon mein faili hui hai. Aapka naam sunne se bhi log pavitra ho jaate hain.”

Sabha mein baithe Yadav sochne lage ki pehle Jarasandh ka saamna kiya jaaye ya Rajasuya yagya ki taiyaari.

Tab Krishna ne muskuraakar Uddhav se poocha, “Tum batao, humein kya karna chahiye?”

Uddhav vinamrata se Krishna ka aadesh maankar jawab dene ke liye taiyaar ho gaye."""
        create_image_text_layout(text_content=text2, layout="full")
        
        # Chapter 71
    with st.expander("Chapter 71 - Śrī Kṛṣṇa’s visit to Indraprastha"):
        text1 = """ 
        Rishi Shukadev bole, “Narad ji ki baat aur sabha ke logon ki salah sunkar Uddhav ne Krishna se kaha,

“Hey Prabhu, aapko Yudhishthira ki Rajasuya yagya mein madad bhi karni chahiye aur Jarasandh ke bandi rajaon ko bhi bachana chahiye.”

Uddhav ne samjhaaya, “Rajasuya yagya wahi raja kar sakta hai jo sab dishaon ko jeet chuka ho. Isliye pehle Jarasandh ko harana zaroori hai.”"""
        create_image_text_layout(
            "attached_assets/chapter10/10.71.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Phir Uddhav bole, “Jarasandh bahut shaktishaali hai. Uske paas bahut badi sena hai. Use sena se haraana mushkil hai. Lekin Bhima uske barabar balwaan hain.”

“Isliye Bhima ko Brahman ka roop lekar Jarasandh se ekal yudh maangna chahiye. Aapke saath hone par Bhima zaroor jeetenge.”

Sabko Uddhav ki baat sahi lagi. Narad ji aur Yadav sab khush hue.

Phir Krishna ne yatra ki taiyaari karne ka aadesh diya.

Unhone apni raniyon, putron aur sevakon ko pehle hi bhej diya. Uske baad Balarama aur Raja Ugrasena se anumati lekar Krishna apne Garud chinh waale rath par baith gaye.

Krishna ki badi sena bhi saath chal padi. Har taraf shankh, nagade aur turhiyon ki awaaz gunj rahi thi.

Krishna ki raniyan sundar vastra aur gehne pehne hue sone ki palkiyon mein chal rahi thi.

Raaste mein Krishna kai deshon, nadiyon aur gaonon se guzarte hue Indraprastha pahunch gaye.

Jab Yudhishthira ko pata chala ki Krishna aa rahe hain, toh woh bahut khush hue. Woh apne bhaiyon aur purohiton ke saath Krishna ka swagat karne bahar aaye.

Yudhishthira ne Krishna ko dekhte hi gale laga liya. Unki aankhon mein khushi ke aansu aa gaye.

Bhima ne bhi Krishna ko zor se gale lagaya. Arjuna, Nakula aur Sahadeva bhi bahut khush hue.

Krishna ne sab bade logon aur Brahmano ko pranam kiya.

Indraprastha nagari ko sundar phoolon, jhandon aur sugandhit paani se sajaya gaya tha. Nagar ki sab mahilaayein Krishna ko dekhne ke liye gharon ki chhaton aur raaston par aa gayin.

Woh Krishna aur unki raniyon ko dekhkar bahut prasann hui.

Kunti bua Krishna ko dekhkar bahut khush hui. Unhone pyar se Krishna ko gale lagaya.

Draupadi ne Krishna ki raniyon ka adar aur satkar kiya.

Yudhishthira ne Krishna aur unke saath aaye sab logon ke rehne ka bahut achcha prabandh kiya.

Krishna kai mahine tak Indraprastha mein rahe. Woh Arjuna ke saath van aur nagar mein ghoomte aur sabko khushi dete the."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 72
    with st.expander("Chapter 72 - Jarāsandha slain"):
        text1 = """ 
        Rishi Shukadev bole, “Ek din Raja Yudhishthira apni sabha mein baithe the. Unke saath rishi, Brahman, bhai aur bade-buzurg sab maujood the.

Tab Yudhishthira ne Krishna se kaha,

“Hey Govind, main Rajasuya yagya karna chahta hoon. Kripya aap humein is mahaan yagya ko poora karne mein madad kijiye.”

Yudhishthira bole, “Jo log aapke charanon ki seva karte hain, unka jeevan safal ho jaata hai. Main chahta hoon ki duniya bhi yeh dekhe.”"""
        create_image_text_layout(
            "attached_assets/chapter10/10.72.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Krishna muskuraaye aur bole, “Hey Raja, tumhara sankalp bahut achcha hai. Lekin Rajasuya yagya tabhi ho sakta hai jab sabhi raja tumhare adhin ho jaayein.”

Phir Yudhishthira ne apne bhaiyon ko alag-alag dishaon mein vijay yatra ke liye bhej diya.

Bhima poorab gaye, Arjuna uttar, Nakula pashchim aur Sahadeva dakshin ki taraf gaye.

Sabhi Pandav bahut saara dhan aur vijay lekar wapas aaye.

Lekin Jarasandh ab bhi ajey tha. Yudhishthira usse lekar chintit ho gaye.

Tab Krishna, Bhima aur Arjuna ne Brahman ka roop dharan kiya aur Magadh ki rajdhani Girivraj pahunch gaye.

Woh seedha Raja Jarasandh ke paas gaye.

Jarasandh Brahmano ka bahut samman karta tha. Usne kaha, “Maango, tumhe kya chahiye? Main apna sir bhi de sakta hoon.”

Tab Krishna bole, “Hum Brahman nahi hain. Hum Kshatriya hain aur tumse yudh maangne aaye hain.”

Krishna ne apna parichay diya aur Bhima ki taraf dekhkar kaha, “Yeh Bhimasena hain. Yeh tumse ekal yudh karenge.”

Jarasandh zor se hasa aur bola, “Krishna, tum toh Mathura chhodkar bhaag gaye the. Main tumse nahi ladunga. Lekin Bhima mere barabar balwaan hai. Main usse yudh karunga.”

Dono ne bade-bade gada uthaye aur yudh shuru hua.

Bhima aur Jarasandh ka yudh bahut bhayankar tha. Dono ek doosre par zor-zor se vaar kar rahe the.

Kai din tak yudh chalta raha. Na Bhima haar rahe the aur na Jarasandh.

27 din beet gaye.

Ek din Bhima ne Krishna se kaha, “Main ise hara nahi paa raha.”

Krishna Jarasandh ke janm ka rahasya jaante the. Unhone ek patli si lakdi ko beech se phaadkar Bhima ko sanket diya.

Bhima samajh gaye.

Unhone Jarasandh ko zameen par gira diya. Ek pair apne pair se dabaaya aur doosra pair pakadkar uske sharir ko beech se cheer diya.

Is baar Jarasandh dobara zinda nahi ho paaya.

Sab log hairaan reh gaye.

Krishna aur Arjuna ne Bhima ko gale lagakar badhaai di.

Phir Krishna ne Jarasandh ke bete Sahadeva ko Magadh ka raja bana diya.

Uske baad Jarasandh ke kaid kiye hue sabhi rajaon ko azaad kar diya gaya. Sab raja Krishna ke prati kritagya ho gaye."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 73
    with st.expander("Chapter 73 - Return of Kṛṣṇa and others to Indraprastha"):
        text1 = """ 
        Rishi Shukadev bole, “Jab Jarasandh maara gaya, tab uske kaid kiye hue 20,800 raja azaad kiye gaye.

Woh sab bahut kamzor ho chuke the. Kai dinon se bandi rehne ki wajah se unke kapde gande ho gaye the aur sharir sukhe hue lag rahe the.

Jab unhone Krishna ko dekha, toh unki aankhon mein khushi bhar gayi.

Krishna megh jaise saawle rang ke the. Unhone peele vastra pehne the aur unke haath mein shankh, chakra, gada aur kamal tha. Unke gale mein vanmala aur Kaustubh mani chamak rahi thi.

Sab raja Krishna ko dekhte hi unke charanon mein jhuk gaye."""
        create_image_text_layout(
            "attached_assets/chapter10/10.73.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Woh bole, “Hey Prabhu, hum aapko pranam karte hain. Aapne humein bahut bade dukh se bachaya hai.”

Rajaon ne kaha, “Hum apne raj aur dhan ke ghamand mein andhe ho gaye the. Hum duniya ko hi sab kuch samajhne lage the.”

“Lekin ab humein samajh aa gaya hai ki rajya aur dhan sab kuch ek sapne ki tarah hai. Sirf aapke charan hi sachcha sahara hain.”

Krishna unki baatein sunkar prasann hue.

Unhone pyar se kaha, “Ab tumhara mann mere prati sthir rahega. Hamesha yaad rakho ki dhan, sharir aur shakti sab ek din khatam ho jaate hain.”

Krishna ne unhe seekh di, “Apni praja ki raksha dharma ke saath karo. Sukh-dukh mein samaan raho aur apna mann Bhagwan mein lagao.”

Uske baad Krishna ne sevakon ko aadesh diya ki sab rajaon ko snaan karaya jaaye aur naye vastra, gehne aur bhojan diya jaaye.

Magadh ke naye raja Sahadeva ne bhi sabka bahut adar kiya.

Phir Krishna ne sab rajaon ko sundar rathon mein bitha kar unke rajya wapas bhej diya.

Woh sab raja Krishna ki mahima gaate hue apne-apne desh laut gaye.

Iske baad Krishna, Bhima aur Arjuna Indraprastha ki taraf chale.

Jab woh nagar ke paas pahunche, tab unhone apne shankh bajaaye.

Shankh ki awaaz sunkar Indraprastha ke log samajh gaye ki Jarasandh haar gaya hai.

Sab log bahut khush hue.

Bhima, Arjuna aur Krishna ne Yudhishthira ko poori kahani sunaayi.

Yeh sunkar Yudhishthira ki aankhon mein khushi ke aansu aa gaye. Woh itne prasann hue ki kuch der tak kuch bol hi nahi paaye."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 74
    with st.expander("Chapter 74 - Yudhiṣṭhira’s Rājasūya: Śiśupāla slain"):
        text1 = """ 
        Rishi Shukadev bole, “Jab Yudhishthira ne Jarasandh ki mrityu aur Krishna ki mahima suni, toh woh bahut prasann hue.

Unhone Krishna se kaha, “Hey Prabhu, teenon lok ke devta aur mahan rishi bhi aapke aadesh ko maante hain. Phir bhi aap hum jaise saamanya logon ke saath itne prem se rehte hain. Yeh aapki mahaanta hai.”

Iske baad Yudhishthira ne Rajasuya yagya ki taiyaari shuru kar di.

Vyasa ji, Vashishtha, Vishwamitra, Parashurama aur bahut saare mahan rishi yagya mein bulaaye gaye. Bhishma, Drona, Kripacharya, Dhritarashtra aur Kaurav bhi aaye."""
        create_image_text_layout(
            "attached_assets/chapter10/10.74.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Har taraf utsav jaisa mahaul tha.

Yagya ke din ek bada prashn utha — sabse pehle samman kis vyakti ko diya jaaye? Sabha mein bahut saare mahan log baithe the.

Tab Sahadeva khade hue aur bole,

“Sabse pehla samman Bhagwan Krishna ko milna chahiye. Woh sabke swami hain. Yeh poora jagat unhi se chalta hai.”

Sahadeva ne kaha, “Krishna hi yagya hain, mantra hain aur sabke hriday mein rehne wale Parmatma hain.”

Sabha ke adhiktar log Sahadeva ki baat se sehmat ho gaye.

Yudhishthira bahut khush hue. Unhone Krishna ke charan dhoye aur us pavitra jal ko apne sir par rakha. Unke bhaiyon aur parivaar ne bhi waise hi kiya.

Sab log “Jai Krishna!” kehkar unka samman karne lage. Aasmaan se phoolon ki varsha hone lagi.

Lekin yeh sab dekhkar Chedi raja Shishupala ko bahut gussa aa gaya.

Woh khada hokar chillane laga,

“Yahan itne mahan rishi aur buzurg baithe hain. Phir bhi tum log ek gwale Krishna ko sabse bada samman de rahe ho?”

Usne Krishna ko bahut buri baatein kahi aur unka apmaan karne laga.

Sabha mein baithe logon ko yeh baat bahut buri lagi. Kai logon ne apne kaan band kar liye aur kuch log gusse mein uth khade hue.

Bhima aur doosre yoddha Shishupala ko maarne ke liye taiyaar ho gaye.

Lekin Krishna shaant rahe.

Jab Shishupala hadh paar kar gaya, tab Krishna ne Sudarshan Chakra chala diya.

Ek pal mein Chakra ne Shishupala ka sir kaat diya.

Sab log hairaan reh gaye.

Tab sabne dekha ki Shishupala ke sharir se ek tej nikla aur seedha Krishna mein sama gaya.

Rishi Shukadev bole, “Shishupala teen janmon tak Krishna se dvesh karta raha, lekin uska mann hamesha Krishna mein laga raha. Isi wajah se antim samay mein usse bhi moksha mil gaya.”

Rajasuya yagya safalta se poora hua. Yudhishthira ne sabhi mehmano aur Brahmano ko bahut saare uphaar diye.

Sab log Krishna aur Yudhishthira ki prashansa karte hue apne ghar laut gaye.

Lekin Duryodhana andar hi andar jalan se bhar gaya. Woh Pandavo ki shaan aur samriddhi dekhkar khush nahi tha."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 75
    with st.expander("Chapter 75 - Discomfiture of Duryodhana"):
        text1 = """ 
        Raja Parikshit ne poocha, “Rajasuya yagya ke baad sab log khush the, lekin Duryodhana hi udaas aur jalan se bhara hua kyun tha?”

Rishi Shukadev bole, “Rajasuya yagya bahut shaan se poora hua tha. Har vyakti ko koi na koi zimmedaari di gayi thi.”

Bhima rasoi sambhaal rahe the. Duryodhana khazane ki dekhbhaal kar raha tha. Sahadeva mehmano ka swagat kar rahe the aur Nakula samaan ki vyavastha dekh rahe the.

Arjuna bade-buzurgon ki seva kar rahe the aur Krishna swayam mehmano ke pair dho rahe the.

Draupadi sabko bhojan parosne ka kaam dekh rahi thi. Karna daan aur uphaar baant rahe the."""
        create_image_text_layout(
            "attached_assets/chapter10/10.75.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Yagya poora hone ke baad sab log Ganga ji mein avabhrita snaan ke liye gaye.

Har taraf shankh, dhol aur sangeet ki awaaz gunj rahi thi. Raja, raniyan aur sab log sundar vastra aur gehne pehne hue the.

Log khushi mein ek doosre par sugandhit paani aur kesar chhidak rahe the.

Yudhishthira Draupadi ke saath rath par bahut tejomay lag rahe the. Snaan ke baad unhone sabhi mehmano ko vastra, gehne aur uphaar diye.

Sab log Rajasuya yagya ki safalta dekhkar bahut prasann hue.

Krishna bhi Yudhishthira ko khush karne ke liye kuch aur samay Indraprastha mein ruk gaye.

Lekin Duryodhana ke mann mein jalan bharne lagi.

Usne Pandavo ka bada mahal dekha, jo Maya danav ne banaya tha. Mahal itna adbhut tha ki wahan zameen aur paani mein farq samajhna mushkil ho jaata tha.

Ek din Duryodhana us mahal mein ghoom raha tha.

Jahan saaf zameen thi, usne use paani samajhkar apne kapde upar utha liye. Yeh dekhkar log hans pade.

Thodi der baad jahan sach mein paani tha, usne use zameen samjha aur seedha paani mein gir gaya.

Bhima zor se hansne lage. Doosre raja aur mahal ki mahilaayein bhi muskuraane lagi.

Yudhishthira ne sabko rokne ki koshish ki, lekin Krishna chup rahe.

Duryodhana ka chehra sharm aur gusse se bhar gaya. Usne sir jhuka liya aur bina kuch kahe Hastinapur laut gaya.

Uske mann mein jalan aur dvesh aur bhi badh gaya. Yahi jalan aage chal kar bahut bade sangharsh ka kaaran bani."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 76
    with st.expander("Chapter 76 - Fight with Śālva"):
        text1 = """ 
        Rishi Shukadev bole, “Ab main tumhe Krishna ki ek aur adbhut leela sunata hoon — Shalva ke vinaash ki kahani.”

Shalva, Shishupala ka bahut kareebi dost tha. Jab Krishna Rukmini ko swayamvar se le gaye the, tab Shalva bhi wahan maujood tha aur Yadavo se haar gaya tha.

Us din se woh Krishna se badla lena chahta tha."""
        create_image_text_layout(
            "attached_assets/chapter10/10.76.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Sab rajaon ke saamne usne gusse mein kaha, “Main poori prithvi se Yadavo ka naam mita dunga!”

Iske baad Shalva ne Bhagwan Shiva ki kathin tapasya ki. Woh sirf thodi si dhool khaakar jeevit raha.

Ek saal baad Shiva ji usse prasann ho gaye aur bole, “Maango, kya chahiye?”

Shalva bola, “Mujhe ek aisa udne wala nagar chahiye jise koi devta, manushya ya rakshas na tod sake.”

Shiva ji ne “Tathastu” kaha.

Phir Maya danav ne Shalva ke liye ek lohe ka adbhut vimaan-nagar banaya, jiska naam tha Saubha.

Woh kabhi aasman mein udta, kabhi gayab ho jaata aur kabhi achanak kahin bhi dikhai deta tha.

Kuch samay baad Shalva ko pata chala ki Shishupala aur Jarasandh dono mare gaye hain. Yeh sunkar woh bahut gusse mein bhar gaya.

Usne apni sena ke saath Dwaraka par hamla kar diya.

Saubha vimaan se bade-bade pathar, ped aur hathiyaar barsne lage. Tez aandhi aur dhool se poori Dwaraka pareshan ho gayi.

Log darr gaye.

Tab Pradyumna ne sabko himmat di aur kaha, “Darro mat!”

Pradyumna, Satyaki, Samba, Akrura aur doosre Yadav yoddha sena lekar yudh ke liye nikle.

Bahut bhayankar yudh hua.

Shalva ka Saubha vimaan bahut jadui tha. Kabhi ek jagah dikhai deta, kabhi dusri jagah. Kabhi woh aasman mein hota aur kabhi paani ke upar.

Yadav sena ko samajhna mushkil ho raha tha ki asli Saubha kahaan hai.

Lekin Pradyumna ne apne divya astron se Shalva ki maya ko todna shuru kar diya.

Unhone Shalva aur uski sena par teeron ki baarish kar di. Sab log Pradyumna ki veerta dekhkar hairaan ho gaye.

Tab Shalva ka senapati Dyuman achanak Pradyumna ke paas aaya aur usne lohe ki gada se zor ka vaar kiya.

Pradyumna gambhir roop se ghaayal ho gaye aur kuch der ke liye behosh ho gaye.

Unke saarathi ne turant unhe yudh bhoomi se door le gaya.

Hosh aane par Pradyumna gusse mein bole, “Tum mujhe yudh se bahar kyun laaye? Hamare vansh mein koi yoddha kabhi peeth dikhakar nahi bhaagta!”

Saarathi ne vinamrata se kaha, “Prabhu, yeh mera kartavya tha. Jab yoddha sankat mein ho, toh saarathi ko uski raksha karni chahiye.”

Yeh sunkar Pradyumna shaant ho gaye aur fir se yudh ke liye taiyaar hone lage."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 77
    with st.expander("Chapter 77 - Slaying of King Śālva"):
        text1 = """ 
        Rishi Shukadev bole, “Jab Pradyumna ko hosh aaya, toh unhone fir se apna kavach pehna aur dhanush uthaya. Phir woh bole, “Mujhe turant Dyuman ke paas le chalo!”

Pradyumna fir se yudh bhoomi mein laut aaye.

Unhone haste hue Dyuman par teer chalaaye. Kuch teeron se uske ghodon ko maara, kuch se uska dhanush tod diya aur ek tez teer se uska sir kaat diya."""
        create_image_text_layout(
            "attached_assets/chapter10/10.77.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Doosri taraf Satyaki, Samba, Gada aur doosre Yadav yoddha bhi Shalva ki sena ko haraane lage.

Yeh bhayankar yudh 27 din aur raat tak chalta raha.

Isi beech Krishna Indraprastha se Dwaraka laut rahe the. Raaste mein unhe bure sanket dikhai diye. Unhe laga ki Dwaraka mein kuch bura hua hai.

Jab Krishna Dwaraka pahunche, toh unhone dekha ki nagar toot-phoot gaya hai. Bagiche barbaad ho gaye the aur kai imaaratein toot chuki thi.

Yeh sab dekhkar Krishna dukhi hue.

Tab unhone pratigya ki, “Main Shalva ko maare bina Dwaraka mein pravesh nahi karunga.”

Krishna turant apne Garud chinh waale rath par baithkar Shalva ke peeche nikle.

Jaldi hi unhone aasman mein Saubha vimaan ko dekh liya.

Krishna ne apne saarathi Daruk se kaha, “Mera rath seedha Shalva ke paas le chalo. Darne ki zaroorat nahi.”

Yudh shuru hua.

Shalva ne Krishna ke saarathi par ek bhayanak bhala pheka. Lekin Krishna ne apne teeron se use tukde-tukde kar diya.

Krishna ne kai teer chalaakar Saubha vimaan ko hila diya.

Tab Shalva ne Krishna ke baaye haath par vaar kiya. Ek pal ke liye Krishna ka dhanush neeche gir gaya. Yeh dekhkar sab log hairaan reh gaye.

Shalva ghamand se bola, “Tumne hamare dost Shishupala ko maara tha. Aaj main tumhe bhi khatam kar dunga!”

Krishna shaant swar mein bole, “Asli veer zyada baatein nahi karte. Woh apni shakti yudh mein dikhate hain.”

Itna kehkar Krishna ne apni gada se Shalva par zor ka vaar kiya. Shalva khoon ugalne laga.

Tab Shalva ne apni maya ka prayog kiya.

Achanak ek aadmi Krishna ke paas aaya aur rota hua bola, “Hey Krishna, Shalva ne aapke pita Vasudev ko pakad liya hai!”

Thodi der baad Shalva ek aadmi ko lekar aaya jo bilkul Vasudev ji jaisa lag raha tha.

Shalva chillaya, “Dekho, main tumhare pita ko maar deta hoon!”

Aur usne us aadmi ka sir kaat diya.

Yeh dekhkar Krishna ek pal ke liye dukhi ho gaye, jaise koi aam insaan ho.

Lekin phir unhone samajh liya ki yeh sab Shalva ki jadui maya hai.

Asli Vasudev ji surakshit the.

Tab Krishna ka gussa aur badh gaya.

Unhone Sudarshan Chakra uthaya. Chakra suraj ki tarah chamak raha tha.

Krishna ne use Saubha vimaan ki taraf chala diya.

Ek hi pal mein Sudarshan Chakra ne Saubha ko tukde-tukde kar diya. Vimaan samundar mein girkar toot gaya.

Shalva fir bhi gada lekar Krishna par hamla karne dauda.

Lekin Krishna ne ek teer se uska haath kaat diya.

Uske baad Krishna ne Sudarshan Chakra se Shalva ka sir kaat diya, bilkul waise hi jaise Indra ne Vritrasur ko maara tha.

Aasmaan mein devtaon ne dhol bajaaye aur phool barsaaye.

Krishna vijay paakar Dwaraka laut aaye. Nagar ke log bahut khush hue aur unka bada swagat kiya.

Krishna fir apni raniyon aur Yadavo ke saath khushi se rehne lage."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 78
    with st.expander("Chapter 78 - Dantavaktra and Vidūratha Slain: Balarāma’s Pilgrimage"):
        text1 = """ 
        Rishi Shukadev bole, “Shalva ke marne ke baad uska dost Dantavakra bahut gusse mein bhar gaya. Woh Shishupala, Shalva aur Paundraka ka badla lena chahta tha.

Woh akela hi gada lekar Krishna ki taraf dauda. Uske kadam se zameen hilne lagi.

Krishna ne bhi turant apni Kaumodaki gada uthayi aur uska saamna karne lage.

Dantavakra gusse mein bola, “Krishna! Tum hamare rishtedaar hoke bhi apne doston ko maarte ho. Aaj main tumhe khatam kar dunga!”

Itna kehkar usne Krishna ke sir par zor se gada maari."""
        create_image_text_layout(
            "attached_assets/chapter10/10.78.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Lekin Krishna bilkul nahi hile.

Phir Krishna ne apni gada se Dantavakra ke seene par bahut zor ka prahar kiya.

Dantavakra khoon ugalta hua zameen par gir gaya aur uski mrityu ho gayi.

Sabne dekha ki uske sharir se ek chamakta hua tej nikla aur Krishna mein sama gaya, bilkul Shishupala ki tarah.

Dantavakra ka bhai Viduratha yeh dekhkar bahut dukhi aur gusse mein aa gaya. Woh talwar aur dhal lekar Krishna par hamla karne dauda.

Lekin Krishna ne Sudarshan Chakra se uska sir bhi kaat diya.

Is tarah Krishna ne Dantavakra aur Viduratha dono ka ant kar diya.

Devtaon ne aasman se phool barsaaye aur Krishna ki jai-jaikaar karne lage.

Krishna vijay paakar Dwaraka laut aaye. Nagar ke log bahut khush hue aur bade prem se unka swagat kiya.

Raja Parikshit ne fir poocha, “Jab Mahabharat ka yudh hone wala tha, tab Balarama ji ne kya kiya?”

Rishi Shukadev bole, “Jab Balarama ne dekha ki Kaurav aur Pandav yudh karne par tule hue hain aur koi bhi shanti nahi chahta, tab unhone yudh se door rehne ka faisla kiya.”

Woh bole, “Main dono pakshon se prem karta hoon. Main kisi ek ka saath nahi dunga.”

Isliye Balarama teerth yatra par nikal gaye.

Woh Prabhas, Saraswati nadi aur kai pavitra sthalon par gaye. Har jagah snaan kiya, devtaon aur rishiyon ko pranam kiya aur Brahmano ko daan diya.

Aakhir mein woh Naimisharanya pahunche, jahan bahut saare rishi yagya kar rahe the.

Sabhi rishi Balarama ko dekhkar khade ho gaye aur unka samman kiya.

Lekin Romaharshana Suta naam ka ek kathavachak apni jagah par hi baitha raha. Usne na pranam kiya aur na hi samman dikhaya.

Yeh dekhkar Balarama ko gussa aa gaya.

Unhone kaha, “Sirf gyaan hona hi kaafi nahi hota. Vinamrata aur achcha vyavahar bhi zaroori hai.”

Phir Balarama ne ek chhoti si kush ghaas uthayi aur usse hi Romaharshana ko maar diya.

Sab rishi darr gaye aur bole, “Hey Balarama, yeh theek nahi hua. Woh hamare dwara sammanit vyakti tha.”

Balarama shaant hokar bole, “Agar mujhse galti hui hai, toh main iska prayaschit karunga. Aap jo kahenge, main wahi karunga.”

Rishiyon ne kaha, “Balvala naam ka ek dusht danav humein pareshaan karta hai. Har poornima aur amavasya ko woh hamare yagya ko ashuddh kar deta hai. Aap uska vadh kijiye.”

Balarama ne unki baat maan li aur danav ko maarne ke liye taiyaar ho gaye."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 79
    with st.expander("Chapter 79 - Balvala Killed: Balarāma’s Pilgrimage"):
        text1 = """ 
        Rishi Shukadev bole, “Jab agla poornima ka din aaya, tab achanak tez aandhi chalne lagi. Har taraf dhool aur buri badboo fail gayi.

Phir aasman se gandagi, khoon aur gandi cheezein yagya bhoomi par girne lagi. Yeh sab dusht danav Balvala kar raha tha.

Kuch der baad Balvala khud saamne aaya. Woh bahut bada aur bhayanak lag raha tha. Uska sharir kaale pahad jaisa tha aur uske daant aur aankhen darawni thi.

Yeh dekhkar Balarama ne apna hal aur musal yaad kiya. Dono divya hathiyaar turant unke paas aa gaye.

Balvala aasman mein ud raha tha. Balarama ne apne hal se use kheenchkar neeche gira diya.

Phir unhone apne musal se uske sir par bahut zor ka vaar kiya."""
        create_image_text_layout(
            "attached_assets/chapter10/10.79.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Balvala zor se cheekha aur khoon bahaate hue zameen par gir gaya, bilkul vajra se toote pahad ki tarah.

Sabhi rishi bahut khush ho gaye. Unhone Balarama ki jai-jaikaar ki aur pavitra jal se unka abhishek kiya.

Rishiyon ne Balarama ko sundar Vaijayanti mala, vastra aur gehne bhi diye.

Uske baad Balarama ne apni teerth yatra jaari rakhi.

Woh Kaushiki nadi, Sarayu, Prayag, Gomati, Gandaki aur kai pavitra nadiyon aur teerthon par gaye. Har jagah snaan kiya, devtaon aur pitron ko jal arpit kiya aur Brahmano ko daan diya.

Woh Shri Rangam, Kanchi, Venkat parvat aur Rameshwaram jaise pavitra sthalon par bhi gaye.

Setu par Balarama ne Brahmano ko hazaaron gaayein daan mein di.

Baad mein woh Agastya rishi se mile aur unka aashirvaad liya.

Yatra karte-karte Balarama ko pata chala ki Mahabharat ka yudh lagbhag samaapt ho gaya hai aur adhiktar Kshatriya maare ja chuke hain.

Yeh sunkar woh Kurukshetra pahunche.

Wahan Bhima aur Duryodhana gada yudh kar rahe the. Dono bahut gusse mein the.

Balarama ne unhe rokne ki koshish ki.

Woh bole, “Tum dono bahut shaktishaali ho. Yeh yudh ab band kar do. Isse kisi ka bhala nahi hoga.”

Lekin Bhima aur Duryodhana ne unki baat nahi maani.

Balarama samajh gaye ki ab yeh sab bhagya ka hissa hai. Isliye woh chup-chaap Dwaraka laut gaye.

Baad mein woh fir Naimisharanya gaye aur wahan rishiyon ke saath milkar yagya kiya.

Balarama ne rishiyon ko adhyatmik gyaan bhi diya. Unhone samjhaaya ki poora jagat Bhagwan mein hi basa hai.

Rishi Shukadev bole, “Jo vyakti subah-shaam Balarama ji ki in pavitra leelaon ko yaad karta hai, woh Bhagwan Vishnu ka priya ban jaata hai.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 80(a)
    with st.expander("Chapter 80(a) - The Story of the Brāhmaṇa Śrīdāman (introductory)"):
        text1 = """ 
        Rishi Shukadev bole, “Jab Bhima ne gada yudh mein Duryodhana ko hara diya, tab Mahabharat ka yudh samaapt ho gaya. Krishna ka dharti ka bojh kam karne ka uddeshya bhi poora ho chuka tha.

Kauravo ki sena mein sirf Kripacharya, Kritavarma aur Ashwatthama jaise kuch hi bade yoddha bache the. Pandavo ki taraf se paanch Pandav, Satyaki aur kuch anya veer bach gaye the.

Yudh ke baad Krishna Hastinapur gaye."""
        create_image_text_layout(
            "attached_assets/chapter10/10.80a.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Wahan unhone andhe raja Dhritarashtra, dukhi Gandhari aur buddhimaan Vidura ko santvana di. Sab apne putron aur parivaar ke vinaash se bahut dukhi the.

Krishna ne pyar aur dhairya se sabko sambhala.

Uske baad unhone Yudhishthira ko rajya sambhalne ke liye taiyaar kiya.

Phir Krishna Dwaraka lautne lage.

Pandav unse bichhadte waqt bahut udaas ho gaye. Unki aankhon mein aansu aa gaye.

Krishna suraj ki tarah chamakne wale rath par baithkar Dwaraka ki taraf chale.

Jab Dwaraka ke logon ko pata chala ki Krishna laut rahe hain, tab poori nagari ko sajaya gaya.

Har taraf jhande, phool aur sundar toran lagaye gaye. Raaston par sugandhit paani chhidka gaya.

Brahman, mahilaayein aur bachche sab Krishna ka swagat karne aaye. Sabke haath mein phool, deepak aur kalash the.

Shankh aur dhol ki awaaz se poori Dwaraka gunj uthi.

Krishna nagar mein pravesh karte hue bahut tejomay lag rahe the.

Sabse pehle woh Sudharma sabha mein gaye. Wahan unhone Vasudev ji, Balarama aur apni sabhi maataon ko pranam kiya.

Yadav logon ne bade prem aur samman se Krishna ka swagat kiya.

Krishna sabke beech waise chamak rahe the jaise taare aur grahon ke beech poornima ka chand chamakta hai.

Mahabharat ke baad jo raja bach gaye the, woh bhi Krishna ka adar karte the. Krishna ne Yudhishthira ko dharti ka sachcha samrat bana diya aur unki madad se dharma ke saath rajya chalne laga.

Is tarah Krishna Dwaraka mein shaanti aur prem ke saath rehne lage."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 80(b)
    with st.expander("Chapter 80(b) - The Story of the Brāhmaṇa Śrīdāman"):
        text1 = """ 
        Raja Parikshit ne kaha, “Hey Rishi, Krishna ki aur pavitra leelaayein sunaaiye. Unki kathayein sunne se mann ko shanti milti hai.”

Rishi Shukadev bole, “Sach mein, wahi jeebh safal hai jo Bhagwan ki mahima gaaye. Wahi kaan safal hain jo unki kathayein sune.”

Phir Shukadev ji ne ek gareeb Brahman ki kahani sunani shuru ki.

Woh Brahman Krishna ka purana mitra tha. Kuch log use Shridaman ke naam se jaante the."""
        create_image_text_layout(
            "attached_assets/chapter10/10.80b.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Woh bahut gyani aur shaant swabhav ka tha. Lekin woh aur uski patni bahut gareebi mein jeevan bita rahe the.

Unke paas achche kapde aur poora bhojan bhi nahi hota tha. Fir bhi woh imaandari aur santosh ke saath jeete the.

Ek din uski patni ne dheere se kaha,

“Hey Swami, aapke mitra Krishna ab Dwaraka ke raja hain. Woh Brahmano aur bhakton se bahut prem karte hain. Aap unse milne kyun nahi jaate?”

Woh boli, “Krishna dayaalu hain. Shayad woh hamari madad kar dein.”

Brahman ne shaant swar mein kaha, “Mujhe dhan nahi chahiye. Lekin Krishna ka darshan zaroor karna chahta hoon.”

Phir usne poocha, “Lekin hum Krishna ke liye uphaar mein kya le jaa sakte hain?”

Uski patni pados ke Brahmano ke ghar gayi aur mushkil se chaar mutthi poha maangkar laayi.

Usne un poho ko ek purane kapde mein baandh diya aur kaha, “Yahi Krishna ko prem se de dijiyega.”

Brahman poha lekar Dwaraka ki taraf chal diya. Raaste bhar woh bas Krishna ke baare mein sochta raha.

Dwaraka pahunchkar woh Krishna ke mahal tak gaya.

Krishna ne door se hi apne purane dost ko dekh liya.

Woh turant apne singhasan se uth gaye aur daudkar Brahman ko gale laga liya.

Krishna ki aankhon mein khushi ke aansu aa gaye.

Phir Krishna ne apne mitra ko apne hi aasana par bithaya aur swayam unke pair dhoye.

Unhone us pavitra jal ko apne sir par rakha.

Rukmini ji bhi pankha lekar Brahman ki seva karne lagi.

Mahal ki sab mahilaayein hairaan thi. Woh sochne lagi, “Yeh gareeb aur saadhaaran Brahman kaun hai, jise Krishna itna adar de rahe hain?”

Krishna aur Brahman dono purane din yaad karne lage.

Krishna muskuraakar bole, “Kya tumhe apne Guru Sandipani ka ashram yaad hai?”

Phir Krishna ne ek purani ghatna sunayi.

Woh bole, “Ek baar Guru Mata ne humein jungle se lakdiyaan laane bheja tha. Tab achanak tez aandhi aur baarish shuru ho gayi.”

“Har taraf andhera ho gaya tha. Hum dono jungle mein raasta bhatak gaye the.”

“Humne ek doosre ka haath pakadkar poori raat mushkil mein bitaayi.”

“Subah Guru Sandipani humein dhoondte hue aaye. Unhone humari guru-bhakti dekhkar bahut khushi se aashirvaad diya tha.”

Krishna bole, “Guru ki seva aur aashirvaad se hi jeevan safal hota hai.”

Brahman vinamrata se bola, “Hey Krishna, aap toh sabke Guru aur Bhagwan hain. Aapke saath rehkar hi sab kuch safal ho jaata hai.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 81
    with st.expander("Chapter 81 - The Story of the Parched Rice (The story of Śrīdāman continued)"):
        text1 = """ 
        Rishi Shukadev bole, “Jab Krishna apne gareeb Brahman mitra se purani baatein kar rahe the, tab woh muskuraakar bole,

‘Hey Brahman mitra, tum mere liye ghar se kya uphaar laaye ho?’

Krishna haste hue bole,

‘Mere bhakt prem se agar ek patta, phool, phal ya thoda sa paani bhi dete hain, toh mujhe woh bahut priya lagta hai.’"""
        create_image_text_layout(
            "attached_assets/chapter10/10.81.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Brahman yeh sunkar sharma gaye. Unke paas sirf thoda sa poha tha, jo unki patni ne mushkil se maangkar diya tha.

Woh use dene mein jhijhak rahe the aur chupchaap sir jhuka kar baithe rahe.

Lekin Krishna toh sabke mann ki baat jaante the.

Unhone mann hi mann socha,

‘Mera yeh mitra dhan ke liye kabhi mere paas nahi aaya. Yeh sirf apni patni ko khush karne ke liye yahaan aaya hai. Main ise aisa dhan dunga jo devtaon ko bhi mushkil se milta hai.’

Yeh sochkar Krishna ne khud Brahman ke kapde ke andar bandha hua pohe ka potli nikaal li.

Krishna khushi se bole,

‘Arey! Yeh toh poha hai. Mujhe yeh bahut pasand hai!’

Phir Krishna ne prem se ek mutthi poha kha liya.

Jab woh doosri mutthi lene lage, tab Rukmini ji ne pyar se unka haath pakad liya.

Woh boli,

‘Prabhu, bas ek mutthi hi kaafi hai. Isse hi inhe iss janm aur agle janm ki saari samriddhi mil jaayegi.’

Us raat Brahman Krishna ke mahal mein bade sukh se rahe. Unhe swarg jaisa anubhav ho raha tha.

Agli subah woh ghar ke liye nikal pade.

Krishna kuch door tak khud unke saath chale aur mitra ki tarah pyar se baatein karte rahe.

Raaste mein Brahman sochne lage,

‘Krishna ne mujhe kitna prem diya. Main toh bahut gareeb hoon, phir bhi unhone mujhe gale lagaya.’

‘Rukmini ji ne bhi meri seva ki. Krishna ne mere pair dhoye aur mujhe devta jaise samman diya.’

Phir Brahman ne socha,

‘Shayad Krishna ne mujhe dhan isliye nahi diya, kyunki adhik dhan se insaan ghamandi ho jaata hai aur Bhagwan ko bhool jaata hai.’

Aisa sochte-sochte woh apne ghar ke paas pahunche.

Lekin wahan pahunchkar woh hairaan reh gaye.

Jahan pehle unki chhoti si jhopdi thi, wahan ab ek bada sundar mahal khada tha. Woh suraj aur chand ki tarah chamak raha tha.

Uske aas-paas sundar bagiche, talaab aur phool khile hue the. Pakshi madhur awaaz mein gaa rahe the.

Sundar sevak aur sevikaayein unka swagat karne bahar aaye.

Brahman samajh hi nahi paaye ki yeh sab kaise ho gaya.

Tab unki patni bahar aayi. Ab woh bhi Devi Lakshmi ki tarah sundar aur tejomayi lag rahi thi.

Uski aankhon mein khushi ke aansu bhar aaye.

Brahman apni patni ke saath us bade mahal mein gaye. Andar sab kuch heere, moti aur sundar ratnon se saja hua tha.

Lekin itni samriddhi milne ke baad bhi Brahman ka mann vinamr aur shaant raha.

Woh sochne lage,

‘Yeh sab Krishna ki kripa hai. Woh apne bhakton ko bina maange bhi sab kuch de dete hain.’

‘Krishna bahut dayaalu hain. Woh chhoti si bhent ko bhi bahut bada maan lete hain, agar usmein prem ho.’

Brahman ne prarthana ki,

‘Har janm mein mujhe Krishna ka prem, unki mitrata aur unki bhakti milti rahe.’

Rishi Shukadev bole, “Is tarah Krishna ke Brahman mitra ne prem aur bhakti ke bal par ant mein Bhagwan ka divya dham prapt kiya.”

“Jo vyakti is pavitra kahani ko shraddha se sunta hai, uske mann mein bhi Bhagwan ke prati bhakti badhne lagti hai.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 82
    with st.expander("Chapter 82 - Meeting of Vṛṣṇis and Gopas of Vṛndāvana"):
        text1 = """ 
        Rishi Shukadev bole, “Ek baar Dwaraka mein rehte hue Krishna aur Balarama ko pata chala ki jaldi hi surya grahan hone wala hai.

Dharmik log ise bahut pavitra samay maante the, isliye Bharat ke har kone se log Kurukshetra ke pavitra teerth Syamantapanchaka jaane lage.

Yahi wahi jagah thi jahan Bhagwan Parashurama ne purane samay mein Kshatriyo ke vinaash ke baad yagya kiya tha."""
        create_image_text_layout(
            "attached_assets/chapter10/10.82.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Krishna bhi apni 16,000 raniyon, putron, sena aur Yadav parivaar ke saath wahan gaye.

Raaste bhar shankh, dhol aur Vedic mantron ki awaaz gunj rahi thi. Sab log “Krishna! Govinda!” ka naam ga rahe the.

Kurukshetra pahunchkar logon ne snaan kiya, vrat rakha aur Brahmano ko gaayein, vastra aur sona daan diya.

Wahan desh ke bahut saare raja aur rishi bhi aaye hue the.

Krishna aur Yadav logon ne Matsya, Kuru, Kekaya, Madra aur kai anya deshon ke rajaon se milkar unka swaagat kiya.

Tabhi Nanda Baba aur Gokul ke gop bhi Krishna se milne aaye. Unke saath doodh aur makhan se bhari bail-gaadiyaan thi.

Krishna aur Balarama ne jaise hi Nanda Baba aur Yashoda Maiya ko dekha, woh bahut khush ho gaye.

Dono bhai turant unke paas gaye aur prem se unhe gale laga liya.

Yashoda Maiya ne dono ko apni god mein bithaya aur unhe gale lagakar aansuon se bhigone lagi. Bahut saalon baad apne laadle bachchon ko dekhkar unka dukh door ho gaya.

Devaki aur Rohini bhi Yashoda ko gale lagakar boli,

“Hey Vraja ki rani, tumhara upkaar kabhi nahi chukaya ja sakta.”

“Tumne Krishna aur Balarama ko apne bachchon ki tarah paala aur hamesha unki raksha ki.”

Udhar Gopiyan bhi Krishna ko dekhkar bhaavuk ho gayin.

Woh itni der tak Krishna ko dekhna chahti thi ki unhe palkein jhapakna bhi bura lag raha tha.

Unhone mann hi mann Krishna ko gale laga liya.

Krishna ne un sabse alag-alag milkar prem se baat ki.

Woh muskuraakar bole,

“Hey priya saathiyon, kya tum humein yaad karti ho? Hum apne parivaar aur dushmano ke kaam mein uljhe rahe, isliye tumse door rahe.”

“Lekin milna aur bichhadna sab Bhagwan ki ichchha se hota hai.”

“Tumhare mann mein jo prem aur bhakti mere liye hai, wahi tumhe antim sachchai aur moksha tak pahunchayegi.”

Krishna ne unhe samjhaaya ki Bhagwan har jeev ke andar aur baahar dono jagah hote hain.

Yeh adhyatmik gyaan sunkar Gopiyon ka mann shaant ho gaya. Unka prem aur bhakti aur bhi gehra ho gaya.

Phir sab log prem aur khushi ke saath ek doosre ki baatein sunte aur Krishna ki leelaon ko yaad karte rahe.

Rishi Shukadev bole, “Jo vyakti Krishna aur Gopiyon ke is pavitra milan ki kahani shraddha se sunta hai, uske mann mein bhi Bhagwan ke prati shuddh bhakti jagti hai.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 83
    with st.expander("Chapter 83 - Narration of Their Marriage Episodes by Kṛṣṇa’s Consorts"):
        text1 = """ 
        Rishi Shukadev bole, “Kurukshetra mein sab log Krishna ki mahima ga rahe the aur unki leelaon ki baatein kar rahe the.

Tab Draupadi ne Krishna ki raniyon se pyaar se poocha,

‘Hey Rukmini, Satyabhama, Jambavati aur Krishna ki sabhi priya raniyon, humein bataaiye ki Krishna ne aapse vivaah kaise kiya?’

Sab raniyan muskuraane lagi aur ek-ek karke apni kahani sunane lagi.

Sabse pehle Rukmini ji boli,"""
        create_image_text_layout(
            "attached_assets/chapter10/10.83.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        “Jab mere bhai mujhe zabardasti Shishupala se vivaah karwana chahte the, tab Krishna sher ki tarah aaye aur mujhe sab rajao ke beech se utha kar le gaye.”

Satyabhama boli,

“Mere pita ne galti se Krishna par Syamantak mani churaane ka ilzaam lagaya tha. Lekin Krishna ne sach saamne laakar mani wapas de di.”

“Tab mere pita ko apni galti ka ehsaas hua aur unhone mera vivaah Krishna se kar diya.”

Jambavati boli,

“Mere pita Jambavan pehle Krishna ko pehchaan nahi paaye. Unhone 27 din tak Krishna se yudh kiya.”

“Baad mein unhe samajh aaya ki Krishna hi Bhagwan Ram hain. Tab unhone mujhe Krishna ko samarpit kar diya.”

Kalindi boli,

“Main Krishna ko pati ke roop mein paane ke liye tapasya kar rahi thi. Krishna ne mujhe dekha aur apna liya.”

Bhadra boli,

“Krishna ne mere swayamvar mein sab rajao ko hara diya aur mujhe Dwaraka le aaye.”

Satya boli,

“Mere pita ne saat bahut balwaan saand rakhe the. Jo unhe kabu kar leta, wahi mujhse vivaah kar sakta tha.”

“Krishna ne bachchon ki tarah aasani se un saandon ko niyantrit kar liya aur mujhe jeet liya.”

Mitravinda boli,

“Mera mann pehle se hi Krishna mein laga hua tha. Isliye mere pita ne khushi se mera vivaah unse kar diya.”

Phir Lakshmana apni kahani sunane lagi.

Woh boli,

“Main Narad ji se Krishna ki mahaan leelaayein sunkar unse prem karne lagi thi.”

“Mere pita ne mere swayamvar mein ek kathin pareeksha rakhi.”

“Ek machhli ko upar ghumaya gaya aur neeche paani mein uski parchhaai dikh rahi thi. Jo dhanurdhari us parchhaai ko dekhkar machhli ko maar deta, wahi mujhse vivaah karta.”

“Bahut saare mahan raja aaye — Jarasandh, Shishupala, Duryodhana aur Karna bhi.”

“Kuch dhanush bhi nahi chadha paaye. Kuch machhli ko dekh hi nahi paaye.”

“Arjuna ne bhi prayas kiya, lekin teer sirf machhli ko chhoo kar nikal gaya.”

“Tab Krishna uthkar aaye.”

“Unhone aasani se dhanush uthaya, paani mein parchhaai dekhi aur ek hi teer mein machhli ko gira diya.”

“Sab jagah shankh aur dhol bajne lage. Devtaon ne phool barsaaye.”

“Main sharmaate hue Krishna ke paas gayi aur unke gale mein varmala daal di.”

“Lekin doosre raja gusse mein aa gaye aur Krishna par hamla kar diya.”

“Krishna mujhe rath mein bithakar sher ki tarah sabke beech se nikal gaye aur sab rajao ko hara diya.”

Uske baad 16,000 raniyon ki taraf se kuch raniyan boli,

“Humein Bhaumasura ne bandi bana rakha tha. Krishna ne us dusht ko maar kar humein azaad kiya.”

“Krishna ne daya karke hum sabse vivaah kiya.”

“Hum na swarg maangti hain, na rajya aur na moksha. Humein sirf Krishna ke charanon ki seva chahiye.”

“Wahi hamare liye sabse bada sukh hai.”

Rishi Shukadev bole, “Is tarah Krishna ki sabhi raniyon ne prem aur bhakti se apni vivaah ki kahaniyaan sunaayi. Unka mann hamesha Krishna mein hi laga rehta tha.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 84
    with st.expander("Chapter 84 - Vasudeva’s Sacrifice"):
        text1 = """ 
        Rishi Shukadev bole, “Jab sab raniyon ne Krishna ke vivaah ki kahaniyaan sunaayi, tab Kunti, Gandhari, Draupadi aur sab Gopiyan bahut bhaavuk ho gayin. Unki aankhon mein khushi ke aansu aa gaye.

Isi samay bahut saare mahan rishi Krishna aur Balarama se milne aaye.

Unmein Vyasa ji, Narad ji, Vishwamitra, Parashurama, Vashishtha, Bhrigu, Kashyap, Atri, Markandeya aur kai mahan tapasvi shamil the.

Sab raja, Pandav, Krishna aur Balarama turant khade ho gaye aur bade adar se rishiyon ko pranam kiya.

Krishna ne unhe aasan, phool, chandan aur pair dhone ke liye jal arpit kiya.

Jab sab shaant hokar baith gaye, tab Krishna vinamrata se bole,"""
        create_image_text_layout(
            "attached_assets/chapter10/10.84.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        “Aaj hum bahut dhanya ho gaye hain. Aap jaise mahan yogiyon ka darshan devtaon ko bhi mushkil se milta hai.”

Krishna ne kaha,

“Teerth aur murtiyaan dheere-dheere pavitra karti hain, lekin mahan sant toh sirf apne darshan se hi logon ko pavitra kar dete hain.”

“Jo vyakti sirf shareer aur sansaar ko sach maanta hai aur santon ka adar nahi karta, woh moorkh hai.”

Krishna ki gehri baatein sunkar sab rishi kuch der chup ho gaye.

Phir woh muskuraakar bole,

“Hey Prabhu, aap sach mein adbhut hain. Aap sabke swami hoke bhi aam manushya ki tarah vyavahar karte hain.”

“Aap hi sansaar ko rachate, sambhalte aur samaapt karte hain. Fir bhi aap kisi cheez se bandhe nahi hote.”

“Bhakton ki raksha aur dushton ko rokne ke liye hi aap yug-yug mein avataar lete hain.”

Rishiyon ne Krishna ko pranam kiya aur apne ashramon ko lautne lage.

Tab Krishna ke pita Vasudev vinamrata se unke paas aaye aur bole,

“Hey mahan rishiyon, kripya bataaiye ki kaise insaan apne karmo ke bandhan se mukt ho sakta hai?”

Narad ji bole,

“Yeh koi aashcharya nahi hai ki aap Krishna ko apna beta samajhkar yeh prashn pooch rahe hain.”

“Bhagwan paas hote hue bhi log unki asli mahima ko nahi samajh paate.”

Rishiyon ne kaha,

“Bhagwan Vishnu ki bhakti aur yagya se mann pavitra hota hai.”

“Grihastha ko imaandari se kamaaye dhan se yagya, daan aur dharma karna chahiye.”

“Insaan par devtaon, rishiyon aur purvajon ka rin hota hai. Inhe dharm se poora karna chahiye.”

“Hey Vasudev, aapne Bhagwan Krishna ki bhakti ki hai. Isi wajah se Bhagwan swayam aapke putra bane.”

Yeh sunkar Vasudev bahut prasann hue.

Unhone rishiyon se yagya karvaane ki prarthana ki.

Phir Kurukshetra mein bade-bade yagya hue. Har taraf dhol, shankh aur Vedic mantron ki awaaz gunjne lagi.

Vasudev aur unki raniyon ne sundar vastra aur gehne pehne.

Krishna, Balarama, Yadav aur sab raja bhi utsav mein shaamil hue.

Yagya ke baad Vasudev ne Brahmano ko gaayein, bhoomi, sona aur bahut saare uphaar daan diye.

Sab logon ko bhojan karaya gaya — Brahman, raja, aam log aur jaanwaron tak ko bhi.

Uske baad sab raja aur rishi Krishna ki prashansa karte hue apne-apne rajyon ko lautne lage.

Nanda Baba bhi kuch samay tak Krishna aur Balarama ke paas rahe.

Ek din Vasudev ne pyar se Nanda Baba ka haath pakadkar kaha,

“Bhai Nanda, tumhara prem aur mitrata bahut mahaan hai. Tumne hamesha hamara saath diya.”

“Hum tumhara upkaar kabhi nahi chuka sakte.”

“Rajya aur dhan kabhi-kabhi insaan ko andha bana dete hain. Isi wajah se hum tumhari seva poori tarah nahi kar paaye.”

Yeh kehkar Vasudev ki aankhon mein aansu aa gaye.

Nanda Baba bhi Krishna aur Balarama se bichhadne ka sochkar udaas ho gaye.

Kuch samay baad woh Gopon aur Gopiyon ke saath Vraj laut gaye.

Lekin unka mann hamesha Krishna ke charanon mein hi laga raha."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 85
    with st.expander("Chapter 85 - Restoration of his Elder Brothers by Kṛṣṇa (from the Realm of Death)"):
        text1 = """ 
        Rishi Shukadev bole, “Kurukshetra ke yagya ke baad ek din Krishna aur Balarama apne mata-pita Vasudev aur Devaki ko pranam karne gaye.

Vasudev ne prem se dono ko gale lagaya. Ab unhe poori tarah samajh aa chuka tha ki Krishna aur Balarama aam putra nahi, balki swayam Parmatma hain.

Woh bhaavuk hokar bole,

“Hey Krishna, hey Balarama! Ab mujhe samajh aa gaya hai ki aap dono hi is poore brahmand ke kaaran hain.”

“Surya ka prakash, agni ki garmi, chand ki shitalta aur dharti ki sugandh — sab aap hi hain.”

“Sab jeev aapki Maya mein bandhkar sansaar mein bhatak rahe hain.”

“Main bhi moha mein padkar aapko sirf apna beta samajhta raha.”"""
        create_image_text_layout(
            "attached_assets/chapter10/10.85.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        “Ab main aapke charanon mein sharan leta hoon.”

Krishna muskuraaye aur vinamrata se bole,

“Pitashri, aapne bahut gehri gyaan ki baat kahi hai.”

“Sab jeev ek hi Parmatma ke roop hain. Farq sirf shareer aur Maya ki wajah se dikhai deta hai.”

Rishi Shukadev bole, “Krishna ki baatein sunkar Vasudev ka mann shaant ho gaya.”

Tab Devaki wahan baithi hui thi. Unhe yaad aaya ki Krishna aur Balarama ne apne Guru Sandipani ke mare hue putra ko wapas lauta diya tha.

Unki aankhon mein aansu aa gaye.

Devaki boli,

“Hey Krishna, hey Balarama! Kans ne mere chhe bachchon ko janm lete hi maar diya tha.”

“Agar aap chahein, toh kripya mujhe mere un bachchon ka ek baar darshan kara dijiye.”

Krishna aur Balarama ne turant Yogmaya ka sahara liya aur Sutal lok chale gaye.

Wahan Raja Bali rehte the.

Jaise hi Bali ne Krishna aur Balarama ko dekha, woh turant khade ho gaye aur unke charanon mein gir pade.

Unhone bade prem se unke pair dhoye aur unka swagat kiya.

Bali bhaavuk hokar bole,

“Hey Prabhu, aapka darshan devtaon ko bhi mushkil se milta hai. Aaj hum bahut dhanya ho gaye.”

Krishna ne Bali se kaha,

“Devaki ke jo chhe putra Kans ne maare the, woh ab tumhare paas hain. Hum unhe apni mata ko dikhane ke liye le jaana chahte hain.”

Krishna ne bataya ki woh bachche pehle ek purane shraap ki wajah se Asur yoni mein janme the.

Ab unhe mukti dene ka samay aa gaya tha.

Bali ne vinamrata se un chhe bachchon ko Krishna ko saunp diya.

Phir Krishna aur Balarama un bachchon ko lekar Dwaraka laut aaye.

Jab Devaki ne apne bachchon ko dekha, toh unki aankhon se khushi ke aansu behne lage.

Unhone sab bachchon ko gale laga liya aur baar-baar unka sir choomne lagi.

Maa ka prem dekhkar unke stanon se doodh bhi bahne laga.

Bachchon ne woh doodh piya jo pehle Krishna ne bhi piya tha.

Krishna ke sparsh aur us pavitra doodh ke prabhav se unhe apna asli divya gyaan wapas mil gaya.

Phir un chhe bachchon ne Krishna, Balarama, Vasudev aur Devaki ko pranam kiya.

Sabke dekhte hi dekhte woh divya roop dharan karke swarg ki taraf chale gaye.

Devaki yeh sab dekhkar hairaan reh gayin. Woh samajh gayin ki Krishna ki Maya aur shakti sach mein adbhut hai.

Rishi Shukadev bole, “Krishna ki aisi anek adbhut leelaayein hain, jinhe gin paana mushkil hai.”

“Jo vyakti shraddha se Krishna ki in pavitra kathaaon ko sunta ya sunaata hai, uska mann Bhagwan mein lagne lagta hai aur use antim mein param shanti milti hai.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 86
    with st.expander("Chapter 86 - Elopement of Subhadrā: The Lord’s Grace on Śrutadeva"):
        text1 = """ 
        Raja Parikshit ne poocha, “Hey Rishi, mere dada Arjuna ne Krishna aur Balarama ki behen Subhadra se vivaah kaise kiya?”

Rishi Shukadev bole, “Ek samay Arjuna teerth yatra par nikle hue the. Yatra karte-karte woh Prabhas kshetra pahunche.”

Wahan unhe pata chala ki Balarama Subhadra ka vivaah Duryodhana se karna chahte hain.

Yeh sunkar Arjuna chintit ho gaye, kyunki woh Subhadra se prem karte the.

Isliye Arjuna ne ek sanyasi ka roop dharan kar liya. Woh trishul nahi, balki teen dand waale tapasvi jaise kapde pehenkar Dwaraka pahunch gaye."""
        create_image_text_layout(
            "attached_assets/chapter10/10.86.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Barish ke chaar mahine woh wahin chupkar rahe.

Balarama unhe pehchaan nahi paaye aur bade adar se unki seva karte rahe.

Ek din Balarama ne unhe mahal mein bhojan ke liye bulaya.

Wahin Arjuna ne pehli baar Subhadra ko dekha.

Subhadra bhi Arjuna ko dekhkar unse prem karne lagi. Dono chup-chaap ek doosre ko dekhkar muskuraane lage.

Arjuna mann hi mann sochne lage ki Subhadra ko kaise apna banaya jaaye.

Krishna sab samajh rahe the. Unhone bhi Arjuna ka saath diya.

Ek din ek bade utsav ke samay Subhadra mandir darshan ke liye rath par nikli.

Tab Arjuna turant rath par chadh gaye aur Subhadra ko lekar wahan se nikal pade.

Jab Yadav sainikon ne rokne ki koshish ki, tab Arjuna ne dhanush uthakar sabko peeche hata diya.

Woh sher ki tarah Subhadra ko lekar chale gaye.

Yeh khabar sunkar Balarama bahut gusse mein aa gaye.

Lekin Krishna aur doosre logon ne unhe shaant kiya.

Unhone samjhaaya ki Arjuna bahut mahaan yoddha hain aur Subhadra bhi unse prem karti hain.

Yeh sunkar Balarama ka gussa shaant ho gaya.

Phir unhone khushi se Subhadra aur Arjuna ko bahut saare uphaar bheje — haathi, ghode, rath, dhan aur sevak-sevikaayein bhi.

Is tarah Arjuna aur Subhadra ka vivaah prem aur khushi ke saath sampann hua.

Rishi Shukadev bole, “Ab main Krishna ke do mahaan bhakton ki kahani sunata hoon.”

Mithila nagari mein Shrutadeva naam ke ek gareeb Brahman rehte the.

Woh bahut gyani, shaant aur santusht the. Unke paas zyada dhan nahi tha, lekin woh hamesha Krishna ki bhakti mein khush rehte the.

Usi Mithila mein Bahulashva naam ke raja bhi rehte the. Woh bhi Krishna ke bahut bade bhakt the.

Krishna dono bhakton se bahut prem karte the.

Ek din Krishna Narad ji, Vyasa ji aur kai mahan rishiyon ke saath Mithila ki taraf chale.

Raaste mein har gaon aur nagar ke log phool aur uphaar lekar Krishna ka swagat karne aaye.

Jab Mithila ke logon ko pata chala ki Krishna aa rahe hain, tab poori nagari khushi se bhar gayi.

Raja Bahulashva aur Brahman Shrutadeva dono Krishna ko apne ghar bulana chahte the.

Krishna sabko khush karna chahte the.

Isliye unhone apni Yogmaya se ek saath do roop dharan kiye.

Ek roop Raja Bahulashva ke mahal gaya aur doosra roop gareeb Brahman Shrutadeva ke ghar.

Raja Bahulashva ne bade aadar se Krishna aur rishiyon ke pair dhoye, unhe sundar aasan diye aur bahut saare uphaar arpit kiye.

Woh bole,

“Hey Prabhu, aapka mere ghar aana hi meri sabse badi kripa hai.”

Udhar Shrutadeva apne chhote se ghar mein itne khush hue ki woh naachne lage.

Unhone ghaas ki chatai bichhaayi aur prem se Krishna aur rishiyon ko baithaya.

Unhone saadhaaran phal, Tulsi aur sugandhit jal se Krishna ki pooja ki.

Shrutadeva bhaavuk hokar bole,

“Hey Prabhu, aaj mera jeevan safal ho gaya.”

Krishna muskuraakar bole,

“Hey Shrutadeva, yeh mahan rishi tum par kripa karne ke liye mere saath aaye hain.”

“Teerth aur murtiyaan dheere-dheere pavitra karti hain, lekin santon ka darshan turant mann ko pavitra kar deta hai.”

“Jo bhakti aur samman tum mujhe dete ho, wahi in mahan Brahmano ko bhi do. Mujhe wahi sabse adhik priya hai.”

Shrutadeva ne Krishna aur sab rishiyon ki poori shraddha se seva ki.

Rishi Shukadev bole, “Krishna ne Raja Bahulashva aur Shrutadeva dono ko samaan prem diya.”

“Dono ne sachchi bhakti ke bal par antim mein Bhagwan ka divya dham prapt kiya.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 87
    with st.expander("Chapter 87 - Śruti Gītā (Hyman of Praise by The Vedas)"):
        text1 = """ 
        Raja Parikshit ne poocha, “Hey Rishi, Ved jo prakriti aur gunon se jude hue hain, woh nirgun aur anant Parmatma ka varnan kaise kar sakte hain?”

Rishi Shukadev bole, “Hey Raja, yeh bahut gehra prashn hai. Ab main tumhe ek purani pavitra katha sunata hoon.”

“Ek samay Devarshi Narad Badarikashram gaye. Wahan Maharishi Narayan tapasya kar rahe the.”

Narad ji ne unse bhi yahi prashn poocha."""
        create_image_text_layout(
            "attached_assets/chapter10/10.87.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Tab Narayan Rishi bole,

“Bahut pehle Janalok mein Brahma ji ke manas putron — Sanak, Sanandan aur anya mahan rishiyon — ne Parmatma ke baare mein charcha ki thi.”

“Us sabha mein Sanandan ne Vedon ka gehra rahasya samjhaya tha.”

Sanandan bole,

“Pralay ke samay jab poora sansaar samaapt ho jaata hai, tab sirf Parmatma hi bache rehte hain.”

“Tab Ved swayam Bhagwan ki stuti karte hain, jaise raja ke gayak subah unhe jagate hain.”

Ved bole,

“Hey Prabhu, kripya sab jeevon ki agyaanata ko door kijiye. Aap hi sachche, anant aur sarvashaktimaan hain.”

“Aapki Maya ki wajah se jeev apne asli roop ko bhool jaate hain aur sansaar mein dukh paate hain.”

“Yeh poora jagat aapse hi bana hai aur antim mein aap mein hi sama jaata hai.”

“Jaise mitti se bartan bante hain aur tootkar fir mitti ban jaate hain, waise hi sab kuch aapse hi aata hai aur aap mein hi laut jaata hai.”

Vedon ne kaha,

“Buddhimaan log aapki kathaaon ko sunte aur sunaate hain. Aapki leelaayein mann ko pavitra kar deti hain.”

“Jo log aapki bhakti karte hain, wahi sach mein jeevit hain. Jo Bhagwan ko bhool jaate hain, unka jeevan bas saans lene jaisa hai.”

“Bhagwan har jeev ke hriday mein rehte hain, lekin jo log sirf sansaarik kaamon mein uljhe rehte hain, woh unhe pehchaan nahi paate.”

“Jo sant aur bhakt prem se Bhagwan ka naam lete hain, Bhagwan unke bahut paas hote hain.”

Vedon ne aur kaha,

“Hey Prabhu, jo vyakti aapke charanon mein sharan leta hai, woh janm-mrityu ke dukh se paar ho jaata hai.”

“Lekin jo log shareer aur dhan ko hi sab kuch samajhte hain, woh Maya mein bhatak jaate hain.”

“Yog aur tapasya bhi tab tak adhuri hai jab tak mann mein Bhagwan ke prati prem na ho.”

“Bhagwan ke bhakt sant is dharti ko pavitra karte hain.”

“Unke charanon ki dhool bhi teerth ke samaan pavitra hoti hai.”

Ved bole,

“Yeh sansaar ek sapne ki tarah hai. Sirf Bhagwan hi sachchi aur sada rehne wali sachchai hain.”

“Jo vyakti Bhagwan Hari ka dhyaan karta hai, woh Maya ke bandhan se mukt ho jaata hai.”

Rishi Narayan ne Narad ji se kaha,

“Yeh Vedon ka gehra rahasya hai. Isse mann ke sab vikar dheere-dheere jal jaate hain.”

Rishi Shukadev bole, “Narad ji ne is pavitra gyaan ko shraddha se suna aur fir Vyasa ji ko sunaaya.”

“Hey Raja Parikshit, isi tarah Ved nirgun Parmatma ka varnan seedhe shabdon se nahi, balki unki leela, mahima aur tattva ko samjhaakar karte hain.”

“Jo vyakti shraddha se Bhagwan Hari ka naam, gun aur kathaaon ka smaran karta hai, uska mann pavitra ho jaata hai aur dheere-dheere use param shanti milti hai.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 88
    with st.expander("Chapter 88 - God Rudra Saved"):
        text1 = """ 
        Raja Parikshit ne poocha, “Hey Rishi, ek ajeeb baat samajh nahi aati. Bhagwan Shiva toh vairaagi hain, fir bhi unke bhakt aksar dhan aur sukh pa lete hain. Lekin Bhagwan Vishnu, jo Lakshmi ji ke pati hain, unke bhakt kai baar gareebi aur kashton ka saamna karte hain. Aisa kyun?”

Rishi Shukadev bole, “Yeh prashn pehle Yudhishthira ne bhi Krishna se poocha tha.”

Tab Krishna ne kaha,

“Jis vyakti par main sachchi kripa karta hoon, uska dhan dheere-dheere chheen leta hoon.”

“Jab uska dhan chala jaata hai, tab rishtedaar aur dost bhi usse door ho jaate hain.”

“Fir woh dukhi hokar duniya ki asliyat samajhne lagta hai.”"""
        create_image_text_layout(
            "attached_assets/chapter10/10.88.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        “Uske baad woh mere bhakton ka sang karta hai aur dheere-dheere mera sachcha gyaan paata hai.”

Krishna bole,

“Meri sabse badi kripa dhan nahi, balki apna divya gyaan dena hai. Lekin yeh bahut gehra hota hai, isliye log jaldi samajh nahi paate.”

“Isi wajah se kai log doosre devtaon ki pooja karte hain, kyunki wahan unhe jaldi vardaan mil jaate hain.”

Rishi Shukadev bole, “Bhagwan Shiva aur Brahma ji bahut jaldi prasann ya krodhit ho jaate hain. Lekin Vishnu ji soch-samajhkar vardaan dete hain.”

“Ab main tumhe ek purani kahani sunata hoon.”

Ek raakshas tha jiska naam tha Vrikasura. Woh Shakuni ka beta tha.

Ek din usne Narad ji se poocha,

“Brahma, Vishnu aur Shiva mein kaun sabse jaldi vardaan deta hai?”

Narad ji bole,

“Shiva ji bahut jaldi prasann ho jaate hain. Tum unki tapasya karo.”

Yeh sunkar Vrikasura Himalaya ke Kedarnath kshetra gaya aur Shiva ji ko prasann karne ke liye kathin tapasya karne laga.

Woh apne sharir ka maans kaat-kaatkar agni mein chadhaane laga.

Saat din beet gaye, lekin Shiva ji prakat nahi hue.

Tab Vrikasura ne apna sir kaatne ka faisla kar liya.

Jaise hi woh yeh karne wala tha, Shiva ji turant agni se prakat ho gaye aur uska haath pakad liya.

Unhone pyar se kaha,

“Bas karo! Main tumse prasann hoon. Jo vardaan chaho maang lo.”

Vrikasura ne bahut bhayanak vardaan maanga.

Woh bola,

“Jiske sir par main haath rakh doon, woh turant mar jaaye.”

Shiva ji ek pal ke liye chintit hue, lekin fir bhi unhone “Tathastu” keh diya.

Vrikasura ne socha, “Chalo pehle Shiva par hi is vardaan ko aazmaata hoon!”

Woh Shiva ji ke sir par haath rakhne ke liye unke peeche dauda.

Yeh dekhkar Shiva ji ghabra gaye aur bhaagne lage.

Woh dharti, swarg aur kai lokon mein bhaagte rahe, lekin koi bhi unki madad nahi kar paaya.

Aakhir mein Shiva ji Vishnu Bhagwan ke paas pahunche.

Bhagwan Vishnu ne sab samajh liya.

Unhone ek sundar chhote Brahmachari ladke ka roop dharan kiya aur Vrikasura ke saamne aaye.

Woh bade vinamr swar mein bole,

“Hey raakshas raj, tum bahut thak gaye lagte ho. Thoda aaram karo.”

“Waise tum itni jaldi mein kahaan ja rahe ho?”

Vrikasura ne saari kahani bata di.

Tab Vishnu bole,

“Tum sach mein Shiva ji ki baat par vishwas karte ho? Daksha ke shraap ke baad woh Pret aur Pishaachon ke swami ban gaye hain.”

“Ho sakta hai unhone jhooth bola ho.”

“Tum chaho toh abhi apne sir par haath rakhkar vardaan ki sachchai jaan sakte ho.”

Vrikasura Vishnu ji ki meethi baaton mein aa gaya.

Usne bina soche apne hi sir par haath rakh diya.

Jaise hi usne aisa kiya, uska sir phat gaya aur woh turant mar gaya.

Aasmaan mein devta “Jai!” bolne lage aur phool barsane lage.

Shiva ji ki jaan bach gayi.

Tab Vishnu ji muskuraakar bole,

“Hey Mahadev, jo mahan logon ka apmaan karta hai, uska vinaash uske apne paapon se hi ho jaata hai.”

Rishi Shukadev bole, “Jo vyakti Vishnu ji dwara Shiva ji ki raksha ki yeh pavitra kahani shraddha se sunta hai, woh bhay aur paapon se mukt ho jaata hai.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 89
    with st.expander("Chapter 89 - Restoration to Life of Brāhmaṇa’s Sons"):
        text1 = """ 
        Raja Parikshit ne poocha, “Hey Rishi, Brahma, Vishnu aur Shiva mein sabse mahaan kaun hain?”

Rishi Shukadev bole, “Ek baar bahut saare rishi ek bade yagya mein yahi prashn charcha kar rahe the.”

“Sabne milkar Maharishi Bhrigu ko sach jaanne ke liye bheja.”

Sabse pehle Bhrigu ji Brahma ji ke paas gaye.

Unhone jaan-bujhkar Brahma ji ko pranam nahi kiya."""
        create_image_text_layout(
            "attached_assets/chapter10/10.89.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Yeh dekhkar Brahma ji ko gussa aa gaya, lekin woh samajh gaye ki Bhrigu unke putra hain. Isliye unhone apna krodh rok liya.

Phir Bhrigu ji Kailash par Shiva ji ke paas gaye.

Shiva ji bade prem se unhe gale lagane aaye.

Lekin Bhrigu ji peeche hat gaye aur kathor shabdon mein bole,

“Aap ajeeb reeti se rehte hain. Main aapko sparsh nahi karna chahta.”

Yeh sunkar Shiva ji ko bahut gussa aa gaya. Woh trishul lekar unki taraf badhe.

Tab Mata Parvati ne madhur shabdon se Shiva ji ko shaant kiya.

Uske baad Bhrigu ji Vaikunth gaye, jahan Bhagwan Vishnu Lakshmi ji ke saath virajmaan the.

Bhrigu ji ne wahan jaakar Vishnu ji ke seene par pair se laat maari.

Lekin Vishnu ji turant uth khade hue aur vinamrata se bole,

“Hey Brahman dev, humein maaf kijiye. Hum aapke aane ka pata nahi laga paaye.”

Phir Vishnu ji ne bade prem se Bhrigu ji ke pair dabaaye aur bole,

“Aapke komal pair ko mere kathor seene se chot toh nahi lagi?”

“Kripya apne charan jal se mujhe pavitra kijiye.”

Yeh dekhkar Bhrigu ji ka hriday bhakti se bhar gaya. Unki aankhon mein aansu aa gaye.

Woh wapas yagya mein gaye aur sab rishiyon ko poori kahani sunaayi.

Tab sabne samajh liya ki Vishnu ji sabse shaant, dayaalu aur sarvottam hain.

Rishi Shukadev bole, “Ab main tumhe Krishna aur Arjuna ki ek adbhut leela sunata hoon.”

Dwaraka mein ek Brahman ka har bachcha janm lete hi gayab ho jaata tha.

Dukhi Brahman har baar rajmahal ke paas jaakar rota aur kehta,

“Yeh sab bure rajaon ki wajah se ho raha hai!”

Ek din Arjuna ne uski baat suni aur garv se bola,

“Main tumhare agle bachche ki raksha karunga. Agar nahi kar paaya, toh agni mein pravesh kar lunga.”

Brahman bola,

“Jab Krishna, Balarama aur Pradyumna mere bachche nahi bacha paaye, toh tum kaise bachaoge?”

Arjuna ne kaha,

“Main Gandiva dhanush dhaaran karne wala Arjuna hoon. Main maut se bhi lad sakta hoon!”

Krishna muskuraaye, lekin Arjuna ko anumati de di.

Jab Brahman ki patni ko bachcha hone wala tha, tab Arjuna ne poore ghar ko divya baanon se gher diya.

Har taraf suraksha ka chakra bana diya gaya.

Thodi der baad bachcha paida hua aur zor-zor se rona laga.

Lekin agle hi pal woh achanak aasman mein gayab ho gaya.

Brahman gusse se chillane laga,

“Dekho! Arjuna bhi kuch nahi kar paaya!”

Arjuna bahut sharminda hue.

Woh Yamlok, Indralok aur kai lokon mein bachche ko dhoondhne gaye, lekin kahin nahi mila.

Apni pratigya yaad karke woh agni mein pravesh karne wale the.

Tab Krishna ne unhe rok liya.

Krishna bole,

“Chalo, main tumhe sach dikhaata hoon.”

Dono Krishna aur Arjuna ek divya rath par baithkar brahmand ke paar nikle.

Woh andhere aur samudron ko paar karte hue ek adbhut prakashmay lok mein pahunche.

Wahan unhone Anant Shesh ko dekha, jinke hazaar phan chamak rahe the.

Unke upar ek divya roop mein Maha Vishnu virajmaan the.

Unka sharir megh jaisa shyam tha aur woh peele vastra pehne hue the.

Krishna aur Arjuna ne haath jodkar pranam kiya.

Tab Maha Vishnu muskuraakar bole,

“Maine hi Brahman ke bachchon ko yahaan bulaya tha, kyunki main tum dono ka darshan karna chahta tha.”

“Tum dono Nara aur Narayana ke roop mein dharti par dharm ki raksha ke liye aaye ho.”

Uske baad Maha Vishnu ne sab bachchon ko Krishna aur Arjuna ko wapas de diya.

Dono un bachchon ko lekar Dwaraka laut aaye.

Brahman apne sab bachchon ko dekhkar khushi se ro pada.

Arjuna bhi yeh sab dekhkar samajh gaye ki unki saari shakti Krishna ki kripa se hi hai.

Rishi Shukadev bole, “Krishna ne dharti par rehkar anek adbhut leelaayein ki aur dharm ko fir se sthapit kiya.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 90
    with st.expander("Chapter 90 - The Song of Queens: Resume of Kṛṣṇa’s Sports"):
        text1 = """ 
        Rishi Shukadev bole, “Dwaraka nagari bahut sundar aur samriddh thi. Wahan har taraf khushi, utsav aur samriddhi dikhai deti thi.

Raaste haathiyon, ghodon, rathon aur veer Yadav yoddhaon se bhare rehte the.

Bagiche phoolon aur madhur awaaz waale pakshiyon se sajhe rehte the."""
        create_image_text_layout(
            "attached_assets/chapter10/10.90.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Krishna apni 16,000 raniyon ke saath alag-alag mahalon mein rehte the. Apni Yogmaya se woh ek saath sabhi ke paas upasthit ho jaate the.

Har mahal mein sundar talaab the, jinmein kamal khile rehte aur pakshi madhur sur mein gaate rehte the.

Krishna apni raniyon ke saath jal-kreeda karte, hans-te aur prem bhari baatein karte the.

Kabhi raniyan un par sugandhit paani chhidakti aur kabhi Krishna un par paani daalte. Sab jagah hansi aur khushi ka mahaul hota.

Sangeetkar dhol, veena aur mridang bajaakar Krishna ki mahima gaate rehte.

Krishna ki madhur baatein, pyari muskaan aur prem bhari nazar dekhkar sab raniyan unmein hi kho jaati thi.

Kabhi-kabhi Krishna door hote, toh raniyan virah mein prakriti se baatein karne lagti thi.

Ek rani ne samundar se kaha,

“Hey samundar, tum raat bhar kyun garajte rehte ho? Kya tum bhi Krishna ke virah mein udaas ho?”

Doosri rani ne chand se kaha,

“Hey chand, tum itne kamzor aur pheeke kyun lag rahe ho? Kya tum bhi Krishna ki yaad mein dukhi ho?”

Ek rani ne badal se kaha,

“Hey megh, tum Krishna jaise shyam ho. Kya tum bhi unki yaad mein aansu barsa rahe ho?”

Kisi ne koel se kaha,

“Tumhari madhur awaaz humein Krishna ki pyari baatein yaad dilati hai.”

Aur ek rani ne hans se kaha,

“Aao hans ji, baitho aur humein Krishna ki koi khabar sunaao.”

Raniyan Krishna ke prem mein itni doobi rehti thi ki kabhi hansne lagti, kabhi chup ho jaati aur kabhi virah mein bhaavuk ho jaati.

Rishi Shukadev bole, “Krishna ki raniyon ka prem bahut pavitra tha. Isi prem aur bhakti ke bal par unhone antim mein Bhagwan ka param dham prapt kiya.”

“Krishna ne grihastha jeevan jeete hue bhi dharm ka adarsh dikhaya.”

“Unke har mahal mein dharm, prem aur khushi ka vaas tha.”

Krishna ke bahut saare putra hue. Pradyumna unmein sabse bade aur Krishna ke samaan veer the.

Pradyumna ke putra Aniruddha hue aur Aniruddha ke putra Vajra hue, jo baad mein Yadu vansh ke bache hue vanshaj bane.

Rishi Shukadev bole, “Yadav log Krishna mein itne leen rehte the ki khaate, bolte, chalte ya sote waqt bhi unka mann Krishna mein hi laga rehta tha.”

“Krishna ne dharti ka bojh kam kiya, dusht rajaon ka vinaash kiya aur dharm ko fir se sthapit kiya.”

“Jo vyakti Krishna ki in pavitra leelaon ko shraddha se sunta ya sunaata hai, uske mann mein bhi dheere-dheere Bhagwan ke prati prem aur bhakti jagne lagti hai.”"""
        create_image_text_layout(text_content=text2, layout="full")
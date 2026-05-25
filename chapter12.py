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
    create_image_text_layout("attached_assets/chapter12/chapter12.jpg", layout="full")
    # Book 12 - Twelfth Skandha

    # Chapter 1
    with st.expander("Chapter 1 - Dynasties of the Kali Age"):
        text1 = """ 
        Kali Yug ke Raja aur Badalte Vansh

Raja Parikshit ne poocha,

“Jab Shri Krishna Vaikunth chale gaye, tab dharti par kaunse rajaon ne raj kiya?”

Shukdev ji bole,

“Hey Rajan, ab main tumhe Kali Yug ke rajaon aur vanshon ki kahani sunata hoon.”

Pradyot Vansh

Sabse pehle Brihadrath vansh ka antim raja Purunjaya hoga."""
        create_image_text_layout(
            "attached_assets/chapter12/12.1.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Lekin uska mantri Sunak use maar dega aur apne bete Pradyot ko raja bana dega.

Uske baad uske vansh ke raja kuch samay tak raj karenge.

Shishunag Vansh

Phir Shishunag naam ka raja aayega.

Uske vansh mein kai raja honge jo Magadh par raj karenge.

Yeh vansh kai saalon tak chalega.

Nand Vansh ka Uday

Uske baad Mahapadma Nand naam ka shaktishaali raja janm lega.

Woh bahut dhanwan hoga aur poori dharti par apna raj jama lega.

Shukdev ji bole,

“Woh dusre Parshuram ki tarah Kshatriyon ka vinaash karega.”

Mahapadma Nand ke baad uske aath putra raj karenge.

Maurya Vansh

Phir ek buddhimaan Brahman Nand vansh ko samaapt karega.

Wahi Chandragupt Maurya ko raja banaayega.

Uske vansh mein Ashokvardhan yani Samrat Ashok jaise mahaan raja paida honge.

Maurya vansh bahut samay tak dharti par raj karega.

Shung aur Kanva Vansh

Maurya vansh ke baad Shung vansh aur phir Kanva vansh ka raj aayega.

Yeh raja bhi dheere-dheere dharti par apna adhikaar jamaayenge.

Andhra aur Doosre Raja

Uske baad Andhra vansh ke kai raja raj karenge.

Phir Abhir, Shak, Yavan, Turushk aur Hoon jaise doosre vansh bhi dharti par raj karenge.

Bahut se raja lalchi aur adharmi honge.

Kali Yug ki Girti Hui Duniya

Shukdev ji ne dukhi hokar kaha,

“Kali Yug mein adharm dheere-dheere badhega.”

Raja jhooth bolenge, gussa karenge aur sirf paisa aur shakti ke peeche bhaagenge.

Woh nirdosh logon, mahilaon aur gaayon ko bhi dukh pahunchayenge.

Log bhi apne rajaon jaise banne lagenge.

Sachchai, daya aur dharm kam hote jaayenge.

Logon ki Soch Badal Jaayegi

Kali Yug mein log chhoti umr ke, kamzor aur hamesha pareshaan rehne lagenge.

Lalach aur jhagda badhta jaayega.

Bahut se log Vedo aur dharm ka samman karna chhod denge.

Shukdev ji bole,

“Jab raja adharmi hote hain, tab praja bhi dheere-dheere waise hi ban jaati hai.”

Antim Seekh

Is kahani ke through Shukdev ji ne samjhaya ki Kali Yug mein dharm dheere-dheere kam hoga.

Lekin jo vyakti Bhagwan ko yaad rakhega aur sachchai ke raaste par chalega, woh andhkaar mein bhi sahi raasta paa lega."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 2
    with st.expander("Chapter 2 - The Evils of the Kali Age"):
        text1 = """ 
        Chapter 2 – Kali Yug ki Buraiyaan

Shukdev ji ne Raja Parikshit se kaha,

“Kali Yug mein dheere-dheere dharm, sachchai, daya aur pavitrata kam hote jaayenge.”

Logon ki yaad-dasht, sharirik shakti aur jeevan ki umr bhi kam hone lagegi.

Paisa hi Sab Kuch Ban Jaayega

Shukdev ji bole,

“Kali Yug mein insaan ki izzat uske gunon se nahi, balki paison se hogi.”

Jiske paas dhan hoga, log usi ko bada aur samajhdaar maanenge.

Sach aur nyaay ki jagah taakat aur paisa zyada important ho jaayega."""
        create_image_text_layout(
            "attached_assets/chapter12/12.2.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Rishton mein Sachcha Prem Kam Hoga

Log shaadi aur rishton ko bhi sirf apni pasand aur sukh ke hisaab se dekhenge.

Vyapar mein dhokha aam baat ban jaayega.

Sirf baahari roop aur dikhawa hi mahatvapurn samjha jaayega.

Dharm Sirf Dikhawa Ban Jaayega

Shukdev ji ne kaha,

“Log dharm ka paalan sachche mann se nahi, sirf dikhawa karne ke liye karenge.”

Sirf janeu pehen lena hi Brahman hone ki nishani maana jaayega, chahe vyakti ke karm kaise bhi hon.

Log pavitrata se zyada baahari sajawat par dhyaan denge.

Raja Chor Jaise Ban Jaayenge

Kali Yug ke raja praja ki raksha karne ke bajaay unhe lootne lagenge.

Tax aur atyachaar badh jaayenge.

Dukhi log jungle aur pahaadon mein jaakar rehne lagenge aur phal, jad aur shahad khaakar jeevan bitaayenge.

Prakriti bhi Badal Jaayegi

Kabhi sukhha padega, kabhi tez baarish hogi.

Log bhookh, pyaas aur bimariyon se pareshaan rahenge.

Shukdev ji bole,

“Kali Yug mein insaan ki adhiktam umr sirf pachaas saal ke aas-paas reh jaayegi.”

Dharm aur Sanskaar Kam Ho Jaayenge

Log Vedo aur sanskaron ka paalan chhod denge.

Sabhi varnon aur ashramon ka farq dheere-dheere mitne lagega.

Log sirf apne pet aur swaarth ke liye jeene lagenge.

Ped-Paudhe aur Jeev bhi Kamzor Honge

Aushadhiyaan kam asar karengi.

Bade ped bhi chhote aur kamzor ho jaayenge.

Gaayein kam doodh dene lagenge.

Kalki Avatar ka Aagman

Lekin Shukdev ji ne ek umeed bhari baat bhi kahi.

Jab Kali Yug ka andhkaar bahut badh jaayega, tab Bhagwan Vishnu Kalki avatar lekar dharti par aayenge.

Woh Shambhal gaon mein Vishnuyash naam ke Brahman ke ghar janm lenge.

Kalki Bhagwan safed ghode Devadatta par savaar hokar adharmi aur dusht rajaon ka vinaash karenge.

Phir dheere-dheere dharm aur sachchai wapas aayegi.

Satya Yug ki Wapsi

Kalki avatar ke baad logon ke mann pavitra hone lagenge.

Sachchai, daya aur bhakti fir se badhegi.

Aur is tarah ek naye Satya Yug ki shuruaat hogi.

Samay Sabko Hara Deta Hai

Ant mein Shukdev ji ne ek gehri seekh di.

Woh bole,

“Bade-bade raja aur samraat bhi samay ke saamne tik nahi paate.”

Jo raja kabhi poori dharti ko apna samajhte the, aaj unka sirf naam aur kahaniyaan hi bachi hain.

Isliye insaan ko ahankaar nahi karna chahiye aur hamesha dharm aur Bhagwan ko yaad rakhna chahiye."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 3
    with st.expander("Chapter 3 - Dharma (Righteous Way of Life) in every Yuga: Efficacy of God’s Name"):
        text1 = """ 
        Chapter 3 – Har Yug ka Dharm aur Hari Naam ki Mahima

Shukdev ji ne kaha,

“Dharti rajaon ko dekhkar hansati hai.”

Woh kehti hai,

“Yeh raja khud maut ke haathon ka khilona hain, phir bhi mujhe jeetne ka sapna dekhte hain.”

Rajaon ka Ahankaar

Raja sochte hain,"""
        create_image_text_layout(
            "attached_assets/chapter12/12.3.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        “Pehle hum apne dushmanon ko haraayenge, phir poori dharti par raj karenge.”

Lekin woh yeh nahi samajhte ki maut hamesha unke paas khadi hai.

Bahut se mahaan raja — Bharat, Sagar, Raghu, Yayati, Ravan aur Hiranyakashyap jaise shaktishaali log bhi ek din sab kuch chhodkar chale gaye.

Aaj sirf unki kahaniyaan hi bachi hain.

Shukdev ji bole,

“Yeh sab kahaniyaan humein yeh samjhaane ke liye hain ki duniya ki cheezein hamesha rehne wali nahi hain.”

Bhagwan ki Bhakti Sabse Zaroori

Unhone kaha,

“Jo vyakti sachchi bhakti paana chahta hai, use hamesha Bhagwan Vishnu aur Krishna ki leelaon aur gunon ko sunna aur yaad karna chahiye.”

Har Yug ka Dharm

Raja Parikshit ne poocha,

“Har yug mein log kaise hote hain? Aur Kali Yug ke paap se bachne ka raasta kya hai?”

Tab Shukdev ji ne chaar yugon ka varnan kiya.

Satya Yug

Satya Yug mein dharm apne poore chaaron charanon par tika hota hai.

Sachchai, daya, tapasya aur sabki raksha karna logon ka swabhav hota hai.

Log shaant, dayaalu aur sabko samaan dekhne wale hote hain.

Unka mann dhyaan aur Bhagwan mein laga rehta hai.

Treta Yug

Treta Yug mein dharm thoda kam ho jaata hai.

Log yagya aur tapasya mein vishwas rakhte hain.

Dharm, dhan aur sukh — in teenon par log dhyaan dete hain.

Dwapar Yug

Dwapar Yug mein dharm aadha reh jaata hai.

Log shaurya, yash aur bade yagyaon ko mahatva dete hain.

Lekin greed aur ahankaar bhi badhne lagta hai.

Kali Yug

Kali Yug mein dharm ka sirf ek hissa reh jaata hai, aur woh bhi dheere-dheere kam hota jaata hai.

Log lalchi, jhoothe aur swarthi ho jaate hain.

Bina wajah jhagda aur dushmani badhne lagti hai.

Kali Yug ke Log

Shukdev ji bole,

“Kali Yug mein log paisa aur vasna ke peeche bhaagenge.”

Dharm aur sachchai kam ho jaayegi.

Raja praja ko lootenge.

Vyapari dhokha denge.

Guru aur sadhu ka roop lekar bhi log sirf paisa kamaane lagenge.

Log apne maa-baap aur rishtedaron ka dhyaan tak nahi rakhenge.

Dukh aur Dar

Kali Yug mein log hamesha tension aur darr mein jeeyenge.

Kabhi akaal padega, kabhi bhaari tax lagega.

Log bhojan, kapde aur sukh ki kami se pareshaan rahenge.

Chhoti si baat par dost aur rishtedaar bhi ek doosre se ladne lagenge.

Sabse Badi Umeed

Lekin Shukdev ji ne ek bahut sundar baat kahi.

Woh bole,

“Kali Yug buraiyon se bhara hai, lekin ismein ek mahaan gun bhi hai.”

“Sirf Bhagwan Krishna ka naam lene se bhi insaan paapon aur bandhanon se mukta ho sakta hai.”

Hari Naam ki Mahima

Satya Yug mein log dhyaan se Bhagwan ko paate the.

Treta Yug mein yagya se.

Dwapar Yug mein pooja aur seva se.

Lekin Kali Yug mein sirf Hari Naam ka kirtan hi moksha dene ke liye kaafi hai.

Shukdev ji bole,

“Jo vyakti Krishna ka naam shraddha se leta hai, uska mann pavitra ho jaata hai.”

Bhagwan ka naam hazaaron janmon ke paap tak mita sakta hai.

Antim Seekh

Ant mein Shukdev ji ne Raja Parikshit se kaha,

“Hey Rajan, apne mann mein Bhagwan Keshav ko basa lo.”

“Jeevan ke antim samay mein bhi agar mann Bhagwan mein laga ho, toh insaan moksha paa leta hai.”

Aur isi wajah se Kali Yug mein bhi bhakti aur Hari Naam sabse bada sahara maana gaya hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4
    with st.expander("Chapter 4 - The Four-Fold Pralaya"):
        text1 = """ 
        Chapter 4 – Chaar Prakar ke Pralaya

Shukdev ji ne Raja Parikshit se kaha,

“Ab main tumhe srishti ke vinaash yani Pralaya ke baare mein bataata hoon.”

Unhone samjhaya ki Pralaya chaar prakar ka hota hai.

Brahma ka Din aur Raat

Shukdev ji bole,

“Hazaar Chaturyug milkar Brahma ji ka ek din banta hai.”

Aur utni hi lambi unki ek raat hoti hai.

Jab Brahma ji ka din samaapt hota hai, tab srishti ka ek bada vinaash hota hai.

Isse Naimittik Pralaya kaha jaata hai."""
        create_image_text_layout(
            "attached_assets/chapter12/12.4.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Us samay Bhagwan Narayan sab kuch apne andar samaakar Sheshnaag par yog nidra mein chale jaate hain.

Prakritik Pralaya

Jab Brahma ji ki poori aayu samaapt ho jaati hai, tab aur bhi bada vinaash hota hai.

Isse Prakritik Pralaya kehte hain.

Tab poori srishti dheere-dheere apne mool roop Prakriti mein sama jaati hai.

Bhayankar Sukha aur Aag

Sabse pehle sau saal tak baarish nahi hoti.

Dharti sukhi aur bina ann ke ho jaati hai.

Log bhookh se pareshaan hokar ek doosre ko hi khaane lagte hain.

Phir Surya apni bhayankar garmi se samundar, nadiyaan aur dharti ka saara paani sukha deta hai.

Uske baad Sheshnaag ke mukh se nikli vinaashkari aag poori srishti ko jalane lagti hai.

Dharti har taraf se jalne lagti hai.

Tez Hawa aur Mahabaarish

Phir sau saal tak bahut tez aandhiyaan chalti hain.

Aasmaan dhool aur dhuein se bhar jaata hai.

Uske baad bade-bade kaale baadal garajne lagte hain aur sau saal tak lagataar bhayankar baarish hoti hai.

Dheere-dheere poori srishti paani mein doob jaati hai.

Panch Tatvon ka Vilay

Shukdev ji ne samjhaya,

“Dharti ka gandh paani mein sama jaata hai.”

Phir paani ka ras agni mein sama jaata hai.

Agni ka roop hawa mein, hawa ka sparsh aakash mein aur aakash ki dhvani ahankaar mein sama jaati hai.

Aakhir mein sab kuch Prakriti mein vilin ho jaata hai.

Sab Kuch Shaant Ho Jaata Hai

Us avastha mein na din hota hai, na raat.

Na dharti hoti hai, na Surya, na hawa aur na hi koi jeev.

Har taraf gehri shaanti hoti hai.

Sirf avyakta Prakriti aur Parmatma ka astitva rehta hai.

Maya aur Sansar

Shukdev ji bole,

“Yeh sansar ek sapne ki tarah aata aur chala jaata hai.”

Jaise badal aasman mein dikhte hain aur phir gayab ho jaate hain, waise hi duniya bhi Parmatma mein utpann hoti hai aur phir unmein sama jaati hai.

Ahankaar hi Bandhan Hai

Unhone ek sundar example diya.

“Jaise Surya se bane badal hi Surya ko chhupa dete hain, waise hi ahankaar insaan ko Bhagwan se door kar deta hai.”

Jab gyaan ki talwar se ahankaar ka naash hota hai, tab Atma ko apna asli roop samajh aata hai.

Isi ko Atyantik Pralaya ya moksha kaha gaya hai.

Nitya Pralaya

Shukdev ji ne bataya ki ek Pralaya har pal hota rehta hai.

Sharir har pal badalta rehta hai — bachpan se jawaani aur budhape tak.

Lekin insaan ko yeh badlaav turant mehsoos nahi hota.

Isi ko Nitya Pralaya kehte hain.

Sabse Bada Sahara

Ant mein Shukdev ji bole,

“Jo vyakti sansar ke dukh aur janam-maran ke samundar ko paar karna chahta hai, uske liye Bhagwan ki leelaon aur naam ka shravan sabse bada sahara hai.”

Bhagwan ki kathayein hi jeevan ki sachchi naav hain, jo insaan ko sansar ke dukh se paar laga deti hain."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 5
    with st.expander("Chapter 5 - Śuka’s Concluding Precept Concerning Brahman"):
        text1 = """ 
        Chapter 5 – Shukdev ji ki Antim Brahm Gyaan ki Seekh

Shukdev ji ne Raja Parikshit se kaha,

“Yeh Bhagavat Mahapuran Bhagwan Hari ki mahima se bhara hua hai.”

Unhone samjhaya ki Brahma ji aur Shiv ji bhi Bhagwan Hari ki shakti se hi apna kaam karte hain.

Sharir aur Atma Alag Hain

Shukdev ji bole,

“Hey Rajan, yeh mat socho ki tum marne wale ho.”"""
        create_image_text_layout(
            "attached_assets/chapter12/12.5.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        “Sharir ek din janm leta hai aur ek din khatam ho jaata hai. Lekin Atma kabhi nahi marti.”

Unhone samjhaya ki Atma sharir se bilkul alag hai, jaise lakdi se alag agni hoti hai.

Sapne ka Example

Shukdev ji ne ek simple example diya.

“Jaise sapne mein insaan apne aap ko dukhi ya marta hua dekhta hai, lekin asli mein woh surakshit hota hai, waise hi Atma sharir ki mrityu se prabhavit nahi hoti.”

Atma na janm leti hai aur na kabhi marti hai.

Ghade aur Aakash ki Seekh

Unhone kaha,

“Jab mitti ka ghada toot jaata hai, tab uske andar ka aakash bahar ke aakash mein mil jaata hai.”

Waise hi jab sharir khatam hota hai, tab gyani vyakti ki Atma Brahman mein ek ho jaati hai.

Maya ka Bandhan

Shukdev ji bole,

“Maya mann ko banaati hai, aur mann hi insaan ko sansar ke bandhan mein baandhta hai.”

Mann hi ichchha, karm aur janam-maran ka kaaran banta hai.

Deepak ka Example

Unhone ek aur sundar example diya.

“Jaise tel, baati aur aag milkar deepak jalate hain, waise hi karm, mann aur sharir milkar jeevan chalate hain.”

Jab yeh sambandh toot jaata hai, tab sharir samaapt ho jaata hai.

Lekin Atma hamesha bani rehti hai.

Atma ka Sachcha Roop

Shukdev ji ne kaha,

“Atma aakash ki tarah sab jagah vyapt hai.”

Woh naash hone wali cheez nahi hai.

Na uska koi aarambh hai aur na ant.

Krishna ka Dhyaan

Shukdev ji ne Raja Parikshit ko samjhaya,

“Apna mann poori tarah Bhagwan Vasudev mein laga do.”

“Dhyaan aur gyaan ke saath apne asli roop ko samajhne ki koshish karo.”

Takshak se Darne ki Zaroorat Nahi

Shukdev ji bole,

“Takshak saamp tumhare sharir ko kaat sakta hai, lekin tumhari Atma ko chhoo bhi nahi sakta.”

“Koi bhi mrityu Atma ka kuch nahi bigaad sakti.”

Main hi Brahman Hoon

Phir unhone ek bahut gehri seekh di.

“Jab insaan sach mein samajh leta hai — ‘Main hi Brahman hoon’ — tab uska darr khatam ho jaata hai.”

Us samay use na sharir alag lagta hai, na sansar aur na hi maut.

Har jagah use sirf Parmatma ka hi roop dikhai deta hai.

Antim Prashn

Shukdev ji ne pyaar se poocha,

“Hey Parikshit, maine tumhe Bhagwan Hari ki leelaon aur Brahm gyaan ka saar bata diya.”

“Ab batao, tum aur kya sunna chahte ho?”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6(a)
    with st.expander("Chapter 6(a) - Takṣaka Bites Parīkṣit—Janmejaya’s Serpent Sacrifice"):
        text1 = """ 
        Chapter 6 – Parikshit ki Mrityu aur Sarp Yagya

Suta ji ne kaha, “Shukdev ji se Bhagavat ka gyaan sunne ke baad Raja Parikshit ka mann poori tarah shaant ho gaya.”

Raja ne haath jodkar Shukdev ji ko pranam kiya aur kaha,

“Ab mera jeevan safal ho gaya hai.”

“Ab mujhe Takshak ya maut se koi darr nahi hai.”

Parikshit ka Nidar Mann

Parikshit bole,

“Aapne mujhe Bhagwan Hari ka gyaan diya. Ab mera mann Brahman mein sthir ho gaya hai.”"""
        create_image_text_layout(
            "attached_assets/chapter12/12.6a.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        “Main ab shaanti se apna sharir chhodne ke liye taiyaar hoon.”

Shukdev ji yeh sunkar prasann hue aur doosre rishiyon ke saath wahan se chale gaye.

Ganga Kinare Dhyaan

Raja Parikshit Ganga ji ke kinaare kush ke aasan par baith gaye.

Unhone apne mann aur indriyon ko control kiya aur poori tarah Bhagwan mein dhyaan laga diya.

Ab unka mann sansar se bilkul alag ho chuka tha.

Woh ek vriksh ki tarah shaant aur sthir baithe rahe.

Takshak ka Aana

Isi beech Takshak naag Raja Parikshit ko dasne ke liye aa raha tha.

Raaste mein uski mulaqat Kashyap Rishi se hui, jo zehar ka ilaaj jaante the.

Takshak ne unhe dhan dekar wapas bhej diya.

Phir Takshak ne Brahman ka roop dharan kiya aur Raja Parikshit ke paas pahunch gaya.

Usne Raja ko das liya.

Sharir ka Ant, Atma ka Nahi

Takshak ke zehar se Raja Parikshit ka sharir turant jal kar bhasm ho gaya.

Lekin us samay Parikshit ka mann poori tarah Brahman mein sama chuka tha.

Isliye unhe koi darr ya dukh mehsoos nahi hua.

Aasmaan mein dundubhi bajne lagi.

Devtaon ne phool barsaaye aur Gandharv gaane lage.

Sab jaante the ki Raja Parikshit ne moksha paa liya hai.

Janmejaya ka Gussa

Jab Parikshit ke putra Janmejaya ko pata chala ki Takshak ne unke pita ko maara hai, toh woh bahut gusse mein aa gaye.

Unhone ek bhayankar Sarp Yagya shuru kar diya.

Us yagya ki agni mein saare saamp kheenchkar girne lage aur jalne lage.

Bade-bade naag bhi bach nahi pa rahe the.

Takshak ne Maangi Madad

Darr kar Takshak Devraj Indra ke paas chala gaya aur unki sharan le li.

Lekin yagya ki shakti itni zyada thi ki Brahmano ne mantra bolkar Takshak ko Indra ke saath hi yagya ki agni mein kheenchna shuru kar diya.

Indra ka vimaan bhi hilne laga.

Brihaspati ki Seekh

Tab Devguru Brihaspati wahan aaye aur Janmejaya ko samjhaya.

Woh bole,

“Hey Rajan, kisi ki mrityu ka asli kaaran uska apna karm hota hai.”

“Saamp, agni, rog ya koi aur cheez sirf ek zariya hote hain.”

Unhone kaha,

“Nirdosh saampo ko maarna theek nahi hai. Kripya yeh yagya rok dijiye.”

Janmejaya ne unki baat maan li aur Sarp Yagya rok diya.

Maya aur Gussa

Suta ji ne samjhaya,

“Bhagwan ki Maya bahut shaktishaali hai.”

Isi Maya ke kaaran log gussa, badla aur ahankaar mein galat kaam kar baithte hain.

Asli Gyani Kaun Hai?

Jo vyakti “main” aur “mera” ka ahankaar chhod deta hai, wahi sachcha gyani hota hai.

Aise log sabke saath shaanti aur daya se rehte hain.

Antim Seekh

Suta ji bole,

“Insaan ko bure shabdon aur dukh ko shaanti se sehna chahiye.”

“Kisi se dushmani nahi rakhni chahiye, kyunki yeh sharir ek din chhodkar jaana hi hai.”

Aur jo vyakti Bhagwan Vishnu ka dhyaan karta hai, woh dheere-dheere Maya aur sansar ke bandhan se azaad ho jaata hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6(b)
    with st.expander("Chapter 6(b) - Classification of Vedas in Different Branches"):
        text1 = """ 
        Chapter 6(b) – Vedo ka Vibhajan aur Om ka Rahasya

Shaunak Rishi ne Suta ji se poocha,

“Vyasa ji ke shishyon ne Vedo ko kitni shaakhaon mein baanta tha? Kripya humein yeh kahani bataaiye.”

Om ka Janm

Suta ji bole,

“Shuruaat mein Brahma ji gehre dhyaan mein baithe the.”

Tab unke hriday se ek divya dhvani nikli.

Yahi pavitra dhvani baad mein “Om” bani.

Yogiyon ne isi Om ka dhyaan karke apne mann ko shuddh kiya aur moksha paaya."""
        create_image_text_layout(
            "attached_assets/chapter12/12.6b.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Om ka Arth

Suta ji ne samjhaya ki Om teen aksharon se milkar bana hai — A, U aur M.

Yeh teenon milkar bahut si cheezon ka pratik hain.

Jaise:

Teen gun — Sattva, Rajas aur Tamas
Teen lok — Prithvi, Aakash aur Swarg
Teen avastha — Jaagrit, Swapna aur Sushupti

Om hi sabhi mantraon aur Vedo ka beej maana gaya hai.

Brahma ji ne Vedo ko Prakat Kiya

Brahma ji ne Om aur aksharon ki madad se chaar Vedo ko prakat kiya.

Phir unhone unhe apne putron aur rishiyon ko sikhaya.

Yeh gyaan guru se shishya tak chalta raha.

Vyasa ji ka Vedo ko Baantna

Samay ke saath logon ki yaad-dasht aur samajh kam hone lagi.

Tab Bhagwan Vishnu ki ichchha se Ved Vyas ji ne Vedo ko alag-alag bhaagon mein baant diya, taaki log unhe aasani se seekh sakein.

Unhone chaar Ved alag kiye:

Rigveda
Yajurveda
Samaveda
Atharvaveda
Chaar Shishya

Vyasa ji ne har Ved ek alag shishya ko diya.

Rigveda → Paila
Yajurveda → Vaishampayan
Samaveda → Jaimini
Atharvaveda → Sumantu

Phir in shishyon ne bhi apne shishyon ko Ved sikhaye aur kai shaakhaayein bani.

Yajnavalkya aur Yajurveda

Ek baar Vaishampayan apne shishyon se naraaz ho gaye.

Unke shishya Yajnavalkya ne garv se kaha,

“Main akela hi kathin tapasya kar sakta hoon.”

Yeh sunkar guru ko gussa aa gaya.

Unhone kaha,

“Jo kuch maine tumhe sikhaya hai, use wapas karo.”

Tab Yajnavalkya ne seekha hua Yajurveda bahar nikaal diya.

Doosre rishiyon ne tittiri pakshi ka roop lekar us gyaan ko grahan kiya.

Isi wajah se us shaakha ka naam Taittiriya pada.

Surya Dev se Naya Gyaan

Uske baad Yajnavalkya ne Surya Dev ki tapasya ki.

Unhone Surya Dev ki bahut sundar stuti ki aur naye Yajurveda gyaan ki prarthana ki.

Surya Dev prasann hue aur ghode ke roop mein unke saamne aaye.

Unhone Yajnavalkya ko naye Yajurveda mantra diye.

Yeh shaakhaayein Vajasaneyi naam se prasiddh hui.

Samaveda ki Shaakhaayein

Jaimini aur unke shishyon ne Samaveda ko bahut si shaakhaon mein baant diya.

Kai rishiyon ne alag-alag jagahon par Vedon ka prachaar kiya.

Is tarah Ved gyaan poori duniya mein phailta gaya.

Antim Seekh

Suta ji ne samjhaya,

“Ved sirf pustakein nahi hain. Yeh Bhagwan se nikla hua pavitra gyaan hai.”

Aur Om us gyaan ka sabse pavitra roop maana gaya hai.

Jo vyakti shraddha aur dhyaan se Om aur Vedon ka smaran karta hai, uska mann dheere-dheere shuddh aur shaant ho jaata hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7
    with st.expander("Chapter 7 - The Branches of the Atharva Veda: Characteristics of the Purāṇas"):
        text1 = """ 
        Chapter 7 – Atharvaveda ki Shaakhaayein aur Puranon ki Visheshata

Suta ji ne kaha,

“Sumantu Rishi Atharvaveda ke bade gyani the.”

Unhone Atharvaveda apne shishya Kabandh ko sikhaya.

Kabandh ne ise do bhaagon mein baantkar Pathya aur Vedadarsh ko diya.

Phir unke shishyon ne bhi ise alag-alag shaakhaon mein baant diya.

Is tarah Atharvaveda ka gyaan guru se shishya tak failta gaya."""
        create_image_text_layout(
            "attached_assets/chapter12/12.7.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Puranon ke Guru

Suta ji ne bataya ki Purano ka gyaan bhi guru parampara se chala.

Kai mahaan rishiyon ne Purano ko seekha aur duniya mein phailaya.

Suta ji bole,

“Maine bhi apne guruon se sabhi Purano ka gyaan praapt kiya.”

Purano ki 10 Vishesh Baatein

Rishiyon ne bataya ki ek Mahapuran mein 10 mukhya vishay hote hain.

Yeh hain:

Srishti ka nirmaan
Jeevon ki rachna
Jeevan chalane ka niyam
Bhagwan ki raksha aur avataar
Karmon ka kaaran
Manu ke yug
Rajaon ke vansh
Unke itihaas aur kahaniyaan
Pralaya yani vinaash
Sabka antim aadhaar — Brahman
Srishti ka Rahasya

Suta ji ne samjhaya,

“Sabse pehle Prakriti aur teen gun — Sattva, Rajas aur Tamas se srishti ki shuruaat hoti hai.”

Phir dheere-dheere indriyaan, tattva aur jeev utpann hote hain.

Bhagwan ka Rakshan

Bhagwan Vishnu baar-baar avataar lekar duniya ki raksha karte hain.

Kabhi Varah roop mein, kabhi Ram aur Krishna ke roop mein.

Woh dushton ka vinaash aur dharm ki raksha karte hain.

Manvantar aur Rajaon ke Vansh

Har Manu ka ek alag yug hota hai.

Us yug mein alag devta, rishi aur raja hote hain.

Purano mein un sab vanshon aur rajaon ki kahaniyaan bataayi gayi hain.

Chaar Prakar ka Pralaya

Rishiyon ne kaha ki sansar ka vinaash bhi kai prakar ka hota hai.

Kabhi samay aane par, kabhi Prakriti ke roop mein, aur kabhi gyaan se ahankaar khatam hone par.

Brahman hi Sabka Aadhaar

Suta ji bole,

“Jaise mitti se bane bartan alag dikhte hain, lekin sabka aadhaar mitti hi hoti hai, waise hi poori srishti ka asli aadhaar Brahman hai.”

Wahi har jagah maujood hai.

Gyaan se Mukti

Jab insaan samajh leta hai ki duniya ek Maya hai aur Brahman hi sach hai, tab uska mann sansar se alag ho jaata hai.

Woh dheere-dheere moksha ki taraf badhne lagta hai.

18 Mahapuran

Suta ji ne 18 Mahapuranon ke naam bhi bataaye.

Unmein Vishnu Puran, Shiv Puran, Bhagavat Puran, Garud Puran, Skand Puran aur Matsya Puran jaise prasiddh Puran shamil hain.

Antim Seekh

Suta ji ne kaha,

“Ved aur Puran Bhagwan ka diya hua pavitra gyaan hain.”

Jo vyakti shraddha aur dhyaan se inhe sunta ya samajhta hai, uska mann pavitra hota hai aur uska jeevan sahi raaste par chalne lagta hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 8
    with st.expander("Chapter 8 - Mārkaṇḍeya’s Penance and Praise of Lord Nārāyaṇa"):
        text1 = """ 
        Chapter 8 – Markandeya Rishi ki Tapasya aur Bhagwan Narayan ki Kripa

Shaunak Rishi ne Suta ji se poocha,

“Humne suna hai ki Markandeya Rishi bahut lambi aayu wale the.”

“Yeh bhi kaha jaata hai ki jab poori duniya pralaya ke paani mein doob gayi thi, tab bhi woh jeevit the.”

“Unhone ek divya baalak ko bargad ke patte par lete hue bhi dekha tha. Kripya iska rahasya bataaiye.”

Markandeya ki Kathor Tapasya"""
        create_image_text_layout(
            "attached_assets/chapter12/12.8.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Suta ji bole,

“Markandeya Rishi bachpan se hi bahut pavitra aur anushasit the.”

Unhone Vedon ka adhyan kiya aur jeevan bhar brahmacharya ka vrat rakha.

Woh jata, vriksh ki chaal ke vastra aur rudraksh dharan karte the.

Subah-shaam Bhagwan Hari ka dhyaan aur pooja karte the.

Sanyam Bhara Jeevan

Markandeya bahut simple jeevan jeete the.

Jo bhiksha milti, pehle guru ko arpan karte.

Guru ki anumati milne par hi bhojan karte, warna vrat rakhte.

Is tarah tapasya, gyaan aur bhakti mein lage rehkar unhone mrityu tak ko jeet liya.

Devta bhi Hairaan Ho Gaye

Unki tapasya dekhkar Brahma ji, Shiv ji aur doosre devta bhi hairaan ho gaye.

Markandeya ka mann poori tarah shaant ho chuka tha.

Woh hamesha Bhagwan Hari ka dhyaan karte rehte the.

Indra ko Hui Chinta

Bahut samay beet gaya.

Tab Devraj Indra ko darr hua ki kahin Markandeya apni tapasya se swarg ka adhikaar na paa lein.

Isliye Indra ne unki tapasya todne ka socha.

Kaamdev ka Aana

Indra ne apsaraayein, Gandharv, Kaamdev, Basant ritu aur sugandhit hawa ko Markandeya ke ashram bheja.

Ashram Himalaya ke sundar sthaan par tha.

Wahan phool, ped, pakshi aur jharne bahut sundar lag rahe the.

Apsaraayein nritya aur sangeet karne lagi.

Kaamdev ne apne prem baan chalaaye.

Ek apsara khelte hue Markandeya ke saamne aayi aur hawa se uske vastra hilne lage.

Sabko laga ki ab Rishi ka dhyaan toot jaayega.

Tapasya ki Shakti

Lekin Markandeya Rishi bilkul shaant baithe rahe.

Unka mann zara bhi nahi hila.

Kaamdev aur sab devta unki tapasya ke tej se darr gaye.

Woh sab waapas laut gaye.

Suta ji bole,

“Mahaan sant gussa, moh aur vasna se pare hote hain.”

Bhagwan Nara-Narayan ka Darshan

Markandeya ki bhakti se prasann hokar Bhagwan Vishnu Nara aur Narayan Rishi ke roop mein prakat hue.

Ek ka rang gora tha aur doosre ka neela.

Dono tapasvi vastra pehne hue bahut divya lag rahe the.

Unke chehre kamal ki tarah sundar chamak rahe the.

Markandeya ka Anand

Bhagwan ko dekhkar Markandeya ka hriday khushi se bhar gaya.

Unki aankhon mein aansu aa gaye aur sharir romanchit ho gaya.

Woh turant uthkar dandvat pranam karne lage.

Phir unhone Bhagwan ki pooja ki aur vinamrata se stuti karne lage.

Bhagwan ki Mahima

Markandeya bole,

“Hey Prabhu, aap hi sabke jeevan ka aadhaar hain.”

“Brahma, Shiv aur sab jeev aapki shakti se hi kaam karte hain.”

“Aap hi sansar ki raksha ke liye alag-alag avataar lete hain.”

Bhagwan ke Charanon ka Sahara

Rishi bole,

“Jo vyakti aapke charanon ki sharan le leta hai, uska darr aur dukh door ho jaata hai.”

“Aapke charan hi sansar ke dukh se bachne ka sabse bada sahara hain.”

Maya ka Asar

Markandeya ne kaha,

“Bhagwan sabke andar hote hue bhi Maya ke kaaran log unhe pehchaan nahi paate.”

Lekin jo bhakti aur gyaan ka raasta pakadta hai, woh dheere-dheere Bhagwan ko samajhne lagta hai.

Antim Seekh

Is kahani se yeh seekh milti hai ki sachchi tapasya aur bhakti se insaan moh, darr aur vasna par vijay paa sakta hai.

Aur jo vyakti poori shraddha se Bhagwan ki sharan leta hai, uspar Bhagwan khud kripa karte hain."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 9
    with st.expander("Chapter 9 - The Lord Exhibits His Māyā"):
        text1 = """ 
        Chapter 9 – Bhagwan ne Dikhayi Apni Maya

Suta ji ne kaha,

“Jab Markandeya Rishi ne Bhagwan Narayan ki itni sundar stuti ki, tab Bhagwan bahut prasann hue.”

Bhagwan bole,

“Hey Mahaan Rishi, tumne tapasya, Ved adhyan aur bhakti se siddhi praapt kar li hai.”"""
        create_image_text_layout(
            "attached_assets/chapter12/12.9.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        “Maango, tum jo bhi vardaan chaho.”

Markandeya ki Ichchha

Markandeya vinamrata se bole,

“Prabhu, aapka darshan hi mere liye sabse bada vardaan hai.”

Lekin phir unhone ek anokhi baat kahi.

“Main aapki Maya dekhna chahta hoon — wahi Maya jiske kaaran log ek hi Parmatma mein alag-alag roop dekhte hain.”

Bhagwan muskuraaye aur bole,

“Tum meri Maya zaroor dekhoge.”

Phir Bhagwan apne Badarikashram chale gaye.

Bhakti mein Doobe Rishi

Uske baad Markandeya apne ashram mein rehkar har jagah Bhagwan ko dekhne lage.

Kabhi agni mein, kabhi Surya mein, kabhi paani aur hawa mein.

Kabhi-kabhi bhakti mein itna doob jaate ki pooja karna bhi bhool jaate.

Pralaya ki Shuruaat

Ek shaam Markandeya Pushpabhadra nadi ke kinaare dhyaan kar rahe the.

Achanak bahut tez aandhi chalne lagi.

Kaale baadal aasman mein chha gaye.

Bijli chamakne lagi aur zor-zor se garajne lagi.

Phir itni tez baarish hui ki poori dharti paani mein doobne lagi.

Poora Sansar Doob Gaya

Samundar chaaron taraf fail gaya.

Badi-badi lehron aur bhayankar magarmachhon se paani daraawna lag raha tha.

Dharti, pahaad, nagar aur saare jeev paani mein doob gaye.

Sirf Markandeya Rishi hi bach paaye.

Woh andhere aur tufaan ke beech akela tairte rahe.

Maya ka Darr

Kabhi woh lehron mein ghoom jaate, kabhi jal jeev unhe kaatne lagte.

Kabhi dukh mehsoos hota, kabhi darr, kabhi thodi si khushi.

Aisa lag raha tha jaise anant saal beet gaye hon.

Bhagwan ki Maya ne unhe poori tarah hairaan kar diya tha.

Bargad ke Patte par Divya Baalak

Tabhi unhone door ek chhota sa bargad ka ped dekha.

Uski ek shaakh par ek sundar baalak patte par leta hua tha.

Uska rang neele panna jaisa chamak raha tha.

Uski aankhen kamal ki tarah sundar thi aur woh apne pair ka angutha muh mein lekar muskurate hue choos raha tha.

Uska divya tej andhere ko mita raha tha.

Rishi ka Anand

Us baalak ko dekhte hi Markandeya ki thakaan aur darr sab khatam ho gaya.

Unka hriday khushi se bhar gaya.

Woh us adbhut baalak ke paas jaane lage.

Vishnu ke Sharir mein Puri Srishti

Jaise hi baalak ne saans andar li, Markandeya uski saans ke saath uske sharir ke andar chale gaye.

Andar jaakar woh hairaan reh gaye.

Unhone poori srishti dekhi — aasman, dharti, Surya, Chandrama, pahaad, samundar, nagar, log, devta aur apna khud ka ashram tak.

Sab kuch waise hi tha jaise pralaya se pehle tha.

Wapas Bahar Aana

Phir baalak ne saans bahar chhodi aur Markandeya fir se samundar mein aa gaye.

Unhone fir bargad ka ped aur woh divya baalak dekha.

Baalak muskuraakar unki taraf dekh raha tha.

Markandeya samajh gaye ki yeh koi aam baalak nahi, swayam Bhagwan Vishnu hain.

Woh unhe gale lagane ke liye aage badhe.

Lekin turant hi baalak, bargad ka ped aur pralaya ka paani sab gayab ho gaya.

Maya ka Rahasya

Achanak Markandeya ne khud ko apne purane ashram mein shaant baitha hua paaya.

Tab unhe samajh aaya ki yeh sab Bhagwan Vishnu ki divya Maya thi.

Antim Seekh

Is kahani se yeh seekh milti hai ki poora sansar Bhagwan ki Maya se chal raha hai.

Sirf Bhagwan hi sachche aur sada rehne wale hain.

Jo vyakti unki sharan leta hai, woh darr aur bhram se paar ho jaata hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 10
    with st.expander("Chapter 10 - God Śiva’s Boon to Mārkaṇḍeya"):
        text1 = """ 
        Chapter 10 – Bhagwan Shiv ka Markandeya ko Vardaan

Suta ji ne kaha,

“Bhagwan Vishnu ki adbhut Maya dekhne ke baad Markandeya Rishi aur bhi zyada Bhagwan ki sharan mein chale gaye.”

Rishi ne prarthana ki,

“Hey Prabhu, aapke charan hi sansar ke darr se bachane wale hain.”

“Bade-bade gyani log bhi aapki Maya mein phans jaate hain aur ahankaar karne lagte hain.”"""
        create_image_text_layout(
            "attached_assets/chapter12/12.10.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Shiv ji ka Aana

Ek din Bhagwan Shiv apni patni Parvati aur apne gano ke saath aakash mein bhraman kar rahe the.

Tab unhone Markandeya Rishi ko gehre dhyaan mein baithe dekha.

Parvati ji boli,

“Prabhu, dekhiye yeh Rishi kitne shaant aur sanyami hain.”

“Inka mann samundar ki tarah sthir hai.”

“Kripya inse prasann hokar inhe vardaan dijiye.”

Shiv ji ki Prashansa

Bhagwan Shiv muskuraaye aur bole,

“Yeh Rishi kisi vardaan, siddhi ya moksha tak ki ichchha nahi rakhte.”

“Inhone Bhagwan Vishnu mein sachchi bhakti pa li hai.”

Phir Shiv ji bole,

“Lekin santon ka sang sabse bada laabh hota hai. Isliye chalo inse milte hain.”

Gehri Samadhi

Jab Shiv ji Markandeya ke paas aaye, tab Rishi itni gehri samadhi mein the ki unhe kuch bhi mehsoos nahi hua.

Unhe na apna sharir yaad tha aur na hi aas-paas ki duniya.

Shiv ji Hriday mein Prakat Hue

Tab Shiv ji yog shakti se Markandeya ke hriday mein pravesh kar gaye.

Achanak Rishi ne apne andar ek tejomay roop dekha.

Unhone Shiv ji ko dekha — teen netron wale, jata dhari, haath mein trishul aur damru liye hue.

Unka tej ugte Surya ki tarah chamak raha tha.

Markandeya yeh adbhut darshan dekhkar hairaan reh gaye.

Rishi ne Kiya Swagat

Samadhi tootne ke baad Markandeya ne aankhen kholi aur Shiv ji ko Parvati ji ke saath saamne khada dekha.

Woh turant uthkar pranam karne lage.

Unhone Shiv ji ka poore samman ke saath swagat kiya.

Pushp, chandan, dhoop aur deep se unki pooja ki.

Markandeya ki Stuti

Rishi bole,

“Hey Mahadev, aapke kaaran hi duniya mein sukh aur shanti hai.”

“Aap hi Brahma, Vishnu aur Rudra roop mein sansar ko chalate hain.”

“Main aapko pranam karta hoon.”

Shiv ji ki Seekh

Bhagwan Shiv bahut prasann hue.

Woh bole,

“Brahman aur sachche sant bahut pavitra hote hain.”

“Hum — Brahma, Vishnu aur main bhi unka samman karte hain.”

Shiv ji ne kaha,

“Teerth aur murtiyaan dheere-dheere pavitra karti hain, lekin santon ka darshan turant mann ko pavitra kar deta hai.”

Markandeya ki Vinamrata

Markandeya bole,

“Prabhu, aapka darshan hi mere liye sabse bada vardaan hai.”

“Phir bhi agar aap kuch dena chahte hain, toh mujhe Bhagwan Vishnu aur unke bhakton mein sada bhakti dijiye.”

“Aur meri aapke prati bhi kabhi na tootne wali shraddha bani rahe.”

Shiv ji ka Vardaan

Shiv ji bahut khush hue.

Unhone kaha,

“Tumhari Vishnu bhakti hamesha bani rahegi.”

“Tumhe amar kirti, gyaan aur vairagya praapt hoga.”

“Tum budhape aur mrityu se bhi surakshit rahoge bahut lambe samay tak.”

Shiv ji ne unhe ek aur vardaan diya.

“Tum ek mahaan Purana ke rachayita banoge.”

Yahi Purana baad mein Markandeya Purana ke naam se prasiddh hua.

Antim Seekh

Suta ji ne kaha,

“Markandeya Rishi aaj bhi apni bhakti aur yog shakti ke liye prasiddh hain.”

Is kahani se yeh seekh milti hai ki sachchi bhakti mein ahankaar nahi hota.

Jo vyakti Bhagwan aur santon se prem karta hai, uska mann dheere-dheere Maya aur sansar ke bandhan se azaad ho jaata hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 11
    with st.expander("Chapter 11 - Significance of the Various parts of the Lord’s Image"):
        text1 = """ 
        Chapter 11 – Bhagwan Vishnu ke Divya Roop ka Rahasya

Shaunak Rishi ne Suta ji se poocha,

“Bhagwan Vishnu asal mein shuddh chetna hain. Phir Tantra aur dhyaan mein unhe haath, pair, shankh, chakra aur abhushan ke saath kyun dikhaya jaata hai?”

“Kripya humein iska rahasya bataaiye.”

Srishti hi Bhagwan ka Virat Roop Hai

Suta ji bole,"""
        create_image_text_layout(
            "attached_assets/chapter12/12.11.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        “Poora brahmand Bhagwan ka hi Virat roop hai.”

Dharti unke charan maani jaati hai.

Aasmaan unka sir hai.

Surya unki aankhen hain.

Hawa unki saans hai.

Dishaayein unke kaan hain.

Chaand unka mann maana gaya hai.

Ped-paudhe unke sharir ke rom hain aur baadal unke baal.

Is tarah poori srishti Bhagwan ke sharir ka roop maani gayi hai.

Bhagwan ke Abhushanon ka Arth

Suta ji ne samjhaya,

“Bhagwan ka har abhushan aur hathiyaar ek gehra arth rakhta hai.”

Kaustubh mani → Jeev ki shuddh chetna
Vanmala → Maya aur teen gun
Peela vastra → Ved
Janeu → Pavitra Omkar
Shankh → Jal tattva
Sudarshan chakra → Agni aur shakti
Gada → Pran shakti aur bal
Dhanush → Samay
Baan → Indriyaan
Garud aur Lakshmi ka Rahasya

Garud Bhagwan ke vahaan hain aur Vedon ka pratik maane jaate hain.

Mata Lakshmi Bhagwan ki divya shakti aur tej ka roop hain.

Bhagwan ke Chaar Roop

Suta ji bole,

“Bhagwan Vishnu chaar roop mein bhi dhyaan kiye jaate hain.”

Vasudev
Sankarshan
Pradyumna
Aniruddh

Yeh roop mann, buddhi aur jeevan ke alag-alag pehlu ko sambhalte hain.

Ek hi Bhagwan, Kai Roop

Suta ji ne samjhaya,

“Bhagwan ek hi hain, lekin Maya ke kaaran woh alag-alag roop mein dikhai dete hain.”

Wahi srishti banaate, sambhalte aur samaapt karte hain.

Lekin unka asli roop hamesha ek aur pavitra rehta hai.

Bhagwan Krishna ki Prarthana

Suta ji ne prem se prarthana ki,

“Hey Krishna, hey Govind, aap hamesha apne bhakton ki raksha kariye.”

“Aapki leela aur naam sunna hi jeevan ko pavitra bana deta hai.”

Subah ka Smaran

Suta ji bole,

“Jo vyakti subah snaan karke Bhagwan ke is Virat roop ka dhyaan karta hai, uska mann dheere-dheere pavitra ho jaata hai.”

Surya Dev ka Rahasya

Phir Shaunak Rishi ne Surya Dev ke baare mein poocha.

Suta ji ne bataya,

“Surya Dev bhi Bhagwan Vishnu ka hi ek roop hain.”

Woh har mahine alag-alag devtaon, rishiyon, Gandharvon, Naagon aur Yakshon ke saath milkar sansar ka paalan karte hain.

Har Mahine Alag Saathi

Har mahine Surya Dev ke saath naye saathi hote hain.

Jaise:

Chaitra mein Dhata aur Tumburu
Vaishakh mein Aryama aur Narad
Jyeshtha mein Mitra aur Menaka
Shravan mein Indra aur Vishvavasu

Aur isi tarah saal bhar alag-alag dev shaktiyaan Surya Dev ke saath kaam karti hain.

Surya Rath ka Rahasya

Rishi Surya Dev ki stuti karte hain.

Gandharv unke liye geet gaate hain.

Apsaraayein nritya karti hain.

Naag unke rath ko baandhte hain aur Yaksh usse taiyaar karte hain.

Hazaaron Valakhilya Rishi unke aage chal kar Bhagwan Hari ki stuti karte hain.

Antim Seekh

Suta ji ne kaha,

“Bhagwan Hari hi Surya roop mein poori duniya ko jeevan dete hain.”

Jo vyakti shraddha se Bhagwan ke Virat roop aur Surya Dev ki mahima ka smaran karta hai, uska mann shuddh hota hai aur paap dheere-dheere door ho jaate hain।"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 12
    with st.expander("Chapter 12 - A Synoptic Review of the twelve Skandhas of Śrīmad Bhāgavata"):
        text1 = """ 
        Chapter 12 – Shrimad Bhagavat ka Saar

Suta ji ne kaha,

“Main Bhagwan Hari ko pranam karta hoon, jo poori srishti ke rachayita hain.”

“Ab main tumhe Shrimad Bhagavat ka saar bataata hoon.”

Bhagavat ka Mahatva

Suta ji bole,

“Yeh Bhagavat Purana insaan ke jeevan ke liye bahut mangalkari hai.”

Ismein Bhagwan Vishnu aur Krishna ki divya leelaon ka varnan hai.

Jo ise shraddha se sunta hai, uske paap dheere-dheere mitne lagte hain."""
        create_image_text_layout(
            "attached_assets/chapter12/12.12.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Pehle Skandh ki Kahani

Ismein Raja Parikshit ki kahani bataayi gayi.

Kaise unhe shraap mila aur kaise unhone mrityu se pehle Bhagwan ka gyaan sunne ka sankalp liya.

Narad ji ke purv janm aur bhakti ka bhi varnan hai.

Dusre aur Teesre Skandh

Suta ji bole,

“Inmein srishti ki rachna aur Bhagwan ke avataaron ka varnan hai.”

Vidur aur Maitreya ki baatcheet bhi bataayi gayi hai.

Kapil Bhagwan ne Devahuti ko Atma aur bhakti ka gyaan diya.

Dhruv aur Prahlad

Bhagavat mein Dhruv ki kathor tapasya aur Prahlad ki Vishnu bhakti ka bhi sundar varnan hai.

Prahlad ne mushkilon mein bhi Bhagwan ka naam nahi chhoda.

Samudra Manthan aur Avataar

Bhagwan ke Matsya, Kurma, Narasimha aur doosre avataaron ki kahaniyaan bhi bataayi gayi hain.

Samudra manthan aur amrit praapti ka varnan bhi hai.

Rajaon aur Vanshon ki Kahani

Surya vansh aur Chandra vansh ke mahaan rajaon ki kahaniyaan bataayi gayi hain.

Ram ji, Sagar, Yayati aur doosre mahaan rajaon ka bhi varnan hai.

Krishna Leela

Suta ji bole,

“Bhagavat ka sabse madhur bhaag Krishna ki leelaayein hain.”

Putana vadh, Govardhan uthana, Kaliya naag ko shaant karna aur Raas Leela sabka sundar varnan hai.

Krishna ne Kans, Shishupal aur bahut se dushton ka vinaash kiya.

Pandav aur Yadav Vansh

Bhagwan Krishna ne Pandavo ki raksha ki aur dharti ka bhaar kam kiya.

Baad mein Yadav vansh ka ant aur Krishna ka Vaikunth prasthan bhi bataaya gaya.

Kali Yug ka Varnan

Barahve Skandh mein Kali Yug ki buraiyon ka varnan hai.

Log dheere-dheere sachchai aur dharm se door hote jaayenge.

Lekin Hari Naam hi sabse bada sahara bataya gaya hai.

Hari Naam ki Mahima

Suta ji bole,

“Agar koi insaan girte waqt ya dukh mein bhi ‘Hari’ naam le le, toh uske paap kam hone lagte hain.”

Bhagwan ka naam Surya ki tarah andhkaar mita deta hai.

Bhagwan ki Katha Sabse Pavitra

Suta ji ne kaha,

“Wahi baatein sach mein sundar aur pavitra hain jisme Bhagwan Hari ki mahima ho.”

Baaki bina Bhagwan ki yaad ke baatein mann ko sachchi shanti nahi deti.

Gyaan aur Bhakti

Sirf gyaan ya karm kaafi nahi hai.

Agar unmein Bhagwan ki bhakti nahi ho, toh woh adhure hain.

Bhakti se hi mann pavitra aur shaant hota hai.

Bhagavat Sunne ka Phal

Jo vyakti shraddha aur dhyaan se Bhagavat ko padhta ya sunta hai, uska mann pavitra hota hai.

Uske andar Bhagwan ki yaad mazboot hone lagti hai.

Aur dheere-dheere woh sansar ke dukh aur darr se azaad ho jaata hai.

Shukdev ji ko Pranam

Ant mein Suta ji ne Shukdev ji ko pranam kiya.

Woh bole,

“Shukdev ji ka mann hamesha Brahman mein sthir tha.”

Lekin Krishna ki madhur leelaon ne unka hriday bhi prem se bhar diya.

Isliye unhone daya se yeh Bhagavat Purana duniya ko sunaya.

Antim Seekh

Bhagavat ka saar yahi hai —

Bhagwan ka naam, unki leela aur bhakti hi jeevan ka sabse bada sahara hai.

Jo vyakti prem aur shraddha se Bhagwan ko yaad karta hai, uska jeevan safal ho jaata hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 13
    with st.expander("Chapter 13 - The extent of Each of the Eighteen Purāṇas"):
        text1 = """ 
        Chapter 13 – 18 Puranon ka Mahatva aur Bhagavat ki Mahima

Suta ji ne kaha,

“Main us Bhagwan ko pranam karta hoon jinki mahima Brahma, Indra aur devta bhi gaate hain.”

“Yogi log gehre dhyaan mein unka darshan karte hain, lekin unki poori mahima ko samajhna bahut kathin hai.”

Kurma Avatar ki Mahima

Suta ji ne Bhagwan ke Kurma Avatar ko yaad kiya.

Jab Samudra Manthan ho raha tha, tab Bhagwan ne vishal kachhue ka roop liya.

Mandarachal parvat unki peeth par rakha gaya."""
        create_image_text_layout(
            "attached_assets/chapter12/12.13.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Unki saanson ki shakti se samundar mein lehron ka uthna-baithna chalta raha.

18 Mahapuran

Suta ji bole,

“Ab main tumhe 18 Mahapuranon ke baare mein bataata hoon.”

Har Purana mein alag-alag kahaniyaan aur gyaan diya gaya hai.

Kuch Pramukh Puran
Brahma Purana → 10,000 shlok
Padma Purana → 55,000 shlok
Vishnu Purana → 23,000 shlok
Shiv Purana → 24,000 shlok
Bhagavat Purana → 18,000 shlok
Narad Purana → 25,000 shlok
Markandeya Purana → 9,000 shlok
Agni Purana → 15,400 shlok
Skanda Purana → 81,100 shlok

Is tarah sabhi Puranon ko milaakar lagbhag 4 lakh shlok hote hain.

Bhagavat ka Vishesh Sthaan

Suta ji bole,

“Sabhi Puranon mein Shrimad Bhagavat sabse pavitra maana gaya hai.”

Bhagwan Vishnu ne sabse pehle yeh gyaan Brahma ji ko diya tha.

Phir yeh gyaan guru parampara se Narad, Vyas, Shukdev aur Raja Parikshit tak pahucha.

Bhagavat ka Saar

Bhagavat ke shuruaat, beech aur ant — har jagah bhakti aur vairagya ka updesh diya gaya hai.

Ismein Bhagwan Hari ki madhur leelaon ka amrit bhara hua hai.

Upanishadon ka Saar

Suta ji ne kaha,

“Bhagavat sabhi Upanishadon ka saar hai.”

Yeh sikhata hai ki Atma aur Parmatma alag nahi hain.

Asli lakshya moksha aur Bhagwan ki bhakti paana hai.

Bhagavat Daan ka Mahatva

Jo vyakti Bhadrapad Purnima ke din shraddha se Bhagavat ka daan karta hai, use bahut bada punya milta hai.

Aisa vyakti Bhagwan ke param dham ko praapt karta hai.

Bhagavat Sabse Madhur Hai

Suta ji bole,

“Jo vyakti Bhagavat ka amrit pee leta hai, uska mann doosri cheezon mein zyada nahi lagta.”

Jaise Ganga sabhi nadiyon mein sabse pavitra hai, waise hi Bhagavat sabhi Puranon mein sabse mahaan maana gaya hai.

Bhagwan ki Mahima

Bhagavat mein Bhagwan ke sachche roop ka varnan hai —

Sachchidanand roop, jo Maya aur dukh se pare hain.

Yeh gyaan sirf pavitra aur bhakti wale hriday mein samajh aata hai.

Bhagavat Sunne ka Phal

Jo vyakti prem aur shraddha se Bhagavat ko sunta, padhta aur uspar dhyaan karta hai, uska mann dheere-dheere pavitra ho jaata hai.

Uske paap mitne lagte hain aur woh sansar ke bandhan se azaad hone lagta hai.

Shukdev ji ko Pranam

Suta ji ne Shukdev ji ko pranam kiya.

Woh bole,

“Shukdev ji ne daya karke Raja Parikshit ko yeh Bhagavat sunaya tha, taaki unhe moksha mil sake.”

Antim Prarthana

Ant mein Suta ji ne Bhagwan se prarthana ki,

“Hey Vasudev, har janm mein hamare mann mein aapke charanon ki bhakti bani rahe.”

Antim Seekh

Bhagwan ka naam lena, unki leela sunna aur bhakti mein jeevan bitana hi jeevan ka sabse bada dhan hai.

Jo vyakti sachche mann se Hari ka smaran karta hai, uske dukh aur paap dheere-dheere door ho jaate hain."""
        create_image_text_layout(text_content=text2, layout="full")
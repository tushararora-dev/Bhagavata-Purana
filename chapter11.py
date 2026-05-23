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
    create_image_text_layout("attached_assets/chapter11/chapter11.jpg", layout="full")
    # Book 11 - Eleventh Skandha
    text0 = """
    <h2>Book 11 - Eleventh Skandha</h2>
    """
    # Book 11 - Eleventh Skandha

    # Chapter 1
    with st.expander("Chapter 1 - Sage’s Curse: Imprecating the Annihilation of Yadu’s Race"):
        text1 = """ 
        Raja Parikshit ne poocha, “Hey Rishi, Yadavo jaise mahaan aur Brahmano ka samman karne waale logon ko shraap kaise lag gaya?”

“Unke beech jhagda kaise hua? Kripya sab vistaar se bataaiye.”

Rishi Shukadev bole, “Bhagwan Krishna ne dharti ka bojh kam kar diya tha.”

“Bahut saare dusht raja aur asur Kurukshetra yudh mein mare ja chuke the.”"""
        create_image_text_layout(
            "attached_assets/chapter11/11.1.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        “Lekin Krishna ne socha ki Yadav vansh bhi bahut balwaan aur ajey ho gaya hai.”

“Koi bhi unhe hara nahi sakta tha, kyunki Krishna swayam unki raksha kar rahe the.”

Tab Krishna ne mann mein vichaar kiya,

“Ab samay aa gaya hai ki Yadav vansh bhi iss dharti se vida ho.”

“Lekin main apne hi vansh ko seedhe khud nahi maarunga.”

“Unka vinaash unke apne andar ke jhagdon se hoga, jaise baans ka jungle apni hi ghisav se jal uthta hai.”

Rishi Shukadev bole, “Ek din Vishwamitra, Durvasa, Narad, Vashishtha aur kai mahan rishi Dwaraka se teerth yatra ke liye nikle.”

Tab kuch shararti Yadav yuvaon ne mazaak karne ki sochi.

Unhone Samba ko, jo Jambavati ka putra tha, stree ke kapde pehna diye.

Uske pet par kapda baandhkar use garbhvati stree jaisa bana diya.

Phir woh sab rishiyon ke paas gaye aur jhoothi vinamrata se bole,

“Hey mahan rishiyon, yeh sundari bahut sharmati hai.”

“Iska bachcha hone wala hai. Kripya bataaiye, iske garbh se ladka paida hoga ya ladki?”

Rishi turant samajh gaye ki unka mazaak udaaya ja raha hai.

Woh krodhit ho gaye aur bole,

“Hey moorkho! Iske garbh se ek lohe ka musal paida hoga jo tumhare poore vansh ka vinaash karega!”

Yeh sunkar sab Yadav yuva bahut darr gaye.

Jab unhone Samba ke kapde hataaye, toh sach mein uske andar ek lohe ka bada musal nikla.

Sab log ghabra gaye aur use lekar Raja Ugrasena ke paas pahunche.

Dwaraka ke sab log yeh dekhkar dar gaye, kyunki Brahmano ka shraap kabhi jhootha nahi hota tha.

Raja Ugrasena ne turant aadesh diya ki us lohe ke musal ko peeskar chooran bana diya jaaye.

Us chooran ko samundar mein phenk diya gaya.

Lekin musal ka ek chhota tukda poori tarah nahi peesa ja saka.

Use bhi samundar mein phenk diya gaya.

Samundar ki lehron se woh chooran kinaare par aa gaya aur wahan Eraka naam ki ghaas ugne lagi.

Aur jo chhota lohe ka tukda tha, use ek machhli ne nigal liya.

Baad mein woh machhli machhuaare ke jaal mein pakdi gayi.

Machhuaare ne machhli ke andar se woh lohe ka tukda nikala aur use apne teer ki nok bana liya.

Rishi Shukadev bole, “Bhagwan Krishna yeh sab jaante the.”

“Woh chaahte toh Brahmano ke shraap ko rok sakte the.”

“Lekin Krishna ne use nahi roka, kyunki Yadav vansh ka ant ab nishchit ho chuka tha.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 2
    with st.expander("Chapter 2 - Bhāgavata Dharma: Nārada’s Narration of King Nimi’s Dialogue"):
        text1 = """ 
        Raja Parikshit ne poocha, “Hey Rishi, insaan ko Bhagwan ki sachchi bhakti kaise milti hai? Aur ek mahaan bhakt ki pehchaan kya hoti hai?”

Rishi Shukadev bole, “Ek baar Devarshi Narad Dwaraka aaye.”

Vasudev ji ne unka bada adar kiya aur vinamrata se bole,

“Hey Maharishi, sant log hamesha sabka bhala karte hain.”"""
        create_image_text_layout(
            "attached_assets/chapter11/11.2.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        “Kripya humein woh dharm bataaiye jisse Bhagwan prasann hote hain aur jeev sansaar ke dukh se mukt ho jaata hai.”

Narad ji khush hokar bole,

“Hey Vasudev, tumne bahut uttam prashn poocha hai.”

“Bhagavat dharm ko sunna, samajhna aur apnaana mann ko pavitra kar deta hai.”

Phir Narad ji ne ek purani katha sunaayi.

Woh bole,

“Pehle Videha desh ke Raja Nimi ne mahan rishiyon se yahi prashn poocha tha.”

“Yeh rishi Rishabhdev ke putra the aur bade gyani aur vairaagi the.”

Unke naam the — Kavi, Hari, Antariksha, Prabuddha, Pippalayana aur anya mahaan yogi.

Jab woh Raja Nimi ke yagya mein aaye, tab Raja ne unka bada samman kiya aur vinamrata se poocha,

“Hey mahan rishiyon, kripya humein woh maarg bataaiye jisse Bhagwan prasann hote hain aur jeev ko moksha milta hai.”

Sabse pehle Rishi Kavi bole,

“Bhagwan Vishnu ke charanon ki bhakti hi sabse surakshit aur uttam maarg hai.”

“Sansaar mein jeev sharir ko hi apna sachcha roop samajhkar darr aur dukh paata hai.”

“Lekin Bhagwan ki bhakti se yeh darr door ho jaata hai.”

Rishi Kavi ne kaha,

“Jo bhi kaam insaan kare — sharir, mann, buddhi ya vaani se — use Bhagwan Narayan ko samarpit kar dena chahiye.”

“Bhagwan ki kathaa sunni chahiye, unka naam gaana chahiye aur bina sharm ke unki bhakti karni chahiye.”

“Jo bhakt prem se Bhagwan ka naam leta hai, kabhi hansta hai, kabhi rota hai aur kabhi naachne lagta hai.”

“Uska hriday Bhagwan ke prem se pighal jaata hai.”

Rishi ne ek sundar baat kahi,

“Jaise bhojan karne se ek saath pet bharta hai, shakti milti hai aur bhookh door hoti hai, waise hi Bhagwan ki bhakti se ek saath prem, gyaan aur vairagya milte hain.”

Tab Raja Nimi ne poocha,

“Hey Rishi, ek mahaan bhakt ki pehchaan kya hoti hai?”

Rishi Hari bole,

“Sabse uttam bhakt wahi hai jo har jeev mein Bhagwan ko dekhta hai aur sabko samaan samajhta hai.”

“Jo Bhagwan se prem karta hai, bhakton se mitrata rakhta hai, nirbal logon par daya karta hai aur dushton se door rehta hai, woh madhyam bhakt hai.”

“Jo sirf murti ki pooja karta hai lekin Bhagwan ke bhakton aur doosre jeevon ka samman nahi karta, woh abhi shuruaati bhakt hai.”

Rishi Hari ne aur kaha,

“Jo sukh-dukh, bhookh-pyaas aur darr se zyada prabhavit nahi hota aur hamesha Bhagwan ko yaad karta hai, wahi sachcha bhakt hai.”

“Jiske mann mein ‘mera’ aur ‘tera’ ka bhed nahi rehta, woh Bhagwan ko bahut priya hota hai.”

“Jo ek pal ke liye bhi Bhagwan ko bhoolna nahi chahta, wahi sabse mahaan bhakt hai.”

Rishi Shukadev bole, “Is tarah mahan rishiyon ne Raja Nimi ko Bhagavat dharm ka gehra gyaan diya.”

“Jo vyakti shraddha se Bhagwan ki bhakti karta hai aur unka naam leta hai, uska mann dheere-dheere shaant aur pavitra ho jaata hai.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 3
    with st.expander("Chapter 3 - Discourses on the Māyā and the means to Transcend it"):
        text1 = """ 
        Raja Nimi ne poocha, “Hey mahan rishiyon, Bhagwan ki Maya kya hai? Yeh jeev ko kaise bandh leti hai? Aur insaan is Maya se kaise paar ho sakta hai?”

Rishi Antariksha bole,

“Bhagwan ne apni Maya se iss sansaar ki rachna ki.”

“Jeev asal mein shuddh aur pavitra aatma hai, lekin Maya use sharir se jod deti hai.”"""
        create_image_text_layout(
            "attached_assets/chapter11/11.3.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        “Tab jeev sochne lagta hai — ‘Yeh sharir hi main hoon.’ Isi bhram ko Maya kehte hain.”

“Jeev kabhi jagta hai, kabhi sapna dekhta hai aur kabhi gehri neend mein chala jaata hai.”

“Lekin in sab avasthaon se alag uski asli aatma sada shaant aur amar rehti hai.”

Rishi ne samjhaaya,

“Jeev apne purane karmo ke kaaran baar-baar janm leta hai aur sukh-dukh bhogta rehta hai.”

“Isi tarah woh sansaar ke chakra mein ghoomta rehta hai.”

Phir Rishi Antariksha ne pralaya ka varnan kiya.

Woh bole,

“Ek samay aisa bhi aata hai jab poora sansaar samaapt ho jaata hai.”

“Bahut saalon tak baarish nahi hoti. Suraj ki garmi sab kuch jala deti hai.”

“Fir bhayanak aag aur pralay ke baadal poore brahmand ko dhak lete hain.”

“Dheere-dheere dharti, jal, agni, vaayu aur aakash sab apne mool roop mein sama jaate hain.”

“Ant mein sab kuch Bhagwan ki Maya mein vilin ho jaata hai.”

Raja Nimi ne fir poocha,

“Hey Rishi, iss kathin Maya se jeev kaise bach sakta hai?”

Tab Rishi Prabuddha bole,

“Jo log sirf dhan, ghar aur sukh ke peeche bhaagte hain, unhe antim mein dukh hi milta hai.”

“Isliye buddhimaan vyakti ko ek sache guru ki sharan leni chahiye.”

“Guru se bhakti aur satya ka gyaan seekhna chahiye.”

Rishi ne kaha,

“Bhagwan ke bhakton ka sang karo.”

“Sab par daya rakho, vinamr bano aur mann ko shaant rakho.”

“Jhooth, hinsa aur ghamand se door raho.”

“Bhagwan Hari ki kathaa suno, unka naam gaao aur har kaam unhe samarpit karo.”

“Apna dhan, ghar, parivaar aur jeevan bhi Bhagwan ki seva samajhkar jeeyo.”

“Bhakton ke saath milkar Bhagwan ki mahima gaane se mann pavitra ho jaata hai.”

“Fir bhakt kabhi rota hai, kabhi hansta hai aur kabhi prem mein naachne lagta hai.”

“Is tarah dheere-dheere woh Maya se paar ho jaata hai.”

Uske baad Raja Nimi ne poocha,

“Hey Rishi, Brahman ya Paramatma ka asli roop kya hai?”

Tab Rishi Pippalayana bole,

“Bhagwan hi is sansaar ki rachna, paalan aur vinaash ka kaaran hain.”

“Wahi Brahman, Paramatma aur Narayan hain.”

“Unhe mann, buddhi ya shabdon se poori tarah samajhna mushkil hai.”

“Woh janm aur mrityu se pare hain.”

“Sharir badalta hai, lekin aatma sada ek samaan rehti hai.”

“Jab mann shuddh ho jaata hai aur bhakti badh jaati hai, tab Bhagwan swayam hriday mein prakat ho jaate hain.”

Phir Raja Nimi ne poocha,

“Hey Rishi, karm karte hue bhi insaan moksha kaise paa sakta hai?”

Tab Rishi Avirhotra bole,

“Vedo mein bataye gaye karm dharm ke liye hote hain.”

“Lekin karm ka asli uddeshya mann ko pavitra banana hai.”

“Jo vyakti bina phal ki ichchha ke karm karta hai aur sab Bhagwan ko samarpit kar deta hai, woh karm ke bandhan se mukt ho jaata hai.”

Rishi ne aage kaha,

“Bhagwan ki pooja shraddha aur pavitrata se karni chahiye.”

“Unka dhyaan hriday mein bhi karna chahiye.”

“Jo vyakti har jeev aur har vastu mein Bhagwan ko dekhta hai, woh jaldi hi sansaar ke bandhan se mukt ho jaata hai.”

Rishi Shukadev bole, “Is tarah mahan rishiyon ne Raja Nimi ko Maya, bhakti, Brahman aur karm ka gehra gyaan diya.”

“Jo vyakti shraddha se Bhagwan Hari ka naam leta hai aur unki bhakti karta hai, woh dheere-dheere Maya ke andhkaar se bahar aa jaata hai aur param shanti paata hai.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4
    with st.expander("Chapter 4 - Description of the Lord’s Incarnations by Drumila"):
        text1 = """ 
        Raja Nimi ne poocha, “Hey Maharishi, Bhagwan Hari ke alag-alag avataaron aur unki divya leelaon ke baare mein humein bataaiye.”

Tab Rishi Drumila bole,

“Bhagwan ki mahima anant hai. Koi bhi unke sab gun aur avataaron ko poori tarah gin nahi sakta.”

“Dharti ki dhool ke kan shayad gin liye jaayein, lekin Bhagwan ki mahima nahi.”

Rishi ne samjhaaya,"""
        create_image_text_layout(
            "attached_assets/chapter11/11.4.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        “Bhagwan Narayan ne hi iss brahmand ki rachna ki aur fir swayam usmein pravesh karke sab jeevon ke andar virajmaan ho gaye.”

“Brahma, Vishnu aur Shiva bhi unki hi shakti ke roop hain.”

“Brahma rachna karte hain, Vishnu paalan karte hain aur Rudra vinaash karte hain.”

“Lekin in sabke peeche ek hi Parmatma ki shakti kaam karti hai.”

Fir Rishi Drumila ne Bhagwan ke avataaron ka varnan kiya.

Woh bole,

“Bhagwan Nara aur Narayan Rishi ke roop mein Dharma aur Murti ke ghar janme.”

“Woh Badarikashram mein kathin tapasya karte the.”

“Indra ko darr hua ki kahin woh uska swarg na le lein.”

Isliye Indra ne Kamdev aur apsaraon ko unki tapasya todne bheja.

Apsaraayein sundar nritya aur madhur bhaav se unhe mohit karne lagi.

Lekin Narayan Rishi bilkul shaant rahe.

Woh muskuraakar bole,

“Darro mat. Tum sab hamare mehmaan ho.”

Phir Bhagwan ne apni yog shakti se apsaraon se bhi adhik sundar streeon ko prakat kar diya.

Yeh dekhkar sab devta aur apsaraayein hairaan reh gaye.

Unhone Bhagwan ki mahima sweekar kar li.

Rishi Drumila bole,

“Bhagwan ne sansaar ki raksha ke liye anek avataar liye.”

“Matsya avataar mein unhone pralay ke samay Manu, rishiyon aur jeevon ki raksha ki.”

“Varaha avataar mein unhone samundar mein doobi hui dharti ko uthaya aur Hiranyaksha raakshas ko maara.”

“Kurma avataar mein samudra manthan ke samay Mandarachal parvat ko apni peeth par sambhaala.”

“Narasimha avataar mein Bhagwan ne bhakt Prahlad ki raksha ki aur Hiranyakashipu ka vinaash kiya.”

“Vamana avataar mein unhone Raja Bali se teen pag bhoomi maangkar poori prithvi devtaon ko wapas dilayi.”

“Parashurama avataar mein adharmi kshatriyon ka vinaash kiya.”

“Ram avataar mein unhone samundar par setu banaya aur dusht Ravan ko maara.”

Rishi ne aage kaha,

“Bhagwan Krishna bhi Yadu vansh mein avataar lenge aur dharti ka bojh kam karenge.”

“Woh aise kaam karenge jo devtaon ke liye bhi kathin honge.”

“Fir Kaliyug mein Bhagwan Buddha roop mein aayenge aur logon ko ahimsa ka maarg dikhayenge.”

“Ant mein Bhagwan Kalki roop mein prakat hokar adharm ka vinaash karenge.”

Rishi Drumila bole,

“Bhagwan ke avataar aur leelaayein anant hain.”

“Woh hamesha dharm ki raksha aur bhakton ke kalyaan ke liye avataar lete hain.”

Rishi Shukadev bole, “Jo vyakti Bhagwan Hari ke avataaron ki kathaa shraddha se sunta hai, uska mann pavitra ho jaata hai aur uske andar dheere-dheere bhakti jagne lagti hai.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 5
    with st.expander("Chapter 5 - Yuga-wise Methods of Worshipping the Lord"):
        text1 = """ 
        Raja Nimi ne poocha, “Hey mahan rishiyon, jo log Bhagwan Hari ki bhakti nahi karte aur apni ichchhaon mein hi uljhe rehte hain, unka kya hota hai?”

Tab Rishi Camasa bole,

“Bhagwan ne hi chaar varn aur jeevan ke alag-alag aashram banaye hain.”"""
        create_image_text_layout(
            "attached_assets/chapter11/11.5.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        “Lekin jo log apne hi rachayita Bhagwan ko bhool jaate hain, woh dheere-dheere adharm aur dukh mein gir jaate hain.”

Rishi ne daya bhare swar mein kaha,

“Jo log Bhagwan ki kathaa aur bhakti se door rehte hain, un par daya karni chahiye aur unhe sahi maarg dikhana chahiye.”

“Bahut log Vedo ka sachcha arth samjhe bina sirf sukh aur swarg ki ichchha mein lage rehte hain.”

“Woh dhan, sundarta, bal aur ghamand mein andhe ho jaate hain.”

“Fir woh bhakton aur Bhagwan dono ka apmaan karne lagte hain.”

Rishi ne samjhaaya,

“Maans, madira aur bhog ki ichchha toh praniyon mein pehle se hoti hai.”

“Vedo ka uddeshya in ichchhaon ko badhaana nahi, balki dheere-dheere unse door karna hai.”

“Lekin moorkh log Vedo ka galat arth nikaal kar apni ichchha poori karne lagte hain.”

“Jo log hinsa aur paap karte hain, unhe baad mein uska dukh bhi bhogna padta hai.”

Raja Nimi ne fir poocha,

“Hey Rishi, alag-alag yugon mein Bhagwan kaise pooje jaate hain?”

Tab Rishi Karabhajana bole,

“Har yug mein Bhagwan alag roop aur naam se prakat hote hain.”

“Krita Yug mein Bhagwan safed roop mein prakat hote hain.”

“Us yug ke log shaant aur tapasvi hote hain.”

“Woh dhyaan aur tapasya se Bhagwan ki pooja karte hain.”

“Tretayug mein Bhagwan laal roop dhaaran karte hain.”

“Us samay log bade-bade yagya karke unki pooja karte hain.”

“Dwaparyug mein Bhagwan shyam-neele roop mein prakat hote hain.”

“Woh peele vastra pehente hain aur shankh, chakra aur gada dhaaran karte hain.”

“Us yug mein log mandiron, pooja aur mantraon se Bhagwan ki aaradhana karte hain.”

Fir Rishi bole,

“Lekin Kaliyug sabse vishesh hai.”

“Kaliyug mein sirf Bhagwan ka naam gaane aur unki kathaa sunne se bhi jeev ka uddhaar ho sakta hai.”

“Buddhimaan log Hari naam sankirtan ko sabse bada yagya maante hain.”

“Bhagwan ka naam lena hi iss yug ka sabse bada dharm hai.”

Rishi ne prem se kaha,

“Jo vyakti Hari ka naam gaata hai, uska mann dheere-dheere pavitra ho jaata hai.”

“Bhagwan ke charan sansaar ke dukh se paar le jaane waali naav jaise hain.”

“Isliye mahan log bhi Kaliyug mein janm lena chahte hain, kyunki iss yug mein bhakti bahut aasaan hai.”

Rishi ne aur kaha,

“Dakshin Bharat ki pavitra nadiyon ke paas bahut saare Hari bhakt janm lenge.”

“Jo log un pavitra sthalon ka jal peete aur Hari ka naam lete hain, unka hriday shuddh ho jaata hai.”

Fir Narad ji ne Vasudev se kaha,

“Hey Vasudev, tum bahut bhaagyashaali ho.”

“Bhagwan Krishna ne tumhe apne mata-pita ke roop mein chuna.”

“Unke saath rehkar, unhe gale lagakar aur unse prem karke tumhara hriday pehle hi pavitra ho chuka hai.”

“Krishna ko sirf apna putra mat samjho. Woh swayam Parmatma hain jo sansaar ki raksha ke liye manushya roop mein aaye hain.”

Rishi Shukadev bole, “Yeh pavitra gyaan sunkar Vasudev aur Devaki ka moh dheere-dheere door ho gaya.”

“Jo vyakti shraddha se in mahan rishiyon ki baaton ko sunta aur yaad rakhta hai, uska mann Maya se mukt hone lagta hai aur uske andar Bhagwan ke prati sachchi bhakti jagti hai.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6
    with st.expander("Chapter 6 - Lord Kṛṣṇa Requested to return to Vaikuṇṭha"):
        text1 = """ 
        Rishi Shukadev bole, “Ek din Devarshi Narad ke jaane ke baad Brahma ji, Shiv ji aur bahut saare devta Dwaraka aaye.”

Unke saath Indra, Marut, Gandharv, Apsaraayein, Siddh aur kai mahan rishi bhi the.

Sab Bhagwan Krishna ka darshan karna chahte the.

Jab woh Dwaraka pahunche, toh us nagari ki shaan aur sundarta dekhkar hairaan reh gaye.

Sab devta Krishna ke sundar roop ko prem se dekhne lage. Unki aankhen tript hi nahi ho rahi thi.

Unhone Krishna par swarg ke pushpon ki varsha ki aur unki stuti karne lage."""
        create_image_text_layout(
            "attached_assets/chapter11/11.6.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Devta bole,

“Hey Prabhu, hum aapke charanon mein pranam karte hain.”

“Aapke charan hi bhakton ko sansaar ke dukh aur karmo ke bandhan se bachate hain.”

“Aap hi is brahmand ko rachate, sambhalte aur samaapt karte hain, fir bhi Maya aapko kabhi bandh nahi paati.”

“Sirf aapki kathaa sunne se hi mann pavitra ho jaata hai.”

Devtaon ne kaha,

“Bhagwan, aapke charan Ganga ji se bhi adhik pavitra hain.”

“Jo log prem se aapka naam lete hain aur aapki kathaa sunte hain, unka jeevan safal ho jaata hai.”

Fir Brahma ji Krishna se bole,

“Hey Prabhu, aapne dharti ka bojh kam kar diya.”

“Dharm ko fir se sthapit kiya aur duniya mein apni mahima phaila di.”

“Ab 125 saal beet chuke hain jabse aap Yadu vansh mein prakat hue.”

“Yadav vansh bhi ab Brahmano ke shraap se vinaash ke paas pahunch chuka hai.”

“Agar aapki ichchha ho, toh ab apne divya dham Vaikunth laut chaliye.”

Bhagwan Krishna muskuraakar bole,

“Hey Brahma ji, jo aap keh rahe hain, woh main pehle hi tay kar chuka hoon.”

“Dharti ka bojh kam ho chuka hai.”

“Lekin Yadav vansh ab apni shakti aur dhan ke ghamand mein bhar gaya hai.”

“Agar main inhe roke bina chala gaya, toh yeh poori duniya ko vinaash ki taraf le jaayenge.”

“Brahmano ka shraap ab unke vinaash ka kaaran banega.”

“Unke ant ke baad hi main Vaikunth jaaunga.”

Rishi Shukadev bole, “Yeh sunkar Brahma aur sab devta Krishna ko pranam karke apne-apne lok laut gaye.”

Uske baad Krishna ne Dwaraka mein bahut bure apashagun dekhe.

Woh Yadav buzurgon se bole,

“Har taraf ashubh sanket dikh rahe hain.”

“Brahmano ka shraap bhi hamare vansh par aa chuka hai.”

“Isliye ab humein Dwaraka chhodkar Prabhas teerth jaana chahiye.”

Krishna ne kaha,

“Wahan snaan karke hum devtaon aur pitron ki pooja karenge.”

“Brahmano ko bhojan aur daan denge. Isse humare paap door honge.”

Yadav log Krishna ki baat maan kar yatra ki taiyaari karne lage.

Lekin Uddhav ji sab samajh gaye.

Woh ek shaant jagah par Krishna ke paas aaye aur bhaavuk hokar bole,

“Hey Prabhu, aap ab iss sansaar ko chhodne wale hain.”

“Main aapse ek pal ke liye bhi door nahi reh sakta.”

“Kripya mujhe bhi apne saath le chaliye.”

Uddhav ji ki aankhon mein aansu aa gaye.

Woh bole,

“Jo vyakti ek baar aapki madhur leela aur baatein sun leta hai, uska mann duniya ke sukh mein nahi lagta.”

“Humne aapke saath baithkar, chal kar, khaakar aur hanskar jeevan bitaya hai.”

“Aapke bina hum kaise jee paayenge?”

“Hum toh aapki bachi hui mala, vastra aur prasad paakar hi apne jeevan ko safal maante hain.”

“Bhakt aapki kathaa sunte, yaad karte aur ek doosre ko sunaate hue hi Maya se paar ho jaate hain.”

Rishi Shukadev bole, “Uddhav ki prem bhari baatein sunkar Bhagwan Krishna unse kuch gehra gyaan kehne wale the.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7
    with st.expander("Chapter 7 - The Legend of the Avadhūta and his Preceptors"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter11/11.7.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 8
    with st.expander("Chapter 8 - What the Avadhūta learnt from the Nine-Preceptors"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter11/11.8.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 9
    with st.expander("Chapter 9 - The Discourse of the Avadhūta Concluded"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter11/11.9.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 10
    with st.expander("Chapter 10 - How the Jīva is Ensnared in Saṃsāra"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter11/11.10.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 11
    with st.expander("Chapter 11 - Characteristics of Bondage and Liberation and of Devotion"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter11/11.11.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 12
    with st.expander("Chapter 12 - The Performance and Renunciation of Prescribed Karmas"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter11/11.12.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 13
    with st.expander("Chapter 13 - The Spiritual Knowledge Imparted by the Divine Swan"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter11/11.13.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 14
    with st.expander("Chapter 14 - The Path of Devotion and the Method of Meditation"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter11/11.14.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 15
    with st.expander("Chapter 15 - The Super-normal Powers Attained by Yoga"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter11/11.15.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 16
    with st.expander("Chapter 16 - Description of Viṣṇu’s Glorious Manifestations"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter11/11.16.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 17
    with st.expander("Chapter 17 - The Sacred Duties of a Celibate and a Householder"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter11/11.17.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 18
    with st.expander("Chapter 18 - Duties of Hermits (Vānaprastha) and Sannyāsins"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter11/11.18.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 19
    with st.expander("Chapter 19 - Exposition of Spiritual Knowledge"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter11/11.19.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 20
    with st.expander("Chapter 20 - Elucidation of Karma, Jñāna and Bhakti Yogas"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter11/11.20.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 21
    with st.expander("Chapter 21 - Criteria for determining the good and the evil"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter11/11.21.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 22
    with st.expander("Chapter 22 - Enumeration of Principles (Tattvas)"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter11/11.22.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 23
    with st.expander("Chapter 23 - The Song of a Recluse (Bhikṣu Gītā)"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter11/11.23.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 24
    with st.expander("Chapter 24 - Elucidation of Sāṃkhya Yoga"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter11/11.24.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 25
    with st.expander("Chapter 25 - The Three Guṇas and Their Workings"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter11/11.25.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 26
    with st.expander("Chapter 26 - The Song of Aila (Purūravas)"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter11/11.26.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 27
    with st.expander("Chapter 27 - The Yoga of Active Service"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter11/11.27.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 28
    with st.expander("Chapter 28 - The Essence of the Path of Knowledge (Jñāna Yoga)"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter11/11.28.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 29
    with st.expander("Chapter 29 - Bhakti Yoga Recapitulated: Departure of Uddhava to Badarikāśrama"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter11/11.29.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 30
    with st.expander("Chapter 30 - Extermination of the Race of Yādavas"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter11/11.30.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 31
    with st.expander("Chapter 31 - Lord Kṛṣṇa’s Return to Vaikuṇṭha"):
        text1 = """ """
        create_image_text_layout(
            "attached_assets/chapter11/11.31.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")

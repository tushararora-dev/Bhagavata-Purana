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
        text1 = """ 
        Rishi Shukadev bole, “Bhagwan Krishna ne Uddhav se kaha,

‘Hey Uddhav, jo tumne kaha, wahi ab hone wala hai.’

‘Devta aur Brahma ji chahte hain ki main jaldi apne divya dham Vaikunth laut jaun.’

‘Dharti ka bojh kam karne ke liye main aur Balram is sansaar mein aaye the. Ab woh kaarya poora ho chuka hai.’"""
        create_image_text_layout(
            "attached_assets/chapter11/11.7.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        ‘Yadav vansh bhi Brahmano ke shraap se jaldi hi apne hi jhagdon mein samaapt ho jaayega.’

‘Aur mere jaane ke baad samundar Dwaraka nagari ko dubo dega.’

Krishna ne fir kaha,

‘Mere prithvi se jaate hi Kaliyug ka prabhav badhne lagega.’

‘Log dheere-dheere adharm aur buri aadaton mein phans jaayenge.’

‘Isliye tum yahaan zyada der mat rukna.’

‘Sab rishton aur moh ko chhodkar sirf mujh mein apna mann lagaana.’

‘Sabko samaan drishti se dekhte hue dharti par bhraman karna.’

Krishna bole,

‘Jo kuch hum aankhon, kaanon aur mann se dekhte aur mehsoos karte hain, woh sab Maya ka khel hai aur ek din samaapt ho jaata hai.’

‘Asli sach toh aatma hai, jo amar hai.’

‘Jo vyakti sab jeevon mein mujhe dekhta hai aur apne mann ko shaant rakhta hai, woh sansaar ke dukh se bach jaata hai.’

Rishi Shukadev bole, “Krishna ki baatein sunkar Uddhav aur bhi adhik gyaan paana chahte the.”

Woh vinamrata se bole,

“Hey Prabhu, aapne jo vairagya aur tyag ka maarg bataya hai, woh bahut kathin lagta hai.”

“Jin logon ka mann sansaar ke sukh mein laga ho, unke liye yeh bahut mushkil hai.”

“Mera mann bhi abhi ‘main’ aur ‘mera’ ke moh mein phansa hua hai.”

“Kripya mujhe aisa gyaan dijiye jisse main bhi iss Maya se paar ho jaun.”

“Hey Krishna, aapke bina koi bhi mujhe sachcha gyaan nahi de sakta.”

“Devta bhi aapki Maya se poori tarah pare nahi hain.”

“Main toh aapki sharan mein aaya hoon.”

Tab Bhagwan Krishna bole,

“Hey Uddhav, buddhimaan vyakti apne anubhav aur vivek se bhi gyaan paa sakta hai.”

“Insaan ka apna aatma hi uska sabse bada guru ban sakta hai.”

“Manushya janm bahut anmol hai, kyunki isi mein jeev Bhagwan ko samajh sakta hai.”

Krishna ne fir ek purani katha sunaayi.

Woh bole,

“Ek baar Raja Yadu ne ek avadhut Brahman ko dekha.”

“Woh yuva tha, lekin bilkul nishchint aur anand mein rehta tha.”

“Na usse dhan ki chinta thi aur na kisi cheez ka moh.”

Raja Yadu ne poocha,

‘Hey Brahman, aap itne nishchint aur anandit kaise rehte hain?’

‘Duniya ke log toh kaam, dhan aur sukh ke peeche bhaagte rehte hain.’

‘Lekin aap bina kisi chinta ke ek bachche ki tarah ghoom rahe hain.’

‘Aapne yeh gyaan kahaan se paaya?’

Tab Avadhut bole,

‘Maine prakriti aur jeev-jantuon se seekh li hai.’

‘Mere 24 guru hain.’

‘Dharti, hawa, aakash, paani, agni, suraj, chand, samundar, madhumakkhi, hiran, machhli aur kai anya jeev mere guru bane.’

Avadhut ne samjhaaya,

‘Dharti se maine dhairya aur sahanshilta seekhi.’

‘Pedon aur pahaadon se maine doosron ke liye jeena seekha.’

‘Hawa se maine seekha ki duniya mein rehkar bhi kisi cheez se chipakna nahi chahiye.’

‘Aakash se maine seekha ki aatma sab jagah hai, lekin kisi cheez se bandhati nahi.’

‘Paani se maine pavitrata aur madhur swabhav seekha.’

‘Agni se maine tej aur pavitrata seekhi.’

‘Suraj se maine seekha ki lena aur dena dono bina moh ke karna chahiye.’

Phir Avadhut ne kabootar ki kahani sunaayi.

Woh bole,

“Ek kabootar apni patni aur bachchon se bahut adhik moh karta tha.”

“Ek din shikaari ne uske bachchon ko jaal mein pakad liya.”

“Unhe bachane ke chakkar mein pehle maa kabootri aur fir pita kabootar bhi jaal mein phans gaye.”

“Is tarah poora parivaar vinaash ho gaya.”

Avadhut bole,

“Jo vyakti sansaarik moh mein zyada phans jaata hai, uska haal bhi us kabootar jaisa ho jaata hai.”

“Manushya janm moksha paane ka ek khula dwar hai.”

“Lekin jo sirf ghar-parivaar aur moh mein hi phansa rahe, woh apne jeevan ka sachcha uddeshya kho deta hai.”

Rishi Shukadev bole, “Bhagwan Krishna Uddhav ko dheere-dheere gehra aatma-gyaan aur vairagya ka maarg samjha rahe the.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 8
    with st.expander("Chapter 8 - What the Avadhūta learnt from the Nine-Preceptors"):
        text1 = """ 
        Avadhut Brahman ne Raja Yadu se kaha,

“Hey Raja, sukh aur dukh har jeev ke jeevan mein aate hain.”

“Isliye buddhimaan vyakti ko unke peeche bhaagna nahi chahiye.”

“Maine अजगर yani boa-constrictor se seekha ki jo kuch bina adhik mehnat ke mil jaaye, usi mein santusht rehna chahiye.”"""
        create_image_text_layout(
            "attached_assets/chapter11/11.8.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        “Jaise ajgar chupchaap pada rehta hai aur jo bhojan milta hai wahi kha leta hai, waise hi sant vyakti ko bhi adhik lalach nahi karna chahiye.”

“Kabhi bhojan kam mile ya na mile, tab bhi shaant rehna chahiye.”

Avadhut bole,

“Maine samundar se seekha ki mann ko gehra aur shaant rakhna chahiye.”

“Jaise bahut saari nadiyan samundar mein girti hain, fir bhi samundar apni seema nahi todta, waise hi buddhimaan vyakti ko sukh ya dukh mein zyada hilna nahi chahiye.”

“Maine patange se seekha ki sundarta aur vasna ke peeche bhaagna vinaash ka kaaran ban sakta hai.”

“Patanga aag ki roshni dekhkar usmein jal jaata hai.”

“Waise hi insaan bhi moh mein padkar dukh paata hai.”

“Maine madhumakkhi se seekha ki thoda-thoda lekar jeevan chalana chahiye aur adhik sangrah nahi karna chahiye.”

“Lekin maine yeh bhi dekha ki madhumakkhi saara jeevan shahad jama karti hai aur aakhir mein koi aur aakar use le jaata hai.”

“Isliye dhan ka adhik lalach aur sangrah dukhad hota hai.”

Avadhut ne kaha,

“Maine hathi se seekha ki kaam vasna insaan ko bandh leti hai.”

“Jaise hathi maada hathi ke moh mein phanskar pakad liya jaata hai, waise hi manushya bhi vasna mein phans sakta hai.”

“Maine hiran se seekha ki madhur sangeet bhi kabhi-kabhi vinaash ka kaaran ban sakta hai.”

“Shikaari madhur awaaz se hiran ko phansa leta hai.”

“Isliye mann ko sada saavdhaan rakhna chahiye.”

“Maine machhli se seekha ki jeebh ka lalach bahut khatarnak hota hai.”

“Machhli swaad ke lalach mein kaante ko nigal leti hai aur pakdi jaati hai.”

“Jo vyakti jeebh par niyantran kar leta hai, woh dheere-dheere sab indriyon ko jeet leta hai.”

Uske baad Avadhut ne Pingala naam ki ek vaishya ki kahani sunaayi.

Woh bole,

“Ek raat Pingala sundar kapde aur gehne pehenkar apne ghar ke baahar khadi thi.”

“Woh kisi dhanwaan grahak ka intezaar kar rahi thi.”

“Bahut log aaye aur chale gaye, lekin koi uske paas nahi aaya.”

“Raat bahut beet gayi aur uski umeedein tootne lagi.”

“Woh dukhi aur thaki hui ho gayi.”

Fir achanak uske mann mein ek gehra vichaar aaya.

Pingala boli,

‘Main kitni moorkh thi jo jhoothe sukh aur swarthi logon ke peeche bhaag rahi thi.’

‘Sachcha sukh toh Bhagwan mein hai.’

‘Sansaar ke log na kabhi poori khushi de sakte hain aur na sada saath reh sakte hain.’

‘Ab main Bhagwan Narayan ko hi apna sachcha priya maanungi.’

‘Main jo kuch bhi Bhagwan ki ichchha se milega, usi mein santusht rahungi.’

Rishi Shukadev bole, “Jaise hi Pingala ne duniya ki jhoothi aasha chhod di, uske mann ko shaanti mil gayi.”

“Us raat woh bahut sukoon se soyi.”

Avadhut Brahman bole,

“Sabse bada dukh jhoothi umeed aur lalach hai.”

“Aur sabse bada sukh hai — ichchhaon ko chhodkar Bhagwan mein santusht rehna.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 9
    with st.expander("Chapter 9 - The Discourse of the Avadhūta Concluded"):
        text1 = """ 
        Avadhut Brahman ne Raja Yadu se kaha,

“Hey Raja, jis cheez ko log bahut sambhaal kar rakhna chahte hain, wahi kai baar dukh ka kaaran ban jaati hai.”

“Jo vyakti adhik moh aur sangrah chhod deta hai, wahi sachcha sukh paata hai.”

“Maine ek cheel se seekha ki chhod dene mein hi shaanti hai.”

“Ek cheel maans ka tukda lekar udd rahi thi. Doosre pakshi us par hamla karne lage.”

“Jab usne maans ka tukda chhod diya, tab use turant shaanti mil gayi.”"""
        create_image_text_layout(
            "attached_assets/chapter11/11.9.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Avadhut bole,

“Maine bachche se seekha ki nirdosh aur chinta se mukt rehna kitna sukh deta hai.”

“Jo vyakti duniya ke ghamand aur moh se pare ho jaata hai, woh bachche ki tarah nishchint ho jaata hai.”

“Maine ek kanya se bhi seekha.”

“Ek din uske ghar mehmaan aaye, lekin ghar mein aur koi nahi tha.”

“Woh akeli chaawal pees rahi thi. Uski choodiyan aapas mein takraakar awaaz kar rahi thi.”

“Usne ek-ek karke saari choodiyan tod di aur har haath mein sirf ek choodi chhod di.”

“Fir awaaz band ho gayi.”

“Tab maine samjha ki zyada log saath rahenge toh jhagda aur baatein badhengi.”

“Isliye saadhak ko akela aur shaant rehkar Bhagwan ka dhyaan karna chahiye.”

Avadhut ne kaha,

“Maine baan banane waale ek kaarigar se seekha ki mann ko ekagra kaise karte hain.”

“Woh apne kaam mein itna dhyaan lagaaye hua tha ki usse raja ki badi sawaari ke guzarne ka bhi pata nahi chala.”

“Waise hi yogi ko bhi apna mann poori tarah Bhagwan mein laga dena chahiye.”

“Maine saanp se seekha ki akela rehna aur bina adhik ghar-grihasthi ke jeena achha hai.”

“Saanp doosron ke banaye hue bill mein reh leta hai aur bina shor ke apna jeevan bitaata hai.”

“Maine makdi se seekha ki Bhagwan hi iss sansaar ko rachate aur fir samay aane par use apne andar sama lete hain.”

“Jaise makdi apna jaal khud banati aur wapas sama leti hai.”

“Maine bhanwre aur keede se bhi seekha.”

“Keeda darr aur dhyaan mein lagataar bhanwre ko yaad karta hai aur dheere-dheere uske jaise roop mein badal jaata hai.”

“Waise hi insaan jiska dhyaan baar-baar jis cheez par lagata hai, dheere-dheere usi jaise gun apna leta hai.”

Avadhut bole,

“Mera apna sharir bhi mera guru bana.”

“Yeh sharir janm leta hai, budha hota hai aur ek din samaapt ho jaata hai.”

“Isliye maine samjha ki ispar adhik moh karna theek nahi.”

“Insaan sharir ke sukh ke liye dhan, ghar aur parivaar mein uljha rehta hai.”

“Lekin antim samay mein sab yahin chhoot jaata hai.”

“Maine yeh bhi dekha ki indriyan insaan ko alag-alag disha mein kheenchti rehti hain.”

“Jeebh swaad ke peeche bhaagti hai, aankhen sundarta ke peeche aur mann ichchhaon ke peeche.”

“Isliye jo vyakti apne mann aur indriyon ko sambhaal leta hai, wahi sachchi shaanti paata hai.”

Avadhut ne fir kaha,

“Bahut janmon ke baad insaan ko yeh anmol manushya janm milta hai.”

“Yeh sharir nashwar hai, lekin isi ke dwaara Bhagwan ko paaya ja sakta hai.”

“Isliye buddhimaan vyakti ko maut aane se pehle hi Bhagwan ki bhakti aur aatma-gyaan mein lag jaana chahiye.”

“Sansaar ke sukh toh har janm mein mil sakte hain, lekin moksha ka maarg manushya jeevan mein hi khulta hai.”

Rishi Shukadev bole, “Avadhut Brahman ki baatein sunkar Raja Yadu ka moh door ho gaya.”

“Woh sab jeevon ko samaan drishti se dekhne lage aur unka mann shaant ho gaya.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 10
    with st.expander("Chapter 10 - How the Jīva is Ensnared in Saṃsāra"):
        text1 = """ 
        Bhagwan Krishna ne Uddhav se kaha,

“Hey Uddhav, jo vyakti bina kisi swaarth ke apne kartavya karta hai aur sab kuch mujhe samarpit kar deta hai, uska mann dheere-dheere pavitra ho jaata hai.”

“Insaan ko apne varn aur aashram ke anusaar dharm ka paalan karna chahiye, lekin phal ki ichchha nahi rakhni chahiye.”

“Duniya ke log sukh ke peeche bhaagte hain, lekin aksar unhe dukh hi milta hai.”"""
        create_image_text_layout(
            "attached_assets/chapter11/11.10.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        “Jaise sapne mein dekhi hui cheezein sach nahi hoti, waise hi sansaar ke bahut se sukh bhi ek bhram jaise hain.”

Krishna bole,

“Jo vyakti sirf meri bhakti mein laga rehta hai, use ahimsa, satya aur indriya niyantran jaise gun apnaane chahiye.”

“Use ek sache aur shaant guru ki seva karni chahiye.”

“Use ghamand, irsha aur adhik bolne se bachna chahiye.”

“Dheere-dheere use ghar, dhan aur parivaar ke prati adhik moh bhi chhodna chahiye.”

Krishna ne samjhaaya,

“Sharir aur aatma alag hain.”

“Sharir janm leta hai, badalta hai aur ek din samaapt ho jaata hai.”

“Lekin aatma sada amar aur prakashmay rehti hai.”

“Jaise agni lakdi mein rehkar bhi lakdi se alag hoti hai, waise hi aatma sharir mein rehkar bhi usse alag hai.”

“Lekin agyaan ki wajah se jeev khud ko sharir samajhne lagta hai. Isi se sansaar ka bandhan shuru hota hai.”

Krishna bole,

“Guru aur shishya ka sambandh bhi pavitra hota hai.”

“Jaise do lakdiyon ko ragadne se agni nikalti hai, waise hi guru ke gyaan se shishya ke mann mein satya ka prakash hota hai.”

“Fir yeh gyaan dheere-dheere Maya aur moh ko jala deta hai.”

Bhagwan ne fir kaha,

“Log sochte hain ki swarg aur bhog se sukh milega.”

“Lekin swarg ka sukh bhi ek din samaapt ho jaata hai.”

“Jab punya khatam ho jaata hai, tab jeev ko fir se neeche aana padta hai.”

“Isliye jo sukh shuru aur ant waala ho, woh sachcha sukh nahi ho sakta.”

Krishna ne samjhaaya,

“Jo vyakti adharm aur buri sangat mein pad jaata hai, woh dheere-dheere lalchi, kaami aur kathor ban jaata hai.”

“Fir woh paap karta hai aur dukh paata hai.”

“Lekin jo vyakti bhakti aur satya ka maarg pakadta hai, woh Maya ke bandhan se dheere-dheere bahar aa jaata hai.”

Bhagwan bole,

“Indriyan aur mann hi karm karwaate hain.”

“Jab tak jeev gunon aur ichchhaon mein uljha rehta hai, tab tak use janm-mrityu aur dukh ka darr bana rehta hai.”

“Lekin jo vyakti mujhe sab jagah dekhta hai aur mere charanon mein sharan leta hai, uska darr door ho jaata hai.”

Rishi Shukadev bole, “Krishna ki gehri baatein sunkar Uddhav ke mann mein aur prashn jagne lage.”

Uddhav vinamrata se bole,

“Hey Prabhu, agar aatma sach mein azaad aur amar hai, toh fir woh Maya mein bandh kaise jaati hai?”

“Ek bandha hua aur ek mukt vyakti kaise pehchaana jaata hai?”

“Woh kaise jeete hain, kaise chalte-phirte hain aur duniya ko kaise dekhte hain?”

“Hey Krishna, kripya meri is uljhan ko door kijiye.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 11
    with st.expander("Chapter 11 - Characteristics of Bondage and Liberation and of Devotion"):
        text1 = """ 
        Chapter 11 – Bandhan, Mukti aur Bhakti ki Kahani

Bhagwan Krishna ne Uddhava se kaha, “Insaan sochta hai ki woh bandhan mein hai ya azaad hai. Lekin asli Atma kabhi bandhi nahi hoti. Yeh sab Maya ka khel hai.”

Unhone samjhaya ki dukh, sukh, darr aur moh sab sapne ki tarah hote hain. Jaise sapna sach nahi hota, waise hi duniya ka bahut saara dukh bhi sirf bhram hota hai.

Krishna ne kaha, “Gyaan aur agyaan dono meri shaktiyan hain. Agyaan insaan ko baandhta hai, aur gyaan use azaad karta hai.”"""
        create_image_text_layout(
            "attached_assets/chapter11/11.11.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Phir Bhagwan ne ek sundar misaal di. Ek ped par do pakshi baithe the. Ek pakshi phal kha raha tha. Kabhi meetha, kabhi kadwa. Dusra pakshi bas shaant hokar dekh raha tha.
Pehla pakshi Jiva tha, jo duniya ke sukh-dukh mein uljha rehta hai. Dusra Bhagwan tha, jo hamesha shaant aur azaad rehte hain.

Bhagwan ne kaha, “Jo vyakti samajh leta hai ki woh sirf shareer nahi, balki Atma hai, woh dheere-dheere dukh se door ho jata hai.”

Ek gyani vyakti kisi ki burai ya tareef mein zyada nahi padta. Woh sabko ek samaan dekhta hai. Uska mann shaant rehta hai.

Krishna ne bataya ki sirf kitab padhne se sachcha gyaan nahi milta. Agar dil mein bhakti aur prem na ho, toh sab mehnat adhuri reh jaati hai.

Phir Uddhava ne poocha, “Bhagwan, sachcha sant kaun hota hai?”

Bhagwan muskuraaye aur bole, “Jo sab par daya karta hai, kisi se jalan nahi rakhta, sach bolta hai aur apne mann ko shaant rakhta hai, wahi sachcha sant hai.”

Unhone kaha ki sachcha bhakt hamesha Bhagwan ki kahaniyan sunta hai, unka naam leta hai, dusron ki madad karta hai aur bina swarth ke seva karta hai.

Bhagwan ne samjhaya, “Jo vyakti apni sabse pyari cheez bhi prem se mujhe arpan karta hai, uska jeevan safal ho jata hai.”

Ant mein Krishna ne kaha, “Sabse bada raasta bhakti ka hai. Achhe aur sant logon ki sangat se hi sachchi bhakti paida hoti hai.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 12
    with st.expander("Chapter 12 - The Performance and Renunciation of Prescribed Karmas"):
        text1 = """ 
        Chapter 12 – Santon ki Sangat aur Sachchi Bhakti

Bhagwan Krishna ne Uddhava se kaha, “Sirf yoga, tapasya, daan ya Vedas padhne se mujhe paana aasaan nahi hota. Sabse bada raasta hai achhe santon ki sangat.”

Unhone samjhaya ki jab insaan achhe aur bhakt logon ke saath rehta hai, tab uska mann dheere-dheere pavitra ho jata hai.

Bhagwan ne bahut examples diye. Unhone bataya ki Prahlad, Hanuman, Gajendra haathi, Jatayu pakshi aur Vrindavan ki Gopiyan sabne bhakti aur santon ki sangat se unhe paaya."""
        create_image_text_layout(
            "attached_assets/chapter11/11.12.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Krishna ne kaha, “Inme se kai logon ne bade yagya ya kathin tapasya nahi ki thi. Phir bhi unhone mujhe paa liya, kyunki unka prem sachcha tha.”

Vrindavan ki Gopiyan Krishna se bahut prem karti thi. Jab Krishna Mathura chale gaye, toh unhe bahut dukh hua. Unka mann hamesha Krishna mein hi laga rehta tha.

Bhagwan ne kaha, “Sachchi bhakti mein insaan apne aap ko bhi bhool jata hai. Sirf Bhagwan ka prem reh jata hai.”

Phir Krishna ne Uddhava ko samjhaya ki duniya ek bade vriksh ki tarah hai. Is vriksh ki jad hai ichchha aur karm. Is par sukh aur dukh dono phal lagte hain.

Jo log sirf duniya ke sukh ke peeche bhaagte hain, woh dukhi rehte hain. Lekin jo gyaan aur bhakti ka raasta chunte hain, woh shanti pa lete hain.

Bhagwan ne kaha, “Guru ki seva aur sachcha gyaan ek tez kulhadi ki tarah hai. Yeh janam-maran ke bandhan ko kaat deta hai.”

Unhone akhir mein kaha, “Mere prati poori shraddha aur prem rakho. Santon ki sangat karo. Tab tumhe asli shanti aur moksha milega.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 13
    with st.expander("Chapter 13 - The Spiritual Knowledge Imparted by the Divine Swan"):
        text1 = """ 
        Chapter 13 – Divine Hans ki Gyaan Bhari Seekh

Bhagwan Krishna ne Uddhava se kaha, “Sattva, Rajas aur Tamas yeh teen gun insaan ke mann aur buddhi ke hote hain, Atma ke nahi.”

Unhone samjhaya ki Sattva guna shanti, sachchai aur bhakti ko badhata hai. Rajas insaan ko ichchha aur lalach mein daalta hai. Tamas आलस aur andhkaar laata hai.

Krishna ne kaha, “Jo vyakti achhi cheezein, achhe vichaar aur achha sang chunta hai, uska Sattva badhta hai. Phir uske andar bhakti aur gyaan aata hai.”"""
        create_image_text_layout(
            "attached_assets/chapter11/11.13.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Uddhava ne poocha, “Log jaante hue bhi galat cheezon ke peeche kyun bhaagte hain?”

Bhagwan bole, “Jab mann par Rajas ka asar hota hai, toh insaan baar-baar sukh dene wali cheezon ke baare mein sochta hai. Dheere-dheere uski ichchha bahut strong ho jaati hai aur woh apne aap ko rok nahi paata.”

Krishna ne samjhaya ki gyani vyakti ko apne mann ko dhyaan aur saans par control karke shaant banana chahiye.

Phir Uddhava ne poocha, “Aapne purane rishiyon ko yeh gyaan kaise diya tha?”

Bhagwan ne ek purani kahani sunayi.

Bahut pehle Sanak aur dusre rishiyon ne Brahma ji se poocha, “Mann aur duniya ek dusre mein itne uljhe kyun hain? Insaan inse azaad kaise ho?”

Brahma ji kuch der sochte rahe, lekin jawab poori tarah samajh nahi paaye. Tab Bhagwan ek sundar hans ke roop mein wahan aaye.

Rishiyon ne poocha, “Aap kaun hain?”

Bhagwan muskuraaye aur bole, “Jab sab mein ek hi Atma hai, toh ‘tum kaun ho’ aur ‘main kaun hoon’ ka farq sirf mann ka bhram hai.”

Unhone samjhaya ki yeh duniya sapne ki tarah hai. Jaise sapna tootne par sab gayab ho jata hai, waise hi duniya ke bahut saare dukh aur farq bhi ek din mit jaate hain.

Bhagwan ne kaha, “Jo vyakti apne andar mujhe mehsoos karta hai, woh darr aur moh se azaad ho jata hai.”

Unhone bataya ki mann ko dheere-dheere duniya ki ichchhaon se hata kar Bhagwan mein lagana chahiye. Tab insaan ko asli shanti milti hai.

Ant mein Bhagwan ne kaha, “Gyaan, yoga aur dharma ka asli lakshya main hi hoon. Jo mujhe apne dil mein pa leta hai, uske sab doubts khatam ho jaate hain.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 14
    with st.expander("Chapter 14 - The Path of Devotion and the Method of Meditation"):
        text1 = """ 
        Chapter 14 – Bhakti ka Raasta aur Dhyaan ki Vidhi

Uddhava ne Krishna se poocha, “Log kehte hain ki moksha paane ke bahut raaste hain. Kya sab barabar hain ya koi ek sabse bada hai?”

Bhagwan Krishna bole, “Sabse uttam raasta Bhakti ka hai. Jab insaan sachche prem se mujhe yaad karta hai, uska mann dheere-dheere duniya ki ichchhaon se door ho jata hai.”

Krishna ne bataya ki prachin samay mein unhone yeh gyaan Brahma ji ko diya tha. Brahma ji ne ise Manu aur rishiyon ko sikhaya. Phir yeh gyaan duniya mein phail gaya."""
        create_image_text_layout(
            "attached_assets/chapter11/11.14.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Lekin har insaan ka swabhav alag tha. Isliye logon ne alag-alag raaste chun liye.
Kisi ne dhan ko sabse bada maana. Kisi ne tapasya ko. Kisi ne sukh aur bhog ko.

Bhagwan ne kaha, “Yeh sab cheezein kuch samay ke liye khushi deti hain, lekin hamesha ki shanti nahi deti.”

Unhone samjhaya ki jo vyakti bina kisi swarth ke Bhagwan se prem karta hai, wahi asli anand paata hai.

Krishna bole, “Mera sachcha bhakt mujhe chhodkar aur kuch nahi chahta. Na swarg, na shakti, na dhan.”

Bhagwan ne kaha ki bhakti ek jalti hui agni ki tarah hai. Jaise aag lakdi ko jala kar raakh bana deti hai, waise hi bhakti paapon aur bure sanskaron ko mita deti hai.

Jo bhakt prem se Bhagwan ka naam leta hai, kabhi gaata hai, kabhi ro padta hai aur kabhi khushi se nachne lagta hai, uska dil pavitra ho jata hai.

Krishna ne samjhaya, “Jis tarah mann baar-baar duniya ki cheezon ko sochkar unmein phans jata hai, waise hi agar mann mujhe yaad kare, toh woh mujh mein hi lag jata hai.”

Phir Uddhava ne poocha, “Dhyaan ka sahi tareeka kya hai?”

Bhagwan ne bade shaant mann se bataya:

“Ek saaf aur shaant jagah par seedha baitho. Saans ko dheere-dheere control karo. Mann ko shaant banao.”

Phir unhone kaha ki dhyaan mein Bhagwan ke sundar roop ko mann mein dekhna chahiye — unka komal chehra, madhur muskaan, shankh, chakra aur unka daya se bhara roop.

Krishna bole, “Dheere-dheere mann ko duniya se hata kar sirf mujhmein laga do. Tab insaan ko asli shanti aur anand milta hai.”

Ant mein Bhagwan ne kaha, “Jab mann poori tarah Bhagwan mein sama jata hai, tab saare darr, dukh aur bhram khatam ho jaate hain.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 15
    with st.expander("Chapter 15 - The Super-normal Powers Attained by Yoga"):
        text1 = """ 
        Chapter 15 – Yog ki Shaktiyan aur Asli Raasta

Bhagwan Krishna ne Uddhava se kaha, “Jo yogi apne mann, indriyon aur saans par control kar leta hai aur mujhmein dhyaan lagata hai, usse bahut adbhut shaktiyan mil sakti hain.”

Uddhava ne poocha, “Yeh shaktiyan kaunsi hoti hain?”

Bhagwan ne bataya ki yog se kai siddhiyan milti hain. Kuch yogi apne shareer ko bahut chhota ya bahut bada bana sakte hain. Kuch door ki cheezein dekh aur sun sakte hain. Kuch mann ki speed se kahin bhi pahunch sakte hain."""
        create_image_text_layout(
            "attached_assets/chapter11/11.15.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Kuch yogi apni ichchha se alag roop le sakte hain. Kuch dusron ke mann ko samajh sakte hain. Yeh sab yog ki shaktiyan thi.

Lekin Krishna ne ek bahut zaroori baat kahi.

Unhone bola, “Yeh siddhiyan dekhne mein bahut badi lagti hain, lekin asli yog ka lakshya sirf shakti paana nahi hai.”

Bhagwan ne samjhaya ki agar yogi in shaktiyon mein hi phans jaye, toh uska dhyaan Bhagwan se hat sakta hai.

Krishna bole, “Sachcha yog wahi hai jo insaan ko Bhagwan ke aur kareeb le aaye.”

Phir unhone alag-alag dhyaan ke tareeke bataye.
Kisi yogi ko Bhagwan ko prakriti mein dekhna chahiye. Kisi ko unhe apne hriday mein mehsoos karna chahiye. Kisi ko unki shant aur prakashmay roop par dhyaan lagana chahiye.

Bhagwan ne kaha, “Jo vyakti poore mann se mujhmein dhyaan lagata hai, uske andar dheere-dheere pavitrata aur gyaan jagta hai.”

Unhone samjhaya ki yog se mili shaktiyan temporary hoti hain, lekin Bhagwan ka prem aur moksha sabse bada dhan hai.

Krishna bole, “Jo bhakt sirf mujhe paana chahta hai, uske liye siddhiyan bhi rukawat ban sakti hain.”

Ant mein Bhagwan ne kaha, “Main sabke andar hoon aur sab jagah maujood hoon. Jo mujhe har jeev mein dekhta hai, wahi asli yog ko samajhta hai.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 16
    with st.expander("Chapter 16 - Description of Viṣṇu’s Glorious Manifestations"):
        text1 = """ 
        Chapter 16 – Bhagwan Vishnu ki Divya Mahima

Uddhava ne Krishna se kaha, “Hey Prabhu, aap har jagah kaise maujood hain? Log aapko kin-kin roopon mein yaad karein?”

Bhagwan Krishna muskuraaye aur bole, “Main hi sabka creator, protector aur guide hoon. Har jeev aur har sundar cheez mein mera hi ek hissa chhupa hai.”

Krishna ne samjhaya ki duniya ki har khaas aur shaktishaali cheez unki mahima ka ek chhota sa roop hai.

Unhone kaha, “Vedo mein main Om hoon. Devtaon mein main Indra hoon. Pahadon mein Himalaya hoon. Nadiyon mein Ganga hoon.”"""
        create_image_text_layout(
            "attached_assets/chapter11/11.16.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Bhagwan bole, “Pedon mein main Peepal hoon. Pashuon mein sher hoon. Pakshiyon mein Garuda hoon. Hathi mein Airavat hoon.”

Krishna ne kaha, “Rishiyon mein Narad hoon. Veeron mein Arjun hoon. Bhakton mein Prahlad hoon.”

Unhone samjhaya ki jahan bhi shakti, sundarta, daya, gyaan ya himmat dikhe, samajh lo wahan Bhagwan ka ek ansh hai.

Krishna bole, “Jo bhi cheez logon ko achchai aur sachchai ki taraf le jaaye, usmein meri chamak hoti hai.”

Phir Bhagwan ne ek zaroori baat kahi.

“Sirf duniya ki sundar cheezon mein ulajh mat jaana. Un sabke peeche jo ek sachchai hai, mujhe pehchaano.”

Unhone kaha ki mann, vaani aur indriyon ko control karna bahut zaroori hai. Agar insaan apne mann ko sambhal nahi paata, toh uska gyaan dheere-dheere bekaar ho jata hai.

Krishna ne samjhaya, “Jaise kaccha ghada paani nahi sambhal sakta, waise hi bina mann ko control kiye tapasya aur gyaan tik nahi paate.”

Ant mein Bhagwan bole, “Apna mann aur dil poori tarah mujhmein laga do. Tab tum janam-maran ke dukh se azaad ho jaoge.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 17
    with st.expander("Chapter 17 - The Sacred Duties of a Celibate and a Householder"):
        text1 = """ 
        Chapter 17 – Brahmachari aur Grihastha ke Kartavya

Uddhava ne Krishna se kaha, “Hey Prabhu, log kaise jeevan jeeyein ki unke andar bhakti badhe aur woh sahi raaste par chalein?”

Bhagwan Krishna bole, “Har insaan ke jeevan ka ek dharm aur zimmedari hoti hai. Agar woh imaandari aur bhakti se apne kartavya nibhaye, toh uska mann pavitra ho jata hai.”

Krishna ne bataya ki purane yug mein log bahut simple aur pavitra the. Unka mann sirf Bhagwan ki bhakti mein laga rehta tha."""
        create_image_text_layout(
            "attached_assets/chapter11/11.17.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Phir dheere-dheere society mein alag-alag zimmedariyan bani. Kuch log gyaan aur shiksha dene lage, kuch raksha karne lage, kuch vyapar karne lage aur kuch seva karne lage.

Bhagwan ne kaha, “Sabse zaroori baat hai achha swabhav.”

Unhone samjhaya ki sachchai, daya, santosh, self-control aur bhakti har insaan ke liye zaroori hain.

Phir Krishna ne Brahmachari yani student jeevan ke baare mein bataya.

Unhone kaha, “Ek vidyarthi ko discipline mein rehna chahiye. Guru ka samman karna chahiye. Mann aur indriyon ko control mein rakhna chahiye.”

Student ko simple jeevan jeena chahiye, dhyaan aur padhai par focus karna chahiye aur ahankaar se door rehna chahiye.

Bhagwan ne kaha, “Guru ko sirf teacher nahi, balki Bhagwan ka roop samajhna chahiye.”

Uske baad Krishna ne Grihastha jeevan samjhaya.

Unhone kaha, “Ek householder ko imaandari se kamaana chahiye, parivaar ka dhyaan rakhna chahiye aur dusron ki madad karni chahiye.”

Lekin Krishna ne ek important baat bhi kahi.

“Parivaar se prem karo, lekin itna attached mat ho jao ki Bhagwan ko bhool jao.”

Unhone samjhaya ki duniya ke rishte safar mein mile musafiron jaise hote hain. Kuch samay saath rehte hain, phir alag ho jaate hain.

Bhagwan bole, “Jo vyakti ghar mein rehkar bhi mann se shaant aur detached rehta hai, wahi sach mein azaad hai.”

Krishna ne bataya ki insaan ko paisa aur sukh ke peeche andha nahi banna chahiye. Zyada moh aur chinta insaan ko dukhi kar dete hain.

Ant mein Bhagwan ne kaha, “Chahe student ho, householder ho ya sanyasi — agar koi apne kartavya bhakti aur sachchai se karta hai, toh woh dheere-dheere mujhe paa leta hai.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 18
    with st.expander("Chapter 18 - Duties of Hermits (Vānaprastha) and Sannyāsins"):
        text1 = """ 
        Chapter 18 – Vanaprastha aur Sanyasi ka Jeevan

Bhagwan Krishna ne Uddhava se kaha, “Jab insaan dheere-dheere budhape ki taraf badhta hai, toh use duniya ke moh ko kam karke Bhagwan ki taraf mann lagana chahiye.”

Unhone bataya ki Vanaprastha jeevan mein vyakti ghar ki zimmedari apne bachchon ko dekar shaant aur simple jeevan jeeta hai.

Woh jungle ya shaant jagah mein rehkar phal, jad aur prakriti ki simple cheezon se jeevan chalata hai. Dheere-dheere uska mann duniya se alag hone lagta hai."""
        create_image_text_layout(
            "attached_assets/chapter11/11.18.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Krishna ne kaha, “Vanaprasthi ko tapasya, self-control aur dhyaan se apne mann ko pavitra banana chahiye.”

Lekin Bhagwan ne ek important baat bhi samjhayi.

“Bahut kathin tapasya sirf dikhawa ya chhoti ichchhaon ke liye karna moorkhta hai. Asli lakshya Bhagwan ko paana hai.”

Phir Krishna ne Sanyasi ke jeevan ke baare mein bataya.

Unhone kaha, “Jab insaan ke mann mein sachcha vairagya aa jaye aur duniya ke sukh bekaar lagne lage, tab woh sanyas le sakta hai.”

Ek sanyasi ko bahut simple jeevan jeena chahiye. Zyada samaan, paisa ya comfort nahi rakhna chahiye.

Woh sirf zarurat bhar ka khaana aur kapde rakhe aur bina ahankaar ke jeevan bitaye.

Bhagwan bole, “Sachcha sanyasi wahi hai jo mann aur indriyon ko control kare. Sirf sanyasi ke kapde pehen lene se koi mahaan nahi ban jaata.”

Krishna ne samjhaya ki sanyasi ko sab logon ko ek samaan dekhna chahiye. Kisi se dushmani ya gussa nahi rakhna chahiye.

Unhone kaha, “Yeh duniya aur shareer ek sapne ki tarah hain. Isliye inmein zyada moh nahi rakhna chahiye.”

Bhagwan ne bataya ki jo vyakti sachche guru ki seva karta hai aur bhakti ke saath gyaan seekhta hai, woh dheere-dheere Bhagwan ko mehsoos karne lagta hai.

Krishna bole, “Har ashram ka apna dharm hai — student ka guru seva, householder ka parivaar aur samaj ki raksha, vanaprasthi ka tapasya aur sanyasi ka self-control.”

Lekin sabke liye ek cheez sabse important hai — Bhagwan ki bhakti.

Ant mein Bhagwan ne kaha, “Jo vyakti apne kartavya imaandari aur bhakti se karta hai aur har jeev mein mujhe dekhta hai, woh jaldi hi mujhe paa leta hai.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 19
    with st.expander("Chapter 19 - Exposition of Spiritual Knowledge"):
        text1 = """ 
        Krishna ne kaha, “Vanaprasthi ko tapasya, self-control aur dhyaan se apne mann ko pavitra banana chahiye.”

Lekin Bhagwan ne ek important baat bhi samjhayi.

“Bahut kathin tapasya sirf dikhawa ya chhoti ichchhaon ke liye karna moorkhta hai. Asli lakshya Bhagwan ko paana hai.”

Phir Krishna ne Sanyasi ke jeevan ke baare mein bataya.

Unhone kaha, “Jab insaan ke mann mein sachcha vairagya aa jaye aur duniya ke sukh bekaar lagne lage, tab woh sanyas le sakta hai.”

Ek sanyasi ko bahut simple jeevan jeena chahiye. Zyada samaan, paisa ya comfort nahi rakhna chahiye.

Woh sirf zarurat bhar ka khaana aur kapde rakhe aur bina ahankaar ke jeevan bitaye.

Bhagwan bole, “Sachcha sanyasi wahi hai jo mann aur indriyon ko control kare. Sirf sanyasi ke kapde pehen lene se koi mahaan nahi ban jaata.”

Krishna ne samjhaya ki sanyasi ko sab logon ko ek samaan dekhna chahiye. Kisi se dushmani ya gussa nahi rakhna chahiye.

Unhone kaha, “Yeh duniya aur shareer ek sapne ki tarah hain. Isliye inmein zyada moh nahi rakhna chahiye.”

Bhagwan ne bataya ki jo vyakti sachche guru ki seva karta hai aur bhakti ke saath gyaan seekhta hai, woh dheere-dheere Bhagwan ko mehsoos karne lagta hai.

Krishna bole, “Har ashram ka apna dharm hai — student ka guru seva, householder ka parivaar aur samaj ki raksha, vanaprasthi ka tapasya aur sanyasi ka self-control.”

Lekin sabke liye ek cheez sabse important hai — Bhagwan ki bhakti.

Ant mein Bhagwan ne kaha, “Jo vyakti apne kartavya imaandari aur bhakti se karta hai aur har jeev mein mujhe dekhta hai, woh jaldi hi mujhe paa leta hai.”"""
        create_image_text_layout(
            "attached_assets/chapter11/11.19.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Uddhava ne vinamrata se kaha, “Hey Prabhu, sansar ke dukh bahut bade hain. Aap hi meri raksha kar sakte hain. Kripya mujhe bhakti aur gyaan ka sahi raasta samjhaiye.”

Tab Krishna ne Bhishma Pitamah ki seekh yaad dilayi.

Unhone kaha, “Asli gyaan yeh hai ki har jeev aur har cheez mein ek hi Parmatma ko dekha jaye.”

Jo vyakti har jagah ek hi Atma ko mehsoos karta hai, uska darr aur moh dheere-dheere khatam ho jata hai.

Phir Bhagwan ne Bhakti ka simple raasta bataya.

“Prem se meri kahaniyan suno, mera naam lo, meri stuti karo, dusron ki seva karo aur har kaam mujhe samarpit karo.”

Krishna ne kaha, “Jab mann Bhagwan mein lagta hai, tab woh shaant aur pavitra ho jata hai. Lekin jab mann duniya ki ichchhaon mein phans jata hai, tab dukh badhne lagta hai.”

Uske baad Uddhava ne poocha, “Asli self-control aur achchai kya hoti hai?”

Bhagwan ne bahut simple jawab diya.

“Dusron ko dukh na dena, sach bolna, lalach se door rehna aur mann ko control karna hi asli dharm hai.”

Krishna bole, “Asli daan dusron ko suraksha aur daya dena hai. Asli bahaduri apni buri ichchhaon ko jeetna hai.”

Unhone kaha, “Jo har jagah ek hi Bhagwan ko dekhta hai, wahi sach mein gyani hai.”

Bhagwan ne samjhaya ki sirf bahar ka dikhawa important nahi hota. Asli pavitrata mann ki hoti hai.

Krishna bole, “Jiska mann indriyon ka gulaam hai, woh dukhi rehta hai. Lekin jo mann ko control kar leta hai, wahi sachcha swami hai.”

Ant mein Bhagwan ne kaha, “Achha aur bura samajhne ka sabse bada tareeka yeh hai — dusron ki kamiyaan dekhne ki aadat chhod do aur apna mann Bhagwan mein laga do.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 20
    with st.expander("Chapter 20 - Elucidation of Karma, Jñāna and Bhakti Yogas"):
        text1 = """ 
        Chapter 20 – Karma, Gyaan aur Bhakti ka Asli Arth

Uddhava ne Krishna se poocha, “Agar Vedas achhe aur bure karm bataate hain, toh phir aap kyun kehte hain ki achha-bura sochne mein hi ulajhna theek nahi?”

Bhagwan Krishna bole, “Logon ki alag-alag soch aur swabhav ke liye maine teen raaste bataye hain — Karma Yoga, Gyaan Yoga aur Bhakti Yoga.”

Unhone samjhaya:"""
        create_image_text_layout(
            "attached_assets/chapter11/11.20.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        “Jo duniya aur karmon se thak chuka hai, uske liye Gyaan ka raasta hai.
Jo abhi bhi ichchhaon mein laga hai, uske liye Karma ka raasta hai.
Aur jiske dil mein mere liye prem jag gaya hai, uske liye Bhakti ka raasta sabse sundar hai.”

Krishna ne kaha ki insaan ko apne kartavya karte rehna chahiye jab tak uske mann mein sachchi bhakti ya vairagya na aa jaye.

Bhagwan bole, “Yeh manushya janam bahut keemti hai. Swarg ke devta bhi is janam ko paana chahte hain, kyunki isi jeevan mein moksha mil sakta hai.”

Unhone ek sundar misaal di.

“Yeh shareer ek nauka ki tarah hai. Guru uska maajhi hai aur Bhagwan ki kripa hawa ki tarah madad karti hai. Jo insaan is mauke ka use nahi karta, woh apne aap ko nuksan pahunchata hai.”

Krishna ne samjhaya ki mann bahut chanchal hota hai. Kabhi-kabhi dhyaan karte waqt bhi woh duniya ki taraf bhaagta hai.

Lekin yogi ko himmat nahi harni chahiye. Dheere-dheere pyaar aur practice se mann ko wapas Bhagwan ki taraf lana chahiye.

Bhagwan bole, “Jaise ghode ko pyaar aur control se sambhala jaata hai, waise hi mann ko bhi sambhalna chahiye.”

Unhone kaha ki jab insaan Bhagwan ki bhakti karta rehta hai, toh uske mann ki buri ichchhaayein dheere-dheere khatam hone lagti hain.

Krishna ne bataya, “Jab Bhagwan dil mein mehsoos hone lagte hain, tab saare doubts toot jaate hain aur purane karmon ka bandhan bhi khatam ho jata hai.”

Phir Bhagwan ne ek bahut pyari baat kahi.

“Sachche bhakt ko na swarg chahiye, na shakti aur na hi moksha. Use sirf Bhagwan ka prem chahiye.”

Krishna bole, “Jo kuch bhi karma, tapasya, gyaan ya yoga se milta hai, woh sab ek sachcha bhakt aasani se pa leta hai.”

Ant mein Bhagwan ne kaha, “Sabse bada raasta desireless bhakti ka hai. Jo bina kisi lalach ke mujhe prem karta hai, wahi sachchi shanti aur moksha paata hai.” """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 21
    with st.expander("Chapter 21 - Criteria for determining the good and the evil"):
        text1 = """ 
        Chapter 21 – Achha aur Bura Samajhne ki Seekh

Bhagwan Krishna ne Uddhava se kaha, “Jo log bhakti, gyaan aur bina swarth wale karm ka raasta chhod dete hain aur sirf chhote sukh ke peeche bhaagte hain, woh janam-maran ke chakkar mein phanse rehte hain.”

Unhone samjhaya ki har insaan ko apna dharm aur kartavya imaandari se nibhana chahiye. Apna sahi kaam karna hi achchai hai, aur galat raaste par chalna burai hai.

Krishna bole, “Kabhi-kabhi ek hi cheez kisi ke liye achhi hoti hai aur kisi aur ke liye buri. Yeh sab samay, jagah aur paristhiti par depend karta hai.” """
        create_image_text_layout(
            "attached_assets/chapter11/11.21.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Bhagwan ne kaha ki duniya mein niyam isliye banaye gaye hain taaki log sahi aur galat ka farq samajh sakein.

Unhone samjhaya ki sabhi jeev ek hi Parmatma se bane hain. Phir bhi har vyakti ka kaam aur zimmedari alag hoti hai.

Krishna bole, “Insaan jab kisi cheez mein zyada sukh dekhne lagta hai, tab usmein moh paida hota hai.”

Moh se ichchha paida hoti hai. Ichchha se jhagda aur gussa badhta hai. Aur gusse se buddhi dheere-dheere khatam hone lagti hai.

Bhagwan ne kaha, “Jiska mann duniya ki ichchhaon mein phans jata hai, woh apne asli swaroop ko bhool jata hai.”

Unhone ek simple example diya.

“Jaise bachche ko dawa dene ke liye pehle mithai ka lalach diya jaata hai, waise hi Vedo mein bhi kabhi-kabhi swarg aur sukh ki baat karke logon ko dharm ki taraf laaya jaata hai.”

Lekin Krishna ne samjhaya ki asli lakshya sirf swarg ya sukh nahi, balki moksha aur Bhagwan ko paana hai.

Bhagwan bole, “Jo log sirf bhog aur sukh ke peeche bhaagte hain, woh sachchai ko samajh nahi paate.”

Unhone kaha ki kuch log Vedo ka galat matlab samajhkar bina wajah jaanwaron ko dukh dete hain aur sirf apni ichchha poori karna chahte hain.

Krishna ne saaf kaha, “Asli gyaan wahi hai jo insaan ko daya, self-control aur bhakti ki taraf le jaaye.”

Phir Bhagwan ne Vedo ki mahima batayi.

“Vedo ka asli arth bahut gehra hai. Unka antim sandesh yeh hai ki sab jagah ek hi Parmatma hai.”

Krishna bole, “Main hi Vedo ka saar hoon. Shuru mein Vedas duniya ki alag-alag cheezein samjhate hain, lekin ant mein sabko ek hi sachchai tak le jaate hain — Bhagwan.”

Ant mein Bhagwan ne kaha, “Jo vyakti moh aur lalach chhodkar bhakti aur sachchai ka raasta chunta hai, wahi asli shanti aur mukti paata hai.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 22
    with st.expander("Chapter 22 - Enumeration of Principles (Tattvas)"):
        text1 = """ 
        Chapter 22 – Prakriti aur Atma ka Rahasya

Uddhava ne Krishna se poocha, “Hey Prabhu, alag-alag rishi tattvon ki alag sankhya kyun batate hain? Koi 25 kehta hai, koi 26 aur koi aur sankhya.”

Bhagwan Krishna muskuraaye aur bole, “Sab apni samajh aur drishti ke hisaab se baat karte hain. Isliye alag-alag ginti sahi ho sakti hai.”

Unhone samjhaya ki duniya mein jo bhi dikh raha hai, woh Prakriti aur Purush se bana hai.

Prakriti matlab prakritik duniya — shareer, mann aur indriyaan.
Purush matlab Atma — jo sab dekhne wala aur hamesha amar hai."""
        create_image_text_layout(
            "attached_assets/chapter11/11.22.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Krishna bole, “Atma kabhi badalti nahi. Lekin shareer har samay badalta rehta hai.”

Unhone kaha ki Maya aur teen gun — Sattva, Rajas aur Tamas — insaan ko uljha dete hain.

Inhi ke kaaran log alag-alag soch aur jhagde mein phans jaate hain.

Bhagwan ne samjhaya, “Jab mann shaant ho jaata hai aur indriyaan control mein aa jaati hain, tab jhagda aur confusion khatam ho jaata hai.”

Phir Krishna ne tattvon ko simple tareeke se bataya.

Paanch mahabhoot — dharti, jal, agni, hawa aur aakash.
Phir mann, buddhi, ahankaar aur indriyaan.

Yeh sab milkar shareer aur sansar banate hain.

Lekin Atma in sabse alag hai.

Krishna bole, “Atma sirf dekhne wali hai. Woh kabhi janam nahi leti aur kabhi marti nahi.”

Uddhava ne phir poocha, “Agar Atma aur shareer alag hain, toh log dono ko ek kyun samajhte hain?”

Bhagwan ne jawab diya, “Maya ke kaaran insaan shareer ko hi apna asli roop maan leta hai.”

Unhone ek example diya.

“Jaise sapne mein insaan khud ko alag roop mein dekhता hai aur sapna sach lagta hai, waise hi sansar bhi Maya ki wajah se sach jaisa lagta hai.”

Krishna bole, “Janam aur mrityu shareer ke hote hain, Atma ke nahi.”

Shareer bachpan, jawaani aur budhape se guzarta hai. Lekin Atma hamesha waise hi rehti hai.

Bhagwan ne kaha, “Jo vyakti shareer aur duniya se bahut moh kar leta hai, woh baar-baar janam leta rehta hai.”

Achhe karm aur Sattva gun se upar ki yoni milti hai. Rajas aur Tamas se dukh aur neeche ki yoniyan milti hain.

Krishna ne samjhaya ki Atma asal mein azaad hai. Lekin ahankaar aur moh ki wajah se woh khud ko bandh hua samajhne lagti hai.

Phir Bhagwan ne ek gehri baat kahi.

“Jaise behte paani ke paas khade ped humein hilte hue lagte hain, waise hi Atma bhi shareer ke saath judi hui lagti hai. Lekin asal mein Atma kabhi nahi badalti.”

Krishna bole, “Sansar ka sukh aur dukh sapne ki tarah hai. Jab tak mann unmein phansa rahega, tab tak insaan dukhi rahega.”

Isliye Bhagwan ne Uddhava ko salah di,

“Indriyon ke peeche mat bhaago. Apne mann ko sachchai aur bhakti mein lagao.”

Ant mein Krishna ne kaha, “Jo vyakti apne mann ko control karke Bhagwan ki sharan leta hai, wahi Maya aur sansar ke dukh se bahar nikal paata hai.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 23
    with st.expander("Chapter 23 - The Song of a Recluse (Bhikṣu Gītā)"):
        text1 = """ 
        Chapter 23 – Bhikshu Gita ki Gehri Seekh

Shukdev ji ne kaha, “Jab Uddhava ne Krishna se mann ko shaant rakhne ka raasta poocha, tab Bhagwan ne ek purani kahani sunayi.”

Krishna bole, “Kathor shabdon ka dard kabhi-kabhi teer ke ghaav se bhi zyada hota hai.”

Phir unhone Avanti nagar ke ek Brahman ki kahani batayi.

Woh Brahman bahut ameer tha, lekin bahut kanjoos aur gusse wala bhi tha. Woh apne parivaar, mehmaan aur sevakon tak ka dhyaan nahi rakhta tha.

Uska mann sirf dhan jama karne mein laga rehta tha.

Dheere-dheere uske apne hi log usse nafrat karne lage."""
        create_image_text_layout(
            "attached_assets/chapter11/11.23.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Phir ek din uska saara dhan chala gaya. Kuch rishtedaron ne le liya, kuch chor chura le gaye aur kuch samay ke saath khatam ho gaya.

Brahman bahut dukhi ho gaya.

Woh sochne laga, “Maine poori zindagi dhan ke liye mehnat ki, lekin na mujhe sukh mila aur na dharm.”

Usne samjha ki dhan ke saath darr, jhagda aur dukh bhi aate hain.

Krishna ne bataya ki lalach se kai buraiyaan paida hoti hain — jhooth, gussa, dushmani, ahankaar aur dhokha.

Brahman ne socha, “Ab jo zindagi bachi hai, use Bhagwan aur tapasya mein lagaunga.”

Usne sab kuch chhod diya aur ek shaant sanyasi ban gaya.

Woh gaon-gaon bhiksha maangkar jeene laga.

Lekin log uska mazaak udaate the. Kuch uski cheezein chheen lete, kuch use gaali dete aur kuch us par thook dete.

Kayi log use maarte aur pareshaan karte the.

Phir bhi woh shaant raha.

Woh samajh chuka tha ki asli dukh ka kaaran baahar ke log nahi, balki apna mann hai.

Tab us Brahman ne ek gehri baat kahi:

“Na log, na devta, na samay aur na hi kismat — sukh aur dukh ka asli kaaran sirf mann hai.”

Usne samjhaya ki mann hi moh, gussa aur dukh paida karta hai.

Agar mann control mein ho, toh insaan mushkilon mein bhi shaant reh sakta hai.

Brahman bola, “Jo apne mann ko jeet leta hai, wahi sabse bada vijeta hai.”

Usne kaha, “Hum dusron ko dushman samajhte hain, lekin asal mein hum apne mann ke hi gulaam hote hain.”

Krishna ne Uddhava se kaha, “Isliye mann ko Bhagwan mein lagao aur use control karna seekho. Yahi Yoga ka saar hai.”

Ant mein Bhagwan bole, “Jo vyakti is Bhikshu Gita ko samajhta aur yaad rakhta hai, woh sukh aur dukh dono mein shaant rehna seekh jaata hai.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 24
    with st.expander("Chapter 24 - Elucidation of Sāṃkhya Yoga"):
        text1 = """ 
        Chapter 24 – Sankhya Yoga ka Gyaan

Bhagwan Krishna ne Uddhava se kaha, “Ab main tumhe Sankhya Yoga ka sachcha gyaan samjhaunga. Isse insaan moh aur bhram se bahar aa sakta hai.”

Krishna bole, “Shuru mein sirf ek hi sachchai thi — Brahman. Na alag duniya thi aur na alag jeev.”

Phir Maya ke kaaran sab alag-alag dikhne laga.

Bhagwan ne samjhaya ki do mukhya tattva hain — Prakriti aur Purush.

Prakriti matlab poori material duniya — shareer, mann aur prakritik cheezein.
Purush matlab Atma — jo hamesha dekhne wali aur amar hai."""
        create_image_text_layout(
            "attached_assets/chapter11/11.24.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Krishna bole, “Prakriti se teen gun paida hote hain — Sattva, Rajas aur Tamas.”

Sattva shanti aur gyaan deta hai.
Rajas ichchha aur kaam karne ki shakti deta hai.
Tamas andhkaar aur alasya laata hai.

Inhi teen gunon se poora sansar chalta hai.

Bhagwan ne bataya ki pehle Mahat tattva paida hua, phir Ahankaar aur uske baad indriyaan aur paanch mahabhoot — aakash, hawa, agni, jal aur prithvi.

Yeh sab milkar poori srishti banaate hain.

Krishna bole, “Meri shakti se yeh sab tattva milkar brahmand ka nirmaan karte hain.”

Phir unhone bataya ki Brahma ji ka janm kaise hua.

“Cosmic jal mein main Narayan roop mein tha. Mere nabhi se ek kamal nikla aur us kamal se Brahma ji prakat hue.”

Brahma ji ne phir devta, lok aur praja ka nirmaan kiya.

Bhagwan ne samjhaya ki alag-alag lok bhi hain — Swarg lok, Prithvi lok aur neeche ke lok.

Lekin unhone ek khaas baat kahi:

“Jo bhakti ka raasta chunta hai, uska antim ghar Vaikunth hota hai.”

Krishna ne phir sansar ke ant ka rahasya bataya.

Jab pralaya aata hai, tab dheere-dheere sab kuch wapas apne mool tattvon mein milne lagta hai.

Prithvi jal mein, jal agni mein, agni hawa mein aur hawa aakash mein sama jaati hai.

Aakhir mein sab kuch Prakriti aur phir Brahman mein vilin ho jaata hai.

Bhagwan bole, “Jo vyakti samajh leta hai ki Atma alag hai aur duniya sirf badalne wali Maya hai, uska bhram toot jaata hai.”

Unhone ek simple example diya.

“Jaise Suraj nikalte hi andhera khatam ho jaata hai, waise hi sachcha gyaan aate hi moh aur confusion khatam ho jaata hai.”

Ant mein Krishna ne kaha,

“Sankhya Yoga ka asli uddeshya yeh samajhna hai ki Atma amar hai aur Bhagwan hi sabka antim sach hain.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 25
    with st.expander("Chapter 25 - The Three Guṇas and Their Workings"):
        text1 = """ 
        Chapter 25 – Teen Gunon ka Rahasya

Bhagwan Krishna ne Uddhava se kaha, “Ab main tumhe teen gunon — Sattva, Rajas aur Tamas — ke baare mein samjhaunga. Yeh teenon hi insaan ke sochne aur jeene ka tareeka badalte hain.”

Sattva Guna – Shanti aur Gyaan

Krishna bole, “Sattva guna mann ko shaant aur pavitra banata hai.”

Isse insaan mein daya, sachchai, patience, self-control aur santosh aata hai.

Aisa vyakti dusron ki madad karta hai aur galat kaam se door rehta hai.

Uska mann Bhagwan aur sachchai ki taraf jaata hai."""
        create_image_text_layout(
            "attached_assets/chapter11/11.25.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
Rajas Guna – Ichchha aur Bechaini

Bhagwan ne kaha, “Rajas guna insaan ko hamesha kuch paane ki ichchha deta hai.”

Isse lalach, ahankaar, competition aur zyada kaam karne ki aadat badhti hai.

Aisa vyakti fame, paisa aur sukh ke peeche bhaagta rehta hai.

Uska mann kabhi shaant nahi rehta.

Tamas Guna – Andhkaar aur Aalas

Krishna bole, “Tamas guna mann ko andhera aur sust bana deta hai.”

Isse gussa, jhooth, alasya, confusion aur dukh badhte hain.

Aisa vyakti sahi aur galat ka farq samajhne mein mushkil mehsoos karta hai.

Teenon Gun Sab Mein Hain

Bhagwan ne samjhaya ki har insaan mein yeh teenon gun hote hain, bas kisi mein ek zyada hota hai aur kisi mein doosra.

Jab Sattva badhta hai, toh insaan shaant aur gyaani banta hai.
Jab Rajas badhta hai, toh mann restless ho jaata hai.
Aur jab Tamas badhta hai, toh alasya aur andhkaar badhne lagta hai.

Mann ki Pehchaan

Krishna ne kaha,

“Agar mann shaant ho, indriyaan control mein ho aur darr kam ho, toh samajh lo Sattva guna badh raha hai.”

“Agar mann hamesha bechain rahe aur ichchhaon mein uljha ho, toh Rajas ka prabhav hai.”

“Agar mann udaas, sust aur confused rahe, toh Tamas ka asar hai.”

Bhakti Sabse Upar Hai

Bhagwan ne ek bahut gehri baat kahi.

“Jo vyakti bina kisi swarth ke sirf meri bhakti karta hai, woh teenon gunon se upar uth jaata hai.”

Unhone bataya ki khaana, jagah, kaam, soch aur vishwas — sab par gunon ka asar hota hai.

Achha aur pavitra bhojan Sattvik hota hai.
Bahut teekha aur sirf taste ke liye khaaya gaya bhojan Rajasic hota hai.
Ganda aur unhealthy bhojan Tamasic hota hai.

Mukti ka Raasta

Krishna bole, “Insaan ko pehle Sattva guna badhana chahiye. Phir dheere-dheere teenon gunon se upar uthkar Bhagwan mein mann lagana chahiye.”

Unhone Uddhava se kaha,

“Yeh manushya janm bahut keemti hai. Iska use gyaan, bhakti aur self-control ke liye karo.”

Ant mein Bhagwan ne kaha,

“Jo vyakti indriyon ko control karke bhakti mein sthir ho jaata hai, woh janam-maran aur Maya ke bandhan se azaad ho jaata hai.” """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 26
    with st.expander("Chapter 26 - The Song of Aila (Purūravas)"):
        text1 = """ 
Chapter 26 – Raja Pururava ki Seekh

Bhagwan Krishna ne Uddhava se kaha, “Jo vyakti bhakti ka raasta pakadta hai aur mujhe apne mann mein paata hai, woh dheere-dheere Maya aur moh se azaad ho jaata hai.”

Phir Krishna ne Raja Pururava ki kahani sunayi.

Pururava ek bahut mahaan aur shaktishaali raja tha. Lekin woh apsara Urvashi ke prem mein itna doob gaya ki apne aap ko hi bhool baitha.

Jab Urvashi usse chhodkar chali gayi, tab Pururava pagal ki tarah uske peeche bhaagne laga.”"""
        create_image_text_layout(
            "attached_assets/chapter11/11.26.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Woh rota hua kehta, “Ruko Urvashi, mujhe chhodkar mat jao!”

Prem aur moh mein doobe hone ke kaaran use samay ka bhi pata nahi chala. Kai saal beet gaye, lekin uska mann kabhi shaant nahi hua.

Phir ek din usse apni galti samajh aayi.

Pururava bola, “Mera moh kitna bada tha! Main poori duniya ka raja hote hue bhi ek prem ke jaal mein phans gaya.”

Usne samjha ki vasna aur moh insaan ki buddhi ko andha bana dete hain.

Woh bola, “Meri shakti, mera rajya aur mera gyaan sab bekaar ho gaya, kyunki main apne mann ko control nahi kar paaya.”

Pururava ne apni galti ka dosh Urvashi ko nahi diya.

Usne kaha, “Galti meri hi thi. Maine apni indriyon ko sambhala nahi.”

Krishna ne samjhaya ki shareer dekhne mein sundar lag sakta hai, lekin asal mein woh sirf maans, haddiyan aur khoon se bana hai.

Moh aur Maya hi use khoobsurat dikhate hain.

Bhagwan ne kaha, “Jo vyakti sirf shareer aur sukh ke peeche bhaagta hai, woh kabhi asli shanti nahi paa sakta.”

Pururava ko dheere-dheere samajh aa gaya ki sansarik sukh kabhi mann ko poori tarah santusht nahi karte.

Tab usne duniya ke moh ko chhod diya aur Bhagwan ki taraf mann laga diya.

Krishna ne Uddhava ko ek bahut zaroori baat samjhayi:

“Buri sangat insaan ko andhkaar ki taraf le jaati hai. Isliye hamesha achhe aur sant logon ka saath karna chahiye.”

Bhagwan bole, “Sant log hi insaan ko sansar ke dukh aur moh se bahar nikaalte hain.”

Unhone santon ki tareef karte hue kaha,

“Jaise doobte hue vyakti ko naav bachati hai, waise hi sant insaan ko sansar ke samundar se paar kara dete hain.”

Ant mein Krishna ne kaha,

“Jo vyakti bhakti, satsang aur self-control ka raasta chunta hai, woh dheere-dheere mann ki shanti aur Bhagwan ka sachcha anand pa leta hai.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 27
    with st.expander("Chapter 27 - The Yoga of Active Service"):
        text1 = """ 
        Chapter 27 – Bhagwan ki Seva aur Bhakti ka Yoga

Uddhava ne Krishna se poocha, “Hey Prabhu, log aapki pooja kaise karein? Kaunsi bhakti aur seva se insaan moksha paa sakta hai?”

Bhagwan Krishna bole, “Meri pooja ke bahut saare tareeke hain. Main tumhe simple roop mein samjhata hoon.”

Unhone kaha ki bhakti teen tareekon se ki ja sakti hai — Vedic, Tantric aur dono ka mila hua roop.

Krishna bole, “Sabse zaroori cheez hai shraddha aur sachcha mann.”

Bhagwan Har Jagah Hain"""
        create_image_text_layout(
            "attached_assets/chapter11/11.27.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Krishna ne samjhaya ki unki pooja sirf murti mein hi nahi hoti.

Insaan Bhagwan ko agni, Suraj, jal, hriday aur pavitra Brahman mein bhi dekh sakta hai.

Woh bole, “Jo bhi bhakti aur prem se mujhe yaad karta hai, main uske paas hota hoon.”

Pooja se Pehle Shuddhi

Bhagwan ne bataya ki pooja se pehle sharir aur mann dono ko saaf rakhna chahiye.

Snan, prarthana aur shaant mann ke saath pooja karni chahiye.

Unhone kaha ki murti alag-alag cheezon ki ho sakti hai — pathar, lakdi, mitti, chandan ya mann mein sochi hui roop mein bhi.

Bhakti Mein Prem Sabse Zaroori

Krishna bole, “Agar koi bhakt sirf ek boond paani bhi prem se chadhaaye, toh mujhe bahut khushi hoti hai.”

Lekin bina bhakti ke diye gaye bade-bade uphaar mujhe khush nahi karte.

Unhone phool, chandan, dhoop, deepak aur bhojan chadhaane ki baat bhi samjhayi.

Dhyaan aur Mantra

Bhagwan ne kaha ki pooja ke waqt mann ko un par lagaana chahiye.

Bhakt ko unka sundar roop yaad karna chahiye — shankh, chakra, gada aur kamal dharan kiye hue.

Krishna bole, “Mann se ki hui pooja bhi utni hi mahatvapurn hai jitni baahar ki pooja.”

Bhajan aur Katha

Bhagwan ne kaha,

“Meri pooja ke baad mere gun gaao, meri kathayein suno aur khushi se bhajan karo.”

Dance, music aur Bhagwan ki leelaon ka smaran bhi bhakti ka hissa hai.

Sachchi Prarthana

Krishna ne ek gehri prarthana batayi:

“Hey Prabhu, main sansar ke dukh aur darr se ghabraya hua hoon. Mujhe apni sharan mein rakhiye.”

Mandir aur Seva ka Mahatva

Bhagwan ne kaha ki jo log mandir banaate hain, pooja aur seva ka intezaam karte hain, woh bahut punya paate hain.

Lekin jo log Bhagwan ya Brahman ke liye di hui cheez churaate hain, woh paap ke bhaagi bante hain.

Bhakti ka Asli Phal

Ant mein Krishna ne Uddhava se kaha,

“Jo vyakti bina swarth ke prem aur shraddha se meri seva karta hai, woh dheere-dheere mere paas aa jaata hai.”

Bhagwan bole,

“Sachchi bhakti sirf pooja nahi, balki prem, shraddha aur mann ki pavitrata hai.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 28
    with st.expander("Chapter 28 - The Essence of the Path of Knowledge (Jñāna Yoga)"):
        text1 = """ 
        Chapter 28 – Gyaan Yoga ka Saar

Bhagwan Krishna ne Uddhava se kaha, “Jo vyakti sachcha gyaan pa leta hai, woh duniya mein kisi ki burai ya zyada tareef nahi karta.”

Krishna bole, “Yeh poora sansar Prakriti aur Atma ka khel hai. Isliye samajhdaar vyakti sab mein ek hi Parmatma ko dekhta hai.”

Duniya ek Sapne Jaisi Hai

Bhagwan ne samjhaya ki duniya ki bahut si cheezein asli lagti hain, lekin waise hi hain jaise sapne ya mirage.

Jaise sapne mein dukh aur khushi sach lagte hain, waise hi Maya insaan ko sansar mein uljha deti hai.

Krishna bole, “Jo vyakti sirf baahari farq dekhta hai, woh andhkaar mein phans jaata hai.”"""
        create_image_text_layout(
            "attached_assets/chapter11/11.28.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Atma aur Shareer Alag Hain

Uddhava ne poocha, “Agar Atma alag hai aur shareer alag, toh dukh aur janam-maran kis ko hota hai?”

Bhagwan ne jawab diya,

“Atma kabhi janam nahi leti aur kabhi marti nahi. Janam aur mrityu shareer aur ahankaar se jude hote hain.”

Unhone samjhaya ki jab Atma mann, indriyon aur shareer ko hi apna roop maan leti hai, tab sansar ka dukh shuru hota hai.

Ahankaar hi Bandhan Hai

Krishna bole, “Dukh, gussa, darr, lalach aur moh — yeh sab ahankaar se paida hote hain, Atma se nahi.”

Atma toh hamesha shuddh aur prakash roop hai.

Sona aur Gehno ka Example

Bhagwan ne ek simple example diya.

“Jaise sona alag-alag gehno mein badal jaata hai, lekin asal mein sona hi rehta hai, waise hi poora sansar Bhagwan ka hi roop hai.”

Naam aur roop alag lagte hain, lekin sachchai ek hi hai.

Gyaan ki Talwar

Krishna ne kaha, “Insaan ko gyaan ki talwar se moh aur bhram ko kaat dena chahiye.”

Jab sachcha gyaan aa jaata hai, tab insaan samajh leta hai ki duniya ki zyada cheezein temporary hain.

Sachcha Gyani Kaise Hota Hai

Bhagwan bole, “Jo vyakti sachchai ko jaan leta hai, woh duniya mein rehte hue bhi usmein phasta nahi.”

Woh sukh aur dukh dono mein shaant rehta hai.

Maya ka Asar

Krishna ne samjhaya ki jab tak mann mein ichchha aur vasna rehti hai, tab tak Maya ka asar bana rehta hai.

Isliye bhakti aur mann ka control bahut zaroori hai.

Yog aur Sharir

Bhagwan ne kaha ki kuch log sirf sharir ko strong aur young banane mein lage rehte hain.

Lekin shareer ek din khatam ho hi jaata hai.

Isliye samajhdaar vyakti shareer se zyada Atma aur Bhagwan par dhyaan deta hai.

Antim Seekh

Krishna ne Uddhava se kaha,

“Jo vyakti bhakti, gyaan aur self-control ke saath jeevan jeeta hai, woh Maya ke bandhan se azaad ho jaata hai.”

Aur jo apna mann Bhagwan mein laga deta hai, woh asli shanti aur anand pa leta hai।"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 29
    with st.expander("Chapter 29 - Bhakti Yoga Recapitulated: Departure of Uddhava to Badarikāśrama"):
        text1 = """ 
        Chapter 29 – Uddhava ki Vidai aur Bhakti ka Saar

Uddhava ne Krishna se kaha, “Hey Prabhu, mann ko control karna bahut mushkil hai. Aam logon ke liye koi simple raasta batayiye jisse woh aasani se aap tak pahunch sakein.”

Bhagwan Krishna muskuraaye aur pyaar se bole, “Main tumhe sabse achha aur simple raasta batata hoon — Bhakti.”

Har Kaam Bhagwan ko Samarpit Karo

Krishna ne kaha,

“Jo bhi kaam karo, mujhe yaad karke karo. Apne mann aur dil ko mujhme lagao.”"""
        create_image_text_layout(
            "attached_assets/chapter11/11.29.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Unhone samjhaya ki bhakti sirf mandir tak simit nahi hai.

Bhagwan bole, “Mere bhakton ke saath raho, pavitra jagahon par jao aur milkar bhajan, utsav aur kirtan karo.”

Sab Mein Bhagwan Ko Dekho

Krishna ne ek bahut gehri baat kahi.

“Har jeev mein mujhe dekho — chahe woh achha ho ya bura, ameer ho ya gareeb.”

Jo vyakti sabko samaan nazar se dekhta hai, wahi sachcha gyani hai.

Bhagwan bole, “Jab insaan sab mein mujhe dekhne lagta hai, tab uska gussa, jalan aur ahankaar dheere-dheere khatam ho jaata hai.”

Namrata aur Prem

Krishna ne kaha ki insaan ko itna vinamra banna chahiye ki woh har jeev ka samman kare — chahe woh janwar ho ya koi gareeb vyakti.

Unhone kaha, “Mann, vaani aur karm — teeno se meri bhakti karo.”

Bhakti Sabse Aasaan Raasta

Bhagwan bole, “Mere paas pahunchne ke bahut raaste hain, lekin sabse asaan aur shaktishaali raasta hai sab mein Bhagwan ko dekhna.”

Unhone samjhaya ki bhakti mein ki gayi chhoti si mehnat bhi kabhi bekaar nahi jaati.

Krishna ka Vachan

Krishna ne kaha,

“Jo vyakti mera gyaan doosre bhakton ko samjhata hai, main khud uspar kripa karta hoon.”

Aur jo shraddha se is gyaan ko sunta hai, woh karmon ke bandhan se dheere-dheere azaad ho jaata hai.

Uddhava ka Moh Toot Gaya

Krishna ki baatein sunkar Uddhava ki aankhon mein aansu aa gaye.

Woh bole, “Prabhu, aapne mere mann ka andhkaar mita diya. Ab mera moh aur dukh khatam ho gaya.”

Uddhava ne Krishna ke charanon mein sir jhuka diya.

Badarikashram Jaane ka Aadesh

Tab Krishna ne kaha,

“Hey Uddhava, ab tum Badarikashram jao. Wahan tapasya aur dhyaan karo.”

Unhone kaha ki Uddhava pavitra Ganga aur Alaknanda ke jal se apne mann ko aur pavitra kare.

Krishna bole, “Simple jeevan jeeyo, indriyon ko control mein rakho aur jo gyaan maine diya hai uspar hamesha manan karo.”

Bhavuk Vidai

Yeh sunkar Uddhava bahut bhavuk ho gaya.

Woh Krishna se door nahi jaana chahta tha. Aankhon mein aansu lekar usne baar-baar Krishna ko pranam kiya.

Krishna ne apni khadaun Uddhava ko di. Uddhava ne unhe apne sir par rakha aur bhaari mann se Badarikashram ki taraf chal diya.

Wahan pahunchkar usne Krishna ke bataye hue bhakti aur gyaan ke raaste par jeevan bitaya.

Ant mein Uddhava ne Bhagwan ko hi apna sab kuch maan kar unka divya dhaam prapt kar liya."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 30
    with st.expander("Chapter 30 - Extermination of the Race of Yādavas"):
        text1 = """ 
        Chapter 30 – Yadavo ka Ant aur Krishna ka Prasthan

Raja Parikshit ne poocha, “Jab Uddhava Badarikashram chale gaye, tab Krishna ne Dwarka mein kya kiya? Aur Yadav vansh ka ant kaise hua?”

Shukdev ji ne kahani shuru ki.

Ashubh Sanket

Krishna ne Dwarka mein bahut bure sanket dekhe — aasman, dharti aur hawa sab ajeeb lag rahe the.

Tab Krishna ne Yadavo se kaha,"""
        create_image_text_layout(
            "attached_assets/chapter11/11.30.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        “Yeh achhe sanket nahi hain. Humein turant Dwarka chhod dena chahiye.”

Unhone mahilaon, bachchon aur buzurgon ko surakshit jagah bhej diya.

Baaki sab Prabhas teerth gaye, jahan unhone snan, daan aur pooja ki.

Vinash ki Shuruaat

Lekin kismat kuch aur hi thi.

Yadav yoddhaon ne ek bahut tez sharab pee li. Usse unka hosh aur samajh dono khatam ho gaye.

Dheere-dheere mazaak jhagdon mein badal gaya.

Phir bhayankar yudh shuru ho gaya.

Bhai bhai se ladne laga. Dost dost par hamla karne lage. Pita aur putra bhi ek doosre ke saamne aa gaye.

Krishna ki Maya ke kaaran sab apna hosh kho baithe the.

Eraka Ghaas ka Loha Ban Jana

Jab unke hathiyaar khatam ho gaye, tab unhone zameen ki Eraka ghaas ukhaadi.

Lekin woh ghaas turant lohe ke gadaon jaise sakht ban gayi.

Sab ek doosre ko maarne lage.

Krishna aur Balram ne unhe rokna chaha, lekin woh un par bhi hamla karne lage.

Tab Krishna aur Balram ne bhi ghaas uthayi aur usi se yudh karna pada.

Dheere-dheere poora Yadav vansh khatam ho gaya.

Balram ka Prayan

Yeh sab dekhkar Balram samundar ke kinaare chale gaye.

Wahan unhone yog dhyaan lagaya aur shaanti se apna sharir chhod diya.

Krishna ka Antim Samay

Uske baad Krishna ek peepal ke ped ke neeche shaant hokar baith gaye.

Unka divya roop chamak raha tha — neele megh jaisa rang, vanmala, mukut aur Kaustubh mani ke saath.

Tab Jara naam ka ek shikari wahan aaya.

Usne Krishna ke pair ko door se hiran samajh liya aur teer chala diya.

Jab woh paas aaya, tab usne dekha ki usne Bhagwan Krishna ko teer maara hai.

Woh darr gaya aur Krishna ke charanon mein gir pada.

Woh rota hua bola, “Prabhu, mujhse yeh galti anjaane mein ho gayi. Kripya mujhe maaf kar dijiye.”

Krishna ne shaant swar mein kaha,

“Dar mat, Jara. Yeh sab meri ichchha se hi hua hai.”

Krishna ne use maaf kar diya aur swarg jaane ka aashirvaad diya.

Daruka ka Dukh

Krishna ke saarathi Daruka unhe dhoondte hue wahan pahunch gaye.

Krishna ko dekhkar unki aankhon mein aansu aa gaye.

Krishna ne unse kaha,

“Dwarka jao aur sabko bata do ki Yadav vansh ka ant ho chuka hai. Jaldi hi samundar Dwarka ko bhi dubo dega.”

Unhone kaha ki sab log Arjun ke saath Indraprastha chale jaayein.

Antim Seekh

Krishna ne Daruka ko samjhaya,

“Yeh duniya aur sansar Maya ka khel hai. Isliye mann ko Bhagwan aur sachchai mein sthir rakho.”

Is tarah Krishna ne apni dharti ki leela samaapt ki.

Aur duniya ko yeh seekh dekar chale gaye ki ahankaar, gussa aur adharm aakhir mein vinaash hi laate hain."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 31
    with st.expander("Chapter 31 - Lord Kṛṣṇa’s Return to Vaikuṇṭha"):
        text1 = """ 
        Chapter 31 – Krishna ka Vaikunth Wapsi

Shukdev ji ne kaha, “Jab Daruka Dwarka laut gaya, tab aasman mein ek adbhut drishya dikhai diya.”

Brahma ji, Shiv ji aur Mata Parvati ke saath bahut se devta, rishi, Gandharv aur divya jeev Krishna ke paas aaye.

Sab Krishna ke Vaikunth wapas jaane ka drishya dekhna chahte the.

Aasman divya vimaano se bhar gaya. Devta Krishna ki mahima gaate hue un par phool barsa rahe the.

Krishna ka Divya Roop"""
        create_image_text_layout(
            "attached_assets/chapter11/11.31.jpg",
            text1,
            layout="side",
            image_position="left"
        )
        text2 = """ 
        Krishna ne sab devtaon ko dekha aur shaant hokar dhyaan mein baith gaye.

Unhone apni aankhen bandh kar li aur gehri samadhi mein chale gaye.

Phir bina apna divya shareer chhode, woh apne asli dhaam Vaikunth ki taraf chale gaye.

Us samay aasman mein dundubhi bajne lagi aur phoolon ki baarish hone lagi.

Satya, Dharma, Tej aur Lakshmi jaise divya gun bhi Krishna ke saath dharti chhodkar chale gaye.

Devta bhi Hairaan Reh Gaye

Brahma aur doosre devta Krishna ke is adbhut prasthan ko poori tarah samajh nahi paaye.

Krishna itni divya tarah se antardhyaan hue jaise badalon mein chamakti bijli pal bhar mein gayab ho jaaye.

Sab devta unki mahima gaate hue apne-apne lok laut gaye.

Krishna ki Leela

Shukdev ji ne samjhaya,

“Bhagwan ka janm, karm aur ant sab unki divya leela hai.”

Woh sansar ko rachkar usmein leela karte hain aur phir sab kuch apne andar sama lete hain.

Krishna chaahte toh apne shareer ko hamesha rak sakte the, kyunki unhone maut ke lok se bhi logon ko wapas laaya tha.

Lekin unhone duniya ko yeh dikhaya ki jo Atma mein sthir ho jaata hai, woh sharir ke bandhan se pare ho jaata hai.

Dwarka mein Dukh

Udhar Daruka Dwarka pahunch gaya.

Woh rote hue Vasudev aur Ugrasen ke charanon mein gir pada aur Yadav vansh ke vinaash ki khabar di.

Yeh sunkar poori Dwarka dukh mein doob gayi.

Devaki, Rohini aur Vasudev Krishna aur Balram ke bina jee nahi paaye aur shok mein apne praan chhod diye.

Yadav vansh ki mahilaayein bhi apne pati aur parivaar ke saath agni mein pravesh kar gayin.

Rukmini aur Krishna ki doosri raniyon ne bhi Krishna ko yaad karte hue apna sharir tyaag diya.

Arjun ka Dukh

Arjun apne priya mitra Krishna ke bichhadne se bahut dukhi tha.

Lekin usne Krishna ke diye hue Gita ke gyaan ko yaad karke apne mann ko sambhala.

Usne sab Yadavo ke antim sanskaar karvaaye aur bache hue logon ko surakshit Indraprastha le gaya.

Dwarka ka Doobna

Krishna ke chale jaane ke baad samundar dheere-dheere Dwarka nagari ko dubone laga.

Sirf Krishna ka mahal paani mein nahi dooba.

Arjun ne Yadav vansh ke bache hue logon ki raksha ki aur Vajra ko unka naya raja bana diya.

Antim Seekh

Shukdev ji ne kaha,

“Jo vyakti Krishna ki leelaon aur unke gyaan ko shraddha se sunta ya sunata hai, uska mann pavitra ho jaata hai.”

Aur jo sachche prem se Bhagwan ko yaad karta hai, woh dheere-dheere sansar ke dukh aur paapon se mukta ho jaata hai."""
        create_image_text_layout(text_content=text2, layout="full")

# numbers-nobody-publishes
Licensee matching &amp; revenue/employee estimation

## Partea 1

Pentru partea 1, am avut de ales un eșantion de firme din cele date în fișierul sursǎ `licensee_list.csv`. Eșantionul ales a fost de **9 firme**.
<img width="1051" height="315" alt="Captură de ecran din 2026-09-06 la 23 34 18" src="https://github.com/user-attachments/assets/3290eadc-8ccb-4e93-8fcb-663432306230" />

Nu am utilizat o metodǎ de eșantionare regǎsitǎ în teorie și literatura de specialitate (cum ar fi spre exemplu eșantionarea din k în k pași sau cea aleatoare). Bazat pe sfaturile primite, am selectat un eșantion mic care sǎ cuprindă entități care „esueasa" într‐un mod diferit. Am selectat ce mi-a atras mie cel mai mult atenția si mi s-a părut ca va fi o provocare. Printre firmele selectate se numǎrǎ: un grup mare de inginerie listat la bursă, cu declarații publice curate (Siemens Energy), un distribuitor industrial public (Fastenal), un asigurător mutual cu norme de transparență mai flexibile (LV=), un administrator de active alternative listat la bursă, unde „venitul” în sine este un concept ambiguu (EQT AB), un startup românesc trasabil prin datele registrului local (FintechOS), un nume de marcă pentru consumatori care ascunde entitatea contractantă reală (Uber Eats - Uber Technologies, Inc.), un nume comun de cel puțin două companii reale fără legătură (Phoenix Group), o companie privată fără declarații publice statutare (Apex Group Ltd.) și o entitate a cărei existență nu am putut confirma deloc (Panificație Straja S.R.L.).

Procesul de gândire ce a stat in spatele muncii de a găsi date despre firmele selectate, de a cântări informațiile găsite si a alege-o pe cea care mi s-a părut mie potrivită, se regăsește in fișierul atașat `firme_alese.xlsx`. 

## Partea 2

Pentru partea a 2a, am ales ruta detectivului. De ce am ales aceasta ruta? Dintr-un motiv important. După ce m-am uitat de mai multe ori peste eșantionul selectat, mi-am dat seama ca unele unități din eșantion vor avea nevoie de un alt tip de dovada, ceea ce a furnizat judecata de la caz la caz in locul unui model general prin care sa preiau date. 
Pentru fiecare cifra pusă in document, am prezentat estimarea punctuală, metoda/sursa care a produs-o, data și un nivel de încredere (Ridicat/ Moderat), fiecare nivel având o bandă de eroare explicită (mai jos urmează sa fie explicată). Un număr simplu nu oferă unui analist nimic cu care să se apere sau să se îndoiască de el. 

Spre exemplu, am preluat date prin rapoartele anuale publicate de către firmele in cauza in care erau transparente despre venituri si număr angajați, fiind cea mai de încredere sursa. Au fost cazuri in care am găsit aceste rapoarte postate pe o pagina dedicată potentialilor investitori, cel mai probabil cu scopul de a ii atrage in a investi. 

Ce am învățat uitându-ma prin rapoarte si este si un lucru de care trebuie sa ținem cont pe viitor? Faptul ca anii fiscali nu se aliniază între companii așa cum se întâmplă în cazul entităților din România (de exemplu, anul fiscal al Siemens Energy se încheie la 30 septembrie, nu la 31 decembrie). 

Pentru Phoenix group initial gasisem cifra pentru anul 2024 (venituri de 206 milioane USD), dar un raport mai recent pentru anul fiscal 2025 a arătat că veniturile s-au înjumătățit aproape la 118 milioane USD. Utilizarea cifrei învechite ar fi picat testul „descrie compania la momentul în care declarați?”, așa că am renunțat la cifra pentru anul fiscal 2024 în favoarea anului curent si am ales sa caut mai amantutit. 

Un alt impediment a reprezentat compania LV= (care am crezut inițial ca e o prescurtare pentru Louis Vuitton înainte sa o caut pe internet), a prezentat inițial LV= cu venituri de 5,4 milioane de lire sterline și 1.200 de angajați, o cifră mică pentru o companie cu poziția sa pe piață (probabil o înregistrare învechită sau atribuită greșit). 

Reproductibilitatea acestei metode este valabilă pentru companiile care sunt listate la bursa din lume , de aceea putem lua un interval de încredere de ± 5%.

Pentru firma inregostrata in România, am găsit date, bineînțeles unde era si de așteptat, pe `listafirme.ro`. Este o metoda ușor reproductibile, dar este limitată din punct de vedere geografic, deoarece putem găsi doar date din România. Declarațiile anuale românești pot fi căutate centralizat, sunt gratuite și sunt asociate unui cod fiscal unic (CUI). Aici a fost cel mai ușor, deoarece companiile din România depun prin lege cifre reale, verificabile , ceea ce face ca entitățile înregistrate în RO să fie disproporționat de ușor de verificat decât companiile private din orice altă parte a acestui eșantion.

Ca reproductibilitate undeva la 1,3 milioane de companii active sunt înregistrate la ONRC, dintre care aproximativ 816.000 au depus o declarație anuală pentru 2025. Ca interval de încredere putem lua ±10%.

Un al mod prin care am găsit necesarul de informații a fost prin estimări ale furnizorilor de date terță, pe care le-am utilizat doar atunci când nu exista o înregistrare principală sau înregistrarea nu a raportat cifra specifică necesară. Încrederea este moderata într-o astfel de metoda, deoarece acești furnizori estimează adesea cifrele în loc să le raporteze direct. Metoda este reproductibila limitat, funcționează bine pentru companii mari cunoscute, dar daca am aplica pentru firme mici, probabil nu am avea succes, cum nu am avut eu cu firma Panificație Straja SRL. 

Un impediment a fost la Apex Group, unde găsisem surse unde era menționat jumătate din numărul de angajați din sursa in care am ales sa am încrederea cea mai mare. Interval de încredere ±20- 25%, deoarece acești furnizori estimează ei înșiși adesea, în loc să raporteze o cifră depusă.

Pe lângă aceste metode, important de menționat este căzut EQT AB. EQT AB este un administrator de active alternative, „venitul total” raportat este venitul din comisioane de management/performanță (sau cel puțin așa am considerat eu). Activele sale administrate de aprox . 270 de miliarde de euro spun, probabil, mai multe despre amploarea sa reală. Aceasta este o judecată care merită semnalată separat clientului, deoarece un nivel de licențiere bazat doar pe „venituri” ar putea evalua greșit o afacere bazată pe comisioane precum aceasta.


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

## Partea 3

Aș livra așa ceva? Nu:) . Parțial vorbind, pentru firmele unde am găsit date concrete din surse cu încredere ridicată, da. Doar ca, in fișierul sursa erau scrise anumite firme atât de general, ca in cazul Phoenix Group. Despre care Phoenix Group zice clientul? Cel din Germania, firma pharma? De cel din UAE? La fel si la Apex? Care din ele? Compania mica care are o entitate si la Brașov priducator de schimbătoare de caldura? Cea din Insulele Bermude?. De asemenea, cazul Panificație Straja S.R.L. rămâne „not found", fără să pot spune sigur dacă firma nu există sau doar eu am ratat-o.

Primul pas pe care l-aș face când as avea un client, nu ar fi sa ma apuc de capul meu fără sa am toate informațiile necesare. Astfel munca este mult mai migăloasă, durează mai mult, deci ineficientă si probabil rezultatul este necalitativ. Cel puțin eu din experiența proprie si de la facultate de când făceam proiecte si scriam la licență, știu ca rezultatul final la care ajungi, trebuie sa fie ceva de pe urma căruia sa poți scoate bani, un rezultat care ți-ar aduce venituri, te-ar ajuta la luare de decizii CARE îți aduc bani. In contextul de fata, clientul nu cred ca ar avea ce face cu livrabilul meu. 

Dacă aș continua, aș cere acces la contractul original pentru aceste cazuri, orice detaliu în plus față de numele scris de agentul de vânzări (adresă, CUI/VAT) ar reduce mult din ghicit și aș căuta o a doua sursă independentă pentru cifrele de la furnizori terți, ca să restrâng intervalul de eroare. Ce nu pot vedea verificările mele, oricât de atent aș căuta est dacă entitatea potrivită e chiar cea care a semnat licența , dacă vreo firmă din eșantion s-a restructurat recent pentru ca o achiziție ar schimba „mărimea" reală fără să apară imediat în vreun raport , și dacă eșantionul meu de 9 din 100 e reprezentativ , probabil am ales, fără să-mi dau seama, firme mai vizibile internațional, mai ușor de cercetat decât multe din celelalte 91 de nume.

## Partea 4

S-a potrivit cumva ca doua firme din eșantionul ales sa aparțin unei categorii de business adică intermediari financiari,administratori de active, de fonduri, de comisioane , unde venitul raportat nu reflectă amploarea reală a activității, ci comisioanele de management sau de performanță încasate (cum am menționat anterior). EQT AB și Apex Group, amândouă au fost cele mai greu de cercetat, pentru EQT AB, activele administrate (aprox.270 mld. €) spun mult mai mult despre mărimea reală decât venitul raportat iar pentru Apex Group, lipsa oricărei declarații publice a forțat o estimare cu bandă de eroare de ±20-25% din surse terță. După părerea mea, având in vedere ca eșantionare nu s-a produs pe o baza teoretică, ci pe o preferință subiectivă a mea si cu toate astea reprezentativitatea acestei categorii este destul de semnificativă, e foarte probabil ca licențiați similari  să reprezinte o parte semnificativă și nedetectată din restul celor 100 de nume. 

Recomandarea mea ar fi ca in cazul acestei categorii sa se găsească o metrica diferită fata de restul categoriilor, bazata pe active administrate, număr angajați, sau volum de tranzacții procesate. 


## Partea 5

Doream sa rulez codul in Google Colab pentru ca îmi era mie mai ușor fiind obișnuită cu interfața si cu ce am mai lucrat cu meridian si in internship, doar ca din păcate astăzi Google are niște probleme semnalate si de către alți utilizatori astfel încât va voi arată pas cu pas procesul prin care am trecut in terminal. 

<img width="1390" height="394" alt="Captură de ecran din 2026-09-07 la 12 56 34" src="https://github.com/user-attachments/assets/dcd991ee-3840-4fb2-a622-84b810d5ee24" />
Am verificat versiunea de Python pe care o aveam pe laptop, mai apoi am instalat pandas. Cele doua avertizări sunt minore si le-am ignorat complet.

<img width="1390" height="395" alt="Captură de ecran din 2026-09-07 la 12 59 00" src="https://github.com/user-attachments/assets/8f05c284-503c-4354-81a8-1ab67dc642dd" />
Am creat un folder unde am lucrat si acolo am desacrcat fișierele de care aveam nevoie mai departe. 

<img width="1390" height="115" alt="Captură de ecran din 2026-09-07 la 13 00 36" src="https://github.com/user-attachments/assets/76f3af02-1f33-4b9f-beba-1666d09e115e" />
Arată de unde vine coloana CAEN pentru proxy

<img width="1390" height="212" alt="Captură de ecran din 2026-09-07 la 13 01 46" src="https://github.com/user-attachments/assets/7d26b7de-6e7e-46e9-a095-219d0cb35b51" />
De ce am ales codul 1048 ca insemand activa. am ales 1048 pentru că procentul lui se încadrează cel mai bine în intervalul 30-45% așteptat pentru firme active, pe baza datelor publice ONRC. Cifra rezultată (1.644.538) e totuși mai mare decât cifra oficială ONRC (1,3 milioane, iulie 2026), ceea ce sugerează că definiția "activă" din acest fișier ar putea fi mai largă decât cea folosită de ONRC în statisticile sale publice

<img width="1390" height="203" alt="Captură de ecran din 2026-09-07 la 13 10 09" src="https://github.com/user-attachments/assets/82a13130-c70e-4b1a-8465-77273b4fae93" />
Rezultatul final

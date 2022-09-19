from colorama import Fore
from random import randint

hk416 = 0
Sjokoladeis = 0
Vaniljeis = 0
kniv = 1
mistenkligpille = 0

liv = randint(80,120)

def sjekk_liv():
    if liv < 1:
        print("du døde")
        print("slutt")
        exit()



mc = input("Velg navn ")


def hjemme():
    print ("Det er en vanlig dag. " + mc + " sitter hjemme.")
    print("Men det er et problem. Sola skinner og det er glovarmt.")
    print( mc + " bestemmer deg for å kjøpe is.")
    ute()


def ute():
    global Sjokoladeis, liv
    print( mc + " går ut og finner iskremsjappa. Der står iskremmannen og gir ut is.")
    print("nå må " + mc + " velge is.")
    valg1 = input("A: sjokaladeis | B: Vaniljeis -> ")
    if valg1 == "A":
        sjokolade()

    if valg1 == "B":
        vanilje()

def sjokolade():
    global Sjokoladeis, liv
    Sjokoladeis += 1
    print ("Du fikk: 1 sjokoladeis")
    print( mc + " kjøper sjokaladeis.")
    print("men plutselig står en gjeng der og ser på deg med sinte fjes.")
    print("de tror at du er rasist. hva skal du gjøre nå?")
    valg1a = input("A: Forklare til gjengen hvorfor du IKKE er rasist av å spise sjokoladeis | B: Løp bort fra gjengen | C: bli der og bank gjengen opp -> ")
    if valg1a == "A":
        print("Du forklarer til gjengen hvorfor du ikke er rasistisk av å spise sjokoladeis.")
        print("de mener at det du sier er BS og de banker deg opp.")
        liv -= 10
        print("du mister noen tenner og blir sent til sykehuset.")
        sykehus()

def vanilje():
    print ("du fikk: 1 vaniljeis.")
    print(mc + " kjøper vaniljeis.")
    print("du går hjem med isen og sjekker telefonen")
    print("du ser nyhetene, og trykker inn på det")
    print("å nei! Bergen har erklert selvstendighet og har formet ''fri bergen bevegelsen''. du blir nå kalt inn i hæren.")
    print("blir du med i hæren?")
    valg2 = input("A: Du blir med | B: Du blir ikke med -> ")
    if valg2 == "A":
        militær_leir()
    
    if valg2 == "A":
       
        global Vaniljeis, valg24, valg24b
        print("du ble ikke med i hæren")
        print("du nyter iskremen din")
        Vaniljeis -= 1
        print("du hører plutselig en lyd fra skogen")
        print("bryr du deg?")
        valg24 = input("A: Du bryr deg og sjekker ut lyden | B: du bryr deg ikke og sjekker ikke ut lyden -> ")
        if valg24 == "B":
            print("du sjekker ikke ut lyden og står der")
            print("plutselig ser du noe komme løpene ut skogen")
            print("Jeff Bezos kommer løpene mot deg i full fart")
            print("han er klar for å drepe deg. hva skal du gjøre nå?")
            valg24b = input("A: Angrip tilbake | B: Dukk unna! -> ")
            if valg24b == "A":
                if hk416 > 0:
                    print("Du tar hk416en din og skyter Jeff bezos ned")
                else:
                    print("du gjør deg klar for å ta imot angrepet")
                






def militær_leir():
    global hk416
    print("du blir med i hæren og trenes opp til å bli en soldat")
    print("på vei bort til treningssalen finner du en hk416 stående intill veggen")
    print("vil du stjele den?")
    rifle = input("A: Du tar våpnet | B: Du lar det bli -> ")
    if rifle == "A":
        print ("Du tok våpnet")
        hk416 += 1
        print ("Du gjømmer våpnet i sekken")
    elif rifle == "B": 
        print("du lot våpnet bli og stjal det ikke")
    
    print ("du hører noen rope: '' " + mc + " !!''")
    print("du snur deg rundt og ser barnehage-mobberen din!")
    print("Hva skal du gjøre nå? Han ser veldig sint ut.")
    valg2a = input("A: slå han ned | B: spør han hva det er -> ")
    if valg2a == "B":
        print("du spør han hva det er")
        print("''jeg skulle bare si unnskyld for å mobbe deg i barnehagen'' sier han")
        print("du aksepterer unnskyldningen og du snur deg for å fortsette videre")
        print("du kommer fram til trenningsalen og legger fra deg sekken din med utgangen")
        print("der står instruktøren og snakker til deg og resten av skvadronen din")
        c130()
    if valg2a == "A":
            print("du går bort til han og banker han opp")
            print("han ligger nede på bakken og gråter")
            print("''Kom hit nå, " + mc + "!!!'' roper instruktøren.")
            print ("du ble hentet inn til instruktørens kontor")
            print("da du er der inne kjefter instruktøren på deg")
            print("men du får ikke med deg alt hun sier. hva gjør du nå?")
            valg2b = input("A: bank opp instruktøren | B: hør resten ferdig -> ")
            if valg2b == "A":
                print("Du røyser deg opp og banker livet ut av instruktøren")
                print("hun ligger nede på gulvet og gråter")
                print("du tar en kniv ut av lommen din og stikker henne i halsen")
                print("nå snur du deg og løper ut av kontoret før noen finner bevis")
                print("ved utgangen blir du stoppet av en skvadron med armerte soldater")
                print("hva gjør du i denne situasjonen?")
                valg2c = input("A: angripe soldatene | B: overgi deg -> ")
                if valg2c == "A":
                    if hk416 > 0: 
                        print("du bruker hk416 din og skyter ned soldatene")
                        print("du drepte alle soldatene, og løp videre")
                        skogen()
                    else:
                        global liv
                        print("du angriper soldatene")
                        print("men før du får tid til å slåss så skyter de deg ned")
                        liv -= 500
                        sjekk_liv()

def skogen():
    print("du løper bort veien")
    print("men lengre nede ser du en pansret blokade!")
    print("du ser 2 cv90er og rundt 8 soldater")
    print("hvordan skal du komem deg unna?")
    valg2d = input("A: snu deg og løp inn i skogen | B: skyt på fiendene med våpnet ditt -> ")
    if valg2d == "A":
        print("du snur og løper rett inn i skogen")
        print("det ser ut som at du mistet dem, men for å være sikker fortsetter du videre")
        print("du kommer frem til ett busstopp med veien")
        print("men da du ser til venstre, ser du en fergekai")
        print("hva velger du?")
        valg2e = input ("A: Du velger fergen | B: Du går videre veien -> ")
        if valg2e == "A":
            Kina()

def Kina():
    global liv
    print("du velger fergen")
    print("du venter på å nå land")
    print("etter hva som føles ut som flere uker, ender du endelig opp på land")
    print("du går av fergen")
    print("du ser deg rundt etter skilt som kansje kan vise deg hvor du er")
    print("du ser ett skilt der det står: ''欢迎来到中国，游客我们会说英文''")
    print("å nei. du er i Kina")
    print("plutselig så hyler folkene som er på kaien etter de ser hk416en din")
    print("da kommer det plutselig en skvadron med kinesiske soldater i biler kjørende inn på kaien.")
    print("du prøver å skyte dem med hk416en din, men du blir desværre skutt ned av ett maskingevær")
    liv -= 500
    sjekk_liv()



def sykehus():
    global mistenkligpille
    print("på sykehuset forklarer du hvordan og hvem du ble banket opp av.")
    print("doktoren er litt mistenkelig. han spør: ''Vil du ha denne pillen? Gi den til gjengen og se hva som skjer ;)'' ")
    print("tar du imot pillen?")
    valg1b = input("A: ta pillen og gi den til gjengen | B: ikke ta pillen -> ")
    if valg1b == "A":
        mistenkligpille = randint(0,1)
        print("Du tar pillen og går ut av sykehuset.")
        slum()

def slum():
    global mistenkligpille
    print("Neste dag går du til iskremsjappe og møter gjengen.")
    print("du gir dem pillen og sier: ''Spis denne pillen for 1000kr''")
    print("''ok pyse. vi spiser den.''")
    if mistenkligpille > 0:
        print("gjenglederen spiser pillen. Plutselig detter han ned og dør. de andre i gjengen ser på deg og løper bort")
        print("gratulerer. du drepte en person fordi du mistet en tann. er du stolt?")
        print("Slutt")
        exit()
    else: 
        print("Du gir dem pillen")
        print("gjenglederen spiser pillen")
        print("ingenting skjer")
        print("''Haha! ingenting skjedde! gi oss pengene!''")
        valg1c = input("A: Gi dem pengene | B: Løp bort med pengene -> ")
        if valg1c == "A":
            print("du gir dem pengene og går bort, trist")
            print("men du har litt penger igjen")
            print("og du føler deg sulten for iskrem")
            print("du snur og går tilbake til iskremsjappa")
            ute()
        if valg1c == "B":
            pass
def c130():
    global hk416, liv
    print("til slutt blir dere blir sent videre til å slåss mot fri bergen bevegelsen.")
    print("du er plassert ombord i en c-130 og sent til bergen")
    print("ombord flyet gir skvadron lederen deg en hk416")
    hk416 += 1
    print("plutselig opner dørene seg, og skvadron lederen roper: ''Ta fallskjermene og hopp ut!!!''")
    print("du ser en paraply og en fallskjerm. hvilken velger du?")
    valg23 = input("A: Ta paraplyen | B: Ta Fallskjermen | C: Ta ingenting og hopp rett ut -> ")
    if valg23 == "A":
        print("du tar paraplyen")
        print("du hopper ut")
        print("plutselig ser du at paraplyen ikke holdt, og du detter ned raskt")
        print("du traff bakken")
        liv -= 600
        sjekk_liv()
    if valg23 == "C":
        print("du tar ingenting")
        print("du hopper ut")
        print("din idiot, hvorfor hoppet du ut uten fallskjerm?!?")
        print("du traff bakken")
        liv -= 600
        sjekk_liv()
    if valg23 == "B":
        print("du tok fallskjermen")
        print("du hopper ut")
        print("du aktiverte fallskjermen")
        print("men så feilet fallskjermen")
        print("du detter ned")
        print("og du våkner opp, hjemme i sengen din")
        print("det var bare ett mareritt")
        hjemme()














































hjemme()

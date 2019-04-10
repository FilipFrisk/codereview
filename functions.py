"""
Läser fundamenta.txt och lägger allt i en lista.
"""

def textlasning_fundamenta(): 
  f=open("fundamenta.txt","r")
  tmp_lista = []
  while True:
    foretagsnamn = f.readline().strip()
    if foretagsnamn == "":
      break
    soliditet = f.readline().strip()
    if soliditet == "":
      break
    pe = f.readline().strip()
    if pe == "":
      break
    ps = f.readline().strip()
    if ps == "":
      break 
    tmp_lista.append([foretagsnamn,soliditet,pe,ps])
  f.close()
  return(tmp_lista)

"""
Används i aktier för att läsa txt filerna.
"""

def textlasning_kurser(file):
  fil = open(file,"r")
  kurser = []
  for rad in fil:
    rad = rad.split()
    kurser.append(rad)
  fil.close()
  return(kurser)

"""
Läser in data ifrån kurser.txt och OMX.txt samt retunerar listor med kursdata.
"""

def aktier():
  Ericsson_kurser = []
  Electrolux_kurser = []
  AstraZeneca_kurser = []
  HennesMauritz_kurser = []
  OMX_kurser = []
  tmp_lista = []
  kurser = textlasning_kurser("kurser.txt")
  OMX = textlasning_kurser("OMX.txt")
  for i in range(67):
    tmp_lista.append([kurser[i+1][0]])
    tmp_lista.append([kurser[i+1][1]])
    Ericsson_kurser.append(tmp_lista[0][0])
    Ericsson_kurser.append(float(tmp_lista[1][0]))
    tmp_lista = tmp_lista[2:]
  
  for i in range(67):
    tmp_lista.append([kurser[i+69][0]])
    tmp_lista.append([kurser[i+69][1]])
    Electrolux_kurser.append(tmp_lista[0][0])
    Electrolux_kurser.append(float(tmp_lista[1][0]))
    tmp_lista = tmp_lista[2:]  
  
  for i in range(67):
    tmp_lista.append([kurser[i+137][0]])
    tmp_lista.append([kurser[i+137][1]])
    AstraZeneca_kurser.append(tmp_lista[0][0])
    AstraZeneca_kurser.append(float(tmp_lista[1][0]))
    tmp_lista = tmp_lista[2:]  

  for i in range(67):
    tmp_lista.append([kurser[i+205][0]])
    tmp_lista.append([kurser[i+205][1]])
    HennesMauritz_kurser.append(tmp_lista[0][0])
    HennesMauritz_kurser.append(float(tmp_lista[1][0]))
    tmp_lista = tmp_lista[2:]  

  for i in range(67):
    tmp_lista.append([OMX[i][0]])
    tmp_lista.append([OMX[i][1]])
    OMX_kurser.append(tmp_lista[0][0])
    OMX_kurser.append(float(tmp_lista[1][0]))
    tmp_lista = tmp_lista[2:]

  return(Ericsson_kurser,Electrolux_kurser,AstraZeneca_kurser,HennesMauritz_kurser,OMX_kurser)


"""
Funktion som beräknar betavärdet på OMX under givna perioden.
"""

def kursutveckling_omx(lista):
  tmp_2 =[]
  for i in range(1,134,2): #data = datum,kurs,datum,kurs....
    tmp_2.append(lista[i])
  slut_kurs = tmp_2[66]
  start_kurs = tmp_2[0]
  kursforandring = (slut_kurs/start_kurs) - 1
  kursforandring = round((kursforandring)*100,2)
  return(kursforandring)

class aktie: #skapar objektet för alla olika fundamenta per aktie
    def __init__(self,foretagsnamn,soliditet,pe,ps,kurser):
        self.foretagsnamn = foretagsnamn
        self.soliditet = soliditet
        self.pe = pe
        self.ps = ps
        self.kurser = kurser

    def hamtaFundament(self):
        return(print('företagets soliditet är {self.soliditet}'.format(self=self) + "\n" +
               'företagets p/e är {self.pe}'.format(self=self) + "\n"
               'företagets p/s är {self.ps}'.format(self=self) ))

    def t_data(self):
      tdata = aktie.avkastning_maxmin_30(self)
      return(print("\n" +'kursutveckling(30 senaste dagarna){} %'.format(tdata[0]) + "\n" +
               'betavärde {}'.format(tdata[1]) + "\n"
               'lägsta kurs(30 senaste dagarna) {}'.format(tdata[2]) + "\n" +
               'högsta kurs(30 senaste dagarna) {}'.format(tdata[3])))
    
    def kurser(self,textlangd,antal_kurser_i_txt,langd):
      tmp = []
      tmp_short = []
      for i in range(1,textlangd,2): #data = datum,kurs,datum,kurs....
          tmp.append(self.kurser[i])
      for i in range(langd):
          tmp_short.append(tmp[antal_kurser_i_txt-i]) #datan blir åt andra hållet
      return(tmp,tmp_short)

    def avkastning_maxmin_30(self):
        [tmp,tmp_30] = aktie.kurser(self,134,66,30)
        max_varde_30 = max(tmp_30) #fel det ska vara 30 senaste dagarna
        min_varde_30 = min(tmp_30)
        slut_kurs = tmp_30[0]
        start_kurs = tmp_30[29]
        kursforandring = (slut_kurs/start_kurs) - 1
        avkastning_30 = round((kursforandring)*100,1)
        beta_varde = aktie.beta_varde(self)
        beta_varde = round((kursforandring),3)
        return([str(avkastning_30),str(beta_varde),min_varde_30,max_varde_30])

    def beta_print(self):
        [x,beta,z,w] = self.avkastning_maxmin_30()
        return({self.foretagsnamn:float(beta)})

    def beta_varde(self):
        [tmp,tmp_30] = aktie.kurser(self,134,66,30)
        slut_kurs = tmp[66]
        start_kurs = tmp[0]
        kursforandring = (slut_kurs/start_kurs) - 1
        [Ericsson_kurser,Electrolux_kurser,AstraZeneca_kurser,HennesMauritz_kurser,OMX_kurser] = aktier()
        OMX_kursforandring = kursutveckling_omx(OMX_kurser)
        beta = kursforandring / OMX_kursforandring
        return(beta)


"""
Print funktioner för läsbarhet i main.
"""

def tillbaka_huvudmeny():
  return(input("Tryck på enter för att komma tillbaka till huvudmenyn"))

def presentera(analystyp,aktie):
  return(print("\n"+'—————{} analys för {}————–'.format(analystyp,aktie)))



"""
En funktion som printar en lista i ordning med siffror.
"""
def huvudmeny(lista):
  #print("\n")
  for rad in range(1,len(lista)+1):
    print("{}.{} ".format(rad,lista[rad-1]))
  #print("\n")

"""
En funktion som ställer en fråga och retunerar svaret.
"""

def inputs(question,antalval):
  while True:
    try:
      x = question 
      svar = input('{}'.format(x))
      validerainput(int(svar),antalval) #4:an är antal möjliga alternativ
      return(svar)
    except ValueError:
      print("\n")
      print("Försök igen")
      print("\n")

"""
Felhanterar input till funktionen inputs.
"""

def validerainput(svar,antalval):
        lista = list(range(1,antalval+1))
        if svar not in lista:
          raise ValueError





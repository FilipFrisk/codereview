import functions
#Fixa funktioner till printsen 
[Ericsson_kurser,Electrolux_kurser,AstraZeneca_kurser,HennesMauritz_kurser,OMX_kurser] = functions.aktier() # dra ner alla kurser ifrån filer

lista = functions.textlasning_fundamenta()

Ericsson = functions.aktie(lista[0][0],lista[0][1],lista[0][2],lista[0][3],Ericsson_kurser)
Electrolux = functions.aktie(lista[1][0],lista[1][1],lista[1][2],lista[1][3],Electrolux_kurser)
AstraZeneca = functions.aktie(lista[2][0],lista[2][1],lista[2][2],lista[2][3],AstraZeneca_kurser)
HennesMauritz = functions.aktie(lista[3][0],lista[3][1],lista[3][2],lista[3][3],HennesMauritz_kurser)

I_huvudmeny = ["Fundamental analys (Vid långsiktigt aktieinnehav)","Teknisk analys (Vid kort aktieinnehav)","Rangordning av aktier med avseende på dess betavärde","Avsluta"]

while True:
	print(""" 
			—————————Meny———————————
		""")
	functions.huvudmeny(I_huvudmeny) # Funktion som skapar huvudmenyn baserat på listan på rad 3 med strängar
	svar = int(functions.inputs("Vilket alternativ vill du välja? ",4)) #En funktion som vailderar valet i huvudmenyn
	if svar == 1: #fördelar svaren ifrån användaren
		print("\n")
		print("En fundamental analys kan utföras på följande aktier:")
		functions.huvudmeny([lista[0][0],lista[1][0],lista[2][0],lista[3][0]]) 
		svar = int(functions.inputs("Vilken aktie vill du göra fundamental analys på? ",4))
		if svar == 1:
			functions.presentera("Fundamental analys","Ericsson")
			Ericsson.hamtaFundament()
			print("\n")
			functions.tillbaka_huvudmeny()
		elif svar == 2:
			functions.presentera("Fundamental analys","Electrolux")
			Electrolux.hamtaFundament()
			print("\n")
			functions.tillbaka_huvudmeny()
		elif svar == 3:
			functions.presentera("Fundamental analys","AstraZeneca")
			AstraZeneca.hamtaFundament()
			print("\n")
			functions.tillbaka_huvudmeny()
		elif svar == 4:
			functions.presentera("Fundamental analys","HennesMauritz")
			HennesMauritz.hamtaFundament()
			print("\n")
			functions.tillbaka_huvudmeny()
	elif svar == 2:
		print("\n")
		print("En teknisk analys kan utföras på följande aktier:")
		functions.huvudmeny([lista[0][0],lista[1][0],lista[2][0],lista[3][0]]) 
		svar = int(functions.inputs("Vilken aktie vill du göra teknisk analys på? ",4))
		if svar == 1:
			functions.presentera("Teknisk analys","Ericsson")
			Ericsson.t_data()
			print("\n")
			functions.tillbaka_huvudmeny()
		elif svar == 2:
			functions.presentera("Teknisk analys","Electrolux")
			Electrolux.t_data()
			print("\n")
			functions.tillbaka_huvudmeny()
		elif svar == 3:
			functions.presentera("Teknisk analys","AstraZeneca")
			AstraZeneca.t_data()
			print("\n")
			functions.tillbaka_huvudmeny()
		elif svar == 4:
			functions.presentera("Teknisk analys","HennesMauritz")
			HennesMauritz.t_data()
			print("\n")
			functions.tillbaka_huvudmeny()

	elif svar == 3:
		print("\n")

		beta1 = Ericsson.beta_print()
		beta2 = HennesMauritz.beta_print()
		beta3 = AstraZeneca.beta_print()
		beta4 = Electrolux.beta_print()

		betavarden = {}
		betavarden.update(beta1)
		betavarden.update(beta2)
		betavarden.update(beta3)
		betavarden.update(beta4)
		nr = 1
		print("—–Rangordning av aktier med avseende på dess betavärde——")
		print("\n")
		for i in betavarden:
			print (str(nr) + "." + i +" "+ str(betavarden[i]))
			nr=nr+1
		#a = beta1.values()
		#print(a)
		#test = [beta1,beta2,beta3,beta4]
		#print(beta1("Ericsson"))
		#tmp = []
		#for i in range(len(test)):
		#	tmp.append(float(test[i][0]))
		#	tmp.append(test[i][1])
		#print(tmp)
		#for i in range(len(test)):
		#	test1 = max(tmp)
		#	tmp = tmp.remove(test1)
		#	print((i+1)+"."+ .format(test1)


		#betavarden = [float(beta1[0]),float(beta2[0]),float(beta3[0]),float(beta4[0])]
		#betavarden_i_ordning = sorted(betavarden)	
		#functions.huvudmeny([str(betavarden_i_ordning[3]),str(betavarden_i_ordning[2]),str(betavarden_i_ordning[1]),str(betavarden_i_ordning[0])]) 

		#print("\n")
		functions.tillbaka_huvudmeny()
	elif svar == 4:
		print("Programmet avslutat!")
		exit()





















#for i in range(4):
#	for k in range(4):
#		lista[i] = functions.aktie(lista[i][k],lista[i][k],lista[i][k],lista[i][k])
		
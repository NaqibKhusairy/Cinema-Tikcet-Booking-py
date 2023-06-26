from datetime import date
import os
os.system('cls')
totalPrice = 0
BilUser=1
table = [
			["Bil.","  \tTajuk\t","Children","Adults","\tSenior Citizen"],
			[" 1", "   Mechamato Movie", " RM10","  \tRM13","    \t     RM11"],
			[" 2", "\t 65", " \t RM11","  \tRM14","    \t     RM12"],
			[" 3", "     Polis Evo 3", " RM15","  \tRM18","    \t     RM14"],
			[" 4", "   Didi And Friend", " RM9","  \tRM12","    \t     RM10"]
		]
TiketBooked=[]
while True :
	print("\n---------------------- Cinema Online ------------------------\n")
	tarikh = date.today()
	print("\t\t"+str(tarikh))
	print("\t\tTicket Pricing")
	print("\n-------------------------------------------------------------")
	print()
	for row in table:
		for col in row:
			print(col,end="\t")
		print()
	print("\n-------------------------------------------------------------")
	name=input("\n\tName :  ")
	name=name.upper()
	phone_no=input("\tPhone Number :  ")
	MovieNo = int(input("\tChoose Movie [1 or 2 or 3 or 4] = "))
	if MovieNo == 1 or MovieNo== 2 or MovieNo == 3 or MovieNo== 4:
		if MovieNo ==1 :
			movieName=table[1][1]
		elif MovieNo ==2 :
			movieName=table[2][1]
		elif MovieNo ==3 :
			movieName=table[3][1]
		elif MovieNo ==4 :
			movieName=table[4][1]
		TiketType = int(input("\tChoose Tiket Type Children(1) or Adults(2) or Senior Citizen(3) [1 or 2 or 3] = "))
		if TiketType == 1 or TiketType==2 or TiketType==3 :
			if TiketType == 1:
				TiketType=table[0][2]
				if MovieNo == 1:
					TiketPrice = 10
				elif MovieNo == 2:
					TiketPrice = 11
				elif MovieNo == 3:
					TiketPrice = 15
				elif MovieNo == 4:
					TiketPrice = 9
			elif TiketType == 2:
				TiketType=table[0][3]
				if MovieNo == 1:
					TiketPrice = 13
				elif MovieNo == 2:
					TiketPrice = 14
				elif MovieNo == 3:
					TiketPrice = 18
				elif MovieNo == 4:
					TiketPrice = 12
			elif TiketType == 3:
				TiketType=table[0][4]
				if MovieNo == 1:
					TiketPrice = 11
				elif MovieNo == 2:
					TiketPrice = 12
				elif MovieNo == 3:
					TiketPrice = 14
				elif MovieNo == 4:
					TiketPrice = 10
			else:
				print("\n-------------------------------------------------------------\n")
				print("     You just need to fill either 1 or 2 or 3!!!")
				print("\n--------------------------------------------------------\n")
				break
		else:
			print("\n-------------------------------------------------------------\n")
			print("     You just need to fill either 1 or 2 or 3 or 4 !!!")
			print("\n--------------------------------------------------------\n")
			break
		movieName=movieName.upper()
		TiketType=TiketType.upper()
		print("\n------------------------- RECIEPT ---------------------------\n")
		print("\tYour Booking Details")
		print("\tName : " + name)
		print("\tPhone No : " + phone_no)
		print("\tMovie : \b" + movieName)
		print("\tTiket Type : "+TiketType)
		print("\tTiket Price : RM"+str(TiketPrice))
		totalPrice += TiketPrice
		print("\n-------------------------------------------------------------\n")
		TiketBooked.append(
			{
				'name' : name,
				'phone_no' : phone_no,
				'movieName' : movieName,
				'TiketType' : TiketType,
				'TiketPrice' : str(TiketPrice)
			})
	else:
			print("\n-------------------------------------------------------------\n")
			print("     You just need to fill either 1 or 2 !!!")
			print("\n-------------------------------------------------------------\n")
			break
	AskUser=input("Insert Y to Continue Booking More Tiket or press Enter to Exit = ")
	AskUser=AskUser.upper()
	if AskUser == 'Y':
		BilUser+=1
		os.system('cls')
		print("\n-------------------------------------------------------------\n")
		print()
	else:
		os.system('cls')
		print("\n-------------------------------------------------------------\n")
		print("\tThankYou To Booking Tiket With Us.")
		if(BilUser==1):
			print("\tYou Booking "+str(BilUser)+" Tiket.")
		else:
			print("\tYou Booking "+str(BilUser)+" Tikets.")
		print("\n------------------------- RECIEPT ---------------------------\n")
		print("\tYour Booking Details")
		for x in range(BilUser):
			print("\tName : " +TiketBooked[x]['name'])
			print("\tPhone No : " + TiketBooked[x]['phone_no'])
			print("\tMovie \b: " + TiketBooked[x]['movieName'])
			print("\tTiket Type : "+TiketBooked[x]['TiketType'])
			print("\tTiket Price : RM"+TiketBooked[x]['TiketPrice'])
			print("\n-------------------------------------------------------------")
		print("-------------------------------------------------------------")
		print("\n\tYour Total Price is = RM "+str(totalPrice)+"\n")
		print("-------------------------------------------------------------\n")
		break
#hier kommt der effektive Zinssatz nach der Rechnung 
Angebote=[]

def effektiv(Zinssatz,Gebühren,Kapital,Tage):


    Zinsen=Kapital*Zinssatz*Tage/(365*100)
    print(Zinsen)

    Bearbeitungsgebür=Kapital/100*2
    #print(Bearbeitungsgebür)


    ausgezahltes_Kaptital=Kapital-Bearbeitungsgebür
    #print(ausgezahltes_Kaptital)

    #print(Zinsen,"\n",ausgezahltes_Kaptital)
    Kreditkosten=Zinsen+Bearbeitungsgebür


    effektiver_Zinssatz=Kreditkosten*100*365/(ausgezahltes_Kaptital*Tage)
    Antwort="Der Effektive Zinssatz liegt bei {:.3f} % ".format(effektiver_Zinssatz)
    List.append(Antwort)
    
    
#Hier schreibt man wie viele Angebote man vergleichen möchte
Anzahl=int(input("Anzahl der Angebote:"))

for i in range(Anzahl):
    Zinssatz=float(input("Gib ein Zinssatz ein:"))
    Gebühren=int(input("Bearbeitungsgebühren:"))
    Kapital=int(input("Mein Kapital:"))
    Tage=int(input("Gib die Dauer an !"))
    effektiv(Zinssatz,Gebühren,Kapital,Tage)
    

print("Das günstigere Angebot ist ",min(List))




# mit freundlichen Grüßen ֎֎ 








def effektiv(Zinssatz,Gebüren,Kapital,Tage,):


    Zinsen=Kapital*Zinssatz*Tage/(365*100)
    print(Zinsen)

    Bearbeitungsgebür=Kapital/100*2
    #print(Bearbeitungsgebür)


    ausgezahltes_Kaptital=Kapital-Bearbeitungsgebür
    #print(ausgezahltes_Kaptital)

    #print(Zinsen,"\n",ausgezahltes_Kaptital)
    Kreditkosten=Zinsen+Bearbeitungsgebür


    effektiver_Zinssatz=Kreditkosten*100*365/(ausgezahltes_Kaptital*Tage)
    print("Der Effektive Zinssatz liegt bei {:.3f} % ".format(effektiver_Zinssatz))


print(effektiv(Zinssatz,2,80000,292))












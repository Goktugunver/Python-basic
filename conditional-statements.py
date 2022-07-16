usdYesterday = 7.55
usdToday = 7.55
down = "the exchange rate has fallen"
up = "the exchange rate has risen"
stable = "the exchange rate has stable"


if usdYesterday>usdToday:
    print(down)
elif usdYesterday<usdToday:
    print(up)
elif usdYesterday==usdToday:
    print(stable)

#--------------------------------------------------------------------#
##we can use a different method : 

#if usdYesterday>usdToday:
    #print(down)
#elif usdYesterday<usdToday:
    #print(up)
#else: 
    #print(stable)
#--------------------------------------------------------------------#
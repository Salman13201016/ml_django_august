#Name: Md. Mahbubur Rahman
#Address: Dhaka
#Email: CreativesMahbub@gmail.com
#Mobile: 01833647547


#Each Cake Raw Material Cost for Per Pound
BlackForest = 180
VanillaCake = 150
RedVelvet = 220
LemonSponge = 165
ChocolateCake = 170

#Trasportatio Cost for each pound
Trasportationcoast = 150

#Space coast for each pound
SpaceCost = 50

#Staff Cost for Each pound 
StaffCost = 60

#Utility Coas for each pound
BlackForestUtl = (BlackForest * .03) + Trasportationcoast
VanillaCakeUtl = (VanillaCake * .03) + Trasportationcoast 
RedVelvetUtl = (RedVelvet * .03) + Trasportationcoast
LemonSpongeUtl = (LemonSponge * .03) + Trasportationcoast
ChocolateCakeUtl = (ChocolateCake * .03) + Trasportationcoast

#Total inventory Coast for each cake per pound
BlackForestInvtCost = BlackForest + BlackForestUtl + Trasportationcoast + SpaceCost + StaffCost
VenillaCakeInvtCost = VanillaCake + VanillaCakeUtl + Trasportationcoast + SpaceCost + StaffCost
RedVelvetInvtCost = RedVelvet + RedVelvetUtl + Trasportationcoast + SpaceCost + StaffCost
LemonSpongeInvtCost = LemonSponge + LemonSpongeUtl + Trasportationcoast + SpaceCost + StaffCost
ChocolateCakeInvtCost = ChocolateCake + ChocolateCakeUtl + Trasportationcoast + SpaceCost + StaffCost


#Sellin Price for Each Pound
BlackForestPrice = 780
VenillaCakePrice = 600
RedVelvetPrice = 800
LemonSpongePrice = 650
ChocolateCakePrice = 660

#5% Discounted Selling for each pound
BlackForestDisc5 = BlackForestPrice - (BlackForestPrice * .05)
VenillaCakeDisc5 = VenillaCakePrice - (VenillaCakePrice * .05)
RedVelvetDisc5 = RedVelvetPrice - (RedVelvetPrice * .05)
LemonSpongeDisc5 = LemonSpongePrice - (LemonSpongePrice * .05)
ChocolateCakeDisc5 = ChocolateCakePrice - (ChocolateCakePrice * .05)

#7% Discounted Selling for each pound
BlackForestDisc7 = BlackForestPrice - (BlackForestPrice * .07)
VenillaCakeDisc7 = VenillaCakePrice - (VenillaCakePrice * .07)
RedVelvetDisc7 = RedVelvetPrice - (RedVelvetPrice * .07)
LemonSpongeDisc7 = LemonSpongePrice - (LemonSpongePrice * .07)
ChocolateCakeDisc7 = ChocolateCakePrice - (ChocolateCakePrice * .07)

# after 5% discounted Profit on first 3 cakes
BlackForestDisc5Prof = BlackForestDisc5 - BlackForestInvtCost
VanillaCakeDisc5Prof = VenillaCakeDisc5 - VenillaCakeInvtCost
RedVelvetDisc5Prof = RedVelvetDisc5 - RedVelvetInvtCost
LemonSpongeDisc5Prof = LemonSpongeDisc5 - LemonSpongeInvtCost
ChocolateCakeDisc5Prof = ChocolateCakeDisc5 - ChocolateCakeInvtCost

#after 5% discounted Profit on reat of the cakes 
BlackForestDisc7Prof = BlackForestDisc7 - BlackForestInvtCost
VanillaCakeDisc7Prof = VenillaCakeDisc7 - VenillaCakeInvtCost
RedVelvetDisc7Prof = RedVelvetDisc7 - RedVelvetInvtCost
LemonSpongeDisc7Prof = LemonSpongeDisc7 - LemonSpongeInvtCost
ChocolateCakeDisc7Prof = ChocolateCakeDisc7 - ChocolateCakeInvtCost

#Total Pieces of Sale 5% Discounted sale
BlackForestQuant = 5
VanillaCakeQuant = 7
RedVelvetQuant = 10
LemonSpongeQuant = 5
ChocolateCakeQuant = 9

#Total Profit on Sale without first 3 cakes
BlackForestProfWO3 = ((BlackForestQuant - 3) * BlackForestDisc7Prof)
VanillaCakeProfWO3 = ((VanillaCakeQuant - 3) * VenillaCakeDisc7)
RedVelvetProfWO3 = ((RedVelvetQuant - 3) * BlackForestDisc7Prof)
LemonSpongeProfWO3 = ((LemonSpongeQuant - 3) * BlackForestDisc7Prof)
ChocolateCakeProfWO3 = ((ChocolateCakeQuant - 3) * BlackForestDisc7Prof)

#Total Profit on Total sale
BlackForestProf = BlackForestProfWO3 + (BlackForestDisc5Prof * 3)
VenillaCakeProf = VanillaCakeProfWO3 + (VanillaCakeDisc5Prof * 3)
RedVelvetProf = RedVelvetProfWO3 + (RedVelvetDisc5Prof * 3)
LemonSpongeProf = LemonSpongeProfWO3 + (LemonSpongeDisc5Prof * 3)
ChocolateCakeProf = ChocolateCakeProfWO3 + (ChocolateCakeDisc5Prof * 3)

print("1. Raw material Cost sequencely = ", BlackForest, VanillaCake, RedVelvet, LemonSponge, ChocolateCake)
print("2. Selling Price of each pound sequencely =", BlackForestPrice, VenillaCakePrice, RedVelvetPrice, LemonSpongePrice, ChocolateCakePrice)
print("3. after discounted 5% on Selling Price of each pound sequencely =", BlackForestDisc5, VenillaCakeDisc5, RedVelvetDisc5, LemonSpongeDisc5, ChocolateCakeDisc5)
print("4. after discounted 7% on Selling Price of each pound sequencely =", BlackForestDisc7, VenillaCakeDisc7, RedVelvetDisc7, LemonSpongeDisc7, ChocolateCakeDisc7)
print("5. Total Profit on sale =", BlackForestProf, VenillaCakeProf, RedVelvetProf, LemonSpongeProf, ChocolateCakeProf)
print("6. Total Profit on in Percentage =", (BlackForestProf / BlackForestInvtCost * 100), (VenillaCakeProf/VenillaCakeInvtCost * 100 ), (RedVelvetProf / RedVelvetInvtCost * 100 ), (LemonSpongeProf / LemonSpongeInvtCost * 100), (ChocolateCakeProf/ChocolateCakeInvtCost * 100))





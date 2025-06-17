# Naam van de auteur: Jaïr Lijkwan
# Doel van het programma: Leeftijdberekening: Het programma vraagt de naam van de gebruiker (user) en stopt dit in een variabele. 
# Vervolgens vraagt het programma het geboortejaar van deze gebruiker en leest deze in.
# Bereken de leeftijd van de persoon en drukt deze af.
# Tot slot: Berekent het programma de leeftijd af in "Venusjaren".

# Vraag de naam van een persoon en lees deze in een variabele genaamd "naam"
naam = input("Hoe heet je? ")

# Vraag het geboortejaar van de persoon en lees deze in een variabele genaamd "geboortejaar"
geboortejaar = int(input("Wat is je geboortejaar? "))

# huidige jaartal
huidige_jaartal = 2020

# Berekenen van de leeftijd van de gebruiker wordt gedaan door huidige jaartal min geboortejaar te berekenen.
leeftijd = huidige_jaartal - geboortejaar

# Drukt de leeftijd van de persoon af op aarde
print("Beste " + naam + ", in "  + str(huidige_jaartal) + " zal je leeftijd op aarde " + str(leeftijd) + " zijn.")

# Een venusjaar is 0.62 keer de lengte van een jaar op aarde.
venusjaren = 0.62

# De berekenings is om de leeftijd van de persoon te delen door venusjaren
berekening_leeftijd_venusjaren = leeftijd / venusjaren

# Print de gebruiker zijn leeftijd in Venusjaren
print("En je leeftijd is dan " + str(berekening_leeftijd_venusjaren) + " in Venusjaren.")
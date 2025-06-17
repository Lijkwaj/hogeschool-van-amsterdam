# Naam van de auteur: Jaïr Lijkwan
# Doel van het programma: BMI berekenen: Het programma berekent de BMI (Body Mass Index) van de gebruiker. 
# Het programma vraagt het gewicht van de gebruiker in kilogram en leest deze in.
# Het programma vraagt vervolgens de lenget van de gebruiker in centimenters (cm) en leest deze in.
# Hierbij berekent het programma de BMI van de gebruiker en drukt deze af.

# Vraagt de gebruiker naar gewicht in kilogram (kg)
gewicht_kg = float(input("Gewicht in kilogram : "))

# Vraagt de gebruiker naar lenget in centimers (cm)
lengte_cm = int(input("Lengte in centimeter: "))

# Lengte in centimer omzetten in meters.
lengte_m = lengte_cm / 100

# Berekening bmi alternatief bmi = gewicht_kg / lengte_m ** 2
bmi = gewicht_kg / (lengte_m * lengte_m)

# Drukt BMI af van de gebruiker
print("BMI: " + str(bmi))
# Aanmaken van een lijst
dieren = ['hond', 'kat', 'vogel', 'cavia', 'slang']  # Maak de lijst dieren

# Print de volledige lijst
print("Volledige lijst van dieren:", dieren)

print()

# Print het eerste en laatste dier in de lijst
print("Eerste dier:", dieren[0])
print("Laatste dier:", dieren[-1])

print()
# Toevoegen en verwijderen van elementen uit de lijst
dieren.append('hamster')  # Voeg 'hamster' toe aan het einde van de lijst
dieren.insert(1, 'konijn')  # Voeg 'konijn' op de tweede positie in de lijst toe
dieren.remove('vogel')  # Verwijder 'vogel' uit de lijst

print()
# Print de aangepaste lijst
print("Aangepaste lijst van dieren:", dieren)

print()
# Verwijderen en verplaatsen van elementen uit de lijst met pop
del dieren[2]  # Verwijder 'kat' met de del-statement
print("Lijst na verwijderen van 'kat':", dieren)

print()
# Verplaats het laatste dier naar een nieuwe lijst
verkocht_dier = dieren.pop()  # Verwijder het laatste dier en sla het op
print(f"Verkocht dier: {verkocht_dier.title()}.")
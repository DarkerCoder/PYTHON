# Write a program to fill in a letter template given below with name and date
# Letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>'''

Letter = '''
Dear <|Name|>,
 You are selected!
<|Date|>'''

Letter = Letter.replace("Name", "Pradip")
Letter = Letter.replace("Date", "29 June,2024")
# Letter = Letter.replace("Name", "Pradip").replace("Date", "29 June,2024")

print(Letter)

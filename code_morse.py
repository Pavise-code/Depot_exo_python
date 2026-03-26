#Dans ce kata, il faut écrire un simple décodeur en code Morse.
#Le code Morse encode chaque caractère sous forme d’une séquence de « points » et de « tirets ». 
#Le code Morse est insensible à la majuscule, traditionnellement on utilise des majuscules.
#Lorsque le message est écrit en code Morse, 
  # un seul espace est utilisé pour séparer les codes de caractères 
  # et 3 espaces sont utilisés pour séparer les mots. 
  # Par exemple, le message en code Morse est .A·−Q−−·−1·−−−−HEY JUDE···· · −·−−   ·−−− ··− −·· 
#REMARQUE : Les espaces supplémentaires avant ou après le code n’ont aucun sens et doivent être ignorés.
#il existe des codes de service spéciaux, le plus notoire étant le signal de détresse international SOS = ···−−−···
  # Ces codes spéciaux sont traités comme des caractères spéciaux uniques, 
  # et sont généralement transmis comme des mots séparés.
#########
# Votre tâche est d’implémenter une fonction qui prendrait le code Morse en entrée 
  # et retournerait une chaîne décodée lisible par l’humain.
# Par exemple :
# decode_morse('.... . -.--   .--- ..- -.. .')
# #should return "HEY JUDE"
##########
# REMARQUE : Pour le codage, il faut utiliser des caractères ASCII et , et non des caractères Unicode..-
# il exeiste je crois une table des codes Morse préchargée comme dictionnaire. A chercher !!sinon utiliser dic_MORSE_CODE{}

# Define Morse code mapping manually
dic_MORSE_CODE = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
    "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
    "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
    ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
    "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
    "--..": "Z",
    "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
    ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",
    ".-.-.-": ".", "--..--": ",", "..--..": "?", "-.-.--": "!",
    "-....-": "-", "-..-.": "/", ".--.-.": "@", "-.--.": "(", "-.--.-": ")"
}

#SOLUTION
morseCode = ".... .   .--." #(H E [3 espaces] P)
def decodeMorse(morseCode):
    CHARS = " "
    WORDS = "   "
    lst = []
    for word in morseCode.strip().split(WORDS):
        wordLst = []
        for character in word.split(CHARS):
            wordLst.append("".join(dic_MORSE_CODE[character]))
        lst.append("".join(wordLst))
    print(" ".join(lst))
    #return " ".join(lst)

decodeMorse(morseCode)

# Exemple de "voyage" d'un message :
# Entrée : ".... .   .--. (H E [3 espaces] P)
# split("   ") crée : ['.... .', '.--.'] (Deux blocs de mots).
# 1er tour de boucle : word vaut ".... .".
# wordLst est créé vide [].
# word.split(" ") crée ['....', '.'].
# On traduit et on remplit wordLst -> ['H', 'E'].
# On colle wordLst -> "HE".
# On range dans lst -> ['HE'].
# 2ème tour de boucle : word vaut ".--.".
# wordLst est recréé vide [].
# On traduit -> ['P'].
# On colle -> "P".
# On range dans lst -> ['HE', 'P'].
# Fin : " ".join(['HE', 'P']) donne "HE P".
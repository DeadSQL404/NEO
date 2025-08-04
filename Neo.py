import speech_recognition as sr

def ecouter_et_detecter():
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 1  # tolérance entre les mots
    with sr.Microphone() as source:
        print("Assistant en veille... Dites 'Linux' pour l'activer.")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # filtre bruit ambiant
        audio = recognizer.listen(source)
        try:
            texte = recognizer.recognize_google(audio, language="fr-FR")
            print("Vous avez dit :", texte)
            if "linux" in texte.lower():
                print("✅ Assistant activé")
                return True
            else:
                print("❌ Mot-clé non détecté")
        except sr.UnknownValueError:
            print("❌ Je n'ai pas compris.")
        except sr.RequestError:
            print("❌ Erreur avec le service de reconnaissance vocale.")

    return False

# Lancement du test
if ecouter_et_detecter():
    print("➡️ On peut maintenant passer à l'étape suivante.")
else:
    print("🔁 Relancez et réessayez.")

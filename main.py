import time # Dodaj to na samej górze plikuc
import os
import speech_recognition as sr
from groq import Groq
from github import Github, Auth
from gtts import gTTS
import pygame # do odtwarzania dźwięku

# --- KONFIGURACJA ---
GROQ_API_KEY = "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".strip()
GITHUB_TOKEN = "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".strip()
REPO_NAME = "AI_Nauczyciel_Programowania_z_GitHubem"

# Inicjalizacja klientów
client = Groq(api_key=GROQ_API_KEY)
auth = Auth.Token(GITHUB_TOKEN)
g = Github(auth=auth)

pygame.mixer.init()

def mow(tekst):
    """Generuje głos za pomocą gTTS i odtwarza go."""
    print(f"Mentor: {tekst}")
    tts = gTTS(text=tekst, lang='pl')
    tts.save("output.mp3")
    
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    pygame.mixer.music.unload() # Zwolnienie pliku

def sluchaj():
    recognizer = sr.Recognizer()
    # Te dwie linie poniżej sprawią, że mikrofon nie będzie tak czuły na krótkie pauzy
    recognizer.pause_threshold = 2.0  # Czeka 2 sekundy ciszy zanim uzna, że skończyłeś
    recognizer.operation_timeout = None
    
    with sr.Microphone() as source:
        print("\nSłucham... (mów śmiało, czekam)")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        # Zwiększamy czas nagrywania do 15 sekund
        audio = recognizer.listen(source, timeout=None, phrase_time_limit=15)
    
    try:
        wynik = recognizer.recognize_google(audio, language="pl-PL")
        return wynik
    except:
        return ""



def zapisz_na_github(tytul, kod, opis):
    try:
        user = g.get_user()
        login = user.login
        
        try:
            repo = user.get_repo(REPO_NAME)
        except:
            repo = user.create_repo(REPO_NAME)
            
        # Dodajemy unikalny numer (timestamp), żeby uniknąć błędu "sha"
        znacznik = int(time.time())
        bezpieczna_nazwa = tytul.lower().replace(" ", "_")
        sciezka_kod = f"{bezpieczna_nazwa}/kod_{znacznik}.py"
        sciezka_notatki = f"{bezpieczna_nazwa}/notatki_{znacznik}.md"
        
        repo.create_file(sciezka_kod, f"Lekcja: {tytul}", kod)
        repo.create_file(sciezka_notatki, f"Notatki: {tytul}", opis)
        
        url = f"https://github.com/{login}/{REPO_NAME}"
        return f"SUKCES! Nowa lekcja zapisana. Link: {url}"
    except Exception as e:
        return f"Błąd GitHuba: {e}"

def mentor_ai():
    system_prompt = (
    "Jesteś precyzyjnym robotem-nauczycielem Pythona. "
    "Kiedy użytkownik prosi o ZAPISANIE lekcji, Twoim JEDYNYM zadaniem jest wypisanie "
    "poniższego formatu bez żadnego dodatkowego tekstu przed lub po: "
    "ZAPISZ_LEKCJE|Tytuł|Kod_Pythona|Krótki_Opis_Markdown"
    )
    historia = [{"role": "system", "content": system_prompt}]
    
    mow("Cześć! Tu Twój mentor na Groq Cloud. Co dzisiaj kodujemy?")

    while True:
        pytanie = sluchaj()
        if not pytanie: continue
        print(f"Ty: {pytanie}")

        if "koniec" in pytanie.lower():
            mow("Do zobaczenia!")
            break

        historia.append({"role": "user", "content": pytanie})
        
        # Wywołanie Groq (Model Llama 3)
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant", # To jest aktualny, bardzo szybki model
            messages=historia
        )
        
        odpowiedz = completion.choices[0].message.content

        # Logika automatycznego zapisu na GitHub - ulepszona
        # Szukamy słowa kluczowego, nawet jeśli AI coś dopisało przed nim
        if "ZAPISZ_LEKCJE" in odpowiedz:
            # Tniemy tekst od momentu znalezienia słowa kluczowego
            fragment_do_zapisu = odpowiedz.split("ZAPISZ_LEKCJE")[1]
            czesci = fragment_do_zapisu.split("|")
            
            if len(czesci) >= 4:
                tytul = czesci[1].strip()
                kod = czesci[2].strip()
                opis = czesci[3].strip()
                
                status_github = zapisz_na_github(tytul, kod, opis)
                mow(status_github)
            else:
                mow("Słyszę prośbę o zapis, ale format jest niepełny. Powtórz proszę.")

if __name__ == "__main__":
    mentor_ai()

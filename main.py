import time # Dodaj to na samej górze plikuc
import os
import speech_recognition as sr
from groq import Groq
from github import Github, Auth
from gtts import gTTS
import pygame # do odtwarzania dźwięku
import re
import keyboard
import pygame

# --- KONFIGURACJA ---
GROQ_API_KEY = "gsk_".strip()
GITHUB_TOKEN = "ghp_".strip()
REPO_NAME = "AI_Nauczyciel_Programowania_z_GitHubem"

# Inicjalizacja klientów
client = Groq(api_key=GROQ_API_KEY)
auth = Auth.Token(GITHUB_TOKEN)
g = Github(auth=auth)

pygame.mixer.init()


def mow(tekst):
    """Czyści tekst i odtwarza go, pozwalając na przerwanie spacją."""
    # 1. Czyszczenie tekstu (Twoje sprawdzone reguły)
    tekst_do_czytania = tekst.replace("`", "").replace("#", "").replace("*", "")
    tekst_do_czytania = re.sub(r'[^\w\s,.;:!?()\-ąćęłńóśźżĄĆĘŁŃÓŚŹŻ]', '', tekst_do_czytania)
    
    print(f"Mentor: {tekst}") 
    
    if tekst_do_czytania.strip():
        # 2. Generowanie mowy
        tts = gTTS(text=tekst_do_czytania, lang='pl')
        tts.save("output.mp3")
        
        # 3. Odtwarzanie z kontrolą przerwania
        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()
        
        print(">>> [INFO] Naciśnij SPACJĘ, aby przerwać i zadać pytanie...")
        
        while pygame.mixer.music.get_busy():
            # Sprawdzamy, czy Damian nacisnął spację
            if keyboard.is_pressed('space'):
                pygame.mixer.music.stop() # Wyłączamy dźwięk
                print("\n[SYSTEM] Przerwano odtwarzanie. Słucham Cię, Damian!")
                break 
            continue
            
        pygame.mixer.music.unload()

def sluchaj():
    recognizer = sr.Recognizer()
    
    # --- PARAMETRY CZUŁOŚCI ---
    recognizer.dynamic_energy_threshold = True 
    recognizer.pause_threshold = 4.0          # Czeka 3.5s ciszy przed końcem nagrania
    recognizer.non_speaking_duration = 1.0    # Zwiększamy czas na 'oddech' wewnątrz słowa
    recognizer.phrase_threshold = 0.1         # Minimalny czas mowy
    
    with sr.Microphone() as source:
        print("\n[SYSTEM] Kalibracja szumów (zachowaj ciszę)...")
        recognizer.adjust_for_ambient_noise(source, duration=1.0)
        
        print(">>> Mów teraz, Damian! Słucham...")
        try:
            # Słuchamy przez max 20 sekund jednej wypowiedzi
            audio = recognizer.listen(source, timeout=7, phrase_time_limit=20)
            
            print("[SYSTEM] Rozpoznawanie...")
            wynik = recognizer.recognize_google(audio, language="pl-PL")
            return wynik
        except sr.WaitTimeoutError:
            print("[SYSTEM] Cisza... nikt nic nie powiedział.")
            return ""
        except Exception as e:
            print(f"[SYSTEM] Nie zrozumiałem: {e}")
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
    "Jesteś Surowym Mentorem Programowania. Twoim uczniem jest Damian. "
    "ZASADA NR 1: Nigdy nie lej wody. Piszesz konkretnie i technicznie. UŻYWAJ WYŁĄCZNIE JĘZYKA PYTHON. Zakaz używania składni C/C++. Kod musi być gotowy do wklejenia do pliku .py i uruchomienia."
    "ZASADA NR 2: W sekcji 'Szczegółowy_Opis' musisz napisać minimum 15 długich, ponumerowanych zdań. "
    "Jeśli opis będzie bełkotem lub będzie krótki, Damian uzna, że Twój procesor uległ awarii. "
    "STRUKTURA NOTATKI .md: "
    "## 🧠 Dogłębna Teoria (min. 5 zdań o tym jak działa stos wywołań) "
    "## 🚀 Analiza Systemu Rakietowego (min. 5 zdań o lądowaniu) "
    "## 🛠️ Misje Bojowe (Musisz podać DOKŁADNIE 3 trudne zadania z opisem danych wejściowych i oczekiwanego wyniku)."
    "3. INTELIGENCJA SŁUCHU: Damian uczy się Pythona. Jeśli usłyszysz 'bajka', 'pajton', 'fajton' – to znaczy PYTHON. Jeśli usłyszysz 'ich' lub 'iv' – to znaczy IF. Jeśli powie 'elsy' – to znaczy ELSE. Zawsze interpretuj mowę Damiana w kontekście programowania i rakiet SpaceX."
    "5. FORMAT ZAPISU: Jeśli Damian użyje słowa 'GitHub', 'zapisz' lub 'lekcja', TWOIM ABSOLUTNYM OBOWIĄZKIEM jest dodanie na samym końcu odpowiedzi frazy: ZAPISZ_LEKCJE|Tytuł|Kod|Szczegółowy_Opis. Bez tego tagu Damian straci dostęp do lekcji!"
)
    historia = [{"role": "system", "content": system_prompt}]
    
    mow("Cześć Damian!! Tu Twój mentor na Groq Cloud. Co dzisiaj kodujemy?")

    while True:
        pytanie = sluchaj()
        if not pytanie: continue
        print(f"Ty: {pytanie}")

        if "wyłącz" in pytanie.lower() or "koniec" in pytanie.lower():
            mow("Jasne Damian! Wyłączam się.")
            break # To zatrzyma program natychmiast

        historia.append({"role": "user", "content": pytanie})
        
        # Wywołanie Groq (Model Llama 3)
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=historia,
            temperature=0.1,  # Rygor: Mentor trzyma się faktów i zasad
            max_tokens=4096   # Przestrzeń: 70b potrzebuje miejsca na długi opis i kod
        )
        
        odpowiedz = completion.choices[0].message.content

        # Logika automatycznego zapisu na GitHub - ulepszona
        # Szukamy słowa kluczowego, nawet jeśli AI coś dopisało przed nim
        # Reagujemy TYLKO jeśli AI faktycznie wygenerowało pełny format
        # Reagujemy TYLKO jeśli AI faktycznie wygenerowało pełny format
        # --- LOGIKA DECYZJI O ZAPISIE ---
        # Sprawdzamy, czy w Twoim pytaniu padło słowo sugerujące chęć zapisu
        slowa_klucze = ["zapisz", "lekcja", "notatka", "github", "archiwizuj"]
        uzytkownik_chce_zapisac = any(s in pytanie.lower() for s in slowa_klucze)

        # Reagujemy TYLKO jeśli Ty chciałeś zapisu ORAZ AI wygenerowało poprawny format
        # --- LOGIKA DECYZJI O ZAPISIE (Uproszczona i Pewna) ---
        # Sprawdzamy tylko, czy Mentor wygenerował tag zapisu. 
        # Nie obchodzi nas już, czy Google dobrze usłyszało słowo "GitHub".
        if "ZAPISZ_LEKCJE|" in odpowiedz:
            print("[SYSTEM] Wykryto instrukcję zapisu! Łączę z GitHubem...")
            fragmenty = odpowiedz.split("ZAPISZ_LEKCJE|")
            
            # Czytamy tylko tekst PRZED tagiem, żeby Mentor go wypowiedział
            czysta_odpowiedz = fragmenty[0].strip()
            mow(czysta_odpowiedz)
            
            # Przetwarzamy części do zapisu
            for f in fragmenty[1:]:
                czesci = f.split("|")
                if len(czesci) >= 3:
                    tytul = czesci[0].strip()
                    kod = czesci[1].strip()
                    opis = czesci[2].strip()
                    
                    status = zapisz_na_github(tytul, kod, opis)
                    mow(status) # Mentor powie "Sukces, zapisano!"
        else:
            # Jeśli w odpowiedzi nie ma tagu, po prostu przeczytaj co napisał Mentor
            mow(odpowiedz.strip())

if __name__ == "__main__":
    mentor_ai()

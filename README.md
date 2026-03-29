# 🎙️ Mentor AI: Głosowy Asystent Nauki Pythona

Ten projekt to inteligentny asystent głosowy, który nie tylko uczy programowania, ale automatycznie dokumentuje moje postępy na GitHubie. System wykorzystuje model **Llama 3** (via Groq Cloud) do generowania lekcji oraz interfejs głosowy do interakcji.

## 🚀 Jak to działa?
1. **Rozmawiam z Mentorem** – Zadaję pytania o Pythona głosem.
2. **AI Generuje Wiedzę** – Mentor tłumaczy zagadnienie i przygotowuje przykład kodu.
3. **Automatyczny Zapis** – Po wydaniu komendy, bot tworzy folder, plik `.py` z kodem oraz notatki `.md` bezpośrednio w tym repozytorium.

## 🛠️ Technologia
* **Język:** Python 3.12.9
* **Mózg AI:** Groq Cloud API (Model: `llama-3.1-8b-instant`)
* **Głos (TTS):** gTTS (Google Text-to-Speech)
* **Słuch (STT):** SpeechRecognition (Google API)
* **Integracja:** PyGithub (Automatyczne commity i tworzenie plików)

## 📂 Struktura Repo
Lekcje są zapisywane w osobnych folderach z unikalnymi znacznikami czasu:
- `nazwa_lekcji/kod_12345.py` - Czysty kod do uruchomienia.
- `nazwa_lekcji/notatki_12345.md` - Wyjaśnienie teorii i zadań.

---

## 🗺️ Mapa Drogowa Nauki (Postęp)
- [ ] 01. Wstęp i print()
- [ ] 02. Zmienne i Typy Danych
- [ ] 03. Operatory Matematyczne
- [ ] 04. Pobieranie danych (input)
- [ ] 05. Instrukcje Warunkowe (if/else)
- [ ] ... (i kolejne etapy)

---

## 🔧 Instalacja i Uruchomienie
Aby odpalić projekt u siebie:
1. Sklonuj repozytorium.
2. Zainstaluj biblioteki: `pip install groq PyGithub gTTS pygame speechrecognition`.
3. Wstaw swoje klucze API (`GROQ_API_KEY`, `GITHUB_TOKEN`) w pliku `main.py`.
4. Uruchom: `python main.py`.

---
*Projekt stworzony przez Damian4578 w ramach nauki automatyzacji i sztucznej inteligencji.*

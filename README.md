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
# 🗺️ Mapa Drogowa Nauki Pythona (Postęp)

Ten plik służy do śledzenia moich postępów w nauce. Każdy punkt to kolejna lekcja, którą Mentor AI wygenerował i zapisał w tym repozytorium.

---

## 🟢 ETAP 1: Fundamenty (Zrozumienie bazy)
- [ ] **Lekcja 01: Wstęp i Funkcja `print()`** *Cel: Wyświetlanie komunikatów w konsoli.*
- [ ] **Lekcja 02: Zmienne i Typy Danych** *Cel: Przechowywanie liczb (int, float) i tekstu (str).*
- [ ] **Lekcja 03: Operatory Matematyczne** *Cel: Podstawowe obliczenia i operacje logiczne.*
- [ ] **Lekcja 04: Interakcja (`input`)** *Cel: Pobieranie danych od użytkownika w czasie rzeczywistym.*

---

## 🟡 ETAP 2: Sterowanie Programem (Logika)
- [ ] **Lekcja 05: Instrukcje Warunkowe (`if`, `elif`, `else`)** *Cel: Tworzenie programów podejmujących decyzje.*
- [ ] **Lekcja 06: Pętla `while`** *Cel: Powtarzanie kodu, dopóki warunek jest spełniony.*
- [ ] **Lekcja 07: Pętla `for`** *Cel: Automatyzacja zadań na zbiorach danych.*
- [ ] **Lekcja 08: Obsługa Błędów (`try`, `except`)** *Cel: Zapobieganie "wybuchaniu" programu przy błędach.*

---

## 🔵 ETAP 3: Przechowywanie Danych (Kolekcje)
- [ ] **Lekcja 09: Listy (`list`)** *Cel: Zarządzanie wieloma elementami w jednej zmiennej.*
- [ ] **Lekcja 10: Krotki i Zbiory (`tuple`, `set`)** *Cel: Praca z danymi niezmiennymi i unikalnymi.*
- [ ] **Lekcja 11: Słowniki (`dict`)** *Cel: Przechowywanie danych w parach klucz-wartość.*

---

## 🟣 ETAP 4: Funkcje i Moduły (Porządek)
- [ ] **Lekcja 12: Funkcje (`def`)** *Cel: Pisanie kodu wielokrotnego użytku.*
- [ ] **Lekcja 13: Moduły i Biblioteki** *Cel: Korzystanie z gotowych narzędzi Pythona.*
- [ ] **Lekcja 14: Praca z plikami** *Cel: Zapisywanie i odczytywanie danych z dysku.*

---

## 🔴 ETAP 5: Zaawansowane (OOP)
- [ ] **Lekcja 15: Podstawy Klas i Obiektów** *Cel: Modelowanie rzeczywistych obiektów w kodzie.*

---
*Ostatnia aktualizacja: March 2026*

---

## 🔧 Instalacja i Uruchomienie
Aby odpalić projekt u siebie:
1. Sklonuj repozytorium.
2. Zainstaluj biblioteki: `pip install groq PyGithub gTTS pygame speechrecognition`.
3. Wstaw swoje klucze API (`GROQ_API_KEY`, `GITHUB_TOKEN`) w pliku `main.py`.
4. Uruchom: `python main.py`.

---
*Projekt stworzony przez Damian4578 w ramach nauki automatyzacji i sztucznej inteligencji.*

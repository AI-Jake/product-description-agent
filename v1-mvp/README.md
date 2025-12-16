\# Product Description Agent - V1 MVP



Generator opisów produktów dla Allegro w języku polskim.



\## 🎯 Co to robi?



Generuje profesjonalne opisy produktów dla platformy Allegro:

\- Tytuł (max 50 znaków)

\- Opis (100-150 słów)

\- 5 punktów z korzyściami

\- Słowa kluczowe



\## 📋 Wymagania



\- Python 3.7+

\- Konto Claude Pro (do manualnego workflow)



\## 🚀 Jak używać?



\### Krok 1: Uruchom skrypt



```bash

python agent.py

```



\### Krok 2: Wprowadź informacje o produkcie



Skrypt zapyta o:

\- Nazwę produktu

\- Cechy produktu (lista)

\- Grupę docelową (opcjonalnie)



\### Krok 3: Skopiuj prompt



Skrypt wygeneruje prompt. Skopiuj go.



\### Krok 4: Wklej do Claude.ai



1\. Otwórz https://claude.ai

2\. Wklej prompt

3\. Poczekaj na odpowiedź Claude

4\. Skopiuj całą odpowiedź



\### Krok 5: Wklej odpowiedź z powrotem



Wklej odpowiedź Claude do skryptu (zakończ wpisując KONIEC)



\### Krok 6: Gotowe!



Skrypt sformatuje opis, możesz go zapisać do pliku lub skopiować.



\## 📝 Przykład użycia



```

Nazwa produktu: Bidon stalowy 750ml

Cechy:

&nbsp; 1. Izolacja termiczna 24h

&nbsp; 2. BPA Free

&nbsp; 3. Szczelny

&nbsp; 4. Szeroka nakrętka

&nbsp; 5. Antypoślizgowy

Grupa docelowa: Osoby aktywne, siłownia



→ Generuje gotowy opis do Allegro

```



\## ✅ Cechy V1



\- ✅ Polski język (native)

\- ✅ Format Allegro (tytuł 50 znaków)

\- ✅ Anty-szablonowe słownictwo

\- ✅ Konwersacyjny ton

\- ✅ Optymalizacja pod mobile

\- ✅ Emoji (popularne na Allegro)

\- ✅ Zapisywanie do pliku



\## 🔮 Roadmap



\### V2 (Planowane)

\- Automatyzacja z API

\- Batch processing (wiele produktów)

\- Więcej platform (Amazon, Shopify)



\### V3 (Przyszłość)

\- Multi-język (niemiecki, angielski)

\- Badanie konkurencji

\- SEO optimization

\- Plagiarism checking



\## 📂 Struktura plików



```

v1-mvp/

├── agent.py           # Główny skrypt

├── prompts.py         # Szablony promptów

├── requirements.txt   # Zależności (brak w V1)

└── README.md         # Ta instrukcja

```



\## 💡 Tips



\### Dla lepszych opisów:

\- Podawaj konkretne cechy (nie "ładny" ale "kolor niebieski")

\- Używaj liczb (nie "długo trzyma" ale "24 godziny")

\- Myśl o korzyściach, nie tylko cechach



\### Dla szybszej pracy:

\- Przygotuj listę cech przed uruchomieniem

\- Zachowaj szablon odpowiedzi Claude

\- Edytuj opis przed publikacją na Allegro



\## 🐛 Troubleshooting



\*\*Problem:\*\* "No module named 'prompts'"

\*\*Rozwiązanie:\*\* Upewnij się, że jesteś w folderze v1-mvp



\*\*Problem:\*\* "Tytuł za długi"

\*\*Rozwiązanie:\*\* Skróć nazwę produktu lub usuń mniej ważne słowa



\*\*Problem:\*\* "Znaleziono zakazane słowa"

\*\*Rozwiązanie:\*\* To słowa-szablony AI. Poproś Claude o regenerację.



\## 📞 Support



Masz problem? Chcesz coś poprawić?

\- Sprawdź kod w `agent.py` i `prompts.py`

\- Wszystkie promptы są edytowalne w `prompts.py`



\## 📄 License



MIT - Użyj jak chcesz, rozwijaj jak chcesz.



---



\*\*Version:\*\* 1.0.0  

\*\*Date:\*\* December 16, 2024  

\*\*Author:\*\* AI-Jake  

\*\*Platform:\*\* Allegro (Polish market)


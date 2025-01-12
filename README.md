# Problema Rucsacului - Knapspack Problem

## Timp de rezolvare

A durat aproximativ o zile calendaristice pentru a implementa această soluție pentru problema rucsacului, incluzând timpul necesar pentru generarea testelor, implementarea algoritmilor și crearea automatizărilor cu Makefile. Pe parcursul dezvoltării, am utilizat Git pentru a sincroniza munca și a păstra o copie de rezervă a progresului.

> **NOTE:** Acest proces m-a ajutat să exersez utilizarea Git și să consolidez cunoștințele despre managementul proiectelor software. De asemenea, am devenit mai confortabil cu organizarea și testarea proiectelor complexe.

## Conținutul Arhivei
Această arhivă conține implementarea unei soluții pentru problema rucsacului (**Knapsack Problem**) și un generator de teste automate pentru evaluare. Fișierele incluse sunt:

1. **`generate_data.py`**: Script Python pentru generarea testelor de intrare. Creează fișiere de test cu diverse configurații pentru a evalua performanța algoritmilor propuși.
2. **`knapsack.py`**: Script Python care implementează soluțiile pentru problema rucsacului folosind trei metode:
   - **Backtracking**: Soluție exactă, dar lentă pentru cazuri mari.
   - **Programare Dinamică**: Soluție optimă și eficientă din punct de vedere al timpului, dar consumatoare de memorie pentru cazuri mari.
   - **Euristică Greedy**: Soluție aproximativă, rapidă dar posibil suboptimă.
3. **`Makefile`**: Automatizează generarea datelor și rularea soluțiilor. Include reguli pentru:
   - `make`: Rularea regulii implicite `build`.
   - `make build`: Rulează secvențial `generate_data.py` și `knapsack.py`.
   - `make clean`: Șterge testele generate anterior.

> ***NOTE:*** Arhiva este organizată pentru a facilita atât generarea testelor, cât și rularea automată a soluțiilor.

## Cum se pot evalua soluțiile

1. **Generarea testelor**:
   - Rulează comanda `make` sau `make build` pentru a genera datele de test folosind `generate_data.py` și pentru a executa soluțiile implementate în `knapsack.py`.
   - Testele sunt salvate în directorul `knapsack_tests`.

2. **Rularea soluțiilor**:
   - Fiecare test din directorul `knapsack_tests` este procesat în ordine numerică (`test_1.txt`, `test_2.txt`, etc.).
   - Rezultatele sunt afișate în terminal pentru fiecare test și fiecare metodă (Backtracking, Programare Dinamică, Greedy).

3. **Curățarea datelor**:
   - Rulează `make clean` pentru a șterge fișierele generate în timpul testării.

## Surse externe utilizate

1. **Algoritmi și structuri de date**:
   - Documentație standard Python: [https://docs.python.org/](https://docs.python.org/)
   - Articole despre problema rucsacului:[Google Knapspack Progblem](https://developers.google.com/optimization/pack/knapsack), [Geeks for Geeks](https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/), [W3Schools](https://www.w3schools.com/dsa/dsa_ref_knapsack.php).

2. **Asistență AI**:
   - OpenAI ChatGPT: Pentru clarificări, sugestii și optimizarea codului. Nu s-au utilizat fragmente directe de cod fără ajustări specifice pentru acest proiect.

3. **Sisteme de build și automatizare**:
   - Referințe pentru scrierea de Makefile-uri eficiente: GNU Make Documentation.

## Observații finale

- Asigurați-vă că aveți instalat Python 3 și utilitarul `make` pe sistemul dumneavoastră.
- Dacă întâmpinați probleme, verificați dependențele și permisiunile pentru directoarele generate.

Pentru întrebări suplimentare, contactați autorul arhivei.


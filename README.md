# Základy jazyka Python — Priebežné zadania (VV1)

Tento repozitár obsahuje týždenné mini-úlohy pre predmet Základy jazyka Python.
Každý týždeň má 5 úloh, termín odovzdania je 1 týždeň.

## Štruktúra
- `course/week01` až `course/week10`: zadania a šablóny riešení
- `tests/week01` až `tests/week10`: testy pre úlohy
- `scripts/run_tests.py`: skript na spúšťanie testov
- `conftest.py`: sumarizácia bodov VV1 pri spustení `pytest`
- `requirements.txt`: balíky potrebné pre lokálne spustenie

## Ako študent pracuje
- Študent upravuje iba riešenia v súboroch `course/weekXX/taskYY.py`.
- Názvy súborov, funkcií, tried a metód musia zostať presne podľa šablóny.
- Testy v priečinku `tests/` sa nemenia.

## Spustenie testov
Použitie:
`python scripts/run_tests.py --week 01`

Skript spustí testy iba pre zvolený týždeň a vypíše počet úspešných a neúspešných testov.

Spustenie všetkých týždňov (odporúčané pre študenta):
`pytest`

Na konci výpisu sa zobrazí sumarizácia bodov VV1, napr.:
- `Splnené úlohy v tomto behu: 17 z 50`
- `Body (VV1): 17 / 50`

Spustenie jedného týždňa cez `pytest`:
`pytest tests/week03`

Ak príkaz `pytest` nie je dostupný v PATH, použite:
`python -m pytest`

## Požiadavky
- Anaconda (Python 3.x)
- Balíky: `matplotlib`, `numpy`, `pandas`, `scipy` (súčasť Anaconda)
- `pytest` (bežne dostupný v Anaconda prostredí)

## Práca s Anaconda prostredím (odporúčaný postup)
### Prečo vytvárať samostatné prostredie
- Izolácia závislostí: balíky pre tento predmet sa nemiešajú s inými projektmi.
- Reprodukovateľnosť: študent, učiteľ aj testovacie PC môžu mať rovnaké verzie balíkov.
- Jednoduchšia diagnostika chýb: je jasné, v akom prostredí sa test spúšťa.
- Bezpečný reset: pri probléme sa prostredie dá zmazať a vytvoriť znova bez poškodenia `base`.

### 1. Zobrazenie existujúcich prostredí
Použite jeden z príkazov:
- `conda env list`
- `conda info --envs`

Ako zistiť aktívne prostredie:
- v zozname je označené hviezdičkou `*`
- v termináli býva prefix, napr. `(zjp-vv1)`

### 2. Vytvorenie nového prostredia pre predmet
Odporúčaný názov:
- `zjp-vv1`

Príkaz:
`conda create -n zjp-vv1 python=3.11 -y`

Prečo `python=3.11`:
- je stabilný a kompatibilný s `numpy`, `pandas`, `matplotlib`, `scipy`, `pytest`
- je vhodný pre začiatočnícke úlohy a testovanie v tomto repozitári

### 3. Aktivácia správneho prostredia
Príkaz:
`conda activate zjp-vv1`

Overenie, že ste v správnom prostredí:
- `python --version`
- `python -c "import sys; print(sys.executable)"`

### 4. Inštalácia balíkov z `requirements.txt`
Po aktivácii prostredia spustite:
- `python -m pip install --upgrade pip`
- `python -m pip install -r requirements.txt`

Prečo `python -m pip`:
- používa `pip` priamo z aktuálne aktívneho Python interpretra
- znižuje riziko, že sa balíky nainštalujú do iného prostredia

### 5. Kontrola inštalácie
Rýchla kontrola importov:
`python -c "import numpy, pandas, matplotlib, scipy; print('OK')"`

Kontrola testov:
- `python -m pytest`
- alebo `python -m pytest tests/week03`

## Ako vytvoriť vlastný `requirements.txt`
### Odporúčaný spôsob (pre projekt)
- Zapíšte iba priame závislosti projektu (napr. `pytest`, `numpy`, `pandas`, `matplotlib`, `scipy`, `jupyterlab`).
- Nepíšte tam balíky zo štandardnej knižnice (`unittest`, `random`, `os`, `sys`).
- Tento spôsob je prehľadný a ľahšie sa udržiava.

### Automatický snapshot aktuálneho prostredia
Príkaz:
`python -m pip freeze > requirements.txt`

Kedy použiť:
- ak chcete presnú kópiu prostredia (napr. pre reprodukciu chyby)

Nevýhody v Anaconda prostredí:
- súbor môže byť zbytočne dlhý
- obsahuje aj nepriamo nainštalované balíky, ktoré projekt priamo nepotrebuje

Praktické odporúčanie:
- pre bežnú výučbu udržiavajte krátky `requirements.txt` ručne
- pre archiváciu presného stavu si vytvorte napr. `requirements-lock.txt` cez `pip freeze`

## Pravidlá hodnotenia (VV1)
- 10 týždňov, 5 úloh každý týždeň
- termín odovzdania: 1 týždeň
- každá úloha = 1 bod
- maximum: 50 bodov

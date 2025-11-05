# Zadání projektu

## Základ
- Textová hra na hrdiny a jejich souboj v aréně - formát 1:1
- Programátor definuje hrdiny a ti budou mezi sebou bojovat
- Boj probíhá na kola, dokud jeden z oponentů nezemře
    - nutno kontrolovat na infinit loop
    - boj zprostředkovává aréna
    - soupeři na sebe nevidí napřímo (aby se nemohli ovlivňovat)
- Hero classes
    - warrior
    - mage
    - archer
    - healer
    - summoner?
- Skills
    - mají buď počet použití per fight
    - nebo cooldown
    - nebo casting time (wasting fight round)
    - nebo price (mana, stamina)
- Princip fungování:
    - začne souboj
    - aréna představí oba soupeře - aréna refreshen oba soupeře (aby neměly vyplýtvaný skilly…)
    - začne kolo souboje
    - aréna na prvním vypočítá útok
    - aréna na druhém vypočítá obranu
    - aréna odečte na druhém životy
    - kontrola na úmrtnost
    - aréna na druhém vypočítá útok
    - aréna na prvním vypočítá obranu
    - aréna prvnímu odečte životy
    - kontrola na úmrtnost
    - konec kola
- STAT BLOCK (range 1-10?)
    - STR - ovlivňuje close attack
    - DEX - ovlivňuje long attack
    - END - defense
    - INT - spells
    - CHA - ???

## Rozšíření pro den otevřených dveří (21-22.11.)
- Ovládání pro uživatele (hráče)
  - výběr postavy
  - rozdělení části statů uživatelem
  - manuální ovládání boje - ke zvážení
- Poskytování informací
  - ke statům
  - ke skillům/spelům
  - co se v aréně děje
  - jak "vypadá" soupeř (confused, shaken, tired, ...)

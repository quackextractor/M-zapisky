### Otázka 1

**Jaká je role aktivační funkce v neuronu?**
* a. Převádí výsledek výpočtu neuronu na jeho výstup.
* b. Rozhoduje o tom, kolik vrstev bude mít neuronová síť.
* c. Určuje počet vstupů, které neuron může přijmout.
* d. Převádí vstupní data do binárního tvaru ještě před výpočtem neuronu.

**Správná odpověď:** **a. Převádí výsledek výpočtu neuronu na jeho výstup.**

**Zdůvodnění:** Umělý neuron nejprve sečte své vstupy vynásobené příslušnými vahami a přičte zkreslení (bias). Tento mezivýsledek se pak předá aktivační funkci. Aktivační funkce jej transformuje na konečnou hodnotu, kterou neuron pošle dál jako svůj výstup. Aktivační funkce zároveň do sítě typicky vnáší nelinearitu, díky čemuž se síť může učit složité vztahy v datech. Ostatní možnosti popisují architekturu sítě nebo předzpracování dat, což není úkolem aktivační funkce.

---

### Otázka 2

**Jaká je role vstupní vrstvy v neuronové síti?**
* a. Vypočítává konečný výstup celé neuronové sítě.
* b. Určuje architekturu neuronové sítě podle typu vstupních dat.
* c. Aktualizuje váhy neuronů během procesu učení.
* d. Přijímá vstupní data a předává je dalším vrstvám sítě.

**Správná odpověď:** **d. Přijímá vstupní data a předává je dalším vrstvám sítě.**

**Zdůvodnění:** Vstupní vrstva slouží jako rozhraní mezi vnějšími daty a zbytkem neuronové sítě. Její uzly obvykle neprovádějí žádné matematické operace (nemají váhy ani aktivační funkce), pouze načtou surová data a beze změny je přepošlou do první skryté vrstvy k dalšímu zpracování.

---

### Otázka 3

**Jaký bude výstup programu?**

```python
class Neuron:
    def __init__(self, w1, w2, b, activation):
        self.w1 = w1
        self.w2 = w2
        self.b = b
        self.activation = activation

    def vypocet(self, x1, x2):
        z = x1*self.w1 + x2*self.w2 + self.b
        return self.activation(z)

def clamp(x):
    if x > 1:
        return 1
    elif x < -1:
        return -1
    else:
        return x

n = Neuron(1, 1, 0, clamp)
print(n.vypocet(1, 1))
```

* a. 2
* b. 1
* c. 0
* d. -1

**Správná odpověď:** **b. 1**

**Zdůvodnění:** Kód reprezentuje jednoduchý model neuronu. Zde je postup výpočtu krok za krokem:
1. Vytvoří se instance třídy Neuron s vahami `w1 = 1`, `w2 = 1`, zkreslením `b = 0` a aktivační funkcí `clamp`.
2. Při zavolání `n.vypocet(1, 1)` se do metody předají vstupní hodnoty `x1 = 1` a `x2 = 1`.
3. Vypočítá se vnitřní hodnota `z = (x1 * w1) + (x2 * w2) + b`, což po dosazení dává `(1 * 1) + (1 * 1) + 0`. Výsledek `z` je tedy 2.
4. Následně se na tuto hodnotu aplikuje aktivační funkce voláním `clamp(2)`.
5. Ve funkci `clamp` se vyhodnotí podmínka `x > 1`. Protože 2 je větší než 1, funkce okamžitě vrátí hodnotu 1.

---

### Otázka 4

**Jaký problém může nastat, pokud bychom kategorické proměnné reprezentovali čísly, například:**
pes = 1, kočka = 2, králík = 3

* a. Model vyžaduje více vrstev.
* b. Model může chybně interpretovat rozdíly mezi čísly jako vztah mezi kategoriemi.
* c. Model nebude možné trénovat gradientním sestupem.
* d. Neuronová síť neumí pracovat s čísly většími než 1.

**Správná odpověď:** **b. Model může chybně interpretovat rozdíly mezi čísly jako vztah mezi kategoriemi.**

**Zdůvodnění:** Pokud přiřadíme nezávislým kategoriím celá čísla, algoritmus strojového učení automaticky předpokládá matematické uspořádání a velikost. Model by z takových dat mohl vyvodit nepřesné závěry, například že králík má třikrát větší hodnotu než pes, případně že průměr ze psa a králíka je kočka. Abychom se tomuto problému vyhnuli, používá se u nezávislých kategorií technika zvaná "one-hot encoding".
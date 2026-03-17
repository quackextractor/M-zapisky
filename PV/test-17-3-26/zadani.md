**Jaká je role aktivační funkce v neuronu?**
* a. Převádí výsledek výpočtu neuronu na jeho výstup.
* b. Rozhoduje o tom, kolik vrstev bude mít neuronová síť.
* c. Určuje počet vstupů, které neuron může přijmout.
* d. Převádí vstupní data do binárního tvaru ještě před výpočtem neuronu.

**Jaká je role vstupní vrstvy v neuronové síti?**
* a. Vypočítává konečný výstup celé neuronové sítě.
* b. Určuje architekturu neuronové sítě podle typu vstupních dat.
* c. Aktualizuje váhy neuronů během procesu učení.
* d. Přijímá vstupní data a předává je dalším vrstvám sítě.

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

**Jaký problém může nastat, pokud bychom kategorické proměnné reprezentovali čísly, například:**
pes = 1, kočka = 2, králík = 3
* a. Model vyžaduje více vrstev.
* b. Model může chybně interpretovat rozdíly mezi čísly jako vztah mezi kategoriemi.
* c. Model nebude možné trénovat gradientním sestupem.
* d. Neuronová síť neumí pracovat s čísly většími než 1.
# [J. Родословная: подсчет уровней](https://contest.yandex.ru/contest/28069/problems/J/)

---
| Ограничение времени | 1 секунда |
| :--- | :--- |
| Ограничение памяти | 64Mb |
| Ввод | стандартный ввод или input.txt |
| Вывод | стандартный вывод или output.txt |
---
В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель. Каждом элементу дерева сопоставляется целое неотрицательное число, называемое высотой. У родоначальника высота равна 0, у любого другого элемента высота на 1 больше, чем у его родителя. Вам дано генеалогическое древо, определите высоту всех его элементов.

---
## Формат ввода
Программа получает на вход число элементов в генеалогическом древе N. Далее следует N-1 строка, задающие родителя для каждого элемента древа, кроме родоначальника. Каждая строка имеет вид имя_потомка имя_родителя.

## Формат вывода
Программа должна вывести список всех элементов древа в лексикографическом порядке. После вывода имени каждого элемента необходимо вывести его высоту.

---
## Пример 1

| Ввод | Вывод |
| :--- | :--- |
| 9 | Alexander_I 4 |
| Alexei Peter_I | Alexei 1 |
| Anna Peter_I | Anna 1 |
| Elizabeth Peter_I | Elizabeth 1 |
| Peter_II Alexei | Nicholaus_I 4 |
| Peter_III Anna | Paul_I 3 |
| Paul_I Peter_III | Peter_I 0 |
| Alexander_I Paul_I | Peter_II 2 |
| Nicholaus_I Paul_I | Peter_III 2 |

## Пример 2

| Ввод | Вывод |
| :--- | :--- |
| 10 | AQHFYP 3 |
| AQHFYP MKFXCLZBT | AYKOTYQ 2 |
| AYKOTYQ QIUKGHWCDC | IWCGKHMFM 1 |
| IWCGKHMFM WPLHJL | MJVAURUDN 2 |
| MJVAURUDN QIUKGHWCDC | MKFXCLZBT 2 |
| MKFXCLZBT IWCGKHMFM | PUTRIPYHNQ 2 |
| PUTRIPYHNQ UQNGAXNP | QIUKGHWCDC 1 |
| QIUKGHWCDC WPLHJL | UQNGAXNP 1 |
| UQNGAXNP WPLHJL | WPLHJL 0 |
| YURTPJNR QIUKGHWCDC | YURTPJNR 2 |

## Пример 3

| Ввод | Вывод |
| :--- | :--- |
| 10 | BFNRMLH 3 |
| BFNRMLH CSZMPFXBZ | CSZMPFXBZ 2 |
| CSZMPFXBZ IHWBQDJ | FMVQTU 9 |
| FMVQTU FUXATQUGIG | FUXATQUGIG 8 |
| FUXATQUGIG IRVAVMQKN | GNVIZ 6 |
| GNVIZ IQGIGUJZ | IHWBQDJ 1 |
| IHWBQDJ LACXYFQHSQ | IQGIGUJZ 5 |
| IQGIGUJZ JMUPNYRQD | IRVAVMQKN 7 |
| IRVAVMQKN GNVIZ | JMUPNYRQD 4 |
| JMUPNYRQD BFNRMLH |LACXYFQHSQ 0  |

---
## Примечания
Эта задача имеет решение сложности O(n), но вам достаточно написать решение сложности O(n<sup>2</sup>) (не считая сложности обращения к элементам словаря). Пример ниже соответствует приведенному древу рода Романовых.

python105

# Функции
Всичко хубаво с писането на код в ipython и времянки по един ред или малки скриптчета обаче в даден момент ще ни се наложи да преизползваме кода който вече сме писали.  
Естествения избор който ще ни дойде първи на ум ще бъде да направим copy paste на кода който сме написали.  
Е да ама не. Идеята на програмните езици е да преизползваме всичко което сме написали до сега по възможно най-оптималния начин(поне за който се сещаме в момента).  
За целта дефинираме така наречените функции. 

Ключовата дума с която правим това е **def** (от define).  
пример:  

```python
def example(param1):
    return
```

## 1. Синтаксис
Синтаксиса за дефиниране на функция е следният:  
`def <име на функция>(параметър1, параметър2, параметър3 = <стойност по подразбиране>, <параметър N>):`

Като приемлив стил и ориентир за именоване на функции и променливи хвърляме едно око на [PEP8](https://www.python.org/dev/peps/pep-0008/#function-and-variable-names) .  
За име на функция обикновено избираме кратко но достатъчно описателно име което да ни подсказва каква работа ще извършва тази функция.


### tl;dr;
Имената на функции **може да**:
* се състоят от букви - желателно е да са малки букви, но могат да бъдат всякакви. - a-z A-Z 
* да съдържат цифри след първата буква в името  
* да съдържат _ (долна черта)

Имената на функции **`не може`** да:
* започват с цифра
* бъдат запазени или ключови думи
* съдържат специални символи или оператори - напр !@#$%^&*()-+=

## 2. Параметри и аргументи
Често програмистите бъркат употребата на параметър и аргумент използвайки ги взаимозаменяемо в програмния жаргон.  
Би било добре да се прави разграничение между тях въпреки, че всеки ще ви разбере какво се опитвате да кажете когато общувате с вашите побратими в код.  
За целта ще използвам следния пример:

```python
def somefunction(firstparam, secondparam):
    return firstparam * secondparam + firstparam
    
first_argument = 100
second_argument = 300
somefunction(first_argument, second_argument)
```

Когато описваме дефиницията на функцията - след името в () скоби описваме **параметри** и техните имена.  
Когато извикваме тази функция подаваме **аргументи** на тези параметри.



## 3. Примери с функции за

### 3.1. изтриване на случаен елемент от списък
```python
from random import randint
def poprand(dataset):
    dataset.pop(randint(0,len(l)-1))
    return dataset
```
### 3.2. умножаване на елементи от числа в списък
```python
def multiplyitems(items, multiplier):
    for index,_ in enumerate(items):
        items[index] = items[index] * multiplier
    return items
```
### 3.3. създаване на списък от файлове и подреждането им по големина от директория
```python
from glob import glob
from os import stat
def fileusage(path):
    files = glob(path)
    fsizes = []
    filedata = []

    for f in files:
        fsizes.append(stat(f).st_size)
 
    for z in zip(fsizes, files):
        filedata.append(z)
    
    return filedata
```
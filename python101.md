На първата среща си говорихме за:
1. Променливите в Python
- int, float, list, tuple, лека закачка с dict

2. __str__ и различните начини за запис на текст: 
- ' ' - 'буквален' низ или literal string
- " " - string който може да бъде .format()-иран
- ''' ''' или ''' ''' - многоредов string
- f-stringове - `f' '`

3. __list__ и работа със списъци
- листовете са _mutable_ или 'променяеми'/'непостоянни' - реда и броя на техните елементи може да бъде променян
- .append() - добавяме нов елемент в края на списъка
- .extend() е същото като оператора __+=__ - добавяне на елементи от друг изброим обект
- .sort() - елементарно/вградено сортиране на списъка
- .pop() - връщане(return value) и изтриване на последния или произволен елемент в списъка
- .insert() - добавяне на елемент на произволно място в списъка спрямо index
- направихме sorted() на лист с tuples който съдържаше имена на файлове и размери на файловете

4. __tuple__ и работа с наредени n-торки
- tuples са immutable или постоянни/непроменими
- най-простата структура от данни	

5. __dict__ и работа с 'речници'/hashmap-ове
- що е то - списък с "ключове"(keys) и "стойности"(values) зад тях
- ключовете се пресмятат по предварително зададен алгоритъм който създава "еднопосочен" резултат на _произволно количество данни_ така, че когато същите данни биват пресметнати по същият алгоритъм да дават същият резултат, за да може този резултат да бъде използван за намирането на търсената стойност зад този ключ.
- .values() ни връщат списък

6. използвахме shutils, glob,  да копираме файлове за спорта

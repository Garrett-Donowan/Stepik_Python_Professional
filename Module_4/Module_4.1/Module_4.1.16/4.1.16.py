"""По чатам одного немалоизвестного мессенджера начали появляться 
новости сомнительного содержания. Оказалось, что некий молодежный клуб решил подшутить, 
распространяя всякие глупости. Однако подобное хулиганство мешает доверчивым людям, 
особенно пенсионного возраста, поэтому группа независимых программистов решила разработать бота, 
который мог бы оценить степень достоверности новости, а также отнести её к какой-либо категории.

Напишите программу, которая выводит все новости заданной категории, 
располагая их по возрастанию степени достоверности.

Формат входных данных
На вход программе подается произвольное количество строк, в каждой строке, 
кроме последней, записана новость, категория, к которой она относится, 
и ее достоверность в следующем формате:

<новость> / <категория> / <достоверность>
В последней строке подается одиночная категория.

Формат выходных данных
Программа должна вывести все новости, которые относятся к введенной категории. 
Новости должны быть расположены в порядке возрастания степени достоверности, 
а при совпадении степеней достоверности — в лексикографическом порядке самих новостей."""
import sys

news = []
raw_data = [line.strip().split(" / ") for line in sys.stdin]
for el in raw_data:
    if len(el) > 1:
        if (el[1] == raw_data[-1][0]):
            news.append([el[0], float(el[2])])
print(*(i[0] for i in sorted(news, key=lambda x: (float(x[1]), x[0]))), sep='\n')







"""Sample Input:

На рейсах Поражения второй пилот будет исполнять обязанности бортпроводника / Авиация / 0.3
Огурец исключит из своих рядов членов, не проголосовавших за Единую Арстоцку на выборах / Политика / 0.8
Орбистанские точки общепита будут закрыты для вакцинированных граждан / Общество / 0.7
Джорджи Костава получил членский билет Независимого Кобрастана / Политика / 0.0
В Колечии повысят призывной возраст до 40 лет / Политика / 1.0
Всем гражданам Антегрии въезд в Арстоцку запрещен / Политика / 0.8
Политика
Sample Output:

Джорджи Костава получил членский билет Независимого Кобрастана
Всем гражданам Антегрии въезд в Арстоцку запрещен
Огурец исключит из своих рядов членов, не проголосовавших за Единую Арстоцку на выборах
В Колечии повысят призывной возраст до 40 лет
Напишите программу. Тестируется через stdin → stdout"""
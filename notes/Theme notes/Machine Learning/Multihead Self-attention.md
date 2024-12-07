Как уже было сказано в [[Self-attention]], этап внимания позволяет определить вероятности слов для всех позиций относительно одного слова *(из-за ограничения [[Softmax]])*.

Меняя матрицы $Q, K$ и $V$ мы можем определять, относительно какого слова из входной последовательности создавать внимание.

Тогда можно просто провести процесс [[Self-attention]] $h = 8$(например) раз относительно последних $h$ слов из входной последовательности. Получим $h$ матриц формата $[n\times d_v]$, затем сконкатенируем их по второму измерению, получим матрицу формата $[n\times d_v*h]$. Дальше 
умножим эту огромную матрицу на другую, формата $[d_v*h\times d_{model}]$ (что-то типа *собирающей* матрицы). В итоге получим матрицу формата $[n\times d_{model}]$, которая отображает максимально вероятное слово, для каждой из $n$ позиций. Дальше делаем [[De-embedding]] и получаем нормальный словесный вывод.

И вот тут у нас всплывает проблема производительности. [[Self-attention]] и так занимает основную часть работы [[LLM]]'ки, а тут мы еще и хотим $h$ раз его провести. Выходом их данной сложной ситуации может быть уже известное нам проецирование слов на пространство меньшей размерности, для увеличения производительности.

Идея простая: делаем проективное пространство в $h$ раз меньше, тогда прогнать по нему [[Self-attention]] будет в $h$ раз быстрее, тогда прогнав его $h$ раз мы затратим  ресурсов столько же, сколько уходит на один проход по обычному проективному пространству размерности $d_{model}$. Тут и возникают числа $d_k$ и $d_v$. Их можно получить делением $d_{model}$ на $h$. В общем случае $d_k$ и $d_v$ не обязаны быть равными друг другу, но, например, в работе [[Attention is all you need]] они равны.

Собственно, математическая запись [[Multihead Self-attention]] такова:
$$
Multihead(Q, K, V) = Concat(head_1, head_2, \dots, head_h)\,W^0, \text{ где}
$$
$$
head_i = Attention(Q\,W^i_q, K\,W^i_k, V\, W^i_v), \text{ где}
$$
$$
	Q, K, V \in \mathbb{R}^{[n\times d_{model}]}
$$
$$
	W^i_q, W^i_k \in \mathbb{R}^{[d_{model}\times d_k]}, W^i_v \in \mathbb{R}^{[d_{model}\times d_v]}, W^0 \in \mathbb{R}^{[hd_v\times d_{model}]}
$$

Тут важное замечание, которое неявно вылезало раньше: у нас используется очень много готовых матриц, например, для составления матриц $Q, K$ и $V$, собирающей матрицы и т.д.
Всех их можно воспринимать как нейронные сети без скрытых слоев, а значит, можно обучить в процессе тренировки. Тем не менее, вероятно, есть уже обученные модели для всех этих целей. Особенно для популярных языков типа английского.


[[LLM]] [[Self-attention]] [[Multihead Self-attention]]
Данный этап в [[Transformer]]'ах предусмотрен для предотвращения появления больших значений в весах нейронок.

Обобщенный алгоритм такой:
* Все значения в матрице сдвигаются так, чтобы иметь среднее 0
* Все значения в матрице скалируются так, чтобы иметь отклонение от среднего 1

Да, это очень похоже на нормализацию стандартного распределения, где для случайной величины $X \textasciitilde N(m, \sigma)$ имеем $\frac{X-m}{\sigma} \textasciitilde N(0, 1)$

[[LLM]] [[Normalization]]
Она же карта теней. Довольно эффективный способ отрисовки теней, основанный на буфере глубины.

Идея такая, мы можем отрендерить сцену с точки зрения источника света(т.е. с его перспективно-видовой матрицей). После этого у нас в буфере глубины будут сохранены расстояния от источника света до ближайшего фрагмента(глубины). Потом при нормальном рендере для каждого фрагмента, зная его координаты, мы можем определить минимальную глубину от источника света и, сравнив с настоящей глубиной от источника света до фрагмента, выяснить -- находится он в тени(если текущая глубина больше минимальной) или на свету(в обратном случае).

Собственно, если мы обозначим вещественным числом будем обозначать "количество" тени для данного фрагмента(0 -- отсутствие тени, 1 -- полное затенение), то мы можем умножить диффузионную и бликовую составляющую света на коэффициент (1 - shadow), тем самым большей тени получаться более темные фрагменты. Фоновую компоненту света умножать не будем, т.к. она не зависит от тени и положения источника света.

При реализации возникает проблема: во время второго "обычного" рендера буфер глубины перезаписывается -- значит нам надо где-то сохранить буфер глубины. Для этой цели мы будем использовать буфер кадра([[Framebuffer]])

### Pipeline настройки фреймбуфера для хранения буфера глубины 
```C++
// Создание фреймбуфера
GLuint fbo;
glGenFramebuffers(1, &fbo);
// Создание 2d текстуры
GLuint depthTexture;
glGenTextures(1, &depthTexture);
//Привязка текстуры
glBindTexture(GL_TEXTURE_2D, depthTexture);
// Выделение памяти под текстуру
glTexImage2D(GL_TEXTURE_2D, 0, GL_DEPTH_COMPONENT, width, height, 0, GL_DEPTH_COMPONENT, GL_FLOAT, NULL);
// Установка параметров под текстуру
glTexParameteri(GL_TEXTURE_MAG_FILTER, GL_NEAREST); // как фильтровать текстуру вдали
glTexParameteri(GL_TEXTURE_MIN_FILTER, GL_NEAREST); // как фильтровать текстуру вблизи
glTexParameteri(GL_TEXTURE_WRAP_S, GL_CLAMP_TO_BORDER); // Все значения по координате s > 1 приводятся к 1
glTexParameteri(GL_TEXTURE_WRAP_T, GL_CLAMP_TO_BORDER); // Все значения по координате t > 1 приводятся к 1

// Теперь надо эту текcтуру прикрепить к буферу кадра как буфер глубины

// Привязываем буфер кадра и текстуру
glBindFramebuffer(GL_FRAMEBUFFER, fbo);
glBindTexture(GL_TEXTURE_2D, texture);

// Привязываем буфер глубины
glFramebufferTexture2D(GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, GL_TEXTURE_2D, depthTexture, 0);
// Ставим настройки того, что в буфер цвета рендера не будет
glDrawBuffer(GL_NONE);
glReadBuffer(GL_NONE);

// Отвязываем наш буфер кадра
glBindFramebuffer(GL_FRAMEBUFFER, 0);

```


### Ренгединг в буфер глубины
Когда мы хотим отрендерить сцену в наш буфер глубины достаточно прикрепить наш буфер кадра, шейдерную программу и отрендерить сцену как обычно.

```C++
glBindFramebuffer(GL_FRAMEBUFFER, fbo);
glUseProgram(depthMapCreationProgram);

renderScene();

glUseProgram(0);
glBindFramebuffer(GL_FRAMEBUFFER, 0);
```

### Использование буфера глубины
После этого при обычном рендеринге сцены мы можем прикрепить заполненный буфер глубины как обычную 2д текстуру. Значениями в этой текстуре будут те самые глубины.

```C++
glUseProgram(defaultProgram);
GLint loc = glGetUniformLocation("depthMap", defaultProgram);
if(loc > 0)
	glUniform1i(loc, depthMapTextureBlock);
glActiveTexture(GL_TEXTURE0 + depthMapTextureBlock);
glBindTexture(GL_TEXTURE_2D, depthTexture);
/*
	Остальные действия по подготовке к рендеру
*/

renderScene();

glUseProgram(0);
```

[[Computer Graphics]] [[Shadow]] [[Модели освещения]]
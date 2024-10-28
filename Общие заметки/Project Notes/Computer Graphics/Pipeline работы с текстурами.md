
- glPixelStorei -- установка настроек хранения текстуры
	- GL_UNPACK_ALIGMENT -- величина выравнивания
- glGenTexture -- создание идентификатора объекта текстуры
- glBindTexture(type, id) -- установка текстуры текущей для типа type:
	- GL_TEXTURE_1D
	- GL_TEXTURE_2D
	- GL_TEXTURE_3D
	- GL_TEXTURE_CUBE_MAP
- glTexParameter*(type, param, value) -- установка настроек для текущей текстуры типа type. Основные настройки
	-  GL_TEXTURE_WRAP_S -- что делать, если текстура вышла за границу по координате s
	- GL_TEXTURE_WRAP_T -- что делать, если текстура вышла за границу по координате t 
		- GL_REPEAT -- повторять
		- GL_CLAMP_TO_EDGE -- сводить к ближайшему допустимому значению
		- GL_WRAP -- брать дробную часть
	- GL_TEXTURE_MAG_FILTER/GL_TEXTURE_MIN_FILTER -- указать поведение при растяжении/сжатии текстуры
		- GL_NEAREST -- приведение к ближайшему
- glTexImage1D/glTexImage2D/glTexImage3D -- загрузка 1d/2d/3d изображения в текущую текстуру
- glDeleteTexture -- удаление всех ресурсов текстуры

[[Computer Graphics]] [[Текстуры]]
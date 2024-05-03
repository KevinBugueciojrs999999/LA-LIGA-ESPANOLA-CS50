# PROYECTO: LA LIGA ESPAÑOLA CS50
### Video Demo:  https://www.youtube.com/watch?v=Czi_EjSjcwo&ab_channel=KevinBuguecio
---

## DESCRIPCIÓN

La Liga Española CS50 es mi proyecto final para el curso de CS50 y tiene como objetivo ofrecer a los usuarios que se registren varios datos e información útil sobre la temporada actual de la liga española de fútbol.

Dentro de mi aplicación, los usuarios podrán ver resultados en vivo de la jornada actual (en caso de que se esté jugando), resultados de partidos en las anteriores jornadas, día y horario del kickoff de los próximos encuentros y saber el estado en el que se encuentran todos los partidos (en juego, programado, finalizado o suspendido).

Por otra parte, los usuarios podrán ver información básica de los equipos, como el nombre de su estadio, fecha de fundación, plantilla, entrenador y las competiciones que disputarán en la temporada actual.

Otra funcionalidad es que el usuario podrá agregar un máximo de 3 equipos (además de poder eliminarlos) a su lista de equipos favoritos y acceder rápidamente a ellos desde su perfil.

## ESTRUCTURA DEL PROYECTO

El proyecto está estructurado de la siguiente manera:

- **Carpeta raíz:** Contiene los archivos principales del proyecto y las siguientes carpetas:
  - **src:** Contiene las carpetas api, models, static, y templates, así como los archivos app.py y config.py.
    - **app.py:** Archivo principal donde se gestionan las funciones principales del proyecto y las rutas.
    - **config.py:** Archivo donde se configura la conexión con la base de datos local.
  - **entorno virtual:** Donde se trabajó para mantener un orden de las dependencias necesarias sin afectar al ordenador directamente.
    

#### Motivo de la Estructuración

La estructura del proyecto se ha organizado de esta manera por las siguientes razones:

- **Mantenibilidad:** Facilita la organización y la mantenibilidad del código.
- **Escalabilidad:** Permite que el proyecto sea escalable y fácil de ampliar en el futuro.
- **Claridad:** La organización del código en carpetas y archivos claros y descriptivos facilita su comprensión y mantenimiento.

## TECNOLOGÍAS UTILIZADAS

- **Python:** Se eligió por su versatilidad, simplicidad y robustez.
- **Flask:** Es ligero, flexible y fácil de aprender, lo que lo hace ideal para proyectos de cualquier tamaño. Ha servido muchisimo no solo para gestionar la navegación sino también el proceso de creación de usuario y las sesiones activas.
- **Virtual Env:** Permite mantener las dependencias de forma aislada del sistema global.
- **HTML5, CSS3, BS5:** Utilizados para la maquetación y el diseño de la interfaz de usuario.
- **XAMPP -> PHPMYADMIN:** Utilizados para gestionar la base de datos en local del proyecto. En esta parte gestiono las tablas de usuario con todas las credenciales y la contraseña pasada por un hash y los equipos favoritos de los usuarios.

## API UTILIZADA

Se utilizó la API de https://www.football-data.org/ para obtener datos relevantes para el proyecto. Se estudió la documentación para consumir efectivamente todos los recursos disponibles.

Esta API nos permite obtener información actualizada al momento sobre distintas ligas de fútbol del mundo. Particularmente en mi caso he decidido centrarme en La Liga Española de fútbol para poder enfocarme mucho mejor en las peticiones y rutas. Sin embargo, con unos pocos retoques es posible reutilizar todo mi código para hacer la misma app pero con otras ligas o incluso, elegir al comienzo de cual liga se quiere sacar información.

### OTROS DETALLES

Tenemos que tener en cuenta que en este proyecto he utilizado un metodo de autenticación basado en flask_login importando LoginManager, login_user, logout_user, login_required, current_user.

He utilizado las librerias de este framework ya que me permiten llevar un control muchisimo más sencillo de la gestión de usuarios y verificar si estos se encuentran o no logeados para poder restringir el acceso a determinadas rutas del proyecto.

Cada usuario tiene de 0 a 3 equipos favoritos y estos se almacenan en una tabla dentro de la base de datos local que guardo en el sistema. Esta tabla está ligada con una clave foranea a la tabla principal de usuarios registrados por lo que en esa tabla habrá un máximo de 3 id de equipos para cada usuario.

He visto conveniente utilizar procesos de flask como include o extend que me sirven para evitar repetir código en ciertas partes de la estructura de mi proyecto.

## CONCLUSIÓN

La Liga Española CS50 ha sido un desafío que me ha llevado al límite de mis capacidades actuales de programación. He tenido que buscar mucha información y leer mucha documentación, así como recurrir a la experiencia de otros programadores que han enfrentado problemas similares.

Creo que la estructura del proyecto está diseñada para ser mantenible, escalable y clara, lo que facilitará su desarrollo continuo y mejora en el futuro.

Aunque creo que podría mejorar muchas cosas si comenzara de cero, CS50 ha sido un camino de aprendizaje constante y desafiante del que me retiro muy satisfecho por la superación personal que ha supuesto.

He aprendido mucho con este proyecto y estoy muy orgulloso de haberlo finalizado.

¡Muchas gracias!

---
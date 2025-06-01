## Ejercicio 6: Aplicación Multi-pantalla con MDNavigationDrawer

**Objetivo:**  
Construir una aplicación que integre navegación entre varias pantallas utilizando el **MDNavigationDrawer** de KivyMD para cambiar el contenido de la aplicación.

**Enunciado:**  
Crea una aplicación KivyMD con las siguientes especificaciones:

### Estructura y Navegación:
- **ScreenManager:**  
  - Utiliza un ScreenManager para gestionar al menos tres pantallas:
    - **Pantalla "Inicio":**  
      - Mostrar un mensaje de bienvenida y una breve descripción de la aplicación.
    - **Pantalla "Perfil":**  
      - Mostrar información ficticia de un usuario (por ejemplo, nombre y correo electrónico).
      - Se puede mejorar visualmente utilizando un **MDCard** que contenga dichos datos.
    - **Pantalla "Configuración":**  
      - Mostrar opciones ficticias de configuración de la aplicación.
  
- **MDNavigationDrawer:**  
  - Debe contener opciones de navegación con íconos y textos para cada una de las pantallas ("Inicio", "Perfil" y "Configuración").
  - Al seleccionar una opción, el contenido principal (ScreenManager) debe cambiar a la pantalla correspondiente.

- **MDToolbar:**  
  - Ubicada en la parte superior de la aplicación, y debe incluir un botón de menú (hamburguesa) que abra y cierre el NavigationDrawer.

### Detalles de la Interfaz:
- Cada pantalla debe contener al menos un **MDLabel** o **MDCard** que identifique claramente de qué sección se trata.
- En la pantalla "Perfil", añade un **MDFloatingActionButton** o un botón adicional que, al presionarse, muestre más detalles del usuario mediante un **MDDialog** (por ejemplo, "Editar Perfil" o "Ver detalles").

### Requisitos Adicionales:
- Asegúrate de que la navegación sea fluida y que la interfaz se adapte a diferentes tamaños de pantalla.
- Incorpora transiciones suaves entre pantallas. (KivyMD y ScreenManager ofrecen diversas transiciones; experimenta con ellas para mejorar la experiencia de usuario).

### Extras (Opcionales):
- Agrega animaciones para la apertura y cierre del NavigationDrawer.
- Permite que la aplicación guarde la última pantalla visitada y la recupere en el siguiente inicio (esto puede integrar la parte de persistencia vista en el curso).

---
# OTP Validator

Esta aplicación de escritorio permite generar y validar códigos OTP (One-Time Passwords), así como enviarlos por SMS o WhatsApp (requiere configuración adicional).

## Instalación

1.  **Clona o descarga el repositorio:**

    *   **Clonar con Git:**
        ```bash
        git clone https://github.com/NicoAye/otp_validator.git
        cd otp_validator
        ```
    *   **Descargar como ZIP:** Descarga el archivo ZIP desde [https://github.com/NicoAye/otp_validator](https://github.com/NicoAye/otp_validator) y extrae su contenido en una carpeta.

2.  **Crea un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    venv\Scripts\activate  # Windows
    # source venv/bin/activate (macOS/Linux)
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

## Configuración

1.  **Configura el archivo `config.py`:**

    *   **`secret`:** Cambia el valor predeterminado de `secret` por una cadena segura y aleatoria. Este secreto se utiliza para generar los OTPs.
    *   **`interval`:** Define el intervalo de tiempo (en segundos) durante el cual un OTP es válido (predeterminado: 30 segundos).
    *   **`tolerance`:** Define la tolerancia (en intervalos) para la validación de OTPs.  Un valor de 1 permite que los OTPs generados en el intervalo anterior o posterior también sean válidos.
    *   **Configuración de SMS y WhatsApp (Opcional):** Si deseas enviar OTPs por SMS o WhatsApp, debes configurar las credenciales de Twilio o Selenium (consulta la sección "Envío de OTPs por SMS y WhatsApp" más abajo).

2.  **Opcional: Crea un archivo `config.json`:** Si el archivo `config.json` no existe, la aplicación utilizará los valores predeterminados definidos en `config.py`. Puedes crear un archivo `config.json` para personalizar la configuración y persistirla entre ejecuciones.  El formato del archivo debe ser JSON:

    ```json
    {
        "secret": "YourSecureSecretKey",
        "interval": 30,
        "tolerance": 1,
        "twilio_account_sid": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "twilio_auth_token": "your_auth_token",
        "twilio_phone_number": "+1234567890",
        "whatsapp_phone_number_id": "whatsapp:+1234567890"
    }
    ```

## Ejecución

1.  **Ejecuta la aplicación:**
    ```bash
    python otp_validator.py
    ```

2.  **Interactúa con la interfaz gráfica:**

    *   **Secret Key:** Ingresa o genera un secreto compartido.
    *   **OTP:** Ingresa el OTP a validar.
    *   **Interval & Tolerance:** Modifica los valores según sea necesario.
    *   **Phone Number:** Ingresa el número de teléfono del destinatario (para SMS o WhatsApp).
    *   **Twilio Account SID, Auth Token, Phone Number, WhatsApp Number ID:** Ingresa tus credenciales de Twilio (si usas Twilio).
    *   **Botones:**
        *   "Send OTP via SMS": Envía el OTP por SMS (requiere configuración de Twilio).
        *   "Send OTP via WhatsApp": Envía el OTP por WhatsApp (requiere configuración de Twilio o Selenium).
        *   "Validate OTP": Valida el OTP ingresado.
        *   "Save Configuration": Guarda la configuración actual en `config.json`.

## Envío de OTPs por SMS y WhatsApp

**Importante:** Para enviar OTPs por SMS o WhatsApp, debes configurar al menos uno de los siguientes servicios:

### Opción 1: Twilio (Recomendado)

1.  **Crea una cuenta en Twilio:** [https://www.twilio.com/](https://www.twilio.com/)
2.  **Obtén tus credenciales:**
    *   **Account SID:** Encuéntralo en el panel de control de tu cuenta de Twilio.
    *   **Auth Token:** Encuéntralo en el panel de control de tu cuenta de Twilio.
    *   **Twilio Phone Number:** Compra un número de teléfono en Twilio.
    *   **WhatsApp Number ID:** Si deseas enviar mensajes por WhatsApp, debes activar tu número de Twilio para WhatsApp Business y obtener tu WhatsApp Number ID en la consola de Twilio.
3.  **Ingresa tus credenciales en el archivo `config.py` o a través de la interfaz gráfica de la aplicación.**

### Opción 2: Selenium (¡Usar con precaución!)

**Advertencia:** El uso de Selenium con WhatsApp Web puede violar los términos de servicio de WhatsApp y podría resultar en la suspensión de tu cuenta. Úsalo bajo tu propia responsabilidad.

1.  **Instala Selenium:**
    ```bash
    pip install selenium
    ```
2.  **Descarga el ChromeDriver:**
    *   Descarga el ChromeDriver compatible con tu versión de Google Chrome desde [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads).
    *   Coloca el `chromedriver.exe` en un directorio que esté en tu PATH (ejemplo: `C:\Windows\System32`) o en la misma carpeta que el archivo `otp_validator.py`.
3.  **Comenta la línea `if whatsapp_sender.send_whatsapp(phone_number, message):` y descomenta la línea `if whatsapp_sender.send_whatsapp_selenium(phone_number, message):` en la función `send_otp_whatsapp` en el archivo `gui.py`.**

## Creación de un Archivo Ejecutable (.exe)

1.  **Instala PyInstaller:**
    ```bash
    pip install pyinstaller
    ```

2.  **Ejecuta PyInstaller:**
    ```bash
    pyinstaller --onefile --noconsole otp_validator.py
    ```

3.  **Encuentra el archivo .exe:** El archivo ejecutable se encontrará en la carpeta `dist`.

**Nota:** El proceso de PyInstaller puede tardar unos minutos. Es posible que tu software antivirus marque el archivo `.exe` como sospechoso. Puedes añadir una excepción en tu antivirus si confías en el código fuente.

## Consideraciones de Seguridad

*   **Protege el secreto:** El secreto utilizado para generar los OTPs debe ser almacenado de forma segura. No lo compartas con terceros.
*   **Twilio Auth Token:** Trata tu Twilio Auth Token como una contraseña. No lo compartas y no lo subas a repositorios públicos.
*   **Selenium:** El uso de Selenium con WhatsApp Web puede tener implicaciones de seguridad. Úsalo con precaución y bajo tu propia responsabilidad.

## Limitaciones

*   La aplicación solo ha sido probada en Windows.
*   El envío de SMS y WhatsApp depende de servicios de terceros (Twilio o Selenium) y puede estar sujeto a limitaciones y costos.

## Licencia

[Indica la licencia de tu proyecto. Por ejemplo, MIT License]


import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def enviar_email_prueba():
    mensaje = Mail(
        from_email='tu_correo_verificado@ejemplo.com',
        to_emails='destinatario@ejemplo.com',
        subject='Prueba desde Python',
        html_content='<strong>¡Hola!</strong> Estoy aprendiendo a enviar correos con Python.'
    )

    try:
        api_key = "API_KEY"

        sg = SendGridAPIClient(api_key)
        respuesta = sg.send(mensaje)

        print(f"Correo enviado. Código de estado: {respuesta.status_code}")

    except Exception as e:
        print(f"Ocurrió un error: {e}")


if __name__ == "__main__":
    enviar_email_prueba()

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_github_login_click():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.maximize_window()

    try:
        print("--- Entrando a GitHub.com ---")
        driver.get("https://github.com/")

        boton_login = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/login']"))
        )

        print("Botón encontrado. Haciendo click...")
        boton_login.click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )

        if "login" in driver.current_url:
            print("¡ÉXITO! Hemos llegado a la página de inicio de sesión.")
        else:
            print("FALLO: No estamos en la página correcta.")

    except Exception as e:
        print(f"Ocurrió un error durante la prueba: {e}")

    finally:
        print("Cerrando el navegador...")
        driver.quit()


if __name__ == "__main__":
    test_github_login_click()

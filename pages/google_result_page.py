from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class GoogleResultPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.download_link_locator = (By.CSS_SELECTOR, 'a[href*="python.org"]')
        self.timeout = timeout

    def open_python_page(self):
        try:
            python_download_link = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(self.download_link_locator) # noqa E501
            )

            python_download_link = python_download_link.get_attribute('href')

            self.driver.get(python_download_link)

        except Exception as e:

            return {
                'error': True,
                'message': f'Erro ao abrir pagina do python: {e}',
                'data': None
            }

        return {
            'error': False,
            'message': 'Pagina aberta com sucesso',
            'data': None
        }
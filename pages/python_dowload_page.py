from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from utils import remove_punctuation


class PythonDownloadPage:
    def __init__(self, driver, timeout=10, version='3.11.9'):
        self.input_search = (By.CSS_SELECTOR, 'textarea[name="q"]')
        self.driver = driver
        self.version = version
        self.timeout = timeout

    def open_version_page(self):
        try:

            current_version = remove_punctuation(self.version)

            link_download = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, f'a[href*="{current_version}"]')) # noqa E501
            )

            link_download = link_download.get_attribute('href')
            
            self.driver.get(link_download)

        except Exception as e:

            return {
                'error': True,
                'message': f'Erro ao abrir pagina da versão: {e}',
                'data': None
            }

        return {
            'error': False,
            'message': 'Pagina aberta com sucesso',
            'data': None
        }
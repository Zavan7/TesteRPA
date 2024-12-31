from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from utils import remove_punctuation


class PythonVersionPage:
    def __init__(self, driver, timeout=10, ):
        self.input_search = (By.CSS_SELECTOR, 'textarea[name="q"]')
        self.driver = driver
        self.timeout = timeout

    def dowload_file_python(self):
        try:

            link_download_64_bits = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.LINK_TEXT, 'Windows installer (64-bit)')) # noqa E501
            )

            link_download_64_bits = link_download_64_bits.get_attribute('href')

            self.driver.get(link_download_64_bits)

            filename = str(link_download_64_bits).split('/')[-1]

        except Exception as e:

            return {
                'error': True,
                'message': f'Erro ao baixar arquivo: {e}',
                'data': None
            }

        return {
            'error': False,
            'message': 'Arquivo baixado com sucesso',
            'data': filename
        }
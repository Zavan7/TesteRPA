from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class GoogleHomePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.input_search = (By.CSS_SELECTOR, 'textarea[name="q"]')
        self.timeout = timeout

    def search(self, search_term):
        try:

            input_search = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(self.input_search)
            )

            input_search.send_keys(search_term)
            input_search.send_keys(Keys.RETURN)

        except Exception as e:

            return {
                'error': True,
                'message': f'Erro ao pesquisar no Google: {e}',
                'data': None
            }

        return {
            'error': False,
            'message': 'Consulta realizada com sucesso',
            'data': None
        }
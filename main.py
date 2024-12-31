from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from pages.python_dowload_page import PythonDownloadPage
from pages.python_version_page import PythonVersionPage
from selenium.webdriver.chrome.options import Options
from pages.google_result_page import GoogleResultPage
from pages.google_home_page import GoogleHomePage
from database.mongodb import MongoDB
from settings import DOWLOADS_DIR
from selenium import webdriver
from wasabi import Printer
import time
import os

db = MongoDB("hcosta")
TIMEOUT = 10
msg = Printer()


def main() -> None:

    try:
    
        result = {
            'start_date': None,
            'end_date': None,
            'duration': None,
            'filename': None,
            'full_path': None,
            'status': None,
            'message': None
        }

        start_date = time.time()
    
        filename = None
        full_path = None
        status = None

        msg.info('Iniciando o processo de download do Python...')
        msg.info('Removendo arquivos da pasta de downloads...')

        for root, _, files in os.walk(DOWLOADS_DIR):
            for file in files:
                os.remove(os.path.join(root, file))

        msg.good('Arquivos removidos com sucesso!')
        msg.info('Iniciando o navegador...')

        service = ChromiumService(
            ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install()
        )

        chrome_options = Options()
        chrome_options.add_argument('--safebrowsing-disable-download-protection')

        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": DOWLOADS_DIR, # Diretório de download
            "download.prompt_for_download": False, # Desabilita a janela de pergunta para download
            "download.directory_upgrade": True, # Atualiza o diretório de download
            "safebrowsing.enabled": True # Habilita o download seguro
        })

        driver = webdriver.Chrome(
            service=service, 
            options=chrome_options
        )

        msg.info('Navegador iniciado com sucesso!')

        driver.get('https://www.google.com')

        google_home_page = GoogleHomePage(driver)
        google_result_page = GoogleResultPage(driver)
        python_dowload_page = PythonDownloadPage(driver, version='3.11.9')
        python_verion_page = PythonVersionPage(driver)
        
        search_term = google_home_page.search('baixar python')
        if search_term['error']:
            result['message'] = search_term['message']
            status = 'fail'
            return search_term
        
        msg.good(search_term['message'])
        
        python_page = google_result_page.open_python_page()
        if python_page['error']:
            result['message'] = python_page['message']
            status = 'fail'
            return python_page
        
        msg.good(python_page['message'])
        
        version_page = python_dowload_page.open_version_page()
        if version_page['error']:
            result['message'] = version_page['message']
            status = 'fail'
            return version_page

        msg.good(version_page['message'])

        file_python = python_verion_page.dowload_file_python()
        if file_python['error']:
            result['message'] = file_python['message']
            status = 'fail'
            return file_python
        
        time.sleep(5)
        
        filename = file_python['data']
        full_path = os.path.join(DOWLOADS_DIR, filename)
        result['message'] = file_python['message']

        status = 'success' if os.path.exists(full_path) else 'fail'

    except:
        msg.fail('Erro ao baixar arquivo')

    finally:
        end_date = time.time()
        duration = end_date - start_date
        duration = f'{duration:.2f}'

        start_date = time.strftime('%d/%m/%Y %H:%M:%S', time.localtime(start_date))
        end_date = time.strftime('%d/%m/%Y %H:%M:%S', time.localtime(end_date))

        result['start_date'] = start_date
        result['end_date'] = end_date
        result['duration'] = duration
        result['filename'] = filename
        result['full_path'] = full_path
        result['status'] = status

        driver.quit()

        return result


if __name__ == '__main__':
    result = main()
    log_id = db.insert("automation_logs", result)
    print(log_id)

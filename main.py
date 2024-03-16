from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


# Указываем ссылку на расширение
extension_url = 'https://chrome.google.com/webstore/detail/ilehaonighjijnmpnagapkhpcdbhclfg'

# Учетные данные для входа на веб-сайт
username = 'seinarukiro'
password = 'Callmevampire4464!'

# Указываем путь к исполняемому файлу браузера Chrome
chrome_options = Options()
chrome_options.binary_location = '/usr/bin/google-chrome'  # Замените путь на действительный путь к Chrome на вашей системе
chrome_options.add_argument('--headless')  # Запуск без GUI (для сервера)

# Инициализация драйвера браузера с использованием webdriver_manager
driver = webdriver.Chrome(ChromeDriverManager().install())

# Открытие ссылки на расширение в Chrome Web Store
driver.get('https://chrome.google.com/webstore/category/extensions')

# Находим поле поиска и вводим ссылку на расширение
search_box = driver.find_element_by_css_selector('input[aria-label="Search Chrome Web Store"]')
search_box.send_keys(extension_url)
search_box.submit()

# Ждем, пока кнопка "Add to Chrome" станет доступной
add_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Add to Chrome"]'))
)

# Нажимаем кнопку "Add to Chrome"
add_button.click()

# Ждем, пока кнопка "Add extension" станет доступной
add_extension_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Add extension"]'))
)

# Нажимаем кнопку "Add extension"
add_extension_button.click()

# Ожидаем, пока расширение загрузится и будет доступно
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'extension_id')))

# Находим кнопку "LOGIN" на расширении и кликаем по ней
login_button = driver.find_element_by_id('login_button')
login_button.click()

# Ожидаем переадресации на веб-сайт
WebDriverWait(driver, 10).until(EC.url_contains('https://app.getgrass.io/'))

# Вводим учетные данные на веб-сайте
username_input = driver.find_element_by_id('field-:r0:')
password_input = driver.find_element_by_id('field-:r1:')

username_input.send_keys(username)
password_input.send_keys(password)

# Нажимаем кнопку "ACCESS MY ACCOUNT"
access_button = driver.find_element_by_xpath('//button[contains(text(), "ACCESS MY ACCOUNT")]')
access_button.click()

# Закрываем браузер
driver.quit()

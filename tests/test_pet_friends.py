from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Проверка успешной авторизации
def test_should_success_auth(browser):
    actual_result = browser.find_element(By.CSS_SELECTOR, 'h1').text
    assert actual_result == "PetFriends"


# Проверка дополнительных элементов (картинка, тайтл, описание) в карточках питомцев
def test_should_additional_info_in_pet_cards(browser):
    images = browser.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = browser.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = browser.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != '', 'Image not found'
        assert names[i].text != '', 'Name not found'
        assert descriptions[i].text != '', 'Description not found'
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0, 'Species not found'
        assert len(parts[1]) > 0, 'Age not found'


# Проверка отображения или существования элементов на странице
def test_should_check_element_with_explicit_wait(browser):
    # Ожидание существования навигационной панели в DOM
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'navbarNav')))
    # Ожидание отображения кнопки "PetFriends"
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a.navbar-brand.header2')))
    # Ожидание отображения кнопки "Мои питомцы"
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/my_pets"]')))
    # Ожидание отображения кнопки "Все питомцы" в DOM
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/all_pets"]')))
    # Ожидание отображения кнопки "Выйти"
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.btn.btn-outline-secondary')))
    # Ожидание отображения центральной надписи "PetFriends"
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1.text-center')))
    # Ожидание отображения центральной надписи "Все питомцы наших пользователей"
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.text-center:nth-child(2)')))
    # Ожидание существования таблицы с питомцами в DOM
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.card-deck')))

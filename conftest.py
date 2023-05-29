import pytest
from settings import email, password, base_url
from selenium.webdriver.common.by import By
from selenium import webdriver


# Инициализация браузера и его закрытие в конце тестов
@pytest.fixture()
def browser():
    print("\nstart browser for test")
    driver = webdriver.Chrome()
    yield driver
    print("\nquit browser")
    driver.quit()


@pytest.fixture(autouse=True)
def login(browser):

    # Устанавливаем неявное ожидание
    browser.implicitly_wait(5)
    browser.get(base_url)

    # Нажать на кнопку регистрации
    btn_new_user = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-success")
    btn_new_user.click()

    # Нажать на кнопку "У меня уже есть аккаунт"
    btn_exist_acc = browser.find_element(By.CSS_SELECTOR, "a[href='/login']")
    btn_exist_acc.click()

    # Ввод email
    field_email = browser.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys(email)

    # Ввод пароля
    field_pass = browser.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys(password)

    # Нажать на кнопку "Войти"
    btn_submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    btn_submit.click()


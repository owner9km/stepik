import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


def test_find_button(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_xpath("//button[@class='btn btn-lg btn-primary btn-add-to-basket']").text
    assert button == 'Añadir al carrito', "Опаньки, проверка кнопки стоит на испанском языке, а на францазком будет валиться,это нормально!!"

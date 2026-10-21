from selenium import webdriver


def test_home_page_title():
    driver = webdriver.Chrome()

    try:
        driver.get("https://demowebshop.tricentis.com/")

        assert "Demo Web Shop" in driver.title

    finally:
        driver.quit()

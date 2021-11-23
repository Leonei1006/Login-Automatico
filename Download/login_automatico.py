from selenium import webdriver
navegador = webdriver.Chrome()
navegador.get("https://www.amazon.com.br/")
navegador.find_element_by_xpath('//*[@id="nav-link-accountList-nav-line-1"]').click()
navegador.find_element_by_xpath('//*[@id="ap_email"]').send_keys('xxxxxxxxxxxxx@xxxxxx.com')
navegador.find_element_by_xpath('//*[@id="continue"]').click()
navegador.find_element_by_xpath('//*[@id="ap_password"]').send_keys('xxxxxxxxx')
navegador.find_element_by_xpath('//*[@id="signInSubmit"]').click()
navegador.find_element_by_xpath('//*[@id="ap-account-fixup-phone-skip-link"]').click()

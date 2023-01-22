import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin(unittest.TestCase): # test scenario

    def setUp(self): # buka browser
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_case_1_success_login(self): # test case
        self.browser.get("https://barru.pythonanywhere.com/daftar")
        time.sleep(2)
        self.browser.find_element(By.ID, "email").send_keys("tester@jagoqa.com")
        time.sleep(2)
        self.browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("testerjago")
        time.sleep(2)
        self.browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[3]").click()
        time.sleep(2)
        
        # GET DATA FROM POP UP
        popup_atas = self.browser.find_element(By.ID, "swal2-title").text
        popup_bawah = self.browser.find_element(By.ID, "swal2-content").text
        time.sleep(2)

        # VALIDASI
        self.assertIn('Welcome', popup_atas)
        self.assertEqual(popup_bawah, 'Anda Berhasil Login')
        time.sleep(2)

    def test_case_2_failed_login_with_empty_email_and_password(self): # test case
        self.browser.get("https://barru.pythonanywhere.com/daftar")
        time.sleep(2)
        self.browser.find_element(By.ID, "email").send_keys("")
        time.sleep(2)
        self.browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("")
        time.sleep(2)
        self.browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[3]").click()
        time.sleep(2)
        
        # GET DATA FROM POP UP
        popup_atas = self.browser.find_element(By.ID, "swal2-title").text
        popup_bawah = self.browser.find_element(By.ID, "swal2-content").text
        time.sleep(2)

        # VALIDASI
        self.assertIn("User's not found", popup_atas)
        self.assertEqual(popup_bawah, 'Email atau Password Anda Salah')
        time.sleep(2)

    def test_case_3_failed_login_with_valid_email_and_empty_password(self): # test case
        self.browser.get("https://barru.pythonanywhere.com/daftar")
        time.sleep(2)
        self.browser.find_element(By.ID, "email").send_keys("tester@jagoqa.com")
        time.sleep(2)
        self.browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("")
        time.sleep(2)
        self.browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[3]").click()
        time.sleep(2)
        
         # GET DATA FROM POP UP
        popup_atas = self.browser.find_element(By.ID, "swal2-title").text
        popup_bawah = self.browser.find_element(By.ID, "swal2-content").text
        time.sleep(2)

        # VALIDASI
        self.assertIn("User's not found", popup_atas)
        self.assertEqual(popup_bawah, 'Email atau Password Anda Salah')
        time.sleep(2)

    def test_case_4_failed_login_with_invalid_email(self): # test case
        self.browser.get("https://barru.pythonanywhere.com/daftar")
        time.sleep(2)
        self.browser.find_element(By.ID, "email").send_keys("tester")
        time.sleep(2)
        self.browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("testerjago")
        time.sleep(2)
        self.browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[3]").click()
        time.sleep(2)
        
        # GET DATA FROM POP UP
        email_form = self.browser.find_element(By.ID, "email").get_attribute("validationMessage")
        time.sleep(2)

        # VALIDASI
        self.assertIn('Please include', email_form)
        time.sleep(2)

    def test_case_5_failed_login_with_valid_email_and_invalid_password(self): # test case
        self.browser.get("https://barru.pythonanywhere.com/daftar")
        time.sleep(2)
        self.browser.find_element(By.ID, "email").send_keys("tester@jagoqa.com")
        time.sleep(2)
        self.browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("qa")
        time.sleep(2)
        self.browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[3]").click()
        time.sleep(2)
        
         # GET DATA FROM POP UP
        popup_atas = self.browser.find_element(By.ID, "swal2-title").text
        popup_bawah = self.browser.find_element(By.ID, "swal2-content").text
        time.sleep(2)

        # VALIDASI
        self.assertIn("User's not found", popup_atas)
        self.assertEqual(popup_bawah, 'Email atau Password Anda Salah')
        time.sleep(2)

    def test_case_6_failed_login_with_unregister_email_and_password(self): # test case
        self.browser.get("https://barru.pythonanywhere.com/daftar")
        time.sleep(2)
        self.browser.find_element(By.ID, "email").send_keys("nama@gmail.com")
        time.sleep(2)
        self.browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("nama")
        time.sleep(2)
        self.browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[3]").click()
        time.sleep(2)
        
        # GET DATA FROM POP UP
        popup_atas = self.browser.find_element(By.ID, "swal2-title").text
        popup_bawah = self.browser.find_element(By.ID, "swal2-content").text
        time.sleep(2)

        # VALIDASI
        self.assertIn("User's not found", popup_atas)
        self.assertEqual(popup_bawah, 'Email atau Password Anda Salah')
        time.sleep(2)    

    def tearDown(self): # tutup browser
        self.browser.close() 


if __name__ == "__main__": 
    unittest.main()
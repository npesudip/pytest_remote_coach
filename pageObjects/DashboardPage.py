from selenium.webdriver.common.by import By


class DashboardPage:
    total_subscriber_id = "total-subscribers-total"

    def __init__(self, driver):
        self.driver = driver

    def get_total_subscriber(self):
        total_subscriber = self.driver.find_element(By.ID, self.total_subscriber_id).text
        return total_subscriber

from selenium.webdriver.common.by import By

from StudyNotes.TestDevelopHomework.PhaseFourHomework.po.base_page import BasePage


class AddMemberPage(BasePage):

    _addMember_usernameEle = (By.ID, "username")
    _addMember_acctidEle = (By.ID, "memberAdd_acctid")
    _addMember_phoneEle = (By.ID, "memberAdd_phone")
    _addMember_saveButt0nEle = (By.CSS_SELECTOR, ".js_btn_save")

    def add_member(self,name):
        """
        添加成员操作
        :return:
        """
        from StudyNotes.TestDevelopHomework.PhaseFourHomework.po.contact_page import ContactPage

        # 输入姓名、账号、手机号
        # 加*的作用为解包
        # 不解包传入参数为：(By.ID, "username")，解包传入参数为：By.ID, "username"
        self.find(self._addMember_usernameEle).send_keys(name)
        self.find(self._addMember_acctidEle).send_keys("123")
        self.find(self._addMember_phoneEle).send_keys("15023456789")

        #点击保存
        self.find(self._addMember_saveButt0nEle).click()

        return ContactPage(self.driver)
from selenium.webdriver.common.by import By

from PhaseFourHomework.po.base_page import BasePage


class MainPage(BasePage):

    # 企业微信首页地址链接
    # 添加单下划线代表私有属性，通过包名调用时不展示
    _mainPage_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    _base_url = _mainPage_url

    _contact_ele = (By.ID, "menu_contacts")
    _main_addMember = (By.CSS_SELECTOR,".ww_indexImg_AddMember")

    def goto_contact(self):
        """
        跳转通讯录页面
        :return:
        """
        from StudyNotes.TestDevelopHomework.PhaseFourHomework.po.contact_page import ContactPage

        #点击通讯录导航栏跳转通讯录
        self.find(self._contact_ele).click()

        return ContactPage(self.driver)

    def goto_add_member(self):
        """
        跳转到添加成员页面
        :return:
        """
        from StudyNotes.TestDevelopHomework.PhaseFourHomework.po.add_member_page import AddMemberPage

        # 点击添加成员
        self.find(self._main_addMember).click()

        return AddMemberPage(self.driver)




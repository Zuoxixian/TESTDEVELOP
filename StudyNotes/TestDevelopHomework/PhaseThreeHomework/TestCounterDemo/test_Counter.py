import allure
import pytest
import yaml

def get():
    with open("../datas/data.yml",encoding = "UTF-8") as datasList:
        #读取yaml文件中add集合
        Datas = yaml.safe_load(datasList)
        # print(addDatas)
        # print("--------------")
        #获取addDatas中datas列表
        add_datas = Datas["add"]["datas"]
        div_datas = Datas["div"]["datas"]
        # print(add_datas)
        # print("-------------")
        # 获取addDatas中datasId列表
        add_datasId = Datas["add"]["dataId"]
        div_datasId = Datas["div"]["dataId"]
        # print(add_datasId)
        return Datas

#get()["add"]["datas"]
#get()["add"]["dataId"]

# def test_get():
#     get()

@allure.feature("计算器验证模块")
class TestCounter:
    @allure.story(f"计算器加法方法")
    @pytest.mark.parametrize(["addend1","addend2","expectResult"],get()["add"]["datas"],ids = get()["add"]["dataId"])
    def test_add(self,counterBegin,addend1,addend2,expectResult):
        #with allure.step(f"{}"):
        addResult = counterBegin.add(addend1,addend2)
        assert addResult == expectResult

    @allure.story(f"计算器加法方法")
    @pytest.mark.parametrize(["divisor", "dividend", "expectResult"], get()["div"]["datas"], ids=get()["div"]["dataId"])
    def test_div(self, counterBegin, divisor, dividend, expectResult):
        # with allure.step(f"{}"):
        addResult = counterBegin.div(divisor, dividend)
        assert addResult == expectResult

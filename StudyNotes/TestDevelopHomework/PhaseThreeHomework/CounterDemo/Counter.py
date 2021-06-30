#计算器，被测模块
class CounterDemoTest:
    def add(self,addend1,addend2):
        try:
            result = addend1 + addend2
        except:
            return "输入值存在非数字值"
        if isinstance(result,int):
            return result
        elif isinstance(result,float):
            return round(result,2)
        else:
            return "输入值存在非数字值"
        # #根数输入值获取类型
        # addendOneType = type(addend1)
        # addendTwoType = type(addend2)
        # #判断为整形或者浮点型，除此外其他的判定为错误类型
        # if addendOneType == addendTwoType and isinstance(addend1,int):
        #     return addend1 + addend2
        # elif (addendOneType == addendTwoType and isinstance(addend1,float)) or isinstance(addend1,float) or isinstance(addend2,float):
        #     result = addend1 + addend2
        #     return round(result,2)
        # else:
        #     return "输入值存在非数字值"


    def sub(self,a,b):
        return a - b

    def mul(self,a,b):
        return a * b

    def div(self,divisor,dividend):
        try:
            result = divisor / dividend
        except:
            if dividend == 0:
                return "被除数不能为0"
            else:
                return "输入值存在非数字值"
        if isinstance(result,int):
            return result
        elif isinstance(result,float):
            return round(result,2)
        else:
            return "输入值存在非数字值"
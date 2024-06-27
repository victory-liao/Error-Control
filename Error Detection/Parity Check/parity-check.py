"""
author: victory liao
date: 2024-06-27
"""


class ParityCheck:
    """奇偶校验"""

    @staticmethod
    def generate_parity_code(binary_data, flag="odd"):
        """
        生成二进制数据对应的奇校验编码/偶校验编码
        :param binary_data: 二进制数据
        :param flag: odd/even
        :return: flag为odd时返回奇校验编码，flag为even时返回偶校验码
        """
        # 将二进制字符串转换为字符列表
        binary_data_list = list(binary_data)

        # 统计字符列表中1的个数
        total_one_in_binary_data = binary_data_list.count("1")

        # 校验码
        check_code = ""

        # 根据字符列表中1的个数和flag确定校验码
        if total_one_in_binary_data % 2 == 0 and flag == "odd":
            check_code = "1"
        elif total_one_in_binary_data % 2 != 0 and flag == "odd":
            check_code = "0"
        elif total_one_in_binary_data % 2 == 0 and flag == "even":
            check_code = "0"
        elif total_one_in_binary_data % 2 != 0 and flag == "even":
            check_code = "1"

        # 将校验码添加到字符列表中
        binary_data_list.append(check_code)

        # 将字符列表中的字符连接起来得到校验编码并返回
        return "".join(binary_data_list)

    @staticmethod
    def parity_check(data_to_be_checked, flag="odd"):
        """
        通过奇校验/偶校验对二进制数组进行检错
        :param data_to_be_checked: 待检错二进制数据
        :param flag: odd/even
        :return: True表示待检数据有错，False表示不能判断待检数据的正确性
        """
        # 将待检错二进制数据转换为字符列表
        data_to_be_checked_list = list(data_to_be_checked)

        # 统计字符列表中1的个数
        total_one_in_data = data_to_be_checked_list.count("1")

        # 根据字符列表中1的个数和flag判断数据是否错误
        if total_one_in_data % 2 == 0 and flag == "odd":
            return True
        elif total_one_in_data % 2 != 0 and flag == "odd":
            return False
        elif total_one_in_data % 2 == 0 and flag == "even":
            return False
        elif total_one_in_data % 2 != 0 and flag == "even":
            return True


# 主函数
if __name__ == "__main__":
    # 二进制数据
    binary_data = "010101"

    # 创建奇偶校验对象
    pc = ParityCheck()
    # 生成奇校验码
    odd_parity_code = pc.generate_parity_code(binary_data, "odd")
    print("odd parity code:", odd_parity_code)
    # 生成偶校验码
    even_parity_code = pc.generate_parity_code(binary_data, "even")
    print("even parity code:", even_parity_code)

    # 使用奇校验进行检错
    # 数据错误的情况
    data_to_be_checked1 = "0101011"
    result1 = pc.parity_check(data_to_be_checked1, "odd")
    if result1 is True:
        print(f"{data_to_be_checked1}中存在错误，校验方式：odd")
    else:
        print(f"不能判断{data_to_be_checked1}是否错误，校验方式：odd")
    # 不能判断的情况
    data_to_be_checked2 = "1101011"
    result2 = pc.parity_check(data_to_be_checked2, "odd")
    if result2 is True:
        print(f"{data_to_be_checked2}中存在错误，校验方式：odd")
    else:
        print(f"不能判断{data_to_be_checked2}是否错误，校验方式：odd")

    # 使用偶校验进行检错
    # 数据错误的情况
    data_to_be_checked3 = "1101011"
    result3 = pc.parity_check(data_to_be_checked3, "even")
    if result3 is True:
        print(f"{data_to_be_checked3}中存在错误，校验方式：even")
    else:
        print(f"不能判断{data_to_be_checked3}是否错误，校验方式：even")
    # 不能判断的情况
    data_to_be_checked4 = "0101011"
    result4 = pc.parity_check(data_to_be_checked4, "even")
    if result4 is True:
        print(f"{data_to_be_checked4}中存在错误，校验方式：even")
    else:
        print(f"不能判断{data_to_be_checked4}是否错误，校验方式：even")

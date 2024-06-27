"""
author: 该代码引用自https://blog.csdn.net/qq_31064397/article/details/89928453
date: 2024-06-27
"""


def XOR(str1, str2):
    """
    实现模2减法
    :param str1: 操作数1
    :param str2: 操作数2
    :return: 模2减法结果
    """
    ans = ''

    if str1[0] == '0':
        return '0', str1[1:]
    else:
        for i in range(len(str1)):
            if str1[i] == '0' and str2[i] == '0':
                ans = ans + '0'
            elif str1[i] == '1' and str2[i] == '1':
                ans = ans + '0'
            else:
                ans = ans + '1'
    return '1', ans[1:]


def CRC_Encoding(str1, str2):
    """
    CRC编码
    :param str1: 原始数据
    :param str2: 生成多项式
    :return: 最终发送数据
    """
    # 求生成多项式的长度
    length = len(str2)
    # 给原始数据（被除数）补0
    str3 = str1 + '0' * (length - 1)
    print(str3)
    # 存放CRC编码
    ans = ''
    # 存放计算过程的余数
    yus = str3[0:length]
    print(yus)

    # 求余数
    for i in range(len(str1)):
        str4, yus = XOR(yus, str2)  # 异或
        print(str4, yus)  # 1 1001
        ans = ans + str4  # ans = 1
        if i == len(str1) - 1:
            break
        else:
            yus = yus + str3[i + length]  # yus = 1001 + 1
            print(yus)

    # 将原始数据与余数拼接
    ans = str1 + yus

    # 返回CRC编码
    return ans


# CRC解码
def CRC_Decoding(str1, str2):
    # 求生成多项式的长度
    length = len(str2)
    # 给原始数据序列补0
    str3 = str1 + '0' * (length - 1)
    # 存放结果
    ans = ''
    # 存放计算过程中的余数
    yus = str3[0:length]

    # 求余数
    for i in range(len(str1)):
        str4, yus = XOR(yus, str2)
        ans = ans + str4
        if i == len(str1) - 1:
            break
        else:
            yus = yus + str3[i + length]

    # 余数为0，表示数据正确
    return yus == '0' * len(yus)


# 主函数
def main():
    """
    对CRC编码方法CRC_Encoding、解码方法CRC_Decoding进行测试
    :return: 无
    """
    while True:
        print('==' * 30)

        setting = input("请输入运行模式（0：退出，1：CRC编码，2：CRC验证）：")

        if setting == '0':
            break
        elif setting == '1':  # 生成CRC编码
            str1 = input("请输入数据：")
            str2 = input("请输入生成比特模式：")
            str3 = CRC_Encoding(str1, str2)
            print("{} 编码后为: {}".format(str1, str3))
        elif setting == '2':  # CRC验证
            str1 = input("请输入验证数据：")
            str2 = input("请输入生成比特模式：")
            flag = CRC_Decoding(str1, str2)
            if flag:
                print("验证完成，未出错")
            else:
                print("sorry 验证数据已出错")
        else:
            print("请正确输入：")


if __name__ == "__main__":
    # 调用CRC主函数
    main()

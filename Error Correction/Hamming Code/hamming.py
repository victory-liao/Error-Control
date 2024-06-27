"""
author: victory liao
date: 2024-06-27
"""


import operator
from functools import reduce


class HammingCode:
    """
    求二进制数据序列对应的汉明码（hamming code）
    """

    def __init__(self, sent_data):
        """
        :param sent_data: 要发送的二进制数据
        :param received_data: 接收到的二进制数据（需要进行检错并纠错的数据）
        :param data_sequence_indexs: 数据和校验码组成的序列中每个数据的索引
        :param data_sequence: 数据和校验码组成的序列
        :param check_code_indexes: 校验码在数据和校验码组成的序列中的索引
        :param index_p_arrays: 校验码p1,p2,...,pr与d1,d2,...,dk组成的列表
        :param p_values: 求得的校验码值
        :param h_code: 最终求得的汉明码
        """
        self.sent_data = sent_data
        self.k = len(sent_data)
        self.r = 1
        self.data_sequence_indexs = []
        self.data_sequence = {}
        self.check_code_indexes = []
        self.index_p_arrays = []
        self.p_values = []
        self.h_code = ""
        self.indexes_need2check_array = []

    def build_data_sequence(self):
        """
        构建校验码和数据组成的数据序列
        :return: 无
        """
        # 计算r
        while 2 ** self.r < self.r + self.k + 1:
            self.r += 1
        print("r:", self.r)

        # 将校验码插入到数据序列中（第i个插入到2^i-1索引处）
        for i in range(1, self.r + 1):
            tmp_index = 2 ** (i - 1)
            self.check_code_indexes.append(tmp_index)
            self.data_sequence[tmp_index] = None
        print("check code indexes:", self.check_code_indexes)

        # 将数据添加到数据序列中
        data_index = 0
        for index in range(1, self.r + self.k + 1):
            if index not in self.data_sequence.keys():
                self.data_sequence[index] = int(self.sent_data[data_index])
                data_index += 1
        data_sequence = self.data_sequence
        print("data sequence:", data_sequence)

        # 计算校验码
        self.data_sequence_indexs = [i for i in range(1, self.k + self.r + 1) if i not in self.check_code_indexes]
        print("data sequence indexes:", self.data_sequence_indexs)

    def compute_hamming_code(self):
        """
        构建校验码p1,p2,...,pr与d1,d2,...,dk组成的列表，并根据列表求汉明码
        :return:
        """
        # 构建校验码p1,p2,...,pr与d1,d2,...,dk组成的列表
        for index in self.data_sequence_indexs:
            tmp_list = list(bin(index)[2:].zfill(self.r))
            tmp_list = list(map(lambda x: int(x), tmp_list))

            self.index_p_arrays.append(tmp_list)
        print("index_p_arrays:", self.index_p_arrays)

        # 根据列表中的数据求校验码p1,p2,...,pr
        for col in range(self.r - 1, -1, -1):
            useful_data = []
            tmp_index_need2check = []
            for row in range(len(self.index_p_arrays)):
                if self.index_p_arrays[row][col] == 1:
                    tmp_index_need2check.append(self.data_sequence_indexs[row])
                    useful_data.append(self.data_sequence[self.data_sequence_indexs[row]])

            tmp_p_value = reduce(operator.xor, useful_data)

            self.p_values.append(tmp_p_value)

            self.indexes_need2check_array.append(tmp_index_need2check)

        # 用求得的校验码值填充数据序列中的空位
        p_value_index = 0
        for x in self.check_code_indexes:
            self.data_sequence[x] = self.p_values[p_value_index]
            p_value_index += 1

        # 输出hamming code
        for i in range(1, self.k + self.r + 1):
            self.h_code += str(self.data_sequence[i])

    def error_check(self, received_data):
        """
        找到接收数据中错误信息的索引
        :param received_data: 接收的数据
        :return: 数据的错误位
        """
        check_code_of_received_data = []

        for i in range(self.r):
            data_need2check_list = [int(received_data[j - 1]) for j in self.indexes_need2check_array[i]]
            data_need2check_list.extend([self.data_sequence[self.check_code_indexes[i]]])
            tmp_code = str(reduce(operator.xor, data_need2check_list))
            check_code_of_received_data.append(tmp_code)

        check_code_of_received_data.reverse()
        check_code_of_received_data = "".join(check_code_of_received_data)

        return int(check_code_of_received_data, 2)

    @staticmethod
    def correct_error(received_data, pos):
        """
        对接收的错误数据进行纠错
        :param received_data: 接收的错误数据
        :param pos: 错误位
        :return: 正确的数据
        """
        received_data = list(received_data)

        if received_data[pos] == "0":
            received_data[pos] = "1"
        else:
            received_data[pos] = "0"

        return "".join(received_data)

    def output_check_code(self):
        """
        输出汉明码中的校验码
        :return:
        """
        check_code = ""

        for i in self.check_code_indexes:
            check_code += self.h_code[i - 1]

        return check_code


if __name__ == "__main__":
    sent_data = "101101"
    hc = HammingCode(sent_data)
    hc.build_data_sequence()
    hc.compute_hamming_code()
    print("hamming code:", hc.h_code)
    print("check code:", hc.output_check_code())
    print("need to check:", hc.indexes_need2check_array)

    received_data = "0010111101"
    error_pos = hc.error_check(received_data)
    print("error pos:", error_pos)
    right_data = hc.correct_error(received_data, error_pos)
    print("right data:", right_data)


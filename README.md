# Error-Control
Python implementation of error control, including error detection and correction.

- Error Detection

  - Parity Check

    - 求二进制序列对应的奇/偶校验编码
      - 对应方法：generate_parity_code(binary_data, flag)

    - 利用奇/偶校验对二进制序列进行检错
      - 对应方法：parity_check(data_to_be_checked, flag)

  - CRC

- Error Correction

  - Hamming Code
    - 求二进制序列（发送方）的汉明码
      - 对应方法：compute_hamming_code()
    - 检验二进制序列中的错误（接收方）
      - 对应方法：error_check()
    - 对二进制序列（接收方）进行纠错
      - 对应方法：correct_error(received_data, pos)


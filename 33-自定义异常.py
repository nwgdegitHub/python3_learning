# python中 抛出异常用raise
class ShortInputError(Exception):
    def __init__(self, length, min_len):
        self.length = length
        self.min_len = min_len

    def __str__(self):
        return f'你输入的长度是{self.length}, 要求不能少于{self.min_len}'


# if __name__ == '__main__': # 只在当前文件起效


def main():
    try:
        content = input('请输入:')
        if len(content) < 3:
            raise ShortInputError(len(content), 3)
    except Exception as result:
        print(result)
    else:
        print('没有异常,完成')

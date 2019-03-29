import numpy as np

# 문법 파일 불러오기
class Grammar :
    def __init__(self):
        self.contents = None
        self.len = 0

    def load(self, filePath):
        try :
            self.contents = np.loadtxt(filePath, dtype='str', delimiter=' -> ', encoding='utf-8')
            self.len = len(self.contents)
            print("문법 정보를 불러왔습니다.")
            print("문법의 개수는 {}개 입니다".format(self.len))

        # 파일 없을 때 예외 처리
        except:
            print("문법 정보가 없습니다.")

# 사전 파일 불러오기
class Dict :
    def __init__(self):

        self.contents = None
        self.numberOfContents = 0

    def load(self, filePath):
        try:
            # 첫 문자에 ufeff가 붙는 현상 제거 : utf-8-sig로 해결
            self.contents = np.loadtxt(filePath, dtype='str', delimiter='   ', encoding='utf-8-sig')
            print("사전을 불러왔습니다. (utf-8 인코딩)")
            self.numberOfContents = len(self.contents)
            print("사전에 들어있는 단어 개수는 " + str(self.numberOfContents) + "개 입니다.")

        # 사전 파일 없을 때 예외 처리
        except:
            print("사전이 없습니다. ")

# 문장 파일 불러오기
class Sentence :
    def __init__(self):

        self.contents = None
        self.len = 0

    def load(self, filePath):
        try:
        # 첫 문자에 ufeff가 붙는 현상 제거 : utf-8-sig로 해결
            self.contents = np.loadtxt(filePath, dtype='str', delimiter='\n')
            print("문장을 불러왔습니다. (utf-8 인코딩)")
            self.len = len(self.contents)
            print("불러온 문장은 " + str(self.len) + "개 입니다.")

        # 문장 파일 없을 때 예외 처리
        except:
            print("불러올 문장이 없습니다.")
#
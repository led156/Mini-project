import os, datetime, shutil

class Convert():
    def __init__(self):
        self.allow_type = [".cpp", ".java"] # 해당하는 확장자명을 가진 파일들의 이름을 바꿀 것.
        self.rename = {"n": "baekjoon", "p":"programmers"} # 파일의 시작 이름에 따라 바꿀 파일명 지정.
        self.user_name = "뚜룽지"


    def to_date(self, file_name): # 파일을 읽고 해당 파일의 수정일을 형식에 맞게 반환한다.
        m_time = os.path.getmtime(file_name)
        m_time = datetime.datetime.fromtimestamp(m_time)
        return datetime.datetime.strftime(m_time, '%Y-%m-%d')


    def read_all_file(self): # allow_type에 맞는 형식자를 가진 파일 리스트를 반환한다.
        dir_list = os.listdir('./')
        file_list = []
        for file_name in dir_list:
            if os.path.splitext(file_name)[-1] in self.allow_type: 
            #if os.path.splitext(file_name)[-1] == '.cpp':
                file_list.append(file_name)
        return file_list


    def find_folder(self, date): # 해당 이름을 가진 폴더의 존재유무를 반환한다.
        dir_list = os.listdir('./')
        if dir_list.count(date) == 0:
            return False
        return True


    def check_has_folder(self, file_name): # 해당 이름을 가진 폴더가 없다면, 만드는 함수. 성공유무를 반환한다.
        # 파일의 수정일 받아오기
        date = self.to_date(file_name)
        # 수정일 이름을 가진 폴더가 있는지 확인
        if not self.find_folder(date):
            # 없다면 create_folder
            os.mkdir(date)
        return True


    def rename_file(self, file_name): # 해당 파일명을 형식대로 바꾸어 리턴한다.
        tag = file_name[0]
        problem_name = ""
        file_type = ""
        if tag == "n":
            problem_name, file_type = os.path.splitext(file_name)
            problem_name = problem_name[1:]
        else:
            problem_name, file_type = os.path.splitext(file_name)
            problem_name = os.path.splitext(file_name)[-2]
            tag = "p"
        
        return self.rename[tag]+"_"+problem_name+"_"+self.user_name+file_type


    def move_file(self, file_name): # 파일들을 해당 폴더로 이동한다.
        # 이동할 폴더명
        folder = self.to_date(file_name)
        # 파일명을 형식대로 따온다.
        new_file_name = self.rename_file(file_name)
        # 폴더경로를 추가한다.
        new_file_name = "./"+folder+"/"+new_file_name
        # 이동한다.
        shutil.move(file_name, new_file_name)


    def exec(self):
        list = []
        list = self.read_all_file()

        for file_name in list:
            if self.check_has_folder(file_name):
                self.move_file(file_name)

convert = Convert()
convert.exec()
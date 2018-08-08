## coding=utf-8

import requests
import pandas as pd


class MoodleHandler():
    base_url = "http://ido.khjh.hc.edu.tw/moodle"
    teacher_credentials = {
        'username': 'khjht260',
        'password': '650103',
    }
    course_num = '196'
    VALID_ELEMENTS = ["已經完成", "已經完成(及格)"]
    def __init__(self):
        pass

    def checkAuth(self, data):
        rs = requests.session()
        false_data = {"username": "haha", "password": "haha"}
        false_res = rs.post(
            MoodleHandler.base_url + "/login/index.php", 
            data=false_data
        )
        real_res = rs.post(
            MoodleHandler.base_url + "/login/index.php", 
            data=data
        )
        print(len(false_res.content))
        print(len(real_res.content))
        return len(real_res.content) > len(false_res.content) * 1.1

    def getUserInfo(self, data):
        print(data)
        user_id = data['username']
        user_id=''.join(i for i in user_id if i.isdigit())
        num_progress = self._get_progress_num()
        return {"credits": num_progress[user_id]}
    
    def _get_progress_num(self):
        rs = requests.session()
        res = rs.post(MoodleHandler.base_url+"/login/index.php", data=MoodleHandler.teacher_credentials)
        report1 = rs.get(MoodleHandler.base_url+"/report/progress/index.php?course="+MoodleHandler.course_num+"&format=csv")

        with open('moodle_data.csv', 'w+', encoding='utf-8') as file:
            file.write(report1.text)

        data = pd.read_csv('moodle_data.csv', index_col=0, encoding='utf-8')
        data = data.to_dict('index')

        stats = {}
        for student in data:
            scores = list(data[student].values())
            count = self.get_count(scores)
            student_id = student.split(' ')[0]
            stats[student_id] = count

        stats['260'] = 13
        return stats

    @staticmethod
    def get_count(arr_score):
        valids = [arr_score.count(element) for element in MoodleHandler.VALID_ELEMENTS]
        return sum(valids)
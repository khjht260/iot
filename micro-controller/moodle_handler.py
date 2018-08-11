## coding=utf-8
import pandas as pd
import redis

import requests
import io

from settings import db_settings

class MoodleHandler():
    base_url = "http://ido.khjh.hc.edu.tw/moodle"
    teacher_credentials = {
        'username': 'khjht260',
        'password': '650103',
    }
    course_num = '196'
    database_ip = db_settings['db_ip']
    database_port = db_settings['db_port']
    database_password = db_settings['db_password']

    VALID_ELEMENTS = ["已經完成", "已經完成(及格)"]
    def __init__(self):
        self.conn = redis.StrictRedis(
            host=MoodleHandler.database_ip,
            port=MoodleHandler.database_port,
            password=MoodleHandler.database_password,
        )

    def set_db(self, key, val):
        self.conn.set(key, val)

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
        num_spent = self._get_spent_num(user_id)
        return {
            "num_progress": num_progress[user_id],
            "num_spent": num_spent,
        }
    
    def _get_progress_num(self):
        rs = requests.session()
        res = rs.post(MoodleHandler.base_url+"/login/index.php", data=MoodleHandler.teacher_credentials)
        report = rs.get(MoodleHandler.base_url+"/report/progress/index.php?course="+MoodleHandler.course_num+"&format=csv")
        report_file = io.StringIO(report.text)

        data = pd.read_csv(report_file, index_col=0, encoding='utf-8')
        data = data.to_dict('index')

        stats = {}
        for student in data:
            scores = list(data[student].values())
            count = self.get_count(scores)
            student_id = student.split(' ')[0]
            stats[student_id] = count

        stats['260'] = 13
        print('done getting progress num')
        return stats

    def _get_spent_num(self, user_id):
        print('user_id: ', user_id)
        num_spent = self.conn.get(user_id)
        if num_spent is None:
            num_spent = 0
        else:
            num_spent = int(num_spent)
        return num_spent

    @staticmethod
    def get_count(arr_score):
        valids = [arr_score.count(element) for element in MoodleHandler.VALID_ELEMENTS]
        return sum(valids)
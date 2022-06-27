import mysql.connector
#  순서 1 mysql workbench에 유저 생성하고 데이터 가져오기 -> user.py(회원가입)
def get_connection() :
    connection = mysql.connector.connect(
        host = 'yh-db.cv5n2at5qukz.ap-northeast-2.rds.amazonaws.com',
        database = 'posting_db',
        user = 'posting_user',
        password = 'posting1234'
    )
    return connection
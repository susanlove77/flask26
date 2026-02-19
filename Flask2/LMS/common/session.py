import pymysql

class Session:

    login_member = None

    @staticmethod
    def get_connection(): # 데이터베이스에 연결용 코드
        print("get_connection()메서드 호출 - mysql에 접속됩니다.")

        return pymysql.connect(
            host='192.168.0.178',
            user='kkk',
            password='1234',
            db='mbc',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor

        )

    @classmethod
    def login(cls, member):
        cls.login_member = member

    @classmethod
    def logout(cls):
        cls.login_member = None

    @classmethod
    def is_login(cls):
        return cls.login_member is not None

    @classmethod
    def is_admin(cls):
        return cls.is_login() and cls.login_member.role == "admin"

    @classmethod
    def is_manager(cls):
        return cls.is_login() and cls.login_member.role in ("manager", "admin")


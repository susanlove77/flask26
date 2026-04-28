import sqlite3
import os

class Session:
    current_user = None
    # SQLite 파일 경로 (DATABASE_URL 설정에 맞춰 'local.db' 사용)
    DB_PATH = os.path.join(os.getcwd(), 'local.db')

    @staticmethod
    def get_connection():
        # pymysql 대신 sqlite3를 사용하여 로컬 파일에 연결합니다.
        conn = sqlite3.connect(Session.DB_PATH)
        
        # MySQL의 DictCursor처럼 결과를 딕셔너리 형태로 받기 위한 설정
        conn.row_factory = sqlite3.Row 
        return conn

    @classmethod
    def login(cls, member):
        cls.current_user = member

    @classmethod
    def logout(cls):
        cls.current_user = None

    @classmethod
    def is_logged_in(cls):
        return cls.current_user is not None

    @classmethod
    def is_admin(cls):
        # member가 객체라면 .role, 딕셔너리라면 ['role'] 사용
        if not cls.is_logged_in():
            return False
        role = getattr(cls.current_user, 'role', None) or cls.current_user.get('role')
        return role == "admin"

    @classmethod
    def is_manager(cls):
        if not cls.is_logged_in():
            return False
        role = getattr(cls.current_user, 'role', None) or cls.current_user.get('role')
        return role in ("admin", "manager")
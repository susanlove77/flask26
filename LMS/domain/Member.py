# oop 기반의 Member 객체용
# oop: 객체 지향 프로그래밍 - 데이터 + 기능을 하나로 묶어서 다룸
# AUTO_INCREMENT 데이터가 추가될 때 숫자를 자동으로 1씩 올려주는 기능
class Member:

    def __init__(self, id, uid, pw, name, role="user", active=True):
        self.id = id  # DB의 PK -> AUTO_INCREMENT 자동번호 생성
        self.uid = uid  # 아이디
        self.pw = pw  # 비밀번호
        self.name = name  # 이름
        self.role = role  # 권한
        self.active = active  # 활성화 여부
        self.created_at = self.created_at

        # 사용법
        # member = Member("kkw","1234","김기원","user")
        # Member객체를 member변수에 넣음

    @classmethod # self대신 cls라는 객체를 사용 (주소대신 객체)
    def from_db(cls, row: dict):
        #            row : dict(타입 명시) 힌트
        """
        DictCursor로부터 전달받은 딕셔너리 데이터를 Member 객체로 변환합니다.
        """
        if not row:  # cls로 전달된 값이 없으면
            return None

        return cls( # db에 있는 정보를 dict 타입으로 받아와 id에 넣음
            id=row.get('id'),  # id : 2
            uid=row.get('uid'), # uid : kkw
            pw=row.get('password'),  # password : 1111
            name=row.get('name'),    # name : 김기원
            role=row.get('role'),    # role : admin
            active=bool(row.get('active')), # active : 1 -> True
            created_at =  row.get('created_at')
        )

    def is_admin(self):   # role이 admin 인지 확인하는 메서드
        return self.role == "admin"

    def __str__(self): # member객체를 문자열로 출력할 때 사용(테스트용)
        return f"{self.name}({self.uid}:{self.pw}) [{self.role} ]"
    # __str__ = 객체를 print 했을 때 보여줄 설명서
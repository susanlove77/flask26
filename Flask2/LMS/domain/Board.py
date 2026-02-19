class Board:
    def __init__(self, id, title, content, member_id, active=True, writer_name=None, writer_uid=None,created_at=None):
        self.id = id
        self.title = title
        self.content = content
        self.member_id = member_id
        self.active = active  # 삭제 여부 (boolean 1/0)

        # JOIN을 통해 가져올 추가 정보들 (선택 사항)
        self.writer_name = writer_name
        self.writer_uid = writer_uid
        self.created_at = created_at

    @classmethod
    def from_db(cls, row: dict):
        """DB에서 가져온 딕셔너리 데이터를 Board 객체로 변환"""
        if not row: return None

        return cls(
            id=row.get('id'),
            title=row.get('title'),
            content=row.get('content'),
            member_id=row.get('member_id'),
            created_at=row.get('created_at'),  # 날짜 데이터 추가
            active=bool(row.get('active',1)), # 현재 미구현!
            writer_name=row.get('writer_name') if row.get('writer_name') else row.get('name'),
            writer_uid=row.get('writer_uid') if row.get('writer_uid') else row.get('uid')
        )

    def __str__(self): # print(board)로 테스트용
        """목록 출력 시 확인용 (터미널 디버깅용)"""
        writer = self.writer_name if self.writer_name else f"ID:{self.member_id}"
        date_str = self.created_at.strftime('%Y-%m-%d') if self.created_at else "N/A"
        return f"{self.id:<4} | {self.title:<20} | {writer:<10} | {date_str}"
        #  아이디 왼쪽으로 최소 4칸 폭으로 출력  제목 왼쪽으로 20칸 폭으로 출력  글쓴이 왼쪽으로 10칸 폭으로 출력
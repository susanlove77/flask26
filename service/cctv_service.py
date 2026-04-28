# service/cctv_service.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()

class CctvService:
    _session = requests.Session()

    @staticmethod
    def get_its_cctv_data():
        url = "https://openapi.its.go.kr:9443/cctvInfo"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        }

        params = {
            "apiKey": os.getenv("ITS_API_KEY"),
            "type": "ex", # 고속도로: ex, 국도: its
            "cctvType": "1", # 1: 실시간 스트림(HLS/M3U8)
            "minX": "126.50",
            "maxX": "127.50",
            "minY": "37.30",
            "maxY": "37.60",
            "getType": "json"
        }
        
        try:
            print(f"[INFO] ITS API 요청 시작...")
            response = CctvService._session.get(url, params=params, headers=headers, timeout=15)
            response.raise_for_status() # 403, 404 등 에러 발생 시 예외 발생
            
            data = response.json()
            raw_data = data.get("response", {}).get("data", [])
            
            if not raw_data:
                print("[WARN] 해당 범위 내에 CCTV 데이터가 없습니다.")
                return None

            print(f"[SUCCESS] {len(raw_data)}개의 CCTV 데이터를 불러왔습니다.")
            return raw_data # 가공하기 편하게 실제 리스트만 반환
                
        except Exception as e:
            print(f"[CRITICAL] CCTV API 에러: {str(e)}")
            return None
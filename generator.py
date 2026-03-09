import os

# 평택퀵서비스 - 평택 전지역 (읍/면/동/거점) 데이터
pyeongtaek_data = [
    {
        "dist": "고덕신도시",
        "towns": ["삼성전자캠퍼스", "브레인시티", "고덕동", "고덕면", "해창리", "여염리", "좌교리"]
    },
    {
        "dist": "남부권역",
        "towns": ["비전동", "동삭동", "용이동", "세교동", "합정동", "평택역", "유천동", "팽성읍"]
    },
    {
        "dist": "북부권역",
        "towns": ["송탄", "서정동", "지산동", "독곡동", "신장동", "진위면", "서탄면", "중앙동"]
    },
    {
        "dist": "서부권역",
        "towns": ["평택항", "포승공단", "안중읍", "청북읍", "오성면", "현덕면", "포승읍"]
    }
]

def generate_pyeongtaek_pages():
    # 1. 평택 전체 통합 페이지 생성
    reg_folder = "평택퀵서비스"
    os.makedirs(reg_folder, exist_ok=True)
    # 신속한 배송 키워드 반영
    header = "---\nlayout: board\ntown: 평택\ntown_full: 경기도 평택시 신속한 배송\n---"
    with open(f"{reg_folder}/index.html", 'w', encoding='utf-8') as f:
        f.write(header)
    print(f"✔️ 통합 페이지 생성: {reg_folder}")

    # 2. 각 권역 및 동네별 페이지 생성
    for group in pyeongtaek_data:
        dist_name = group['dist']
        
        # 권역별 폴더 생성 (예: 고덕신도시퀵서비스)
        dist_folder = f"{dist_name}퀵서비스"
        os.makedirs(dist_folder, exist_ok=True)
        with open(f"{dist_folder}/index.html", 'w', encoding='utf-8') as f:
            f.write(f"---\nlayout: board\ntown: {dist_name}\ntown_full: 경기도 평택시 {dist_name} 신속한 배송\n---")
        print(f"✔️ 권역 페이지 생성: {dist_folder}")

        for town_name in group['towns']:
            # 동네 폴더 생성 (예: 비전동퀵서비스)
            folder_name = f"{town_name}퀵서비스"
            os.makedirs(folder_name, exist_ok=True)
            
            # 레이아웃 board 유지 및 신속한 배송 정보 삽입
            content = f"---\nlayout: board\ntown: {town_name}\ntown_full: 경기도 평택시 {dist_name} {town_name} 신속한 배송\n---"
            
            with open(f"{folder_name}/index.html", 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✔️ 생성 완료: {folder_name}")

if __name__ == "__main__":
    generate_pyeongtaek_pages()
    print("\n🚀 평택 전지역(읍/면/동/핵심거점) 타겟 페이지 생성이 완료되었습니다!")
    print("✅ 이제 깃허브에 올리시면 평택퀵서비스.8222quick.com에 즉시 반영됩니다.")
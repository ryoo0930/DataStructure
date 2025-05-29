from UnsortedTableMap import UnsortedTableMap  # UnsortedTableMap 클래스 가져오기

def main():
    m = UnsortedTableMap()                       # 빈 맵 생성 :contentReference[oaicite:0]{index=0}

    # 1) 값 설정 (삽입/업데이트)
    m['apple'] = 3                               # 키 'apple'에 값 3 삽입
    m['banana'] = 5                              # 키 'banana'에 값 5 삽입
    m['apple'] = 4                               # 'apple' 값 3 → 4로 업데이트

    # 2) 값 조회
    print("apple:", m['apple'])                  # 출력: apple: 4
    print("banana:", m['banana'])                # 출력: banana: 5

    # 3) 길이 확인
    print("맵 크기:", len(m))                     # 출력: 맵 크기: 2 :contentReference[oaicite:1]{index=1}

    # 4) 반복(iteration)
    print("모든 키와 값:")
    for key in m:
        print(f"  {key} → {m[key]}")

    # 5) 삭제
    del m['banana']                              # 'banana' 항목 삭제
    print("삭제 후 맵:", list(m.items()))         # 출력: 삭제 후 맵: [('apple', 4)]

    # 6) 예외 처리: 없는 키 조회 시 KeyError
    try:
        print(m['orange'])
    except KeyError as e:
        print("예외 발생:", e)

if __name__ == '__main__':
    main()

# 사용자로부터 "남자" 또는 "여자" 라는 문자열 입력받기
Sexual = input("성별을 한글로 입력하세요 (남자/여자):" )

# 입력된 문자일이 "남자"인 경우 "MAN"으로 변환하여 출력
if (Sexual=="남자"):
    print("MAN")
    
# 입력된 문자열이 "여자"인 경우 "WOMAN"으로 변환하여 출력
elif (Sexual=="여자"):
    print("WOMAN")
    
# 이외의 입력에 대해서는 오류 메세지 출력
else :
    print("잘못된 입력입니다.")
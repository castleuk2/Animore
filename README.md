1. terminal에서 pip install pandas, pip install geopy, pip install folium, pip install haversine
2. main.py를 다운로드 후 각 클래스 파일과 함수파일 (*_Class.py, folium_func.py download) 다운로드 main에 import 하는 형식으로 코딩.
   center.csv  파일 저장 후 파일 경로 일치시키고
   프로그램 실행
   -중요점 : 본인의 위치는 도로명 주소(국내 ex:문수로 362, 강서구 화곡동 333 등)로 작성하여야 하며 원하는 병원의 지역을 입력할 때는 서울의 지역(강서구, 은평구 등) 을 입력해야 프로그램이 원활히 진행됨
4. -	프로그램에 대한 개요(Block diagram)
고객의 이름, 전화번호, 주소/ Pet의 Info를 획득
원하는 지역(서울)의 주소를 입력한 이후 해당 지역의 병원 리스트가 제시됨
해당리스트가 지도에 표시된다. (Webbrowser를 통해 자동화)
각 지역의 지점을 클릭하면 해당 지점까지의 거리가 표시되며 이를 참고하여 병원을 선택하고
예약을 진행한다.
예약을 진행한 이후/ 리뷰를 작성하는 탭으로 넘어가서
평점과 리뷰를 입력하면
해당내용이 csv파일에 반영이 된다.
-	Main advantage
위치(집과의 거리)를 통한 선택의 편리화, 자체적으로 개발한 process, 소비자가 남긴 리뷰/평점이 유지되어 이를 통해 이후 고객의 더 좋은 선택을 도움
-	제작 Part
각각의 system에 대한 개발방식(opensource or 자체개발)을 표를 통해서 확인할 수 있으며
일부 part에 대해서는 공동개발이 필요하여 해당부분의 내용을 작성함
-	Demo 영상 제작
시뮬레이션을 통하여 어떤 방식으로 진행/저장 되는가에 대하여 촬영
-	참고부문
python-visualization/folium: Python Data. Leaflet.js Maps. (github.com) 
깃허브에 올라온 folium관련 플러그인과 내용들을 참고하여 제작하였다.


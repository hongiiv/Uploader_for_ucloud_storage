# ucloud biz storage python uploader

본 업로더는 python을 이용한 ucloud biz 업로드 기능을 구현한 것입니다.

* 몇몇 기능들은 CloudStack User API와 호환되지 않습니다. (예, listAvailableProductTYpes는 cloud biz User API에만 있음)
* 자세한 API에 대한 기능은 http://cloudincubation.olleh.com/index.html Cloud Incubation Center 홈페이지를 참고

## Requirements

## Usage
사용자 인증에 사용할 토큰을 생성
$ curl -v -H "X-Storage-User:유저이메일주소" -H "X-Storage-Pass:발급받은 API KEY" ssproxy.ucloudbiz.olleh.com/auth/v1.0

이에 대한 응답으로 헤더에 
X-Storage-Token: 토큰

스토리지에 대한 URL이 JSON 형태로 응답됨
{"storage": {"default": "local", "local": "https://ssproxy.ucloudbiz.olleh.com/v1/AUTH_637fcd45-c87e-4d9a-bfdd-385cff5bc5e7"}}

uploader.py 소스코드의
headers['X-Auth-Token']='헤더에 응답 받은 토큰을 입력'
path="스토리지의 URL을 도메인을 뺀 나머지 부분을 다음의 형식으로 입력 v1/~~~/컨테이너명/{파일명은 입력받은 파일명이 자동 입력}"

$ python uploader.py 업로드할파일명

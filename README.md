## Use SSL in FLASK APP

pip install pyopenssl

```buildoutcfg
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(ssl_context='adhoc')
```

```buildoutcfg
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(ssl_context=('cert.pem', 'key.pem'))
```

### SERVER SETTING

- 이 명령어에 대해 알아보자.
```
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
```
- x509 포맷의 인증서를
- rsa 4096의 개인키를 만들고 key.pem, 365일 인증서를 cert.pem








---
### OPENSSL 사용법

OpenSSL은 : SSL v2/v3와 TLS v1 프로토콜을 지원하는 범용 암호법 라이브러리이다.

 대부분 리눅스 배포판에 기본 설치 되어 있음.

1. 개인키생성

 1) 3DES 로 암호화(PassPhrase필요)

    openssl genrsa -des3 -out 키이름.key 1024

 2) 암호화 하지 않음

    openssl genrsa -out 파일이름.key 1024

 3) 기존 비밀키에 패스워드 추가

    openssl rsa -in out 키이름.key -des3 -out 새로운키이름.key

 4) 기존 비밀키에 패스워드 제거

    openssl rsa -in 키이름.key -out 새로운키이름.key

​

2. CSR생성 (인증서 서명 요청을 위해 필요)

  openssl req -new -key 키이름.key -out csr이름.csr

​

3. 자체 서명 인증서 생성하기

  openssl req -new -key 키이름.key -x509 -out 인증서이름.crt

  openssl req -new -x509 -nodes -sha1 -days 365 -key server.key -out server.crt

​

4. 인증서 다루는 법

  1) 인증서 확인(보기)

    openssl x509 -noout -text -in 인증서파일.crt

  2) 비밀키 보기

    openssl rsa -noout -text -in 키파일.key

※ 아파치가 설치되어 있고 SSL모듈이 있으면 개인키 및 CSR 코드만 생성하면 된다.
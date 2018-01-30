		===============================================================
		|| 	BoB 6th Digital_Forensic 3rd Stage Assignment	     ||
		||							     ||
		||	    Category : Tech 	      No. 06		     ||	
		||							     ||
		||		@Author : L3ad0xff (Lee Moonwon)	     ||
		||							     ||
		||	      Cybercrime-related server information	     ||
		||	        gathering tool : What is that's ip?	     ||
		===============================================================

  모든 개발은 python3.6 환경에서 이루어졌다.
  아래 python code를 실행 시키기 위해서는 추가 모듈이 필요하다.

======================================= 환경설정 ================================================

  1. Linux (Linux kali 4.9.0-kali3-amd64 #1 Debian 4.9.18-1kali1)
	- Linux 터미널 창에서 다음과 같이 python3.6 설치
		1) wget https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tgz
		2) tar xvfz Python-3.6.4.tgz 
		3) cd Python-3.6.4/
		4) /configure
		5) make
	- 다음과 같은 명령어로 python3를 명령어로 실행할 수 있도록 설정
		1) cd /usr/bin/
		2) ln -s /root/Python-3.6.4/python ./python3
	- 필요한 Module 설치
		1) pip3 install pandas
		2) pip3 install dnspython

  2. Window (for running GUI)
	- Window환경에서 python3를 설치, 실행 경로 지정
	- cmd화면에서 pip3 install pandas을 실행 (pandas 모듈 설치)
	- cmd화면에서 pip3 install dnspython 실행 (dns 모듈 설치)
	- cmd화면에서 pip3 install PyQt5 실행 (QT Designer에서 생성한 layout을 python과 연동)
	  (단, python2와 같이 설치 되어 있을 경우 pip3를 이용하여 실행)
	- python2와 함께 설치가 되어 있을 경우 cmd에서 python 입력 시 python3가 실행되도록 설정



======================================== 실행방법 ===============================================

  DNS_Query를 이용하여 IP 주소를 획득하는 것은 linux 환경에서만 사용한다.

  Linux kali 4.9.0-kali3-amd64 #1 Debian 4.9.18-1kali1

  1. start.py 파일과 DNS_Query.py 파일을 같은 경로에 놓는다.

  2. start.py : DNS_Query.py를 백그라운드에서 실행 시킨다.
	- Linux : Terminal 창에서 python3 start.py를 실행
		-> 'fl0ckfl0ck.csv' 파일 생성한다. (해당 파일이 없을 경우)

======================================== GUI 실행 ===============================================

  1. GUI_dns_query.py를 실행한다.
	- Linux : python3 GUI_dns_query.py
	- Window : python GUI_dns_quert.py

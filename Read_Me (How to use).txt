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

  ��� ������ python3.6 ȯ�濡�� �̷������.
  �Ʒ� python code�� ���� ��Ű�� ���ؼ��� �߰� ����� �ʿ��ϴ�.

======================================= ȯ�漳�� ================================================

  1. Linux (Linux kali 4.9.0-kali3-amd64 #1 Debian 4.9.18-1kali1)
	- Linux �͹̳� â���� ������ ���� python3.6 ��ġ
		1) wget https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tgz
		2) tar xvfz Python-3.6.4.tgz 
		3) cd Python-3.6.4/
		4) /configure
		5) make
	- ������ ���� ��ɾ�� python3�� ��ɾ�� ������ �� �ֵ��� ����
		1) cd /usr/bin/
		2) ln -s /root/Python-3.6.4/python ./python3
	- �ʿ��� Module ��ġ
		1) pip3 install pandas
		2) pip3 install dnspython

  2. Window (for running GUI)
	- Windowȯ�濡�� python3�� ��ġ, ���� ��� ����
	- cmdȭ�鿡�� pip3 install pandas�� ���� (pandas ��� ��ġ)
	- cmdȭ�鿡�� pip3 install dnspython ���� (dns ��� ��ġ)
	- cmdȭ�鿡�� pip3 install PyQt5 ���� (QT Designer���� ������ layout�� python�� ����)
	  (��, python2�� ���� ��ġ �Ǿ� ���� ��� pip3�� �̿��Ͽ� ����)
	- python2�� �Բ� ��ġ�� �Ǿ� ���� ��� cmd���� python �Է� �� python3�� ����ǵ��� ����



======================================== ������ ===============================================

  DNS_Query�� �̿��Ͽ� IP �ּҸ� ȹ���ϴ� ���� linux ȯ�濡���� ����Ѵ�.

  Linux kali 4.9.0-kali3-amd64 #1 Debian 4.9.18-1kali1

  1. start.py ���ϰ� DNS_Query.py ������ ���� ��ο� ���´�.

  2. start.py : DNS_Query.py�� ��׶��忡�� ���� ��Ų��.
	- Linux : Terminal â���� python3 start.py�� ����
		-> 'fl0ckfl0ck.csv' ���� �����Ѵ�. (�ش� ������ ���� ���)

======================================== GUI ���� ===============================================

  1. GUI_dns_query.py�� �����Ѵ�.
	- Linux : python3 GUI_dns_query.py
	- Window : python GUI_dns_quert.py

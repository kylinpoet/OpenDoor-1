这个是我用这个哥们的开源项目所修改，因为他这个项目太多问题了，的需要我自己去修改以一下。主要有

修改记录
------------
    * 支持https
    * 支持http端口，就是这么逗比，官方竟然不支持
    * 不使用动态函数调用，不利于分析
    * http，https连接池，节省资源


OWASP Directory Access scanner
====================
.. image:: http://dl2.joxi.net/drive/2016/08/04/0001/0378/90490/90/4b4470c268.jpg
    :target: http://dl2.joxi.net/drive/2016/08/04/0001/0378/90490/90/4b4470c268.jpg
    

.. image:: https://travis-ci.org/stanislav-web/OpenDoor.svg?branch=master
    :target: https://travis-ci.org/stanislav-web/OpenDoor
.. image:: https://badge.fury.io/py/opendoor.svg
    :target: https://badge.fury.io/py/opendoor
        
This application scans the site directories and find all possible ways to login, empty directories and entry points.
Scans conducted in the dictionary that is included in this application.
This software is written for informational purposes and is an open source product under the GPL license.

**Testing of the software on the commercial systems and organizations is prohibited!**

.. image:: http://dl2.joxi.net/drive/2016/08/12/0001/0378/90490/90/25658c11fe.jpg
    :target: http://dl2.joxi.net/drive/2016/08/12/0001/0378/90490/90/25658c11fe.jpg
    
Requirements
------------
    * Python 2.7.x

Install Dependencies
------------
    sudo pip install -r requirements.txt

Implements
------------
    * multithreading
    * filesystem log
    * detect redirects
    * random user agent
    * random proxy from proxy list
    * verbose mode
    * subdomains scanner

Changelog
------------
    * *v1.0.0* - all the basic functionality is available
    * *v1.0.1* - added debug level as param --debug
    * *v1.2.1* - added filesystem logger (param --log)
    * *v1.2.2* - added example of usage (param --examples)
    * *v1.3.2* - added posibility to use random proxy from proxylist (param --proxy)
    * *v1.3.3* - simplify dependency installation    
    * *v1.3.4* - added code quality watcher    
    * *v1.3.5* - added ReadTimeoutError ProxyError handlers
    * *v1.3.51* - fixed code style, resolve file read errors
    * *v1.3.52* - code docstyle added
    * *v2.3.52* - subdomains scan available! (param --check subdomains). Added databases

Basic usage
------------
    python ./opendoor.py --url "http://joomla-ua.org"

Help
------------
    usage: opendoor.py [-h] [-u URL] [--update] [--examples] [-v] [-c CHECK]
                   [-t THREADS] [-d DELAY] [-r REST] [--debug DEBUG] [-p] [-l]

    optional arguments:
      -h, --help            show this help message and exit
      --update              Update from version control
      --examples            Examples of usage
      -v, --version         Get current version
      -c CHECK, --check CHECK
                        Directory scan eg --check=directories or subdomains
                         (directories by default)
      -t THREADS, --threads THREADS
                        Allowed threads
      -d DELAY, --delay DELAY
                        Delay between requests
      -r REST, --rest REST  Request timeout
      --debug DEBUG         Debug level (0 by default)
      -p, --proxy           Use proxy list
      -l, --log             Use filesystem log

    required named arguments:
      -u URL, --url URL     URL or page to scan; -u http://example.com

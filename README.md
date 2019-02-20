# Transcript

```
lbakken@shostakovich ~/issues/rabbitmq-users/kombu-heartbeat-rb0Lqx1rSSQ_QtWy4gDNAgAJ (master=)
$ git clean -fxd
Removing consumer.log
Removing venv/

lbakken@shostakovich ~/issues/rabbitmq-users/kombu-heartbeat-rb0Lqx1rSSQ_QtWy4gDNAgAJ (master=)
$ virtualenv venv/3.7.2
Using base prefix '/usr'
New python executable in /home/lbakken/issues/rabbitmq-users/kombu-heartbeat-rb0Lqx1rSSQ_QtWy4gDNAgAJ/venv/3.7.2/bin/python
Installing setuptools, pip, wheel...done.

lbakken@shostakovich ~/issues/rabbitmq-users/kombu-heartbeat-rb0Lqx1rSSQ_QtWy4gDNAgAJ (master=)
$ source venv/3.7.2/bin/activate
(3.7.2) lbakken@shostakovich ~/issues/rabbitmq-users/kombu-heartbeat-rb0Lqx1rSSQ_QtWy4gDNAgAJ (master=)
$ pip install oslo-messaging
Collecting oslo-messaging
  Using cached https://files.pythonhosted.org/packages/67/71/b45e07c71dfe16853c903e55649ea83e0106150e4821c8f76d7d17596b7f/oslo.messaging-9.4.0-py2.py3-none-any.whl
Collecting oslo.utils>=3.33.0 (from oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/37/20/6f3738063bab1e7d5e4b3cba91af80fd1d1718ee6e27652707629ae1bc7a/oslo.utils-3.40.2-py2.py3-none-any.whl
Collecting oslo.i18n>=3.15.3 (from oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/ee/aa/2d3774130b3cabeec12df47452753c3aa8d91e1aaa229d872195cc2ba314/oslo.i18n-3.23.0-py2.py3-none-any.whl
Collecting amqp>=2.4.0 (from oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/27/32/5c8a0d355b247446eb73f89c0fa4a22c1832764c0cc9d2bc43b9256d9366/amqp-2.4.1-py2.py3-none-any.whl
Collecting futurist>=1.2.0 (from oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/f7/bb/73e57500a1070753d918513a4936a9519bea6d3cf34439997992f0b50d32/futurist-1.8.0-py2.py3-none-any.whl
Collecting debtcollector>=1.2.0 (from oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/9b/01/fbbe8ad43ffebe5cd75476448b17825e31c4fc7b9b26519571ec91972c5c/debtcollector-1.20.0-py2.py3-none-any.whl
Collecting oslo.config>=5.2.0 (from oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/43/b8/e24031669c2acb0e6bdacf3ea98967f3726a35f94f7efffc37b1a2bd3c96/oslo.config-6.8.0-py2.py3-none-any.whl
Collecting pbr!=2.1.0,>=2.0.0 (from oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/8c/7f/fed53b379500fd889707d1f6e61c2a35e12f2de87396894aff89b017d1d6/pbr-5.1.2-py2.py3-none-any.whl
Collecting oslo.serialization!=2.19.1,>=2.18.0 (from oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/b2/43/6353874dab2b15c0fa6fec1500894c33a24c637e1d068bd1a85268bd2cc2/oslo.serialization-2.28.1-py2.py3-none-any.whl
Collecting PyYAML>=3.12 (from oslo-messaging)
Collecting oslo.middleware>=3.31.0 (from oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/88/d3/95c6c376024a816e40051bb8fd9ba0364a22a23d56bd8e2608598d5371a3/oslo.middleware-3.37.0-py2.py3-none-any.whl
Collecting oslo.service!=1.28.1,>=1.24.0 (from oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/5a/89/fd0c481461fca0eaf9760f32c00da2c2642da94e0993c18ec9a751346013/oslo.service-1.37.0-py2.py3-none-any.whl
Collecting stevedore>=1.20.0 (from oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/35/fa/8683fab2a6e15ecfe107996e56fab91e52fe3ec0b40ca9440a0e1ffe6892/stevedore-1.30.0-py2.py3-none-any.whl
Collecting kombu!=4.0.2,>=4.0.0 (from oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/29/48/c709a54c8533ed46fd868e593782c6743da33614f8134b82bc0955455031/kombu-4.3.0-py2.py3-none-any.whl
Collecting cachetools>=2.0.0 (from oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/39/2b/d87fc2369242bd743883232c463f28205902b8579cb68dcf5b11eee1652f/cachetools-3.1.0-py2.py3-none-any.whl
Collecting six>=1.10.0 (from oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/73/fb/00a976f728d0d1fecfe898238ce23f502a721c0ac0ecfedb80e0d88c64e9/six-1.12.0-py2.py3-none-any.whl
Collecting WebOb>=1.7.1 (from oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/06/e1/4acd2b4327fceb4c6446bdbca515f807ab83188526fd654940c00bcf8cc3/WebOb-1.8.5-py2.py3-none-any.whl
Collecting oslo.log>=3.36.0 (from oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/b9/b6/f38ed638c90cd4647d19c2cfd355f1f211aa89ca89a63ae4c43e3e0a3602/oslo.log-3.42.2-py2.py3-none-any.whl
Collecting iso8601>=0.1.11 (from oslo.utils>=3.33.0->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/ef/57/7162609dab394d38bbc7077b7ba0a6f10fb09d8b7701ea56fa1edc0c4345/iso8601-0.1.12-py2.py3-none-any.whl
Collecting netifaces>=0.10.4 (from oslo.utils>=3.33.0->oslo-messaging)
Collecting netaddr>=0.7.18 (from oslo.utils>=3.33.0->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/ba/97/ce14451a9fd7bdb5a397abf99b24a1a6bb7a1a440b019bebd2e9a0dbec74/netaddr-0.7.19-py2.py3-none-any.whl
Collecting pytz>=2013.6 (from oslo.utils>=3.33.0->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/61/28/1d3920e4d1d50b19bc5d24398a7cd85cc7b9a75a490570d5a30c57622d34/pytz-2018.9-py2.py3-none-any.whl
Collecting pyparsing>=2.1.0 (from oslo.utils>=3.33.0->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/de/0a/001be530836743d8be6c2d85069f46fecf84ac6c18c7f5fb8125ee11d854/pyparsing-2.3.1-py2.py3-none-any.whl
Collecting Babel!=2.4.0,>=2.3.4 (from oslo.i18n>=3.15.3->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/b8/ad/c6f60602d3ee3d92fbed87675b6fb6a6f9a38c223343ababdb44ba201f10/Babel-2.6.0-py2.py3-none-any.whl
Collecting vine>=1.1.3 (from amqp>=2.4.0->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/62/dd/e30f828a39914626d67876b987d6fc47616b64de680cd0f746fc9c8aab47/vine-1.2.0-py2.py3-none-any.whl
Collecting PrettyTable<0.8,>=0.7.1 (from futurist>=1.2.0->oslo-messaging)
Collecting wrapt>=1.7.0 (from debtcollector>=1.2.0->oslo-messaging)
Collecting requests>=2.18.0 (from oslo.config>=5.2.0->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/7d/e3/20f3d364d6c8e5d2353c72a67778eb189176f08e873c9900e10c0287b84b/requests-2.21.0-py2.py3-none-any.whl
Collecting rfc3986>=1.2.0 (from oslo.config>=5.2.0->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/e1/59/1d547e9e5e1bf8074951067c3d6b31a2e29fd5b49bd7d32e53ff0da6406c/rfc3986-1.2.0-py2.py3-none-any.whl
Collecting msgpack>=0.5.2 (from oslo.serialization!=2.19.1,>=2.18.0->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/a8/7b/630049fc4af9e68a625738612edc264ce7cb586c5001a2d4d2209a4f61c1/msgpack-0.6.1-cp37-cp37m-manylinux1_x86_64.whl
Collecting statsd>=3.2.1 (from oslo.middleware>=3.31.0->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/47/33/c824f799128dfcfce2142f18d9bc6c55c46a939f6e4250639134222d99eb/statsd-3.3.0-py2.py3-none-any.whl
Collecting oslo.context>=2.19.2 (from oslo.middleware>=3.31.0->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/7c/c9/937cdf551431ae7bec6be7d72d18a0558a1d1f8ceb43e0f8e2c73d8d220a/oslo.context-2.22.0-py2.py3-none-any.whl
Collecting Jinja2>=2.10 (from oslo.middleware>=3.31.0->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/7f/ff/ae64bacdfc95f27a016a7bed8e8686763ba4d277a78ca76f32659220a731/Jinja2-2.10-py2.py3-none-any.whl
Collecting PasteDeploy>=1.5.0 (from oslo.service!=1.28.1,>=1.24.0->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/67/0c/faa9971b2e5e048b3b30008d04c72e4d5f63b42f48937c169acce2c5e70a/PasteDeploy-2.0.1-py2.py3-none-any.whl
Collecting Paste>=2.0.2 (from oslo.service!=1.28.1,>=1.24.0->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/80/fe/46e078c17d1c20c4ed706c77137311f6df0be3e5a0e4cd0c2f0851e34c16/Paste-3.0.6-py2.py3-none-any.whl
Collecting oslo.concurrency>=3.25.0 (from oslo.service!=1.28.1,>=1.24.0->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/86/1e/555fe1435c665fc3c067a18f7e1fcb768e945f35ff8c19ecbdadfbc98ee9/oslo.concurrency-3.29.0-py2.py3-none-any.whl
Collecting Yappi>=0.98 (from oslo.service!=1.28.1,>=1.24.0->oslo-messaging)
Collecting eventlet!=0.18.3,!=0.20.1,>=0.18.2 (from oslo.service!=1.28.1,>=1.24.0->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/86/7e/96e1412f96eeb2f2eca9342dcc4d5bc9305880a448b603b0a8e54439b71c/eventlet-0.24.1-py2.py3-none-any.whl
Collecting greenlet>=0.4.10 (from oslo.service!=1.28.1,>=1.24.0->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/9d/ef/ac10aa1293f64939e4511909c570d969566126214af5dd7ba0afd353d88b/greenlet-0.4.15-cp37-cp37m-manylinux1_x86_64.whl
Collecting fixtures>=3.0.0 (from oslo.service!=1.28.1,>=1.24.0->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/a8/28/7eed6bf76792f418029a18d5b2ace87ce7562927cdd00f1cefe481cd148f/fixtures-3.0.0-py2.py3-none-any.whl
Collecting Routes>=2.3.1 (from oslo.service!=1.28.1,>=1.24.0->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/50/50/c1c0666778c7986368896b0e0f640e41160a43cd3ffc7ff008f61f0f6cfd/Routes-2.4.1-py2.py3-none-any.whl
Collecting monotonic>=1.4 (from oslo.log>=3.36.0->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/ac/aa/063eca6a416f397bd99552c534c6d11d57f58f2e94c14780f3bbf818c4cf/monotonic-1.5-py2.py3-none-any.whl
Collecting python-dateutil>=2.7.0 (from oslo.log>=3.36.0->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/41/17/c62faccbfbd163c7f57f3844689e3a78bae1f403648a6afb1d0866d87fbb/python_dateutil-2.8.0-py2.py3-none-any.whl
Collecting pyinotify>=0.9.6; sys_platform != "win32" and sys_platform != "darwin" and sys_platform != "sunos5" (from oslo.log>=3.36.0->oslo-messaging)
Collecting idna<2.9,>=2.5 (from requests>=2.18.0->oslo.config>=5.2.0->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/14/2c/cd551d81dbe15200be1cf41cd03869a46fe7226e7450af7a6545bfc474c9/idna-2.8-py2.py3-none-any.whl
Collecting certifi>=2017.4.17 (from requests>=2.18.0->oslo.config>=5.2.0->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/9f/e0/accfc1b56b57e9750eba272e24c4dddeac86852c2bebd1236674d7887e8a/certifi-2018.11.29-py2.py3-none-any.whl
Collecting chardet<3.1.0,>=3.0.2 (from requests>=2.18.0->oslo.config>=5.2.0->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl
Collecting urllib3<1.25,>=1.21.1 (from requests>=2.18.0->oslo.config>=5.2.0->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/62/00/ee1d7de624db8ba7090d1226aebefab96a2c71cd5cfa7629d6ad3f61b79e/urllib3-1.24.1-py2.py3-none-any.whl
Collecting MarkupSafe>=0.23 (from Jinja2>=2.10->oslo.middleware>=3.31.0->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/e4/c4/adcc2d6f2ac2146cc04e076f14f1006c1de8e1e747fa067668b6573000b8/MarkupSafe-1.1.0-cp37-cp37m-manylinux1_x86_64.whl
Collecting fasteners>=0.7.0 (from oslo.concurrency>=3.25.0->oslo.service!=1.28.1,>=1.24.0->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/14/3a/096c7ad18e102d4f219f5dd15951f9728ca5092a3385d2e8f79a7c1e1017/fasteners-0.14.1-py2.py3-none-any.whl
Collecting dnspython>=1.15.0 (from eventlet!=0.18.3,!=0.20.1,>=0.18.2->oslo.service!=1.28.1,>=1.24.0->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/ec/d3/3aa0e7213ef72b8585747aa0e271a9523e713813b9a20177ebe1e939deb0/dnspython-1.16.0-py2.py3-none-any.whl
Collecting testtools>=0.9.22 (from fixtures>=3.0.0->oslo.service!=1.28.1,>=1.24.0->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/87/74/a4d55da28d7bba6d6f49430f22a62afd8472cb24a63fa61daef80d3e821b/testtools-2.3.0-py2.py3-none-any.whl
Collecting repoze.lru>=0.3 (from Routes>=2.3.1->oslo.service!=1.28.1,>=1.24.0->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/b0/30/6cc0c95f0b59ad4b3b9163bff7cdcf793cc96fac64cf398ff26271f5cf5e/repoze.lru-0.7-py3-none-any.whl
Collecting unittest2>=1.0.0 (from testtools>=0.9.22->fixtures>=3.0.0->oslo.service!=1.28.1,>=1.24.0->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/72/20/7f0f433060a962200b7272b8c12ba90ef5b903e218174301d0abfd523813/unittest2-1.1.0-py2.py3-none-any.whl
Collecting extras>=1.0.0 (from testtools>=0.9.22->fixtures>=3.0.0->oslo.service!=1.28.1,>=1.24.0->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/03/e9/e915af1f97914cd0bc021e125fd1bfd4106de614a275e4b6866dd9a209ac/extras-1.0.0-py2.py3-none-any.whl
Collecting python-mimeparse (from testtools>=0.9.22->fixtures>=3.0.0->oslo.service!=1.28.1,>=1.24.0->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/26/2e/03bce213a9bf02a2750dcb04e761785e9c763fc11071edc4b447eacbb842/python_mimeparse-1.6.0-py2.py3-none-any.whl
Collecting traceback2 (from testtools>=0.9.22->fixtures>=3.0.0->oslo.service!=1.28.1,>=1.24.0->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/17/0a/6ac05a3723017a967193456a2efa0aa9ac4b51456891af1e2353bb9de21e/traceback2-1.4.0-py2.py3-none-any.whl
Collecting argparse (from unittest2>=1.0.0->testtools>=0.9.22->fixtures>=3.0.0->oslo.service!=1.28.1,>=1.24.0->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/f2/94/3af39d34be01a24a6e65433d19e107099374224905f1e0cc6bbe1fd22a2f/argparse-1.4.0-py2.py3-none-any.whl
Collecting linecache2 (from traceback2->testtools>=0.9.22->fixtures>=3.0.0->oslo.service!=1.28.1,>=1.24.0->oslo-messaging)
  Using cached https://files.pythonhosted.org/packages/c7/a3/c5da2a44c85bfbb6eebcfc1dde24933f8704441b98fdde6528f4831757a6/linecache2-1.0.0-py2.py3-none-any.whl
Installing collected packages: pytz, Babel, six, pbr, oslo.i18n, iso8601, netifaces, netaddr, wrapt, debtcollector, pyparsing, oslo.utils, vine, amqp, PrettyTable, futurist, idna, certifi, chardet, urllib3, requests, PyYAML, stevedore, rfc3986, oslo.config, msgpack, oslo.serialization, statsd, oslo.context, MarkupSafe, Jinja2, WebOb, oslo.middleware, PasteDeploy, Paste, monotonic, fasteners, oslo.concurrency, Yappi, greenlet, dnspython, eventlet, linecache2, traceback2, argparse, unittest2, extras, python-mimeparse, testtools, fixtures, repoze.lru, Routes, python-dateutil, pyinotify, oslo.log, oslo.service, kombu, cachetools, oslo-messaging
Successfully installed Babel-2.6.0 Jinja2-2.10 MarkupSafe-1.1.0 Paste-3.0.6 PasteDeploy-2.0.1 PrettyTable-0.7.2 PyYAML-3.13 Routes-2.4.1 WebOb-1.8.5 Yappi-1.0 amqp-2.4.1 argparse-1.4.0 cachetools-3.1.0 certifi-2018.11.29 chardet-3.0.4 debtcollector-1.20.0 dnspython-1.16.0 eventlet-0.24.1 extras-1.0.0 fasteners-0.14.1 fixtures-3.0.0 futurist-1.8.0 greenlet-0.4.15 idna-2.8 iso8601-0.1.12 kombu-4.3.0 linecache2-1.0.0 monotonic-1.5 msgpack-0.6.1 netaddr-0.7.19 netifaces-0.10.9 oslo-messaging oslo.concurrency-3.29.0 oslo.config-6.8.0 oslo.context-2.22.0 oslo.i18n-3.23.0 oslo.log-3.42.2 oslo.middleware-3.37.0 oslo.serialization-2.28.1 oslo.service-1.37.0 oslo.utils-3.40.2 pbr-5.1.2 pyinotify-0.9.6 pyparsing-2.3.1 python-dateutil-2.8.0 python-mimeparse-1.6.0 pytz-2018.9 repoze.lru-0.7 requests-2.21.0 rfc3986-1.2.0 six-1.12.0 statsd-3.3.0 stevedore-1.30.0 testtools-2.3.0 traceback2-1.4.0 unittest2-1.1.0 urllib3-1.24.1 vine-1.2.0 wrapt-1.11.1
(3.7.2) lbakken@shostakovich ~/issues/rabbitmq-users/kombu-heartbeat-rb0Lqx1rSSQ_QtWy4gDNAgAJ (master=)
(reverse-i-search)`rm': ^C rabbitmq.config
(3.7.2) lbakken@shostakovich ~/issues/rabbitmq-users/kombu-heartbeat-rb0Lqx1rSSQ_QtWy4gDNAgAJ (master=)
$ pip list
Package            Version
------------------ ----------
amqp               2.4.1
Babel              2.6.0
cachetools         3.1.0
certifi            2018.11.29
chardet            3.0.4
debtcollector      1.20.0
dnspython          1.16.0
eventlet           0.24.1
extras             1.0.0
fasteners          0.14.1
fixtures           3.0.0
futurist           1.8.0
greenlet           0.4.15
idna               2.8
iso8601            0.1.12
Jinja2             2.10
kombu              4.3.0
linecache2         1.0.0
MarkupSafe         1.1.0
monotonic          1.5
msgpack            0.6.1
netaddr            0.7.19
netifaces          0.10.9
oslo.concurrency   3.29.0
oslo.config        6.8.0
oslo.context       2.22.0
oslo.i18n          3.23.0
oslo.log           3.42.2
oslo.messaging     9.4.0
oslo.middleware    3.37.0
oslo.serialization 2.28.1
oslo.service       1.37.0
oslo.utils         3.40.2
Paste              3.0.6
PasteDeploy        2.0.1
pbr                5.1.2
pip                19.0.2
prettytable        0.7.2
pyinotify          0.9.6
pyparsing          2.3.1
python-dateutil    2.8.0
python-mimeparse   1.6.0
pytz               2018.9
PyYAML             3.13
repoze.lru         0.7
requests           2.21.0
rfc3986            1.2.0
Routes             2.4.1
setuptools         40.8.0
six                1.12.0
statsd             3.3.0
stevedore          1.30.0
testtools          2.3.0
traceback2         1.4.0
unittest2          1.1.0
urllib3            1.24.1
vine               1.2.0
WebOb              1.8.5
wheel              0.33.1
wrapt              1.11.1
yappi              1.0

(3.7.2) lbakken@shostakovich ~/issues/rabbitmq-users/kombu-heartbeat-rb0Lqx1rSSQ_QtWy4gDNAgAJ (master=)
$ python ./server-net-hb.py
Traceback (most recent call last):
  File "./server-net-hb.py", line 135, in <module>
    if parser.tf_queue_name:
AttributeError: 'Namespace' object has no attribute 'tf_queue_name'
```

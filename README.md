Для розробки сценаріїв використано Python3.12 і стандартну бібліотеку numpy.
# C:\Users\User\AppData\Local\Programs\Python\Python312\Scripts\

```powershell
PS> python -m venv azwenv
PS> azwenv/Scripts/activate
(azenv)PS> pip install -r requirements.txt
(azenv)PS> pip install numpy
(azenv)PS> pip show numpy
Name: numpy
Version: 2.4.6
Summary: Fundamental package for array computing in Python
Home-page: https://numpy.org
Author: Travis E. Oliphant et al.
Author-email: 
License-Expression: BSD-3-Clause AND 0BSD AND MIT AND Zlib AND CC0-1.0
Location: D:\Project\code\260521-numpy\azwenv\Lib\site-packages
Requires: 
Required-by:
(azenv)PS> pip freeze > requirements.txt
(azenv)PS> deactivate
```
or
```bash
python -m venv azwenv
source az_env/bin/activate
(az_env)$ pip install -r requirements.txt
(az_env)$ pip freeze > requirements.txt
(az_env)$ deactivate
```
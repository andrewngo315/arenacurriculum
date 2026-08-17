# 11. Virtual Environment (do, don't code)

This chapter has nothing to assert. Do it in a terminal, paste the output under each
step, and the runner will mark it done once every `OUTPUT:` block is filled in.

The book uses the third-party `virtualenv` tool; `python3 -m venv` is the stdlib
equivalent and is what ARENA uses — same activate, same deactivate, same isolation.

## 1. Make one

The venv command itself is silent — paste the `ls` output.

```
python3 -m venv /tmp/scratchenv
ls /tmp/scratchenv/bin
```

OUTPUT:
```
Activate.ps1    activate        activate.csh    activate.fish   pip             pip3            pip3.9          python          python3         python3.9
```

## 2. Activate it, and prove you're inside it

```
source /tmp/scratchenv/bin/activate
which python
python -c "import sys; print(sys.prefix)"
```

OUTPUT:
```
/tmp/scratchenv/bin/python
/private/tmp/scratchenv
```

## 3. Install something and show it's isolated

```
pip install requests
python -c "import requests; print(requests.__file__)"
```

OUTPUT:
```
(scratchenv) andrew@Andrews-MacBook ARENA % pip install requests
python -c "import requests; print(requests.__file__)"
Collecting requests
  Downloading requests-2.32.5-py3-none-any.whl (64 kB)
     |████████████████████████████████| 64 kB 4.3 MB/s 
Collecting certifi>=2017.4.17
  Downloading certifi-2026.7.22-py3-none-any.whl (136 kB)
     |████████████████████████████████| 136 kB 18.7 MB/s 
Collecting idna<4,>=2.5
  Downloading idna-3.18-py3-none-any.whl (65 kB)
     |████████████████████████████████| 65 kB 20.4 MB/s 
Collecting charset_normalizer<4,>=2
  Downloading charset_normalizer-3.5.1-cp39-cp39-macosx_10_9_universal2.whl (368 kB)
     |████████████████████████████████| 368 kB 51.7 MB/s 
Collecting urllib3<3,>=1.21.1
  Downloading urllib3-2.6.3-py3-none-any.whl (131 kB)
     |████████████████████████████████| 131 kB 30.6 MB/s 
Installing collected packages: urllib3, idna, charset-normalizer, certifi, requests
Successfully installed certifi-2026.7.22 charset-normalizer-3.5.1 idna-3.18 requests-2.32.5 urllib3-2.6.3
WARNING: You are using pip version 21.2.4; however, version 26.0.1 is available.
You should consider upgrading via the '/private/tmp/scratchenv/bin/python3 -m pip install --upgrade pip' command.
/private/tmp/scratchenv/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(
/private/tmp/scratchenv/lib/python3.9/site-packages/requests/__init__.py
```

## 4. Deactivate and compare where `requests` comes from

Both imports work — that is the point. Compare the two paths: inside the venv
`requests` came from `/tmp/scratchenv/...`, outside it comes from your system
site-packages. Note `python3`, not `python` — outside a venv there is no bare
`python` on this machine, and that PATH change is exactly what activation does.

```
deactivate
python3 -c "import requests; print(requests.__file__)"
```

OUTPUT:
```
/Users/andrew/Library/Python/3.9/lib/python/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(
/Users/andrew/Library/Python/3.9/lib/python/site-packages/requests/__init__.py
```

## 5. In one sentence, why does ARENA want you using one?

ANSWER: No idea
Self-correction: A virtual environment allows isolation between projects that have different requirements. 

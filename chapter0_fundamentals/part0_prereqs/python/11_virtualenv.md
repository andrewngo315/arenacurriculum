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
```

## 2. Activate it, and prove you're inside it

```
source /tmp/scratchenv/bin/activate
which python
python -c "import sys; print(sys.prefix)"
```

OUTPUT:
```
```

## 3. Install something and show it's isolated

```
pip install requests
python -c "import requests; print(requests.__file__)"
```

OUTPUT:
```
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
```

## 5. In one sentence, why does ARENA want you using one?

ANSWER:

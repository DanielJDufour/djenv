import json
import os
import re
import simple_env as se

for k in os.environ:
    if k not in ['SETTINGS_MODULE']:
        if re.match(r'^DJANGO_[A-Z][A-Z_]+[A-Z]$', k):
            v = se.get(k)

            if isinstance(v, str):
                v = v.strip() # remove excess white space
                if ((v.startswith("{") and v.endswith("}")) or (v.startswith("[") and v.endswith("]"))):
                    v = json.loads(v)

            globals()[k.replace("DJANGO_", "")] = v

del k
del json
del os
del re
del v
del se

import subprocess
import json

jsonString = "{\"passage\": \"Mr. John Allen hereby sells the property on Baker road to Mrs. Ashley Henderson for a sum of $60,000 under the condition that she does not get a pet animal in the premises\", \"question\": \"Who is selling?\"}"
open('/home/heisenberg/projects/codefundo/paralegal/data/all.jsonl', 'a').write(str(jsonString));
open('/home/heisenberg/projects/codefundo/paralegal/data/tmp.jsonl', 'w').write(str(jsonString));
subprocess.call(["python3.6", "-m", "allennlp.run", "predict", "bidaf-model-2017.09.15-charpad.tar.gz", "data/tmp.jsonl"])

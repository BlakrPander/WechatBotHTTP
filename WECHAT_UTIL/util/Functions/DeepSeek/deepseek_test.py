import json
from DeepSeekClient import DeepSeekClient as dsc
from collections import deque

with open('configurations.json', 'r') as configurations:
	config=json.load(configurations)
	api_key = config['api-key']
	system_prompt = config['system_prompt']

# with open('system_prompt.json', 'r', encoding='utf-8') as file:
# 	system_prompt_json=json.load(file)
# 	system_prompt=json.dumps(system_prompt_json,ensure_ascii=False)

max_history=10
user_prompt=input()
history=deque(maxlen=max_history)
history.append(
	{"role":"user","content":user_prompt}
)

client=dsc()

# system_prompt = json.dumps(str(system_prompt_string))
# user_prompt="哎好想打游戏啊"
while user_prompt:
	message=[{"role":"system","content":system_prompt}]
	message.extend(list(history))
	# print(message)
	response = client.generateReply(
		prompt=str(message),
		temperature=0.85,  # 适当提高随机性
		max_tokens=300,
		top_p=0.9,
		presence_penalty=0.4  # 允许适度重复萌点
	)
	respond=response
	print(respond)
	history.append({"role":"assistant","content":respond})
	user_prompt=input()
	history.append({"role":"assistant","content":user_prompt})

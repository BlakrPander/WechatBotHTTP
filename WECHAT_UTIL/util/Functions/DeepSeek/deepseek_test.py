#coding=gbk
import json
from DeepSeekClient import DeepSeekClient as dsc
from collections import deque

with open('configurations.json', 'r') as configurations:
    config=json.load(configurations)
    api_key = config['api-key']

with open('system_prompt.json', 'r', encoding='utf-8') as file:
    system_prompt_json=json.load(file)
    system_prompt=json.dumps(system_prompt_json,ensure_ascii=False)

max_history=10
user_prompt=input()
history=deque(maxlen=max_history)
history.append(
    {"role":"user","content":user_prompt}
)

client=()

# system_prompt = json.dumps(str(system_prompt_string))
# user_prompt="���������Ϸ��"
while user_prompt:
    message=[{"role":"system","content":system_prompt}]
    message.extend(list(history))
    # print(message)
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=message,
        temperature=0.85,  # �ʵ���������
        max_tokens=300,
        top_p=0.9,
        presence_penalty=0.4  # �����ʶ��ظ��ȵ�
    )
    respond=response.choices[0].message.content.strip()
    print(respond)
    history.append({"role":"assistant","content":respond})
    user_prompt=input()
    history.append({"role":"assistant","content":user_prompt})

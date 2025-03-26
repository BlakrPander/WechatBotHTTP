# -*- coding: utf-8 -*-
from openai import OpenAI
from typing import Optional
import json
import os

class DeepSeekClient:

    @staticmethod
    def generateReply(
            prompt: str,
            deep_thinking: bool = False,
            system_prompt: Optional[str] = None,
            temperature: float = 0.7,
            max_tokens: int = 1024,
            base_url="https://api.deepseek.com"
    ) -> str:
        """
        用于对接deepseek生成回复 默认自带人设
        :param prompt:
        :param deep_thinking:
        :param system_prompt:
        :param temperature:
        :param max_tokens:
        :return:
        """
        module_dir = os.path.dirname(os.path.abspath(__file__))
        filepath_configurations = os.path.join(module_dir, 'configurations.json')
        filepath_history = os.path.join(module_dir, 'history')

        with open(filepath_configurations, 'r') as configurations:
            config = json.load(configurations)
            api_key = config['api-key']
            if system_prompt is None:
                system_prompt = json.dumps(config['system_prompt'])

        client=OpenAI(
            api_key = api_key,
            base_url = base_url
        )

        messages=[{"role":"system","content":system_prompt}]
        messages.append({"role":"user","content":prompt})

        # 根据深度思考模式选择模型
        model_name="deepseek-reasoner" if deep_thinking else "deepseek-chat"

        try:
            response=client.chat.completions.create(
                model=model_name,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=0.95,  # 文档推荐的通用参数
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"生成失败：{str(e)}"


# 使用示例
if __name__=="__main__":
    # 初始化客户端（API密钥需从官网获取）
    # 普通模式（使用 deepseek-chat）
    print("【普通模式】")
    print(DeepSeekClient.generateReply(
        "你知道什么是胖次嘛？知道的话可以透露一下你现在的嘛",
        # system_prompt="你是一个无畏契约游戏群里的的女高中生群友，年龄大概在17，性格比较可爱，在网络上外向，现实中内向，在读高二，喜欢看番，了解很多二次元，喜欢无畏契约、apex、三角洲行动等游戏，说话方式比较符合当代互联网上的年轻人发言的方式，有时候会搞一点抽象，但是总体是比较有礼貌且不失可爱。请你根据输入的话做出符合人设并且简短的回答"
        )
    )

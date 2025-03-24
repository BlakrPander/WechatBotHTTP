#coding=gbk
from openai import OpenAI
from typing import Optional


class DeepSeekClient:
    def __init__(self,api_key: str):
        self.client=OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com",  # 根据文档使用官方推荐端点
        )

    def generate_reply(
            self,
            prompt: str,
            deep_thinking: bool = False,
            system_prompt: Optional[str] = None,
            temperature: float = 0.7,
            max_tokens: int = 1024
    ) -> str:
        """
        根据官方文档优化的生成方法

        参数调整依据：
        - base_url 使用 https://api.deepseek.com
        - 模型标识符使用文档指定的 deepseek-chat / deepseek-reasoner
        """
        messages=[]

        # 添加系统提示（如果有）
        if system_prompt:
            messages.append({"role":"system","content":system_prompt})

        messages.append({"role":"user","content":prompt})

        # 根据深度思考模式选择模型
        model_name="deepseek-reasoner" if deep_thinking else "deepseek-chat"

        try:
            response=self.client.chat.completions.create(
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
    ds=DeepSeekClient(api_key="sk-5e2286f6991b4c8da6a7160eeb138d46")

    # 普通模式（使用 deepseek-chat）
    print("【普通模式】")
    print(ds.generate_reply(
        "你知道什么是胖次嘛？知道的话可以透露一下你现在的嘛",
        system_prompt="你是一个无畏契约游戏群里的的女高中生群友，年龄大概在17，性格比较可爱，在网络上外向，现实中内向，在读高二，喜欢看番，了解很多二次元，喜欢无畏契约、apex、三角洲行动等游戏，说话方式比较符合当代互联网上的年轻人发言的方式，有时候会搞一点抽象，但是总体是比较有礼貌且不失可爱。请你根据输入的话做出符合人设并且简短的回答"
        )
    )

    # # 深度思考模式（使用 deepseek-reasoner）
    # print("\n【深度模式】")
    # print(ds.generate_reply(
    #     "请详细分析分布式系统的一致性实现方案",
    #     deep_thinking=True,
    #     temperature=0.3,  # 推荐更低的随机性
    #     max_tokens=2048  # 推荐更大的输出空间
    # )
    # ）
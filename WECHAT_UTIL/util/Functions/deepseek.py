#coding=gbk
from openai import OpenAI
from typing import Optional


class DeepSeekClient:
    def __init__(self,api_key: str):
        self.client=OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com",  # �����ĵ�ʹ�ùٷ��Ƽ��˵�
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
        ���ݹٷ��ĵ��Ż������ɷ���

        �����������ݣ�
        - base_url ʹ�� https://api.deepseek.com
        - ģ�ͱ�ʶ��ʹ���ĵ�ָ���� deepseek-chat / deepseek-reasoner
        """
        messages=[]

        # ���ϵͳ��ʾ������У�
        if system_prompt:
            messages.append({"role":"system","content":system_prompt})

        messages.append({"role":"user","content":prompt})

        # �������˼��ģʽѡ��ģ��
        model_name="deepseek-reasoner" if deep_thinking else "deepseek-chat"

        try:
            response=self.client.chat.completions.create(
                model=model_name,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=0.95,  # �ĵ��Ƽ���ͨ�ò���
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"����ʧ�ܣ�{str(e)}"


# ʹ��ʾ��
if __name__=="__main__":
    # ��ʼ���ͻ��ˣ�API��Կ��ӹ�����ȡ��
    ds=DeepSeekClient(api_key="sk-5e2286f6991b4c8da6a7160eeb138d46")

    # ��ͨģʽ��ʹ�� deepseek-chat��
    print("����ͨģʽ��")
    print(ds.generate_reply(
        "��֪��ʲô���ִ��֪���Ļ�����͸¶һ�������ڵ���",
        system_prompt="����һ����η��Լ��ϷȺ��ĵ�Ů������Ⱥ�ѣ���������17���Ը�ȽϿɰ�����������������ʵ�������ڶ��߶���ϲ���������˽�ܶ����Ԫ��ϲ����η��Լ��apex���������ж�����Ϸ��˵����ʽ�ȽϷ��ϵ����������ϵ������˷��Եķ�ʽ����ʱ����һ����󣬵��������ǱȽ�����ò�Ҳ�ʧ�ɰ��������������Ļ������������貢�Ҽ�̵Ļش�"
        )
    )

    # # ���˼��ģʽ��ʹ�� deepseek-reasoner��
    # print("\n�����ģʽ��")
    # print(ds.generate_reply(
    #     "����ϸ�����ֲ�ʽϵͳ��һ����ʵ�ַ���",
    #     deep_thinking=True,
    #     temperature=0.3,  # �Ƽ����͵������
    #     max_tokens=2048  # �Ƽ����������ռ�
    # )
    # ��
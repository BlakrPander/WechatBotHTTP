

class WECHAT_HTTP_APIS:
    # login check
    WECHAT_IS_LOGIN = 0                         # ��¼���

    # self info
    WECHAT_GET_SELF_INFO = 1                    # ��ȡ������Ϣ

    # send message
    WECHAT_MSG_SEND_TEXT = 2                    # �����ı�
    WECHAT_MSG_SEND_AT = 3                      # ����Ⱥ����
    WECHAT_MSG_SEND_CARD = 4                    # ���������Ƭ
    WECHAT_MSG_SEND_IMAGE = 5                   # ����ͼƬ
    WECHAT_MSG_SEND_FILE = 6                    # �����ļ�
    WECHAT_MSG_SEND_ARTICLE = 7                 # ����xml����
    WECHAT_MSG_SEND_APP = 8                     # ����С����

    # receive message
    WECHAT_MSG_START_HOOK = 9                   # ����������ϢHOOK��ֻ֧��socket����
    WECHAT_MSG_STOP_HOOK = 10                   # �رս�����ϢHOOK
    WECHAT_MSG_START_IMAGE_HOOK = 11            # ����ͼƬ��ϢHOOK
    WECHAT_MSG_STOP_IMAGE_HOOK = 12             # �ر�ͼƬ��ϢHOOK
    WECHAT_MSG_START_VOICE_HOOK = 13            # ����������ϢHOOK
    WECHAT_MSG_STOP_VOICE_HOOK = 14             # �ر�������ϢHOOK

    # contact
    WECHAT_CONTACT_GET_LIST = 15                # ��ȡ��ϵ���б�
    WECHAT_CONTACT_CHECK_STATUS = 16            # ����Ƿ񱻺���ɾ��
    WECHAT_CONTACT_DEL = 17                     # ɾ������
    WECHAT_CONTACT_SEARCH_BY_CACHE = 18         # ���ڴ��л�ȡ������Ϣ
    WECHAT_CONTACT_SEARCH_BY_NET = 19           # ���������û���Ϣ
    WECHAT_CONTACT_ADD_BY_WXID = 20             # wxid�Ӻ���
    WECHAT_CONTACT_ADD_BY_V3 = 21               # v3���ݼӺ���
    WECHAT_CONTACT_ADD_BY_PUBLIC_ID = 22        # ��ע���ں�
    WECHAT_CONTACT_VERIFY_APPLY = 23            # ͨ����������
    WECHAT_CONTACT_EDIT_REMARK = 24             # �޸ı�ע

    # chatroom
    WECHAT_CHATROOM_GET_MEMBER_LIST = 25        # ��ȡȺ��Ա�б�
    WECHAT_CHATROOM_GET_MEMBER_NICKNAME = 26    # ��ȡָ��Ⱥ��Ա�ǳ�
    WECHAT_CHATROOM_DEL_MEMBER = 27             # ɾ��Ⱥ��Ա
    WECHAT_CHATROOM_ADD_MEMBER = 28             # ���Ⱥ��Ա
    WECHAT_CHATROOM_SET_ANNOUNCEMENT = 29       # ����Ⱥ����
    WECHAT_CHATROOM_SET_CHATROOM_NAME = 30      # ����Ⱥ������
    WECHAT_CHATROOM_SET_SELF_NICKNAME = 31      # ����Ⱥ�ڸ����ǳ�

    # database
    WECHAT_DATABASE_GET_HANDLES = 32            # ��ȡ���ݿ���
    WECHAT_DATABASE_BACKUP = 33                 # �������ݿ�
    WECHAT_DATABASE_QUERY = 34                  # ���ݿ��ѯ

    # version
    WECHAT_SET_VERSION = 35                     # �޸�΢�Ű汾��

    # log
    WECHAT_LOG_START_HOOK = 36                  # ������־��ϢHOOK
    WECHAT_LOG_STOP_HOOK = 37                   # �ر���־��ϢHOOK

    # browser
    WECHAT_BROWSER_OPEN_WITH_URL = 38           # ��΢�����������
    WECHAT_GET_PUBLIC_MSG = 39                  # ��ȡ���ں���ʷ��Ϣ

    WECHAT_MSG_FORWARD_MESSAGE = 40             # ת����Ϣ
    WECHAT_GET_QRCODE_IMAGE = 41                # ��ȡ��ά��
    WECHAT_GET_A8KEY = 42                       # ��ȡA8Key
    WECHAT_MSG_SEND_XML = 43                    # ����xml��Ϣ
    WECHAT_LOGOUT = 44                          # �˳���¼
    WECHAT_GET_TRANSFER = 45                    # �տ�
    WECHAT_MSG_SEND_EMOTION = 46                # ���ͱ���
    WECHAT_GET_CDN = 47                         # �����ļ�����Ƶ��ͼƬ
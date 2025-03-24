#coding=utf
from WECHAT_UTIL.util.ChatroomFunctions import ChatroomFunctions
from WECHAT_UTIL.util.ContactFunctions import ContactFunctions
import json
import copy
import re
from typing import TypedDict, Optional


class WechatMessage(TypedDict):
	# metadata:
	extrainfo:Optional[str]
	id:Optional[str]
	type:Optional[str]
	content:Optional[str]

	# sender
	sender:Optional[str] # 当在群聊里时 sender内容为群聊号 当为私聊时 sender为个人微信id
	self_wechat_id:Optional[str]
	sender_wechat_id:Optional[str]

	# file
	file_path:Optional[str]
	thumb_path:Optional[str]
	sign:Optional[str]

	# time
	time:Optional[int]
	time_stamp:Optional[int]

	# flags
	if_is_send_by_phone:Optional[bool]
	if_is_send_by_myself:Optional[bool]
	if_is_at_me:Optional[bool]
	if_is_in_chatroom:Optional[bool]

	# pid
	process_id:Optional[int]


def messageRestruct(msg: dict) -> WechatMessage:
	restructed_message:WechatMessage = {
		"extrainfo": msg.get('extrainfo',None),
		"id": msg.get('msgid',None),
		"type": msg.get('type',None),
		"content": msg.get('message',None),

		"sender": msg.get('sender',None),
		"self_wechat_id": msg.get('self',None),
		"sender_wechat_id": msg.get('wxid',None),

		"file_path": msg.get('filepath',None),
		"sign": msg.get('sign',None),
		"thumb_path": msg.get('thumb_path',None),

		"time": msg.get('time',None),
		"time_stamp": msg.get('timestamp',None),

		"if_is_send_by_phone": msg.get('isSendByPhone',None),
		"if_is_send_by_myself": msg.get('isSendMsg',None),
		"if_is_at_me": ChatroomFunctions.is_at_me(
			extrainfo = msg.get('extrainfo'),
			my_wxid = msg.get('self')
		),
		"if_is_in_chatroom": (True if "chatroom" in msg.get('sender') else False),

		"wechat_process_id": msg.get('pid',None)
	}
	return restructed_message


def messageProcess(msg:dict) -> bool:
	message=messageRestruct(msg)

	name_chatroom = ""
	name_sender= ""
	name_sender_in_chatroom = ""
	if message['if_is_in_chatroom']:
		name_chatroom = "群聊 " + ChatroomFunctions.get_chatroom_name(message['sender'])
		name_sender_in_chatroom = ChatroomFunctions.get_chatroom_member_nickname(message['sender'],message['sender_wechat_id'])
	else:
		name_sender = "私聊 " + ContactFunctions.get_contact_name(message['sender'])

	if message['if_is_send_by_myself']:
		if message['if_is_in_chatroom']:
			name_sender_in_chatroom = "me"
		else:
			name_sender += " me"

	msg_checks = {
		"emoji": "一个表情包",
		"img": "一个图片",
		"voicemsg": "一条语音信息",
		"videomsg": "一个视频文件",
		"refermsg": "一条回复信息（有待改进）",
		"<pat>": "发送了一个拍一拍",
		"appmsg": "一个链接/小程序"
	}

	sys_checks = {
		"dynacfg": "系统配置消息",
		"revokemsg": "撤回了一条消息",
		"pat": "拍了一下",
		"ChatSync": "正在同步消息",
		"<unreadchatlist>": "正在读取聊天信息"
	}

	if "<msg>" in message['content']: # 利用字典来进行消息的处理
		content = next((v for k, v in msg_checks.items() if k in message['content']), "一条特殊消息")
	elif "sysmsg" in message['content']:
		content = next((v for k, v in sys_checks.items() if k in message['content']), "其他系统消息")
	else:
		content = message['content']

	message_processed = (
		str(message['time']) + " "+
		(name_chatroom + " " + name_sender_in_chatroom + " " if message['if_is_in_chatroom'] else name_sender+" ") +
		("at了你" if message['if_is_at_me'] else "") +
		"发送了 "
	)
	message_processed += content
	print(message_processed)

	return True


if __name__ == "__main__":
	testmsg=[
		{'extrainfo': '<msgsource>\n\t<bizflag>0</bizflag>\n\t<pua>1</pua>\n\t<sec_msg_node>\n\t\t<uuid>aca2a9c892e326b7fc2ca96abd528378_</uuid>\n\t\t<risk-file-flag />\n\t\t<risk-file-md5-list />\n\t</sec_msg_node>\n\t<silence>1</silence>\n\t<membercount>75</membercount>\n\t<signature>V1_Plnpy2u0|v1_2NjBxfHQ</signature>\n\t<tmp_node>\n\t\t<publisher-id></publisher-id>\n\t</tmp_node>\n</msgsource>\n', 'filepath': 'wxid_n55yg50aengs12\\FileStorage\\Cache\\2024-06\\b47b484f2e4b555864707a3fc71a2e77', 'isSendMsg': 0, 'message': '<?xml version="1.0"?>\n<msg>\n\t<appmsg appid="" sdkver="0">\n\t\t<title>最一拖四的luv吗</title>\n\t\t<type>57</type>\n\t\t<appattach>\n\t\t\t<cdnthumbaeskey />\n\t\t\t<aeskey></aeskey>\n\t\t</appattach>\n\t\t<refermsg>\n\t\t\t<type>1</type>\n\t\t\t<svrid>1604224351016489853</svrid>\n\t\t\t<fromusr>44043383416@chatroom</fromusr>\n\t\t\t<chatusr>lisongj398156529</chatusr>\n\t\t\t<displayname>卡面来打李</displayname>\n\t\t\t<content>luv</content>\n\t\t\t<msgsource>&lt;msgsource&gt;&lt;sequence_id&gt;841110256&lt;/sequence_id&gt;\n\t&lt;pua&gt;1&lt;/pua&gt;\n\t&lt;silence&gt;1&lt;/silence&gt;\n\t&lt;membercount&gt;75&lt;/membercount&gt;\n\t&lt;signature&gt;V1_OnOSggZa|v1_OnOSggZa&lt;/signature&gt;\n\t&lt;tmp_node&gt;\n\t\t&lt;publisher-id&gt;&lt;/publisher-id&gt;\n\t&lt;/tmp_node&gt;\n&lt;/msgsource&gt;\n</msgsource>\n\t\t\t<createtime>1717567707</createtime>\n\t\t</refermsg>\n\t</appmsg>\n\t<fromusername>wxid_wt8bvv5gcerl22</fromusername>\n\t<scene>0</scene>\n\t<appinfo>\n\t\t<version>1</version>\n\t\t<appname />\n\t</appinfo>\n\t<commenturl />\n</msg>\n', 'msgid': 3751372273182503154, 'pid': 5896, 'self': 'wxid_n55yg50aengs12', 'sender': '44043383416@chatroom', 'sign': '2410be29486c9b225f060037d7adccd2', 'thumb_path': '', 'time': '2024-06-05 14:39:05', 'timestamp': 1717569545, 'type': 49, 'wxid': 'wxid_wt8bvv5gcerl22'},
		{'extrainfo': '<msgsource>\n\t<signature>v1_k+wjY1js</signature>\n\t<tmp_node>\n\t\t<publisher-id></publisher-id>\n\t</tmp_node>\n</msgsource>\n', 'filepath': '', 'isSendByPhone': 1, 'isSendMsg': 1, 'message': '<msg>\n<op id=\'1\'>\n<username>44043383416@chatroom</username>\n<name>lastMessage</name>\n<arg>{"messageSvrId":"3751372273182503154","MsgCreateTime":"1717569545"}</arg>\n</op>\n</msg>', 'msgid': 4447548990507664829, 'pid': 5896, 'self': 'wxid_n55yg50aengs12', 'sender': '44043383416@chatroom', 'sign': '', 'thumb_path': '', 'time': '2024-06-05 14:39:07', 'timestamp': 1717569547, 'type': 51, 'wxid': '44043383416@chatroom'},
		{'extrainfo': '<msgsource>\n\t<bizflag>0</bizflag>\n\t<pua>1</pua>\n\t<silence>1</silence>\n\t<membercount>75</membercount>\n\t<signature>V1_62nTDrsY|v1_62nTDrsY</signature>\n\t<tmp_node>\n\t\t<publisher-id></publisher-id>\n\t</tmp_node>\n</msgsource>\n', 'filepath': '', 'isSendMsg': 0, 'message': '那我', 'msgid': 8562150924436329210, 'pid': 5896, 'self': 'wxid_n55yg50aengs12', 'sender': '44043383416@chatroom', 'sign': '9a58eeffab0637937fb8ec9f6edb5075', 'thumb_path': '', 'time': '2024-06-05 14:39:09', 'timestamp': 1717569549, 'type': 1, 'wxid': 'wxid_wt8bvv5gcerl22'},
		{'extrainfo': '<msgsource>\n\t<signature>v1_KGgBmnT7</signature>\n\t<tmp_node>\n\t\t<publisher-id></publisher-id>\n\t</tmp_node>\n</msgsource>\n', 'filepath': '', 'isSendByPhone': 1, 'isSendMsg': 1, 'message': '<msg>\n<op id=\'1\'>\n<username>44043383416@chatroom</username>\n<name>lastMessage</name>\n<arg>{"messageSvrId":"8562150924436329210","MsgCreateTime":"1717569549"}</arg>\n</op>\n</msg>', 'msgid': 6884863618392569340, 'pid': 5896, 'self': 'wxid_n55yg50aengs12', 'sender': '44043383416@chatroom', 'sign': '', 'thumb_path': '', 'time': '2024-06-05 14:39:11', 'timestamp': 1717569551, 'type': 51, 'wxid': '44043383416@chatroom'},
		{'extrainfo': '<msgsource>\n\t<bizflag>0</bizflag>\n\t<pua>1</pua>\n\t<silence>1</silence>\n\t<membercount>75</membercount>\n\t<signature>V1_TTd//v31|v1_TTd//v31</signature>\n\t<tmp_node>\n\t\t<publisher-id></publisher-id>\n\t</tmp_node>\n</msgsource>\n', 'filepath': '', 'isSendMsg': 0, 'message': '我爱赤石', 'msgid': 5865431892150659828, 'pid': 5896, 'self': 'wxid_n55yg50aengs12', 'sender': '44043383416@chatroom', 'sign': '253670975b5d40d1c6fec547d455bf6e', 'thumb_path': '', 'time': '2024-06-05 14:39:15', 'timestamp': 1717569555, 'type': 1, 'wxid': 'wxid_wt8bvv5gcerl22'},
		{'extrainfo': '<msgsource>\n\t<signature>v1_weZLLBq3</signature>\n\t<tmp_node>\n\t\t<publisher-id></publisher-id>\n\t</tmp_node>\n</msgsource>\n', 'filepath': '', 'isSendByPhone': 1, 'isSendMsg': 1, 'message': '<msg>\n<op id=\'1\'>\n<username>44043383416@chatroom</username>\n<name>lastMessage</name>\n<arg>{"messageSvrId":"5865431892150659828","MsgCreateTime":"1717569555"}</arg>\n</op>\n</msg>', 'msgid': 7953791345212186418, 'pid': 5896, 'self': 'wxid_n55yg50aengs12', 'sender': '44043383416@chatroom', 'sign': '', 'thumb_path': '', 'time': '2024-06-05 14:39:16', 'timestamp': 1717569556, 'type': 51, 'wxid': '44043383416@chatroom'},
		{'extrainfo': '<msgsource>\n\t<bizflag>0</bizflag>\n\t<alnode>\n\t\t<fr>2</fr>\n\t</alnode>\n\t<sec_msg_node>\n\t\t<uuid>7a5b81c49defcf8a35583e9c085804a8_</uuid>\n\t\t<risk-file-flag />\n\t\t<risk-file-md5-list />\n\t</sec_msg_node>\n\t<silence>1</silence>\n\t<membercount>75</membercount>\n\t<signature>V1_pEjkPxw0|v1_CZJz8M/1</signature>\n\t<tmp_node>\n\t\t<publisher-id></publisher-id>\n\t</tmp_node>\n</msgsource>\n', 'filepath': 'wxid_n55yg50aengs12\\FileStorage\\Cache\\2024-06\\700cad84739e9ae4dd0d4b9a8005225d', 'isSendMsg': 0, 'message': '<msg>\n\t<appmsg appid="wx5aa333606550dfd5" sdkver="0">\n\t\t<title>Don\'t Break My Heart</title>\n\t\t<des>黑豹乐队</des>\n\t\t<type>3</type>\n\t\t<url>https://i.y.qq.com/v8/playsong.html?hosteuin=oKvANe6PNKcqNv**&amp;songid=101832218&amp;songmid=&amp;type=0&amp;platform=(10rpl)&amp;appsongtype=(11rpl)&amp;_wv=1&amp;source=qq&amp;appshare=iphone&amp;media_mid=004NxnWA3qhy53&amp;ADTAG=wxfshare</url>\n\t\t<dataurl>http://c6.y.qq.com/rsc/fcgi-bin/fcg_pyq_play.fcg?songid=0&amp;songmid=002YJoz04THQD2&amp;songtype=1&amp;fromtag=46&amp;uin=1428149899&amp;code=5ffb2</dataurl>\n\t\t<songalbumurl>http://wxapp.tc.qq.com/202/20304/stodownload?filekey=30350201010421301f020200ca0402535a04106eb6fcf688a1640e7d8eaeaece11a534020301ba9f040d00000004627466730000000132&amp;hy=SZ&amp;storeid=26660082d000ee42778ee74b8000000ca00004f50535a1cca70b156bef7fd1&amp;bizid=1023</songalbumurl>\n\t\t<songlyric>[ti:Don\'t break my heart]\n[ar:黑豹]\n[al:312972]\n[by:]\n[offset:0]\n[00:00.00]Don\'t Break My Heart - 黑豹乐队\n[00:18.63]词：窦唯\n[00:37.26]曲：窦唯\n[00:55.89]也许是我不懂的事太多\n[01:00.67]也许是我的错\n[01:03.74]\n[01:05.39]也许一切已是慢慢的错过\n[01:10.18]也许不必再说\n[01:13.58]\n[01:15.01]从未想过你我会这样结束\n[01:19.79]心中没有把握\n[01:23.79]\n[01:24.53]只是记得你我彼此的承诺\n[01:29.41]一次次的冲动\n[01:33.44]Don\'t break my heart\n[01:35.97]再次温柔\n[01:38.39]不愿看到你那保持的沉默\n[01:43.19]独自等待\n[01:45.51]默默承受\n[01:48.00]喜悦总是出现在我梦中\n[01:56.58]\n[02:02.97]也许是我不懂的事太多\n[02:07.67]也许是我的错\n[02:12.53]也许一切已是慢慢的错过\n[02:17.29]也许不必再说\n[02:21.12]\n[02:22.13]从未想过你我会这样结束\n[02:26.94]心竟如此难过\n[02:30.91]\n[02:31.79]只是记得你我彼此的承诺\n[02:36.47]一次次的冲动\n[02:40.57]Don\'t break my heart\n[02:43.16]再次温柔\n[02:45.47]不愿看到你那保持的沉默\n[02:50.35]独自等待\n[02:52.60]默默承受\n[02:55.07]喜悦总是出现在我梦中\n[03:02.03]\n[03:02.85]你所拥有的是你的身体\n[03:07.67]诱人的美丽\n[03:12.48]我所拥有的是我的记忆\n[03:17.32]美妙的感觉（oh baby）\n[03:23.85]Don\'t break my heart\n[03:26.21]再次温柔\n[03:28.65]不愿看到你那保持的沉默\n[03:33.45]独自等待\n[03:35.75]默默承受\n[03:38.10]喜悦总是出现在我梦中\n[03:43.06]Don\'t break my heart\n[03:45.19]再次温柔\n[03:47.66]不愿看到你那保持的沉默\n[03:52.46]独自等待\n[03:54.87]默默承受\n[03:57.15]喜悦总是出现在我梦中\n[04:02.09]Don\'t break my heart\n[04:04.50]再次温柔\n[04:06.94]不愿看到你那保持的沉默\n[04:11.62]独自等待\n[04:13.94]默默承受\n[04:16.45]喜悦总是出现在我梦中\n[04:21.13]Don\'t break my heart\n[04:23.57]再次温柔\n[04:26.02]不愿看到你那保持的沉默\n[04:30.94]独自等待\n[04:33.21]默默承受\n[04:35.60]喜悦总是出现在我梦中</songlyric>\n\t\t<appattach>\n\t\t\t<cdnthumburl>3057020100044b3049020100020478ee74b802030f5efb020424c2822b02046660082e042436323532323063372d373931332d343563322d626537632d3636303134613334346465350204012c08030201000405004c4e6100</cdnthumburl>\n\t\t\t<cdnthumbmd5>e8315dd1b26b4a9004f5323e539090cb</cdnthumbmd5>\n\t\t\t<cdnthumblength>7145</cdnthumblength>\n\t\t\t<cdnthumbwidth>150</cdnthumbwidth>\n\t\t\t<cdnthumbheight>150</cdnthumbheight>\n\t\t\t<cdnthumbaeskey>2c5bcf1a1d30c7c5a4582c5beee5e278</cdnthumbaeskey>\n\t\t\t<aeskey>2c5bcf1a1d30c7c5a4582c5beee5e278</aeskey>\n\t\t\t<encryver>0</encryver>\n\t\t\t<filekey>44043383416@chatroom_637804_1717569582</filekey>\n\t\t</appattach>\n\t\t<md5>e8315dd1b26b4a9004f5323e539090cb</md5>\n\t\t<statextstr>GhQKEnd4NWFhMzMzNjA2NTUwZGZkNQ==</statextstr>\n\t\t<musicShareItem>\n\t\t\t<mid>getlinkclisdkmid_002YJoz04THQD2</mid>\n\t\t\t<mvSingerName>黑豹乐队</mvSingerName>\n\t\t\t<mvAlbumName>黑豹 同名专辑</mvAlbumName>\n\t\t\t<musicDuration>316000</musicDuration>\n\t\t</musicShareItem>\n\t</appmsg>\n\t<fromusername>wxid_are7xpv3szkj22</fromusername>\n\t<scene>0</scene>\n\t<appinfo>\n\t\t<version>53</version>\n\t\t<appname>QQ音乐</appname>\n\t</appinfo>\n\t<commenturl />\n</msg>\n', 'msgid': 6028665829346491428, 'pid': 5896, 'self': 'wxid_n55yg50aengs12', 'sender': '44043383416@chatroom', 'sign': '2869906351c8001586febcf475ab1a99', 'thumb_path': 'wxid_n55yg50aengs12\\FileStorage\\Cache\\2024-06\\6a99d41ced4d9f070c0fb97e88695e7a_t.jpg', 'time': '2024-06-05 14:39:42', 'timestamp': 1717569582, 'type': 49, 'wxid': 'wxid_are7xpv3szkj22'},
		{'extrainfo': '<msgsource>\n\t<signature>v1_0vPuWDbZ</signature>\n\t<tmp_node>\n\t\t<publisher-id></publisher-id>\n\t</tmp_node>\n</msgsource>\n', 'filepath': '', 'isSendByPhone': 1, 'isSendMsg': 1, 'message': '<msg>\n<op id=\'1\'>\n<username>44043383416@chatroom</username>\n<name>lastMessage</name>\n<arg>{"messageSvrId":"6028665829346491428","MsgCreateTime":"1717569582"}</arg>\n</op>\n</msg>', 'msgid': 6922455339251347889, 'pid': 5896, 'self': 'wxid_n55yg50aengs12', 'sender': '44043383416@chatroom', 'sign': '', 'thumb_path': '', 'time': '2024-06-05 14:39:44', 'timestamp': 1717569584, 'type': 51, 'wxid': '44043383416@chatroom'},
		{'extrainfo': '<msgsource>\n\t<signature>v1_IKDiTcE1</signature>\n\t<tmp_node>\n\t\t<publisher-id></publisher-id>\n\t</tmp_node>\n</msgsource>\n', 'filepath': '', 'isSendByPhone': 1, 'isSendMsg': 1, 'message': '<msg>\n<op id=\'2\'>\n<username>wxid_wt8bvv5gcerl22</username>\n<name>lastMessage</name>\n<arg>{"messageSvrId":"8642878882907572998","MsgCreateTime":"1717556085"}</arg>\n</op>\n</msg>', 'msgid': 3717254411291744519, 'pid': 5896, 'self': 'wxid_n55yg50aengs12', 'sender': 'wxid_wt8bvv5gcerl22', 'sign': '', 'thumb_path': '', 'time': '2024-06-05 14:40:25', 'timestamp': 1717569625, 'type': 51, 'wxid': 'wxid_wt8bvv5gcerl22'},
		{'extrainfo': '<msgsource>\n\t<signature>v1_p9yLk+2l</signature>\n\t<tmp_node>\n\t\t<publisher-id></publisher-id>\n\t</tmp_node>\n</msgsource>\n', 'filepath': '', 'isSendByPhone': 1, 'isSendMsg': 1, 'message': "<msg>\n<op id='9'>\n<name>MomentsTimelineStatus</name>\n<arg>14407951498049303292,1717561662</arg>\n</op>\n</msg>", 'msgid': 1973620872387544249, 'pid': 5896, 'self': 'wxid_n55yg50aengs12', 'sender': 'wxid_n55yg50aengs12', 'sign': '', 'thumb_path': '', 'time': '2024-06-05 14:40:28', 'timestamp': 1717569628, 'type': 51, 'wxid': 'wxid_n55yg50aengs12'},
		{'extrainfo': '<msgsource>\n\t<signature>v1_uPEHClQa</signature>\n\t<tmp_node>\n\t\t<publisher-id></publisher-id>\n\t</tmp_node>\n</msgsource>\n', 'filepath': '', 'isSendByPhone': 1, 'isSendMsg': 1, 'message': '<msg>\n<op id=\'2\'>\n<username>wxid_wt8bvv5gcerl22</username>\n<name>lastMessage</name>\n<arg>{"messageSvrId":"8642878882907572998","MsgCreateTime":"1717556085"}</arg>\n</op>\n</msg>', 'msgid': 6545077596227799731, 'pid': 5896, 'self': 'wxid_n55yg50aengs12', 'sender': 'wxid_wt8bvv5gcerl22', 'sign': '', 'thumb_path': '', 'time': '2024-06-05 14:40:31', 'timestamp': 1717569631, 'type': 51, 'wxid': 'wxid_wt8bvv5gcerl22'},
		{'extrainfo': '<msgsource>\n\t<signature>v1_+rdaYyyB</signature>\n\t<tmp_node>\n\t\t<publisher-id></publisher-id>\n\t</tmp_node>\n</msgsource>\n', 'filepath': '', 'isSendByPhone': 1, 'isSendMsg': 1, 'message': '<msg>\n<op id=\'1\'>\n<username>wxid_wt8bvv5gcerl22</username>\n<name>lastMessage</name>\n<arg>{"messageSvrId":"8642878882907572998","MsgCreateTime":"1717556085"}</arg>\n</op>\n</msg>', 'msgid': 3521638323423172153, 'pid': 5896, 'self': 'wxid_n55yg50aengs12', 'sender': 'wxid_wt8bvv5gcerl22', 'sign': '', 'thumb_path': '', 'time': '2024-06-05 14:40:31', 'timestamp': 1717569631, 'type': 51, 'wxid': 'wxid_wt8bvv5gcerl22'},
		{'extrainfo': '<msgsource>\n\t<bizflag>0</bizflag>\n\t<alnode>\n\t\t<fr>2</fr>\n\t</alnode>\n\t<sec_msg_node>\n\t\t<uuid>f49b4c85450afa797cc79d64f28bf6e6_</uuid>\n\t\t<risk-file-flag />\n\t\t<risk-file-md5-list />\n\t</sec_msg_node>\n\t<silence>1</silence>\n\t<membercount>75</membercount>\n\t<signature>V1_rzKsbCaI|v1_ROToQWes</signature>\n\t<tmp_node>\n\t\t<publisher-id></publisher-id>\n\t</tmp_node>\n</msgsource>\n', 'filepath': 'wxid_n55yg50aengs12\\FileStorage\\Cache\\2024-06\\33436132f8a29b95f3b00a32e8b015f5.jpg', 'isSendMsg': 0, 'message': '<?xml version="1.0"?>\n<msg>\n\t<appmsg appid="wx8dd6ecd81906fd84" sdkver="0">\n\t\t<title>陽のあたる場所 (阳光普照的地方)</title>\n\t\t<des>MISIA - 陽のあたる場所</des>\n\t\t<type>5</type>\n\t\t<url>https://y.music.163.com/m/song?fx-wechatnew=t1&amp;fx-wxqd=t1&amp;fx-wordtest=&amp;id=477615366&amp;shareToken=16881280651717569641_dfce27730008ac57715a90558bb81660&amp;fx-listentest=t3&amp;uct2=LXWjMbftApWqk3np2E7bOQ==&amp;app_version=9.0.90&amp;dlt=0846</url>\n\t\t<appattach>\n\t\t\t<cdnthumburl>3057020100044b304902010002043f6fc2a202032f5aa90204e0ab697102046660086d042465303039326563352d613738322d343230642d393935392d6461633833313164646130610204052408030201000405004c505500</cdnthumburl>\n\t\t\t<cdnthumbmd5>14a998b13bc46aeb5cac9598c41699b3</cdnthumbmd5>\n\t\t\t<cdnthumblength>5849</cdnthumblength>\n\t\t\t<cdnthumbwidth>135</cdnthumbwidth>\n\t\t\t<cdnthumbheight>135</cdnthumbheight>\n\t\t\t<cdnthumbaeskey>b3a0267def51431ad4c8ea0b8fb8f7be</cdnthumbaeskey>\n\t\t\t<aeskey>b3a0267def51431ad4c8ea0b8fb8f7be</aeskey>\n\t\t\t<encryver>0</encryver>\n\t\t\t<filekey>44043383416@chatroom_14125_1717569645</filekey>\n\t\t</appattach>\n\t\t<md5>14a998b13bc46aeb5cac9598c41699b3</md5>\n\t\t<statextstr>GhQKEnd4OGRkNmVjZDgxOTA2ZmQ4NA==</statextstr>\n\t</appmsg>\n\t<fromusername>wxid_6buqxdi535jk11</fromusername>\n\t<scene>0</scene>\n\t<appinfo>\n\t\t<version>49</version>\n\t\t<appname>网易云音乐</appname>\n\t</appinfo>\n\t<commenturl />\n</msg>\n', 'msgid': 5040535814035608924, 'pid': 5896, 'self': 'wxid_n55yg50aengs12', 'sender': '44043383416@chatroom', 'sign': '658075c3f781d7042659aef3e037672a', 'thumb_path': 'wxid_n55yg50aengs12\\FileStorage\\Cache\\2024-06\\e519c5ec20dca4b040a59e2a90824a7d_t.jpg', 'time': '2024-06-05 14:40:45', 'timestamp': 1717569645, 'type': 49, 'wxid': 'wxid_6buqxdi535jk11'},
		{'extrainfo': '<msgsource>\n\t<bizflag>0</bizflag>\n\t<pua>1</pua>\n\t<silence>1</silence>\n\t<membercount>75</membercount>\n\t<signature>V1_aSgwOtjS|v1_aSgwOtjS</signature>\n\t<tmp_node>\n\t\t<publisher-id></publisher-id>\n\t</tmp_node>\n</msgsource>\n', 'filepath': '', 'isSendMsg': 0, 'message': '霓虹的r&b', 'msgid': 8958216652179275309, 'pid': 5896, 'self': 'wxid_n55yg50aengs12', 'sender': '44043383416@chatroom', 'sign': 'd321b3a88313b9960ffcb13e78e99049', 'thumb_path': '', 'time': '2024-06-05 14:41:25', 'timestamp': 1717569685, 'type': 1, 'wxid': 'wxid_6buqxdi535jk11'},
		{'extrainfo': '<msgsource>\n\t<silence>1</silence>\n\t<membercount>75</membercount>\n\t<signature>V1_rCI6pvjC|v1_mZagMD3s</signature>\n\t<tmp_node>\n\t\t<publisher-id></publisher-id>\n\t</tmp_node>\n</msgsource>\n', 'filepath': '7E16EB066D0402E0DF28F7EA249E6BA0', 'isSendMsg': 0, 'message': '<msg><emoji fromusername="wxid_r4n1dw9h9j0612" tousername="44043383416@chatroom" type="2" idbuffer="media:0_0" md5="7e16eb066d0402e0df28f7ea249e6ba0" len="4406999" productid="" androidmd5="7e16eb066d0402e0df28f7ea249e6ba0" androidlen="4406999" s60v3md5="7e16eb066d0402e0df28f7ea249e6ba0" s60v3len="4406999" s60v5md5="7e16eb066d0402e0df28f7ea249e6ba0" s60v5len="4406999" cdnurl="http://vweixinf.tc.qq.com/110/20402/stodownload?m=7e16eb066d0402e0df28f7ea249e6ba0&amp;filekey=30440201010430302e02016e0402535a042037653136656230363664303430326530646632386637656132343965366261300203433ed7040d00000004627466730000000132&amp;hy=SZ&amp;storeid=26596dd2a0002460e934b4b4e0000006e01004fb2535a1c766bc1e65ab7ece&amp;ef=1&amp;bizid=1022" designerid="" thumburl="" encrypturl="http://vweixinf.tc.qq.com/110/20402/stodownload?m=c02d3ce80a7e180f00f61809e3a0e974&amp;filekey=30440201010430302e02016e0402535a042063303264336365383061376531383066303066363138303965336130653937340203433ee0040d00000004627466730000000132&amp;hy=SZ&amp;storeid=26596dd2a00062d5d934b4b4e0000006e02004fb2535a1c766bc1e65ab7ed8&amp;ef=2&amp;bizid=1022" aeskey="0f2ec89a1f6e46df856c17b79a3394f4" externurl="http://vweixinf.tc.qq.com/110/20403/stodownload?m=a417a0fd5c8cfcd4a4c879fcf7b93d45&amp;filekey=30440201010430302e02016e0402535a04206134313761306664356338636663643461346338373966636637623933643435020302da60040d00000004627466730000000132&amp;hy=SZ&amp;storeid=26596dd2a000a6c14934b4b4e0000006e03004fb3535a1c766bc1e65ab7edf&amp;ef=3&amp;bizid=1022" externmd5="5b800f04152afd61e61302c899773afb" width="287" height="300" tpurl="" tpauthkey="" attachedtext="" attachedtextcolor="" lensid="" emojiattr="" linkid="" desc=""></emoji><gameext type="0" content="0"></gameext></msg>', 'msgid': 6266518922902741145, 'pid': 5896, 'self': 'wxid_n55yg50aengs12', 'sender': '44043383416@chatroom', 'sign': 'fe8284d640459c3ece60929cc27bd34f', 'thumb_path': '', 'time': '2024-06-05 14:41:28', 'timestamp': 1717569688, 'type': 47, 'wxid': 'wxid_r4n1dw9h9j0612'},
		{'extrainfo': '<msgsource>\n\t<silence>1</silence>\n\t<membercount>75</membercount>\n\t<signature>V1_KPebCuvZ|v1_eKdrWP7S</signature>\n\t<tmp_node>\n\t\t<publisher-id></publisher-id>\n\t</tmp_node>\n</msgsource>\n', 'filepath': '1709B6F56C24D4FA14CF46569FFCB884', 'isSendMsg': 0, 'message': '<msg><emoji fromusername="wxid_6buqxdi535jk11" tousername="44043383416@chatroom" type="2" idbuffer="media:0_0" md5="1709b6f56c24d4fa14cf46569ffcb884" len="11260" productid="" androidmd5="1709b6f56c24d4fa14cf46569ffcb884" androidlen="11260" s60v3md5="1709b6f56c24d4fa14cf46569ffcb884" s60v3len="11260" s60v5md5="1709b6f56c24d4fa14cf46569ffcb884" s60v5len="11260" cdnurl="http://vweixinf.tc.qq.com/110/20401/stodownload?m=1709b6f56c24d4fa14cf46569ffcb884&amp;filekey=3043020101042f302d02016e040253480420313730396236663536633234643466613134636634363536396666636238383402022bfc040d00000004627466730000000132&amp;hy=SH&amp;storeid=265e575ca000716c46b49eb660000006e01004fb153481f660b01e6bd34650&amp;ef=1&amp;bizid=1022" designerid="" thumburl="" encrypturl="http://vweixinf.tc.qq.com/110/20402/stodownload?m=0e4d398e0a034adfc4dc3c562b9c0deb&amp;filekey=3043020101042f302d02016e040253480420306534643339386530613033346164666334646333633536326239633064656202022c00040d00000004627466730000000132&amp;hy=SH&amp;storeid=265e575ca0007c9646b49eb660000006e02004fb253481f660b01e6bd3465b&amp;ef=2&amp;bizid=1022" aeskey="3177ba99f4c34b098ac8791202b24743" externurl="http://vweixinf.tc.qq.com/110/20403/stodownload?m=501d00ae925abb0975651c1f71dfd2e0&amp;filekey=3043020101042f302d02016e040253480420353031643030616539323561626230393735363531633166373164666432653002020ed0040d00000004627466730000000132&amp;hy=SH&amp;storeid=265e575ca00084f076b49eb660000006e03004fb353481f660b01e6bd34666&amp;ef=3&amp;bizid=1022" externmd5="f8dd25c71f9ecdbbc266f7a1363977d1" width="239" height="227" tpurl="" tpauthkey="" attachedtext="" attachedtextcolor="" lensid="" emojiattr="" linkid="" desc=""></emoji><gameext type="0" content="0"></gameext></msg>', 'msgid': 2909261694820267452, 'pid': 5896, 'self': 'wxid_n55yg50aengs12', 'sender': '44043383416@chatroom', 'sign': '5fd39d2480c675b52f3a74fb3219aa09', 'thumb_path': '', 'time': '2024-06-05 14:41:27', 'timestamp': 1717569687, 'type': 47, 'wxid': 'wxid_6buqxdi535jk11'},
		{'extrainfo': '<msgsource>\n\t<bizflag>0</bizflag>\n\t<pua>1</pua>\n\t<silence>1</silence>\n\t<membercount>75</membercount>\n\t<signature>V1_H9TV8NXu|v1_H9TV8NXu</signature>\n\t<tmp_node>\n\t\t<publisher-id></publisher-id>\n\t</tmp_node>\n</msgsource>\n', 'filepath': '', 'isSendMsg': 0, 'message': '我听team友達', 'msgid': 1051475368352376841, 'pid': 5896, 'self': 'wxid_n55yg50aengs12', 'sender': '44043383416@chatroom', 'sign': '0127484c811654879bb2302c1d2d8b6e', 'thumb_path': '', 'time': '2024-06-05 14:41:35', 'timestamp': 1717569695, 'type': 1, 'wxid': 'wxid_r4n1dw9h9j0612'},
		{'extrainfo': '<msgsource>\n\t<bizflag>0</bizflag>\n\t<pua>1</pua>\n\t<silence>1</silence>\n\t<membercount>75</membercount>\n\t<signature>V1_ZYBXJHyl|v1_ZYBXJHyl</signature>\n\t<tmp_node>\n\t\t<publisher-id></publisher-id>\n\t</tmp_node>\n</msgsource>\n', 'filepath': '', 'isSendMsg': 0, 'message': '俺たち何で', 'msgid': 6470313386897468621, 'pid': 5896, 'self': 'wxid_n55yg50aengs12', 'sender': '44043383416@chatroom', 'sign': '0b18f5dc2855ba56c550c016a031a178', 'thumb_path': '', 'time': '2024-06-05 14:41:57', 'timestamp': 1717569717, 'type': 1, 'wxid': 'wxid_r4n1dw9h9j0612'},
		{'extrainfo': '<msgsource>\n\t<bizflag>0</bizflag>\n\t<pua>1</pua>\n\t<silence>1</silence>\n\t<membercount>75</membercount>\n\t<signature>V1_7BdJm0gT|v1_7BdJm0gT</signature>\n\t<tmp_node>\n\t\t<publisher-id></publisher-id>\n\t</tmp_node>\n</msgsource>\n', 'filepath': '', 'isSendMsg': 0, 'message': 'team友達', 'msgid': 3194512548679274785, 'pid': 5896, 'self': 'wxid_n55yg50aengs12', 'sender': '44043383416@chatroom', 'sign': 'b10b354875cdd82bf05e47175b1edbef', 'thumb_path': '', 'time': '2024-06-05 14:42:07', 'timestamp': 1717569727, 'type': 1, 'wxid': 'wxid_r4n1dw9h9j0612'},
		{'extrainfo': '', 'filepath': '', 'isSendByPhone': 0, 'isSendMsg': 1, 'message': '{\'extrainfo\': \'<msgsource>\\n\\t<bizflag>0</bizflag>\\n\\t<pua>1</pua>\\n\\t<sec_msg_node>\\n\\t\\t<uuid>aca2a9c892e326b7fc2ca96abd528378_</uuid>\\n\\t\\t<risk-file-flag />\\n\\t\\t<risk-file-md5-list />\\n\\t</sec_msg_node>\\n\\t<silence>1</silence>\\n\\t<membercount>75</membercount>\\n\\t<signature>V1_Plnpy2u0|v1_2NjBxfHQ</signature>\\n\\t<tmp_node>\\n\\t\\t<publisher-id></publisher-id>\\n\\t</tmp_node>\\n</msgsource>\\n\', \'filepath\': \'wxid_n55yg50aengs12\\\\FileStorage\\\\Cache\\\\2024-06\\\\b47b484f2e4b555864707a3fc71a2e77\', \'isSendMsg\': 0, \'message\': \'<?xml version="1.0"?>\\n<msg>\\n\\t<appmsg appid="" sdkver="0">\\n\\t\\t<title>最一拖四的luv吗</title>\\n\\t\\t<type>57</type>\\n\\t\\t<appattach>\\n\\t\\t\\t<cdnthumbaeskey />\\n\\t\\t\\t<aeskey></aeskey>\\n\\t\\t</appattach>\\n\\t\\t<refermsg>\\n\\t\\t\\t<type>1</type>\\n\\t\\t\\t<svrid>1604224351016489853</svrid>\\n\\t\\t\\t<fromusr>44043383416@chatroom</fromusr>\\n\\t\\t\\t<chatusr>lisongj398156529</chatusr>\\n\\t\\t\\t<displayname>卡面来打李</displayname>\\n\\t\\t\\t<content>luv</content>\\n\\t\\t\\t<msgsource>&lt;msgsource&gt;&lt;sequence_id&gt;841110256&lt;/sequence_id&gt;\\n\\t&lt;pua&gt;1&lt;/pua&gt;\\n\\t&lt;silence&gt;1&lt;/silence&gt;\\n\\t&lt;membercount&gt;75&lt;/membercount&gt;\\n\\t&lt;signature&gt;V1_OnOSggZa|v1_OnOSggZa&lt;/signature&gt;\\n\\t&lt;tmp_node&gt;\\n\\t\\t&lt;publisher-id&gt;&lt;/publisher-id&gt;\\n\\t&lt;/tmp_node&gt;\\n&lt;/msgsource&gt;\\n</msgsource>\\n\\t\\t\\t<createtime>1717567707</createtime>\\n\\t\\t</refermsg>\\n\\t</appmsg>\\n\\t<fromusername>wxid_wt8bvv5gcerl22</fromusername>\\n\\t<scene>0</scene>\\n\\t<appinfo>\\n\\t\\t<version>1</version>\\n\\t\\t<appname />\\n\\t</appinfo>\\n\\t<commenturl />\\n</msg>\\n\', \'msgid\': 3751372273182503154, \'pid\': 5896, \'self\': \'wxid_n55yg50aengs12\', \'sender\': \'44043383416@chatroom\', \'sign\': \'2410be29486c9b225f060037d7adccd2\', \'thumb_path\': \'\', \'time\': \'2024-06-05 14:39:05\', \'timestamp\': 1717569545, \'type\': 49, \'wxid\': \'wxid_wt8bvv5gcerl22\'}\n{\'extrainfo\': \'<msgsource>\\n\\t<signature>v1_k+wjY1js</signature>\\n\\t<tmp_node>\\n\\t\\t<publisher-id></publisher-id>\\n\\t</tmp_node>\\n</msgsource>\\n\', \'filepath\': \'\', \'isSendByPhone\': 1, \'isSendMsg\':', 'msgid': 2279218706214836802, 'pid': 5896, 'self': 'wxid_n55yg50aengs12', 'sender': '44043383416@chatroom', 'sign': 'ab88f7fcc35a592b89582cc9e87e3330', 'thumb_path': '', 'time': '2024-06-05 14:42:29', 'timestamp': 1717569749, 'type': 1, 'wxid': '44043383416@chatroom'},
		{'extrainfo': '<msgsource>\n\t<bizflag>0</bizflag>\n\t<pua>1</pua>\n\t<silence>1</silence>\n\t<membercount>75</membercount>\n\t<signature>V1_poNM7F3/|v1_poNM7F3/</signature>\n\t<tmp_node>\n\t\t<publisher-id></publisher-id>\n\t</tmp_node>\n</msgsource>\n', 'filepath': '', 'isSendMsg': 0, 'message': '收到', 'msgid': 8920812368073184622, 'pid': 5896, 'self': 'wxid_n55yg50aengs12', 'sender': '44043383416@chatroom', 'sign': '9f03164642a4778780e78bfaba04d2ae', 'thumb_path': '', 'time': '2024-06-05 14:42:33', 'timestamp': 1717569753, 'type': 1, 'wxid': 'wxid_6buqxdi535jk11'},
		{'extrainfo': '', 'isSendByPhone': 0, 'isSendMsg': 1, 'message': '<revokemsg><![CDATA[你撤回了一条消息 <a href="weixin://revoke_edit_click">重新编辑</a>]]></revokemsg>', 'msgid': 2279218706214836802, 'pid': 5896, 'self': 'wxid_n55yg50aengs12', 'sender': '44043383416@chatroom', 'sign': 'ab88f7fcc35a592b89582cc9e87e3330', 'thumb_path': '', 'time': '2024-06-05 14:42:36', 'timestamp': 1717569756, 'type': 10000, 'wxid': '44043383416@chatroom'},
		{'extrainfo': '<msgsource>\n\t<tmp_node>\n\t\t<publisher-id></publisher-id>\n\t</tmp_node>\n</msgsource>\n', 'filepath': '', 'isSendByPhone': 1, 'isSendMsg': 1, 'message': '<sysmsg type="revokemsg"><revokemsg><session>44043383416@chatroom</session><msgid>824451634</msgid><newmsgid>2279218706214836802</newmsgid><replacemsg><![CDATA[你撤回了一条消息]]></replacemsg></revokemsg></sysmsg>', 'msgid': 710169146, 'pid': 5896, 'self': 'wxid_n55yg50aengs12', 'sender': '44043383416@chatroom', 'sign': '', 'thumb_path': '', 'time': '2024-06-05 14:42:36', 'timestamp': 1717569756, 'type': 10002, 'wxid': '44043383416@chatroom'},
	]
	for msg in testmsg:
		messageProcess(msg)

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
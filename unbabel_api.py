import sys
from unbabel.api import UnbabelApi
import time



def setup():
	unbabel_username = 'hackathon-bettecnico'
	unbabel_api_key = '339c3c0f3bb97c6a097c33f42122b32b74d032b5'
	in_test_mode = 'true'

	uapi = UnbabelApi(unbabel_username, unbabel_api_key, 
	                  sandbox=in_test_mode)

	return uapi


def post_translation(uapi, subtitle_file, subtitle_source, subtitle_target):
	#callback_url = 'https://requestb.in/15y329z1'
	text_format = 'srt'
	subtitle_text = open(subtitle_file, 'r').read()

	t = uapi.post_mt_translations(text=subtitle_text, target_language=subtitle_target, source_language=subtitle_source,
	                       text_format=text_format)
	time.sleep(3)
	
	return uapi.get_mt_translation(t.uid).translation

def main():
	cmdargs = sys.argv
	subtitle_file = cmdargs[1]
	subtitle_source = cmdargs[2]
	subtitle_target = cmdargs[3]

	uapi = setup()
	translated_text = post_translation(uapi, subtitle_file, subtitle_source, subtitle_target)

	print(translated_text.encode('utf-8'))


main()
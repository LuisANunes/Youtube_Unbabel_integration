import sys
import os

caption_source_lang = 'en'
caption_target_lang = 'pt'
sub_srt_en = 'subtitles_en.srt'
sub_srt_pt = 'subtitles_pt.srt'


def main():
	#Youtube link is given as the first argument and parsed to get the video id
	yt_link = sys.argv[1]
	video_id = yt_link.split('=')[1]

	#Call to youtube API to list the captions available for the video
	caption_list_str = os.popen("python captions.py --videoid=\'" + video_id + "\' --action=\'list\'").read()

	#Retrieve the English captions
	caption_vec = caption_list_str.split('\n')
	caption_vec = [x for x in caption_vec if 'in \'' + caption_source_lang + '\' language' in x and '(_' not in x]

	if(len(caption_vec) == 0):
		print ('Error: No manual english subtitles available.')
		return -1
 
	#Get the caption id from the retrieved captions
	caption_id = '(' + caption_vec[0].partition('(')[-1].rpartition(')')[0] + ')'

	#Call youtube API to download the caption with the given id, writing it to a file
	os.system("python captions.py --action=\'download\' --captionid=\'" + caption_id + "\' > " + sub_srt_en)

	#Call unbabel API to translate the subtitle file and write it to another file
	os.system("python unbabel_api.py \'" + sub_srt_en + "\' \'" + caption_source_lang + "\' \'" + caption_target_lang + "\' > " + sub_srt_pt)

	#Call youtube API to upload the file with the translated subtitles
	os.system("python captions.py --action=\'upload\' --videoid=\'" + video_id + "\' --language=\'" + caption_target_lang + "\' --file=" + sub_srt_pt)


main()
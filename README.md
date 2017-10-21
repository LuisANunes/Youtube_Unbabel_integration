# Youtube & Unbabel API Integration

# Functionality: 
Retrieves the English subtitles from a Youtube video, translates it to Portuguese and uploads it.
This demonstration shows that its possible to integrate both API's and that when subtitles are uploaded (by content creators or fans) in any language, its possible to translate it to every language, eliminating the need for constant subtitle creation and submission.

# Usage: 
python youtube_unbabel.py <youtube_link>

<youtube_link> = https://www.youtube.com/watch?v=-gGTL-D0uQs (for example)

# Files:

youtube_unbabel.py -> Executes both API's in respective order, parsing and executing functionality.

captions.py -> Youtube API for captions

unbabel_api.py -> Unbabel API for translation

# Additional Info:
1) We are using .srt files
2) Since its a small demonstration, the integration is searching for english subtitles manually introduced (the automatically translated are error prone) and translating it to portuguese. 
3) Test video: https://www.youtube.com/watch?v=-gGTL-D0uQs
4) When the subtitles are uploaded, they are added as drafts and need to be accepted by the account's owner on the creator studio on Youtube.


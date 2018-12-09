import datetime
now = datetime.datetime.now()

from gmail import GMail, Message

html_content = '''
<p>Ch&agrave;o sếp,</p>
<p>S&aacute;ng nay thức dậy, em thấy m&igrave;nh mệt mỏi, người đau quằn quại. B&aacute;c sĩ bảo em bị <strong>vi&ecirc;m ruột thừa cấp t&iacute;nh</strong>.</p>
<p>Sếp cho em nghỉ ốm 30 ng&agrave;y nh&eacute;&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /></p>
<p>Nh&acirc;n vi&ecirc;n.</p>
'''

gmail = GMail('Van<gaukeo418@gmail.com>','khoailang')
msg = Message('Đơn xin nghỉ ốm', to='Boss<vanb1192@gmail.com>', html=html_content)

if now.hour > 7:
    gmail.send(msg)
else:
    print("It's not yet 7AM")
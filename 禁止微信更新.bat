title 一键禁止PC微信自动升级v2.0
reg add "HKEY_CURRENT_USER\Software\Tencent\WeChat" /v "NeedUpdateType" /t reg_dword /d "0" /f >nul 2>nul 
echo 步骤1完成。

del /f /q %USERPROFILE%\AppData\Roaming\Tencent\WeChat\"All Users"\config\update.data >nul 2>nul 
md %USERPROFILE%\AppData\Roaming\Tencent\WeChat\"All Users"\config\update.data >nul 2>nul 
echo Y|cacls "%USERPROFILE%\AppData\Roaming\Tencent\WeChat\All Users\config\update.data" /T /P %USERNAME%:N >nul 2>nul 
echo 步骤2完成。 

rd /s /q %USERPROFILE%\AppData\Roaming\Tencent\WeChat\patch >nul 2>nul 
md %USERPROFILE%\AppData\Roaming\Tencent\WeChat\patch >nul 2>nul 
echo Y|cacls %USERPROFILE%\AppData\Roaming\Tencent\WeChat\patch /T /P %USERNAME%:N >nul 2>nul 
echo 步骤3完成。 

echo 设置完成，正在自动退出。 
timeout /nobreak /t 2 >nul 2>nul exit

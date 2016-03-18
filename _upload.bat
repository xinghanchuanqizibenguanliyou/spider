@echo off
python $$encrypt.py
cd EncryptedFiles
git init
git add --all **
git commit -m "auto commit"
git remote add origin https://github.com/AdaJass/EncryptedFiles.git
git push -u origin master
pause
 
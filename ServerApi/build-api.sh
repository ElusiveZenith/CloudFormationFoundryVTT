poetry export -f requirements.txt > requirements.txt --without-hashes
pip install -t ./package -r requirements.txt

7z d ServerApi.zip
cd package
7z a -r ../ServerApi.zip .
cd ../src
7z a -r ../ServerApi.zip .
cd ..

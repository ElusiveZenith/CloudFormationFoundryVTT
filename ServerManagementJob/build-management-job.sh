poetry export -f requirements.txt > requirements.txt --without-hashes
pip install -t ./package -r requirements.txt

7z d ServerManagementJob.zip
cd package
7z a -r ../ServerManagementJob.zip .
cd ../src
7z a -r ../ServerManagementJob.zip .
cd ..

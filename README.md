# LibraryManager

This is a simple library management system developed in Django. 

The admin user name and passwords are:\
username: admin \
password: pass1234

The normal user user name and passwords are:\
username: username \
password: password

Only the admin can add, remove and edit the books.\
Normal users can sign up and login and when logged in can borrow or return books.


I hope you enjoy. 


run docker:
docker run -d --name library-manger --restart always --net host -v /home/kharmagas/SourceCode/Github/db.sqlite3:/home/library/db.sqlite3 -v /mnt/storage/library/media:/home/library/media library-manager

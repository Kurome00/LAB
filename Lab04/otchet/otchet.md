1. echo sasha
2. pwd > 2.txt 
whoami >> 2.txt
3. ls -la > otchet/files/3.txt
4. touch 4.txt 
code 4.txt
fgdsdfsdfsdf
touch 4.md
cat 4.txt >> 4.md
5. chmod o-r 4.txt
6. chmod 755 4.md
7. mv 4.txt ~/otchet/files 
mv 4.md ~/otchet/files 
8. sudo chown -c root ~/otchet/files/4.md
9. sudo useradd  -mg wheel -s /bin/zsh test_user
10. sudo passwd test_user (11111111)
11. sudo usermod -aG wheel test_user
12. cat /etc/passwd > ~/otchet/files/12.txt
13. chmod a+w ~/otchet/files/12.txt
14. su -P test_user
15. skip
16. gotovo
15. whoami >> /home/sasha/otchet/files/12.txt
18. exit 
19. tail -n 2  ~/otchet/files/12.txt
20. sudo userdel -r test_user
21. find . -maxdepth 2 -type d -empty > ~/otchet/files/21.txt 
22. sudo find / -maxdepth 3 -user root -name "dev*" >  ~/otchet/files/22.txt
23. mkdir -p test_find/permissions test_find/time
24. touch -a -t 202401010000 ~/test_find/time/one.txt
touch -m -t 202410140000 ~/test_find/time/two.txt
 
25. touch ~/test_find/permissions/cant_write.txt ~/test_find/permissions/can_execute.txt
chmod a-w ~/test_find/permissions/cant_write.txt 
chmod a+x ~/test_find/permissions/can_execute.txt 
26. find ~/test_find -atime +183 -delete 
27. find ~/test_find -empty -type f -perm 755 -exec chmod a-x {} \;
28. man ls > man_ls.txt
29. grep -n '^$' man_ls.txt
30. g
rep '[0-9]' ~/man_ls.txt
31. grep "Richard M. Stallman" ~/man_ls.txt > ~/otchet/files/31.txt
32.wc -lc ~/man_ls.txt 
33.pc -u sasha > ~/otchet/files/33.txt
34. pgrep nano
35. pkill nano

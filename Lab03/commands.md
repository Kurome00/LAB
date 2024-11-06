2. tree -L 2
3. cd /etc/
4. ls -a
5. cd /
ls -l -x
6. cd ~
mkdir structure
7. cd structure
mkdir -p {2023..2018}/files
mkdir -p {2023..2018}/pictures
mkdir -p {2023..2018}/.passwords
8. touch {2018..2023}/files/data.md
9. touch {2018..2023}/pictures/picture.png
10. touch {2018..2023}/.passwords/.passwords.txt
11. touch -ad '20240101' {2018..2023}/files/data.md
12 cd 2018
cd .passwords
touch -md '20181006' .passwords.txt
cd ..
cd ..
touch -md 20181006 2018/.passwords/.passwords.txt
touch -md 20191006 2019/.passwords/.passwords.txt
touch -md 20201006 2020/.passwords/.passwords.txt
touch -md 20211006 2021/.passwords/.passwords.txt
touch -md 20221006 2022/.passwords/.passwords.txt
touch -md 20231006 2023/.passwords/.passwords.txt
13. cp -r structure/2023 ~/Downloads/2025
14. cd ~/Downloads
touch -md 20251006 2025/.passwords/.passwords.txt
15. cp -r ~/Downloads/2025 ~/structure
cd ..
cd Structure
16. mv 2025 2024
17. mv /home/sasha/structure/2024/pictures/picture.png /home/sasha/structure/2024/pictures/image.png
mv /home/sasha/structure/2023/pictures/picture.png /home/sasha/structure/2023/pictures/image.png
mv /home/sasha/structure/2022/pictures/picture.png /home/sasha/structure/2022/pictures/image.png
mv /home/sasha/structure/2021/pictures/picture.png /home/sasha/structure/2021/pictures/image.png
mv /home/sasha/structure/2020/pictures/picture.png /home/sasha/structure/2020/pictures/image.png
mv /home/sasha/structure/2019/pictures/picture.png /home/sasha/structure/2019/pictures/image.png
mv /home/sasha/structure/2018/pictures/picture.png /home/sasha/structure/2018/pictures/image.png
18. mv /home/sasha/structure/2018 ~/Documents
mv /home/sasha/structure/2024 ~/Documents
19. rmdir /home/sasha/Documents/2024~
20.rm -r ~/Documents/2024
21.cat > ~/structure/2019/files/data.md
ewrwer
kjfdmklgjfgd
kl;fdklg;fklo;k%      
22. nano ~/structure/2020/files/data.md
23. code ~/structure/2021/files/data.md
24. cat ~/structure/2020/files/data.md >> ~/structure/2022/files/data.md
25. cd structure 
mkdir soft_links hard_links
26. cd soft_links
ln -s ~/structure/2019 2019
ln -s ~/structure/2020 2020
ln -s ~/structure/2021 2021
ln -s ~/structure/2022 2022
ln -s ~/structure/2023 2023
27. cd ..
cd hard_links
ln ~/structure/2020/files/data.md hardlink1
ln ~/structure/2021/.passwords/.passwords.txt hardlink2
28. cd ..
mkdir archives
30. mv home/sasha/structure/Downloads/image.jpg home/sasha/structure/archives
31. tar -cf image.tar home/sasha/structure/archives/image.png
 tar -cjf image.tar.bz2 home/sasha/structure/archives/image.png
 tar -czf image.tgz home/sasha/structure/archives/image.png
 32. zip -er structure.zip structure/

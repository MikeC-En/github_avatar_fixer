import os
import socket


github_ip = socket.getaddrinfo('github.com', 'https')[0][-1][0]
gist_github_ip = socket.getaddrinfo('gist.github.com', 'https')[0][-1][0]
avatar_ip = socket.getaddrinfo('avatars0.githubusercontent.com', 'https')[0][-1][0]

user_content_enum = ['raw', 'gist', 'cloud', 'camo', 'avatars0', 'avatars1',
    'avatars2', 'avatars3', 'avatars4', 'avatars5', 'avatars6', 'avatars7', 'avatars8']


with open('avatar_conf.txt', 'w+') as file:

    file.write('# GitHub Start\n')
    file.write(f'{github_ip} github.com\n')
    file.write(f'{gist_github_ip} gist.github.com\n')
    file.write(f'{avatar_ip} raw.githubusercontent.com\n')

    for item in user_content_enum:
        file.write(f'{avatar_ip} {item}.githubusercontent.com\n')

    file.write("# GitHub End")

print("Create file success!")
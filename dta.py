#!/usr/bin/env python3
#ver 7.1.0
#27-12-23

black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[1;37;40m"
nc="\033[00m"
version = str("7.1.0")
getdata = 0
con_inf = f'{bgreen}[{bpurple}!{bgreen}] {white}'
con_pls = f'{bgreen}[{bpurple}+{bgreen}] {white}'
con= f'{bblue}$ {bblue}Scriptbox{purple}@{bgreen}'+f'[{bcyan}'+version+f'{bgreen}]{purple}~{white} '
go = f"""

{green}                              $$\            $$\     $$\                      {blue}       $$$$$$\  $$$$$$$\  {green}
                              \__|           $$ |    $$ |                           {blue}$$  __$$\ $$  ____| {green}
 $$$$$$$\  $$$$$$$\  $$$$$$\  $$\  $$$$$$\ $$$$$$\   $$$$$$$\   $$$$$$\  $$\   $$\  {blue}$$ /  $$ |$$ |      {green}
$$  _____|$$  _____|$$  __$$\ $$ |$$  __$$\\_$$  _|   $$  __$$\ $$  __$$\ \$$\ $$  |{blue} \$$$$$$$ |$$$$$$$\  {green}
\$$$$$$\  $$ /      $$ |  \__|$$ |$$ /  $$ | $$ |    $$ |  $$ |$$ /  $$ | \$$$$  /   {blue}\____$$ |\_____$$\ {green}
 \____$$\ $$ |      $$ |      $$ |$$ |  $$ | $$ |$$\ $$ |  $$ |$$ |  $$ | $$  $$<   {blue}$$\   $$ |$$\   $$ |{green}
$$$$$$$  |\$$$$$$$\ $$ |      $$ |$$$$$$$  | \$$$$  |$$$$$$$  |\$$$$$$  |$$  /\$$\  {blue}\$$$$$$  |\$$$$$$  |{green}
\_______/  \_______|\__|      \__|$$  ____/   \____/ \_______/  \______/ \__/  \__|  {blue}\______/  \______/ {green}
                                  $$ |                                                                       
                                  $$ |                                                                       
                                  \__|                                        {yellow}[{blue}v{version[:3]}{yellow}]                 
{yellow}                                                                              {cyan}[{blue}\x42\x79 {green}\x44\x69\x76\x79\x61\x6E\x73\x68{cyan}]
{white}                                                                              [Stable]


"""
def numbering(num):
  return green + "[" + white + str(num) + green + "]"+ white
lts  = f"""
{numbering(1)}zphisher    {numbering(2)}truecallerjs 
"""

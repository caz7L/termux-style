B
    `¼\,  ã               @   sì   d dl Z d dlZd dlZd dlmZ d dlmZ g adZ	dZ
dZdZdZd	Zd ad
Zdd Zdd Zdd Zdd Zdd Zdd Zdd Zdd Zdd Zdd Zdd  Zd!d" Zd#d$ Zye  ee
 e  W n   e  Y nX dS )%é    N)Úchoice)Údatetime)ÚfontÚcolorZ	fontcolorÚ	colornameÚclsÚhelpÚaboutÚexitztermux-stylez$HOME/.termux/fontsz$HOME/.termux/colors)z[1;31mz[1;32mz[1;33mz[1;34mz[1;35mz[1;36mz[0;1mz\nz    c               C   s   t d t d¡ d S )Nzf





































































































Úclear)ÚprintÚosÚsystem© r   r   ú//data/data/com.termux/files/home/Termux/main.pyr      s    r   c               C   s"   t  d¡ t  tt t  d S )Nztermux-reload-settings)r   r   r   ÚheadÚnameÚcmdr   r   r   r   Úwait   s    
r   c             C   s   t  d|  d| d¡ d S )Nzls ú>z.txt)r   r   )ZlokÚnamar   r   r   Úls   s    r   c             C   s   t  dtt d|  ¡ d S )Nzecho -e -n "z" && cowsay -f skeleton.cow )r   r   ÚcÚw)r   r   r   r   r      s    r   c             C   s&   t |  dd}| |¡ | ¡  d S )Nz.txtr   )ÚopenÚwriteÚclose)r   ÚtextZbautr   r   r   Úcreate!   s    
r   c             C   s,   t tt d|  dt tt |  d S )NzYour z:
)r   r   r   Úsp)Útitler   r   r   r   r   %   s    r   c            a   C   sì  t td  dtd  dtd  dtd  dtd  dtd  dtd  dtd  dtd  d	td  dtd  d
td  dtd  dtd  dtd  dtd  dtd  dtd  dtd  dtd  dtd  dtd  dtd  dtd  dtd  dtd  dtd  dtd  dtd  dtd  dtd  dtd  dtd  dtd  dtd  dtd  dtd  dtd  dtd  dtd  dtd  dtd  dtd  dtd  dtd  dtd  dtd  dtd  d` d S )Né   z+-----------+----------------+
ú|é   zcommand    é   zdescryption     z|
zfont       zchange font     zcolor      zchange color    zfontname   zprint font name zcolorname  zprint color namezcls        zclear screen    zhelp       zprint help      zabout      zabout me        zexit       zexit            z+-----------+----------------+)r   r   r   r   r   r   Úbantu'   s    r%   c               C   sh   t dtt dtt dtt dtt dtt dtt dtt dtt d	tt d
 d S )Nz    u9   ÃÂºÂ°âË`âÂ°ÂºÃ [ About Me ] ÃÂºÂ°âË`âÂ°ÂºÃ
zMail   : mayat5172@gmail.com
zWA     : 62895640466851
z&Github : https://github.com/Mayat2715
z2FB     : https://m.facebook.com/mayat.mayat.58555
z0IG     : https://www.instagram.com/mayat2.7.15/
zversion: 1.5
z**screen shot & send to me if there is bug
z#Keep learning)r   r   r   r   r   r   r   r	   4   s    r	   c          	   C   s®  t | d  td ttd tdd ¡ }ttt d|  d x@|D ]8}t 	t
d|¡}td	7 att tt t d
|  qJW datttt d}t 	t
d||d	  ¡}t dt d| d¡ tdd}| ¡ }ttt d| d x@|D ]8}t 	t
d|¡}td	7 att tt t d
|  qþW datttt d}	t 	t
d||	d	  ¡}
t dt d| d|
 d¡ t d¡ td|
 | ¡  t  d S )Nz-termuxz/Sumber font: https://github.com/powerline/fontsZlistfontzlistfont.txtÚrtzList z
 yang ada:Ú r#   z. r   zPilih mana: zls "ú/z">sementara.txtzsementara.txtzList font dari ú:zcp "z" $HOME/.termux/font.ttfzrm $HOME/.termux/sementara.txtÚfontname)r   r   r   Úfontdirr   Ú	readlinesr   r   ÚreÚsubÚwhoÚayr   ÚintÚinputr   r   r   r   r   )ÚaÚhereÚiÚereÚchoseZthereZayeZeyaZhoyZowhZhasilr   r   r   r   A   s8    

"

"

r   c             C   sì   t | d  td ttd tdd ¡ }ttt d|  d x@|D ]8}t 	t
d|¡}td	7 att tt t d
|  qJW datttt d}t 	t
d||d	  ¡}t dt d| d¡ t d¡ td| t  d S )Nz-termuxz[1mSumber color: Idk sorryZ	listcolorzlistcolor.txtr&   zList z
 yang ada:r'   r#   z. r   zPilih mana: zcp "r(   z!" $HOME/.termux/colors.propertieszrm $HOME/.termux/listcolor.txtr   )r   r   r   Úcolordirr   r,   r   r   r-   r.   r/   r0   r   r1   r2   r   r   r   r   )r3   r4   r5   r6   r7   Zthisr   r   r   r   b   s     

"

r   c          	   C   s0   t | d }t| | ¡  W d Q R X t  d S )Nz.txt)r   r   Úreadr   )r3   Úfr   r   r   r*   w   s    r*   c          	   C   s0   t | d }t| | ¡  W d Q R X t  d S )Nz.txt)r   r   r9   r   )r3   r:   r   r   r   r   ~   s    r   c              C   s  t td  dt ¡ j dt ¡ j dt ¡ j dtd  dtt d} | dkrbt  t	|  n°| d	krzt  t
|  n| d
krt|  n| dkrt|  nt| dkr®t  nd| dkr¾t  nT| dkrÖt  tt n<| dkræt  n,| dkrðn"ttt d|  dtt d t  d S )Né   ú[r)   ú]éÿÿÿÿz
>ú r   r   r*   r   r   r	   r   r
   r'   zTidak ada 'z'
zketik 'help' untuk bantuan)r2   r   ÚdZnowZhourZminuteZsecondr   r   r   r   r*   r   r%   r	   r   r   r
   r   r   )Úmainr   r   r   r      s0    J




"r   )r   Úsysr-   Zrandomr   r   r   r@   ZaswZcommandr   r+   r8   r   r/   r0   r   r   r   r   r   r   r   r%   r	   r   r   r*   r   r   r
   r   r   r   r   Ú<module>   s<   !

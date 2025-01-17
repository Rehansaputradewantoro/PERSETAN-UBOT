""" rams module for other small commands. """
from rams import CMD_HELP, ALIVE_NAME
from rams.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.helpmy$")
async def usit(e):
    await e.edit(
        f"**Hai {DEFAULTUSER} Kalau Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.rhelp` Atau Bisa `.help` atau Minta Bantuan Ke:\n"
        "\n[LANDAK🦔](t.me/trvgroup)"
        "\n\n[SUPPORT](https://t.me/ZoneDangerzsex)"
        "\n\n[CHANNEL](https://t.me/Revanstoreya)")


@register(outgoing=True, pattern="^.rvars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://t.me/Revanstoreya/varshelper.txt)")


CMD_HELP.update({
    "ramhelper":
    "`.helpmy`\
\nPenjelasan: Bantuan Untuk Revans-Userbot.\
\n`.rvars`\
\nPenjelasan: Untuk Melihat Beberapa Daftar Vars."
})

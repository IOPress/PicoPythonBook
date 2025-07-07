from rp2 import Flash
import os
flash=Flash()
os.umount('/')
os.VfsLfs2.mkfs(flash)
os.mount(flash, '/')
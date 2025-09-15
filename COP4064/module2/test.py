import pickledb, sys
print("[pickledb] using:", getattr(pickledb, "__file__", "<no __file__>"))
print("[pickledb] has load():", hasattr(pickledb, "load"))
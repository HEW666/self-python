# 方法1
# import mod.mode1
# import mod.mode2
# mod.mode1.in_print()
# mod.mode2.in_print()

# 方法2
from mod.mode1 import in_print
from mod.mode2 import in_print as he
# 同名的功能，如果都被导入，那么后导入的会覆盖先导入的
in_print()
he()

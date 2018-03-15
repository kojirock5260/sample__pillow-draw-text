import sys
from app import App
from compositor.text_compositor import TextCompositor

STRING_DATA = sys.argv[1]
app_logic   = App()
app_logic.addCompositor(TextCompositor(STRING_DATA, 30, 350, 20, False))
app_logic.addCompositor(TextCompositor(STRING_DATA, 60, 200, 20, False))
app_logic.addCompositor(TextCompositor(STRING_DATA, 80, 60, 20, True, "#FF0000"))
app_logic.run();

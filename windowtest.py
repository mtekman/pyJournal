# program = testcurses
import curses
stdscr = curses.initscr()

window = stdscr.subwin(22,30,0,0)
window.box()
window.refresh()
window.addstr(2,10, "This is my line of text")
window.addstr(4,20,"What happened? ")
window.refresh()

curses.napms(1000)
#mystr = chr(window.inch(2,12))
#mystr += chr(window.inch(2,13))
mystr = window.instr(2,12,6)
#window.addstr (8,1, "Str data should be here: ")
#window.addstr (8,20,mystr)
window.refresh()

curses.endwin()
print mystr
